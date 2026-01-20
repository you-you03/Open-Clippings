以下は **B（GitHub APIで `02_Clippings` を取得して `index.json` を生成。git checkout は検索対象を一切展開しない）**方式の、**実行手順書（そのまま作業できるレベル）**です。
前提：`02_Clippings` は **リポジトリ直下**、GitHub Pages は **GitHub Actions** でデプロイ設定済み。

---

# 実行手順書（B方式：API取得 → index.json生成 → GitHub Pages配信）

## 0. ゴール（運用イメージ）

* あなたがやること：`02_Clippings` に Markdown を追加/更新 → `git push`
* 自動で起きること（Actions）：

  1. **リポジトリは “必要最小限のみ” sparse-checkout**（`00_System` 等だけ）
  2. GitHub APIで `02_Clippings/**/*.md` を取得して解析
  3. `00_System/assets/index.json` を生成
  4. `dist/` を組み立てて GitHub Pages にデプロイ
* ブラウザ：`assets/index.json` を読み込み、検索UIを提供（静的）

---

## 1. ファイル配置（確定）

リポジトリに以下を置きます（**検索対象の `02_Clippings` は checkout しない**）。

```
00_System/
  package.json
  tools/
    build_index_api.mjs
  site/
    index.html
    app.js
    style.css
  assets/
    (index.json は Actions 生成でもOK)
.github/
  workflows/
    pages.yml
02_Clippings/
  ... (既存のMarkdown群)
```

---

## 2. `00_System/package.json` を準備

既に存在していても構いませんが、最低限以下の内容にしてください（`type: module` 前提）。

```json
{
  "name": "clippings-search",
  "private": true,
  "type": "module",
  "scripts": {
    "build": "node tools/build_index_api.mjs"
  },
  "dependencies": {
    "gray-matter": "^4.0.3"
  }
}
```

---

## 3. `00_System/tools/build_index_api.mjs` を新規作成

以下をそのまま作成してください（**GitHub APIで `02_Clippings` を列挙→内容取得→index.json生成**）。

````js
// 00_System/tools/build_index_api.mjs
import fs from "node:fs";
import path from "node:path";
import matter from "gray-matter";

const REPO = process.env.GITHUB_REPOSITORY; // "owner/repo"
const TOKEN = process.env.GITHUB_TOKEN;
const REF = process.env.GITHUB_REF_NAME || "main"; // ブランチ名
const CLIPPINGS_PREFIX = "02_Clippings/";
const OUT_PATH = path.resolve("assets/index.json");

const EXCERPT_LEN = 180;
const CONCURRENCY = 8;
const RETRY = 3;

if (!REPO) throw new Error("Missing env: GITHUB_REPOSITORY");
if (!TOKEN) throw new Error("Missing env: GITHUB_TOKEN");

const [owner, repo] = REPO.split("/");

const gh = async (url) => {
  const res = await fetch(url, {
    headers: {
      Authorization: `Bearer ${TOKEN}`,
      "X-GitHub-Api-Version": "2022-11-28",
      Accept: "application/vnd.github+json"
    }
  });
  if (!res.ok) {
    const txt = await res.text().catch(() => "");
    throw new Error(`GitHub API error ${res.status}: ${url}\n${txt}`);
  }
  return res.json();
};

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const withRetry = async (fn, n = RETRY) => {
  let last;
  for (let i = 0; i < n; i++) {
    try {
      return await fn();
    } catch (e) {
      last = e;
      // 503/502等の一時系を想定してバックオフ
      await sleep(400 * Math.pow(2, i));
    }
  }
  throw last;
};

const normalizeTags = (tagsVal) => {
  if (!tagsVal) return [];
  if (Array.isArray(tagsVal)) {
    return tagsVal.map(String).map((s) => s.trim()).filter(Boolean);
  }
  const s = String(tagsVal).trim();
  if (!s) return [];
  // カンマ/空白の双方を許容
  return s
    .split(/[,，\s]+/g)
    .map((x) => x.trim())
    .filter(Boolean);
};

const mdToText = (md) => {
  let t = md;

  // front matter は gray-matter で除去済み想定だが保険
  t = t.replace(/^---[\s\S]*?---\s*/m, "");

  // code fences
  t = t.replace(/```[\s\S]*?```/g, " ");

  // inline code
  t = t.replace(/`[^`]*`/g, " ");

  // images/links: [text](url) -> text
  t = t.replace(/!\[([^\]]*)\]\([^)]+\)/g, "$1");
  t = t.replace(/\[([^\]]+)\]\([^)]+\)/g, "$1");

  // headings/bold/italic/quotes/list markers
  t = t.replace(/^[>#*\-+]+\s+/gm, "");
  t = t.replace(/[*_~]/g, "");

  // collapse spaces
  t = t.replace(/\s+/g, " ").trim();
  return t;
};

const getDefaultBranchSha = async () => {
  const repoInfo = await gh(`https://api.github.com/repos/${owner}/${repo}`);
  const defaultBranch = repoInfo.default_branch;
  const refInfo = await gh(`https://api.github.com/repos/${owner}/${repo}/git/refs/heads/${REF || defaultBranch}`);
  return { sha: refInfo.object.sha, branch: REF || defaultBranch };
};

const listClippingsMarkdownPaths = async (commitSha) => {
  // Tree API: recursive=1 で全体列挙（750件規模なら現実的）
  const tree = await gh(
    `https://api.github.com/repos/${owner}/${repo}/git/trees/${commitSha}?recursive=1`
  );

  if (!tree.tree) throw new Error("Unexpected tree response");

  return tree.tree
    .filter((x) => x.type === "blob")
    .map((x) => x.path)
    .filter((p) => p.startsWith(CLIPPINGS_PREFIX))
    .filter((p) => p.toLowerCase().endsWith(".md"));
};

const fetchFileContent = async (filePath, branch) => {
  // Contents API: base64
  const j = await gh(
    `https://api.github.com/repos/${owner}/${repo}/contents/${encodeURIComponent(filePath)}?ref=${encodeURIComponent(branch)}`
  );
  if (!j.content) throw new Error(`No content in response: ${filePath}`);
  const buf = Buffer.from(j.content.replace(/\n/g, ""), "base64");
  return buf.toString("utf-8");
};

const runPool = async (items, worker, concurrency = CONCURRENCY) => {
  const results = new Array(items.length);
  let idx = 0;

  const runners = Array.from({ length: concurrency }, async () => {
    while (true) {
      const i = idx++;
      if (i >= items.length) break;
      results[i] = await worker(items[i], i);
    }
  });

  await Promise.all(runners);
  return results;
};

(async () => {
  const started = new Date();
  const { sha, branch } = await getDefaultBranchSha();

  const paths = await listClippingsMarkdownPaths(sha);

  // 各mdを取得→解析
  const items = await runPool(
    paths,
    async (p) => {
      const raw = await withRetry(() => fetchFileContent(p, branch));
      const parsed = matter(raw);

      const fm = parsed.data || {};
      const title =
        (fm.title && String(fm.title).trim()) ||
        path.basename(p, path.extname(p));

      const tags = normalizeTags(fm.tags);
      const added = fm.added ? String(fm.added).trim() : "";
      const author = fm.author ? String(fm.author).trim() : "";

      const bodyText = mdToText(parsed.content || "");
      const excerpt = bodyText.slice(0, EXCERPT_LEN);

      const folder = path.dirname(p);

      const searchText = [
        title,
        author,
        folder,
        tags.join(" "),
        bodyText
      ]
        .filter(Boolean)
        .join(" ");

      return {
        id: p,
        path: p,
        title,
        tags,
        added,
        author,
        folder,
        excerpt,
        searchText
      };
    },
    CONCURRENCY
  );

  // 出力ディレクトリ作成
  fs.mkdirSync(path.dirname(OUT_PATH), { recursive: true });

  const out = {
    generatedAt: started.toISOString(),
    count: items.length,
    items
  };

  fs.writeFileSync(OUT_PATH, JSON.stringify(out), "utf-8");

  // ログ
  console.log(`Generated: ${OUT_PATH}`);
  console.log(`Count: ${items.length}`);
})();
````

---

## 4. `.github/workflows/pages.yml` を B方式に差し替え

重要：**checkout は sparse-checkout で 00_System と .github だけ**にします。
これにより、Windowsで問題になる `"` 含むファイル名も、Linuxの長さ問題も、**checkoutで踏みません**。

```yaml
name: Deploy Pages

on:
  push:
    branches: ["main"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: true

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout (sparse)
        uses: actions/checkout@v4
        with:
          fetch-depth: 1
          sparse-checkout: |
            00_System
            .github
          sparse-checkout-cone-mode: false

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: "20"

      - name: Install deps
        run: |
          cd 00_System
          npm ci

      - name: Build index.json via GitHub API
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          cd 00_System
          npm run build

      - name: Prepare dist
        run: |
          rm -rf dist
          mkdir -p dist
          cp -r 00_System/site/* dist/
          mkdir -p dist/assets
          cp 00_System/assets/index.json dist/assets/index.json

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: dist

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    steps:
      - name: Deploy
        id: deployment
        uses: actions/deploy-pages@v4
```

---

## 5. サイト側（`00_System/site/app.js`）の読み込み先

ブラウザ側は `./assets/index.json` を fetch するだけでOKです。
（既に実装済みなら変更不要。未実装なら、このパスで統一してください。）

* `fetch("./assets/index.json")`

---

## 6. 実行手順（あなたの作業）

### 6.1 初回導入（1回だけ）

1. 上記ファイルを追加/差し替え

* `00_System/package.json`
* `00_System/tools/build_index_api.mjs`
* `.github/workflows/pages.yml`

2. commit & push

```bash
git add .
git commit -m "Switch to API-based indexing for Pages"
git push origin main
```

3. GitHub → Actions を確認

* `Deploy Pages` が成功（緑）になれば完了

### 6.2 以降の運用（毎回）

* `02_Clippings` に Markdown を追加/修正して push するだけ
* Actions が index.json を自動更新し、Pagesに反映

---

## 7. 動作確認チェックリスト（失敗時の切り分けが速い）

1. Actions の `Checkout (sparse)` が成功している

   * 失敗する場合：sparse-checkout のパス指定がズレ（`00_System` が直下に無い等）
2. `Build index.json via GitHub API` が成功している

   * 失敗する場合：API制限/トークン/権限/パス問題
3. `dist/assets/index.json` が存在する
4. Pages URL で検索画面が表示される
5. 画面で件数が 750 前後になっている

---

## 8. この方式で「禁止文字」と「長すぎるパス」が解決する理由

* Git checkout で `02_Clippings` を一切展開しない（sparse-checkout）
* ファイル内容は GitHub API から取得し、ローカルのファイル名として保存しない
  → OS依存のファイル名制約を踏まない

---

必要であれば、次に「`app.js`（ShadcnライクUI、タグAND、自由語全文検索、ソート、カード表示）」の確定版も提示します。現時点の最優先は **上記の導入手順で Actions をグリーンにすること**です。

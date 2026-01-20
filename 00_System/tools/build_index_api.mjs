// 00_System/tools/build_index_api.mjs
import fs from "node:fs";
import path from "node:path";
import matter from "gray-matter";

const REPO = process.env.GITHUB_REPOSITORY; // "owner/repo"
const TOKEN = process.env.GITHUB_TOKEN;
const REF = process.env.GITHUB_REF_NAME || "main"; // ブランチ名
const CLIPPINGS_PREFIX = "02_Clippings/";
const OUT_PATH = path.resolve("assets/index.json");

const EXCLUDE_BASENAMES = new Set([
  "folder_index.md",
  "from_raindrop.md"
]);

const EXCLUDE_PATH_CONTAINS = [
  "/0_Index/folder_index",
  "/0_Index/from_raindrop",
  "/0_Index/folder_index.md",
  "/0_Index/from_raindrop.md"
];

const EXCERPT_LEN = 180;
const CONCURRENCY = 3; // レート制限対策: 並列数を減らす
const RETRY = 5; // リトライ回数を増やす
const RATE_LIMIT_RETRY_DELAY = 60000; // レート制限時の待機時間（60秒）

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
  
  // レート制限情報をログ出力
  const rateLimitRemaining = res.headers.get("x-ratelimit-remaining");
  const rateLimitReset = res.headers.get("x-ratelimit-reset");
  if (rateLimitRemaining !== null) {
    console.log(`Rate limit: ${rateLimitRemaining} remaining`);
  }
  
  if (!res.ok) {
    const txt = await res.text().catch(() => "");
    const error = new Error(`GitHub API error ${res.status}: ${url}\n${txt}`);
    error.status = res.status;
    error.responseText = txt;
    error.rateLimitRemaining = rateLimitRemaining;
    error.rateLimitReset = rateLimitReset;
    throw error;
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
      
      // レート制限エラー（403）の場合は長い待機時間
      if (e.status === 403 && e.responseText && e.responseText.includes("rate limit")) {
        let waitTime = RATE_LIMIT_RETRY_DELAY;
        
        // レート制限リセット時間が分かっている場合は、その時間まで待機
        if (e.rateLimitReset) {
          const resetTime = parseInt(e.rateLimitReset, 10) * 1000; // 秒をミリ秒に変換
          const now = Date.now();
          const timeUntilReset = resetTime - now;
          
          if (timeUntilReset > 0 && timeUntilReset < 3600000) { // 1時間以内の場合のみ
            waitTime = timeUntilReset + 5000; // 5秒のマージンを追加
            console.warn(`⚠️  Rate limit exceeded. Waiting until reset time (${new Date(resetTime).toISOString()})...`);
          } else {
            console.warn(`⚠️  Rate limit exceeded. Waiting ${waitTime / 1000}s before retry ${i + 1}/${n}...`);
          }
        } else {
          console.warn(`⚠️  Rate limit exceeded. Waiting ${waitTime / 1000}s before retry ${i + 1}/${n}...`);
        }
        
        await sleep(waitTime);
        continue;
      }
      
      // 503/502等の一時系を想定してバックオフ
      const backoff = 400 * Math.pow(2, i);
      console.warn(`⚠️  Retry ${i + 1}/${n} after ${backoff}ms...`);
      await sleep(backoff);
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
    .filter((p) => p.toLowerCase().endsWith(".md"))
    .filter((p) => {
      const base = path.basename(p).toLowerCase();
      if (EXCLUDE_BASENAMES.has(base)) return false;

      const norm = p.replaceAll("\\", "/"); // 念のため
      return !EXCLUDE_PATH_CONTAINS.some((frag) => norm.includes(frag));
    });
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
      
      // レート制限対策: 各リクエストの間に短い待機時間を追加
      if (i > 0 && i % 10 === 0) {
        await sleep(1000); // 10件ごとに1秒待機
      }
      
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
      let parsed;
      try {
        parsed = matter(raw);
      } catch (e) {
        console.warn(`⚠️  Front matter parse failed: ${p}`);
        parsed = {
          data: {},
          content: raw
        };
      }

      const fm = parsed.data || {};
      const title =
        (fm.title && String(fm.title).trim()) ||
        path.basename(p, path.extname(p));

      const url =
        (fm.source && String(fm.source).trim()) ||
        (fm.url && String(fm.url).trim()) ||
        (fm.link && String(fm.link).trim()) ||
        "";

      let tags = [];
      try {
        tags = normalizeTags(fm.tags);
      } catch {
        tags = [];
      }
      const created =
        (fm.created && String(fm.created).trim()) ||
        (fm.published && String(fm.published).trim()) ||
        "";
      const added = created;
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
        url,
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
    repo: { owner, repo, branch },
    items
  };

  fs.writeFileSync(OUT_PATH, JSON.stringify(out), "utf-8");

  // ログ
  console.log(`Generated: ${OUT_PATH}`);
  console.log(`Count: ${items.length}`);
})();


以下、**4点を一括で潰す指示書**として書き直します（Shadcn風の見た目／オレンジマーカー／YAMLのURL対応／`folder_index` と `from_raindrop` の除外）。

---

# 改善指示書（確定版）

## A. `folder_index` と `from_raindrop` が出続ける件（原因と修正）

### 原因（ほぼ確定）

* **除外ロジックを `build_index_api.mjs` に入れていない**、または
* 入れているが **index.json が更新されていない**（Actionsが走ってない or 生成物が差し替わっていない）、
* もしくは **ファイル名が `folder_index.md` / `from_raindrop.md` ではない**（例：`folder_index` の拡張子違い・大文字小文字・`from_raindrop (1).md` 等）

### 修正（確実に効く方法：basename一致＋パス部分一致の二重フィルタ）

`00_System/tools/build_index_api.mjs` に以下を入れてください。

#### 1) 定数追加（上部、`import` の直後あたり）

```js
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
```

#### 2) `listClippingsMarkdownPaths` の返却フィルタを差し替え

```js
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
```

#### 3) 反映手順

* 修正 → commit → push
* Actions の `Build index.json via GitHub API` が **成功していること**
* ブラウザで **index.json を直で開いて** `folder_index` が含まれないことを確認

  * `https://<pages>/assets/index.json` を開いて検索

---

## B. YAMLフロントマターから `url`（または `source`）を取り出して Open に使う

あなたの例だと `source:` が入っています。一般化して `url` / `source` / `link` を許容します。

### `build_index_api.mjs` の item 生成部分に追加

`fm` を取った直後に入れてください。

```js
const url =
  (fm.url && String(fm.url).trim()) ||
  (fm.source && String(fm.source).trim()) ||
  (fm.link && String(fm.link).trim()) ||
  "";
```

そして return に `url` を追加：

```js
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
```

### UI側（`app.js`）

Open ボタンのリンク先を以下の優先順にします。

1. `item.url`（外部URL）
2. 無ければ GitHub の該当Markdown（従来どおり）

---

## C. ハイライトを「オレンジのマーカー」にする（Shadcn風）

### 方針

`<mark>` を「蛍光ペン」っぽくするには、

* 背景：薄いオレンジ
* 角丸：少し
* 下線/影：不要
* 文字色：黒のまま（反転しない）

### `style.css`

```css
mark {
  background: #ffb020;      /* オレンジ */
  color: #000;
  padding: 0 2px;
  border-radius: 2px;
}
```

※より“マーカー感”を出すなら、少し透明にする：

```css
mark { background: rgba(255, 176, 32, 0.55); }
```

---

## D. Shadcn UI “っぽい”見た目に寄せる指示の出し方（実装方針と具体指示）

いまのUIは「白黒で堅い」方向に寄っています。Shadcnっぽくするなら、要点は以下です。

### 目標スタイル（Shadcnの核）

* ベース：**白背景 + 薄い境界線**（`border: 1px solid #e5e7eb` 相当）
* 角丸：**やや大きめ（10〜12px）**
* 影：**ごく薄い**（カードの浮き）
* タイポ：**system sans**（Inter / Noto Sans JP）
* ボタン：**塗りつぶし黒** or **アウトライン**の2種
* レイアウト：余白を増やし、情報は詰め過ぎないが「視線の流れ」を作る

### あなたの要件（白黒）との整合

* ベージュ禁止は維持
* ただし **境界線を真っ黒に固定**すると“古い管理画面感”が出るので、Shadcn寄せなら
  **黒100%は文字と主要アクションだけ**に使い、枠線は薄いグレー推奨

### 具体指示（CSSトークン化）

`style.css` の先頭にトークンを追加して、全体をこれに寄せてください。

```css
:root{
  --bg: #ffffff;
  --fg: #0a0a0a;
  --muted: #6b7280;
  --border: #e5e7eb;
  --card: #ffffff;
  --ring: rgba(0,0,0,0.12);
  --radius: 12px;
}
body{
  background: var(--bg);
  color: var(--fg);
  font-family: Inter, "Noto Sans JP", system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
}
.card{
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: 0 1px 2px rgba(0,0,0,0.06);
}
.input, select{
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 10px 12px;
}
.input:focus, select:focus{
  outline: none;
  box-shadow: 0 0 0 3px var(--ring);
}
.button{
  border-radius: 10px;
  border: 1px solid var(--border);
  background: #111;
  color: #fff;
  padding: 10px 12px;
  font-weight: 600;
}
.button.secondary{
  background: #fff;
  color: #111;
}
.tag{
  border: 1px solid var(--border);
  border-radius: 999px;
  padding: 3px 8px;
  font-size: 12px;
  color: #111;
  background: #fff;
}
.meta{
  color: var(--muted);
  font-size: 12px;
}
```

### レイアウト指示（2カラム維持＋視線整理）

* Resultsの上に「ヒット件数」「絞り込み条件」を小さく表示
* Cardsは2カラム、gapは20〜24px
* “Open”ボタンはカード下部に固定（今の形は良い）

---

## まとめ：あなたがCursorへ出すべき指示（短文化）

1. `build_index_api.mjs`：`folder_index` / `from_raindrop` を **basename + path contains** で除外
2. `build_index_api.mjs`：front matter から `url/source/link` を抽出して `item.url` に入れる
3. `app.js`：Openは `item.url` 優先、無ければ GitHubリンク
4. `style.css`：Shadcnトークン化（border薄グレー、角丸12px、薄影、Inter/Noto Sans JP）、`mark` はオレンジマーカー
5. push → Actions成功 → `assets/index.json` に除外が反映されていることを確認

---

必要なら、あなたの `00_System/site/app.js` の現行コード（描画部分）を貼ってください。上記の「Openリンク切替」と「ハイライト適用」を、差分形式で確定させます。

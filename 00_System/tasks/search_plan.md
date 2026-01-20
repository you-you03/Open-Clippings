以下に「仕様定義書」と「実装計画書」を提示します。前提として、資材を **`MyObsidian/00_System/` 配下に集約**する構成で成立するよう、パス設計・ビルド/デプロイ手順・UI要件を整合させています。UIは **Shadcn（shadcn/ui）ライク**なトーン（ミニマル、余白、ボーダー、カード、ピル、タイポの階層）を要件として明文化しています。

---

# 仕様定義書

Clippings Search（GitHub Pages / Markdown DB / YAML Front Matter）

## 1. 目的

GitHubリポジトリ内の Markdown（`MyObsidian/02_Clippings/`）をデータベースとして扱い、GitHub Pages上で **自由語（本文含む）＋タグ絞り込み**により検索・閲覧できる静的Webアプリを提供する。AI検索は使用しない。

## 2. 前提・制約

* ホスティング：GitHub Pages（静的配信）
* データ：GitHubリポジトリ内 Markdownファイル
* タグ等メタデータ：Markdown先頭のYAMLフロントマターから抽出
* 件数規模：現状750件、増加を想定（1,000〜3,000件程度までを目安に同一方式で運用）
* 検索：クライアントサイド（ブラウザ内）で実行
* 日本語：本文に含まれる可能性を前提（分かち書きは初期では導入しない）

## 3. 対象範囲

### 3.1 検索対象

* ディレクトリ：`MyObsidian/02_Clippings/`
* 対象ファイル：`MyObsidian/02_Clippings/**/*.md`

### 3.2 管理・実行資材（集約場所）

* `MyObsidian/00_System/` 配下に以下を配置する。

  * `tools/`（インデックス生成スクリプト）
  * `site/`（UI：HTML/JS/CSS）
  * `assets/`（生成物：`index.json` を格納）
  * `package.json`（依存・ビルド定義）
  * `.github/workflows/`（デプロイワークフロー：リポジトリ直下に必須）

※GitHub Actionsのワークフローは仕様上 `.github/workflows` がリポジトリ直下である必要があるため、`00_System` 配下に完全移設はしない。

## 4. データ仕様（YAMLフロントマター）

### 4.1 想定キー

* `title`（文字列）
* `tags`（配列または文字列）
* `added`（追加日：文字列、推奨 `YYYY-MM-DD`）
* `author`（文字列）

### 4.2 フォールバック規則

* `title` 未設定：ファイル名（拡張子除く）をタイトルに採用
* `tags` 未設定：空配列
* `added` 未設定：空文字（表示は `-`）
* `author` 未設定：空文字（表示は `-`）

### 4.3 `tags` の正規化

* 配列：各要素を文字列化・trim・空を除外
* 文字列：カンマ区切り／空白区切りの双方を許容し分割・trim・空を除外

## 5. インデックス仕様（`index.json`）

### 5.1 出力先

* `MyObsidian/00_System/assets/index.json`

### 5.2 JSON構造

* `generatedAt`：ISO日時
* `count`：件数
* `items[]`：各Markdownのインデックス

### 5.3 itemsフィールド

* `id`：ファイルパス（`MyObsidian/02_Clippings/...`）
* `title`
* `tags[]`
* `added`
* `author`
* `folder`：格納フォルダー（ファイルを除いたパス）
* `excerpt`：冒頭抜粋（本文プレーンテキストの先頭N文字）
* `path`：リンク先（原則 `id` と同一）
* `searchText`：検索対象テキスト（後述）

### 5.4 検索対象テキストの定義（`searchText`）

以下を連結し、FlexSearchに投入する。

* `title`
* `author`
* `folder`
* `tags`（連結文字列）
* `bodyText`（Markdown本文をプレーンテキスト化）

## 6. Markdown本文の取り扱い

### 6.1 プレーンテキスト化の規則

* コードフェンス（```）は除去
* インラインコード（`...`）は除去
* 画像リンク、URLリンクはテキストのみ残す（または除去）
* 見出し記号、強調記号などの記号は除去
* 連続空白は単一空白に正規化

### 6.2 冒頭抜粋（excerpt）

* `bodyText` 先頭から固定長で切り出し
* 既定：180文字（性能と可読性のトレードオフ。運用で調整可能）

## 7. UI/UX仕様（Shadcnライク）

### 7.1 デザイン原則

* ミニマル、余白重視、薄いボーダー、カードベース、角丸（大きめ）
* タイポ階層：見出し > サブ情報 > 本文抜粋
* コンポーネント：Input / Button / Select / Badge(Pill) / Card / Separator
* 状態表現：hover、active、focus ring、disabled（必要箇所）

### 7.2 画面構成

単一ページ（`index.html`）で完結する。

* ヘッダー

  * タイトル
  * メタ情報（件数、インデックス生成日時）
* 検索パネル（Card）

  * 自由語入力（Input）
  * タグフィルタ（Badgeのトグル。複数選択）
  * 並び替え（Select）
  * クリア（Button）
* 結果領域

  * 結果件数
  * 結果リスト（Cardの縦並び）

### 7.3 表示項目（結果カード）

* タイトル（クリック可能）
* タグ（Pillで表示）
* 追加日（`added`）
* 作者（`author`）
* 格納フォルダー（`folder`）
* 冒頭抜粋（`excerpt`）

### 7.4 フィルタリング仕様

* タグ選択はAND条件（選択した全タグを含む記事のみ表示）
* 自由語検索は全文（`searchText`）を対象
* 自由語が空の場合：タグフィルタのみで絞り込み
* クリア：自由語・タグ選択・並び替えを既定へ戻す

### 7.5 並び替え仕様

* `relevance`：関連度（自由語検索時のみFlexSearchの順序を優先）
* `added_desc`：追加日 新しい順（`YYYY-MM-DD` の場合に正しく動作）
* `added_asc`：追加日 古い順
* `title_asc`：タイトル昇順

## 8. リンク仕様（閲覧）

* 初期仕様：`path` をそのまま参照し、Markdownファイルを開く

  * 注意：Pages上ではMarkdownがHTML変換されないため「テキスト表示」になる
* 拡張仕様（将来）：SSG導入（Astro/VitePress等）により Markdown→HTML化し、`path` をHTMLへ向ける

## 9. 非機能要件

### 9.1 性能

* 初回ロード：`index.json` のサイズに依存（750件想定で実用域）
* 体感：入力に追従する即時検索（数百ms以内を目標）
* 上限対策（必要時）：`searchText` を短縮／抜粋長削減／分割ロードの検討

### 9.2 可用性

* 完全静的。GitHub Pagesの提供範囲で可用性を担保

### 9.3 セキュリティ

* 公開リポジトリの場合、`index.json` に本文が含まれる（検索用テキスト）。公開範囲の整理が必須
* 可能な選択肢：

  * PrivateリポジトリではGitHub Pagesを使う運用が制約され得る（組織/プラン設定次第）
  * 公開前提なら、本文は「冒頭のみ」「メタのみ」に縮退する設計も可能

### 9.4 運用性

* `main` へのpushで自動再インデックス→自動デプロイ
* 手動実行（workflow_dispatch）も可能

---

# 実装計画書

Clippings Search（00_System配下集約）

## 1. 実装方針

* インデックス生成：Nodeスクリプト（`gray-matter` + `fast-glob`）
* 検索：FlexSearch（ブラウザ内）
* UI：素のHTML/JS/CSSでShadcnライクに整形（将来的にReact化も可能）
* デプロイ：GitHub Actions → GitHub Pages（Actions方式）

## 2. ディレクトリ設計（確定）

### 2.1 追加・配置

* `MyObsidian/00_System/tools/build_index.mjs`
* `MyObsidian/00_System/site/index.html`
* `MyObsidian/00_System/site/app.js`
* `MyObsidian/00_System/site/style.css`
* `MyObsidian/00_System/assets/index.json`（自動生成）
* `MyObsidian/00_System/package.json`

### 2.2 Actions（直下固定）

* `.github/workflows/pages.yml`（直下）

## 3. パス設計（00_System集約に伴う調整点）

### 3.1 インデックス生成の入出力

* 入力（glob）：`MyObsidian/02_Clippings/**/*.md`
* 出力：`MyObsidian/00_System/assets/index.json`

### 3.2 Pages公開時の配置（dist）

デプロイ時に dist を組み立てる。

* `dist/index.html`（`00_System/site/index.html` をコピー）
* `dist/app.js`（同上）
* `dist/style.css`（同上）
* `dist/assets/index.json`（`00_System/assets/index.json` をコピー）

これにより、ブラウザ側は `./assets/index.json` を相対参照できる。

## 4. 実装タスク分解（WBS）

### Phase 0：準備

* リポジトリに `MyObsidian/00_System/` を作成
* `package.json` 配置
* Node実行前提の合意（ActionsでNode 20）

### Phase 1：インデックス生成

* `build_index.mjs` 実装
* 正規化（tags/added/title）実装
* Markdownプレーンテキスト化（コード除外含む）実装
* `index.json` 出力確認（件数、必須フィールド）

完了条件：

* `node MyObsidian/00_System/tools/build_index.mjs` が成功し、`MyObsidian/00_System/assets/index.json` が生成される
* `count` が想定（約750）と一致する

### Phase 2：検索UI

* `index.html`（Shadcnライクの骨格）実装
* `app.js`（ロード・タグ生成・検索・ソート・描画）実装
* `style.css`（Card/Input/Badge/Focus ring/余白）実装
* 表示項目の要件通りのレンダリング確認

完了条件：

* ローカル簡易サーバで検索が動作
* タグAND、自由語検索、ソートが仕様通り

### Phase 3：GitHub Actions / Pages

* `.github/workflows/pages.yml` 実装
* `npm ci` → build → dist構築 → upload → deploy が成功することを確認
* GitHub Pages設定（Actionsデプロイ）反映

完了条件：

* `main` pushで Pages URL に反映
* Pages上で `index.json` 取得、検索動作が確認できる

### Phase 4：品質・運用整備

* README（運用手順・front matter推奨）作成
* 例外系（front matterなし、巨大本文、タグ形式揺れ）テスト
* 性能観測（index.jsonサイズ、初回ロード時間の目安）

## 5. テスト計画

### 5.1 データ整合

* front matterなし：titleがファイル名になる
* tagsが文字列：正しく分割される
* tagsが配列：維持される
* addedが空：表示が `-`、ソートが破綻しない（空は末尾扱い）

### 5.2 UI機能

* タグ単体：該当件数が正しい
* タグ複数：AND条件になっている
* 自由語：タイトル/本文/作者/フォルダーでヒットする
* クリア：状態が既定に戻る

### 5.3 デプロイ

* Actionsで `dist/` に必要ファイルが揃う
* `./assets/index.json` が404にならない

## 6. リスクと対策

### 6.1 index.json肥大化

* リスク：本文を`searchText`に含めるためファイルサイズが増える
* 初期対策：抜粋長の抑制、Markdown整形で不要要素除外
* 追加対策：`searchText` を「本文冒頭のみ」に切替可能なフラグを設計（必要時）

### 6.2 公開範囲

* リスク：公開Pagesはデータが外部に見える
* 対策：公開可能なClippingsのみを対象にする／本文を含めない構成へ縮退

### 6.3 Markdown閲覧UX

* リスク：リンク先がmdテキスト表示
* 対策：将来フェーズでSSG導入しHTML化（仕様に拡張余地を保持）

## 7. 受け入れ基準（Acceptance Criteria）

* Pages上で以下が満たされる

  * 自由語検索が本文まで含めてヒットする
  * タグ絞り込み（複数AND）が動作する
  * 結果カードに「タイトル／タグ／追加日／作者／冒頭抜粋／格納フォルダー」が表示される
  * `main` pushで自動更新される

---

## 00_System集約に関する結論（要点のみ）

* `tools/ site/ assets/ package.json` を `MyObsidian/00_System/` に置く運用は成立します。
* 例外は `.github/workflows/` で、これはリポジトリ直下に置く必要があります。
* Pages配信用には、Actionsで `dist/` を作り、`00_System/site` と `00_System/assets` をそこへコピーする方式が最も確実です。

---

次工程として、上記ドキュメントに完全一致する形で「ファイル一式（最終版のコードとpages.yml）」を `00_System` 前提のパスに合わせて確定させます。必要な追加条件がある場合は「公開/非公開（本文インデックスに含めて良いか）」のみが設計に強く影響します。公開前提で本文を含める場合、情報公開の取り扱いだけは仕様として明記しておくのが必須です。

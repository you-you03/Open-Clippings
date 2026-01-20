# Cursor → GitHub → Notion タスク自動追加

## 概要
`tasks/` 配下にタスク定義（YAML）を追加して `main` に push すると、GitHub Actions が Notion のタスクDBへ自動でページを作成します。
Start/Stop/Today（Button）や Log（期間）、Taken(min.)（Formula）は Notion 側で管理し、APIからは更新しません。

---

## 事前準備（Notion）
1. Notionで Integration を作成し Token を取得
2. タスクDBを Integration に共有（Share → Invite）
3. タスクDBのプロパティ名が以下と一致していることを確認：
   - Name (Title)
   - Status (Status)
   - Do (Date)
   - Due (Date)
   - Flag (Select)
   - Tags_DB (Relation)
   - Projects_DB (Relation)

> 注意：Tags_DB / Projects_DB は Relation 先DBで、該当ページの「タイトル名」で解決します。

---

## GitHub Secrets
Repository Settings → Secrets and variables → Actions → New repository secret

- NOTION_TOKEN : Notion Integration Token
- NOTION_TASKS_DB_ID : Notion タスクDBの Database ID

---

## リポジトリ配置
以下を追加：
- .github/workflows/notion_tasks.yml
- 00_System/scripts/notion_sync.py
- 00_System/tasks/_template.yml

---

## 使い方（運用）
1. `tasks/` 配下に新規タスクYAMLを作る（例：`tasks/2026-01-02_thesis_review.yml`）
2. `main` へ push
3. GitHub Actions `Sync tasks to Notion` が成功すれば、Notion DBにタスクが追加される

---

## 仕様（重複防止）
同一タスクの二重登録を避けるため、以下が一致するページがNotion上に存在する場合は作成しません：
- Name == title
- Due == due（指定されている場合）
- Do == do（指定されている場合）

---

## トラブルシュート
- タグ/プロジェクトが見つからない：
  - Relation先DBに同名タイトルのページが存在するか確認
  - もしくは YAML にページID（UUID）を直接入れる
- Status/Flag が反映されない：
  - Notion側の選択肢名と YAML の文字列が一致しているか確認
- Actionsが動かない：
  - GitHub Actions が有効か、workflowファイルが main に存在するか確認

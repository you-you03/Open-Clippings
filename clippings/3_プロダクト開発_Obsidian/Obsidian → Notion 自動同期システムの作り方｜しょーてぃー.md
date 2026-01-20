---
title: "Obsidian → Notion 自動同期システムの作り方｜しょーてぃー"
source: "https://note.com/shoty/n/nc5d9bf8214b8?sub_rt=share_b"
author:
  - "[[note（ノート）]]"
published: 2025-05-07
created: 2025-05-09
description: "ども、しょーてぃーです。  CursorとObsidianを使ってちょっとよさげなメモ環境を構築したのですが、ページを知り合いに公開・共有することが難しくヤキモキしていました。  そこで、Obsidianの特定のフォルダやファイル→Notionの特定のページに自動同期してみることにしました。  大体、非エンジニアでも10分程度で終わります。 記事をCursorにコピペすればすぐに終わります。                             Obsidianで作ったドキュメントNotionに自動反映するようにしてみた。そのやり方おいておく。 知り合いに共有したいときにNot"
tags:
  - "obsidian"
  - "プロダクト"
  - "clippings"
  - "ノートツール"
---
![見出し画像](https://assets.st-note.com/production/uploads/images/188682802/rectangle_large_type_2_167957ac89c6d2159c573d3aabe6b2bf.png?width=1200)

## Obsidian → Notion 自動同期システムの作り方

[しょーてぃー](https://note.com/shoty)

ども、 [しょーてぃー](https://x.com/shoty_k2) です。  
  
CursorとObsidianを使ってちょっとよさげなメモ環境を構築したのですが、ページを知り合いに公開・共有することが難しくヤキモキしていました。

そこで、Obsidianの特定のフォルダやファイル→Notionの特定のページに自動同期してみることにしました。

大体、 **非エンジニアでも10分程度で終わります** 。  
記事をCursorにコピペすればすぐに終わります。

  

本人の私も概念・要件は理解しているが、非エンジニアすぎてコードの中身は理解しきれておりませんが、優しく見守っていてください。

## このシステムで実現できること

- Obsidianで編集したMarkdownファイルを自動的にNotionページに反映
- フォルダ構造をNotionの親子ページ構造として保持
- 削除したファイルはNotionでも自動的に削除
- Obsidianの内部リンク(\[\[Note\]\])をNotionのページリンクに自動変換
- 無料のサービスだけで構築（サーバー不要）

## 前提条件

- Obsidian（ノートアプリ）
- GitHub（ファイル管理サービス）のアカウント
- Notion（ドキュメント共有サービス）のアカウント

## 手順

### 1\. Notion側の準備

### ① インテグレーションの作成

1. [Notion API](https://www.notion.so/my-integrations) ページにアクセス
2. 「+ 新しいインテグレーション」ボタンをクリック
3. 好きな名前（例：「Obsidian Sync」）をつけて作成
4. 表示されるトークン（\`secret\_XXXXX...\`）をメモ帳などに保存（これが「Notion API Token」）
![画像](https://assets.st-note.com/img/1746605617-WvmxDVtKPG6uHoO0zpy8wIn2.png?width=1200)

  

### ② 親ページの準備

1. Notionで同期先となる親ページを作成（例：「Obsidian Sync」）
2. ページ右上の「・・・」メニューから「接続を追加」を選択
3. 先ほど作成したインテグレーションを追加して「アクセス権を付与」をクリック
4. ページのURLからページIDを取得：
	- URLの末尾部分（例：\` [https://www.notion.so/myworkspace/Obsidian-Sync-a1b2c3d4e5f6](https://www.notion.so/myworkspace/Obsidian-Sync-a1b2c3d4e5f6)...\`の\`a1b2c3d4e5f6...\`部分。?以降はいれないように）

### 2\. GitHub側の設定

### ① リポジトリの準備

1. [GitHub](https://github.com/) にアクセスし、ログイン
2. 「+」→「New repository」で新しいリポジトリを作成
3. 名前を付けて（例：\`obsidian-vault\`）、「Create repository」をクリック
4. リポジトリをローカルにクローン（GitHubデスクトップを使うと簡単）

### ② シークレット設定

1. リポジトリのページで「Settings」タブをクリック
2. 左メニューから「Secrets and variables」→「Actions」を選択
3. 「New repository secret」ボタンをクリック
4. 以下の2つのシークレットを追加：
	- 名前：\`NOTION\_TOKEN\`、値：メモしておいたNotionのトークン
	- 名前：\`PARENT\_PAGE\_ID\`、値：メモしておいたページID

### ③ ワークフローファイルの作成

階層構造を維持して同期させるのためにこちらを使いました(全然スターなくて不安にはなった）。

  

1. リポジトリ内に \`.github/workflows\` フォルダを作成
2. その中に \`notion-sync.yml\` というファイルを作成し、以下の内容を貼り付け：

```rust
name: Sync Obsidian → Notion (hierarchy)

on:
  push:
    paths:
      - "Flow/**.md"       # Flowフォルダ内のMarkdownファイル
      - "Archive/**.md"    # Archiveフォルダ内のMarkdownファイル
      - "Stock/**.md"      # Stockフォルダ内のMarkdownファイル
  workflow_dispatch:       # 手動実行も可能に

jobs:
  sync-to-notion:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
          
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
      
      # 必要な依存関係をインストール
      - name: Install dependencies
        run: npm install @notionhq/client @vrerv/md-to-notion
      
      # Flow フォルダの同期
      - name: Create Flow parent page if not exists
        id: create_flow_page
        run: |
          # スクリプトでFlowページを確認・作成
          FLOW_PAGE_ID=$(node -e '
            const { Client } = require("@notionhq/client");
            
            async function main() {
              const notion = new Client({ auth: process.env.NOTION_TOKEN });
              
              const response = await notion.search({
                query: "Flow",
                filter: {
                  property: "object",
                  value: "page"
                }
              });
              
              const flowPage = response.results.find(page => 
                page.parent?.page_id === process.env.PARENT_PAGE_ID && 
                page.properties?.title?.title?.[0]?.plain_text === "Flow"
              );
              
              if (flowPage) {
                console.log(flowPage.id);
              } else {
                const newPage = await notion.pages.create({
                  parent: {
                    page_id: process.env.PARENT_PAGE_ID
                  },
                  properties: {
                    title: {
                      title: [
                        {
                          text: {
                            content: "Flow"
                          }
                        }
                      ]
                    }
                  }
                });
                console.log(newPage.id);
              }
            }
            
            main().catch(error => {
              console.error(error);
              process.exit(1);
            });
          ')
          echo "FLOW_PAGE_ID=${FLOW_PAGE_ID}" >> $GITHUB_ENV
          echo "flow_page_id=${FLOW_PAGE_ID}" >> $GITHUB_OUTPUT
        env:
          NOTION_TOKEN: ${{ secrets.NOTION_TOKEN }}
          PARENT_PAGE_ID: ${{ secrets.PARENT_PAGE_ID }}

      - name: Sync Flow folder to Notion
        run: |
          npx @vrerv/md-to-notion \
            --token "$NOTION_TOKEN" \
            --page-id "$FLOW_PAGE_ID" \
            --delete \
            --verbose \
            "Flow"
        env:
          NOTION_TOKEN: ${{ secrets.NOTION_TOKEN }}
          FLOW_PAGE_ID: ${{ steps.create_flow_page.outputs.flow_page_id }}
      
      # Stock フォルダの同期（同様の処理）
      - name: Create Stock parent page if not exists
        id: create_stock_page
        run: |
          STOCK_PAGE_ID=$(node -e '
            const { Client } = require("@notionhq/client");
            
            async function main() {
              const notion = new Client({ auth: process.env.NOTION_TOKEN });
              
              const response = await notion.search({
                query: "Stock",
                filter: {
                  property: "object",
                  value: "page"
                }
              });
              
              const stockPage = response.results.find(page => 
                page.parent?.page_id === process.env.PARENT_PAGE_ID && 
                page.properties?.title?.title?.[0]?.plain_text === "Stock"
              );
              
              if (stockPage) {
                console.log(stockPage.id);
              } else {
                const newPage = await notion.pages.create({
                  parent: {
                    page_id: process.env.PARENT_PAGE_ID
                  },
                  properties: {
                    title: {
                      title: [
                        {
                          text: {
                            content: "Stock"
                          }
                        }
                      ]
                    }
                  }
                });
                console.log(newPage.id);
              }
            }
            
            main().catch(error => {
              console.error(error);
              process.exit(1);
            });
          ')
          echo "STOCK_PAGE_ID=${STOCK_PAGE_ID}" >> $GITHUB_ENV
          echo "stock_page_id=${STOCK_PAGE_ID}" >> $GITHUB_OUTPUT
        env:
          NOTION_TOKEN: ${{ secrets.NOTION_TOKEN }}
          PARENT_PAGE_ID: ${{ secrets.PARENT_PAGE_ID }}

      - name: Sync Stock folder to Notion
        run: |
          npx @vrerv/md-to-notion \
            --token "$NOTION_TOKEN" \
            --page-id "$STOCK_PAGE_ID" \
            --delete \
            --verbose \
            "Stock"
        env:
          NOTION_TOKEN: ${{ secrets.NOTION_TOKEN }}
          STOCK_PAGE_ID: ${{ steps.create_stock_page.outputs.stock_page_id }}
      
      # Archive フォルダも同様に同期
      - name: Create Archive parent page if not exists
        id: create_archive_page
        run: |
          ARCHIVE_PAGE_ID=$(node -e '
            const { Client } = require("@notionhq/client");
            
            async function main() {
              const notion = new Client({ auth: process.env.NOTION_TOKEN });
              
              const response = await notion.search({
                query: "Archive",
                filter: {
                  property: "object",
                  value: "page"
                }
              });
              
              const archivePage = response.results.find(page => 
                page.parent?.page_id === process.env.PARENT_PAGE_ID && 
                page.properties?.title?.title?.[0]?.plain_text === "Archive"
              );
              
              if (archivePage) {
                console.log(archivePage.id);
              } else {
                const newPage = await notion.pages.create({
                  parent: {
                    page_id: process.env.PARENT_PAGE_ID
                  },
                  properties: {
                    title: {
                      title: [
                        {
                          text: {
                            content: "Archive"
                          }
                        }
                      ]
                    }
                  }
                });
                console.log(newPage.id);
              }
            }
            
            main().catch(error => {
              console.error(error);
              process.exit(1);
            });
          ')
          echo "ARCHIVE_PAGE_ID=${ARCHIVE_PAGE_ID}" >> $GITHUB_ENV
          echo "archive_page_id=${ARCHIVE_PAGE_ID}" >> $GITHUB_OUTPUT
        env:
          NOTION_TOKEN: ${{ secrets.NOTION_TOKEN }}
          PARENT_PAGE_ID: ${{ secrets.PARENT_PAGE_ID }}

      - name: Sync Archive folder to Notion
        run: |
          npx @vrerv/md-to-notion \
            --token "$NOTION_TOKEN" \
            --page-id "$ARCHIVE_PAGE_ID" \
            --delete \
            --verbose \
            "Archive"
        env:
          NOTION_TOKEN: ${{ secrets.NOTION_TOKEN }}
          ARCHIVE_PAGE_ID: ${{ steps.create_archive_page.outputs.archive_page_id }}
```

### 3\. フォルダ構造の作成

1. リポジトリのルートに好きなフォルダを作成
	1. ここでは、以下のフォルダを同期します。
		- \`Flow\`
		- \`Stock\`
		- \`Archive\`
2. テスト用に、各フォルダに簡単なMarkdownファイルを1つずつ作成
![画像](https://assets.st-note.com/img/1746605676-t8l2NrjpYZ1c6dqBQLoHI5E0.png?width=1200)

  

### 4\. 実際に同期を試す

1. ファイルをGitHubにプッシュ
2. GitHubリポジトリの「Actions」タブから同期の進行状況を確認
3. 数分後、Notionを確認すると同期されているはず！
![画像](https://assets.st-note.com/img/1746605105-SR85juEN0BsaxA6IJCD1FMvV.png?width=1200)

![画像](https://assets.st-note.com/img/1746605498-6EAW18lz4y7LDKwnsjhbuoYX.png?width=1200)

![画像](https://assets.st-note.com/img/1746605217-A5VpwYld8UxSeZIWQNDLc2HX.png?width=1200)

ということで…

1. Obsidianで通常通りノートを編集
2. 変更をGitHubに定期的にプッシュ
3. 自動的にNotionへ同期される

あとは、双方向同期ではないので、notionに万が一編集が加わったら今はnotion MCPでその差分をLLMに判断させて対応です。

  

## トラブルシューティング

### 同期されない場合

1. GitHubの「Actions」タブでワークフローの実行状況を確認
2. 赤色のエラーがある場合は、エラーメッセージを確認
3. 動かないときは…：
	- Notion APIトークンが間違っている
	- ページIDが間違っている
	- Notionページにインテグレーションのアクセス権がない

### 階層構造に問題がある場合

1. Notionでページが正しく階層化されていない場合
2. 同期後、手動でNotionのページを整理しても、次回の同期で上書きされる点に注意

## おわりに

双方向の同期はちょっと面倒そうだったのでやめましたが、できるっぽいです。  
  
Obsidianをつかっていてわかったことは、そもそも私はメモをデジタルで撮ることが苦手＆面倒と感じたので、やめようと思います笑。

---

  

  

## 参考

- [Notion API公式ドキュメント](https://developers.notion.com/)
- [@vrerv/md-to-notion](https://github.com/vrerv/md-to-notion)
- [GitHub Actions公式ドキュメント](https://docs.github.com/ja/actions)

  

  

Obsidian → Notion 自動同期システムの作り方｜しょーてぃー
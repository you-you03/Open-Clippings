---
title: Obsidian Web ClipperとGemini連携による効率的な情報収集設定
source: https://qiita.com/vpkaerun/items/2120699db87526174740
author:
- '[[Qiita]]'
published: 2025-01-12
created: 2025-04-03
description: Obsidian Web ClipperとGemini連携による効率的な情報収集設定このドキュメントでは、Obsidian Web Clipper
  を使用してWebページをクリップし、Google…
tags:
- obsidian
- プロダクト
- clippings
- ai
- ノートツール
read: null
---
[@vpkaerun (楽描人 カエルン)](https://qiita.com/vpkaerun) 投稿日

## Obsidian Web ClipperとGemini連携による効率的な情報収集設定

==このドキュメントでは、Obsidian Web Clipper を使用してWebページをクリップし、Google AI (Gemini 1.5 Flash) を活用してMarkdown形式に変換、さらにMicrosoft Visual Studio CodeのMarkmap拡張機能でマインドマップ風に表示する方法を説明します。==

## 1\. Chrome拡張機能のインストール

========[![スクリーンショット 2025-01-12 015324.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F235474%2F880b2f41-2b3a-44bb-c081-6368d037f9c4.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=54614683930181761f2c85246f668418)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F235474%2F880b2f41-2b3a-44bb-c081-6368d037f9c4.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=54614683930181761f2c85246f668418)========

1. **Chrome ウェブストア** を開きます。
2. **Obsidian Web Clipper** を検索します。
3. **Chromeに追加** をクリックして拡張機能をインストールします。

## 2\. Obsidianの保管庫設定

1. Obsidian Web Clipper のアイコンをクリックします
2. **一般設定** を選択します
3. **保管庫** 欄に、Obsidianで使用する保管庫名を入力します（例: `2025` ）
	- 既存の保管庫を使用する場合は、正確な名前を入力してください
	- 新しい保管庫を使用する場合は、ここで名前を設定できます
4. **Enter** キーを押して保管庫を追加します

## 3\. Google APIキーの取得

1. **Google Cloud Platform** にアクセスし、APIキーを取得します
	- 詳細は以下の「Google Gemini APIキーの取得」を参照してください
2. 取得したAPIキーをメモします

### Google Gemini APIキーの取得手順

1. **Google AI Studio** にアクセスします
2. Googleアカウントでログインします
3. 左側のナビゲーションパネルから **Get API key** をクリックします
4. **Create API key in new project** をクリックします
5. 生成されたAPIキーをコピーします

[![スクリーンショット 2025-01-12 014802_2.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F235474%2Ff1233587-5403-b132-15ed-8f209e1d2bab.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=940e9fcc1675479844222f434e19c6e6)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F235474%2Ff1233587-5403-b132-15ed-8f209e1d2bab.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=940e9fcc1675479844222f434e19c6e6)

## 4\. インタプリタの設定

1. Obsidian Web Clipper の設定画面を開き、 **インタプリタ** タブを選択します
2. **プロバイダー** セクションで、 **+プロバイダーを追加** をクリックします
3. **プロバイダーを編集** ポップアップで、以下の情報を入力します
	- **プロバイダー**: **Google Gemini** を選択
	- **ベースURL**: `https://generativelanguage.googleapis.com/v1beta/chat/completions`
	- **APIキー**: 取得したGoogle Gemini APIキーを入力
4. **保存** をクリックします
5. 次に、 **モデル** セクションで、 **+モデルを追加** をクリックします
6. **モデルを編集** ポップアップで、以下の情報を入力します
	- **プロバイダー**: **Google Gemini** を選択
	- **モデル名**: `gemini 15f` (任意の名前)
	- **モデルID**: `gemini-1.5-flash`
7. **保存** をクリックします
8. **gemini 15f** モデルの右側にあるトグルスイッチをオンにします

[![スクリーンショット 2025-01-12 014854.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F235474%2F88dae3f6-bbe7-82b9-8499-e6a32bfc15ee.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=234626d776448a3939b8cf9190c24bfb)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F235474%2F88dae3f6-bbe7-82b9-8499-e6a32bfc15ee.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=234626d776448a3939b8cf9190c24bfb)

## 5\. テンプレートの設定

1. Obsidian Web Clipper の設定画面を開き、 **テンプレート** タブを選択します
2. **複製：デフォルト2** をクリックして、既存のテンプレートを複製します
3. **動作** セクションで、 **新規ノートを作成** が選択されていることを確認します
4. **ノート名** 欄に `{{date}}-{{title}}` を入力します
5. **ノートの場所** 欄に `80_clips` を入力します
6. **保管庫** 欄は **最後に使用** を選択します
7. **ノートの内容** 欄に以下を入力します
	Copied!
	```text
	{{ページの内容をメタ認知した上で、Markdown記法の見出し2/見出し3、本文を2レベルの箇条書き、文末にハッシュタグを付与}}
	```
8. **保存** をクリックします

[![スクリーンショット 2025-01-12 015018_2.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F235474%2Fbfe23406-6984-10c5-1dac-28b8b9650f1c.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=c344c68bd4863d3ec4c329dc80ffe5ec)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F235474%2Fbfe23406-6984-10c5-1dac-28b8b9650f1c.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=c344c68bd4863d3ec4c329dc80ffe5ec)

## 設定完了

==上記の手順で Obsidian Web Clipper の設定は完了です。Webページから情報をクリップする際、設定したテンプレートが適用され、指定した場所にノートが保存されます。==

==この設定により、Obsidian Web Clipper を Google Gemini を活用した効率的な情報収集ツールとして利用できます。==

[0](https://qiita.com/vpkaerun/items/2120699db87526174740/likers) 4 [comment 0](https://qiita.com/vpkaerun/items/#comments)

==新規登録して、もっと便利にQiitaを使ってみよう==

1. あなたにマッチした記事をお届けします
2. 便利な情報をあとで効率的に読み返せます
3. ダークテーマを利用できます
[ログインすると使える機能について](https://help.qiita.com/ja/articles/qiita-login-user) [新規登録](https://qiita.com/signup?callback_action=login_or_signup&redirect_to=%2Fvpkaerun%2Fitems%2F2120699db87526174740&realm=qiita) [ログイン](https://qiita.com/login?callback_action=login_or_signup&redirect_to=%2Fvpkaerun%2Fitems%2F2120699db87526174740&realm=qiita)
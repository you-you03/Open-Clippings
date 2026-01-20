---
title: "プロダクト開発に必要なもの全部繋げたらCursorが最強のプロダクトマネージャーになった｜田口 信元"
source: "https://note.com/guchey/n/n773a2efd78cf"
author:
  - "[[note（ノート）]]"
published: 
created: 2025-09-03
description: "Ubie株式会社で病気のQ&amp;Aのプロダクトマネージャー（PdM）を務めている、田口（@guchey）です。 Cursorをプロダクトマネジャーが活用する記事を見て、自分もプロダクトマネジメント業務の中心をCursorにしてみることにしました。 
 威力  すごい。各所にあった知識を集約した結果、自分の認知限界を超える相棒になりました。  現在のスプリント、バックログアイテム、OKR、ユーザーストーリー、主要メトリクスを把握したAIは、プロダクトの現在地から未来の姿まで詳細に把握したAIプロダクトマネージャーだった。  ディレクトリ構成  今はこんな構成にしています。  curs"
tags: ["ai", "プロダクト", "clippings", "gpt", "ノートツール"]
image: "assets/rectangle_large_type_2_52b33ab0c686ed75a78a16f33c1b2bae.png"
---
Ubie株式会社で[病気のQ&A](https://ubie.app/byoki_qa)のプロダクトマネージャー（PdM）を務めている、田口（[@guchey](https://x.com/ShingenTaguchi)）です。  
Cursorをプロダクトマネジャーが活用する記事を見て、自分もプロダクトマネジメント業務の中心をCursorにしてみることにしました。

威力
--

**すごい。**各所にあった知識を集約した結果、自分の認知限界を超える相棒になりました。

現在のスプリント、バックログアイテム、OKR、ユーザーストーリー、主要メトリクスを把握したAIは、**プロダクトの現在地から未来の姿まで詳細に把握したAIプロダクトマネージャーだった。**

ディレクトリ構成
--------

今はこんな構成にしています。

```
cursor_pdm/
├── .cursor/              
│   ├── mcp.json          
│   └── rules/            
│       ├── 000_general.mdc
│       ├── 001_github.mdc
│       ├── 002_jira.mdc
│       ├── 003_notion.mdc
│       └── 004_statistics.mdc
├── knowledge/            
│   ├── JIRA.md           
│   ├── OKR.md            
│   ├── ユーザーストーリー.md
│   ├── ダッシュボード.md
│   └── PBI作成ガイド.md
├── repo/                 
│   ├── xxx/             
│   └── yyy/            
├── workflows/            
│   ├── PBIプランニング.md
│   ├── PBIリファインメント.md
│   └── スプリントレビュー.md
└── tmp/
```

まず、knowledgeに格納したデータにはメンションするだけでChatから簡単にアクセスできます。普段利用しているSaaSのURLを羅列します。  
JIRA.mdはこんな感じで書いてます。

```
以下が利用しているJIRAのボードです。
https://xxx.atlassian.net/jira/software/projects/XXXX
```

![](https://assets.st-note.com/img/1742432540-HlinPFQBp9tXANJWhYIoETR8.png?width=1200)

Cursorが情報にアクセスできるようになる

OKRの進捗の確認をするようなユースケースであれば、単にそのページを見ればよかったのですが、各所に散らばったドキュメントを掛け合わせたいときに真価を発揮しました。  
OKRとユーザーストーリーと掛け合わせた壁打ちなどが簡単にできます。

![](https://assets.st-note.com/img/1742380952-b0POBfAm3TSnvkRXFE1uxgMJ.png?width=1200)

OKR壁打ちの開始

型化された資料作成などの業務はワークフローに事前にやるべきことを書いておけばワンパンで完了します。  
例えば、スプリントレビュー用の資料の作成ワークフローを(スプリントレビュー.md)のような名前で作成しておけば、内容に従って各所に散ったデータを統合してnotionに書き出してくれます。

![](https://assets.st-note.com/img/1742381373-O35rTM6uB1IVAFeiSPaZbwsE.png)

テンプレに従って、集めた情報を整理してnotionに出力

ワークフローの実行は、作成したワークフローファイルをメンションするだけです。スプリントレビュー.mdはこんな感じで書いています。

```
<workflow>
1. ユーザーストーリー.mdを読んで内容を理解する。必要に応じてMCPを実行する。
2. OKR.mdを読んで内容を理解する。必要に応じてMCPを実行する。
3. JIRA.mdを読んでスプリントゴールやPBIの内容を理解する。必要に応じてMCPを実行する。
4. ./tmp/sprintreview/goal.mdにスプリントの内容として理解したこととOKR、ユーザーストーリーの内容と紐付けて出力してください。
5. JIRA.mdを読んで完了レーンのPBIの課題キーを取得します。
6. githubのPRを完了レーンの課題キーで検索して、課題に紐づくPRを取得します。
7. ./tmp/sprintreview/pr.mdに完了レーンのPBIとPRの主要な変更内容と注意するべき点を出力します。
   1. 出力する際はPBIタイトル、PBI URL、PRタイトル、 PR URL、PBI担当者、PR担当者、主要な変更、主要な注意するべき点をリストで出力して下さい。
8. ダッシュボード.mdを読んで主要なメトリクスの変化を理解する。必要に応じてMCPを実行する。理解したことを./tmp/sprintreview/metrics.mdに出力してください。
9. <template>タグで指定したテンプレートに従って、./tmp/sprintreview/template.mdを作成してください。
10. ./tmp/sprintreview/goal.md、./tmp/sprintreview/pr.md、/tmp/sprintreview/metrics.mdに出力したことを理解して./tmp/sprintreview/template.mdを更新してください。
    1.  <okr>ブロックにはOKRの進捗状況を出力します。
    2.  <lightdash>ブロックには主要メトリクスの状況を出力します。ABテストに関する言及がある場合、統計的な分析を行なってください。
    3.  <jira>ブロックにはスプリントゴール、PBIとOKR、指標の関係を記載します。
    4.  <demo>ブロックには完了レーンの完了レーンのPBIとPRの主要な変更内容と注意するべき点を出力します。
11. ./tmp/sprintreview/template.mdの内容をユーザーにレビューしてもらってください。
12. 内容がOKであればnotionに出力するための空のページをユーザーに依頼してください。
13. notionに出力します
    1. 見出しは背景色をグレーにしてください。
    2. 箇条書きリスト、番号付きリストを適切に使ってください。
    3. GitHub、JIRAのURLはEmbedしてください。
</workflow>

<template>
```markdown

まず、簡単にスプリントレビューの目的やタイムボックスやワーキングアグリーメントを説明します（例えば、携帯電話をマナーモードにする、アプリの通知をオフにする、発言時以外はマイクをオフにする、など）
開発者にとってはステークホルダーとの数少ない接点なので、そのステークホルダーが初参加なのであれば、参加者がそれぞれ名前や役割などを自己紹介します


<okr>OKRの進捗を紹介</okr>


<lightdash>主要指標の確認</lighdash>


<jira>スプリントの内容をまとめます</jira>


<demo>完成したインクリメントのデモを行います。人間が書くので完成したインクリメントを列挙してください。</demo>


TBD


TBD
```
</template>



指定されたファイルが見つからないときは検索して実行してください。
```

![](https://assets.st-note.com/img/1742380528-lAI3HjGJOwdPSCXzvMN18mYR.png?width=1200)

事前定義したスプリントレビュー用ワークフローをメンションして実行

![](https://assets.st-note.com/img/1742380563-rxMdN6yY8aZTtwXAQVhPgWjs.png?width=1200)

必要に応じて各SaaSからプロダクトにまつわる情報を自動収集

PBIリファインメントの際は主要なメトリクス、ユーザーストーリー、OKRなども一緒にコンテキストとして与えることで、PBIの背景情報や得たい成果物が誰がみてもわかりやすいものになりました。作業完了時にJIRAのPBIも自動更新してくれます。  
ハイコンテキストなPBIを書いてしまいがちだった自分としては、とてもありがたいです。

![](https://assets.st-note.com/img/1742431878-u0VbXodI8eSm1wRci3gE74tH.png?width=1200)

いいアイデアはその場でリファインしてPBIまで作成してもらう

![](https://assets.st-note.com/img/1742431903-9MhmGsyYWwJ5Nj0aTXIoeV2d.png?width=1200)

Cursorが作成したPBI

プランニングの際はPBIとリポジトリをコンテキストで与えています。リポジトリの内容を把握してプランニングしてくれるので見積もりのブレが少なくなります。

ここまでくると、AIが建てたプランニングが完璧であれば、そのまま依頼して作業完了してしまうケースも多くあります。  
チームメンバーの意見や他のステークホルダーの確認が必要なものだけ、持ち帰って検討してプランニングが完了したら、再びPBIのURLを与えて実装をお願いします。

![](https://assets.st-note.com/img/1742432748-yYOotfJDqx9ViAIuEdQP7j2p.png?width=1200)

プロダクトマネージャーやエンジニアといった人間の仕事は、重要で難易度の高いものだけになりそうです。  
**もっと早く全部の情報をCursorに集約すればよかった。**

MCPサーバー
-------

社内の散らばった情報を集約して、Cursorに知識を与えるためにMCPサーバーは不可欠です。  
今回は社内で使っているSaaSに合わせて以下のものを設定しました。

### JIRA（スクラム）

### Notion（ユーザーストーリー・OKR・ドメイン知識）

### Lightdash（分析）

### Git/GitHub

Git/GitHubに関してはMCPサーバーもあるのですが、CLIをCursorに許可させた方が無駄にアクセストークンを払い出す必要がないので使いませんでした。単にproject rulesにCLIの使い方を書いておくだけでいいのでMCPサーバーの設定よりも簡単かもしれません。  
また、CLIも選択肢に入ってくるとMCPサーバーの有無を問わなくなってくるので連携できるサービスが増えます。

まとめ
---

CursorはAIコードエディタにあらず。AIプロダクト開発エージェントです。

最後に
---

今後も生成AI関連の情報を発信するのでよろしければぜひフォローお願いします！

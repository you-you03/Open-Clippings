---
title: "発表から約2週間、いますぐ使えるAgent Skills 10選｜Seiji Takahashi@ベースマキナ"
source: "https://note.com/timakin/n/na8b2789897ea?sub_rt=share_pw"
author:
  - "[[Seiji Takahashi@ベースマキナ]]"
published: 2025-12-28
created: 2025-12-28
description: "皆さまこんにちは、株式会社ベースマキナの代表取締役社長を務めております高橋（@__timakin__）です。  2025年12月18日、AnthropicがAgent Skillsをオープンスタンダードとして発表しました。MCPに続く標準化の動きとして注目を集めています。  面白いのは、発表からわずか数日でOpenAIがCodex CLIとChatGPTに同規格を採用し、GitHub Copilotも対応を発表したこと。Anthropicが仕様を公開し、競合が追従する——MCPで見た流れが再び起きています。さすがAnthropicという感じで、一気に業界標準となりつつありますね。"
tags:
  - "clippings"
  - "ai"
  - "エージェント"
  - "スキル"
  - "開発"
later: false
---
![見出し画像](https://assets.st-note.com/production/uploads/images/239341547/rectangle_large_type_2_4a6ff0dc48ad66a970d8004c123ecf3b.png?width=1280)

## 発表から約2週間、いますぐ使えるAgent Skills 10選

50番目のスキ！

[Seiji Takahashi@ベースマキナ](https://note.com/timakin)

皆さまこんにちは、株式会社ベースマキナの代表取締役社長を務めております高橋（ [@\_\_ **timakin**](https://twitter.com/__timakin__) **\_\_** ）です。

2025年12月18日、AnthropicがAgent Skillsをオープンスタンダードとして発表しました。MCPに続く標準化の動きとして注目を集めています。

面白いのは、発表からわずか数日でOpenAIがCodex CLIとChatGPTに同規格を採用し、GitHub Copilotも対応を発表したこと。Anthropicが仕様を公開し、競合が追従する——MCPで見た流れが再び起きています。さすがAnthropicという感じで、一気に業界標準となりつつありますね。

[**GitHub Copilot now supports Agent Skills - GitHub Changelog** *You can now create Agent Skills to teach Copilot how to perfo* *github.blog*](https://github.blog/changelog/2025-12-18-github-copilot-now-supports-agent-skills/)

この記事では、発表から約2週間で話題になっているスキルを厳選して紹介します。

## この記事でわかること

- Agent Skillsの概要
- カテゴリ別おすすめスキル10選
- インストール方法と注意点

---

## Agent Skillsとは

Agent Skillsは、Claude（やCodex CLI、Copilot）に特定のタスクを教えるための仕組みです。技術的には、\`SKILL.md\`ファイル + スクリプト + リソースで構成されたフォルダです。

特徴的なのは「Progressive Disclosure」という設計思想。Claudeはまずメタデータだけをスキャンして（約100トークン）関連性を判断し、必要なときだけフルコンテンツを読み込みます（約5kトークン）。この仕組みのお陰で大量にスキルを組み込んでもパフォーマンスが劣化しないようです（とはいえ適切に選択できるかは別問題ですが）。

[**Introducing Agent Skills | Claude** *Claude can now use Skills to improve how it performs specific* *www.anthropic.com*](https://www.anthropic.com/news/skills)

---

## ドキュメント処理系（公式）

Anthropicの公式リポジトリには、すぐに使えるドキュメント処理スキルが揃っています。

### 1\. docx（Word文書）

Word文書の生成・編集ができます。テンプレートを使った定型文書の作成、既存文書の修正など、地味だけど実務で重宝するスキルですね。

### 2\. xlsx（Excel）

数式付きのスプレッドシートを生成できます。「売上データをピボットテーブル風にまとめて」といった依頼にも対応可能。

### 3\. pptx（PowerPoint）

プレゼンテーション資料の生成。スライド構成から内容まで一気に作れるのは時間短縮になります。

### 4\. pdf

PDF生成やフォーム作成に対応。契約書のテンプレートなど、フォーマットが固定されたドキュメントに向いています。

---

## 開発ワークフロー系

エンジニアにとって実用的なスキルも充実しています。

### 5\. Playwright Browser Automation

Webアプリのテスト・検証を自動化するスキル。「このフォームの入力バリデーションをテストして」といった依頼に対応できます。Claudeがブラウザを操作してテストを実行し、結果を報告してくれる。

### 6\. Git automation（obra/superpowers）

obra/superpowersというコミュニティ製コレクションに含まれるスキル。コミットメッセージの自動生成、ステージング、プッシュまでを一連の流れで実行できます。\`/brainstorm\`、\`/write-plan\`、\`/execute-plan\`といったコマンドも便利。

### 7\. Test fixing

失敗しているテストを特定し、修正案を提示するスキル。CI/CDでテストが落ちたときに「直して」と頼むだけで対応してくれるのは助かります。

---

## エンタープライズ連携系

Anthropicはパートナー企業と連携し、エンタープライズ向けスキルも提供しています。Skills Directory（claude.com/connectors）から有効化できます。

### 8\. Atlassian（Jira/Trello連携）

「このバグをJiraチケットにして」「Trelloにタスクを追加して」といった依頼に対応。プロジェクト管理ツールとの連携は、PdMにとって特に嬉しいのではないでしょうか。

### 9\. Figma連携

ブランドガイドラインをFigmaのデザインに適用するスキル。マーケティング資料の作成時に、ブランドカラーやタイポグラフィを自動で統一してくれます。

---

## 個人・チーム向けユーティリティ

ちょっとした便利スキルも紹介しておきます。

### 10\. Skill Creator

スキル作成のガイドを提供する「メタスキル」。自分でスキルを作りたいときに、フォーマットやベストプラクティスを教えてくれます。Skillsエコシステムに貢献したい人向け。

他にも、 **Lead Research Assistant** （リード調査・アウトリーチ戦略）や **Domain Name Brainstormer** （ドメイン名のアイデア出し＆空き確認）など、ニッチだけど刺さる人には刺さるスキルがあります。

---

## ほか、コレクション

個別スキルだけでなく、まとめてインストールできるコレクションも話題になっています。

### wshobson/agents

107スキル + 99エージェント + 15オーケストレーターを含む大規模コレクション。67個のプラグインに分かれていて、必要なものだけインストールできます。

Kubernetes、Helm、RAG実装、プロンプトエンジニアリングなど、幅広いドメインをカバー。「とりあえず全部入れる」より「必要なプラグインだけ選ぶ」使い方が推奨されています。

  

### SkillsMP

25,000以上のスキルを検索できるコミュニティマーケットプレイス。GitHubから自動収集しており、Claude Code、Codex CLI、ChatGPTに対応。カテゴリや人気順でフィルタリングできます。

[**Agent Skills Marketplace - Claude, Codex & ChatGPT Skills | SkillsMP** *Browse 25,000+ agent skills compatible with Claude Code, Code* *skillsmp.com*](https://skillsmp.com/)

  

---

## OpenAIも追従——業界標準化の流れ

冒頭でも触れましたが、Agent Skillsはすでに業界標準になりつつあります。

OpenAIはCodex CLIとChatGPTで同じAgent Skills規格を採用。GitHub Copilotも12月18日に対応を発表しました。Cursor、Microsoftも採用済み。

[https://venturebeat.com/ai/anthropic-launches-enterprise-agent-skills-and-opens-the-standard](https://venturebeat.com/ai/anthropic-launches-enterprise-agent-skills-and-opens-the-standard)

これはMCPで見た流れと大体同じですよね。Anthropicが仕様を公開し、オープンスタンダードとして提供する。競合がそれに追従する。結果として、開発者は一度スキルを作れば複数のAIプラットフォームで使えるのは、導入も作成も楽でポータビリティがあっていいですね。

Simon Willisonは「MCPの爆発が控えめに見えるほどのCambrian explosionが起きる」と予測しています。個人的にも、ここ1〜2週間でGitHubに公開されるスキルの数が急増しているのを感じています。

[**Claude Skills are awesome, maybe a bigger deal than MCP** *Anthropic this morning introduced Claude Skills, a new patter* *simonwillison.net*](https://simonwillison.net/2025/Oct/16/claude-skills/)

---

## インストール方法

ご存じの方も多いかもしれませんが、まだ入れてないよという方向けにインストール手順を念の為記載しておきます。

```ruby
# マーケットプレイス登録（初回のみ）
/plugin marketplace add anthropics/skills

# スキルインストール
/plugin install document-skills@anthropics-skills
```

スキルの配置場所：

- 個人用: \`~/.claude/skills/\`
- プロジェクト用: \`.claude/skills/\`

**注意点**: コードを含むスキルは実行前にレビューすることをおすすめします。SkillsMPなどのコミュニティマーケットプレイスは基本的なフィルタリング（2スター以上）をしていますが、信頼できるソースかどうかは自分で判断する必要があります。

---

## さいごに

Agent Skills発表から約2週間、すでにエコシステムが形成されつつあります。

公式のドキュメント処理スキル、パートナー企業によるエンタープライズ連携、コミュニティによる大規模コレクション——MCPで見たエコシステムの急激な整備がSkillsでも起きているのだと思います。

個人的には、MCPと比べてSkillsのほうが扱いやすいと感じる場面が多いです。MCPはサーバーを立てる必要があり、インフラの設定やプロセス管理が発生します。一方Skillsは、フォルダに\`SKILL.md\`を置くだけ。サーバー不要、プロセス管理不要、Gitでバージョン管理もできる。チームで共有するときも\`.claude/skills/\`にコミットするだけで済みます。

もちろんMCPには「外部サービスとリアルタイムに連携できる」という強みがあります。データベースへのクエリや外部APIの呼び出しなど、動的な処理が必要な場合はMCPのほうが適しています。ただ、「特定のタスクの進め方を教える」「ワークフローを定義する」といった用途では、Skillsのシンプルさが際立ちます。

自分のワークフローに合ったスキルを探す楽しさもありますね。「こんなスキルあったらいいな」が見つかったときの嬉しさは、良いVSCode拡張を見つけたときに似ています。まだ発表から2週間なので、これからさらに面白いスキルが出てくるはずですし、自分自身もスキルを作って公開してみたいと考えています。

---

弊社ベースマキナでは日々、技術トレンドだけでなく組織・プロダクト開発トレンドを意識してリサーチなども行っています。同じような話題に興味がある方は、ぜひお声がけください。

- X: [@\_\_ **timakin**](https://twitter.com/__timakin__) **\_\_**
- 会社HP: [https://about.basemachina.com/](https://about.basemachina.com/)

---

## 参考リンク

- [Introducing Agent Skills | Anthropic](https://www.anthropic.com/news/skills)
- [Equipping agents for the real world with Agent Skills | Anthropic](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Anthropic launches enterprise Agent Skills | VentureBeat](https://venturebeat.com/ai/anthropic-launches-enterprise-agent-skills-and-opens-the-standard)
- [GitHub - anthropics/skills](https://github.com/anthropics/skills)
- [GitHub - wshobson/agents](https://github.com/wshobson/agents)
- [SkillsMP Marketplace](https://skillsmp.com/)
- [Claude Skills are awesome | Simon Willison](https://simonwillison.net/2025/Oct/16/claude-skills/)
- [GitHub Copilot now supports Agent Skills](https://github.blog/changelog/2025-12-18-github-copilot-now-supports-agent-skills/)

50番目のスキ！

ありがとうございます！励みになります！(๑╹◡╹๑)ﾉ

[![買うたび 抽選 ※条件・上限あり ＼note クリエイター感謝祭ポイントバックキャンペーン／最大全額もどってくる！ 12.1 月〜1.14 水 まで](https://assets.st-note.com/poc-image/manual/production/20271127_pointback_note_detail.jpg?width=620&dpr=2)](https://note.com/topic/campaign)

発表から約2週間、いますぐ使えるAgent Skills 10選｜Seiji Takahashi@ベースマキナ
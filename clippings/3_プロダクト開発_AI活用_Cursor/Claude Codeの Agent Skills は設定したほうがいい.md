---
title: Claude Codeの Agent Skills は設定したほうがいい
source: https://syu-m-5151.hatenablog.com/entry/2025/12/19/173309
author:
- '[[nwiizo (id:syu-m-5151)]]'
published: 2025-12-19
created: 2025-12-22
description: Claude Codeを使い始めて、様々な発信をしてきました。今回は「Agent Skills」について。これも設定しておくと、Claude
  Codeがグッと使いやすくなる機能です。 Claude Code の settings.json は設定した方がいい - じゃあ、おうちで学べる Claude
  Code の CLAUDE.mdは設定した方がいい - じゃあ、おうちで学べる Claude Code の .claude/commands/**.md は設定した方がいい
  - じゃあ、おうちで学べる Claude CodeのHooksは設定したほうがいい - じゃあ、おうちで学べる Claude…
tags:
- claude-code
- ai活用
- 開発ツール
- エージェント
- 開発環境
later: false
---
Claude Codeを使い始めて、様々な発信をしてきました。今回は「Agent Skills」について。これも設定しておくと、Claude Codeがグッと使いやすくなる機能です。

- [Claude Code の settings.json は設定した方がいい - じゃあ、おうちで学べる](https://syu-m-5151.hatenablog.com/entry/2025/06/05/134147)
- [Claude Code の CLAUDE.mdは設定した方がいい - じゃあ、おうちで学べる](https://syu-m-5151.hatenablog.com/entry/2025/06/06/190847)
- [Claude Code の.claude/commands/\*\*.md は設定した方がいい - じゃあ、おうちで学べる](https://syu-m-5151.hatenablog.com/entry/2025/06/25/062736)
- [Claude CodeのHooksは設定したほうがいい - じゃあ、おうちで学べる](https://syu-m-5151.hatenablog.com/entry/2025/07/14/105812)
- [Claude CodeのSubagentsは設定したほうがいい - じゃあ、おうちで学べる](https://syu-m-5151.hatenablog.com/entry/2025/09/09/143306)

## はじめに

「このプロジェクトでは [python](https://d.hatena.ne.jp/keyword/python) -pptxを使ってスライドを作って」「 [SQL](https://d.hatena.ne.jp/keyword/SQL) は必ずこのフォーマットで書いて」「コードレビューはこの観点でチェックして」。Claude Codeを使っていると、こういう説明を何度も繰り返すことになります。CLAUDE.mdに書けば解決すると感じるでしょう。しかしCLAUDE.mdに書いても、毎回読み込まれるとは限らない。commandsを作っても、手動で呼び出す必要がある。どちらも「繰り返し」を完全には解決してくれません。

私自身、Rustプロジェクトの開発をClaude Codeに任せようとして、この問題に何度もぶつかりました。「ビルドは `cargo fmt` から始めて」「セキュリティチェックはOWASPの観点で」「テストは統合テストまで回して」。1回のセッションでは覚えてくれる。しかし新しいセッションを始めると、また最初から説明し直し。なぜこうなるのか。

この問題の根本にあるのは、LLMの [アーキテクチャ](https://d.hatena.ne.jp/keyword/%A5%A2%A1%BC%A5%AD%A5%C6%A5%AF%A5%C1%A5%E3) 上の制約です。LLMはステートレスで、セッション間で記憶を保持しません。 [トーク](https://d.hatena.ne.jp/keyword/%A5%C8%A1%BC%A5%AF) ン制約とコスト制約があるため、すべての知識を常に保持できません。だから、毎回同じ説明が必要になります。

Agent Skillsは、この制約を回避する仕組みです。すべての知識を常に持たせるのではなく、 **必要な時に必要な知識だけを読み込む** 。この [発想の転換](https://d.hatena.ne.jp/keyword/%C8%AF%C1%DB%A4%CE%C5%BE%B4%B9) により、ステートレスなLLMでも「状態を持っているかのように」振る舞えます。一度Skillを作っておけば、関連するタスクで自動的にその知識が使われます。

[www.anthropic.com](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

このブログが良ければ [**読者になったり**](https://blog.hatena.ne.jp/syu-m-5151/syu-m-5151.hatenablog.com/subscribe?from_url=https%3A%2F%2Fsyu-m-5151.hatenablog.com%2F&utm_source=hatena-follow-button-box&utm_medium=button&utm_campaign=subscribe_blog) 、 **nwiizo** の [**X**](https://x.com/nwiizo) や [**Github**](https://github.com/nwiizo) をフォローしてくれると嬉しいです。

## 他の設定との違い

今まで紹介してきた機能との違いを整理しておきます。

| 機能 | 役割 | 例 |
| --- | --- | --- |
| **CLAUDE.md** | プロジェクトの文脈を伝える | 「うちはTypeScriptで、こういう [アーキテクチャ](https://d.hatena.ne.jp/keyword/%A5%A2%A1%BC%A5%AD%A5%C6%A5%AF%A5%C1%A5%E3) 」 |
| **commands** | 手動で呼び出すショートカット | `/test-and-commit` で一連の作業を実行 |
| **Hooks** | 特定のイベントで自動実行 | ファイル保存後に自動フォーマット |
| **Subagents** | 専門家を自動で呼び出す | [デバッグ](https://d.hatena.ne.jp/keyword/%A5%C7%A5%D0%A5%C3%A5%B0) 時にdebugger subagentが起動 |
| **Rules** | **パス単位でルールを適用** | `src/api/**/*.ts` にセキュリティルール |
| **Agent Skills** | **専門知識をオンボーディング** | PDF操作、 [Excel](https://d.hatena.ne.jp/keyword/Excel) 分析、独自ワークフロー |

**Rulesについて補足**: `.claude/rules/` [ディレクト](https://d.hatena.ne.jp/keyword/%A5%C7%A5%A3%A5%EC%A5%AF%A5%C8) リに配置することで、特定の拡張子や [ディレクト](https://d.hatena.ne.jp/keyword/%A5%C7%A5%A3%A5%EC%A5%AF%A5%C8) リに対して細かいルールを適用できます。CLAUDE.mdがグローバルな設定なのに対し、Rulesは「このパスにはこのルール」という精密なスコープ設定が可能です。無駄なコンテキスト消費を抑えつつ、必要なルールだけを読み込ませる「段階的開示」の考え方に基づいています。Rulesについては別記事で詳しく書く予定です。

表を見ると、各機能には明確な役割分担があります。CLAUDE.mdは文脈、commandsはショートカット、Hooksは自動化、Subagentsは専門家の呼び出し。では、Skillsは何が違うのか。ポイントは、Skillsが「Claudeができること自体を拡張する」点です。他の設定がClaudeの「使い方」を定義するのに対し、SkillsはClaudeの「専門知識」を拡張します。LLMの推論能力自体は変わりませんが、専門家の知識を注入することで出力品質が向上します。

## Agent Skillsとは何か

Anthropicの公式ブログでは、Agent Skillsをこう説明しています。

> Building a skill for an agent is like putting together an onboarding guide for a new hire. （エージェントにSkillを作ることは、新入社員向けのオンボーディングガイドを作るようなものです）

Skillは、指示・ [スクリプト](https://d.hatena.ne.jp/keyword/%A5%B9%A5%AF%A5%EA%A5%D7%A5%C8) ・リソースをまとめたフォルダです。Claudeがタスクに応じて自動的に読み込み、その専門知識を活用します。

[platform.claude.com](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)

Skill に関しても公式ドキュメントが本当に良いのでオススメです。 **Anthropicはとりあえず、公式ドキュメント** これは標語にしてほしいです。

[platform.claude.com](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

それでも自分的にまとめたいので書かせていただきます。

### なぜSkillsが必要なのか

Claude Codeは万能ですが、「特定のタスク」に最適化されていないことがあります。例えば [PowerPoint](https://d.hatena.ne.jp/keyword/PowerPoint) を作ろうとすると、どのライブラリを使うか迷います。フォーマットの細かい仕様を知らない。エッジケースでバグる。毎回試行錯誤が発生します。

一方、Skillsがあれば違います。 **Anthropicのエンジニアが [PowerPoint](https://d.hatena.ne.jp/keyword/PowerPoint) 作成の最適解を徹底的に検証して、その知識をパッケージ化している** 。Claudeはそれを読み込んで、最初からプロとしての出力ができます。この辺は松本勇気さんの [生成AI「戦力化」の教科書](https://bookplus.nikkei.com/atcl/catalog/25/08/28/02166/) なんかもとても良いし今度、 [オライリー](https://d.hatena.ne.jp/keyword/%A5%AA%A5%E9%A5%A4%A5%EA%A1%BC) から翻訳本 [AIエンジニアリング―基盤モデルを用いたAIアプリケーション開発の基礎と実践](https://www.oreilly.co.jp/books/9784814401383/) もとても良い。

### Tool、Skills、MCPの違い

混乱しやすいポイントを整理しておきます。Anthropicの [ブログ記事](https://claude.com/blog/extending-claude-capabilities-with-skills-mcp-servers) では、わかりやすいたとえが使われています。

[claude.com](https://claude.com/blog/extending-claude-capabilities-with-skills-mcp-servers)

> [MCP](https://d.hatena.ne.jp/keyword/MCP) is like having [access](https://d.hatena.ne.jp/keyword/access) to the aisles. Skills, meanwhile, are like an employee's expertise. （ [MCP](https://d.hatena.ne.jp/keyword/MCP) は店の通路へのアクセス。Skillsは店員の専門知識。）

壊れたキャ [ビネット](https://d.hatena.ne.jp/keyword/%A5%D3%A5%CD%A5%C3%A5%C8) を直したいとき、ハードウェアストアに行けば木工用接着剤もクランプも蝶番も揃っています。しかし、 **何を買えばいいか、どう使えばいいかは別問題** です。

| 概念 | 役割 | たとえ |
| --- | --- | --- |
| **Tool** | 何ができるか（Capability） | 店にある道具そのもの |
| **[MCP](https://d.hatena.ne.jp/keyword/MCP)** | 道具へのアクセス（Connectivity） | 店の通路に入ること |
| **Skills** | どう振る舞うか（Behavior） | 道具の使い方を教える店員 |

Toolは「 [API](https://d.hatena.ne.jp/keyword/API) を叩く」「DBに接続する」「ファイルを操作する」といった個別の能力です。 [MCP](https://d.hatena.ne.jp/keyword/MCP) はそれらのToolを統一規格で接続するアダプター。外部システムへの安全で標準化されたアクセスを提供します。

そしてSkillsは「どう振る舞うか（Behavior）」まで定義します。複数のToolをどの順番で、どういう判断基準で使うか。 **Toolの使い方マニュアル付きで渡す** のがSkillsです。 [MCP](https://d.hatena.ne.jp/keyword/MCP) が接続性を提供し、Skillsがその接続性を効果的に使うための手続き的知識を提供する。 **両者は競合するものではなく、組み合わせることで真価を発揮します** 。

この構造は、BDD（Behavior-Driven Development、振る舞い駆動開発）に似ています。BDDは単なるテスト手法ではなく、チーム全体の「対話」を促進し、ビジネス価値の高いソフトウェアを効率的に生み出すための開発アプローチです。TDD（ [テスト駆動開発](https://d.hatena.ne.jp/keyword/%A5%C6%A5%B9%A5%C8%B6%EE%C6%B0%B3%AB%C8%AF) ）が「コードが正しく実装されているか」という開発者視点なのに対し、BDDは「システムが期待通りに振る舞うか」というユーザー・ビジネス視点で考えます。

BDDでは、Gherkin記法を使って「Given-When-Then」形式でシナリオを書きます。

```gherkin
Feature: ログイン機能

  Scenario: ユーザーが正しいIDとパスワードでログインできる
    Given ログインページが表示されている
    When  正しいIDとパスワードを入力してログインボタンを押す
    Then  ホームページにリダイレクトされる
```

このシナリオは、開発者だけでなく、QAエンジニア、プロダクトオーナー、ビジネス担当者など、全員が読めます。これが「生きた仕様書」として機能し、認識の齟齬を埋めます。

Skillsも同じ構造を持っています。

| BDD | Skills |
| --- | --- |
| Given（前提条件） | description（いつ起動するか） |
| When（アクション） | SKILL.md本文（何をするか） |
| Then（期待結果） | 具体的な手順（どう振る舞うか） |

**BDDがテストで「コードの振る舞い」を保証するように、SkillsはAIエージェントの「振る舞い」を保証します。**

BDDの本質的な価値は「ビジネス側とエンジニアの共通言語」でした。「3つのアミーゴ」（PO、開発者、QA）が対話し、全員が納得する仕様を作り上げます。Skillsも同じです。現場の [ドメイン](https://d.hatena.ne.jp/keyword/%A5%C9%A5%E1%A5%A4%A5%F3) エキスパートが [Markdown](https://d.hatena.ne.jp/keyword/Markdown) で書いた手順は、そのままAIの振る舞いになります。つまり、 **Skillsは「AIエージェントのためのBDD」** だと言えます。プログラミングなしで、 [自然言語](https://d.hatena.ne.jp/keyword/%BC%AB%C1%B3%B8%C0%B8%EC) で、AIの振る舞いを定義できます。

Skillsの設計で最も重要な概念が「 [Progressive](https://d.hatena.ne.jp/keyword/Progressive) Disclosure（段階的開示）」です。これは「すべての情報を最初から渡すのではなく、必要になったタイミングで必要な情報だけを渡す」という設計原則です。

なぜこの原則がSkillsに必要なのか。LLMには「コンテキストウィンドウ」という物理的な制約があります。Claude 3.5 Sonnetで約200K [トーク](https://d.hatena.ne.jp/keyword/%A5%C8%A1%BC%A5%AF) ン。これは多いようで、実際のタスクでは意外と消費が早い。コードファイルを10個読み込めば数万 [トーク](https://d.hatena.ne.jp/keyword/%A5%C8%A1%BC%A5%AF) ン、会話履歴が長くなればより消費される。ここに50個のSkillsの全内容（各5000 [トーク](https://d.hatena.ne.jp/keyword/%A5%C8%A1%BC%A5%AF) ン）を読み込んだら、250K [トーク](https://d.hatena.ne.jp/keyword/%A5%C8%A1%BC%A5%AF) ン。コンテキストが溢れます。

だからSkillsは **3段階** で情報を開示します。これは「必要な時に必要な分だけ」というJust-In-Time戦略です。

**Level 1: [メタデータ](https://d.hatena.ne.jp/keyword/%A5%E1%A5%BF%A5%C7%A1%BC%A5%BF) （常にロード）** - 約100 [トーク](https://d.hatena.ne.jp/keyword/%A5%C8%A1%BC%A5%AF) ン/Skill

```yaml
---
name: pdf-processing
description: Extract text and tables from PDF files, fill forms, merge documents.
---
```

起動時に全Skillのname/descriptionだけ読み込みます。50個のSkillがあっても5000 [トーク](https://d.hatena.ne.jp/keyword/%A5%C8%A1%BC%A5%AF) ン程度。これでClaudeは「どんなSkillが使えるか」の全体像を把握できます。

**Level 2: 指示（トリガー時にロード）** - 5000 [トーク](https://d.hatena.ne.jp/keyword/%A5%C8%A1%BC%A5%AF) ン以下が目安

SKILL.mdの本文。「PDFを操作して」と言われたら、descriptionから「pdf-processingが関連する」と判断し、そのSKILL.mdを読み込みます。関係ないSkillは読み込まない。

**Level 3: リソース（必要時にロード）** - 必要に応じて

追加のファイル、 [スクリプト](https://d.hatena.ne.jp/keyword/%A5%B9%A5%AF%A5%EA%A5%D7%A5%C8) 、リファレンス。SKILL.md内で「フォーム入力が必要なら `FORMS.md` を参照」と書いておけば、そのタスクが発生したときだけ読み込みます。

```
pdf-skill/
├── SKILL.md              # Level 2: メイン指示
├── FORMS.md              # Level 3: フォーム入力ガイド
├── reference.md          # Level 3: APIリファレンス
└── scripts/
    └── fill_form.py      # Level 3: ユーティリティスクリプト
```

**この設計の本質は「推論空間の段階的絞り込み」です。** Level 1で「使えるSkillの候補」を提示し、Level 2で「このタスクにはこの手順」を特定し、Level 3で「この具体的な操作にはこのリソース」を提供する。LLMの自由な推論を、段階的に制約していく。これがSkillsの賢さです。

### SkillsとSubagentsの使い分け

「Skillsって、前に書いたSubagentsと同じじゃないですか」という声が聞こえてきます。確かに両方とも「専門知識をパッケージ化する」という点では似ています。しかし、 **コンテキストの扱い方** に決定的な違いがあります。

| 観点 | Skills | Subagents |
| --- | --- | --- |
| コンテキスト | **親と共有** | **独立** |
| 向いているタスク | 継続的な作業、TDDなど | 試行錯誤、調査タスク |
| 状態の引き継ぎ | あり | なし（結果のみ返す） |

**なぜこの違いが生まれるのか。** 技術的には、Skillsは「現在のセッションにドキュメントを追加読み込みする」だけです。会話の流れ、ファイルの状態、変数の値、すべてが共有されたままです。一方、Subagentsは「新しいClaude Codeプロセスを起動する」に近い。独立したコンテキストウィンドウを持ち、親とは結果だけをやり取りします。

**Subagentsはコンテキストが独立しています** 。Claude Codeの中でClaude Codeを呼ぶようなもの。試行錯誤を伴うエラー調査みたいな「ごちゃごちゃした作業」をSubagentに任せると、親側のコンテキストが汚れません。

**なぜ「汚れない」ことが重要なのか。** コンテキストウィンドウは有限です。試行錯誤を10回繰り返すと、その10回分の履歴がコンテキストに残ります。成功した最 [終結](https://d.hatena.ne.jp/keyword/%BD%AA%B7%EB) 果だけが欲しいのに、失敗した9回分も抱え込むことになる。Subagentなら、その試行錯誤は子プロセスの中で完結し、親には「結果：○○が原因でした」という要約だけが返ってきます。

**Skillsはコンテキストを共有します** 。 [テスト駆動開発](https://d.hatena.ne.jp/keyword/%A5%C6%A5%B9%A5%C8%B6%EE%C6%B0%B3%AB%C8%AF) をさせるとき、RED-GREEN-REFACTORのサイクルごとにコンテキストが分断されると困ります。「さっきテスト書いたよね」「なんでこの設計にしたんだっけ」という文脈を保持したまま作業を続けたい。そういうときはSkillsが向いています。

**なぜ「共有する」ことが重要なのか。** TDDは本質的に「対話」です。テストを書く→実装する→ [リファクタリング](https://d.hatena.ne.jp/keyword/%A5%EA%A5%D5%A5%A1%A5%AF%A5%BF%A5%EA%A5%F3%A5%B0) する、この流れの中で「なぜこのテストを書いたか」「なぜこの設計にしたか」という文脈が失われると、 [リファクタリング](https://d.hatena.ne.jp/keyword/%A5%EA%A5%D5%A5%A1%A5%AF%A5%BF%A5%EA%A5%F3%A5%B0) の方向性が定まりません。Skillsなら、この対話の文脈が保持されたまま、TDDの手順だけが注入されます。

使い分けの判断基準はシンプルです。

- **コンテキストを共有したい** → Skills
- **コンテキストを独立させたい** → Subagents

**迷ったときの指針**: タスクの結果が「要約」で十分ならSubagent、結果だけでなく「過程」も重要ならSkillsです。エラー調査は「原因が分かればいい」のでSubagent。コードレビューは「なぜこの指摘をしたか」の文脈が後続の修正に影響するのでSkills。

より詳しい使い分けについては、atusyさんの記事「Claude Codeのユーザー設定プロンプトを使い分けてコンテキスト管理を最適化する」が参考になります。

## 利用可能なビルトインSkills

Skillsの概念は分かった。では、実際にどう使うのか。まずはAnthropicが提供しているビルトインSkillsから見てみましょう。

| Skill | 機能 |
| --- | --- |
| **[PowerPoint](https://d.hatena.ne.jp/keyword/PowerPoint) (pptx)** | プレゼンテーションの作成・編集・分析 |
| **[Excel](https://d.hatena.ne.jp/keyword/Excel) (xlsx)** | [スプレッドシート](https://d.hatena.ne.jp/keyword/%A5%B9%A5%D7%A5%EC%A5%C3%A5%C9%A5%B7%A1%BC%A5%C8) の作成・データ分析・チャート生成 |
| **Word (docx)** | ドキュメントの作成・編集・トラック変更 |
| **PDF (pdf)** | PDF生成・フォーム入力・マージ |

これはclaude.ai、Claude Code、Claude [API](https://d.hatena.ne.jp/keyword/API) で利用可能です。

## 基本的な使い方

### Claude Codeでの使い方

Claude Codeでは、Skillsは [ファイルシステム](https://d.hatena.ne.jp/keyword/%A5%D5%A5%A1%A5%A4%A5%EB%A5%B7%A5%B9%A5%C6%A5%E0) ベースで管理されます。

**配置場所：**

| タイプ | パス | スコープ |
| --- | --- | --- |
| 個人 | `~/.claude/skills/` | 全プロジェクト共通 |
| プロジェクト | `.claude/skills/` | 現在のプロジェクトのみ |

Skillを配置するだけで、Claude Codeが自動的に認識し、関連するタスクで使用します。

### APIでの使い方

```python
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {
                "type": "anthropic",
                "skill_id": "pptx",
                "version": "latest"
            }
        ]
    },
    messages=[{
        "role": "user",
        "content": "再生可能エネルギーについて5枚のプレゼンを作成して"
    }],
    tools=[{
        "type": "code_execution_20250825",
        "name": "code_execution"
    }]
)
```

ポイントは以下の通りです。

- `container.skills` でSkillを指定
- `type: "anthropic"` は公式Skill
- `tools` でcode\_executionを有効化（Skillsの実行に必須）
- Beta headersが必要

### claude.aiでの使い方

claude.aiでは、ビルトインSkillsは **デフォルトで有効** です。「 [PowerPoint](https://d.hatena.ne.jp/keyword/PowerPoint) を作って」と言えば、自動的に [PowerPoint](https://d.hatena.ne.jp/keyword/PowerPoint) Skillが起動します。カスタムSkillsは Settings > Features からZIPファイルでアップロードできます。

## カスタムSkillの作成

ここからが本番です。 **自分専用のSkillを作る** 方法を説明します。

### 基本構造

Skillの最小構成は `SKILL.md` ファイル1つだけです。

```markdown
---
name: my-custom-skill
description: このSkillが何をするか、いつ使うべきかを説明。
---

# My Custom Skill

## 指示
[具体的な手順をここに書く]

## 例
[実際の使用例]
```

**必須フィールド：**

- `name`: 小文字とハイフンのみ、64文字以内
- `description`: 何をするのか、いつ使うのかを説明。1024文字以内

### 実用的なSkill例

私が実際のプロジェクトで使っているSkillsを紹介します。

#### 例1: セキュリティレビュー

`.claude/skills/reviewing-security/SKILL.md`:

```markdown
---
name: reviewing-security
description: "OWASP API Security Top 10 (2023) と Rust セキュリティベストプラクティス。脆弱性検出。Use when: セキュリティ、脆弱性、OWASP、認証、認可、監査を依頼された時。"
---

# セキュリティレビュー

OWASP API Security Top 10 (2023) と Rust セキュリティベストプラクティスに基づくレビュースキル。

## OWASP チェック項目

| ID | リスク | チェック内容 |
|----|-------|-------------|
| API1 | BOLA | tenant_id 検証、file_id との組み合わせ検証 |
| API2 | Broken Auth | gRPC メタデータ認証 |
| API3 | Property | レスポンスの不要情報 |
| API4 | Resource | ファイルサイズ制限、ページネーション |

## Rust セキュリティ

| 項目 | 検索パターン |
|-----|-------------|
| 依存関係脆弱性 | \`cargo audit\` |
| unsafe コード | \`grep -rn "unsafe {" src/\` |
| ハードコード認証情報 | \`grep -rn "(password\|secret\|api_key)" src/\` |
```

`description` に「Use when:」を明記しているのがポイントです。これでClaudeが「セキュリティレビューして」と言われたときに確実に起動します。

#### 例2: ビルドとテスト

`.claude/skills/building-and-testing/SKILL.md`:

```markdown
---
name: building-and-testing
description: "Rustプロジェクトのビルドとテスト実行。フォーマットチェック、lint、ユニットテスト、ビルド確認を一括実行。Use when: ビルド、テスト、cargo test、チェック、確認を依頼された時。"
---

# ビルドとテスト

## 実行手順

1. フォーマットチェック: \`cargo fmt --check\`
2. Lint実行: \`cargo clippy -- -D warnings\`
3. ユニットテスト: \`cargo test --workspace\`
4. ビルド確認: \`cargo build --workspace\`

## 一括実行
```

cargo fmt --check && cargo clippy -- -D warnings && cargo test --workspace && cargo build --workspace

シンプルですが、これだけで「テストして」と言えば毎回同じ手順を実行してくれます。

#### 例3: リファレンス参照型（QAチェック）

[Progressive](https://d.hatena.ne.jp/keyword/Progressive) Disclosureを活用して、参照ファイルを分割する例です。職種ごとにリファレンスを分けることで、必要な情報だけを読み込みます。

```
.claude/skills/qa-check/
├── SKILL.md
└── reference/
    ├── backend.md      # Rustバックエンドのチェック項目
    ├── frontend.md     # フロントエンドのチェック項目
    └── infra.md        # インフラのチェック項目
```

`.claude/skills/qa-check/SKILL.md`:

```markdown
---
name: qa-check
description: "コードレビュー・QAチェック。職種別のベストプラクティスを適用。Use when: レビュー、QA、品質チェック、コードチェックを依頼された時。"
---

# QAチェック

職種別のリファレンスを参照してレビューを実施します。

## リファレンス

**Rust バックエンド** → See [reference/backend.md
](reference/backend.md)
**フロントエンド** → See [reference/frontend.md
](reference/frontend.md)
**インフラ** → See [reference/infra.md
](reference/infra.md)

## 実行手順

1. 変更ファイルの拡張子・パスから対象領域を判定
2. 該当するリファレンスを読み込む
3. チェック項目に従ってレビュー実施
4. 結果をCRITICAL/WARNING/INFOで分類して報告
```

`reference/backend.md` （一部抜粋）:

```markdown
# Rust バックエンド QAチェック項目

## エラーハンドリング
- [ ] unwrap() を本番コードで使用していないか
- [ ] Result型を適切に伝播しているか
- [ ] カスタムエラー型を定義しているか

## セキュリティ
- [ ] SQLインジェクション対策（sqlxのバインドパラメータ使用）
- [ ] 認証・認可のチェック漏れがないか
- [ ] 機密情報のログ出力がないか

## パフォーマンス
- [ ] N+1クエリが発生していないか
- [ ] 不要なclone()がないか
- [ ] async/awaitの適切な使用
```

「バックエンドのコードをレビューして」と言えば `backend.md` だけを読み込み、「インフラの設定をチェックして」と言えば `infra.md` だけを読み込みます。

### slash commandsとskillsの連携

Skillsは自動で起動しますが、明示的に呼び出したいときもあります。そういうときはslash commandsと組み合わせると便利です。

`.claude/skills/git-commit/SKILL.md`:

```markdown
---
name: git-commit
description: Stage meaningful diffs and create Conventional Commits with WHY-focused messages. Use when agent needs to commit code changes.
---

Execute \`/git:commit\` slash command
```

`.claude/commands/git/commit.md`:

```markdown
# Git Commit

変更をすべてコミットせずに、意味のある範囲でできるだけ小さくコミットする。
commit logにはwhyを残す。
...
```

こうすると、Claudeが「コミットすべきだな」と判断したら自動でSkillが起動し、ユーザーが明示的に `/git:commit` を呼んでも同じ挙動になります。 **自動と手動の両方に対応できる** 設計です。

## Skillsのベストプラクティス

**なぜベストプラクティスが重要なのか。** Skillsは「書けば動く」ものではありません。書き方によって、起動率、出力の安定性、 [トーク](https://d.hatena.ne.jp/keyword/%A5%C8%A1%BC%A5%AF) ン効率が大きく変わります。ベストプラクティスは、多くの試行錯誤から導き出されたパターンです。これを知らずに始めると、同じ失敗を繰り返すことになります。

### 1\. 簡潔に書く

コンテキストウィンドウは有限です。Claudeが既に知っていることを書く必要はありません。

**簡潔さが重要な理由は2つあります。** [トーク](https://d.hatena.ne.jp/keyword/%A5%C8%A1%BC%A5%AF) ンが増えると問題が起きます。1つはコスト。 [API](https://d.hatena.ne.jp/keyword/API) の場合、入力 [トーク](https://d.hatena.ne.jp/keyword/%A5%C8%A1%BC%A5%AF) ンに課金されるので、冗長なSkillはそのまま支出増になります。もう1つは「ノイズ」。LLMは与えられた情報を全て考慮しようとします。本質的でない説明が多いと、重要な指示が埋もれて、出力品質が下がります。

**悪い例（冗長）：**

```markdown
PDF (Portable Document Format) files are a common file format that contains
text, images, and other content. To extract text from a PDF, you'll need to
use a library. There are many libraries available for PDF processing...
```

**良い例（簡潔）：**

```markdown
## Extract PDF text

Use pdfplumber:
---
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
---
```

### 2\. 自由度を適切に設定

タスクの性質によって指示の具体性を変えます。

**自由度の設計が重要な理由は単純です。** LLMは指示が曖昧だと「創造的に解釈」します。コードレビューなら創造性は歓迎ですが、DB [マイグレーション](https://d.hatena.ne.jp/keyword/%A5%DE%A5%A4%A5%B0%A5%EC%A1%BC%A5%B7%A5%E7%A5%F3) で創造性を発揮されると困ります。タスクの「リスク」と「多様性の価値」を天秤にかけて、自由度を決めます。

**高自由度（テキスト指示）**: 複数のアプローチが有効な場合

```markdown
## Code Review
1. Analyze structure
2. Check for bugs
3. Suggest improvements
```

**低自由度（具体的 [スクリプト](https://d.hatena.ne.jp/keyword/%A5%B9%A5%AF%A5%EA%A5%D7%A5%C8) ）**: 操作がデリケートな場合。

```markdown
## Database Migration
Run exactly this script:
---
python scripts/migrate.py --verify --backup
---
Do not modify the command.
```

### 3\. フィードバックループを入れる

複雑なワークフローでは検証ステップを入れます。

**[フィードバックループ](https://d.hatena.ne.jp/keyword/%A5%D5%A5%A3%A1%BC%A5%C9%A5%D0%A5%C3%A5%AF%A5%EB%A1%BC%A5%D7) が必要な理由があります。** LLMは「確信を持って間違える」ことがあります。10ステップのワークフローを一気に実行させると、ステップ3でミスしても気づかずステップ10まで進みます。検証ステップを挟むことで、早期に問題を検出し、修正コストを下げられます。

```markdown
## Document Editing Workflow

1. Make edits to XML
2. **Validate immediately**: \`python validate.py\`
3. If validation fails:
   - Review error message
   - Fix issues
   - Validate again
4. **Only proceed when validation passes**
5. Pack the document
```

### 4\. ネストを深くしない

参照ファイルはSKILL.mdから1階層までに留めます。深すぎると部分的にしか読まれません。

**ネストが問題になる理由があります。** LLMは「参照先をどこまで読むか」を自分で判断します。A→B→C→Dとネストしていると、Bまで読んでCは読まない、という判断をすることがあります。重要な情報がDにあると、それが無視される。情報はフラットに配置して、確実に読まれるようにします。

**悪い例：**

```
SKILL.md → advanced.md → details.md → actual_info.md
```

**良い例：**

```
SKILL.md
├── advanced.md
├── reference.md
└── examples.md
```

## 100+の実戦投入可能なSkills

コミュニティが既に多くのSkillsを公開しています。

[github.com](https://github.com/ComposioHQ/awesome-claude-skills)

**人気カテゴリ：**

- **Document Processing**: docx, pdf, pptx, xlsx
- **Development & Code Tools**: [MCP](https://d.hatena.ne.jp/keyword/MCP) Builder, Webapp Testing, [Changelog](https://d.hatena.ne.jp/keyword/Changelog) Generator
- **Data & Analysis**: [CSV](https://d.hatena.ne.jp/keyword/CSV) Data Summarizer, Root Cause Tracing
- **Business & Marketing**: Lead Research Assistant, Competitive Ads Extractor
- **Creative & Media**: [Canvas](https://d.hatena.ne.jp/keyword/Canvas) Design, Theme Factory, Image Enhancer

## よくある失敗と対策

Skillsを作り始めると、最初は思い通りに動かないことが多いです。よくある失敗パターンとその対策をまとめました。

| 問題 | 原因 | 対策 |
| --- | --- | --- |
| Skillがトリガーされない | descriptionが曖昧 | 「何をするか」と「いつ使うか」を明記 |
| コンテキスト不足 | SKILL.mdに情報が足りない | 参照ファイルを追加 |
| [トーク](https://d.hatena.ne.jp/keyword/%A5%C8%A1%BC%A5%AF) ン消費が多すぎる | [Progressive](https://d.hatena.ne.jp/keyword/Progressive) Disclosureしてない | 情報を複数ファイルに分割 |
| 出力が不安定 | 自由度が高すぎる | 具体的なテンプレートや例を追加 |
| [スクリプト](https://d.hatena.ne.jp/keyword/%A5%B9%A5%AF%A5%EA%A5%D7%A5%C8) エラー | エラーハンドリングが甘い | [スクリプト](https://d.hatena.ne.jp/keyword/%A5%B9%A5%AF%A5%EA%A5%D7%A5%C8) 内で明示的にエラー処理 |

## セキュリティ上の注意点

Skillsはフルユーザー権限で実行されます。 **信頼できないソースのSkillsは使わないでください** 。

チェックすべきポイントは以下です。

1. **全ファイルを監査**: SKILL.md、 [スクリプト](https://d.hatena.ne.jp/keyword/%A5%B9%A5%AF%A5%EA%A5%D7%A5%C8) 、リソースをすべて確認
2. **外部接続に注意**: 外部URLへアクセスするSkillは特にリスクが高い
3. **自分で作る or 公式を使う**: 基本的にこの2択

## Skillsの限界と現実

ここまでSkillsの使い方やベストプラクティスを紹介してきました。しかし正直に言うと、Skillsは万能ではありません。実際にシステム化しようとすると、いくつかの困難にぶつかります。

**限界がある理由は明確です。** Skillsは「LLMに追加の情報を渡す」仕組みです。LLMの推論能力自体を向上させるわけではありません。どれだけ精緻なSkillを書いても、LLMが誤解することはあるし、予期しない振る舞いをすることもあります。これはLLMの本質的な不確実性に起因する問題で、Skillsでは解決できません。

**時間目安**: 最初のSkillを動かすまで1-2時間かかります。descriptionの調整、手順の修正、再テストのサイクルが必要だからです。2個目以降は30分程度になります。週3回以上使うタスクでないと元が取れないので、投資対効果を考えて作りましょう。

### 定義ファイル地獄

Skillsを整備していくと、管理すべきファイルが膨大になります。私のプロジェクトでは、こんな構造になりました。

```
.claude/skills/
├── building-and-testing/
├── running-integration-tests/
├── running-e2e-tests/
├── running-mutation-tests/
├── managing-docker-dev/
├── working-with-branches/
├── implementing-issues/
├── checking-pr/
├── reviewing-security/
├── reviewing-quality/
├── using-rust-patterns/
├── using-sqlx-patterns/
├── handling-errors/
└── ... (50個のSkillフォルダ)
```

**「地獄」になる理由は、** Skillsがコードと違って静的解析できないからです。どのSkillがどのタスクで起動するかは、実際に動かしてみないと分からない。コードなら「この関数はどこから呼ばれているか」を検索できますが、Skillsの時は「このSkillはいつ起動するか」をLLMの判断に委ねています。依存関係が [ブラックボックス](https://d.hatena.ne.jp/keyword/%A5%D6%A5%E9%A5%C3%A5%AF%A5%DC%A5%C3%A5%AF%A5%B9) になるのです。

50個のSkillがあると、どれがどの場面で起動するのか把握しきれなくなります。「なんでこのSkillが動いたんだ」という状況が発生します。結局、設計者がすべてのSkillの挙動を把握していないといけません。これは隠れたコストです。

### descriptionの試行錯誤

Skillが起動するかどうかは `description` の書き方次第です。しかし「どう書けば起動するか」は試してみないと分かりません。

**試行錯誤が必要な理由は、** LLMが「意味」で判断するからです。プログラムのように「この文字列が含まれていたら起動」という [決定論](https://d.hatena.ne.jp/keyword/%B7%E8%C4%EA%CF%C0) 的なルールではありません。「code review」と書いても、ユーザーが「PRを見て」と言ったらLLMが「これはcode reviewのことだ」と解釈するかどうかはLLM次第です。LLMの判断基準は私たちには見えません。

```yaml
# 起動しなかった例
description: Helps with code review.

# 起動した例
description: Performs code review. Use when reviewing pull requests, checking code quality, or before merging.
```

「いつ使うか」を明示的に書かないと、Claudeが「このSkillを使うべきだ」と判断してくれません。でも、どこまで具体的に書けばいいのか。書きすぎると他のタスクで起動しなくなるし、曖昧だと意図しない場面で起動します。この塩梅を見つけるのに時間がかかります。

**これはプロンプトエンジニアリングの本質的な難しさと同じです。** 「こう書けば必ずこう動く」という保証がない世界で、試行錯誤を通じて「だいたいこう動く」パターンを見つけていく。Skillsは設定ファイルの形をしていますが、実態はプロンプトエンジニアリングです。

### デバッグの難しさ

「なぜこのSkillが起動しなかったのか」を知る手段が限られています。Claude Codeは内部でどのSkillを候補として検討し、なぜそれを選んだか（選ばなかったか）を教えてくれません。

**[デバッグ](https://d.hatena.ne.jp/keyword/%A5%C7%A5%D0%A5%C3%A5%B0) が難しい理由は、** LLMの判断過程が外部から観察できないからです。プログラムなら [ブレークポイント](https://d.hatena.ne.jp/keyword/%A5%D6%A5%EC%A1%BC%A5%AF%A5%DD%A5%A4%A5%F3%A5%C8) を置いて変数の中身を確認できますが、LLMには「なぜこの判断をしたか」を聞く標準的なインターフェースがありません。ログを見ても「Skill Xを起動しました」という結果しか分からず、「なぜSkill YではなくXを選んだのか」は分かりません。

結果として、「起動しない → descriptionを変える → また試す」のループを繰り返すことになります。プログラムの [デバッグ](https://d.hatena.ne.jp/keyword/%A5%C7%A5%D0%A5%C3%A5%B0) と違って、再現性も低い。同じプロンプトでも起動したりしなかったりします。

**これはLLMベースのシステム全般の課題です。** Skillsに限った話ではありません。LLMの判断を制御したいなら、その不確実性と付き合う覚悟が必要です。

### Skill同士の競合

複数のSkillが似たようなdescriptionを持っていると、どちらが選ばれるか予測できません。

**競合が起きる理由は、** Skillの選択がLLMの「意味的な類似度判断」に依存しているからです。プログラムなら「優先度」を数値で指定できますが、Skillsにはそういう明示的な優先度設定がありません。LLMが「どちらがより適切か」を毎回判断しますが、その判断基準はコンテキスト依存で変わります。

```yaml
# Skill A
description: Reviews code for security issues.

# Skill B
description: Performs security audit on codebase.
```

「セキュリティチェックして」と言ったとき、AとBのどちらが起動するか。両方起動することもあります。Skillが増えるほど、こういう競合が起きやすくなります。

**対策としては、Skillの責務を明確に分離するしかありません。** 「security issues」と「security audit」が重複しているなら、片方を削除するか、descriptionで「Use when: PRの差分をレビューするとき」vs「Use when: プロジェクト全体を監査するとき」のように用途を分けます。これは設計段階で意識する必要があります。

## 「作る、試す、正す」で育てる

ここまで限界をいくつも挙げてきました。descriptionの試行錯誤、 [デバッグ](https://d.hatena.ne.jp/keyword/%A5%C7%A5%D0%A5%C3%A5%B0) の難しさ、Skill同士の競合。これだけ聞くと「やっぱり使わない方がいいのでは」と感じるだろう。しかし、限界があるからといって諦める必要はありません。

ここで参考になるのが、市谷聡啓氏の『作る、試す、正す。 [アジャイル](https://d.hatena.ne.jp/keyword/%A5%A2%A5%B8%A5%E3%A5%A4%A5%EB) なモノづくりのための全体戦略』です。

この本の核心は、 **「正しさ」を探すのではなく、「正しくなる状況」をつくる** というアプローチです。私たちの仕事は「正しいSkillを作る」ことではない。 **「ソフトウェアが正しくなっていく状況」をSkillで設計する** ことです。つまり、Skillの完成度を追い求めるのではなく、 **適切なタイミングでSkillが発動し、結果としてソフトウェアが正しい方向に進む** ——その「状況」を整えることが本質です。

```
作る → 試す → 正す → 作る → 試す → 正す → ...
```
1. **作る**: 最小限のSKILL.mdを書く
2. **試す**: 実際に使ってみて、期待通りに動くか確認する
3. **正す**: 動かなかった部分を修正し、descriptionを調整する

「課題を言葉で確認するだけでは分かった気になる」と市谷氏は指摘しています。Skillsも同様で、頭の中で設計を完璧にしようとしても限界があります。実際に動かしてみて初めて、「このdescriptionでは起動しない」「この手順では不十分」という発見が得られます。

私も最初のSkillは散々でした。descriptionが曖昧すぎて起動しない、手順が抽象的すぎて出力がブレる。でも何度か直していくうちに、「こう書けば確実に起動する」「この粒度で手順を書けば安定する」という感覚が掴めてきました。

**Skillsの価値は「完成品」ではなく「育てるプロセス」にあります。** descriptionの試行錯誤を通じて、私たちはLLMの「判断基準」を逆算的に学んでいる。Skillsは単なる設定ファイルではなく、LLMの振る舞いを観察し理解するための実験装置でもあるのです。

## まとめ

Agent Skillsは、 **LLMのステートレスな制約を回避し、専門知識を必要な時に注入する** 仕組みです。今まで紹介してきた設定（CLAUDE.md、commands、Hooks、Subagents）と組み合わせれば、Claude Codeの使い勝手は大きく変わります。

- **CLAUDE.md**: プロジェクトの文脈
- **commands**: 手動ショートカット
- **Hooks**: 自動実行
- **Subagents**: 専門家の自動呼び出し
- **Skills**: 専門知識の注入 ← NEW

これらの設定を組み合わせることで、Claude Codeは単なる [AIアシスタント](https://d.hatena.ne.jp/keyword/AI%A5%A2%A5%B7%A5%B9%A5%BF%A5%F3%A5%C8) から、チームの一員のように振る舞うツールへと変わります。

### Skillsが示唆するAIエンジニアリングの未来

では、この変化は何を意味するのか。Skillsが示唆するのは、 **「AIエージェントの制御は、プロンプトではなくワークフローで行う時代になった」** ということです。

従来のLLM活用は「良いプロンプトを書く」スキルが中心でした。しかしSkillsの登場で、 [パラダイム](https://d.hatena.ne.jp/keyword/%A5%D1%A5%E9%A5%C0%A5%A4%A5%E0) が変わりました。これからのAIエンジニアリングは、「LLMにどう推論させるか」ではなく、 **「LLMの推論をどう制約し、どう組織の資産として蓄積するか」** が問われます。

[暗黙知](https://d.hatena.ne.jp/keyword/%B0%C5%CC%DB%C3%CE) として個人の頭の中にあったワークフローが、SKILL.mdという明示的なドキュメントになる。これはチーム全体で共有・改善できる「組織の資産」になります。Skillsは単なる便利ツールではなく、 **ワークフローの [形式知](https://d.hatena.ne.jp/keyword/%B7%C1%BC%B0%C3%CE) 化** を促す仕組みでもあるのです。

万能ではありません。descriptionの試行錯誤は避けられないし、Skillが増えると管理コストも上がります。でも「作る、試す、正す」のサイクルを回せば、確実に生産性は上がります。

Claude Codeが雑魚なんじゃない、設定してないだけ。設定すればちゃんと動いてくれます。

## 今日から試せること

記事を読んで「面白そう」と思ったら、まずこれを試してみてください。

**1\. ビルトインSkillsを体験する（1分）**

claude.aiで「 [PowerPoint](https://d.hatena.ne.jp/keyword/PowerPoint) で自己紹介スライドを作って」と言ってみてください。Skillsが自動で起動して、プロ級のスライドが生成されます。

**2\. カスタムSkillの最小構成を作る（5分）**

```sh
mkdir -p ~/.claude/skills/hello-skill
```

`~/.claude/skills/hello-skill/SKILL.md` を作成します。

```markdown
---
name: hello-skill
description: Says hello in a fun way. Use when user asks for a greeting.
---

# Hello Skill

When asked to greet, respond with a creative and fun greeting.
Include an emoji and a short motivational message.
```

Claude Codeを再起動して「挨拶して」と言ってみてください。Skillが起動するはずです。

**3\. 既存のSkillsを眺める（10分）**

[awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) で、他の人が作ったSkillsを見てみてください。SKILL.mdの書き方の参考になります。

## 参考資料

- [Agent Skills - Anthropic Engineering Blog](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Agent Skills Overview - Claude Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Agent Skills Best Practices - Claude Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Using Skills with the API - Claude Docs](https://platform.claude.com/docs/en/build-with-claude/skills-guide)
- [awesome-claude-skills - ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills)
- [Claude Skills Cookbook](https://github.com/anthropics/claude-cookbooks/tree/main/skills)
- [Claude Codeのユーザー設定プロンプトを使い分けてコンテキスト管理を最適化する - atusy](https://blog.atusy.net/2025/12/15/claude-code-user-config-prompts/)
- [Claude Skillsとは何か - r\_kaga](https://zenn.dev/r_kaga/articles/810cc2e8326ca5)
- [振る舞い駆動開発（BDD）とは？ - HQW!](https://www.veriserve.co.jp/helloqualityworld/media/20251008001/)
- [作る、試す、正す。 - 市谷聡啓](https://bnn.co.jp/products/9784802513296)
- [Claude Skillsとは何なのか？](https://blog.lai.so/claude-skills/)
- [Use Agent Skills in VS Code](https://code.visualstudio.com/docs/copilot/customization/agent-skills)

[« 生成AI時代のMarp によるスライド環境の構…](https://syu-m-5151.hatenablog.com/entry/2025/12/19/183148) [「自分の環境では動く」から解放される Ni… »](https://syu-m-5151.hatenablog.com/entry/2025/12/18/111500)
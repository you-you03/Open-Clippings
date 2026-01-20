---
title: Claude Code 逆引きコマンド事典
source: https://zenn.dev/ml_bear/articles/84e92429698177
author:
- '[[Zenn]]'
published: 2025-06-23
created: 2025-06-23
description: null
tags:
- clippings
- cursor
- ai
- プロダクト
- ブランディング
---
103

55[tech](https://zenn.dev/tech-or-idea)

## これは何？

「Claude CodeのXXXで困った時どうする？」という逆引き一問一答形式でまとめたClaude Codeのコマンド集です。

僕は普段から説明書を読まないタイプ(爆)で、Claude CodeもBest Practiceを斜め読みした程度で使ってたのですが、ある時 `claude -r` コマンドを知って「そんな便利なコマンドあるのか！」と驚愕しました笑。

ちゃんと説明書読まないとなぁと反省し、メモをとりながらClaude公式ドキュメント(+多少の入門記事)を読み直したので、メモをまとめて公開してみます。とはいえ、単なるコマンド一覧では「過去の僕」は読まないかなと思ったので笑、逆引き一問一答形式にしています。

内容は2025年6月23日現在では正しいはずですが、界隈の速さを考えると一瞬で陳腐化すると思います。動かない場合は公式ドキュメントを参照していただけると幸いです。また、明らかに間違っているところがあればTwitterなどでご指摘いただけますと助かります。

#### 注意点

本記事ではClaude Codeのはじめかた (インストール方法など) については触れません。Classmethodさんの記事が非常に参考になったのでそちらをご覧いただくことをおすすめします😇

それでは以下にコマンド集をまとめていきます。

## 基本コマンド

#### Claude Code と仕事するぞ！

- `claude`
- VS Code や Cursor の拡張が入ってたら "Run Claude Code" ボタンでもいいですね。
	- 拡張は初回の `claude` 実行でインストールされるはずです
	- 入ってなかったらこの記事とかを参考に解決されるといいと思います

![](https://storage.googleapis.com/zenn-user-upload/15c6d54efb68-20250622.png)  
*Run Claude Code = 右上のAnthropicロゴ*

#### Claude Codeを間違って閉じてしまった！話を続けたい！

- `claude -c` (`claude --continue`) で最新の会話に戻って続けられます。
- 会話履歴はローカルマシンに保存される\[6\]のでマシンをまたいでcontinueできないことには注意が必要です

#### X日前に会話してた作業の続きをしたい。でももうターミナル閉じちゃってる。

- `claude -r` (`claude --resume`) で過去の会話スレッドを選んで入れます。
	- `claude` で立ち上げてから `/resume` でも動作します (なぜか `/continue` はない？)
- `-c` と同様にマシンをまたいで resume できないので注意が必要です。

#### Claude Codeを開かずに単発で質問したい

- `claude -p "{message}"` で質問が可能です。
	- 例: `claude -p "僕がaddしたファイル見てcommitメッセージ作って"`
- (遅いし何やってるか分からないから個人的にはほぼ使ってません😅笑)

#### 改行できない！

(環境依存で色々変わるのでClaude Codeが言っている内容を見ていただけると良いかと思います)

- `\ のあとに Enter` もしくは `Ctrl+j` です。
- Macだと `option+Enter` でも改行できます
- `/terminal-setup` コマンドを打ってターミナルを再起動すると `Shift+Enter` でも改行できるようになります
	- Cursorのkeybindingsには `Shift+Enter` が入っているらしく特に何もせずに `Shift+Enter` で改行できるかなと思います

#### 利用可能なコマンド一覧見たい

- `/help` で見れます

#### Claude Code で使われているモデルが分からない

- `/model` で確認可能です

![](https://storage.googleapis.com/zenn-user-upload/da438ce75478-20250621.png)

- Maxプランの例
	- デフォルトでは使用制限の半分までOpusを使ったあと、Sonnet利用に切り替わります。
	- 使用制限の限界までOpusを使いたい場合は `Opus` を選択するといいです。(その代わり Max x5 プランだとすぐに上限くると思います)

#### Cursor みたいにファイル渡して質問したい

- `@` をつけてファイルを指定して渡せます
- とはいえ Claude Code は賢いので `@` つけずにファイル名を言って質問するだけでも、よしなにファイル検索してうまく処理してくれることが多いです。

#### Claude Code でシェルコマンド打つのどうやるの？

- `!` を打てばbashモードになるので `cd` とか打てます
- Claude Code は賢いのでbashモードにしなくてもシェルコマンド打てば考えてからコマンド実行してくれますが、まぁまぁ遅いので`!`を打ってbashモードにすることをおすすめします。

## 会話制御

#### Claudeが頓珍漢なことしてるからとりあえず止めたい

- `ESC` で止まります

#### 話がこんがらがってきた！X個前の会話の位置に戻りたい

- `ESC` 2回連打で任意の会話の位置に戻れます
- ただしファイル編集履歴は戻らないので、こまめにコミットさせるのが吉です。
	- (CursorのAgentだとcheckpointに戻ってくれるのでその機能早く追加してほしい)

#### もうだめだ、全部リセットして最初から話したい。

- `/clear` で会話履歴全部消せます

#### Claudeが実行した結果が隠れてて見えない

- `Ctrl+r` で展開されます

#### わざわざ展開するのだるい、Claudeが実行した結果はいつも全部見せてほしい。

- `/config` コマンドで設定画面に入って `Verbose output` を `true` にすると良いです。
- もしくは `claude --verbose` で立ち上げるといいです
- とはいえファイル編集のdiffとかも全部出てくるのでややうざいです。

#### Auto Edit ON モードにしたい

- `Shift+tab` でモードが切り替わります

#### Plan モードにしたい

- 上に同じく `Shift+tab` でモードが切り替わります

#### でかいファイル貼り付けるとフリーズしちゃう

- コンテンツをファイルに書き込んで `@` で呼ぶのが推奨とのこと \[3\]
	- `@` じゃなくてもClaudeに「XXXのファイル読んで」って言っても大体は大丈夫
- もしくはPipeで渡す `cat foo.txt | claude`

## 設定

#### Claude が git add -A するのがうざいから禁止したい

- `/permissions` で `Deny` に行ってルール設定できます。(逆に `Allow` もできます)
- `Bash(git add -A:*)` `Bash(git add --all:*)` とか設定すればいいです
	- 詳細は [公式](https://docs.anthropic.com/en/docs/claude-code/iam#configuring-permissions) へ

※ `/permissions` の設定をしてもコマンドの提案はしてくる。Claudeが実行しようとした時にブロックされるので、その結果を見て別の行動をとってくれる。

#### Claudeにファイル編集させたくないディレクトリがある

- これも同様に `/permissions` で `Deny` `Allow` でルール設定できます
- 例: `Edit(docs/*)`: docsディレクトリにあるファイルの編集を (禁止 | 許可) できます
- 同様に `Read(docs/*)` 設定で読み取り自体の制御もできます。

#### WEB検索するときにゴミみたいなサイトの内容を参考にして欲しくない

- これも `/permissions` で `Deny` でドメイン指定して排除できます
- 例: `WebFetch(domain:example.com)` example.com への Fetch を (禁止 | 許可) できます

#### (禁止|許可)したい行動が多い。いちいち /permissions とか打ってられない。

- `.claude/settings.json` を編集したら一気に設定できるよ。
- \[8\]に記載の例

```json
{
  "permissions": {
    "allow": [
      "Bash(npm run lint)",
      "Bash(npm run test:*)",
      "Read(~/.zshrc)"
    ],
    "deny": [
      "Bash(curl:*)"
    ]
  },
  ...
}
```

- `Deny` を有効活用されている方の例

#### 上記のような設定をチームで共有したい

- `.claude/settings.json` をレポジトリに入れて共有するといい

#### Claude Code がいちいち承認求めてくるのだるい、何もかも好きにやってほしい。

- `claude --dangerously-skip-permissions` で起動したらいいです
- 危険が危ない()のでからインターネットアクセスのないコンテナ内での使用を推奨
- (僕は使ったことない笑)

#### レポジトリに Claude Code GitHub Actions をインストールしたい

- `/install-github-app` で入れられます
	- 詳細は [公式](https://docs.anthropic.com/en/docs/claude-code/github-actions) へ
- Claude API Key が必要なので注意

#### カラーテーマ変えたい

- `/theme`

## メモリ・ルール管理

#### CLAUDE.mdってどうやって作るの？

- `/init` で作ってくれます
	- `/init 日本語で作って` で日本語で作ってくれるらしい (僕は常に英語で作ってる)
- もちろん自分で書いてもいいです

#### CLAUDE.md をどこに置くかとかのベストプラクティスってあるの？

- \[7\]には以下のような図が掲載されているので参考にするといいでしょう

![](https://storage.googleapis.com/zenn-user-upload/0bf6a283e1af-20250621.png)

#### CLAUDE.mdをいちいち開いてカスタムルール追記するのめんどい

- `#` を打ってルールを打てば覚えてくれるよ

#### CLAUDE.mdに他のファイルの内容をコピペするのがだるい

- CLAUDE.mdファイルに `@path/to/import` 構文で参照したいファイルをインポートできます。なので単純なコピペ不要です。
- 例

```
See @README.md for project overview and @package.json for
available npm commands for this project.

# Additional Instructions
#### git workflow @docs/git-instructions.md
...
```

- パスは相対パスと絶対パスの両方が使用できます。

#### インポートしたファイルがさらに他のファイルインポートしてたらどうなるの？

- 最大5ホップ先の参照まで再起的に読み込まれます\[7\]

#### インポートさせまくったら今使ってるClaudeが参照してるメモリファイルがどれかわからなくなった

- `/memory` で確認可能です

![](https://storage.googleapis.com/zenn-user-upload/e526d633706e-20250621.png)

## 画像の扱い

#### Claudeに画像見せたい

- 以下3通りが手軽です
	- スクショがクリップボードにある状態で `Ctrl+V` で貼付ける
		- `cmd+v` じゃないから注意
	- `@` を使って画像のファイルパスを指定する
	- MCPツール与えてClaudeにブラウザのスクリーンショットを撮らせる
		- [Playwright MCP](https://github.com/microsoft/playwright-mcp)
		- [iOS シミュレーター MCP](https://github.com/joshuayoes/ios-simulator-mcp)
		- MCPの設定方法は後述

※1: 公式ドキュメントにはClaude Codeウィンドウにドラッグアンドドロップでも出来ると書いてあるが、CursorやVS Codeだと画像が表示されちゃうことが多い気がするので僕はあまり使ってない。

※2: Claude Code関係ないがMacだと画面スクショは以下のコマンド  
・ `Cmd+Shift+Ctrl+4`: 範囲を指定してクリップボードにスクショ  
・ `Cmd+Shift+Ctrl+3`: 画面全体を (以下同文)

## Git操作

#### branch を作ってほしい etc,

- 前提として Claude Code はGit操作に慣れてます
- 「ブランチ作って」って言ったら作ってくれます
- 特によく使う以下3つの操作は単語を打つだけで何するべきか考えてやってくれます
	- `commit`
	- `push`
	- `pr`
- gh CLI入れておくとスムーズです
	- commitしてpushしてPR作らせるぐらいなら、 `gh` なくても全然大丈夫です😇
\`gh\` CLI インストール方法

#### 自分で作業したけどcommit面倒くさいからClaude Codeにやらせたい

- `claude commit` で起動即commitしてくれます

## Custom slash commands

#### Claude CodeにIssueの解決してほしい。でも毎回いろいろ説明するPrompt打つのがだるい。

- Custom slash command を作るといい。
- そもそも Custom slash command とは？
	- `~/.claude/commands/{コマンド名}.md` に指示書くと `/{コマンド名}` で実行できるようになる。これを Custom slash command と呼んでいる。
		- 例: `~/.claude/commands/hoge.md` → `/hoge`
		- 場所は `/{プロジェクトのルートディレクトリ}/.claude/commands/{コマンド名}.md` でも可
		- 注意
			- ドキュメントには `/user:hoge` と説明しているものがあるが古いので注意
	- Custom slash command には `$ARGUMENTS` を設定でき、コマンドの引数を代入することができる。
- Custom slash command を活用したIssue解決指示例
	- 以下のようなプロンプトを `~/.claude/commands/fix-github-issue.md` に書く
	- `/fix-github-issue 1234` を実行

```
以下の手順に従って、GitHub issue #$ARGUMENTS を解決してください

以下のステップに従ってください：
1. \`gh issue view\`を使用してissueの詳細を取得する
2. issueに記載されている問題を理解する
3. 関連するファイルをコードベースから検索する
4. issueを修正するために必要な変更を実装する
5. 修正を検証するためのテストを作成し実行する
6. コードがlintとtype checkをpassすることを確認する
7. 丁寧な説明と共にコミットメッセージを作成する
8. プッシュしてPRを作成する

GitHubに関連するすべてのタスクには、GitHub CLI（\`gh\`）を使用してください。
```

- `$ARGUMENTS` は1個しか入れられないの？
	- 2025年6月時点では1個だけ
	- `$ARGUMENTS` を分割して扱わせる方法もあるらしい
		- どれくらい安定して動くのかは知らない😅
- もっと詳しい方法は [公式](https://docs.anthropic.com/en/docs/claude-code/slash-commands#custom-slash-commands) を参照

## MCP

#### Playwright MCPを設定して、Claude Codeにスクショを撮らせて実装を自己改善させたい。

(MCPの設定は [冒頭で紹介したClassmethodさんの記事](https://dev.classmethod.jp/articles/get-started-claude-code-2nd/#mcp%25E3%2582%25B5%25E3%2583%25BC%25E3%2583%2590%25E3%2583%25BC%25E3%2582%2592%25E8%25BF%25BD%25E5%258A%25A0%25E3%2581%2599%25E3%2582%258B) に詳しいですが、本記事でも少しだけ触れておきます。)

- `.mcp.json` を設定しましょう。以下はPlaywright MCPを設定する例です。(`.mcp.json` を設定する以外にも色々方法はあります / 公式やクラメソさん記事を見てね)

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
    }
  }
}
```

- `.mcp.json` が設定されているプロジェクトで Claude Code を起動すると、MCPを実行していいかどうかを聞かれます。

![](https://storage.googleapis.com/zenn-user-upload/807a0fbe54a5-20250621.png)

- `Tool use` の確認が出てくればうまくMCPを使えている証拠です

![](https://storage.googleapis.com/zenn-user-upload/5f2bf82f6d49-20250621.png)

![](https://storage.googleapis.com/zenn-user-upload/1a2c4851bc66-20250621.png)

#### MCPの権限を管理したい

- `/permissions` や `claude/settings.json` を利用して `Deny` や `Allow` しましょう
- 構文は `/mcp__<server-name>__<prompt-name>` です
- Playwright の例だと以下のようになります

#### MCPの機能を自分でも自由に使いたい

- 多くのMCPはコマンドを自分でも使えます
- 以下の方法で使い方を調べて使ってみましょう
	- `/mcp` でサーバー一覧を出す  
		![](https://storage.googleapis.com/zenn-user-upload/e24e4f939ecf-20250621.png)
	- `View tools`  
		![](https://storage.googleapis.com/zenn-user-upload/4e51010c7243-20250621.png)
	- 好きなツールを選んで中を見るとコマンドを見れます  
		![](https://storage.googleapis.com/zenn-user-upload/04da26f33127-20250621.png)  
		![](https://storage.googleapis.com/zenn-user-upload/3aeb7d2ad166-20250621.png)
- [Claude Code公式のMCP解説](https://docs.anthropic.com/en/docs/claude-code/mcp#use-mcp-prompts-as-slash-commands) にも詳しいのでそちらもどうぞ

![](https://storage.googleapis.com/zenn-user-upload/d9f87d39a934-20250621.png)

## 使い方のコツ

#### Claude Codeがうまくコード書いてくれない。コツを教えて。

- まず、最初に徹底的に計画させるのが大切
	- 計画がないとすぐに解決策のコーディングに取り掛かってしまう。(\[1\]に明記されている)
	- 計画の際には `Shift+Tab` で Plan Mode にしておくと良い。
- 次に、コードを書いて反復してコミットするように指示するのが大事。
	- Claude は、視覚的なモック、テストケース、その他の出力など、明確な反復目標がある場合に最も高いパフォーマンスを発揮するようになっている。(同じく\[1\]に明記)
	- なので
		- 画面作らせる時はスクショ撮らせたりするのが良い
		- TDDで最初にテスト書かせてそれに沿って開発させるのもいい
		- ただしテストを通すためのズルをしたり、テスト通ってないけど気にせず次の作業するねﾃﾍﾍﾟﾛ、とかほざくことも多いので僕も悩んでいる😅

#### 計画がイマイチだ。考えが浅い気がする。

- より深い思考を行う "拡張思考モード" を起動するための「合言葉」がある。難しい実装の計画を立てさせる際には合言葉を利用して"拡張思考モード"にしないと厳しいことが多い。
	- 嘘みたいだがベストプラクティスに明記されている笑
	- "think" < "think hard" < "think harder" < "ultrathink"
- 日本語だと "考えて" < "もっと考えて" < "しっかり考えて" らしい
	- 日本語以外にも多数の言語の「合言葉」をサポートしている笑
	- [この記事](https://zenn.dev/fbbp/articles/7aa9a46518a609) には日本語以外にも中国語、スペイン語の例も載っている。
	- 正直日本語のキーワードは覚えづらいので日本語でPrompt書いた後に英語の合言葉を書けばいいと思う。パターンマッチらしいので動くはず。(動いていると願いたい笑)
- 言うまでもないが思考の深さと待ち時間にはトレードオフがある
	- "think"から段階的に試すことが推奨されている
	- が、実務的には「あー、こりゃ全然ダメだわ」と思った段階で "ultrathink" を指示するので良いと思う。

#### 上手い質問の仕方がよくわからない、例を教えて。

- Claude Codeのベストプラクティス\[1\]曰く、「Claudeは意図を推測できますが、心を読むことはできません。具体的な内容を指示することであなたの期待値に沿った動きができるようになるでしょう。」(意訳) らしいです。
- ベストプラクティスに掲載されている例 (下図 / 筆者意訳) などを参照に、何をやってほしいか具体的に書くように心がけると良いでしょう。

![](https://storage.googleapis.com/zenn-user-upload/b349d36363ad-20250621.png)

#### みんなどんな質問してどんな使い方してるのか知りたい

- \[2\]の動画で紹介されていた質問例がわかりやすいので以下に意訳した上で引用する。
	- @RoutingController.py ってどんな感じで使ってるの？
	- 新しい @app/services/ValidationTemplateFactory をどうやって実装したらいいかな
	- recoverFromException が多くの引数を取るのはなんで？Git履歴を調べて答えて。
	- @src/index.ts API に if/else を追加することで、なぜ issue #18363 が解決できたのだろうか？
	- 新しい @api/ext/PreHooks.php API をリリースしたのはどのバージョンですか？
	- PR #9383 を見て、影響を受けたアプリのバージョンを慎重に確認して
	- 先週僕がリリースしたものを教えて

#### Claude Codeにたくさん修正をしてほしいが全部やらずに忘れちゃう。なんとかしたい。

- 作業用のメモを作成させて、消し込みながら作業させると良い。
- 大量のlintを行わせる例
	- まずClaudeに lint コマンドを実行させる
	- その結果を何らかのファイルに保存させる
	- その後に、Claude Codeにリストを消し込みつつ作業してもらう
	- こうすることで Claude Code は自分がやってない場所を把握し、上手に処理することができる。

#### Claude Code を並行して実行したい

- Git worktrees を使うのがモダンらしい
- 正直僕は使ってないので [公式](https://docs.anthropic.com/en/docs/claude-code/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees) などを参照してほしい😅

## 参考文献

主な参考文献をあげておきます。Claude公式ドキュメントは他にも色々参照した気がするので、気になる点があれば一通り読んでみることをおすすめします。(日本語版には英語版ならあるドキュメントがないこともあるので、ChromeのGoogle翻訳拡張とかで英語版を翻訳して読むのがいいと思います)

1. [Claude Code: Best practices for agentic coding](https://www.anthropic.com/engineering/claude-code-best-practices)
2. [Mastering Claude Code in 30 minutes](https://www.youtube.com/watch?v=6eBSHbLKuN0)
3. [Set up Claude Code](https://docs.anthropic.com/en/docs/claude-code/setup)
4. [Claude: CLI reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference)
5. [Claude: Interactive mode](https://docs.anthropic.com/en/docs/claude-code/interactive-mode)
6. [Claude: Common workflows](https://docs.anthropic.com/en/docs/claude-code/common-workflows#resume-previous-conversations)
7. [Claude: Manage Claude's memory](https://docs.anthropic.com/en/docs/claude-code/memory)
8. [Claude: Settings](https://docs.anthropic.com/en/docs/claude-code/settings)
9. [Claude: Model Context Protocol (MCP)](https://docs.anthropic.com/en/docs/claude-code/mcp)
10. [Claude Code完全攻略Wiki](https://zenn.dev/fbbp/articles/7aa9a46518a609)

103

55

この記事に贈られたバッジ

![Thank you](https://static.zenn.studio/images/badges/paid/badge-frame-3.svg)

103

55
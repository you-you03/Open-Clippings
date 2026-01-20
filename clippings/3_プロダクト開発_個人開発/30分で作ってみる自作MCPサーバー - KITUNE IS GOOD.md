---
title: "30分で作ってみる自作MCPサーバー - KITUNE IS GOOD"
source: "https://sori883.dev/posts/claude_self_made_mcp_server/"
author:
  - ""
published: 
created: 2025-09-03
description: "30分で簡単なMCPサーバーをざっくり作ってClaude Desktopで実行してみる"
tags: ["clippings", "個人開発", "プロダクト", "ai"]
image: "assets/ogp.png"
---
はじめに
----

遅ればせながら..MCPサーバーのキャッチアップをはじめまして、ざっくり理解するために作ってみました。  
今回は、プロンプトに入力されたURLを元にWebサイトから本文を抽出し、Markdownで返すMCPサーバーを作ってみようと思います。

MCPとは
-----

MCP（Model Context Protocol）は、アプリケーションがLLMにコンテキストを提供する方法を標準化するオープンプロトコルです。  
以下の構成要素があります。

* MCPホスト: Claude Desktop、IDE、または MCPを介してデータにアクセスする AI ツールなどのプログラム
* MCPクライアント: サーバーとの1:1接続を維持するクライアント（一般的にはMCPホストに内包）
* MCPサーバー: 標準化されたモデルコンキテストプロトコルを通じて特定の機能を公開する軽量プログラム
* ローカルデータソース: MCPサーバーが安全にアクセスできるコンピューターのファイル、データベース、サービス
* リモートサービス: MCPサーバーが接続できるインターネット経由 (API 経由など) で利用可能な外部システム

[![MCPのアーキテクチャ](/posts/claude_self_made_mcp_server/mcp_architecture_1.webp)](/posts/claude_self_made_mcp_server/mcp_architecture_1.webp)

ざっくり今回作る例で当てはめるとこうなります。

* MCPホストとMCPクライアント：Claude Desktop
* MCPサーバー：今回作成するNode.jsアプリ
* リモートサービス：Webサイト

また、通信規格はMCP Protocol(JSONRPC2.0)なので、MCPサーバーをざっくり言い換えると、JSON貰ってJSON返すだけのプログラムです。

1. Claude DesktopでURLが入力される
2. MCPサーバーがJSON形式でURLを受け取る
3. MCPサーバーがURLにfetchしてコンテンツを取得する
4. JSON形式で結果を返す

MCPサーバーを作ってみよう
--------------

今回はNode.jsアプリをTypescriptで作ります。

因みに成果物はこちらです。

### プロジェクト作成

まずは必要なものをインストールしていきます。

```
npm init
npm install @modelcontextprotocol/sdk @mozilla/readability html-to-md jsdom zod
npm install @types/jsdom @types/node typescript vitest --save-dev
```

次にpackages.jsonに以下を追加します。  
重複項目がある場合は上書きしておきましょう。

```
  "type": "module",
  "main": "src/server.ts",
  "bin": {
    "mcp-server": "build/index.ts"
  },
  "scripts": {
    "build": "tsc",
    "typecheck": "tsc --noEmit",
    "test": "vitest"
  },
  "files": [
    "build"
  ],
```

そして、以下のようなtsconfig.jsonを作成しておきます。

```
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "Node16",
    "moduleResolution": "Node16",
    "outDir": "./build",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
```

### MCPサーバーの作成

`src/server.ts`を作成し、MCPサーバーを実装していきます。  
はじめに`McpServer`を使用してserverを作成します。

```
export const server = new McpServer({
  name: "url2Markdown", 
  version: "0.1.0", 
});
```

次に`server`を使用して、ツールを実装します。

```
server.tool(
  "url2Markdown", 
  "url to markdown", 
  { url: z.string().url() }, 
  
  async ({ url }) => {
    
    const data = await fetch(url).then((res) => res.text());
    
    const md = getExtractContent(data);

   
    return {
      content: [{
        type: "text",
        text: md
      }],
    };
  }
);


function getExtractContent(htmlContent: string) {
  const doc = new JSDOM(htmlContent);
  const article = new Readability(doc.window.document).parse();
  if (!article) {
    throw new Error("Article not found");
  }
  
  
  return html2md(article.content!);
}
```

最後にmain関数を定義し、MCPサーバーを起動するようにします。

```
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  
  console.error("MCP Server running on stdio");
}
 
main().catch((error) => {
  console.error("Fatal error in main():", error);
  process.exit(1);
});
```

この状態で、`npm run build`を実行することでビルドされるはずです。

Claude Desktopに導入してみる
---------------------

下記を参考に開発者モードを有効にして`claude_desktop_config.json`を開きます。

因みにWindowsは左上のハンバーガーボタンを左クリックです。  
[![windowの開発者メニューの場所](/posts/claude_self_made_mcp_server/mcp_calude_desktop_2.webp)](/posts/claude_self_made_mcp_server/mcp_calude_desktop_2.webp)

`claude_desktop_config.json`を以下の通り編集します。  
MACとWindowsでパスの指定方法が違うのでご注意ください。

```
{
  "mcpServers": {
    "url2Markdown": {
      "command": "node",
      "args": [
        "C:\\<ビルドしたserver.jsへのパス>\\mcp-server\\build\\server.js"
      ]
    }
  }
}
```

編集後にClaude Desktopプロセスを再起動するとMCPツールボタンが表示されており、有効化されているMCPサーバー数が表示されているはず。  
画像だと「1」の部分  
[![Claude DesktopでMCPサーバー有効確認](/posts/claude_self_made_mcp_server/mcp_calude_desktop_3.webp)](/posts/claude_self_made_mcp_server/mcp_calude_desktop_3.webp)

ボタンをクリックすると作成した「url2Markdown」が利用可能になっているはずです。  
[![Claude DesktopでMCPサーバー詳細確認](/posts/claude_self_made_mcp_server/mcp_calude_desktop_4.webp)](/posts/claude_self_made_mcp_server/mcp_calude_desktop_4.webp)

試しにURLを与えて、文章を抜き出して貰いました。イイ感じ動いてますね～。
[![Claude DesktopでMCPサーバー詳細確認](/posts/claude_self_made_mcp_server/mcp_calude_desktop_5.webp)](/posts/claude_self_made_mcp_server/mcp_calude_desktop_5.webp)

あとがき
----

MCPサーバーなる名前で小難しそうなイメージですが、実際にはJsonRPCで1ファイルから簡単に作り始められるものなんですね～。  
MCPサーバーには今回実装したTools以外にもResourcesやPrompts等の種類があるようです。  
<https://modelcontextprotocol.io/docs/concepts/architecture>

大きめのMCPサーバー実装も何となく処理分かってると読みやすくなりそうですね。やっぱり手を動かすのは大切。

参考
--

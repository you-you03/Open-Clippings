---
title: "え？本買ってるの？？もっと良い方法あります。 - Qiita"
source: "https://qiita.com/itsuki_m/items/3fe9b1154e6e98b182e4"
author:
  - "[[Qiita]]"
published: 
created: 2025-09-03
description: "はじめに 日々の業務で新しい技術をキャッチアップするのは大変ですよね。特にライブラリやフレームワークの学習では、公式ドキュメントが丁寧でないこともあり、どこから手をつければいいか悩むことも多いと思います。 先日の会社の定例で紹介したTipsが好評だったので、その内容を共有..."
tags: ["clippings", "個人開発", "プロダクト", "ai"]
image: "assets/https%3A%2F%2Fqiita-user-contents.imgix.net%2Fhttps%253A%252F%252Fcdn.qiita.com%252Fassets%252Fpublic%252Farticle-ogp-background-afbab5eb44e0b055cce1258705637a91.png%3Fixlib%3Drb-4.jpg"
---
はじめに
----

日々の業務で新しい技術をキャッチアップするのは大変ですよね。特にライブラリやフレームワークの学習では、公式ドキュメントが丁寧でないこともあり、どこから手をつければいいか悩むことも多いと思います。

先日の会社の定例で紹介したTipsが好評だったので、その内容を共有します。

株式会社シンシアでは、実務未経験のエンジニアの方や学生エンジニアインターンを採用し一緒に働いています。  
※ シンシアにおける働き方の様子はこちら  
<https://www.wantedly.com/companies/xincere-inc/stories>

本記事では、「本を読むのが無駄」という主張ではなく、「本以外にも便利な学習手段がある」という視点でお話しします。

本の必要性
-----

各分野には「名著」と呼ばれる本が存在し、それらは基礎をしっかりと学ぶのに適しています。

しかし、ライブラリやフレームワークの学習ではどうでしょうか？

公式ドキュメントがしっかり整備されている場合もありますが、すべてのドキュメントが初心者に優しいわけではありません。とはいえ、「ドキュメントが分かりにくいからキャッチアップしない」という選択肢はありません。

そこで、本の代替手段として **ChatGPT を活用する方法** を紹介します。

ドキュメントをChatGPTに読ませ、ハンズオンを作らせる
-----------------------------

ライブラリやフレームワークの学習で、公式ドキュメントを読むのが苦痛に感じることはありませんか？ そんなときは、**ChatGPT にドキュメントを要約させ、簡単なハンズオンを作成させる** ことで、より実践的に学ぶことができます。

#### **具体的な方法**

1. **ドキュメントのURLをChatGPTに要約させる**

   ```
   URLのドキュメントを要約してください: [ドキュメントのURL]

   //必要であればGithubのREADMEのURL
   GithubのREADMEを要約してください : [GithubのURL]
   ```

[![スクリーンショット 2025-02-11 19.52.11.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3999339%2Ffaab5c5d-0d74-0113-86a4-16eea57bed57.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=df4950249f4dc90cd3cee9272208055e)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3999339%2Ffaab5c5d-0d74-0113-86a4-16eea57bed57.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=df4950249f4dc90cd3cee9272208055e)  
2. **ハンズオンを作成させる**

```
このライブラリの基本的な使い方を学ぶために、初心者向けのハンズオンを作成してください。
- 必要なセットアップ手順
- 簡単なサンプルコード
- よくあるエラーとその対処法
```

[![スクリーンショット 2025-02-11 19.56.23.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3999339%2F70cbaa44-a4ac-0493-1c57-7de17082cfe4.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=7442683e23de58fc11b261617d731d81)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3999339%2F70cbaa44-a4ac-0493-1c57-7de17082cfe4.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=7442683e23de58fc11b261617d731d81)

1. **実際に手を動かして学ぶ**
   * ChatGPT が作成したハンズオンを試しながら学習を進めることで、単にドキュメントを読むよりも理解が深まります。
   * 必要に応じて、ChatGPTに質問するのも有効です。

#### 難易度調整も可能

初心者向けとするとかなり簡単なハンズオンを作成できます。簡単すぎると感じたら、鬼ムズにすることもできるので、お好みに合わせて調整しましょう。  
[![スクリーンショット 2025-02-11 20.03.42.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3999339%2F876ed3fd-a4ac-e456-44dd-41c089268bd7.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=d8100b3e54fac621de87403e9c79eef3)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3999339%2F876ed3fd-a4ac-e456-44dd-41c089268bd7.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=d8100b3e54fac621de87403e9c79eef3)

まとめ
---

ライブラリやフレームワークの学習では、ChatGPTを活用したハンズオン作成により、効率よくキャッチアップできます。  
ただ単にChatGPTが生成するハンズオンは、どこを参照しているのか不明瞭になりがちですが、こちらで適切な読み物を用意することで、明確な流れのハンズオンを作成できます。

また、ChatGPTに資料を読ませる方法は他にも活用の幅がありそうです。これからの時代、AIの使いこなしが重要なスキルになりそうですね。

---
title: "欲望を渡して、AIにプロンプトを書いてもらう方法｜太田 賢一／Design Mgr"
source: "https://note.com/kenichiota0711/n/nf3a721bb493e"
author:
  - "[[太田 賢一／Design Mgr]]"
published: 2025-12-27
created: 2025-12-27
description: "プロンプトもAIに書いてもらおう。  なぜなら、AIを最も熟知しているのはAIだからです。「プロンプトを作成するためのプロンプト」をメタプロンプトといいます。  AIに「何をしてほしいか」だけでなく、「どう考えて、どう答えるべきか」という指示構造・思考プロセスをAI自身に設計・実行させる技術です。  ビジュアルデザイン生成におけるプロンプトをAIに書いてもらう。今回はそのプロセスを紹介します。         AIが書いたプロンプト  最終的にAIが書いたプロンプトがこちら  ## Role & ConceptCreated by a world-class art dire"
tags:
  - "clippings"
  - "ai"
  - "プロンプト"
  - "デザイン"
  - "メタプロンプト"
later: false
---
![見出し画像](https://assets.st-note.com/production/uploads/images/238919433/rectangle_large_type_2_9da01c92ba5cba6892462ab436258e52.jpeg?width=1280)

## 欲望を渡して、AIにプロンプトを書いてもらう方法

[太田 賢一／Design Mgr](https://note.com/kenichiota0711)

  

プロンプトもAIに書いてもらおう。

なぜなら、AIを最も熟知しているのはAIだからです。 **「プロンプトを作成するためのプロンプト」をメタプロンプトといいます。**

AIに「何をしてほしいか」だけでなく、「どう考えて、どう答えるべきか」という指示構造・思考プロセスをAI自身に設計・実行させる技術です。

ビジュアルデザイン生成におけるプロンプトをAIに書いてもらう。今回はそのプロセスを紹介します。

  

  

## AIが書いたプロンプト

最終的にAIが書いたプロンプトがこちら

```python
## Role & Concept
Created by a world-class art director. A highly experimental 16:9 graphic design visual exploring the fusion of "AI × Design".

## Art Style
A mix of raw Neo-Brutalism and high-fashion editorial collage. Influenced by radical avant-garde aesthetics.

## Elements & Typography
- **Main Typography:** "AI × Design" in a distorted, fragmented, and layered sans-serif.
- **Visual Components:** Abstract 3D rendered shapes, torn paper textures, and grainy black and white photography elements arranged in a dynamic, asymmetrical composition.

## Color Palette
High-contrast and unexpected: Electric blue, acid green, and metallic silver accents set against a raw, industrial concrete background.

## Texture & Finish
Gritty Risograph printing texture mixed with subtle digital noise. High-end editorial print aesthetic. 8k resolution, hyper-detailed tactile surface.
```

形式は、文章形式（Natural Prose）・構造化形式 （YAML / Markdown）どちらでも良いと思います。 **どのような形式であっても、"自分の理想に到達すること" がゴールです。**

![画像](https://assets.st-note.com/img/1766652075-qiOYdR81rDSxNz9gHvJsabXu.jpg?width=1200)

Neo Brutalism & High Fashion Editorial Style

  

  

## 欲望と役割をAIに渡す

このビジュアルを生成してもらう前に、まず以下の文章をAIに投げました。

> GeminiのImagenによるグラフィックデザインの画像生成を、プロフェッショナル且つとにかくかっこよくしたいです。世界で活躍する一流アートディレクターが創造するようなアートセンスが爆発しているビジュアルを生成するための思考やプロンプトを教えてください

ただの欲望です。恥ずかしながら言語化できていません。ですが、後半の「プロンプトを教えてください」という言葉から分かる通り、 **"プロンプトを書く" という役割をAIに渡しています。重要なのは、この方針策定です。**

制作プロセス  
1：方針 / 役割 / 欲望をAIに渡す  
2：AIがプロンプトを書く  
3：プロンプトを調整する  
4：AIが生成する（fixするまで）  
5：4を選び、完成

日々言語化に向き合っている私は、言葉の大切さを理解しています。ですが、1のタイミングにおける言語化は粗く雑なもので良いと思っています。「こうしたいんだけど、どうすればいいか分からない」という **"言葉にならない望み" をAIにぶつけてみましょう。** すべてはそこから始まります。

  

## AIが書いたプロンプトの調整をAIに依頼する

私の欲望を受理したAIはこのように提案してくれました。

「漠然とした指示では普通の画像しか出てきません。一流のセンスを引き出すためには、具体的で・感覚的で・少し挑発的な言葉をプロンプトに組み込む必要があります」 とのこと。そしてまず以下のプロンプトを書いてくれました。

```cpp
A highly experimental graphic design poster, curated by a world-class art director. The style is a mix of brutalism and high-fashion collage. Distorted typography that reads "CHAOS & ORDER" [または好きな言葉] is fragmented and layered over abstract 3D rendered shapes, torn paper textures, and grainy black and white photography elements. The color palette is unexpected: electric blue, acid green, and metallic silver accents on raw concrete background. The composition is dynamic and asymmetrical. Risograph printing texture. High-end editorial aesthetic.
```

さらにここから [**「ビジュアル表現を引き出す言葉」**](https://note.com/kenichiota0711/n/n71a6aea5d44c) を活用します。もし、AIが書いたプロンプトが望み通りのアウトプットを生成できなかった場合、"ディレクション" が必要となります。自分が描きたい世界観を引き出すための言葉を、AIに渡してあげるのです。

ディレクション例：「現在のプロンプトですが、アートテーマに "Ethereal" を融合してください」

  

## 美を追求する欲望

一度で望み通りのビジュアルが生成される場合もあれば、何度生成しても納得いかない場合もあります。AIデザインには "ランダム性" という特徴があるからです。

しかし、そもそもクリエイティブに正解はありません。自分の意図していなかったアウトプットが生成されることを、むしろポジティブに捉える姿勢も持ち合わせていたい。私はそう思います。

そして「納得いかない」という思考に至っているのは "審美眼" を持っているからこそです。 **「もっと美しくしたい** ─ **」その美を追求する欲望をAIに渡して、言語化を手伝ってもらいましょう。**

  

## まとめ

自分の内側から湧き立つ "欲望や理想" がなければ、AIを動かすスタートラインに立てないとも言えます。しかし、それは決して難しいことではありません。

純粋に素直な「こうなったらいいな」という感情さえあればいい。AIと少しずつ対話しながら、ときにAIとAIを対話させながら、"自分の願い" を再発見することを楽しみたい。

高度なプロンプトを考えるのではなく、まずは自分の中にある欲望をAIに話してみる。そこから始めてみましょう。

  

  

  

[![買うたび 抽選 ※条件・上限あり ＼note クリエイター感謝祭ポイントバックキャンペーン／最大全額もどってくる！ 12.1 月〜1.14 水 まで](https://assets.st-note.com/poc-image/manual/production/20271127_pointback_note_detail.jpg?width=620&dpr=2)](https://note.com/topic/campaign)

欲望を渡して、AIにプロンプトを書いてもらう方法｜太田 賢一／Design Mgr
---
title: "Googleの画像生成AI「Nano-banana」をめちゃくちゃ活用できるプロンプトとサンプル画像実例まとめ"
source: "https://gigazine.net/news/20250912-nano-banana-prompt-example-matome/"
author:
  - "[[GIGAZINE]]"
published: 2025-09-12
created: 2025-09-15
description: "Googleが2025年8月に公開した画像生成AI「Gemini 2.5 Flash Image(Nano Banana)」は、入力した画像の特徴を維持しながら編集することが得意で、無料ユーザーでも1日100枚まで画像を生成することが可能です。そんなNano Bananaで使えるプロンプトとその実例をまとめたGitHubのページが有志によって公開されていたので、いくつかピックアップしてみました。"
tags: [クリッピング, ai開発, 画像生成, プロンプト, google]
image: "https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/00.jpg"
---
[ソフトウェア](https://gigazine.net/news/C4/)

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/00_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/00.jpg)

  
Googleが2025年8月に公開した画像生成AI「 **[Gemini 2.5 Flash Image](https://gigazine.net/news/20250827-gemini-2-5-flash-image/) (Nano Banana)** 」は、入力した画像の特徴を維持しながら編集することが得意で、無料ユーザーでも **[1日100枚まで画像を生成することが可能](https://gigazine.net/news/20250908-google-gemini-usage-limits/)** です。そんなNano Bananaで使えるプロンプトとその実例をまとめたGitHubのページが有志によって公開されていたので、いくつかピックアップしてみました。  
  
**Awesome-Nano-Banana-images/README\_en.md at main · PicoTrex/Awesome-Nano-Banana-images · GitHub**  
**[https://github.com/PicoTrex/Awesome-Nano-Banana-images/blob/main/README\_en.md](https://github.com/PicoTrex/Awesome-Nano-Banana-images/blob/main/README_en.md)**  
  
**・目次**  
**[◆1：イラストをフィギュア化](https://gigazine.net/news/20250912-nano-banana-prompt-example-matome/#1)**  
**[◆2：異なる時代の自分の写真](https://gigazine.net/news/20250912-nano-banana-prompt-example-matome/#2)**  
**[◆3：クロスビュー画像の生成](https://gigazine.net/news/20250912-nano-banana-prompt-example-matome/#3)**  
**[◆4：カラーパレットを使った線画の着色](https://gigazine.net/news/20250912-nano-banana-prompt-example-matome/#4)**  
**[◆5：古い写真のカラー化](https://gigazine.net/news/20250912-nano-banana-prompt-example-matome/#5)**  
**[◆6：指定のコーディネートに着替えさせる](https://gigazine.net/news/20250912-nano-banana-prompt-example-matome/#6)**  
**[◆7：キャラクターのポーズ変更](https://gigazine.net/news/20250912-nano-banana-prompt-example-matome/#7)**  
**[◆8：線画からポーズを指定する](https://gigazine.net/news/20250912-nano-banana-prompt-example-matome/#8)**  
**[◆9：地図から立体的な建物のイラストへ](https://gigazine.net/news/20250912-nano-banana-prompt-example-matome/#9)**  
**[◆10：メイクの分析](https://gigazine.net/news/20250912-nano-banana-prompt-example-matome/#10)**  
**[◆11：複数のキャラクターポーズ生成](https://gigazine.net/news/20250912-nano-banana-prompt-example-matome/#11)**  
**[◆12：照明制御](https://gigazine.net/news/20250912-nano-banana-prompt-example-matome/#12)**  
**[◆13：被写体を抽出して透明なレイヤーに配置](https://gigazine.net/news/20250912-nano-banana-prompt-example-matome/#13)**  
**[◆14：アニメの巨大フィギュアを東京のど真ん中に置く](https://gigazine.net/news/20250912-nano-banana-prompt-example-matome/#14)**  
**[◆15：マンガスタイルへの変換](https://gigazine.net/news/20250912-nano-banana-prompt-example-matome/#15)**  
**[◆16：証明写真の作成](https://gigazine.net/news/20250912-nano-banana-prompt-example-matome/#16)**  
  
**◆1：イラストをフィギュア化**  
入力例  

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/01inputa-a_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/01inputa-a.jpg)

  
出力例  

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/01output-a_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/01output-a.jpg)

  
プロンプト  

```
turn this photo into a character figure. Behind it, place a box with the character's image printed on it, and a computer showing the Blender modeling process on its screen. In front of the box, add a round plastic base with the character figure standing on it. set the scene indoors if possible
```

  
**◆2：異なる時代の自分の写真**  
入力例  

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/02input_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/02input.jpg)

  
出力例  

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/02output_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/02output.jpg)

  
プロンプト  

```
Change the characer's style to [1970]'s classical [male] style Add [long curly] hair, [long mustache], change the background to the iconic [californian summer landscape] Don't change the character's face
```

  
注記：\[角括弧\]内のテキストを、希望する時代や詳細情報に変更してください。  
  
**◆3：クロスビュー画像の生成**  
入力例  

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/03input_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/03input.jpg)

  
出力例  

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/03output_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/03output.jpg)

  
プロンプト  

```
Convert the photo to a top-down view and mark the location of the photographer.
```

  
**◆4：カラーパレットを使った線画の着色**  
入力例  

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/04input_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/04input.jpg)

  
出力例  

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/04output_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/04output.jpg)

  
プロンプト  

```
Accurately use the color palette from Figure 2 to color the character in Figure 1
```

  
**◆5：古い写真のカラー化**  
入力例  

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/05input_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/05input.jpg)

  
出力例  

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/05output_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/05output.jpg)

  
プロンプト  

```
restore and colorize this photo.
```

  
**◆6：指定のコーディネートに着替えさせる**  
入力例  

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/06input_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/06input.jpg)

  
出力例  

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/06output_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/06output.jpg)

  
プロンプト  

```
Choose the person in Image 1 and dress them in all the clothing and accessories from Image 2. Shoot a series of realistic OOTD-style photos outdoors, using natural lighting, a stylish street style, and clear full-body shots. Keep the person's identity and pose from Image 1, but show the complete outfit and accessories from Image 2 in a cohesive, stylish way.
```

  
**◆7：キャラクターのポーズ変更**  
入力例  

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/07input_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/07input.jpg)

  
出力例  

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/07output_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/07output.jpg)

  
プロンプト  

```
Have the person in the picture look straight ahead
```

  
**◆8：線画からポーズを指定する**  
入力例  

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/08input_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/08input.jpg)

  
出力例  

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/08output_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/08output.jpg)

  
プロンプト  

```
Change the pose of the person in Figure 1 to that of Figure 2, and shoot in a professional studio
```

  
注記：線画と参考画像をアップロードする必要があります。  
  
**◆9：地図から立体的な建物のイラストへ**  
入力例  

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/09input_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/09input.jpg)

  
出力例  

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/09output_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/09output.jpg)

  
プロンプト  

```
Take this location and make the landmark an isometric image (building only), in the stvle of the game Theme Park
```

  
**◆10：メイクの分析**  
入力例  

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/10input_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/10input.jpg)

  
出力例  

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/10output_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/10output.jpg)

  
プロンプト  

```
Analyze this image. Use a red pen to mark areas that can be improved Analyze this image. Use a red pen to denote where you can improve
```

  
**◆11：複数のキャラクターポーズ生成**  
入力と出力例  

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/11output_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/11output.jpg)

  
プロンプト  

```
Please create a pose sheet for this illustration, making various poses!
```

  
**◆12：照明制御**  
入力と出力例  

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/12output_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/12output.jpg)

  
プロンプト  

```
Change the character from Image 1 to the lighting from Image 2, with dark areas as shadows
```

  
注記：入力では画像と同時に照明の参考画像をアップロードする必要があります。  
  
**◆13：被写体を抽出して透明なレイヤーに配置**  
入力例  

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/13input_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/13input.jpg)

  
出力例  

[![](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/13output_m.jpg)](https://i.gzn.jp/img/2025/09/12/nano-banana-prompt-example-matome/13output.jpg)

  
プロンプト  

```
extract the [samurai] and put transparent background
```

  
注記：\[角括弧\]内のテキストを、抽出したいオブジェクトに置き換えてください。  
  
**◆14：アニメの巨大フィギュアを東京のど真ん中に置く**  
入力例  

  
出力例  

  
プロンプト  

```
A realistic photographic work. A gigantic statue of this person has been placed in a square in the center of Tokyo, with people looking up at it.
```

  
**◆15：マンガスタイルへの変換**  
入力例  

  
出力例  

  
プロンプト  

```
Convert the input photo into a black-and-white manga-style line drawing.
```

  
**◆16：証明写真の作成**  
入力例  

  
出力例  

  
プロンプト  

```
Crop the head and create a 2-inch ID photo with:
  1. Blue background
  2. Professional business attire
  3. Frontal face
  4. Slight smile
```

この記事のタイトルとURLをコピーする

**・関連記事**  
**[Googleが無料の超高品質な画像編集AI「Gemini 2.5 Flash Image」をリリース、日本語で指示できて実写からアニメキャラへの変換も可能 - GIGAZINE](https://gigazine.net/news/20250827-gemini-2-5-flash-image)**  
  
**[Gemini 2.5 Flash Imageでイラストをプロンプト不要でフィギュア化できるイラストフィギュア化専用アプリを使ってみた - GIGAZINE](https://gigazine.net/news/20250903-nano-banana-figurized)**  
  
**[キャラクターを維持したまま別のシチュエーションに描き直せる画像編集AI「Qwen-Image-Edit」が登場、文字の描き直しや「被写体の回転」も可能 - GIGAZINE](https://gigazine.net/news/20250819-qwen-image-edit)**  
  
**[画像生成AI「Qwen-Image」登場、OpenAIやFlux超えの高品質画像を生成可能で「複数行の漢字」を自然に描写できる驚異的テキスト描画性能をアピール - GIGAZINE](https://gigazine.net/news/20250805-qwen-image-image-generation-ai)**  
  
**[ByteDanceが画像生成AI「Seedream 4.0」をリリース、4K解像度の画像を生成可能＆画像編集機能も備えてGoogleやOpenAIを一部テストで上回る - GIGAZINE](https://gigazine.net/news/20250911-seedream-4-bytedance-image-edit-generate)**

**・関連コンテンツ**

- [![](https://i.gzn.jp/img/2025/09/11/seedream-4-bytedance-image-edit-generate/00_m.png)](https://gigazine.net/news/20250911-seedream-4-bytedance-image-edit-generate/)
	[ByteDanceが画像生成AI「Seedream 4.0」をリリース、4K解像度の画像を生成可能＆画像編集機能も備えてGoogleやOpenAIを一部テストで上回る](https://gigazine.net/news/20250911-seedream-4-bytedance-image-edit-generate/)
- [![](https://i.gzn.jp/img/2024/03/06/layer-diffusion-generate-transparent-image/00_m.png)](https://gigazine.net/news/20240306-layer-diffusion-generate-transparent-image/)
	[立ち絵や合成素材に使える背景透過PNG画像を簡単に生成できる画像生成AI「Layer Diffusion」をローカルにインストールして使ってみた](https://gigazine.net/news/20240306-layer-diffusion-generate-transparent-image/)
- [![](https://i.gzn.jp/img/2023/04/04/adobe-firefly-midjourney/00_m.jpg)](https://gigazine.net/news/20230404-adobe-firefly-midjourney/)
	[ジェネレーティブAIの「Adobe Firefly」では「マリオ」「ピカチュウ」などの著作権で保護されたコンテンツが回避されるというのがよく分かる「Midjourney」との比較画像](https://gigazine.net/news/20230404-adobe-firefly-midjourney/)
- [![](https://i.gzn.jp/img/2008/05/20/moocolorfinder/Snap1.png)](https://gigazine.net/news/20080520_moocolorfinder/)
	[サイトで使われている色を調べる「mooColorFinder」](https://gigazine.net/news/20080520_moocolorfinder/)
- [![](https://i.gzn.jp/img/2022/10/14/stable-diffusion-prompt-generator/00_m.png)](https://gigazine.net/news/20221014-stable-diffusion-prompt-generator/)
	[画像生成AI「Stable Diffusion」に描かせたい内容を文章で伝えるだけで一発で何通りものプロンプト・呪文を簡単に自動作成できる「MagicPrompt」Stable Diffusion版](https://gigazine.net/news/20221014-stable-diffusion-prompt-generator/)
- [![](https://i.gzn.jp/img/2016/04/28/sketch-automatic-line-drawing/00_m.png)](https://gigazine.net/news/20160428-sketch-automatic-line-drawing/)
	[ラフ画へ自動的にペン入れして線画にする恐るべきニューラルネットワーク技術を早稲田大学の研究室が開発](https://gigazine.net/news/20160428-sketch-automatic-line-drawing/)
- [![](https://i.gzn.jp/img/2025/08/05/qwen-image-image-generation-ai/00_m.png)](https://gigazine.net/news/20250805-qwen-image-image-generation-ai/)
	[画像生成AI「Qwen-Image」登場、OpenAIやFlux超えの高品質画像を生成可能で「複数行の漢字」を自然に描写できる驚異的テキスト描画性能をアピール](https://gigazine.net/news/20250805-qwen-image-image-generation-ai/)
- [![](https://i.gzn.jp/img/2025/08/27/gemini-2-5-flash-image/00_m.png)](https://gigazine.net/news/20250827-gemini-2-5-flash-image/)
	[Googleが無料の超高品質な画像編集AI「Gemini 2.5 Flash Image」をリリース、日本語で指示できて実写からアニメキャラへの変換も可能](https://gigazine.net/news/20250827-gemini-2-5-flash-image/)

in [ソフトウェア](https://gigazine.net/news/C4/), [ネットサービス](https://gigazine.net/news/C5/), [ウェブアプリ](https://gigazine.net/news/C37/), Posted by log1i\_yk

You can read the machine translated English article **[A summary of prompts and sample images t…](https://gigazine.net/gsc_news/en/20250912-nano-banana-prompt-example-matome)**.
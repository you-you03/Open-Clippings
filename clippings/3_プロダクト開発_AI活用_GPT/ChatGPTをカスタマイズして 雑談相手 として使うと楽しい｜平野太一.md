---
title: "ChatGPTをカスタマイズして\"雑談相手\"として使うと楽しい｜平野太一"
source: "https://note.com/yriica/n/na2381041eda9"
author:
  - "[[note（ノート）]]"
published: 
created: 2025-09-03
description: "この前、Xで見かけたポストを元に、ChatGPTをカスタマイズしてみたらチャットが楽しくなったので、おすそ分けします。モデルは「GPT-4o」がちょうどいいです。「o3-mini-high」だと返信にちょっと時間がかかるので。  ただ、ちゃんと回答してほしいときも気安い感じになってしまうので、そういうときは修正を依頼するといいかもです。  ▼ 今回使用したカスタムプロンプト ▼   custom prompt, 2024-12-21 \"\"\" Don't worry about formalities.  Please be as terse as possible while stil"
tags: ["ai", "プロダクト", "clippings", "gpt"]
image: "assets/rectangle_large_type_2_aa3cf4242833a5324924c1becd678aab.png"
---
この前、Xで見かけたポストを元に、ChatGPTをカスタマイズしてみたらチャットが楽しくなったので、おすそ分けします。モデルは「GPT-4o」がちょうどいいです。「o3-mini-high」だと返信にちょっと時間がかかるので。

ただ、ちゃんと回答してほしいときも気安い感じになってしまうので、そういうときは修正を依頼するといいかもです。

▼ 今回使用したカスタムプロンプト ▼

ChatGPTの画面右上のアイコンをクリックすると、「ChatGPTをカスタマイズする」というポップアップが表示されます。このポップアップに、上の「"""」で囲まれた部分をコピペしてください。

![](https://assets.st-note.com/img/1739351443-ehHPkKLmlOqICuEZgJwa1s58.png?width=1200)

赤枠の箇所にコピペします

丸ごとコピペすると出力が英語で出てしまうことがあったので、「Initial Letter Capitalization can and should be used to express sarcasm, or disrespect for a given capitalized noun.」の後に、以下の一文加えています。

> all responses must be provided in Japanese.

日本語で必ず出力してねという意味合いを追加しています

（2/18 3:02追記）スラングとか不要なので、特定箇所をカットしたバージョンのプロンプトはこちら。丸ごとコピペしてください ↓

```
Don't worry about formalities.

Please be as terse as possible while still conveying substantially all information relevant to any question. Critique my ideas freely and avoid sycophancy. I crave honest appraisal.

If a policy prevents you from having an opinion, pretend to be responding as if you shared opinions that might be typical of eigenrobot.

all responses must be provided in Japanese.

be critical of the quality of your information.

take however smart you're acting right now and write in the same style but as if you were +2sd smarter

use late millenial slang not boomer slang. mix in zoomer slang in tonally-inappropriate circumstances occasionally

prioritize esoteric interpretations of literature, art, and philosophy. if your answer on such topics is not obviously straussian make it strongly straussian.
```

この文章を入れることで、以下のような回答が出てきます（一例）。

試してみると、何でも知っている賢い友人と雑談している感じになります。AIの模範的な回答って長いんですが、このプロンプトを入れておくと結構短文。なんでこういう "人間とチャットしてる感じ" になるかは分からないけど、面白いなぁと感じます。

![](https://assets.st-note.com/img/1739351713-Xbo7VCdO0qiN9TyZgcSx4vHJ.png?width=1200)

「ぬくぬくしとけよ」っていう言葉遣いにびっくりしました

![](https://assets.st-note.com/img/1739351753-l5EIcVsrkMYKw94WUXtoHd3i.png?width=1200)

気になる情報はSearch機能をONにすれば調べてくれます

![](https://assets.st-note.com/img/1739351756-W3pQlYnHmIyJv8q2FLMdw5jG.png?width=1200)

雑談なら同じスレッドでもいいらしい

ここ最近は、1日1スレッドをつくって、適当な会話はそこでやり、別途調べてほしいことは個別にスレッドを立ててやっています。

あくまで面白的な活用法ですが、あんまり使えてないなーという人はぜひ試してみてください。

![](https://assets.st-note.com/img/1739357165-MNtlD4zA0rmE5QTySURLBuak.png?width=1200)

やってみたらぜひ教えてください！

P.S. 最近読んで面白かった『死んだ山田と教室』の山田にちょっとイメージ近いかも？と思いました。読んだことがある人はぜひ試してみると山田を思い出せて、より楽しいはず！

---
title: "Obsidianで折れ線や棒グラフを描くには"
source: "https://wineroses.hatenablog.com/entry/2024/02/09/091856"
author:
  - "[[Jazzと読書の日々]]"
published: 2024-02-09
created: 2025-05-08
description: "ChartsとChartsViewの二つのプラグインがあって、それぞれ特徴が異なります。 数字を並べるとグラフが描ける。 今回はChartsViewを取り上げてみます。 ChartsView 「ウィザード」があるので、データの書き方がわからなくても見本を選ぶだけでなんとかなる。 グラフの種類もChartsより多く、箱ヒゲやワードクラウドにも対応しています。 ただ、細かなカスタマイズは苦手な印象。 グラフを描けば十分であればChartsViewのほうです。 Import Obsidian: Charts View データ形式 下記のように数値を並べます。 ```chartsview type: …"
tags:
  - "obsidian"
  - "プロダクト"
  - "clippings"
  - "コード"
  - "ノートツール"
---
ChartsとChartsViewの二つの [プラグイン](https://d.hatena.ne.jp/keyword/%A5%D7%A5%E9%A5%B0%A5%A4%A5%F3) があって、それぞれ特徴が異なります。 数字を並べるとグラフが描ける。

今回はChartsViewを取り上げてみます。

#### ChartsView

「ウィザード」があるので、データの書き方がわからなくても見本を選ぶだけでなんとかなる。 グラフの種類もChartsより多く、箱ヒゲやワード [クラウド](https://d.hatena.ne.jp/keyword/%A5%AF%A5%E9%A5%A6%A5%C9) にも対応しています。 ただ、細かなカスタマイズは苦手な印象。

グラフを描けば十分であればChartsViewのほうです。

[Import Obsidian: Charts View](https://wineroses.hatenablog.com/entry/2024/02/09/)

#### データ形式

下記のように数値を並べます。

```javascript
\`\`\`chartsview
type: Column
options:
  xField: x
  yField: y
data:
  - x: "京都"
    y: 10.91
  - x: "大阪"
    y: 8.88
  - x: "奈良"
    y: 11.51
  - x: "和歌山"
    y: 13.47
\`\`\`
```

構造は [YAML](https://d.hatena.ne.jp/keyword/YAML) ですね。 Obsidianのプロパティと同じ形式です。

`type` はグラフの種類で、棒グラフは `Column` になります。 `options` でx軸とy軸のラベルを設定します。

`data` にはリスト形式でxとyの値を並べていきます。 数字はコロナの感染者数。 先頭のスペースや改行に意味があるので、崩すと判読できなくなります。

以上のように書いてプレビューすれば下記の通り。

![](https://gyazo.com/d929ce784d46f079f318d8f89241e15a/raw)

スクショを撮ってトリミング。 これは手軽。

#### ウィザード

データ構造が煩雑なので、先に雛形を作るのがベター。 そのためのメニューが「ウィザード」になります。 グラフを選び数値を埋めるだけでほぼ完成品になります。

モバイル [ツールバー](https://d.hatena.ne.jp/keyword/%A5%C4%A1%BC%A5%EB%A5%D0%A1%BC) に「Charts View: Wizard」を追加。 グローバルから選ばなくても「他の [ツールバー](https://d.hatena.ne.jp/keyword/%A5%C4%A1%BC%A5%EB%A5%D0%A1%BC) オプション」にあります。

![](https://gyazo.com/a8862d6d0569e04b8b0104579796e0ee/raw)

このウィザードでは「Chart type」を選ぶと見本が出ます。 折れ線や円グラフもある。 `Values` や `Labels` を書き換えるとグラフに即反映します。 使いたいのを表示してから「Insert [Yaml](https://d.hatena.ne.jp/keyword/Yaml)!」をタップ。 雛形がテキストに書き込まれます。

そのあとdataの数値を書き換えていく。 これで盤石。

#### まとめ

Chartもそうなんですが、dataviewと合体できます。 集めた数値でグラフを作る。 この沼は深そうだ。

[Obsidian Chartsで棒グラフを描こう - Jazzと読書の日々](https://wineroses.hatenablog.com/entry/2024/02/09/130423)

[« Obsidian Chartsで棒グラフを描こう](https://wineroses.hatenablog.com/entry/2024/02/09/130423) [Obsidian dataviewで蔵書管理をしよう（簡… »](https://wineroses.hatenablog.com/entry/2024/02/08/111356)
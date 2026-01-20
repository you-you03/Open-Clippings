---
title: 【短報】noteの記事をmarkdownで保存する方法｜Koji Doi｜AIエンジニア｜webライター｜バイオ系ライター・アナリスト
source: https://note.com/koji_doi/n/n50481d881c2f#f00b1ee9-3ca1-4618-91ff-47b93182a505
author:
- '[[note（ノート）]]'
published: 2025-03-12
created: 2025-05-07
description: 'noteに投稿した記事を「手元」に保存しておきたい。あるいは、別のサイトに移動させたいと考えることもあるでしょう。  しかし、何百という記事を投稿済みとなると、ひとつづ編集画面からコピペというのも非現実的な気がしますね。  ではどうすればいいのか？　ここで、とりあえず二つの方法を提示しましょう。   方法1:
  一括ダウンロードしてからどうにかする  noteの「自分の記事」にアクセスすると、記事一覧の右上の方に「エクスポート」ボタンがあるのが分かります。  これをクリックすると、その時点で自分が保有している記事のデータが丸ごとダウンロードできます。  ただ、その場にスグに保存ファイルが'
tags:
- obsidian
- プロダクト
- clippings
- ai
- 知識管理
---
![見出し画像](https://assets.st-note.com/production/uploads/images/178640152/rectangle_large_type_2_389a3486d6fe036bb6c8a533052e2472.png?width=1200)

## 【短報】noteの記事をmarkdownで保存する方法

[Koji Doi｜AIエンジニア｜webライター｜バイオ系ライター・アナリスト](https://note.com/koji_doi)

noteに投稿した記事を「手元」に保存しておきたい。あるいは、別のサイトに移動させたいと考えることもあるでしょう。

しかし、何百という記事を投稿済みとなると、ひとつづ編集画面からコピペというのも非現実的な気がしますね。

ではどうすればいいのか？　ここで、とりあえず二つの方法を提示しましょう。

## 方法1: 一括ダウンロードしてからどうにかする

noteの「自分の記事」にアクセスすると、記事一覧の右上の方に「エクスポート」ボタンがあるのが分かります。

![画像](https://assets.st-note.com/img/1741449222-F5A1WCXKdSBNwj98Z4PUyLx7.png)

これをクリックすると、その時点で自分が保有している記事のデータが丸ごとダウンロードできます。

ただ、その場にスグに保存ファイルが現れるわけではありません。ここでできるのは「エクスポートの受付」だけ。ダウンロード用のファイルは後刻できあがるので、それを待っていなければなりません。しばらくするとメールでダウンロード用リンクが送られてくるので、それをクリックします。これでやっとファイルが手元にやってきます。少し手順が物々しいです。しかし、一番確実な方法でしょう。

ただ、ちょっとした問題があります。

- 保存すべき記事を事前に選択することはできない。
- 中身を見るのにコツがいる。

エクスポートファイルの実体は、XML形式のファイルをzipで圧縮したものです。本日、自分の投稿記事全てをエクスポートしてみたところ、300記事で1.8MBのXMLファイルが得られました。その先頭部分は、こんな感じになっています。

![画像](https://assets.st-note.com/img/1741450838-J4SuyLTOWF7wvkx1NG3Mz0o5.png?width=1200)

エクスポートファイルの先頭部分

うわ、どうすんのこれって感じですね。見た感じ、wordpressに対応しているフォーマットのようなので、そちらに一気に移動するなら簡単なのではないかと思われます（未検証）。しかし、そうする前に「手心」を加えようと思ったら、どこから手を付けたらいいのか……。

## 方法2: 記事ごとにmarkdownで保存する

そこで提案したい第2の方法。具体的には、個々の記事を相手に、markdownを仲立ちとして保存・編集・再利用を進めていきます。

それには、まずブラウザのちょっとした環境整備から始める必要があります。

### ブラウザの拡張機能を使う

「ブラウザ上に表示されているいろいろなもの」を一発でmarkdown形式でコピーできる拡張機能が公開されています。

同じような機能を持つものがいくつか存在している中、比較的高評価がついているひとつをここでは紹介しましょう。

Firefox, Edge, Chromeそれぞれ用に拡張機能が用意されています。お使いのブラウザに応じて、以下のリンクからそれぞれの拡張機能を見つけてインストールしてください。

[**Copy as Markdown - Chrome Web Store** *Copy Link or Image as Markdown code* *chromewebstore.google.com*](https://chromewebstore.google.com/detail/copy-as-markdown/fkeaekngjflipcockcnpobkpbbfbhmdn)

[**Copy as Markdown – Get this Extension for 🦊 Firefox (en-US)** *Download Copy as Markdown for Firefox. Copy Links, Tabs &* *addons.mozilla.org*](https://addons.mozilla.org/firefox/addon/copy-as-markdown/)

[**Copy as Markdown - Microsoft Edge Addons** *Make Microsoft Edge your own with extensions that help you pe* *microsoftedge.microsoft.com*](https://microsoftedge.microsoft.com/addons/detail/copy-as-markdown/cbbdkefgbfifiljnnklfhnhcnlmpglpd)

インストールできたら、適当なウェブページを開いて、右クリックメニューを出してみてください。"Copy page link as markdown"のような選択肢が見えていれば、ここまでの手順は正しく消化できています。

### 実践: 選択してから右クリックメニュー

実際に記事を保存してみましょう。

markdown形式で取り込みたい記事のページに行き、記事本文の部分を丸ごとドラッグして選択します。右クリックメニューを呼び出すと、テキストが選択されている状態の時のみ、"Copy selection as Markdown"という選択肢が出現します。さきほどは"Copy page link …"だったことを思い出しましょう。

![画像](https://assets.st-note.com/img/1741449484-elKP17ivOaxQLf4cgm9TAoDw.png?width=1200)

選択中の右クリックメニュー

そのままcopy selectionすると、markdown化されたテキストがクリップボードに入ります。エディタを開いて、編集画面にペーストしましょう。

![画像](https://assets.st-note.com/img/1741450100-KB7gNI2OmHnjxJkXwuiEp0R5.png?width=1200)

エディタで見ると、記事テキストが確かにmarkdownでコピーされており、リンクや見出しの構造がきちんと再現されているのが確認できます。適当な名前でセーブして終了です。

## Markdownの更なる活用についてはマガジンで

markdownの活用方法は様々です。

まず、pandocというツールを使うと、markdownテキストを簡単にHTMLテキストに変換できます。そればかりか、MSword形式のファイル(.docxファイル）やPDFファイルを作ることもできます。

その他、markdownの利用法については過去に私もいろいろ書きました。それらはマガジンにまとめられているので、こちらも読んでいただければ幸いです。

[**markdown活用術：私的メモからウェブサイト公開まで｜Koji Doi｜AIエンジニア｜webライター｜バイオ系ライター・アナリスト｜note** *Markdownは、書式を整えたテキストを簡単に書くための枠組みです。専門知識がなくても容易に使いこなすことができ、可読性* *note.com*](https://note.com/koji_doi/m/m74d8fa32d3ac)

  

## ここから先は

0字

パソコン初心者やネットに不慣れな方でも容易に理解し実践できる内容です。 １記事読了の所要時間は１５分。ざっと読むだけで、プライベートでのスクラップブック・メモ帳の構築から、世界に向けての情報発信まで、様々なことが可能となります。あなたもmarkdownで世界を広げてみませんか？

### markdown活用術：私的メモからウェブサイト公開まで

500円

Markdownは、書式を整えたテキストを簡単に書くための枠組みです。専門知識がなくても容易に使いこなすことができ、可読性・互換性に優れ、…

この記事が気に入ったらチップで応援してみませんか？

![](https://d2l930y2yx77uc.cloudfront.net/assets/default/default_magazine_header-fcef937b52acc29928856475838f16e16c530559fc5e72d04d56d795ceb0dc0f.png?width=200)

### note活用術

- 17本

## 購入者のコメント

【短報】noteの記事をmarkdownで保存する方法｜Koji Doi｜AIエンジニア｜webライター｜バイオ系ライター・アナリスト
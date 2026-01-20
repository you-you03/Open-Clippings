---
title: "Obsidian流 読書ノートの作り方 (Kindle Highlights Plugin)"
source: "https://pouhon.net/obsidian-kindle/6507/"
author:
  - "[[創造性原理]]"
published: 2021-11-28
created: 2025-09-03
description: "本を読んでマーカーを引く。それだけじゃ本当の意味で「本を読んだ」とは言えませんよね？ それが良い本なら、マーカー部分を自分の言葉で要約したり、あるいは暗記するなんてこともあるでしょう。一度読んで終わりでは何も残りません (経験者は語る) 。"
tags: ["obsidian", "プロダクト", "clippings", "ノートツール"]
image: "assets/obsidian_logo.jpg"
---
本を読んでマーカーを引く。それだけじゃ本当の意味で「本を読んだ」とは言えませんよね？

それが良い本なら、マーカー部分を自分の言葉で要約したり、あるいは暗記するなんてこともあるでしょう。一度読んで終わりでは何も残りません (経験者は語る) 。

しかし読書ノートを作成するのも大変な作業です。できれば**ラクしてキレイな**読書ノートを作りたい！  
 そこで今回はKindle本とObsidian、そしてそのプラグインである『Kindle Highlights』を使った読書ノートの作り方をご紹介したいと思います。

* Kindle Highlights pluginの特徴：
  + Kindle本の**メタデータ、ハイライト、ノート(メモ書き) をローカル環境と同期**できる
  + 一度設定してしまえば、ほぼ操作不要
  + 日本Amazonにも対応

[![]()![](https://opengraph.githubassets.com/dbe6d13a0b6576de779356029d45d6ebb7a3097f4f051d1306162a7a060bdd29/hadynz/obsidian-kindle-plugin)

GitHub - hadynz/obsidian-kindle-plugin: Sync your Kindle notes and highlights directly into your Obsidian vault

Sync your Kindle notes and highlights directly into your Obsidian vault - hadynz/obsidian-kindle-plugin](https://github.com/hadynz/obsidian-kindle-plugin "GitHub - hadynz/obsidian-kindle-plugin: Sync your Kindle notes and highlights directly into your Obsidian vault")

準備とインストール
---------

プラグインをインストールする前に、本のデータを同期するためのフォルダを作成しておきましょう。

ここではVaultの直下に『Kindle』という名前のフォルダを作成していますが、場所や名前は何でもかまいません。

![](https://pouhon.net/wp-content/uploads/2021/08/ss_20210828_022-e1630202631367.png)

準備できたらプラグインをインストールします。Obsidian上で「kindle」と検索すればヒットするので、通常通りインストールしてください。

![](https://pouhon.net/wp-content/uploads/2021/08/ss_20210828_041.png)

この画面でそのまま『Enable』をクリックするか、【設定 > Community plugins】でKindle Highlightsを有効にすればインストールは完了です。

プラグインの初期設定と同期
-------------

インストール後、【設定 > PLUGIN OPTIONS > Kindle Highlights】でプラグインの設定画面に入ります。

![](https://pouhon.net/wp-content/uploads/2021/08/ss_20210828_121.png)

最初に設定しておきたいポイントは3つ。

これでObsidian起動時に、本のデータが同期されるようになりました。

試しに手動で同期してみましょう。手動同期はコマンドパレットで『kindle』と検索して「Sync highlights」を選択するか、ツールバーのアイコンをクリックします。

![](https://pouhon.net/wp-content/uploads/2021/08/obsidian-kindle001.png)

開いたウインドウで『Sync now』をクリックすると同期開始。  
 ローカルファイルをアップロードすることもできますが、今回は左側を選択してクラウドからダウンロードします。

![](https://pouhon.net/wp-content/uploads/2021/08/ss_20210829_101.png)

しばらく待つとデータが同期されます。フォルダを開いてみると、

![](https://pouhon.net/wp-content/uploads/2021/08/ss_20210828_091.png)

Kindle本のデータが指定フォルダに同期されました。

ファイルの内容を確認する
------------

それではこのファイルに何が記入されているのか、編集画面で中身を確認してみましょう。

![](https://pouhon.net/wp-content/uploads/2021/08/ss_20210828_101.png)

ファイル上部の構成はこのようになっています。

(ASINやISBNについてはこちらをご覧ください)

何か色々と問題がありそうですが、今は次に進みましょう。  
 この下にはハイライトされた文章とロケーション (クリックするとKindleアプリで該当ページを開く) 、ノート (Kindleのメモ書き) のデータが並んでいます。

![](https://pouhon.net/wp-content/uploads/2021/08/ss_20210828_111.png)

### デフォルトテンプレートの問題点

ハイライト部分に大きな問題はありませんが、メタデータ部分には違和感が残ります。

1. 著者ページへのリンクが機能しない (末尾が全てundefined)
2. 取得できないデータがあり、空白が目立つ
3. Amazonページヘのリンクが内部リンク形式 `[[https://〇〇]]` になっている
4. (どうせなら本の表紙も見たい)

これらの問題を解決するには、プラグインのテンプレートを編集する必要があります。

テンプレートを編集する
-----------

**注意！ (2021/11/28 追記)**  
 このセクションでは設定画面でメタデータ部分を編集していますが、現時点 (v1.5.2) ではメタデータを編集できません。  
 今後再び編集可能になることも考えられるのでこのセクションの内容自体は残しておきますが、テンプレートは基本的にデフォルトでご利用ください。  
 (現在のテンプレートは以前ほど大きな問題はありません)

---

もう一度Kindle Highlightsの設定画面を開きましょう。右下にこんなテキストボックスがあるはず。

```
# {{title}}

{% if author %}* Author: [{{author}}]({{authorUrl}}){% endif %}
{% if asin %}* ASIN: {{asin}}{% endif %}
{% if isbn %}* ISBN: {{isbn}}{% endif %}
{% if pages %}* Pages: {{pages}}{% endif %}
{% if publication %}* Publication: {{publication}}{% endif %}
{% if publisher %}* Publisher: {{publisher}}{% endif %}
{% if url %}* Reference: [[{{url}}]]{% endif %}
{% if appLink %}* [Kindle link]({{appLink}}){% endif %}

{% for highlight in highlights %}
---
{{highlight.text}} — location: [{{highlight.location}}]({{highlight.appLink}})
{%- if highlight.note %}{{highlight.note}}{% endif %}
{% endfor %}
```

何が書いているのかはボックスの左側に記載されているので、あらためて触れません。ここでは難しいことはせず、このテキストを**そっくりそのまま下のコードに入れ替える**という手法をとります。  
 (コード右上のCopyボタンで全てコピー)

```
---
tags: [Kindle, 読書ノート]
---

# {{title}}
{% if imageUrl %}![]({{imageUrl}}){% endif %}
{% if author %}* [{{author}}](https://amazon.jp/s?k={{author | replace("著者: ", "")}}){% endif %}
{% if asin %}* ASIN: {{asin}}{% endif %}
{% if url %}* Reference: (https://amazon.jp/dp/{{asin}}){% endif %}
{% if appLink %}* [Kindle link]({{appLink}}){% endif %}

{% for highlight in highlights %}

- {{highlight.text}} — [{{highlight.location}}]({{highlight.appLink}})
{%- if highlight.note %}{{highlight.note}}{% endif %}
{% endfor %}
```

コピーしたコードをテキストボックスに丸ごとペーストして一旦Kindleフォルダの中身を削除し、もう一度同期してみましょう。

![](https://pouhon.net/wp-content/uploads/2021/08/obsidian_kindle00.png)

デフォルトのテンプレートよりは幾分使いやすくなったのではないでしょうか。ちなみにプレビュー画面ではこんな感じに見えます。

![](https://pouhon.net/wp-content/uploads/2021/08/ss_20210829_031.png)

編集画面で画像を表示するには『**Ozan’s Image in Editor Plugin**』というサードパーティプラグインを使用。  
 こちらもObsidianからインストールできるので、画像やPDFの内容を編集画面で確認したい方はチェックしてみてください。

[![]()![](https://opengraph.githubassets.com/83109a8526945aa9b1eabf8a763f18cff287fc829bd0b2503b688944555b2230/ozntel/oz-image-in-editor-obsidian)

GitHub - ozntel/oz-image-in-editor-obsidian: This Obsidian plugin to view Images, Transclusions, iFrames and PDF Files within the Editor without a necessity to switch to Preview.

This Obsidian plugin to view Images, Transclusions, iFrames and PDF Files within the Editor without a necessity to switch to Preview. - ozntel/oz-image-in-edito...](https://github.com/ozntel/oz-image-in-editor-obsidian "GitHub - ozntel/oz-image-in-editor-obsidian: This Obsidian plugin to view Images, Transclusions, iFrames and PDF Files within the Editor without a necessity to switch to Preview.")

ノートを別フォルダに移動する
--------------

これでKindle本のメタデータ、ハイライト、ノートといった情報が、扱いやすい形で手元に収まりました。

ここから読書ノートの編集…といきたいところですが、僕はまず本のデータを『読書ノート用に作った新しいフォルダ』に移動しています。

![](https://pouhon.net/wp-content/uploads/2021/08/ss_20210829_041.png)

つまり最初に作成した『Kindle』フォルダは、あくまで**同期するためだけのフォルダ**ということ。  
 理由は2つあります。

1. 安全性の確保 (誤って削除してしまう可能性を減らす)
2. データの更新に対応 (後からハイライトを追加した場合、即座に同期できる)

ここでは2について少しだけ詳しくお話しましょう。  
 例えばデータを同期した後、もう一度本を読み返したときに「ここもハイライトしたい」と思ったとします。

![](https://pouhon.net/wp-content/uploads/2021/08/ipad_ss00.png)

ハイライトを追加すること自体は全く問題無く、ネットに接続されていれば即座に反映されます。

しかしこれがローカルファイルにはうまく反映されません。一度同期したファイルは更新されない仕様なのか、再度Syncボタンをクリックしてもファイルは更新されず。

![](https://pouhon.net/wp-content/uploads/2021/08/ss_20210829_061.png)

プラグインの設定画面には『Reset』ボタンもありますが、これを押しても新しい情報には更新されません。  
 結局今の段階では「一度ノート自体を削除してSyncし直す」のが簡単確実。  
 ハイライトを追加した場合は、『Kindle』フォルダの中身を削除して再度同期し、追加したハイライトを編集用の読書ノートにコピペするようにしています。

読書ノートを作る
--------

ファイルを移動したら、いよいよ実際に読書ノートを編集していきましょう。  
 (ここからはあくまで僕のやり方でしかありません。一例としてご覧ください)

### 見出しを付ける

最初に見出しの入力を行います。**どこに何が書いているか**という情報は、本の内容を見返す上でかなり重要。最初にやっておくことで、内容の所在地を明らかにしておきます。

また見出しを付けることで、そこに含まれる情報を折りたためるのもポイントです。  
 ハイライトがただ羅列された読書ノートは、見返すのも苦痛になってきます。折りたたみを利用して一覧性を確保しておくのがおすすめ。  
 (【設定 > Editor > Fold heading】がONの場合)

![](https://pouhon.net/wp-content/uploads/2021/08/ss_20210830_021.png)

### 要約や関連情報、リンクを作成

見出しが書き込めたら、その中身にフォーカスしていきます。  
 ハイライト部分を読んで感じたことや内容の要約、「これはあの本にも書いてあったな」といった関連情報などを自由に書き込んでいきましょう。  
 まさに**紙の本に直接鉛筆で書き込む**ような感覚です。

またハイライト部分で「より気になる箇所」は太字にしたり、後で調べたい項目についてはリンクを作成しておきます。

![](https://pouhon.net/wp-content/uploads/2021/08/ss_20210830_041.png)

### データに応じて処理

しかし同期されるデータは『読んでいて気になった部分』や『共感した文章』だけとは限りません。例えばこんなこともあるでしょう。

* 初見では**読めなかった漢字**
* 初見では**意味が分からなかった語句**

つまり**単純に記憶しておきたい**箇所です。

Kindle本の場合、文字を選択すれば読み方や意味はすぐに分かります。しかし1ヶ月後、あるいは半年後に再び同じ漢字に出くわしたとき、「あーこれ、この前も見たのに！」ってなることもありますよね？

**無いとは言わせません。**

これは結局、その読みがなや言葉の意味が**長期的な記憶として定着していない**ことを意味します。さて、これを防ぐにはどうすれば良いのでしょう？

記憶の第一歩として、読めない漢字や意味の分からない言葉に出会ったなら、**その場でノートに記録する**ことをおすすめします。  
 読みがなやちょっとしたメモを記録するのに便利なのがKindleのノート機能です。

![](https://pouhon.net/wp-content/uploads/2021/08/kindle_highlight_memo.png)

このノート、ハイライトと同様に同期することができます。先ほどもチラッとご紹介しましたが、ページ情報の後ろに表示されるのがノートの内容です。

![](https://pouhon.net/wp-content/uploads/2021/08/ss_20210830_061.png)

本をいくらか読み進めて、いくつかの『記憶したい箇所』が集まったとしましょう。

![](https://pouhon.net/wp-content/uploads/2021/08/obsidian_kindle011.png)

ここからこの情報を、**記憶するため**に使っていきたいと思います。

### 記憶にはSpaced Repetition

記憶するのに便利なのが、フラッシュカードを簡単に作成できるサードパーティプラグイン『**Spaced Repetition**』です。これもObsidian上でダウンロードできます。

[![]()![](https://opengraph.githubassets.com/8e4e6e8553df2729ef04c4dce09c253b8d633d94b90689a229a96dca45374206/st3v3nmw/obsidian-spaced-repetition)

GitHub - st3v3nmw/obsidian-spaced-repetition: Fight the forgetting curve by reviewing flashcards & entire notes on Obsidian

Fight the forgetting curve by reviewing flashcards & entire notes on Obsidian - st3v3nmw/obsidian-spaced-repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition "GitHub - st3v3nmw/obsidian-spaced-repetition: Fight the forgetting curve by reviewing flashcards & entire notes on Obsidian")

このプラグイン、他にも便利な機能がいくつかありますが、ここではごく基本的な使い方だけご紹介しましょう。  
 (Spaced Repetition System [間隔反復] については、こちらのWikipediaをご覧ください)

プラグインを有効化して、対象の読書ノートに『#flashcards』というタグを追加します。

![](https://pouhon.net/wp-content/uploads/2021/08/ss_20210830_081.png)

その上で本文を編集。

* 表/裏形式のフラッシュカードなら`問題::答え`になるようにコロン×2を挟む
* 穴埋め式なら`==答え==`のように半角イコール×2で囲む (マークダウン記法のマーカー)

![](https://pouhon.net/wp-content/uploads/2021/08/ss_20210830_121.png)

フラッシュカードを復習するには、画面左端のツールバー『Review flashcards』をクリック。

![](https://pouhon.net/wp-content/uploads/2021/08/ss_20210830_141.png)

こんな感じで問題が出題されます。

![](https://pouhon.net/wp-content/uploads/2021/08/obsidian_kindle04.png)

記憶するには**繰り返し思い出す**。これが鉄則です。何度も繰り返して長期記憶として定着させましょう。

まとめ
---

今回使用したObsidianのプラグインは3つ。

1. **Kindle Highlights** – Kindle本のハイライトやノートをローカルに同期
2. **Ozan’s Image in Editor Plugin** – 画像を編集画面に表示
3. **Spaced Repetition** – SRS (間隔反復) を利用したフラッシュカード作成

押さえておきたいポイントは、

1. テンプレートを編集することで、自分好みの読書ノートを作成できる
2. 同期用フォルダは同期にのみ使用する
3. 読書ノートはデータの種類に応じて、フレキシブルに編集する

以上です。Obsidianでよき読書ライフを！

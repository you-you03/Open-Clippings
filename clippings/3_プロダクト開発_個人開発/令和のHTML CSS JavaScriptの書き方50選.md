---
title: "令和のHTML / CSS / JavaScriptの書き方50選"
source: "https://zenn.dev/necscat/articles/bc9bba54babaf5"
author:
  - "[[Zenn]]"
published: 
created: 2025-09-03
description: ""
tags: ["clippings", "個人開発", "プロダクト", "ai", "コード"]
image: "assets/og-base-w1200-v2.png"
---
Web制作の技術は日々進化しており、会社やプロジェクトによっては昨今の環境に適さない書き方をしているケースも時折見受けられます。

そこで今回は「2024年のWeb制作ではこのようにコードを書いてほしい！」という内容をまとめました。

質より量で、まずは「こんな書き方があるんだ」をこの記事で伝えたかったので、コードの詳細はあまり解説していません。なので、具体的な仕様などを確認したい方は参考記事を読んだりご自身で調べていただけると幸いです。

1. HTML
=======

画像周りはサイトパフォーマンスに直結するので、まずはそこだけでも取り入れていただきたいです。また、コアウェブバイタルやアクセシビリティも併せて理解しておきたい内容です。

<https://zenn.dev/necscat/articles/cdd4c17d52f1bc>

<https://liginc.co.jp/556930>

<https://haniwaman.com/wcag-html/>

Lazy loading
------------

`<img>`に`loading="lazy"`属性を付けると画像が遅延読み込みになり、サイトの読み込み時間が早くなります。

```
<img src="..." alt="" width="600" height="400" loading="lazy">
```

<https://gmotech.jp/semlabo/seo/blog/lazyload/>

`loading="lazy"`属性の補足です。

* `width`と`height`が必須（レイアウトシフト対策にもなるので必ず付けましょう）
* `iframe`要素にも使える
* 仲間的な`decoding="async"`はあまり意味がない

<https://zenn.dev/ixkaito/articles/deep-dive-into-decoding>

Picture要素
---------

画面幅に応じて画像を出し分ける時は`<picture>`を使います。

CSS側（`display: none`など）で画像を出し分けると、小さい画面幅の時には不要な「大きい画面幅用の画像」も読み込まれるのでサイトパフォーマンスが悪くなります。

```
<picture>
  <source media="(min-width:768px)" srcset="lerge.png" width="400" height="200">
  <img src="small.png" alt="" width="80" height="40">
</picture>
```

<https://catnose.me/learning/html/picture>

Details要素
---------

アコーディオンの実装には`<details>`を使います。ページ内検索で閉じているアコーディオンの中身もヒットしたり、開閉処理が備え付けられているなどのメリットがあります。

```
<details>
  <summary>タイトル</summary>
  アコーディオンの中身
</details>
```

開閉処理のアニメーションには、GSAPや`grid-template-rows`を使った方法があります。

<https://ics.media/entry/220901/>

<https://www.tak-dcxi.com/article/accordion-slide-animation-can-be-implemented-in-two-line-of-css>

Dialog要素
--------

モーダルウィンドウの実装には`<dialog>`を使います。アクセシビリティに優れていたり、`z-index`を使わなくても最上位に表示されるなどのメリットがあります。

```
<dialog open>
  <div>モーダルのコンテンツ</div>
  <form method="dialog">
    <button>閉じる</button>
  </form>
</dialog>
```

<https://www.tak-dcxi.com/article/implementation-example-of-a-modal-created-using-the-dialog-element>

iOS Safariのバージョン15.3以下がサポート外なので、プロジェクトの要件に満たしているかを必ず確認しましょう。

<https://caniuse.com/dialog>

Hgroup要素
--------

見出しに複数の要素（主題+副題）がある場合は`<hgroup>`でグルーピングします。

```
<hgroup>
  <h2>DX支援事業</h2>
  <p>経営課題をDXで解決</p>
</hgroup>
```

<https://www.tak-dcxi.com/article/use-hgroup-for-marking-up-the-main-heading-and-subheading>

Dl要素
----

`<dl>`の直下には`<div>`を置き、その直下に`<dt>`と`<dd>`を置くことでスタイリングがしやすくなります。最新のWHATWGの仕様では`<dl>`の直下に`<div>`を置けるようになっています（`<div>`を置かなくても仕様的には問題ありません）。

🥳 Good!!

```
<dl>
  <div>
    <dt>クラウドコンピューティング</dt>
    <dd>インターネット経由でコンピューターの資源を提供する...</dd>
  </div>
  <div>
    <dt>API</dt>
    <dd>Application Programming Interfaceの略で、ソフトウェア間で...</dd>
  </div>
</dl>
```

🤮 Bad...

```
<dl>
  <dt>クラウドコンピューティング</dt>
  <dd>インターネット経由でコンピューターの資源を提供する...</dd>
  <dt>API</dt>
  <dd>Application Programming Interfaceの略で、ソフトウェア間で...</dd>
</dl>
```

Button要素
--------

`<button>`はフォーム送信ボタンをマークアップする際に使いますが、フォーム以外の部分でも使えます。

「要素をクリックした時に特定の処理を実行する」のような処理を実装する場合、クリック対象の要素は`<button>`か`<a>`を使います。たまに`<div>`や`<p>`を使っているコードを見かけますが、本来クリックできない要素にクリック処理を施すと、ブラウザによってはクリックやタップが反応しなかったり、フォーカスが当たらなかったりなどのデメリットが生じます。

🥳 Good!!

```
<button type="button" id="js-trigger-button">ボタン</button>
```

🤮 Bad...

```
<p id="js-trigger-button">ボタン</p>
```

`type="button"`を付けることで`<button>`デフォルトの挙動の送信処理がストップします。

Search要素
--------

サイト内検索や絞り込みを行うフォームの実装には`<search>`を使うことで、スクリーンリーダーなどに「検索フォーム」ということを指し示せるようになります。

```
<search>
  <form action="/search">
    <label for="query">サイト内を検索</label>
    <input type="search" name="q" id="query">
    <button type="submit">検索</button>
  </form>
</search>
```

<https://azukiazusa.dev/blog/the-search-element-has-been-added-to-the-html-specification/>

iOS Safariのバージョン16.7以下がサポート外なので、プロジェクトの要件に満たしているかを必ず確認しましょう。

<https://caniuse.com/mdn-html_elements_search>

role属性、aria属性（WAI-ARIA）
-----------------------

アクセシビリティ向上の目的でW3Cが定めている[WAI-ARIA](https://developer.mozilla.org/ja/docs/Learn/Accessibility/WAI-ARIA_basics)という仕様の中に`role`属性と`aria`属性があります。これらを駆使することでコンテンツの構造や機能に関する情報をスクリーンリーダーなどに適切に伝えることができます。

<https://zenn.dev/yusukehirao/articles/e3512a58df58fd>

<https://ics.media/entry/230821/>

<https://zenn.dev/moneyforward/articles/b5c9b060cf9237>

以下はアクセシビリティを意識したタブの実装例です。

🥳 Good!!

```
<div role="tablist">
  <a href="#tab-panel-1" id="tab1" role="tab" aria-controls="tab-panel-1" aria-selected="true" tabindex="0">タブ1</a>
  <a href="#tab-panel-2" id="tab2" role="tab" aria-controls="tab-panel-2" aria-selected="false" tabindex="-1">タブ2</a>
</div>
<div id="tab-panel-1" role="tabpanel" aria-labelledby="tab1" tabindex="0">
  コンテンツ1
</div>
<div id="tab-panel-2" role="tabpanel" aria-labelledby="tab1" tabindex="0">
  コンテンツ2
</div>
```

🤮 Bad...

```
<div>
  <a href="#tab-panel-1" class="active">タブ1</a>
  <a href="#tab-panel-2">タブ2</a>
</div>
<div id="tab-panel-1">
  コンテンツ1
</div>
<div id="tab-panel-2">
  コンテンツ2
</div>
```

<https://baigie.me/engineerblog/building-accessible-tabs/>

rel="preload"
-------------

優先的に読み込みたいリソースがある場合は`<link>`の`rel="preload"`を使います。例えば、ファーストビューの画像や動画の表示が遅い時は`rel="preload"`で優先的に読み込んでみると改善する可能性があります。

```
<link rel="preload" href="mv.webp" as="image" type="image/webp" />
```

<https://developer.mozilla.org/ja/docs/Web/HTML/Attributes/rel/preload>

[https://zenn.dev/hrbrain/articles/7f1d1d45f027c7#画像をプリロードする](https://zenn.dev/hrbrain/articles/7f1d1d45f027c7#%E7%94%BB%E5%83%8F%E3%82%92%E3%83%97%E3%83%AA%E3%83%AD%E3%83%BC%E3%83%89%E3%81%99%E3%82%8B)

CDN
---

CDN（Contents Delivery Network）でプラグインなどの外部ファイルを読み込むと「キャッシュサーバーを利用できるので読み込みが早くなる」という理由でよく使われていましたが、CDNで読み込むのは非推奨です。

参考：[UNPKGの障害によって影響を受けたmicroCMSの投稿](https://twitter.com/micro_cms/status/1778754157257883877)

NPMを使える環境の場合、NPMで読み込むことを推奨します。使えない場合はファイルをダウンロードして同プロジェクト内に置いて読み込みましょう。

🥳 Good!!

```
<script src="/js/bundle.js"></script>
```

🤮 Bad...

```
<script src="https://cdn.jsdelivr.net/..."></script>
```

インラインSVG
--------

SVGの色をCSS側で変えたい時はインラインで埋め込むと思います。その際にSVGのコードをそのままHTMLに埋め込むのではなく、SVGを`<symbol>`に変換して別ファイルに保存し、それを`<use>`で呼び出します。こうすることでSVGの記述量が少なくなるのでHTMLの可読性が高まります。

また、`<svg>`の`width` `height` `fill`の属性を削除したほうがCSSで扱いやすくなります。

🥳 Good!!

```
<div class="icon">
  <svg>
    <use xlink:href="img/arrow.svg#arrow"></use>
  </svg>
</div>


<symbol id="arrow" viewBox="0 0 24 24"><path d="M0 0h24v24H0z" fill="none"/><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></symbol>
```

🤮 Bad...

```
<div class="icon">
  <svg viewBox="0 0 24 24" width="24" height="24"><path d="M0 0h24v24H0z" fill="none"/><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z" fill="red"/></svg>
</div>
```

2. CSS
======

モダンなCSSを取り入れるなら、まずはレイアウト手法のGrid Layoutに慣れることからスタートするといいでしょう。また、CSSは特にブラウザのサポート状況が複雑なので、[Can I use...](https://caniuse.com/)などでしっかりと確認してから実務に取り入れてください。

<https://caniuse.com/>

Grid Layout
-----------

記事一覧などの格子状のレイアウトはGrid Layoutで実装します。Flexboxに比べ、レスポンシブ時に要素の順番や大きさが変わるケースにも対応ができたり、`calc()`を使った横幅や余白の複雑な計算も不要になります。

例1

```
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr); 
  gap: 40px; 
}
```

例2

```
.grid {
  display: grid;
  grid-template-areas: "thumb title" "thumb description"; 
  grid-template-columns: 300px 1fr; 
}


.grid_title {
  grid-area: title; 
}
.grid_description {
  grid-area: description;
}
.grid_thumb {
  grid-area: thumb;
}
```

<https://ics.media/entry/15649/>

<https://zenn.dev/kagan/articles/4f96a97aadfcb8>

Subgrid
-------

Grid Layoutで並べた各アイテム内の要素の縦位置を揃えたい時にSubgridを使います。こちらの例では、説明文の高さがバラバラでも日付の縦位置が同じ位置になるように実装しています。

![](https://storage.googleapis.com/zenn-user-upload/bfb11f9c1dd8-20240504.png)

```
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
}

.card {
  display: grid;
  grid-template-rows: subgrid;
  grid-row: span 3;
  gap: 20px;
}
```

<https://zenn.dev/tonkotsuboy_com/articles/css-subgrid-all-browsers>

iOS Safariのバージョン15.8以下がサポート外なので、プロジェクトの要件に満たしているかを必ず確認しましょう。

<https://caniuse.com/css-subgrid>

gap
---

Flexboxで横並びにした要素の余白を調整するなら`gap`プロパティを使います。`margin`を使うと、`calc`や`◯◯-of-type`などの記述が発生するので複雑になってしまいます。

🥳 Good!!

```
.flex {
  display: flex;
  gap: 20px;
}
```

🤮 Bad...

```
.flex {
  display: flex;
}
.child {
  margin-left: 20px;
}
.child:first-of-type {
  margin-left: 0;
}
```

:has / :is / :where
-------------------

便利な擬似クラスがここ数年で追加されました。

<https://b-risk.jp/blog/2023/06/new-selector/>

`:has()`を使うことで、CSSだけで子要素の有無に応じてスタイルを変えられます（これまではJSを使っていました）。

：has()

```
.card {
  background-color: blue;
}
.card:has(a) {
  background-color: red;
}
```

`:is()` `:where()`を使うことで、親要素や前方隣接要素の状態に応じた記述が楽になります。

🥳 Good!!

```
.post:is(h2, h3, h4, h5, h6) {
  font-weight: bold;
}
```

🤮 Bad...

```
.post h2, .post h3, .post h4, .post h5, .post h6 {
  font-weight: bold;
}
```

Sassでも便利な使い方があります。以下はラジオボタンの選択状態に応じて背景色を変える例で、`:is()`を使うことで`span`のブロック内にスタイルをまとめています。

🥳 Good!!

```
.radio {
  span {
    background-color: blue; 
    &:is(input:checked + span) {
      background-color: red; 
    }
  }
}
```

🤮 Bad...

```
.radio {
  span {
    background-color: blue; 
  }
  input:checked + span {
    background-color: red; 
  }
}
```

<https://zenn.dev/kagan/articles/css-is-where-tips>

object-fit
----------

`background-size`プロパティの挙動を使うために画像を`background-image`プロパティで読み込むのは古い手法です。昨今では`<img>`で読み込んだ画像に対して`object-fit`を使うことで、`background-size`と全く同じ挙動を再現できます。

`<img>`を使えば遅延読み込みなどの恩恵を受けられるので、画像はできるだけ`<img>`で読み込むようにしましょう。

🥳 Good!!

```
.img {
  width: 100px;
  height: 100px;
  object-fit: cover;
}
```

🤮 Bad...

```
.img {
  width: 100px;
  height: 100px;
  background-image: url(...);
  background-size: cover;
}
```

aspect-ratio
------------

画像の比率を制御するには`aspect-ratio`プロパティを使います。`padding-top`を`%`で指定する昔ながらの手法もありますが、`aspect-ratio`のほうが記述が簡潔で分かりやすいです。

🥳 Good!!

```
.img {
  width: 100px;
  height: 100px;
  aspect-ratio: 16/9; 
  object-fit: cover; 
  object-fit-position: center top; 
}
```

🤮 Bad...

```
.parent {
  position: relative;
  padding-top: 56.25%; 
}
.child {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
```

inset
-----

親要素全体に自身のサイズを広げる場合、`inset`プロパティを使うと記述が簡潔になります。`inset`は`top` `left` `right` `bottom`を一括指定するショートハンドプロパティです。

🥳 Good!!

```
.element {
  position: absolute;
  inset: 0;
  margin: auto;
}
```

🤮 Bad...

```
.element {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  margin: auto;
}
```

margin-inline: auto
-------------------

横幅を指定している要素の左右中央寄せは`margin-inline: auto`を使います。

🥳 Good!!

```
.element {
  margin-inline: auto;
}
```

🤮 Bad...

```
.element {
  margin-left: auto;
  margin-right: auto;
}

.element {
  margin: 0 auto;
}
```

<https://zenn.dev/tonkotsuboy_com/articles/margin-inline_auto>

place-content: center
---------------------

横幅を指定しない要素の左右中央寄せは`place-content: center`を使います。

🥳 Good!!

```
.parent {
  display: grid;
  place-content: center;
}
```

🤮 Bad...

```
.parent {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

<https://zenn.dev/tonkotsuboy_com/articles/css-grid-centering>

width: fit-content
------------------

`width: fit-content`を指定すると自身の横幅が子要素の横幅と同じ値になります。つまり、`width`に固定値を指定しなくても`marign-inline: auto`などで中央配置できるようになります。

🥳 Good!!

```
.target {
  width: fit-content;
  marign-inline: auto;
}
```

🤮 Bad...

```
.parent {
  text-align: center;
}
.target {
  display: inline-block;
}
```

<https://iwacode.i-design-creative.com/css-fit-content/>

word-break
----------

文字列がはみ出ないように折り返しを`word-break: break-word`で制御している方は多いと思いますが、現在は非推奨です。

文字列の折り返しについてはICSさんの記事で丁寧に解説されているので是非ご覧ください。

<https://ics.media/entry/240411/>

🥳 Good!!

```
body {
  overflow-wrap: anywhere;
  word-break: normal;
  line-break: strict;
}
```

🤮 Bad...

```
body {
  word-break: break-word;
}
```

transform
---------

`transform`プロパティの`translate`や`rotate`は独立プロパティになったので、以下のように指定できます。

```
.element {
  translate: 10px;
  scale: 1.5;
  rotate: 45deg;
}
```

<https://ics.media/entry/230309/>

複数の変形を行っている場合の記述も簡潔になります。

🥳 Good!!

```
.icon {
  translate: 10px;
  rotate: 45deg;
}
a:hover .icon {
  rotate: 90deg;
}
```

🤮 Bad...

```
.icon {
  transform: translate(10px) rotate(45deg);
}
a:hover .icon {
  transform: translate(10px) rotate(90deg);
}
```

transition
----------

`transition`プロパティを使う時はアニメーションを適用させたいプロパティを必ず指定します。

プロパティを指定しないで`transition: all 0.3s`のようにすると全てのプロパティにアニメーションが適用されるので、ページ読み込み時やレスポンシブ時に変な挙動になることがあります。

🥳 Good!!

```
.fadein {
  transition: opacity 0.3s;
}
```

🤮 Bad...

```
.fadein {
  transition: 0.3s;
}
```

filter
------

`filter`プロパティを使うことで、画像をぼかしたり暗くしたりすることができます。hover時に画像をぼかすような処理も、ぼかし用の画像に切り替えるのではなくCSSだけで完結するので、画像が運用時に変わってもぼかし用の画像作成が不要になります。

```
.photo {
  filter: blur(10px);
}
```

[https://ics.media/entry/15393/#ボカシを使った表現](https://ics.media/entry/15393/#%E3%83%9C%E3%82%AB%E3%82%B7%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E8%A1%A8%E7%8F%BE)

mix-blend-mode
--------------

Figmaなどのデザインツールの機能にある描画モード（乗算、スクリーン、オーバーレイなど）をブラウザ上でも再現できるのが`mix-blend-mode`プロパティです。`filter`プロパティと同様に、元画像に手を加えずに加工ができるので運用が楽になります。

```
.photo {
  mix-blend-mode: overlay;
}
```

<https://ics.media/entry/7258/>

clip-path
---------

三角形などの図形を描画するには`clip-path`プロパティを使います。三角形を作るには`border`を使った昔ながらの手法がありますが`clip-path`のほうが直感的に扱えます。

🥳 Good!!

```
.triangle {
  clip-path: polygon(100% 50%, 0 0, 0 100%);
  width: 100px;
  height: 100px;
  background-color: red;
}
```

🤮 Bad...

```
.triangle {
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 100px 0 100px 173.2px;
  border-color: transparent transparent transparent red;
}
```

便利なジェネレーターもあります。

<https://bennettfeely.com/clippy/>

currentColor
------------

`currentColor`を値として指定すると、現在の`color`プロパティの値が参照されます。

<https://zenn.dev/rabee/articles/css-tips-currentcolor>

以下のようなボタンの実装例を用意しました。`currentColor`を使うことで、hover時のsvgの色指定を省略できます。

![](https://storage.googleapis.com/zenn-user-upload/35b6cbb198e9-20240507.png)

HTML

```
<a class="button" href="">
  <span>BUTTON</span>
  <svg ... /> // 矢印アイコン
</a>
```

🥳 Good!!

```
.button {
  color: white;
  
}
.button:hover {
  color: blue;
  
}
.button svg {
  fill: currentColor; 
}
```

🤮 Bad...

```
.button {
  color: white;
  
}
.button:hover {
  color: blue;
  
}
.button svg {
  fill: white;
}
.button:hover svg {
  fill: blue;
}
```

clamp()
-------

clamp関数は`vw`などの動的な値に対して最大（最小）値を設定できます。

例えば、フォントサイズに`vw`を指定すると大きく（小さく）なりすぎることがありますが、clamp関数を使うことで最大（最小）の文字サイズを指定できるようになります。ブレイクポイントで`vw`の値を変えるより直感的に扱えます。

🥳 Good!!

```
.text {
  font-size: clamp(16px, 5vw, 20px); 
}
```

🤮 Bad...

```
.text {
  font-size: 5vw;
}
@media (max-width: 767px) {
  .text {
    font-size: 8vw;
  }
}
```

便利なジェネレーターもあります。

<https://min-max-calculator.9elements.com/>

svh
---

要素の高さを画面いっぱいにするには`100vh`ではなく`100svh`を指定します。`vh`はiOSのアドレスバーの高さを含んでしまうので「画面の高さ＋アドレスバーの高さ」になってしまいますが、`svh`はアドレスバーの高さを含まない純粋な「画面の高さ」のみを取得できます。

```
.main-visual {
  height: 100svh;
}
```

<https://zenn.dev/tonkotsuboy_com/articles/svh-dvh-lvh-for-all-browser>

border-radius: 100vmax
----------------------

完全な角丸のボタンを実装する時の`border-radius`には`9999px`などの大きい数値を指定するのではなく`100vmax`を指定することで、ボタンがどんな大きさになっても完全な角丸を保てるようになります。

![](https://storage.googleapis.com/zenn-user-upload/e23ae6c4b5e3-20240507.png)

🥳 Good!!

```
.button {
  border-radius: 100vmax;
}
```

🤮 Bad...

```
.button {
  border-radius: 9999px;
}
```

昨今のブラウザではメディア種別の`screen`を省略しても「画面」と認識してくれるので、メディアクエリの`screen and`は省略しても問題ありません。

🥳 Good!!

```
@media (min-width: 768px) {
  .element { ... }
}
```

🤮 Bad...

```
@media screen and (min-width: 768px) {
  .element { ... }
}
```

また、range記法という記述方法も2023年にリリースされました。

```
@media (width <= 768px) {
  .element { ... }
}
```

<https://zenn.dev/tonkotsuboy_com/articles/css-range-syntax>

iOS Safariのバージョン16.3以下がサポート外なので、使う場合はコンパイラを挟むことを推奨します。

<https://caniuse.com/css-media-range-syntax>

any-hover: hover
----------------

スマホやタブレットなどタップで操作をする端末ではhover処理は無効にします。

タップデバイスを判定するにはメディア特性の`any-hover: hover`を使います。昨今は小さいノートパソコンや大きいスマホなどがあるので、画面幅で判定するのはよろしくありません。

🥳 Good!!

```
@media (any-hover: hover) {
  .button:hover {
    background-color: red;
  }
}
```

🤮 Bad...

```
@media (min-width: 768px) {
  .button:hover {
    background-color: red;
  }
}
```

<https://www.tak-dcxi.com/article/disable-hover-on-mobile-and-hover-implementation-example>

prefers-reduced-motion: reduce
------------------------------

メディア特性の`prefers-reduced-motion`を使うことで、デバイス設定で「視差効果を減らす」が有効かどうかを判定できます。

ユーザーは過度なアニメーションを求めていない場合もあるので、ユーザー側でアニメーションのON/OFFを選択できるように実装してあげることが大切です。

<https://www.webcreatorbox.com/tech/prefers-reduced-motion>  
<https://accessible-usable.net/2021/09/entry_210919.html>

以下は「視覚効果を減らす」が有効化されている時に、アニメーション時間を極限まで短くする例です。

```
@media (prefers-reduced-motion: reduce) {
  *,
  ::before,
  ::after {
    transition-duration: 1ms !important;
    animation-duration: 1ms !important;
    animation-iteration-count: 1 !important;
  }
}
```

Visually Hidden
---------------

Visually Hiddenとは、視覚的には要素を非表示にしたいけど、スクリーンリーダーには読み上げてもらいたい時に使うCSSスニペットです。

```
.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0 0 0 0);
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}
```

<https://qiita.com/randy39/items/fca820d500dfe9ec1a52>

ラジオボタンやチェックボックスの`input`要素を非表示にしてスタイリングする際は、`display: none`ではなくVisually Hiddenを使います。`display: none`で`input`要素自体を消してしまうとフォーカスが当たらないなどの弊害が生じます。

🥳 Good!!

```
[type="radio"] {
  
}
```

🤮 Bad...

```
[type="radio"] {
  display: none;
}
```

<https://web-guided.com/1695/>

親要素の左右にpaddingが指定されている状態で子要素の横幅を画面幅と同じにするレイアウト手法
------------------------------------------------

親要素の左右に`padding`が指定されている状態で、子要素の幅を画面幅と同じにする場合は`calc`と`vw`を使って実装します。

![](https://storage.googleapis.com/zenn-user-upload/44cd626c0fe5-20240512.png)

🥳 Good!!

```
.wrapper {
  padding-left: 40px;
  padding-right: 40px;
}
.photo {
  width: 100vw;
  margin-inline: calc(50% - 50vw);
}
```

従来の書き方だと、以下のように`padding`の値に応じて子要素の`width`や`margin`の値も変わってしまいます。これだと、レスポンシブ時に`padding`の値が変わったら`width`や`margin`も変える必要がありますが、`calc`と`vw`を使うことで再定義が不要になります。

🤮 Bad...

```
.wrapper {
  padding-left: 40px;
  padding-right: 40px;
}
.photo {
  width: calc(100vw + 80px); 
  margin-left: -40px; 
}
```

コンテンツ幅から片方だけ画面の端まではみ出しているレイアウト手法
--------------------------------

このようなレイアウトも`calc`と`vw`を使うことで効率よく実装できます。

![](https://storage.googleapis.com/zenn-user-upload/1c5624f8d20e-20240505.png)

```
.片方だけはみ出させる要素（左配置の場合） {
  width: 50vw;
  margin-left: calc((50vw - 50%) * -1);
}
.片方だけはみ出させる要素（右配置の場合） {
  width: 50vw;
  margin-right: -50vw;
}
```

詳しくはCodepenをご覧ください。

<https://codepen.io/dadada-dadada/pen/JjOXqPZ>

メインコンテンツが少ない状態でもフッターを画面最下部に固定させるレイアウト手法
---------------------------------------

コンテンツ量が少なくてもフッターを画面最下部に固定するレイアウト手法です。

```
body {
  min-height: 100dvh;
}
footer {
  position: sticky;
  top: 100%;
}
```

<https://twitter.com/d151005/status/1729690789343527077?s=20>

3. JavaScript
=============

JavaScriptも画像と同様にパフォーマンスに影響を与えやすい項目なので、ファイルの読み込み方やスクロール時の処理の実装方法などをまずは覚えることをおすすめします。

Defer
-----

`<script>`に`defer`属性を付けると非同期でJSファイルがダウンロードされます。また、ダウンロード開始をできるだけ早くしたいので`</body>`の手前ではなく`<head>`のできるだけ上のほうで読み込ませます。

🥳 Good!!

```
<head>
  <script src="script.js" defer>
  ...
</head>
```

🤮 Bad...

```
  ...
  <script src="script.js">
</body>
```

<https://qiita.com/phanect/items/82c85ea4b8f9c373d684>

また、`type="module"`属性を指定することで、そのファイル内で定義した変数はグローバル変数として扱われなくなります。そのため、他のファイルで同じ変数名を使用していても、名前空間が分離されているのでお互いに影響を与えることがなくなります。

```
<script src="script.js" defer type="module">
```

<https://zenn.dev/kagan/articles/731ca08f45b8c1>

DOMContentLoaded
----------------

JSファイルを`<head>`の中で`defer`を付けて読み込む場合、ページ読み込み時の処理には`DOMContentLoaded`イベントを使うことで、DOMツリー構築完了時の実行が保証されます。これにより、要素の取得エラーなどが発生しなくなります。

`load`イベントの場合は画像などのリソース読み込み完了後に実行されるので、実行タイミングが遅くなってしまいます。即時実行関数は`DOMContentLoaded`とほぼ同じタイミングで実行はされますが、もしJSファイルの読み込み位置が変わったら、その位置によって実行タイミングが変わるので実装時に余計な気を遣う必要が出てきます。

🥳 Good!!

```
window.addEventListener('DOMContentLoaded', () => {
  
});
```

🤮 Bad...

```
window.addEventListener('load', () => {
  
});

(() => {
  
})();
```

Debounce
--------

スクロールイベントやリサイズイベントは実行される頻度が極端に高いので、ブラウザに負荷がかかり画面がカクカクする原因になります。なので、Debounceという手法で実行頻度を減らしてあげます。

debounce関数

```
function debounce(func, timeout) {
  let timer;
  timeout = timeout !== undefined ? timeout : 300; 
  return () => {
    const context = this;
    const args = arguments;
    clearTimeout(timer);
    timer = setTimeout(() => {
      func.apply(context, args);
    }, timeout);
  };
}
```

<https://www.freecodecamp.org/news/javascript-debounce-example/>

以下はリサイズ時にヘッダーを取得する例です。

🥳 Good!!

```
const getHeader = () => document.querySelector('header');
const debouncedFunction = debounce(getHeader)
window.addEventListener('resize', debouncedFunction, false);
```

🤮 Bad...

```
const getHeader = () => document.querySelector('header');
window.addEventListener('resize', getHeader, false);
```

Intersection Observer
---------------------

前項でも書いた通り、スクロールイベントは負荷が高いのであまり使いたくありません。Intersection Observerを使うことで、ブラウザに負荷をかけずにスクロールに応じた処理を実装できます。

<https://ics.media/entry/190902/>

以下はスクロールアニメーションのサンプルで、`data-scroll-anima`属性を持つ要素が画面の上下20%の位置までスクロールされたら属性値が`true`になります。

JavaScript

```
const animaElements = document.querySelectorAll("[data-scroll-anima]");


const doWhenIntersect = entries  => {
  const entriesArray = Array.prototype.slice.call(entries, 0);
  entriesArray.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.dataset.scrollAnima = 'true';
    }
  });
}


const options = {
  root: null,
  rootMargin: '-20% 0px -20% 0px', 
  threshold: 0
};


const observer = new IntersectionObserver(doWhenIntersect, options);
animaElements.forEach((box) => {
  observer.observe(box);
});
```

CSS

```
[data-scroll-anima] {
  opacity: 0;
  transition: opacity .3s;
}
[data-scroll-anima="true"] {
  opacity: 1;
}
```

ブレイクポイントに応じて処理を実行する場合、画面幅をリサイズイベントで監視すると前項で書いた通りブラウザに負荷がかかるので、代わりにmatchMediaを使って今のブレイクポイントを判定します。

また、CSS変数にブレイクポイントを指定しておくことで、CSS側でブレイクポイントの値が変わってもJS側での修正は不要になります。

CSS

```
:root {
  --breackpoint-md: 768px;
}
```

JavaScript

```
const rootStyles = getComputedStyle(document.documentElement);
const breackpointMd = rootStyles.getPropertyValue('--breackpoint-md');
const mediaQueryList = window.matchMedia(`(max-width: ${breackpointMd})`);


const mediaQueryFunction = (event) => {
  if (event.matches) {
    console.log('768px以下です');
  } else {
    console.log('769px以上です');
  }
};


mediaQueryList.addEventListener('change', mediaQueryFunction);


window.addEventListener('DOMContentLoaded', () => mediaQueryFunction(mediaQueryList));
```

<https://zenn.dev/no4_dev/articles/878f4afbff6668d4e28a-2>

Sassでブレイクポイントの変数を定義している場合、以下のようにCSS変数を登録をすれば上記と同じことができます。

Sassの例

```
$breackpoint-md: 768px;
:root {
  --breackpoint-md: #{$breackpoint-md};
}
```

<https://twitter.com/hiro_ghap1/status/1550389210317979649>

375px未満のレスポンシブ対応
----------------

幅320pxのような小さい端末のレスポンシブ対応はCSSで頑張るのではなく、Viewportで表示倍率を縮小します。

昨今のデザインは375pxで作られることが多く、そもそも320px程度まで考慮されていない場合が多いのでCSSで調整するには限界があります。なので、表示倍率を縮小することで実装工数が大幅に削減でき、大量のメディアクエリの記述も発生しなくなります。

<https://liginc.co.jp/451892>

```
const adjustViewport = () => {
  const triggerWidth = 375;
  const viewport = document.querySelector('meta[name="viewport"]');
  const value = window.outerWidth < triggerWidth
    ? `width=${triggerWidth}, target-densitydpi=device-dpi`
    : 'width=device-width, initial-scale=1';
  viewport.setAttribute('content', value);
}
const debouncedFunction = debounce(adjustViewport) 
window.addEventListener('resize', debouncedFunction, false);
```

ES6以降の記法
--------

JavaScriptはES6（ES2015）以降、便利な機能や構文が数多く追加されました。ここからはES6以降に追加されたWeb制作寄りの内容を少し紹介していきます。

<https://qiita.com/soarflat/items/b251caf9cb59b72beb9b>

文字列の結合
------

テンプレートリテラルを使うことで、変数と文字列の結合が楽になります。

🥳 Good!!

```
const message = `私は${name}です。`;
```

🤮 Bad...

```
const message = '私は' + name + 'です。';
```

配列操作
----

配列に関するメソッドはかなり追加されました。新しい配列を生成する`map`、特定の配列を探す`find`、配列の有無を確認する`some`など、これまでは`for`文で行っていた処理をこれらのメソッドを使うことで記述量が圧倒的に短くなります。

```
const users = [
  { id: 1, name: '山田' },
  { id: 2, name: '田中' },
  { id: 3, name: '中村' }
];
```

🥳 Good!!

```
const targetUser = users.find(user => user.id === 2);
```

🤮 Bad...

```
let targetUser;
for (let i = 0; i < users.length; i++) {
  if (users[i].id === 2) {
    targetUser = users[i];
    break;
  }
}
```

スプレッド構文
-------

スプレッド構文を使うことで、配列やオブジェクトの結合や展開が楽になります。

```
let arr1 = [1, 2, 3];
let arr2 = [4, 5];
```

🥳 Good!!

```
let combined = [...arr1, ...arr2]; 


let arrCopy = [...arr1];
```

🤮 Bad...

```
let combined = arr1.concat(arr2); 


let arrCopy = arr1.slice();
```

Async / await
-------------

特定の処理の後に他の処理を実行する場合は Async / await を使います。`setTimeout`で遅延させると、必ずしも遅延させた秒数で手前の処理が終わるとは限らないので絶対に辞めましょう。

🥳 Good!!

```
async function fetchData() {
  const response = await fetch('https://api.example.com/data');
  const data = await response.json();
  return data;
}

async function run() {
  try {
    const data = await fetchData(); 
    console.log('取得したデータ:', data);
  } catch (error) {
    console.error('エラーが発生しました:', error.message);
  }
}

run();
```

🤮 Bad...

```
function fetchData() {
  
}

async function run() {
  const data = fetchData(); 
  
  setTimeout(() => {
    console.log('取得したデータ:', data);
  }, 2000);
}

run();
```

<https://qiita.com/soarflat/items/1a9613e023200bbebcb3>

Fetch / Axios
-------------

APIなど外部からデータを取得する時は`Fetch`か`Axios`を使います。昔は`XMLHttpRequest`やjQueryの`Ajax`を使っていましたが、`Fetch`や`Axios`のほうが例外処理やデータの扱いに優れています。

🥳 Good!!

```
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
```

🤮 Bad...

```
const xhr = new XMLHttpRequest();
xhr.open('GET', 'https://api.example.com/data');
xhr.onload = function() {
  if (xhr.status === 200) {
    console.log(xhr.responseText);
  } else {
    console.error('APIエラー');
  }
};
xhr.onerror = function() {
  console.error('ネットワークエラー');
};
xhr.send();
```

[https://zenn.dev/syu/articles/9840082d1a6633#1.インストール方法](https://zenn.dev/syu/articles/9840082d1a6633#1.%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E6%96%B9%E6%B3%95)

petamorikenさんから[コメント](https://zenn.dev/link/comments/aab60f7236a765)をいただいたので追記です。

非同期処理には中断する処理が必要不可欠です。`AbortController`を使い、タイムアウトしたら中断するような処理も同時に実装するようにしましょう。

```
const controller = new AbortController();
const timeoutId = setTimeout(() => controller.abort(), 5000); 

fetch('https://api.example.com/data', {
  signal: controller.signal
})
  .then(response => {
    clearTimeout(timeoutId); 
    return response.json();
  })
  .then(data => {
    console.log('Success:', data);
  })
  .catch(err => {
    if (err.name === 'AbortError') {
      console.log('Request timed out');
    } else {
      console.error('Error:', err);
    }
  });
```

<https://developer.mozilla.org/ja/docs/Web/API/AbortController>

最後に
===

かなりの量を紹介したので一度に全部を使いこなすのは難しいと思います。個人的にこれだけは...をいくつかピックアップしたので、まずはそれだけでも取り入れてみてください。

* **1. 画像**
  + Lazy loadingで遅延読み込みをして、画像の出し分けはPicture要素を使う
  + 背景画像ではなくImg要素で読み込み、要素いっぱいに広げる時は`object-fit`、縦横比を制御するには`aspect-ratio`を使う
* **2. レイアウト**
  + 格子状のレイアウトはGrid Layoutを、Flexboxの間隔は`gap`を使う
  + 状況に応じて`calc()`と`vw`を組み合わせてレイアウトを組む
* **3. JS最適化**
  + JSファイルは`Defer`で読み込み、処理は`DOMContentLoaded`イベント内で行う
  + スクロールやリサイズのイベントは高負荷なので、Debounceで実行回数を間引く
  + スクロール時の処理は`Intersection Observer`を使う

参考
==

こちらは普段私が情報をキャッチアップしている方々のサイトです。とても勉強になるので是非訪れてみてください。

<https://ics.media/>  
<https://www.tak-dcxi.com/>  
<https://baigie.me/engineerblog/>  
<https://zenn.dev/tonkotsuboy_com>  
<https://zenn.dev/takamoso>  
<https://zenn.dev/yusukehirao>

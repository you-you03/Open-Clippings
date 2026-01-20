---
title: "GPTsをBubble(ノーコード)でアプリ化した話｜KIRIKO.tech株式会社"
source: "https://note.com/kiriko_tech/n/n0b37a403be8f"
author:
  - "[[note（ノート）]]"
published: 
created: 2025-09-03
description: "以下の記事は、4月の初めに書いたもので、その後GPTsが一般公開されるというのでなん～だボツか…となったんですがGPTsアプリ化はアプリ化でおもしろいし需要もあるということで公開します。  こんにちは！KIRIKO.tech(株)代表の佐藤です。  すっかりこのnoteでは、GPT、生成AIの人となっていますが、我々アプリ開発屋でもあります！  


ちょいてつ - もっともお手軽なクラウドソーシングサイト


【TYOITETU(ちょいてつ)】は気軽にちょいっとお仕事の募集や応募ができるサイト。 作品みて！映画どうだった？ツーリン


www.tyoitetu.com



 
 こ"
tags: ["ai", "プロダクト", "clippings", "gpt"]
image: "assets/rectangle_large_type_2_3271da850604b82ce1d9d5201202cd0c.png"
---
**以下の記事は、4月の初めに書いたもので、その後GPTsが一般公開されるというのでなん～だボツか…となったんですがGPTsアプリ化はアプリ化でおもしろいし需要もあるということで公開します。**

こんにちは！[KIRIKO.tech(株)代表の佐藤](https://twitter.com/KIRIKO_tech)です。

すっかりこのnoteでは、GPT、生成AIの人となっていますが、我々アプリ開発屋でもあります！

このWebサイトもノーコードで開発したサイトです。  
今年で3年目(もうそんなに経った！？)になりますが、あたたかいユーザーさんに支えられて今でもちゃんと運営できています。

よければ、遊びにきてください！

さて、本題に。

そうなんです、我々アプリ開発屋なんです！

ということでGPTを活用したアプリが何か作れないかと日々考えていました。

そこで、思いついたんです。**そうだ、GPTｓをアプリ化しようと。**

  

GPTｓをアプリ化？
----------

### きっかけ

そもそもGPTｓをアプリ化するきっかけはどこだったのか。

~~それは単純にGPTｓって有料ユーザーしか使えないよね・・・。ってところにありました~~。

※6月1日付現在GPTsは、無料ユーザーにも解放されるようになりました！！

今やGPTｓはその人が求めれば、求めただけの能力を発揮してくれます。  
すなわち、その人にとってスペシャルな専用アプリができる、できているに等しい。

だけども、それは有料のGPTユーザーしか使えないわけです。

そして、そのパフォーマンスの大きさも一部のユーザーしか知らない。

少し話はずれますが、最近のAI界隈の流れをみると新規の人ってあまり見ないんです。

何が言いたいかというと、もともとGPT使っていた人がGPTsを作り、便利にGPTを使い倒しているといった感じ。

あれです、ゲームでいう１，２，３と新作が出てくるじゃないですか？

多少の新しいプレイ友達は増えようと**基本的には同じメンツで盛り上がっているだけみたいな感じです。**

どうすればこのゲーム(GPTs)のおもしろさ、友達を増やすことができるのかと考えた結果、そうだGPTsをアプリ化して使ってみてもらえばいいじゃん！と思ったわけです。

### アイディアと発想

アプリを作る時に悩むというか、僕の開発の起源ともいえる部分はここです。

どのようなアイディア、発想、動きをさせていくか。

今回はそれに対してあまり悩むことがなかったのも嬉しい気づきできした。

なぜならGPTsを作ればいいだけ、その動きをアプリでするだけだから。

なんならUIデザインも頭を悩ます部分ではあったのですが、これもインスパイアGPTsの画面でいいじゃないか、寄せれば解決じゃんとなりました。

**すごい、すいすい進む**

それでは、いざ作ろうとなりましたそれでは何のGPTsについて作るか。  
作るからには短期で開発したいので、あまり複雑な動きをしたりするのはご法度です。

さらに、なんなら実際に使えるものが望ましい。

アプリ開発をしていて思うのがやはり、アプリは実際に使われてナンボだということです。使われてみて初めて命が宿るというか。

そのため、僕らの日常に近しいものがいいなぁと思いました。

そんな感じで見ているとあったんです、絶好のやつが。

### My English 問題集 GPTs

このGPTsはシンプルに日本語文をひたすら英語翻訳して練習できるものとないります。  
練習した問題と解答のポイントも教えてくれたり。

以下参考まで。

![](https://assets.st-note.com/img/1712663537720-dWepbzJcjc.png?width=1200)

フィードバックもしっかりしてる！

続けて理解度チェック問題から、新しい問題まで延々と出題してくれます。

このGPTs作っといてなんですが、普通に使えるじゃんって思いました。

なんなら受験生の時にこれがあったら自分延々と英語の練習してますもん。

そういえば最近こんなYahoo！の記事が

このGPTsは本来の作成目的である**僕らの日常に近しいものがいい**という思いにピッタリ合致していたので早速これをアプリ化することで決めたのです。

それでは、早速このGPTsをアプリ化していきましょう。

開発環境はBubble
-----------

やはり、ここはスピード感を意識してノーコードのBubbleで開発していこうと思います。

肌感、ローコードのJavaScript、Python等でもcursorとAIを使えばゴリゴリにコードは書けてしまうのでそれでも開発出来なくもないですが、

> 「最終的な「開発のあるべき姿」を考えるとやはり環境構築不要・インフラ構築不要な今のノーコード開発の延長線上にある気がしている」

僕も[株式会社Walkers代表つかささん](https://twitter.com/tsukasa_hiraga)の意見には共感します。  
AIツールの発達はすさまじいものがありますが、やはり確かなものとなるのはノーコードでの開発になってくるのではなのかと。

もちろん、僕の個人的なノーコード、Bubbleへのえこひいきもあるのでそこはご愛嬌。

ちなみに当社のイメージキャラクターは

### ノーコードガールズ

という素敵な女性たちになっています。そう、noteプロフィールのヘッダーたちです。

![](https://assets.st-note.com/img/1712669487531-2vijYKLpli.jpg?width=1200)

彼女はBubbleで開発が得意なのでバブル姉さんと呼ばれています

こんな感じでグッズ展開もしてますので、応援してくださると泣いて喜びます・・・(´;ω;｀)

スタンプもあるよ！

ノーコードガールズは、序盤に紹介した**「TYOITETU」「ちょいてつ」**から生まれました。

どうやってこのWebアプリを世に知らしめることができるのか、試行錯誤の上、生まれたキャラクターでした。

3年経った今、大変ありがたいことにユーザーさん達にも認知され、ノーコード界隈では対面にて知ってるよとおっしゃってくれる方々も増えてきました。

本当に嬉しい限りです。また機会があればこの辺りのこともお話できていければと思っております。  
いやぁ**歴史できてるぅぅぅぅぅ～～**

さて、また脱線しましたが話を戻しそれではBubbleで開発していこうとなりました。

スピード感、安定感、再現性とどれもとってもBubbleは最強のノーコードツールだと思っています。  
  
強いていうならネイティブ化という、いわゆるアップルストアとかグーグルストアで並ぶアプリを作るのに限っては少し弱い部分でしたがそれも近々AI化とともに改善されるとのこと。

**バブル姉さんと同じく、ウチもbubbleで開発したるで**

それでは大変前置きが長くなりましたが、Bubbleの開発画面を開きます。

開発過程を公開
-------

専門的な解説記事はホントお世話になっている[ノーコードラボさん](https://blog.nocodelab.jp/)をご参考いただくとして

この記事では、へぇ～こんな感じで作ってるんだぁ～っていう**ライブ感**を楽しんでください！

大切なのはこんな風に作っているんだぁ～っていう**ライブ感**です！ **この記事において大切なことなので2回言いました！！**

~~お前詳しく説明するのめんどくさいだけでは←というツッコミはなしです~~

### UIデザイン

さて、それでは早速作っていきます。

当初の目的通りUIはGPTに寄せていきます。

こんな感じ

index画面のContainer layout は**基本的にrawかColumu**にしておきましょう！

![](https://assets.st-note.com/img/1712844844335-xfMAx9i5oE.png?width=1200)

基本的にFixedは使わない方向でいきます。

フッターを作ります  
このフッターはGPTでいう入力欄と送信画面を入れるところです。  
フッターなのでFloating Groupを使います。

![](https://assets.st-note.com/img/1712845096879-jBNuvoMmir.png?width=1200)

横幅いっぱい

レイアウトは中ものを横に並べたいのでrow  
横一杯にしたいのでFixed widthのチェックを外します

![](https://assets.st-note.com/img/1712845305454-YWLIEXsyoN.png)

Appearanceでボトムにもっていきます

この時点でGPTっぽくなってきている気がします、気のせいだけかも

![](https://assets.st-note.com/img/1712845478408-uAWPz6wzUr.png?width=1200)

ボトムにインプットとボタンを設置します

### プラグインの動作確認

ここで今回はGPTと連携させたいのでちゃんと連携できるか見てみましょう

ここで動かないと、作る意味がないので開発する上で早めに確認しておきます

意外とこの辺りは、躓きがちです

開発されたままアップデートされていないプラグインも多かったりするので・・・

それでは、その為のテキストを適当に用意

![](https://assets.st-note.com/img/1712847006157-UGZLUalGz4.png?width=1200)

適当にグループを用意

![](https://assets.st-note.com/img/1712845708302-GHKvMHAo7k.png)

グループの中にテキストを入れます

それではプラグインをインストールしてみましょう

OpenAIで調べると出てきます

![](https://assets.st-note.com/img/1712845880395-zHMqDscH8s.png?width=1200)

たくさんありますねー

本当は公式からだしているプラグインがよっかたりするのですが、ないのでインストール数が多いものから試していきます。

ちなみに公式のロゴを使っていて、**いかにも公式っぽいやつ**みたいなも多く存在します

![](https://assets.st-note.com/img/1712846044107-O6pXy9u9o6.png?width=1200)

シークレットキーを出力

開発画面のプラグインの項目に戻ります。

![](https://assets.st-note.com/img/1712846089643-QHz9Iansoz.png?width=1200)



![](https://assets.st-note.com/img/1714751419612-GjXG7qXz1G.png?width=1200)

ここに先ほど取得したAPIキーをいれます。

**⁂注意　先頭にBearer　スペースをいれててからキーを入力してください  
それじゃないと正常に動作しません**

ここで結構な時間を喰ったのは秘密、、、

そして、この時はこのプラグインではうまく行きませんでした　(\*´Д｀)

なので再度、試します

![](https://assets.st-note.com/img/1712846605180-7SgyNA97wP.png?width=1200)

似たようなのばっかりなんじゃ～～

こういったことは日常茶飯事なので、もう慣れです慣れ(経験者は語る)

![](https://assets.st-note.com/img/1712846665071-pHRdDPxxq9.png?width=1200)

なんだかうまく行きそうな予感がするので、ワークフローに移ります

![](https://assets.st-note.com/img/1712846768311-deYPePQLRa.png)

OpenAI Create chat compietion Default Settings (for beginners) を選択

![](https://assets.st-note.com/img/1712846809166-NTU71XZyTM.png?width=1200)

(body)messagesの部分はInput A's value

![](https://assets.st-note.com/img/1712846903300-OnGMu9A0oI.png?width=1200)

次なるアクションを設定します

Elemet Actions のDisplay data を選択

![](https://assets.st-note.com/img/1712847101577-LGcvFAJpq9.png?width=1200)

Element  はGroup text

Data to display を設定

それでは画面に戻り、Text のAppearance を設定

![](https://assets.st-note.com/img/1712847164067-fMe28HH6uG.png)

これでイケてるはずです・・・  
さて・・・頼むで・・・

**「おはよう」**と打ちこんで送信ボタンをクリック

ここでGPTのように返事がかえってこれば成功なのですが・・・。

返ってきた返事は

**おはようございます。こんにちは、何かお手伝いできることはありますか？**

よし！とりあえずは動くことが確認できました、成功です。

![](https://assets.st-note.com/img/1712847487877-iw6SQzyinU.png?width=1200)

いいですね！成功です。

### データベースを構築①

さて、ここでプログラミングやBubble等のノーコードを知らない方は、これでGPTと結びついたならもうGPTの動きをそのまましてくれるんじゃないの？  
なんて思ったんではないでしょうか。

一応、GPTの動きはするのですが、これだとGPTに一回質問をした、利用した動きしかしません。

Chat-GPTを使ったことある人なら前後の文脈をＧＰＴは理解して解答しつづけてくれますよね。

**これだと先ほども言った通り、GPTに一回質問をした、利用した動きしかしないんです。**

なにそれ！だめじゃん！！アナタ言ったじゃんGPT動きデキルよ、でも出来てないじゃん

でも問題ナイナ、そのためのデータベースを構築ナ  
~~↑ナゼカタトコ~~

前後の会話の文脈をもたせて会話させたいですよね、そこでその会話を記憶させるためにデータベースを作成します

![](https://assets.st-note.com/img/1713080651258-6nQOxpUlSx.png?width=1200)

Data Type を作成します

全体の会話を保存するAll Messages

前後の会話を保存する Messages

の２つを作成します

![](https://assets.st-note.com/img/1713080780710-nt84n5rkYf.png)

All Messages にはMessagesというfield を作成します  
Field type はMessages　  
多くの会話が格納されると想定されるのでlistにチェックを入れます。

同じようにMessagesにもFieid  を設定します。

![](https://assets.st-note.com/img/1713081036870-7Yxgqz7OXg.png)

誰が発言したかの発言者を設定

ここでいうrole はロールプレイングゲームのロールかナ？くらいのイメージをしてください

![](https://assets.st-note.com/img/1713081110082-CzIwzf2bcM.png)

会話の内容を設定

それでは、これらのデータをテーブルで表示させましょう

RepeatingGroup を設置します。  
名前はChat Content とでもしておきましょう。

![](https://assets.st-note.com/img/1713081355137-PMwKXYZ2d4.png)

会話を表示させたいので、Type of content はMessages

![](https://assets.st-note.com/img/1713081714619-tbQIvYNahH.png?width=1200)

今回はあくまでChatGPTのような動きをするアプリを作成するでした。

なのでできるだけ、そのChatGPTのUIデザインに近づけていきます。

set field number of rows のチェックを外します。  
そうすることで、続いていく会話を常に表示させます。

Data sours はDo a Search for でMessagesを選択

会話を新しい順に表示させていきたいので、Sort by を Created Date にしてDescending を”yes”にします

![](https://assets.st-note.com/img/1713082470627-TVQl8QPKFi.png)

ここでいうroleはあなた

GPTでいう

![](https://assets.st-note.com/img/1714754938380-MzwbkxjXai.png)

ここの部分を指します

![](https://assets.st-note.com/img/1713082492187-ki0UB01Bc9.png)

そして、このContentは

![](https://assets.st-note.com/img/1714755001651-sn96JheGhz.png)

ここになります

### ワークフローを設定①

それでは、送信ボタンのワークフローに戻り設定していきます。  
先ほどのは、ちゃんと動作しているかの確認用なので消します。

![](https://assets.st-note.com/img/1713082539137-oVxtDCgAzG.png?width=1200)

これは削除

ここでカスタムイベントを設定します。

![](https://assets.st-note.com/img/1713083151368-QrCUyLMiAu.png)

Customを選択

カスタムイベントを設定する理由としては、ワークフローが長くなることを防ぐこととこのイベントを他のワークフローに使いまわしが出来ることが挙げられます。

![](https://assets.st-note.com/img/1713082847308-legvXrjQOi.png?width=1200)



![](https://assets.st-note.com/img/1713082938168-scQ4WVNy7l.png?width=1200)

引数も設定します

全部の会話履歴に合わせて、新しい自分の会話のテキストですね  
これをGPTに渡してやります

![](https://assets.st-note.com/img/1713083224885-y0P7KKSVC4.png)



![](https://assets.st-note.com/img/1713083294076-HJEPa6OaQA.png?width=1200)

ユーザーが作成したメッセージをAIIメッセージに格納します。

イメージとしては、これにより会話の文脈が作成されます。

![](https://assets.st-note.com/img/1713083333607-TrH6gfj3pR.png)



![](https://assets.st-note.com/img/1713083458443-zBtbXLAraC.png?width=1200)

これにより、文脈に会話が追加されました。

![](https://assets.st-note.com/img/1713083519000-3vQuMbOcs2.png?width=1200)

JSONモード

![](https://assets.st-note.com/img/1713083637701-RMYIU8vjZV.png)

ここのMessagesを書きかえていくのですが、ごちゃごちゃやばいので

![](https://assets.st-note.com/img/1713083694741-L9ffIwMvrn.png)

Arbitrary text

![](https://assets.st-note.com/img/1713083962790-zWxrECX3dr.png?width=1200)



![](https://assets.st-note.com/img/1713084108573-PHlJVJDpEk.png?width=1200)

JSON-safe まじ大事

![](https://assets.st-note.com/img/1713084162598-oj3eLsi6Hg.png?width=1200)

Delimiter に　半角の　,　を入れて

![](https://assets.st-note.com/img/1713084235917-KVDFbBg7gA.png?width=1200)

GPTからの応答を作ります

![](https://assets.st-note.com/img/1713084366346-BgN3xVqtbw.png)



![](https://assets.st-note.com/img/1713084423041-LcYXNTij0u.png)

これでカスタムイベントは完了です、なのでこれを送信ボタンに組み込みます

送信ボタンのワークフローに戻り

同じようにクリエイトnew thingでこの動作を入れます

![](https://assets.st-note.com/img/1713084694886-Fprb6AQQuJ.png)

カスタムイベントでオールメッセージを渡す為に、空っぽの時は作成するようにします。

それでは、カスタムイベントを組み込みます

![](https://assets.st-note.com/img/1713084860473-22xYxcatXf.png)



![](https://assets.st-note.com/img/1713084918261-ZlFm4EVOBv.png)

text は書き込んだものを反映させたいのでinput  のvalueを選択

それでは、実際の動きを見てみましょう

![](https://assets.st-note.com/img/1713085432265-jyRNsL1ncg.png?width=1200)

assistantからの返事が来ず・・・失敗ですね

原因を追究していきます

![](https://assets.st-note.com/img/1713085486245-pNgoVW6Jfi.png?width=1200)

カスタムイベントのステップ４を変更  
APIからの要求を全てメッセージズに入れてみます

すると

![](https://assets.st-note.com/img/1713085534613-EGPC2TMHYC.png?width=1200)

こんな返事がかえってきました。  
このエラー内容からJSON関係の不具合だとわかります。

なのでStep３を見返します。  
よくみるとこの(JSONモード)はJSONを返すもの専用の機能だったので通常の(JSONじゃない方に書きかえてみましょう)

ただこのようになってしまった場合でもやることはただのコピペでいいので、焦らず焦らず

ステップ３の隣の→をクリックして新しいワークフローを作成します。

![](https://assets.st-note.com/img/1713087583648-L6kSFvXXdD.png?width=1200)

JSONじゃない方

先ほど作った方をCopyして

![](https://assets.st-note.com/img/1713087683720-Ip6vtma6Y1.png)



![](https://assets.st-note.com/img/1713087786471-xRIvb8KWVa.png)

Dynamic data を押して全文削除、Searchの中で左クリックを押してください

Paste expression を選択するとそのまま張りつけてくれます

そしてJSONの方を削除します。

すると、このようなエラーメッセージがでます

![](https://assets.st-note.com/img/1713088040658-mzB0ve3RSA.png?width=1200)

これは単純に、先ほど設定したものを消したので、新しく作った方のデータがないといっているので

Result of step 3 を再度していしてみれば消えます。

それでは、再度動作確認をしてみましょう。

![](https://assets.st-note.com/img/1713088367167-3kaquHLdUE.png?width=1200)

しっかり返ってきました！！

これからJSON関係でミスっていることがわかりました。

なのでその辺りを確認します。

### My English GPTs 問題集の動きをさせる

それでは、GPTを使っての前後の文脈の構成部分はできました。  
それでは、目的であるGPTsの動きを実装していきましょう。

早速ボタンを用意します。  
GPTsのスターターにならい初級問題スタートとでもしておきましょう。

![](https://assets.st-note.com/img/1713096920947-3KlJR687o8.png)

このボタンにワークフローを追加していきます。

![](https://assets.st-note.com/img/1713096979330-tfTfHfqTH6.png)



![](https://assets.st-note.com/img/1713097166303-s6ZubD9gUK.png?width=1200)

この辺りがGPTsのインストラクションに当たる部分になります。  
お好きなようにカスタムしてください。

![](https://assets.st-note.com/img/1713097276271-x6KARY7fS3.png?width=1200)

次も同じように　create new things でAll messages を選択

![](https://assets.st-note.com/img/1713097334945-6TwRkGXlsx.png?width=1200)

第三ステップでトリガーイベントを呼び出します。

![](https://assets.st-note.com/img/1713097433051-wKMmia0hYc.png?width=1200)

さらに最新の文脈に対して返答してほしいので送信ボタンから渡すAII messages のディセンディングをYesにします

![](https://assets.st-note.com/img/1713097892931-48nsR3jDkR.png?width=1200)

こんな感じ

![](https://assets.st-note.com/img/1717249415537-DOptU6Fwsf.png?width=1200)

最後にTrigger send message を呼び出して完了です。

こんな感じの挙動になります！

お蔵入りするのも、もったいないので掘り出しましたｗ

結びに(6月2日、記述)
------------

いかかだったでしょうか？  
中盤くらいから、若干というかかなりの駆け足でした。

GPTsが一般公開されると聞いた時は、な～んだならアプリ化の必要性や意味は全くなくなったんだな…とか感じたのですが、やはりアプリ化はアプリ化でAIに馴染みのない人やその他＋αの動きをさせるという点でもとても意味があると思います。

**GPTsは、あくまでGPTsのＵＩによる、シンプルかつ独自性のある強み**

**アプリ化は、UＩによる作り込みからその他、機能のオリジナリティを出せる**

というところでしょうか。

今後もアプリ化していこうと思います。

それでは、また皆さんお会いしましょう！！

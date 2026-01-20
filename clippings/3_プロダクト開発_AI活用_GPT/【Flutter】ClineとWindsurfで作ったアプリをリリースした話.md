---
title: "【Flutter】ClineとWindsurfで作ったアプリをリリースした話"
source: "https://zenn.dev/hyshu/articles/1f2b18be3f764b?redirected=1"
author:
  - "[[Zenn]]"
published: 
created: 2025-09-03
description: ""
tags: ["ai", "プロダクト", "clippings", "gpt"]
image: "assets/og-base-w1200-v2.png"
---
Claude 3.7 Sonnet に植物の日記アプリを作ってもらいました。

<https://apps.apple.com/jp/app/id6743403963>

<https://play.google.com/store/apps/details?id=com.dotpx.plantdiary>

私は盆栽をしているのですが、水やりと肥料の管理って大変なんですよね。  
一つのカレンダーアプリで管理すると仕事と盆栽が混ざって嫌ですし、専用のアプリが欲しいと思ったのでした。

まずはプロジェクトの準備
============

完全に0からFlutterプロジェクトを作ってもらうことも出来ますが、費用がかなり増えるのでベースとなるプロジェクトを用意しておきます。  
費用を気にしない方には不要な話なので折りたたんでおきます。

プロジェクトのセットアップ

設計に合わせてディレクトリーを作る
-----------------

先に設計をディレクトリーで作って「設計はディレクトリーを参考にしてください」と指示すると費用が抑えられます。

```
lib
├── application
│   └── usecase
├── domain
│   └── entity
├── feature
│   ├── diary
│   │   └── presentation
│   │       ├── component
│   │       ├── inherited_widget
│   │       └── page
│   │       └── view_model
│   ├── home
│   │   └── presentation
│   │       ├── component
│   │       ├── inherited_widget
│   │       └── page
│   │       └── view_model
│   └── plant
│       └── presentation
│           ├── component
│           ├── inherited_widget
│           └── page
│           └── view_model
├── infrastructure
│   └── db
└── main.dart
```

今回はタブごとに機能が分かれる構造になりそうなので、`feature`もそれに合わせて分けました。  
ディレクトリーの新規作成は禁止しないので、必要に応じて新しく作ってくれます。  
Claude 3.7 Sonnet は一つのファイルにずらーっとコードを書いた方が効率的なのですが、同時に出力上限にも引っかかりやすくなるため、ViewModelを作って分散させるようにします。

pubspec.yamlにパッケージを追加
---------------------

`pubspec.yaml`にも同様にパッケージを追加しておくことで、プロンプトの節約と使うパッケージの制限を行います。  
プロンプトには「**pubspec.yamlの編集は禁止です。既に追加しているパッケージのみを使用してください**」と書きます。

pubspec.yaml

```
name: plantcalendar
description: ""
publish_to: "none"
version: 1.0.0+1

environment:
  sdk: ^3.7.0

dependencies:
  cupertino_icons: ^1.0.8
  drift: ^2.26.0
  drift_flutter: ^0.2.4
  flutter:
    sdk: flutter
  image_picker: ^1.1.2
  path: ^1.8.3
  path_provider: ^2.1.5
  signals: ^6.0.2
  sqlite3_flutter_libs: ^0.5.20
  table_calendar: ^3.2.0

dev_dependencies:
  build_runner: ^2.4.15
  drift_dev: ^2.26.0
  flutter_lints: ^5.0.0
  flutter_test:
    sdk: flutter

flutter:
  uses-material-design: true
```

最近はAPI通信にRiverpod、それ以外の状態管理にSignalsを使うことが多いのですが、今回は通信処理がほぼ無いのでSignals一本で作っていきます。  
ルーティング用のパッケージも必要なほど複雑ではないので、Flutter標準のAPIで済ませます。  
定番パッケージである`freezed`が無い理由は後述します。

`flutter pub get`も実行しておきます。

main.dartをシンプルにする
-----------------

エラーが出ない範囲で最小構成になるようにします。

main.dart

```
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) => MaterialApp(home: Scaffold());
}
```

`ios`か`android`ディレクトリーを退避し、シミュレーターを立ち上げる
----------------------------------------

`ios`と`android`のどちらもディレクトリー内にファイルが沢山あってプロンプト代が増えるので、使わない方をプロジェクトの外に退避させます。  
Claude 3.7 Sonnet は`flutter run`することがあるのでシミュレーターを立ち上げておきます。今回はターミナルへの出力が少なめなのでiOSシミュレーターにしました。

プロジェクトが出来たら何度も使うのでコピーを作っておきます。

Clineが `flutter run` を実行できるように、iOSかAndroidシミュレーターは起動しておいてください。

Windsurfでプロンプト作り
================

最初からClineで作り始めると非効率なので、まずはWindsurfで色々試しながらプロンプトを考えます。  
Cursorでも良いのですが、Windsurfの方がプロジェクト全体の把握の仕方などがClineと似ているため、ずれが生じにくいです。  
あと私的な事情ですが、Cursorの方が細かく範囲指定できるため業務で使うことが多く、あまりクレジットを使いたくないというのもあります(^\_^;)

プロンプト作りは「**Flutterで植物の日記アプリを作成してください。**」から始めて、プロンプト実行時の動作を基に必要な項目を箇条書きで付け足していきます。  
仕様漏れが無いように作るというより、Claude 3.7 Sonnet が出来ないことを潰していく作業に近いです。

例えば`freezed`と`drift`というパッケージにはモデルクラスを作る機能があるので、両方を入れると同名のクラスを作ろうとしてエラーになり、修正できずにループしてしまいました。  
一応プロンプトの指示で解消できますが、そうなるとどちらのパッケージを使ってモデルクラスを作るのかの条件指定が必要になり、結構大変です。  
今回は`freezed`を使うほどでも無いので`drift`一本で作ることにしました。

今回は不要でしたがAPIドキュメントを渡してAIが参照できるようするのも有効です。  
一回のプロンプトによる指示で、希望しているアプリを最後まで作ってくれるようになったら完成です。

出来上がったプロンプトは以下になります。

```
Flutterで植物の日記アプリを作成してください。

# 設計
・pubspec.yamlの編集は禁止です。既に追加しているパッケージのみを使用してください。
・設計は`lib`にあるディレクトリーを参考にしてください。
・UseCase、EntityをViewに受け渡すにはInheritedWidgetを使用してください。
・`signals`を使用したViewModelを利用してください。
・日記は`drift`でdiaryテーブルに保存します。
・クラスとメソッドとメンバー変数に対し、適切なドキュメントコメントを英語で書いてください。
　Example:```
/// Sum two numbers
/// - [left] The first number
/// - [right] The second number
/// - Return: the sum of [left] and [right]
int sum(int left, int right) {
}```
・処理に対しても適切に英語のコメントを加えてください。
・アプリ内のテキストは日本語にしてください。
・`NativeDatabase.createInBackground`を使用するには`package:drift/native.dart`をインポートします。

# 機能
・植物の名前と画像、水やりと肥料の間隔を登録して管理できるようにします。
・日記は文章に加えて、どの植物に水やりをしたか、肥料をやったかの記録が出来ます。
・日記は編集と削除が出来ます。削除する時は確認ダイアログを表示してください。
・本日または本日より前であれば日記が作成できます。
```

かなり短いですが、これには意図があります（後述）

ちなみにコメントの書き方など、文章での説明が難しいところはExampleで示すと上手く解釈してくれます。

このプロンプトだと`InheritedWidget`に対する指示が不十分で、高確率でシミュレーターで実行時にエラーを起こすのですが、簡単に手作業で修正できるものなので敢えてこのままで行きます。

同じアプリを何個もClineに作ってもらう
=====================

一度のプロンプトでClineにアプリを作ってもらうことに成功したら、同じアプリを何個も作ってもらいます。

私がふわっとした完成イメージしかないためです(^^;  
色々な植物日記アプリを作ってもらえば比較検討しやすいですよね。

実はプロンプトを短くしているのもこれが理由で、詳細で適切な指示をすると出来上がるアプリは指示した通りになるのですが、その分アプリの幅は狭まりますし、プロンプトを作るのに時間も掛かります。  
再現性が高いのはもちろん良いことですが、**ほど良い緩さで指示を出した方がAIもアドリブを効かせてくれやすくなります**。一長一短ですね。

今回は5個作ってもらいました。

![アプリのスクリーンショット（植物日記アプリ５つ）](https://res.cloudinary.com/zenn/image/fetch/s--iNqlyeen--/https://storage.googleapis.com/zenn-user-upload/deployed-images/6983d6cef170a4bbbb0d03ee.webp%3Fsha%3D62ebb42000eb42d23ac8af3c1f0f7c7ddffc4907)

全てのアプリから良いとこ取りする
================

どのアプリもUIが違っていて面白いのですが、今回は1番目をベースにすることにします。  
内部処理が一番良く出来ているように見えるのと、UIが無難で使いやすそうなためです。

Widget単位でコピペしていけばそのまま移植できるので、気に入ったUIをポチポチと1番目のアプリに移していきます。

ちなみに内部設計はどれも似通ってることもあり、ページを丸ごと他のアプリから移植したい時は、  
丸々コピペして「**◯◯\_page.dartのエラーを修正してください**」と書くだけでOKです（今回はしませんでしたが）

![アプリのスクリーンショット（植物日記アプリClineによる完成版）](https://res.cloudinary.com/zenn/image/fetch/s--9k259AoN--/https://storage.googleapis.com/zenn-user-upload/deployed-images/95bb4019837e395afb91347c.webp%3Fsha%3De811ce460365a1abd897a643740245f0c1732feb)

余談ですが、5番目のアプリの、アイコン付きで「水やりが必要な植物」などと書かれているUIも良かったのですが、今後項目を増やしていく際にハードコーディングだと厳しそうなので今回は見送りました。  
どこかのタイミングで実装する予定です。

リファクタリングと不具合修正
==============

不具合があるのと、このまま更にAIに書かせるとコードがごちゃごちゃになるので一旦整理と修正をします。

特に指示をしなければ、Claude 3.7 Sonnet はWidgetをある程度の粒度でメソッドにして書いてくれるので、これをそれぞれ別ファイルにします。  
Clineで作る際にプロンプトで指示して分けてもらうことも可能ですが、費用が大幅に増える上に品質も落ちてしまいます。  
「**\_buildXXをStatelessWidgetとして切り出し、`component`ディレクトリーに移してください**」と指示すればやってくれます。

#### タブを独立ページにする

`HomePage`、`PlantPage`、`DiaryPage`に分かれているのですが、タブのUIや切り替え処理は`HomePage`内に書かれていたので`MainTab`として独立させます。  
これはプロンプトで指示しておくべきでしたね。

#### 引数で`dynamic`になっているところを直す

モデルクラスの`Diary`と`Plant`をView側で使う際、プロパティーの`id`をModel側では`int`型で扱っているのにView側では`String`で扱おうとしたために上手くいかず、`dynamic`にすることで対処したみたいです。そんなバカな…。  
もちろん当該箇所ではエラーが起きます。  
とはいえ`dynamic`を検索してクラスに置き換えていくだけです。

リリースまでの追加作業
===========

アプリ自体はこのまま出しても審査に通るくらい出来上がっていますが、まだ追加でやることがあります。

更にデザインを良くする
-----------

Clineはアプリの機能や画面設計に注力するためか、UIがところどころ質素な見た目をしています。

![アプリのスクリーンショット（ダイアログ周りが簡素な見た目をしている）](https://res.cloudinary.com/zenn/image/fetch/s--Zv-rQKgf--/https://storage.googleapis.com/zenn-user-upload/deployed-images/55d45019419952406efa7d4a.webp%3Fsha%3Dd2c9d3a54b49cc994cd44aed8ffe34d02468e4f9)

改善は簡単で、Windsurfに「**◯◯の見栄えを良くしてください**」と指示し、気に入ったUIになるまで繰り返すだけです。  
既に良い感じのUIが他のページに作られていれば「**デザインは◯◯を参考にしてください**」と書けば合わせてくれます。  
ついでに水やりや肥料の記録と日記は別々に記録するようにしました。

![アプリのスクリーンショット（ダイアログ周りを豪華に）](https://res.cloudinary.com/zenn/image/fetch/s--XHXeVLwm--/https://storage.googleapis.com/zenn-user-upload/deployed-images/5a72385475d3e301874a2f24.webp%3Fsha%3D6fa831e1480ea50d750560a8ba77bd703cba6898)

他にもUIや機能面での改善をいくつか行いましたが、初回リリースで完璧にする必要もないので、少ない時間で効果のありそうなところや、将来的に改修しやすくするための設計変更を中心にしました。

収益化のための実装
---------

バナー広告は過去の実装を流用しました。

課金プランのUIは、  
「**プレミアムを購入するためのボトムモーダルシートを実装してください**」と指示したところ、良い感じのUIを作ってくれました。

![アプリのスクリーンショット（Widsurfに一発出ししてもらった課金プランUI）](https://res.cloudinary.com/zenn/image/fetch/s--HGUKlsyi--/https://storage.googleapis.com/zenn-user-upload/deployed-images/47fac96f07bad99478738a00.webp%3Fsha%3Dd54ef5c0e75e4dec84bee144eaaa479763c6f09d)

何度か作ってもらったのを組み合わせつつ調整します。

![アプリのスクリーンショット（完成版の課金プランUI）](https://res.cloudinary.com/zenn/image/fetch/s--NUyT9Bq_--/https://storage.googleapis.com/zenn-user-upload/deployed-images/a0222e0400530792aaff91bf.webp%3Fsha%3D48ee1240a740b89031b668e6c42751452fae588a)

次に、購入後に少しでも買って良かったと思ってもらうために、[confetti](https://pub.dev/packages/confetti)という紙吹雪を降らせるパッケージを追加し、  
「**confettiパッケージを使って、プレミアムを購入後に紙吹雪の舞うリッチな「ご購入ありがとうございます」というダイアログを出すようにしてください**」  
と指示を出して作ってもらいます。

![アプリのスクリーンショット（Widsurfに一発出ししてもらった購入ありがとうダイアログ）](https://res.cloudinary.com/zenn/image/fetch/s--tzewjBG8--/https://storage.googleapis.com/zenn-user-upload/deployed-images/62e8f288a23aaa3f6920afcb.webp%3Fsha%3Dece9ca37fe8cba54c5395701e2179a1424ffd613)

最後に課金処理ですが、流石にAIにしてもらうのは怖いので手動で作りました…。

アプリの多言語対応（ローカライズ）
-----------------

とりあえず人口の多そうな言語を調べつつ、最初は日本語、英語、韓国語、簡体字、繁体字、ドイツ語、フランス語、イタリア語、スペイン語、トルコ語の10言語に対応することにします。

**ローカライズ用パッケージの追加**  
↓  
**AIにコード内の日本語をローカライズファイル(.arb)に移してもらう**  
↓  
**各言語のローカライズファイルを作ってもらう**

の順番で行いました。  
コード内の日本語をローカライズファイルに移してもらうのは、一発では中々してもらえないので何度か実行する必要があります。念のため実行後に正規表現を用いて `[ぁ-んァ-ヶｱ-ﾝﾞﾟ一-龠ー]+` で検索した方が良いかもしれません。

注意点はアプリのUIが完成する前にローカライズすると、追加でテキストのローカライズが必要になった時に言語の数だけクレジットを消費してしまうことです。各言語一行追加するためだけに9クレジットの消費は重い…。  
今回も課金状態の復元（リストア）後のメッセージを忘れていたので、そこだけ英語になっています。

AIに作ってもらうときは**ローカライズは最後の最後**にしましょう。

ストアへの申請に必要な作業
-------------

一番面倒くさい！！

### アプリ名とアイコンとストアスクリーンショット

アプリ名はChatGPTに考えてもらいました。  
自分の発想力だと「**植物日記**」しか思いつかなかったのでありがたや…。

アイコンとストアのスクリーンショットは自分で作りました。

![App Store の草木帖のスクリーンショット）](https://res.cloudinary.com/zenn/image/fetch/s--fUnh7nIh--/https://storage.googleapis.com/zenn-user-upload/deployed-images/43aa54ce003d919cde91640a.webp%3Fsha%3Dde95ff28ef031d71c706f33132a63c3a5dea5fa8)

### 利用規約とプライバシーポリシー

この辺りは昔作ったものがあるのですが、今回特に追加で必要な項目も無いので使い回します。

### ストアの設定

販売する国と地域ごとに、アプリ名とサブタイトルと説明文を…。  
課金プランを承認してもらうためにスクショ撮ったり…。正直一番 ~~面倒~~ 大変な作業ですね。  
翻訳はChatGPTに訊けば、不自然な訳になっていないかも含めて教えてくれます。

App Store は無理ですが Google Play は `Google Play Developer API` があるので、そろそろMCPが登場しても良いのでは（既にあるのだろうか）  
App Store もブラウザー操作でやってくれるMCP登場しないかな…。

ということで無事申請 & 公開できました。  
↓完成したアプリのスクショです。

![アプリのスクリーンショット（最終的な完成系）](https://res.cloudinary.com/zenn/image/fetch/s--VjDlxNnl--/https://storage.googleapis.com/zenn-user-upload/deployed-images/288f63f4d9d9f8eda8ef8521.webp%3Fsha%3D157ade8340dad75d4f0c2aee9c51991003854d7a)

掛かった費用
======

#### Windsurfでプロンプト作り

フローアクションクレジットが40の消費でした。  
Windsurfは何かAIが操作するたびにフローアクションクレジットというものを消費します。  
15ドルのProプランで1500クレジットもらえるので、1クレジット辺り$0.01ですね。1ドル150円換算で**60円**です。

#### Clineでのアプリ作成

Clineで5回+失敗1回実行しました。

1. $1.6340
2. $1.7877
3. $2.6385 (失敗。無限ループに入ったので中止しました)
4. $0.8095
5. $1.8072
6. $2.6205

合計$11.2974 (1ドル150円換算で**約1695円**) でした。

#### Windsurfを使いつつの追加作業

このアプリと関係ない作業にも消費してしまったのでおよそですが、全部合わせたフローアクションクレジットの消費が大体500でした。なので**約750円ほど**です。

以上を合わせて合計**約2500円**ですね。

まとめ
===

これくらい簡単なアプリなら片手間にAIにほとんど作らせて、残りの作業もAIを使いつつ数日で終わらせられる時代になりました。体感ですが9割くらいAIにやってもらいました。  
普段アプリの新規リリースは数ヶ月おきくらいなのでほとんど自動化をしてこなかったのですが、今後はMCPも試しつつ効率化して沢山リリースしていきたいですね。

全く想定していなかったのですが、Clineの費用を抑える手法の多い記事になりました😭  
うっかりしてると1万円とかすぐに行きますからね…！

ちなみに省略していますが、テストの追加や[Melos](https://melos.invertase.dev)を使ったパッケージ分割なども行っています。

今回はFlutterでしたが、KMP (SwiftUI or UIKit, Jetpack Compose) や React Native でも良さそうですし、色々なやり方で作っていきたいなと思いました。

備考
==

本記事は以下の環境で検証しました

```
Flutter 3.29.2 • channel stable • https://github.com/flutter/flutter.git
Framework • revision c236373904 (13 days ago) • 2025-03-13 16:17:06 -0400
Engine • revision 18b71d647a
Tools • Dart 3.7.2 • DevTools 2.42.3
```

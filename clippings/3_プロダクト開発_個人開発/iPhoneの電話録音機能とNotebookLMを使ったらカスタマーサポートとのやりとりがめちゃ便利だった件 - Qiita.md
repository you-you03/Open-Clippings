---
title: "iPhoneの電話録音機能とNotebookLMを使ったらカスタマーサポートとのやりとりがめちゃ便利だった件 - Qiita"
source: "https://qiita.com/Null-Sensei/items/fa1be65f2070a8177627"
author:
  - "[[Qiita]]"
published: 
created: 2025-09-03
description: "iPhoneの電話録音機能とNotebookLMを使ったらカスタマーサポートとのやりとりがめちゃ便利だった件 はじめに 「あ、ナルほど！」でお馴染み、ナル先生です。皆さんは、カスタマーサポートに電話をした後、「あれ？担当者の名前なんだっけ？」「いつまでに何をすればいいだ..."
tags: ["clippings", "個人開発", "プロダクト", "ai"]
image: "assets/https%3A%2F%2Fqiita-user-contents.imgix.net%2Fhttps%253A%252F%252Fcdn.qiita.com%252Fassets%252Fpublic%252Farticle-ogp-background-afbab5eb44e0b055cce1258705637a91.png%3Fixlib%3Drb-4.jpg"
---
iPhoneの電話録音機能とNotebookLMを使ったらカスタマーサポートとのやりとりがめちゃ便利だった件
======================================================

はじめに
----

「あ、ナルほど！」でお馴染み、ナル先生です。皆さんは、カスタマーサポートに電話をした後、「あれ？担当者の名前なんだっけ？」「いつまでに何をすればいいだっけ？」と思うことはありませんか？特に長い通話や、複雑な問題解決の場合は、重要な情報を忘れてしまうことがよくあります。

今回は、iPhoneの電話録音機能と、GoogleのAIツール「[NotebookLM](https://notebooklm.google.com/)」を組み合わせて使うことで、カスタマーサポートとのやりとりを効率的に記録・分析する方法をご紹介します。実際のAppleサポートへの問い合わせを例に、その便利さをお伝えします。

背景：Mac Studioの注文トラブル
--------------------

先日、オンラインのApple StoreでMac Studio（164万3800円）を注文しました。支払い方法として、アカウント残高とクレジットカードの併用を選択したのですが、注文後「ご注文は保留になっています」という状態になり、支払い方法を更新するために電話するよう指示がありました。

このような状況で、Appleサポートに電話することになりました。

使用したツール
-------

1. **iPhoneの通話録音機能**  
   iOS 17.4から利用可能になった通話録音機能を使用しました。

[![image.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F30621%2F66aeda2d-3855-4e37-bd86-3ceee5b99361.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=f6475e66889bdbf7c9a5baa8d30ecc8f)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F30621%2F66aeda2d-3855-4e37-bd86-3ceee5b99361.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=f6475e66889bdbf7c9a5baa8d30ecc8f)

1. **Google NotebookLM**  
   Googleが提供する、音声や文書を分析できるAIツール。

手順
--

### 1. iPhoneで通話を録音する

iPhoneの通話録音機能は非常に簡単に使えます：

1. 通話中に画面上部の「・・・」をタップ
2. 「録音」を選択
3. 録音開始の通知が相手にも流れます（日本の法律に準拠）
4. 通話終了後、録音ファイルが自動的に保存されます

[![image.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F30621%2F6385db28-0908-4ca5-9401-241a5ae902d6.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=e25f99161f4847b96237c577dde4c507)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F30621%2F6385db28-0908-4ca5-9401-241a5ae902d6.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=e25f99161f4847b96237c577dde4c507)

### 2. 録音ファイルをNotebookLMにアップロード

1. NotebookLMにアクセス
2. 新しいノートブックを作成
3. 「ソースを追加」から録音ファイルをアップロード
4. アップロード後、NotebookLMが自動的に音声を文字起こしして分析

[![image.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F30621%2F9bfe1ca6-b31d-48c7-96fb-f5ca60db9efa.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=9279d4bca7514d8fd24d9e5380f93c46)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F30621%2F9bfe1ca6-b31d-48c7-96fb-f5ca60db9efa.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=9279d4bca7514d8fd24d9e5380f93c46)

### 3. NotebookLMでの分析

NotebookLMでは、以下のような質問をして分析結果を得ることができます：

* 「この会話の要点をまとめて」
* 「登場人物は誰？」
* 「解決された問題は何？」
* 「次にやるべきことは？」

実際の分析結果
-------

NotebookLMが自動的に分析してくれた結果は以下の通りです：

### 会話の概要

```
タイムライン
不明 (通話開始前): 近藤義がオンラインのApple StoreでMac Studio (164万3800円) を注文。支払方法はアカウント残高とクレジットカードの併用を選択。注文後、「ご注文は保留なっています」という状況になり、支払い方法を更新するために電話をするよう指示があった。

通話開始: 近藤義がAppleのサポートに電話をかける。自動音声応答システムを経て、担当の本田につながる。

通話中:近藤義がMac Studioのオンライン注文が保留になっていること、支払い方法更新の指示があったことを説明。

本田が近藤の注文状況を確認するため、Wから始まる注文番号 と氏名を確認。
本人確認のため、登録のメールアドレス を確認。

本田がApple IDの確認画面がデバイスに表示されているかを確認。近藤が確認した旨を伝える。

本田が注文内容を確認。2024年3月12日に164万3800円のMac Studioが注文され、アカウント残高とクレジットカードの併用で支払いが滞っていることを確認。アカウント残高での支払い予定額2万3000円に対し、5180円の不足が生じていることが判明。

近藤が不足の理由を尋ねる。本田は他の注文やサブスクリプションの影響の可能性を示唆。不足額の支払い方法について、本田が登録のクレジットカードへの追加請求を提案。近藤がそれを希望する。

本田が追加請求の手続きに入る。

近藤がクレジットカードへの請求通知を受け取ったことを伝える。

本田も追加請求の完了を確認。

支払いの問題が解決したことが確認される。

本田が今後、出荷準備に入ることを説明。伝票と共に通知がある旨を伝える。

近藤が商品の到着予定日 (3月27日から30日) の幅がある理由を質問。

本田が商品が海外 (香港など) から直接出荷されるため、配送に時間がかかる可能性を説明。

通話終了: 近藤が謝意を述べ、通話終了。

登場人物

近藤 (こんどう):オンラインのApple StoreでMac Studioを注文した顧客。注文が保留状態になり、サポートに電話をかけた。
本田 (ほんだ):Apple Storeの担当者。電話で近藤の問い合わせに対応した。丁寧な言葉遣いで、注文状況の確認、本人確認、支払いに関する手続きを行った。

この通話録音からは、上記2名のみが明確な登場人物として特定できます。自動音声応答システムの存在は示唆されていますが、具体的な人物像は不明です。

NotebookLM は不正確な場合があります。回答は再確認してください。
```

メリット
----

1. **情報の正確な記録**  
   担当者の名前、注文番号、日付などの重要情報が正確に記録されます。
2. **会話の要点抽出**  
   長い通話でも、AIが重要なポイントだけを抽出してくれます。
3. **次のアクションの明確化**  
   「次に何をすべきか」が明確になります。
4. **トラブル解決の証拠として**  
   「〜と言われた」というトラブルの際に、証拠として使える可能性があります。

### NotebookLM 新機能 マインドマップも出せます

[![image.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F30621%2F0dcdba8e-9920-4ea7-adf6-d9b56c981287.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=c7000d20ef6871f6fdbcdcfac7fd76a0)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F30621%2F0dcdba8e-9920-4ea7-adf6-d9b56c981287.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=c7000d20ef6871f6fdbcdcfac7fd76a0)

注意点
---

1. **通話録音の法的制約**  
   日本では通話録音は相手に通知する必要があります（iPhoneの機能では自動通知されます）。
2. **プライバシーへの配慮**  
   個人情報を含む録音データの取り扱いには十分注意しましょう。

まとめ
---

iPhoneの通話録音機能とNotebookLMの組み合わせは、特にカスタマーサポートとの重要な会話を記録・分析する上で非常に便利です。私のケースでは、Mac Studioの注文に関する問題がスムーズに解決しただけでなく、その詳細な記録を簡単に保存・分析することができました。

ビジネスシーンや、重要な契約・問い合わせの際に、この方法を活用が良さそうです。

---

おまけ：NotebookLMの他の活用法
--------------------

1. **会議の議事録作成**  
   オンライン会議の録画から自動的に議事録を作成できます。
2. **インタビュー分析**  
   インタビュー音声から重要なインサイトを抽出できます。
3. **講義・セミナーのノート作成**  
   長い講義やセミナーから要点だけを抽出できます。

今は、顧客側としてNotebookLMを活用しましたが、逆にカスタマーサポート側にとっても福音になるかもしれませんね。

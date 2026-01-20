---
title: 令和トラベル Dify講座（社内イベント資料）
source: https://www.docswell.com/s/miyatti/KJ4GN1-2024-07-22-195223#p1
author:
- '[[Daisuke Miyata]]'
published: 2024-07-22
created: 2025-07-11
description: ドクセルはスライドやPDFをかんたんに共有できるサイトです
tags:
- clippings
- dify
- ai
- プロダクト
- ai-development
---
695.1K Views

July 22, 24

スライド概要

社内で実施したDify講座の資料です。  
Dify初級者から中級者向けに参考になる内容もあるかもなので、外部公開してみます。

[![profile-image](https://bcdn.docswell.com/icon/YVXP2DJK.jpg)](https://www.docswell.com/user/miyatti)

[

#### Daisuke Miyata

](https://www.docswell.com/user/miyatti)

[@miyatti](https://www.docswell.com/user/miyatti)

[スライド一覧](https://www.docswell.com/user/miyatti)

株式会社エクスプラザ 生成AIエバンジェリスト / リードAIプロデューサー

シェア

[またはPlayer版](https://www.docswell.com/s/miyatti/#)

埋め込む [»CMSなどでJSが使えない場合](https://www.docswell.com/service/iframe)

ダウンロード

## 関連スライド

##### 各ページのテキスト

[1.](https://www.docswell.com/s/miyatti/#p1)

ノーコードAIアプリ開発プラットフォーム Dify講座 基礎編 by 令和トラベル MLチーム リーダー @miyatti (Miyata Daisuke)

[2.](https://www.docswell.com/s/miyatti/#p2)

目次 1. AI開発概論 2. AI開発領域の分類 3. Difyについて 4. 操作方法 5. ワークフロー：基本 6. ワークフロー：応用 7. チャットボット：基本 8. チャットボット：応用 9. まとめ © 2024 Reiwa travel, Inc.

[3.](https://www.docswell.com/s/miyatti/#p3)

1\. AI開発概論 © 2024 Reiwa travel, Inc.

[4.](https://www.docswell.com/s/miyatti/#p4)

AI開発とは？ AIを使うとなにがいいのか？ AIを使うことで、より柔軟なことができるア プリケーションが作れる AI開発といっても、めちゃくちゃ幅広い 伝統的な 機械学習（ML）開発 と ChatGPT のようなLLMを使った開発 の違い 基盤（モデル）開発とアプリケーション開発 の違い コーディング開発とノーコード開発の違い © 2024 Reiwa travel, Inc.

[5.](https://www.docswell.com/s/miyatti/#p5)

伝統的なML開発とLLM開発の違い 伝統的なML開発： 学習データから独自のモデル開発を作る モデルの性能をどれだけよくするかが重要 LLM開発： 基本的にはモデルはありもを使う モデルを使って、どんなアプリケーションを 作るかが重要 © 2024 Reiwa travel, Inc.

[6.](https://www.docswell.com/s/miyatti/#p6)

LLM開発におけるモデル開発と、ツール 開発の違い 基盤（モデル）開発： 事前学習・事後学習 いろいろなやりかたでモ デル自体をよくする開発 基本的にお金がめちゃかかるので、やれる会 社は限られる 業界特化で一部分を事後学習でよくしたモデ ル開発をやる会社もある アプリケーション開発： 国内のAI開発という場合、コンサルなど含め てこちらが主領域 LLMを利用したアプリケーション構築 ユーザーインターフェース設計も重要です © 2024 Reiwa travel, Inc.

[7.](https://www.docswell.com/s/miyatti/#p7)

LLM開発におけるコーディングとノーコ ードの違い コーディング： プログラミングスキルが必要 ノーコードに比べて自由度が高く、性能をだ しやすい 利用者の意見をききながら、エンジニアが開 発をしていく ノーコード/ローコード： プログラミングスキルが基本的に不要 コーディング開発に比べると、自由度が制限 され、ツールの範囲内での開発になる ノンエンジニア/実際の利用者自身がアプリを 改善していける © 2024 Reiwa travel, Inc.

[8.](https://www.docswell.com/s/miyatti/#p8)

2\. AI開発領域の分類 © 2024 Reiwa travel, Inc.

[9.](https://www.docswell.com/s/miyatti/#p9)

勝ち筋の探索 かたっぱしからやる 1. コンテンツ大量生成支援 （Customer x Static） 2. 業務生産性向上 （社内 x Static） 3. ナレッジシェア （社内 x Dynamic） © 2024 Reiwa travel, Inc.

[10.](https://www.docswell.com/s/miyatti/#p10)

記事生成速度最大化 Customer x Static LLMを活用した 記事コンテンツ作成 人間による ファクトチェック 高い生産性と コンテンツ品質 © 2024 Reiwa travel, Inc.

[11.](https://www.docswell.com/s/miyatti/#p11)

旅行ガイドの例 DifyのWorkflow 情報収集 → 編集者AI → ラ イターAI 効率的なワークフロー 生産性の高い制作プロセス © 2024 Reiwa travel, Inc.

[12.](https://www.docswell.com/s/miyatti/#p12)

© 2024 Reiwa travel, Inc.

[13.](https://www.docswell.com/s/miyatti/#p13)

ナレッジシェア 社内 x Dynamic 社内データを活用した対話 型AI 運用開始段階 © 2024 Reiwa travel, Inc.

[14.](https://www.docswell.com/s/miyatti/#p14)

社内Botの例 DifyでRAG 自前でNotionやSlackからデ ータをとりだす 最適なRAGの設定をDifyで 模索 特定のサービスにロックイ ンされない © 2024 Reiwa travel, Inc.

[15.](https://www.docswell.com/s/miyatti/#p15)

社内DX 社内 x static 今まで人間の手でやってい たオペレーション Dynamicに都度LLMを使う のではなくワークフロー化 する（LLM使わなくてもい い） ノンエニジニアでも作れる ように © 2024 Reiwa travel, Inc.

[16.](https://www.docswell.com/s/miyatti/#p16)

３つの領域の伸び代 静的改善は地味に良い リスクが低い LLMというよりDX 伸び代が死ぬほどある © 2024 Reiwa travel, Inc.

[17.](https://www.docswell.com/s/miyatti/#p17)

Customer x Dynamic 絶対にやり切る Web2.0以来 追い求めた領域 理想としては NoUIの概念 思考しただけで 答えがでる © 2024 Reiwa travel, Inc.

[18.](https://www.docswell.com/s/miyatti/#p18)

3\. Difyについて © 2024 Reiwa travel, Inc.

[19.](https://www.docswell.com/s/miyatti/#p19)

Difyの概要 ノーコードAIアプリ開発プラットフォーム ブロックを線でつなげて簡単にアプリ作成 オープンソースソフトウェア（OSS）として提供されており、誰でも利用可能 コアチームが中国にあり、OSSでありながら迅速なUpdateが行われている © 2024 Reiwa travel, Inc.

[20.](https://www.docswell.com/s/miyatti/#p20)

Difyの主な特長（1/3） 1. LLMの選択と比較が容易 多様なLLMに対応し、APIキーを入れるだけで利用可能 画面上で簡単にLLMの切り替えが可能 新しいモデルに簡単にアップデート可能 2. 外部ツールとの豊富な連携 Google検索やWikipedia検索などとの連携 HTTPブロックを使用し、APIがあるサービスと簡単に連携可能 APIを通じた社内システムとの連携も可能 3. 多様な展開方法 独立したWebページとしての展開 © 2024 Reiwa travel, Inc.

[21.](https://www.docswell.com/s/miyatti/#p21)

Difyの主な特長（2/3） 4. 柔軟な活用方法 LLMを使用する部分のみをDifyで構築し、外部APIとして利用可能 既存システムとの連携が容易 5. LLMのシステムの不確実性への対応 リリース後の調整が容易 現場のフィードバックを高速に反映可能 ノンエンジニアでも直接素早く修正できる © 2024 Reiwa travel, Inc.

[22.](https://www.docswell.com/s/miyatti/#p22)

Difyの主な特長（3/3） 6. RAG（検索拡張生成）の簡単構築 自社データを活用したチャットボットを容易に構築 ファイルのドラッグ＆ドロップでデータ読み込み チャンク分割やVectorStore構築が自動化 チャンクの検索ヒット回数確認や編集が可能 ナレッジの品質改善が容易 © 2024 Reiwa travel, Inc.

[23.](https://www.docswell.com/s/miyatti/#p23)

4\. 操作方法 © 2024 Reiwa travel, Inc.

[24.](https://www.docswell.com/s/miyatti/#p24)

セットアップ 1. Difyホームページにアクセス 2. 「始める」ボタンをクリック 3. Googleアカウントでログイン 4. アカウント作成完了 © 2024 Reiwa travel, Inc.

[25.](https://www.docswell.com/s/miyatti/#p25)

操作方法 「Create from Blank」をクリック アプリタイプを選択 チャットボット テキストジェネレーター エージェント ワークフロー チャットボットは基本/フローモードあり フローモードでブロックを線でつなぐ タイトルと説明を入力して作成 © 2024 Reiwa travel, Inc.

[26.](https://www.docswell.com/s/miyatti/#p26)

5\. ワークフロー：基本 © 2024 Reiwa travel, Inc.

[27.](https://www.docswell.com/s/miyatti/#p27)

基本的なブロック 1/12 開始ブロック ワークフロー開始点、入力 定義 © 2024 Reiwa travel, Inc.

[28.](https://www.docswell.com/s/miyatti/#p28)

基本的なブロック 2/12 回答/終了ブロック フロー終了、結果出力 © 2024 Reiwa travel, Inc.

[29.](https://www.docswell.com/s/miyatti/#p29)

基本的なブロック 3/12 LLMブロック 大規模言語モデル使用 文章生成、感情分析、要約 など © 2024 Reiwa travel, Inc.

[30.](https://www.docswell.com/s/miyatti/#p30)

基本的なブロック 4/12 パラメータ抽出ブロック 文章から情報抽出 © 2024 Reiwa travel, Inc.

[31.](https://www.docswell.com/s/miyatti/#p31)

基本的なブロック 5/12 質問分類機 質問を分類するためのブロ ック 入力された質問を事前に定 義したカテゴリに分類 フローの分岐や適切な回答 の選択に利用 © 2024 Reiwa travel, Inc.

[32.](https://www.docswell.com/s/miyatti/#p32)

基本的なブロック 6/12 変数集約ブロック 複数変数を1つに © 2024 Reiwa travel, Inc.

[33.](https://www.docswell.com/s/miyatti/#p33)

基本的なブロック 7/12 テンプレートブロック 変数値を文字列に埋込 © 2024 Reiwa travel, Inc.

[34.](https://www.docswell.com/s/miyatti/#p34)

デモ：感想チェッカー （前半） 1. 情報取得と返事作成 レビューを名前つきで入 力 名前と日付をパラメータ 抽出で取得 返事を作成 DSLファイルのダウンロード © 2024 Reiwa travel, Inc.

- [https://drive.google.com/file/d/11b4t\_DjvW\_S4NX89yECS4QZt6L8H5lkb/view?usp=sharing](https://www.google.com/url?q=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F11b4t_DjvW_S4NX89yECS4QZt6L8H5lkb%2Fview%3Fusp%3Dsharing)

[35.](https://www.docswell.com/s/miyatti/#p35)

基本的なブロック 8/12 IFブロック 条件分岐 © 2024 Reiwa travel, Inc.

[36.](https://www.docswell.com/s/miyatti/#p36)

デモ：感想チェッカー（後半） 2. 内容判断と改善案検討 ポジティブ/ネガティブで分類 ネガティブな場合： 課題抽出 改善案検討（LLM使用） 返事作成 ポジティブな場合： 良かったポイント抽出 返事作成 © 2024 Reiwa travel, Inc.

[37.](https://www.docswell.com/s/miyatti/#p37)

デモ：感想チェッカー（後半） まとめ 3. 結果の集約とレポートの分割出力 変数集約ブロックで結果を一旦まと める IFブロックで最終レポートは２種類 わけて出力する DSLファイルのダウンロード © 2024 Reiwa travel, Inc.

- [https://drive.google.com/file/d/11a7-5A6d1Wa0lS9Pjy-yPRXAJivOsOLA/view?usp=sharing](https://www.google.com/url?q=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F11a7-5A6d1Wa0lS9Pjy-yPRXAJivOsOLA%2Fview%3Fusp%3Dsharing)

[38.](https://www.docswell.com/s/miyatti/#p38)

6\. ワークフロー:応用 © 2024 Reiwa travel, Inc.

[39.](https://www.docswell.com/s/miyatti/#p39)

外部サービス連携 カスタムツールブロック：Tavily Search AI活用の高度な検索エンジン。自然言 語対応、最新情報取得、信頼性の高い 情報を優先。 ウェブ上の情報を効率的に収集し、関 連性の高い結果を提供。 Difyのカスタムツールブロックとして 利用可能。 © 2024 Reiwa travel, Inc.

[40.](https://www.docswell.com/s/miyatti/#p40)

外部サービス連携 カスタムツールブロック：Jina Reader ドキュメント解析と情報抽出のAIツー ル 多様な形式のドキュメントを解析し、 構造化データを抽出 高度な自然言語処理で重要情報を特定 Tavily Searchと組み合わせて効率的な 情報検索と分析が可能 © 2024 Reiwa travel, Inc.

[41.](https://www.docswell.com/s/miyatti/#p41)

デモ：旅行記事生成ツール（前 半） 1. キーワードからネット検索と旅行ガイ ドページ作成 スタートにキーワード入力欄作成 クエリ作成プロンプト作成 Tavily SearchでURL出力 Jina readerブロックでURL内容取 得 LLMに渡してボディ作成 HTMLテンプレートで整形 DSLファイルのダウンロード © 2024 Reiwa travel, Inc.

- [https://drive.google.com/file/d/11rMVkFqrziu9XNZM8t7Iz5pByPJzqrr3/view?usp=sharing](https://www.google.com/url?q=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F11rMVkFqrziu9XNZM8t7Iz5pByPJzqrr3%2Fview%3Fusp%3Dsharing)

[42.](https://www.docswell.com/s/miyatti/#p42)

基本的なブロッ ク 9/12 イテレーションブ ロック 配列やリストの要 素に対して繰り返 し処理を実行 各要素に対して同 じ操作を適用する 際に使用 結果は新しい配列 として出力される © 2024 Reiwa travel, Inc.

[43.](https://www.docswell.com/s/miyatti/#p43)

基本的なブロッ ク 10/11 コードブロック JavaScriptや pythonで任意の処 理実行 文字列処理など © 2024 Reiwa travel, Inc.

[44.](https://www.docswell.com/s/miyatti/#p44)

コードブロックの使い道1 Iteration後の処理 LLMノード（言語モデルノード）は配 列を直接処理することができません。 Iterationノード（繰り返し処理ノード） は配列のみを出力します。 そのため、Iterationノードの結果を LLMノードで処理するためには、配列 を文字列に変換する中間的なコードノ ードを準備する必要があります。 この中間ノードでは、配列の要素を適 切な形式で連結し、一つの文字列とし て出力します。 © 2024 Reiwa travel, Inc.

[45.](https://www.docswell.com/s/miyatti/#p45)

コードブロックの使い道2 大量の文字列処理 以下のような制限があります(cloud版)： 1. コードBlockの制限：80,000文字まで 2. Pythonコードの制限：大量の文字列を 扱う際に内部エラーが発生する可能性 対策： 手前のcodeブロックで文字数を減らす JavaScriptコードBlockを使用する （Pythonよりもエラーが起きない） OSS（local)版を運用する © 2024 Reiwa travel, Inc.

[46.](https://www.docswell.com/s/miyatti/#p46)

LLMブロックのか きかた Chain of Thought (CoT) プロンプティ ング Chain of Thought （思考の連鎖） は、AIに複雑なタ スクを段階的に考 えさせるプロンプ トエンジニアリン グ技法です。 © 2024 Reiwa travel, Inc.

[47.](https://www.docswell.com/s/miyatti/#p47)

主な特徴と利点： CoTアプローチを使用することで、単に最終結果を求めるよりも、より深い理解と高品質な 出力を得ることができます。 1. 段階的アプローチ： その後、構成に基づいて詳細な内容を作成させる 2. クオリティの向上： 段階を踏むことでAIの思考がより整理され、質の高い出力が得られる LLMにとってもこの方法の方が高品質な結果を生成しやすい 3. 可読性の向上： ステップごとに分けることで、人間にとっても理解しやすい形式になる 4. 修正の容易さ： 各段階で確認と修正が可能なため、最終的な成果物の品質管理がしやすい © 2024 Reiwa travel, Inc.

[48.](https://www.docswell.com/s/miyatti/#p48)

DifyでのCoT的応用 Difyのワークフローは自然と CoT的なやりかたをとりや すい いきなり難しいことをLLM で頼むのではなく、ステッ プを分けるとよい 例えば記事生成でも、いき なり記事をかかせるまえ に、記事の構成を一度作ら せた方がクオリティがあが る © 2024 Reiwa travel, Inc.

[49.](https://www.docswell.com/s/miyatti/#p49)

デモ：旅行記事生成ツール（後 半） 1. 記事のクオリティをあげる クローリング処理をループにして、 より情報量を多くとってこれるよう にする クローリングしたデータを、 LLMに渡せるようにコードBlock で前処理をする LLMを分割し、CoTでクオリティを あげる DSLファイルのダウンロード © 2024 Reiwa travel, Inc.

- [https://drive.google.com/file/d/11fFIlx1nYdSDn6LvrgTHLGYnO5fzBcQd/view?usp=sharing](https://www.google.com/url?q=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F11fFIlx1nYdSDn6LvrgTHLGYnO5fzBcQd%2Fview%3Fusp%3Dsharing)

[50.](https://www.docswell.com/s/miyatti/#p50)

参考: 旅行記事 生成ツール（運 用中） © 2024 Reiwa travel, Inc.

[51.](https://www.docswell.com/s/miyatti/#p51)

7\. チャットボット:基本 © 2024 Reiwa travel, Inc.

[52.](https://www.docswell.com/s/miyatti/#p52)

チャットbotの基本 1. チャットボットの作成: 「最初から作成」をクリック 「チャットボット」を選択 「チャットフローモード」を選択（より柔軟な設定が可能） 2. チャットフローモードの特徴: ワークフローモードと異なり、ユーザーとの対話を前提としたフロー設計 「回答ブロック」が自動的に追加され、LLMの出力がユーザーに返される 3. デバッグとプレビュー: 右上の「デバッグ」ボタンでチャットインターフェースが表示される ワークフローモードの「プレビュー」とは異なり、実際のチャット形式でテスト可能 デバッグ中にリアルタイムでフローの動作を確認できる © 2024 Reiwa travel, Inc.

[53.](https://www.docswell.com/s/miyatti/#p53)

デモ： My Chat AI モデルを選べる 普通にAIとチャットできる DSLファイルのダウンロード © 2024 Reiwa travel, Inc.

- [https://drive.google.com/file/d/11doq0seU12z6VQIfdmVpQl5SnUc2FIdu/view?usp=sharing](https://www.google.com/url?q=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F11doq0seU12z6VQIfdmVpQl5SnUc2FIdu%2Fview%3Fusp%3Dsharing)

[54.](https://www.docswell.com/s/miyatti/#p54)

8\. チャットボット:応用 © 2024 Reiwa travel, Inc.

[55.](https://www.docswell.com/s/miyatti/#p55)

RAG = Retrieval Augmented Generation （検索拡張生成） AIの回答能力を外部情報で強化 する技術 仕組み： 1. ユーザーの質問に関連す る情報を外部データから 検索 2. 検索結果をAIに提供 3. AIが提供された情報を基 に回答を生成 © 2024 Reiwa travel, Inc.

[56.](https://www.docswell.com/s/miyatti/#p56)

RAG = Retrieval Augmented Generation （検索拡張生成） AIの回答能力を外部情報で強化 する技術 メリット： 最新情報や専門知識を含 んだ回答が可能に AIの幻覚（誤った情報の 生成）を減らせる カスタマイズされた知識 ベースで特定分野に強い AIを作れる © 2024 Reiwa travel, Inc.

[57.](https://www.docswell.com/s/miyatti/#p57)

DifyでのRAG DifyでRAGを実装するメリット 1. 簡単な設定: ノーコードでRAGシステムを構築可能 複雑なプログラミングなしで高度な機能を実現 2. リアルタイムの更新: 知識ベースを定期的に更新し、最新情報を反映 常に最新の情報に基づいた回答が可能 3. 統合されたワークフロー: 知識取得から回答生成までのプロセスを一元管理 効率的なAIアプリケーション開発が可能 © 2024 Reiwa travel, Inc.

[58.](https://www.docswell.com/s/miyatti/#p58)

DifyでのRAGのやりか た 全体の流れ Step1 ナレッジをつくる Step2 ワークフロー(Chatbot) を作る © 2024 Reiwa travel, Inc.

[59.](https://www.docswell.com/s/miyatti/#p59)

Knowledgeベースの作成 UIから作る方法 手軽にできる 更新があるときは自分でやる必要がある APIから作る方法 色々制約がない リアルタイムに更新を自動化などできる © 2024 Reiwa travel, Inc.

[60.](https://www.docswell.com/s/miyatti/#p60)

Knowledgeベースの作成 (UIか ら) - Part 1 1. ナレッジの作成をクリック 2. 情報ソースを選択: ウェブサイト PDFファイル テキストドキュメント 3. 選択したソースに応じて設定: ウェブサイト: URLを入力 ファイル: アップロード © 2024 Reiwa travel, Inc.

[61.](https://www.docswell.com/s/miyatti/#p61)

Knowledgeベースの作成 (UIか ら) - Part 2 5. 知識ベースの詳細設定1: チャンクサイズの調整: 文書を適切な大きさに分割 デフォルトは500トークン チャンク重複の設定: 文脈の連続性を保つため デフォルトは50トークン © 2024 Reiwa travel, Inc.

[62.](https://www.docswell.com/s/miyatti/#p62)

Knowledgeベースの作成 (UIか ら) - Part 3 5. 知識ベースの詳細設定2: インデックス方式の選択: ベクトル検索やキーワード検索 など Rerankの有効化: 検索結果の精度向上 関連性の高い情報を優先的に提 供 埋め込みモデルの選択: テキストをベクトル化するモデ ルを指定 © 2024 Reiwa travel, Inc.

[63.](https://www.docswell.com/s/miyatti/#p63)

Knowledgeベースの作成 (UIから) - Part 4 6. 取得開始をクリック 7. 取得した情報を確認し、必要に応じて編集 8. 保存して処理をクリック © 2024 Reiwa travel, Inc.

[64.](https://www.docswell.com/s/miyatti/#p64)

基本的なブロッ ク 11/12 知識取得ブロック 外部データソース から情報取得 © 2024 Reiwa travel, Inc.

[65.](https://www.docswell.com/s/miyatti/#p65)

デモ：slack times Bot 実装手順 1. ナレッジ作成 slack APIから 特定のチャンネルの 情報を集める 2. Chat flow作成 1. 知識取得ブロック追加 2. LLMブロック設定 DSLファイルのダウンロード © 2024 Reiwa travel, Inc.

- [https://drive.google.com/file/d/11oyV1rxaaEa3ShlZ26pftLnEhK9c-2xp/view?usp=drive\_link](https://www.google.com/url?q=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F11oyV1rxaaEa3ShlZ26pftLnEhK9c-2xp%2Fview%3Fusp%3Ddrive_link)

[66.](https://www.docswell.com/s/miyatti/#p66)

基本的なブロッ ク 12/12 HTTPリクエストブ ロック 外部Web/API連携 © 2024 Reiwa travel, Inc.

[67.](https://www.docswell.com/s/miyatti/#p67)

Knowledgeベースの作成 (API から) 1. HTTPリクエストブロックを追加: 外部APIとの通信に使用 2. DifyのAPIを設定: Knowledge APIエンドポイントを 指定 認証情報を設定 3. リクエストを構成: HTTPメソッドを選択 必要なヘッダーとパラメータを設定 © 2024 Reiwa travel, Inc.

[68.](https://www.docswell.com/s/miyatti/#p68)

共有：API経由 knowledge作成フロー © 2024 Reiwa travel, Inc.

[69.](https://www.docswell.com/s/miyatti/#p69)

共有：Learn 博士: 社内問い合わせBOT （運用中） © 2024 Reiwa travel, Inc.

[70.](https://www.docswell.com/s/miyatti/#p70)

Slackチャットボット作成手順 1. Difyでチャットボット開発 2. Slack API設定とボットユーザー作成 3. Makeでワークフロー作成：SlackとDify API連携 4. 統合：Slack→Make→Dify→Slack DifyのAI機能を活用したSlackチャットボットを効率的に構築可能。 © 2024 Reiwa travel, Inc.

[71.](https://www.docswell.com/s/miyatti/#p71)

参考 kei先生のブログ記事 がめちゃくちゃわか りやすいのでおすす めです https://zenn.dev/reiw atravel/articles/2a74 8695005001 © 2024 Reiwa travel, Inc.

- [https://zenn.dev/reiwatravel/articles/2a748695005001](https://www.google.com/url?q=https%3A%2F%2Fzenn.dev%2Freiwatravel%2Farticles%2F2a748695005001)

[72.](https://www.docswell.com/s/miyatti/#p72)

9\. まとめ © 2024 Reiwa travel, Inc.

[73.](https://www.docswell.com/s/miyatti/#p73)

Difyの学習をどのように継続していくべきでしょうか？ Difyは急速に進化するサービスです。最新の情報を常にキャッチアップするために、以下の 方法がおすすめです： 1. SNSでの情報収集 Dify関連のXアカウントをフォロー 日本語公式アカウント: https://x.com/dify\_ai 公式アンバサダー sangminさん: https://x.com/gijigae 最新のアップデートや使用例をチェック 2. コミュニティへの積極的な参加 Difyの公式Discordに参加し、最新情報を入手 グローバルコミュニティ: https://discord.com/invite/FngNHpbcY7 日本語コミュニティ: https://discord.gg/RNhs8tWpeV 疑問点があれば、遠慮なく質問しましょう © 2024 Reiwa travel, Inc.

- [https://x.com/dify\_ai](https://www.google.com/url?q=https%3A%2F%2Fx.com%2Fdify_ai)
- [https://x.com/gijigae](https://www.google.com/url?q=https%3A%2F%2Fx.com%2Fgijigae)
- [https://discord.com/invite/FngNHpbcY7](https://www.google.com/url?q=https%3A%2F%2Fdiscord.com%2Finvite%2FFngNHpbcY7)
- [https://discord.gg/RNhs8tWpeV](https://www.google.com/url?q=https%3A%2F%2Fdiscord.gg%2FRNhs8tWpeV)

[74.](https://www.docswell.com/s/miyatti/#p74)

いかがでしたか？ Difyで簡単にAIアプリケーションを構築可能 デモは約15分で作成 既存ツールとの連携も可能 Google、Notionなど APIを活用した調べ物にも便利 Claude、OpenAIの有料プランAPIを使用 業務効率化に大きな可能性 ぜひDIfyを活用してみてください！ © 2024 Reiwa travel, Inc.
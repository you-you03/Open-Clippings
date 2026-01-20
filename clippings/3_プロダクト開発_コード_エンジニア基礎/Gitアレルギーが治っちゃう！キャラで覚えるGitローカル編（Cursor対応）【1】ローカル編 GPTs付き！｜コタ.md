---
title: Gitアレルギーが治っちゃう！キャラで覚えるGitローカル編（Cursor対応）【1】ローカル編 GPTs付き！｜コタ
source: https://note.com/nyattoh/n/nd731d2e88804?sub_rt=share_pb
author:
- '[[コタ]]'
published: 2025-06-14
created: 2025-06-16
description: 更新履歴： 2025/06/15：GPTsに新キャラを追加  Claude Code と Claude Code Action出てきて、Gitアレルギーなんとかしたくなった  並列実装とか色々見て、やってみたい！･･･と思ったものの。
  説明に出てくる用語わからない。 Cursorに頼んでもなんかぐちゃぐちゃになる。 そのうえWindowsだとハードルがやや高い･･･   つまり、Gitを知らないボクが「どうしたら自分が分かるか」をベースに書いているところがミソです。   Cursor
  とかClaude Code にきちんと指示ができて事足りてる人には向いてません。すぐ、ちゃんとやってく
tags:
- clippings
- エンジニア
- コード
- プロダクト
- ai
---
![見出し画像](https://assets.st-note.com/production/uploads/images/195951521/rectangle_large_type_2_18cdfe22b02ad52518e599c609fb98d8.jpeg?width=1200)

## Gitアレルギーが治っちゃう！キャラで覚えるGitローカル編（Cursor対応）【1】ローカル編 GPTs付き！

割引あり

[コタ](https://note.com/nyattoh)

更新履歴：  
2025/06/15：GPTsに新キャラを追加

## Claude Code と Claude Code Action出てきて、Gitアレルギーなんとかしたくなった

並列実装とか色々見て、やってみたい！･･･と思ったものの。  
説明に出てくる用語わからない。  
Cursorに頼んでもなんかぐちゃぐちゃになる。  
そのうえWindowsだとハードルがやや高い･･･

> **つまり、Gitを知らないボクが「どうしたら自分が分かるか」をベースに書いているところがミソです。**

Cursor とかClaude Code にきちんと指示ができて事足りてる人には向いてません。すぐ、ちゃんとやってくれるAIも登場するでしょ～。

## 💡 やり方だけ教えて！って人はコードの所（背景黒）だけ見てください！

## 💡間違えちゃった時の対応は目次から飛んでくださーい。

  

---

---

## コマンド恐怖症でもなんとかなる？

**なります。**  

### 最初はこのキャラクターだけでやってみよー。

![画像](https://assets.st-note.com/img/1749822053-yfU0rv9ulbSO5wmGKen8zsti.jpg?width=1200)

![画像](https://assets.st-note.com/img/1749824879-7OFMtyAI2wBGphjeuSlY8vTQ.png?width=1200)

---

## GitHubが主役だと思っていたアナタへ

実は、 **Gitの主役は「GitHub」じゃなくて「ローカルのGit」** なんです。

**GitHubはただの"クラウド上の置き場"。**  
Gitこそが、あなたのパソコンの中で **記録をつけて、変更を管理して、作業を進めるエンジン** 。

GitHubはその補助役であり、見せるため・共有するための拡張機能にすぎません。

![画像](https://assets.st-note.com/img/1749828014-0swtSnvEo37if6e9Orl1RQmk.jpg?width=1200)

---

## この記事でやること（必要なのはCursorエディタ無料版だけ）

- GitHubのアカウント不要！
- Cursorの無料プランでOK！
- init先生、ワークツリーくん、カゴくん、ネコくんだけで完結
- Cursor（Claude Code）で書いたプロンプトを保存して履歴管理してみる
- 過去バージョンに戻す「巻き戻し魔法」もやってみる

---

## 🪄 実践テーマ：プロンプトファイルのバージョン管理

### ✏️ 想定する作業

- chat\_prompt.yaml ファイルに、プロンプトの試行錯誤を書く
- 何度も内容を変更していき、その履歴をGitで記録する

---

## 🛠 ステップバイステップ

### ① ディレクトリを作って開いてみよう

**PowerShellやCommand Promptなら･･･**

```
mkdir prompt-dev cd prompt-dev
```

### Cursorなら･･･

![画像](https://assets.st-note.com/img/1749825223-GTw2N4MFfzL9cvCIBxnRdmOE.png?width=1200)

普通にディレクトリ（フォルダ）を作って、右クリックから開くか

![画像](https://assets.st-note.com/img/1749825266-X0eGVzyu7DaSWHfI1v3YMwbJ.png?width=1200)

Cursorのファイル→フォルダーを開く・ターミナル→新しいターミナル

![画像](https://assets.st-note.com/img/1749825364-lfwO3p5KYirgc06CHUdDjekX.png?width=1200)

ここがターミナルというコマンド入力欄ですー

### ② init先生を召喚（Git初期化）

![画像](https://assets.st-note.com/img/1749825740-lkiVGC8meyJwFX16tIoKhMAc.jpg?width=1200)

🌳 mainブランチくんと🪵ワークツリーくんが誕生！

```swift
git init -b main
```

![画像](https://assets.st-note.com/img/1749826273-6myFOiAhXSc0RW1tQBJ8Gx5v.png?width=1200)

こんなのが出たら成功

> **読み飛ばしOK!  
> 【コタの疑問解決】git init だけじゃだめ？**  
>   
> ✅ git init -b main の意味  
> \-b は **\--initial-branch** の略です。  
> つまり -b main は **「最初のブランチ名を main にしてね」** という指定です。でも、Gitの **バージョンによって** 初期ブランチ名が違います。  
>   
> ✅ -b main を使うメリット  
> **どんな環境でも最初のブランチ名を main に固定できる。**  
> チーム開発やGitHub連携で main に統一したいときに便利！  
>   
> **🦉 init先生コメント**  
> 「環境によってブランチ名が変わると混乱するから、-b main を使うと安心じゃぞ。最近のGitでも git config で設定を変えれば、毎回 main にできるぞい。」

![画像](https://assets.st-note.com/img/1749825721-k19w7gCvG563QrWiJtxZmlcM.png?width=1200)

---

### ③ プロンプトファイルを書く

**ここからはCursorだけで説明していきます。**

![画像](https://assets.st-note.com/img/1749826110-3DSUsZcr8hoCRptbefgLnQ9Y.png?width=1200)

新しいファイルを作成・名前はchat\_prompt.yaml

![画像](https://assets.st-note.com/img/1749827032-z7Gqmg3cMsoeknbdvZFKQJ9f.png?width=1200)

ファイルが開いたのを確認

![画像](https://assets.st-note.com/img/1749826991-JGTzt0XVjUmC1YAPxen9M5qS.png?width=1200)

最初のプロンプトを入れてファイルを保存（Ctrl + s）

> #system\_prompt  
> #goal: gitとgithubについて、ユーザの質問に回答する

---

### ④ ステージングカゴくんに入れる

![画像](https://assets.st-note.com/img/1749828064-FabqT51GBRfrdohcvZDkOWpL.jpg?width=1200)

gitが初期化された時点で、worktreeという作業台が見えないけど存在してます～

![画像](https://assets.st-note.com/img/1749827123-GOQvXIVyBNmb5a2iwAfeFTnH.png?width=1200)

**git add**

```
git add chat_prompt.yaml
```

---

### ⑤ コミットネコが記録する

![画像](https://assets.st-note.com/img/1749829091-9OwJlmSxHLGYcBkQZgI3TV6d.jpg?width=1200)

commitネコくんが撮影したスナップショットが、mainくんに貼り付く

![画像](https://assets.st-note.com/img/1749829160-6lnbF7oRI0E3xeXqNsMYtQmW.png?width=1200)

```javascript
git commit -m "初回プロンプトを追加"
```

> **読み飛ばしOK!  
> 【コタの疑問解決】-m の意味  
> 🐱 commitネコが書き残す「アルバムのコメント」**  
>   
> git commit -m "コメント"  
> これは、スナップショット（履歴）にタイトルをつける 命令です。  
>   
> ✅ どういうこと？  
> git commit：ネコが写真（作業記録）を撮る  
> \-m "コメント"：その写真の下に「どんな作業だったか」の説明をつける

### 💬 コメントのコツ（メッセージの書き方）

![画像](https://assets.st-note.com/img/1749830645-xCzSqMhY3iD62wJtG5sBk0cv.png?width=1200)

---

### ⑥ 内容を改変する

![画像](https://assets.st-note.com/img/1749830011-t9DA1xpgcWvwrO8VTbECHSfn.png?width=1200)

Cursorだと、変更されたファイルにMマーク（modify）が付くよ！

---

### ⑦ またステージング → コミット

![画像](https://assets.st-note.com/img/1749830200-51tC8kwTZrXOAz3vo4GiH6Rl.jpg?width=1200)

2枚目の写真が貼り付けられて、最新として認識されてる

![画像](https://assets.st-note.com/img/1749830382-pCP50c2jN7EQSLfmyMktoDIu.png?width=1200)

```cs
git add chat_prompt.yaml
git commit -m "概要と役割を追加"
```

---

## 📸 ここまでで得られること

- **過去のプロンプト履歴が全部残っている！**

### 📖 過去のアルバムを見る：git log

![画像](https://assets.st-note.com/img/1749831842-Tt6p5okHlPmELIABFZ0dQ3bx.png?width=1200)

![画像](https://assets.st-note.com/img/1749830560-XOZLsGEqW0SlH5nJCbNKTFRp.png?width=1200)

**出てくる情報：**

- 📸 コミットID（写真の管理番号）
- 🕒 日時
- 👤 誰が作業したか
- 📝 コメント（ -m のやつ）

### gitターミナル？？こんな風になっちゃった･･･ときは

![画像](https://assets.st-note.com/img/1749832609-uMElKkzQVUZAsB6dajiHWmeO.png?width=1200)

Enter押してもEscもCtrl+Cも効かないよ～

「q」を押してください。普通のところに戻ります。ダメな場合は、一回「:（コロン）」を押してから「q」を。  
（※ vimと同じ操作です）

---

## 🧙♀️ 巻き戻し体験（revert魔法使い / resetうさちゃん）

### ① 前の状態に戻したい！

![画像](https://assets.st-note.com/img/1749831896-MebtvomikO8uQ01FwBGLSsZ3.jpg?width=1200)

```
git revert HEAD
```

🌟 「履歴はそのままに、逆操作を追加」  
→ 例えば、うっかりファイルを削除しちゃった時、その削除を「取り消す記録」を1枚追加するような動きです。  
GitHubにpushしても安全。共有作業向きの巻き戻し。

🪄 **1つ前を取り消す**

```
git revert HEAD
```

🪄 **2つ前を取り消す**

```
git revert HEAD~1
```

🪄 **もっと前の特定のコミットを取り消す**

```python
git log --oneline # ← 履歴一覧でコミットID確認
git revert <コミットID>
```

🧠 ポイント：

- 複数のrevertは **順番に** 実行（古いものから）
- 履歴が汚れず、GitHubとの連携も安心！

💡 まるで「過去の失敗に、未来から修正メモを貼りに行く」ようなイメージ！

---

### ② やっぱり最新のに戻したい（revertした後、元に戻したい）

![画像](https://assets.st-note.com/img/1749833474-bQcpG5TyqvHLoFDKJ80e1aMY.png?width=1200)

```cpp
git log --oneline
git revert <さっきのrevertのコミットID>
```

📸 まるで「取り消した履歴」さえも元に戻せる！  
→ 一度revertした内容を「やっぱやめる」と思ったとき、そのrevert自体をrevertすればOK。

ポイント：

- **履歴は積み重なる** から、全部残る＝後から追跡しやすい。
- GitHubにもそのままpushして問題なし（ **中編で出てくるから今は分からなくてOK!**）。

---

**読み飛ばしOK!**

### 【コタの困った解決】revertうまくいかねー

> **revert する対象が「すでに無効化されたコミット」や「変更が無意味な差分」だと、Gitは「やることない」と判断して終了します。**  
>   
> ＊  
>   
> Gitでは、 **すべてのコミットが「親（parent）」を持つ** というしくみになっていて、これが **履歴の流れや分岐、巻き戻しの正確な動き** を決める基盤になっています。  
>   
> **🧬 親子関係とは？**  
> たとえばこの履歴を見てください：  
>   
> C3 (HEAD) ← 最新のコミット  
> ↑ C2  
> ↑ C1  
>   
> C3 の親は C2  
> C2 の親は C1  
>   
> つまり、\*\*コミットは「親のスナップショットを元に作られる」\*\*という構造です。  
>   
> ＊  
>   
> **❗ なぜ revert に親子関係が関係するの？**  
>   
> Gitの revert は、指定したコミットと **その親の「差分」** を反映させることで逆操作を作ります。  
>   
> 例：C3 は C2 に対する変更  
> git revert C3 は、「C3 - C2 の逆」を新しいコミットとして作る  
>   
> 💡 なので、 **revert する対象が「すでに無効化されたコミット」や「変更が無意味な差分」だと、Gitは「やることない」と判断して終了します。**  
>   
> ＊  
>   
> 🧩 実際の履歴例で見る  
>   
> A ── B ── C ← C: 「重要な変更を追加」  
> ↑ └─ D ← D: 「Cをrevert」→ 変更を打ち消す  
> ↑ └─ E ← E: 「Dをrevert」→ つまりCを再適用したい  
>   
> このように、revertが重なると、 **親子の関係性と差分の内容** によって「何が実行されるか」が変わります。  
>   
> ＊  
>   
> ✅ まとめ  
> Gitのコミットは「親 → 子」の関係でつながるタイムライン  
> revert は「子が親とどう違うか」を見て、それを **逆向きに再現する魔法**  
> だから、親子がわかってないと revert の「どこを戻すのか」が見えなくなる  

---

### ③ リセットうさちゃん発動！（resetで履歴ごと戻す）

![画像](https://assets.st-note.com/img/1749834552-sK16L3bP8YQpIFTGa7uv5Ngf.jpg?width=1200)

うさちゃんハードモードの例

### git reset の3つの魔法（うさちゃんの3モード）

🔁 **図解イメージ（イメージ例）**

![画像](https://assets.st-note.com/img/1749835148-gzWwTOy4RQE1jUcJBmIXs5pL.png?width=1200)

---

### 🐰 resetうさちゃん（soft版）：「メッセージだけ変えてコミットし直したい！」やさしめの巻き戻し魔法

![画像](https://assets.st-note.com/img/1749836668-WUoBalE8ew1Qigs3CqjTZcuP.jpg?width=1200)

うさちゃんソフトモード

- git reset --soft <コミットID>
- **HEAD（履歴の目印）だけが過去に戻る**
- ステージングカゴくんの中身（addした内容）はそのまま
- ファイルの中身もそのまま
- 📦「写真の順番だけ戻した状態」→ すぐ違うメッセージで撮り直せる！

```
git reset --soft HEAD~1
```

---

### 🐰 resetウサちゃん（mixed版）：「gitへ記録する部分を変えたい（ファイルはそのまま）」スタンダード魔法

![画像](https://assets.st-note.com/img/1749836657-21MpUnyl9wrDEBvPxAzJLZbT.jpg?width=1200)

うさちゃんmixedモード

- git reset --mixed <コミットID>（← 省略時はこれがデフォルト）
- **HEADとステージングカゴが巻き戻る**
- ファイルの内容（worktree）はそのまま
- 🧺「カゴが空になる」→ ファイルは残ってるのに記録準備が解除される

```
git reset HEAD~1
```

---

### 🐰 resetウサちゃん（hard版）：「時間ごと巻き戻す」最強魔法（注意⚠）

![画像](https://assets.st-note.com/img/1749836711-lSzxrysf6JwKEAcT0LQ4pvbV.jpg?width=1200)

うさちゃんハードモード

- git reset --hard <コミットID>
- **HEAD・ステージングカゴ・ファイルの内容（worktree）すべて過去に戻る！**
- ファイル自体が **物理的に巻き戻る or 消える** （編集中の内容が失われる可能性）
- 💥「作業そのものが過去に戻る」→ まるでなかったことになる

```
git reset --hard HEAD~1
```

**💥 注意：**

- **GitHubにはpushできない（中編で出てくるから今は分からなくてOK!）**
- **チーム作業ではNG！**
- **使うなら「まだpushしていないローカル限定作業」の時に！**

---

### ✅ うさちゃんモードの選び方

![画像](https://assets.st-note.com/img/1749835299-nRT0J536vm2hZbMe8zFyUOEk.png?width=1200)

---

## ✨ 応用ネタ

- Cursorでプロンプト改善 → Gitで記録 → 最強プロンプト集を作る
- prompt-template.yaml を作ってテンプレ化

---

## 💡 GitとGitHubの違いは？

### 【読み飛ばしOKのコタコラム】

> **🧠 真実：主役はGit、GitHubはただの「便利な倉庫」**  
>   
> **🌳 Git = ローカルで動く、履歴をつける道具**  
> Gitはもともと、ローカル（自分のPC）だけで使うために作られたツール。initして addして commitして…全部ローカルで完結する。  
> **つまり：Gitこそが開発の本体。主役。エンジン。**  
>   
> ☁️ **GitHub = オンラインの置き場（しかもGitの上に乗ってるだけ）  
> **GitHubはそのGitの仕組みをクラウドで共有できるようにしたサービス。「クラウドで見れる・チームで使える・UIがある」ってだけ。  
> **つまり：主役ではない。拡張された図書館のようなもの。**  
>   
> 🎭 なぜみんな間違える？名前が紛らわしい！  
> **「GitHub」が先に広まりすぎた！** しかもGUIで操作できるから、「GitHubが全部やってる」と思いがち。実際は、GitがいないとGitHubはほぼ何もできないん。  
>   
> 💥 だからこそ言いたい！  
> 🗣 「名前に惑わされるな！」本当の主役は、ローカルで地味に働くGitたちなんだ！  
>   
> **ボクがめちゃくちゃ驚いた衝撃の事実**  
>   
> 🔹「え、work treeって最初からあるの？」  
> → 並列開発のためにあとから作ると思ってた…。でも実は、最初の1本目もwork treeだった！  
>   
> 🔹 work treeとbranchの違いが分かってなかった  
> → 両方「分岐」みたいなものだと思ってたけど、work tree＝物理的な作業場所、branch＝論理的な分岐。これ全然違う。  
>   
> 🔹 commitネコがローカルにしかいないの！？  
> → これはほんと衝撃。クラウドに行って記録してるわけじゃないんだ…って知って混乱しました。  
>   
> 🔹 ローカルとクラウドの「持ち物リスト」の違いが全然わかってなかった  
> → 何がどこにあるのか分からず、とにかく全部がクラウドにあると思ってた  
>   
> 🔹 ステージング？なにそれ  
> → 変更したのにcommitされない！？なんで！？addしないとcommitネコは見てくれない！  

---

## 有料部分では･･･

- ✅ **キャラが丁寧にGitを教えてくれるGPTs**
- ✅ **キャラ付き3D図解・イラストまとめ**
- ✅ **まとめ用のGit操作早見表と復習チェックリスト**

が入っています。GPTsは2.GitHub編にも対応してますー。

## ここから先は

316字 / 12画像

この記事のみ ¥ 200〜

まとめ買い用です。

### Git記事まとめ買い

800円

1\. ローカルGit編（500円） 2.ローカルGitとクラウドGitHub連携の全ステップ（500円） が入っています。

Gitアレルギーが治っちゃう！キャラで覚えるGitローカル編（Cursor対応）【1】ローカル編 GPTs付き！｜コタ
---
title: GitアレルギーもCLIアレルギーもバイバイ！【4/4】GitHubでタスク整理･タスク検収･統合する【無料で読めます】｜コタ
source: https://note.com/nyattoh/n/n94dae143d836?sub_rt=share_pw#89f99383-ac61-4e69-adc1-31434e2275f9
author:
- '[[コタ]]'
published: 2025-06-28
created: 2025-06-29
description: 驚愕の事実！  「プル・リクエスト」って「プル」だよね？「ひっぱるんだよね？」 ローカルではなく、GitHub側に引っ張るんだって。これありなのー？  主語がプルするのである。目的語にプルしてもらうのである。   つまり、プル･リクエストはローカルにはない！
  GitHubにしかプルリク＝PRはないのだ！！  コタの驚愕  🪄 この記事でやること：開発タスクの管理 今回の前半全体図 手動でIssue → プルリク →
  CI（Continuous Integration／継続的インテグレーション） → Mergeを体感し、その後haconiwaで効率化！    Issue 作成：GitHu
tags:
- clippings
- エンジニア
- コード
- プロダクト
- github
---
![見出し画像](https://assets.st-note.com/production/uploads/images/198506880/rectangle_large_type_2_c35f7772ac3e020de2c25f5bdbdb368d.jpeg?width=1200)

## GitアレルギーもCLIアレルギーもバイバイ！【4/4】GitHubでタスク整理･タスク検収･統合する【無料で読めます】

[コタ](https://note.com/nyattoh)

## 驚愕の事実！

**「プル・リクエスト」って「プル」だよね？「ひっぱるんだよね？」  
ローカルではなく、GitHub側に引っ張る** んだって。これありなのー？

主語がプルするのである。目的語にプルしてもらうのである。

> **つまり、プル･リクエストはローカルにはない！  
> GitHubにしかプルリク＝PRはないのだ！！**

コタの驚愕

---

## 🪄 この記事でやること：開発タスクの管理

![画像](https://assets.st-note.com/img/1750943165-mCYMD4FyLQPBX85jg1Kcl6wG.jpg?width=1200)

**今回の前半全体図**

**手動でIssue → プルリク → CI（Continuous Integration／継続的インテグレーション） → Mergeを体感し、その後haconiwaで効率化！**

1. **Issue 作成** ：GitHub 上で **Issue（タスクみたいの）** を作成します。
2. **プルリクエスト（PR）作成** ：新しいブランチを作成し、修正を行い、その変更を **PR** として提出。
3. **CI 実行** ：GitHub Actions でテストを通し、 **緑のチェック** が出るまでコードを修正。
4. **Merge & 完了** ：レビューを受けて **PR** が承認されたら、 **Merge** を実行。
5. **haconiwaでラクラク** ！並列コンペ実装

---

## 💡 やり方だけ教えて！って人はコードの所（背景黒）だけ見てください！

## 💡 自分が読みたいところだけ読めばOK！

---

## 今回はこのキャラクターが登場するよ！

![画像](https://assets.st-note.com/img/1750931338-0xUqdXFNGupLwTMyaCDhHiB9.jpg?width=1200)

今回登場するキャラクターのみなさん

---

## 🪄 実践テーマ：GitHubでIssue → プルリク → CI を手動で体感（後半はhaconiwaで並列開発）

### ✏️ 想定する作業

- GitHub の **Issue** を作成して「やること」を整理
- 新しい **ブランチ** を切り、修正作業を行う
- **プルリクエスト（PR）** を作成し、GitHub Actions で CI を通過させる
- **レビュー** を経て **Merge** する
- **haconiwa** を使って、並列開発環境（worktree）を立ち上げ

GitHub で Issue → プルリク → CI の流れを体感しよう（haconiwa活用）

---

## 読み飛ばしOK！前回から引き続き登場するキャラのみなさん

![画像](https://assets.st-note.com/img/1750932494-67IPjkMpqxiUumg48bz2ADHR.jpg?width=1200)

![画像](https://assets.st-note.com/img/1750932501-V8GKatYSwc4iErCvIR6NPzmL.png?width=1200)

![画像](https://assets.st-note.com/img/1750932510-UjiC56fLwSlDInK1qd90gFec.jpg?width=1200)

![画像](https://assets.st-note.com/img/1750932518-lVNXUtk8jG4ZvT0p5h93gFeS.png?width=1200)

![画像](https://assets.st-note.com/img/1750932526-HqvcmDMJdulLBAxi4z0bjGCa.jpg?width=1200)

---

## 「やること」を書くカード（Issue）を作る(1分くらい）

![画像](https://assets.st-note.com/img/1750938743-uOB5rjKtZFa0U3pMPvNQwq8m.jpg?width=1200)

タスクを書く付箋メモみたいなイメージだよ～

### ✅ステップ1: イシューくんの日本語テンプレートでIssueをつくる

![画像](https://assets.st-note.com/img/1750939046-B85vg3aoukQNrD4zFihepMPx.png?width=1200)

**例えばこんな感じ**

![画像](https://assets.st-note.com/img/1750944857-EmDuLKIvfHCZBc5GN4jXzY0S.png?width=1200)

GitHubのリポジトリからIssuesを開いてね

**タイトル：**  
docs: Change heading in README (最初の見出し)

> \### What  
> アプリの説明を変更  
>   
> \### Why  
> 分かりやすくするため  
>   
> \### How  
> \- 'Gitアレルギー診断webアプリ' の 冒頭に 'お手軽' を追加  

日本語版の例

※ previewを押すと、マークダウンがどう見えるか確認できるよ～  

> \### What  
> Change the description of the app.  
>   
> \### Why  
> More easy to understand what this is.  
>   
> \### How  
> \- Update the heading text

英語版の例

---

### ✅ステップ2: イシューくん活用のコツ

![画像](https://assets.st-note.com/img/1750945165-l04MgpL7NAFT2v5ixVJoeOYE.png?width=1200)

チーム開発なら、ここでチャットっぽくやり取りもできるよ～

> **1トピック＝1 Issue** ：  
> タスクメモと同じ感覚で、1つのIssueには1つのやることを書く。  
>   
> **ラベル貼り** ：  
> bug / docs / enhancement… のように色分けされたラベルを貼ると、Issueの種類や優先度がひと目で分かります。  
>   
> **担当者アサイン** ：  
> @名前 で「誰がやるか」を決めると、Issueが放置されるのを防げます。

---

### 読み飛ばしOK! コタコラム：ひとりでも Issue を切るメリット

1. **頭の整理**
	- "TODO.txt" を GitHub に置き換え。検索・ラベル・マイルストーンで並び替え自在。
2. **モチベ管理**
	- 「今日は bug/ログイン失敗時の横幅崩れ (#7) を片付けよう」など、作業単位が明確。
3. **後から来る自分への説明書**
	- 数週間後に「なぜこう実装した？」と迷ったとき、Issue と PR の議論が答えになる。

> **Point**: "他人のため" ではなく "未来の自分" のためのドキュメントと思うと続けやすい。

---

## Issue用のブランチを作成する

![画像](https://assets.st-note.com/img/1750943768-PNJXtvQU3CuYx64LZsd1yBl5.jpg?width=1200)

カメレオンくんが作ってくれるよ！

### ✅ステップ1:修正専用のブランチを切る

```python
# 作業する Issue 用のブランチを作成
git checkout -b issue-<Issue番号>-<ブランチ名>
```

**Isshue番号は、👇ここで確認**

![画像](https://assets.st-note.com/img/1750943846-QPt9lqIHGxzXg63mObdB5YuE.png?width=1200)

GitHubのIssuesのところにある#付きの数字です

> 例えば、Issue 1の「README の修正」を行う場合は：  
> git checkout -b issue-1-readme-fix

![画像](https://assets.st-note.com/img/1750944304-od13VY4zI7w6kC8uRvG9qmJy.png?width=1200)

Cursorだとこんな感じになります

---

## 修正作業をローカルで行って、GitHubへ

![画像](https://assets.st-note.com/img/1750947253-vUzKmgnW6RaXf5rDlPeYAbdO.jpg?width=1200)

2番目の記事で紹介したpushですー

### ✅ステップ1:README.mdを開いて、「お手軽」を書き加える

![画像](https://assets.st-note.com/img/1750945906-Bm0DWf1i6ZwzjvXrGHc3goxh.png?width=1200)

ちなみに、左上の真ん中辺にあるアイコンを押すと、 gitの履歴とかが見られてお得

---

### ✅ステップ2:ローカルGitにコミットする

では、ローカルのGitに先ずはコミットしましょー。  
ステージングカゴくん、コミットネコにお願い！

![画像](https://assets.st-note.com/img/1750946898-kOueZLI9TwG7h4J6UrtKyzFs.jpg?width=1200)

git add.

![画像](https://assets.st-note.com/img/1750946910-HyzeM423nuqPLKWUCE6BwXGI.jpg?width=1200)

git commit -m "fix: README change for Issue #1"

```cs
# 修正後のファイルをステージング
git add .

# 変更をコミット
git commit -m "fix: README change for Issue #1"
```

![画像](https://assets.st-note.com/img/1750946374-FGrfSt3cVB9De5QZT7IhRYzg.png?width=1200)

こんな感じになります

---

### ✅ステップ3: 変更をリモートリポジトリにプッシュする

![画像](https://assets.st-note.com/img/1750947351-4jI9ewACZE3Wcuq0QtXisoUO.jpg?width=1200)

ここで、新しいブランチも一緒に作られるよ

```python
# リモートにプッシュ
git push origin issue-1-readme-fix
```

![画像](https://assets.st-note.com/img/1750947552-OJXN8B4Lec0t7IyFTEzCSlQH.png?width=1200)

**Cursorの結果**

![画像](https://assets.st-note.com/img/1750947631-BSx1v4YQMXagkCWm0bpr3V9l.png?width=1200)

GitHubを見てもブランチができてる！

---

## プルリクで、タスクの検収→ガッチャンコ

### ✅ステップ1:プルリクエスト（PR）を作る

![画像](https://assets.st-note.com/img/1750949635-jLK2o9xe0dH853z4VO7qDnAS.jpg?width=1200)

**プルリク箱くん**

![画像](https://assets.st-note.com/img/1750947789-smZ4MOIFoC7nG9P8iyhRStQf.png?width=1200)

GitHubのcodeを開くと、こんなのが出てるよー

- GitHubのリポジトリにアクセスします。
- プッシュしたブランチが表示されるので、「Compare & pull request」ボタンをクリックします。
- プルリクエストにタイトルや説明を追加し、作成します。

**プルリク箱くん本文の書き方**

> この PR は Issue #1 を解決します。  
>   
> \## 変更内容  
> \* README.md の見出しを変更  
>   
> \## 確認方法  
> \`markdownlint README\_JA.md\` がエラーなしで終了すること

![画像](https://assets.st-note.com/img/1750948396-2AswNDMq7YRxZF0ceUO635uJ.png?width=1200)

GitHubはこんな感じですー

> ※ 「Closes #1」 と本文末に書けば、日本語本文でも自動でIssueが閉じます。

**豆知識**

GitHub Actionsや、Claude Code、Gemini CLIなどでは、ここでテストを行って（タスクの検収）、バグがないことを確認してからマージという方法がとれます。（※）

> **（※）読み飛ばしOK! コタコラム  
> **  
> **CI（Continuous Integration／継続的インテグレーション）って何？  
> **  
> みんなが書いたコードを **こまめに取り込み、 自動でビルド＆テスト** して"壊れていないか"を早期にチェックする仕組み。  
> 上で書いた Actionsなどで自動チェックしてからマージをすることでバグを早期発見・対処して、人的ミスも減らせる。  
>   
> ① ブランチで修正  
> ↓ push  
> ② GitHub がフック  
> ↓  
> ③ CI サーバー（GitHub Actions 等）が  
> \- 依存パッケージをインストール  
> \- コードをビルド  
> \- テストを実行  
> ↓  
> ④ 成功 → ✅ / 失敗 → ❌  
> ↓  
> ⑤ PR 画面に結果表示  

### ✅ステップ2:mainブランチにマージ！

![画像](https://assets.st-note.com/img/1750950695-gcjnDkpHZryL7PsBf3J2KhTX.jpg?width=1200)

**ガッチャンコー！**

![画像](https://assets.st-note.com/img/1750948682-6kTHw9lEgn4IirjdCsy3JGBV.png?width=1200)

**マージ実行！**

---

## お片付け

![画像](https://assets.st-note.com/img/1750951518-1Cdir4q7ZFTn9WRDsjfg5lbe.jpg?width=1200)

要らなくなった、修正用のブランチを削除します。Issueもクローズします。

### ✅ステップ1:GitHub側のブランチ削除

![画像](https://assets.st-note.com/img/1750951101-x5zXU8jAhgNT916LecSKOlnY.png?width=1200)

自動で出てきてくれるボタンを押せばOK!

---

### ✅ステップ2:GitHubのIssueをクローズ

![画像](https://assets.st-note.com/img/1750951696-tvFuC5YBgfjwPqbmhNJc0Mo2.png?width=1200)

---

### ✅ステップ3:ローカルを同期

```python
git pull origin main
git checkout main
```

![画像](https://assets.st-note.com/img/1750952650-8skZhWz90iJlRqNbF6Cf3xPy.png?width=1200)

---

## 小さい悩みあるある

### 🤔ブランチ名が決まらない

docs/修正内容 / feat/追加内容 の2語ルール を参考に、内容がわかる名前にしましょう。

### 🤔PR タイトルが長い

先頭を「動詞: 対象」に固定（例 docs: README 更新）すると簡潔になります。

### 🤔レビュアーがいない

個人リポジトリなら自分で **Approve** してOK。セルフレビューの練習になります。  

---

## コタコラム：「Codex Task → PR」 をソロ開発で

1. **Issue** を書く or 思いついた TODO を Codex "New Task" に直接投げる
2. Codex がクラウド SandBox で実装 → 20 分前後で **自動 PR**
3. 自分がレビューして Merge（CI も回る）
4. Issue 番号を書いておけば PR マージで自動 Close

> **メリット**:  
> "手が空かない日に小さめ Task を投げておくだけ" で翌朝 PR が届く。  
>   
> **注意点**:  
> 生成コードの可読性／テスト網羅率はレビュー必須。  
>   
> **Haconiwa 併用**:  
> Codex が作った変更を手元 worktree に同期→ローカルで動作確認→再 push といった流れも取れる。

---

## Gitをもっと理解したくなったら

Gitを体系的に分かりやすく説明してくれている無料のサイトがあります！  
辞書の代わりとしても活用してみてください。

ボクはこれから、これを元に、最初の記事からもっと分かりやすく説明を加えていこうと思っています。

[**Git** *git-scm.com*](https://git-scm.com/book/ja/v2)

  

このサイトは、「数学ガール」で有名な、結城浩さんから教えていただきました！結城さん、ありがとうございます～～～！！

---

## GitとGitHubの便利な使い方

ここからは、随時更新していく予定の場所です。  
  
プログラムのソースコードっていうイメージがあると思いますが、それだけじゃないよ、というコーナーです。

### 文章の管理

文章の管理にも使えます。  
つまりそう、このnoteの記事とかも、前とどこが変わったかどう変えたのかが分かるようになる････

### 画像の管理

重たくなるので微妙ですが、WEB制作の人やデザイナーの方にはあるあるですがPhotoShopとかでドンドン違うのが送られてきて、前に作業していたファイルどれだっけ、どれが最新だったっけ、ファイル名に日付入れ忘れた、違うバージョンで作業しちゃった･･･がなくなる･･･はず･･･

---

## 最後に

まずは、読んでいただいて本当にありがとうございました。  
これから、またもっと分かりやすく細々と書き直したりしていくと思います。  
  
今回も特典を考えていたのですが、上手く作れなくて記事の公開が大幅に遅れてしまいました。

![画像](https://assets.st-note.com/img/1751109968-G9KsZN1Mhjew68AqBHWL5XVT.png?width=1200)

読んでいる方のGitアレルギーが少しでも治っていますように。

## ここから先は

0字

まとめ買い用です。

### Git記事まとめ買い

1,200円

1\. ローカルGit編（500円） 2.ローカルGitとクラウドGitHub連携の全ステップ（500円） が入っています。 3.さよならG…

[![note会員1000万人突破記念　1000万ポイントみんなで山分け祭　エントリー7/8（火）まで](https://assets.st-note.com/poc-image/manual/production/20250623_1000_top_notedetail.jpg?width=620&dpr=2)](https://note.com/info/n/ncceb4a6506fc)

GitアレルギーもCLIアレルギーもバイバイ！【4/4】GitHubでタスク整理･タスク検収･統合する【無料で読めます】｜コタ
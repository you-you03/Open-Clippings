---
title: "NotebookLMにKindleを取り込むスプリクトをChatGPTで書いてみた(コード全文)｜セージ"
source: "https://note.com/ssblog/n/n4b4664c2949b"
author:
  - "[[note（ノート）]]"
published: 2024-06-18
created: 2025-05-09
description: "こんにちは。ChatGPTでこんなもの作ってみましたっていう記事です。     できる事 ・Kindleを全ページ自動で画面スクショ ・スクショ画像からOCRで文字起こし ・ドキュメントにしてGoogleDriveに自動アップロード ・ついでにPDFファイルとTXTファイルも作成 ・スクショデータは全削除 ・生成されるファイルの名前はOCRの最初の10文字を設定  記事内で生成したコード全文とMacで実際に動かすまでの手順の解説を載せてます。こういうことやってみたかったという人はぜひ試してみてください。  参考までに 私は非エンジニア。素人と言っても全く問題ない程度の知識しかないので、"
tags:
  - "clippings"
  - "notebooklm"
  - "ai"
  - "プロダクト"
---
![見出し画像](https://assets.st-note.com/production/uploads/images/144463644/rectangle_large_type_2_4a0298597793009d4d4d07963b8106bd.png?width=1200)

## NotebookLMにKindleを取り込むスプリクトをChatGPTで書いてみた(コード全文)

[セージ](https://note.com/ssblog)

こんにちは。ChatGPTでこんなもの作ってみましたっていう記事です。

  

できる事  
・Kindleを全ページ自動で画面スクショ  
・スクショ画像からOCRで文字起こし  
・ドキュメントにしてGoogleDriveに自動アップロード  
・ついでにPDFファイルとTXTファイルも作成  
・スクショデータは全削除  
・生成されるファイルの名前はOCRの最初の10文字を設定

記事内で生成したコード全文とMacで実際に動かすまでの手順の解説を載せてます。こういうことやってみたかったという人はぜひ試してみてください。  
  
参考までに  
私は非エンジニア。素人と言っても全く問題ない程度の知識しかないので、そんな人でもこんなことできたよってことが伝わる一つの例になればいいなと思っている。

※Amazon Kindkeの利用規約と著作権法をざっと確認して、「私的利用の複製」の範囲っぽいことは確認済み。違ってたらごめんなさい。  
※Macを使ってること前提になります、Windowsの人は厳しいかも  

## Notebook LMとは

  
NotebookLMを知らない人のために簡易説明  
  
Googleが提供している生成AIサービス群の中の一つ。  
ユーザーのアップロードした資料(PDF、TXT、GoogleDOC等)を読み込んで、サマリーや目次を作ったり、その資料をインプットした上で質問に答えてくれたりする。なんの質問をすればいいかも提案してくれる。

  
さらに今後は資料の内容に沿ってAI同士が会話してくれたり、その会話の中に入って行けたりもするようになるらしい…

もちろん、音声で対話できるようにもなっていくと思うけど、そうなれば本を読むことが苦手な人や視覚よりも聴覚が優位で本を読むことがどうしても難しかった人たちにとって、すごく優しい世界になっていくよな〜と。

本バリバリ読めるぜって人も、情報の取り入れ方がガラッと変わる気がしていて、特に学術論文や難しい書籍から情報を取り入れたいときに力を発揮しそう。

資料の内容を全て暗記して理解している人の隣で質問しながら一緒に読み進めていけるような感じかな？しかもその人が勝手にノートにまとめてくれてるみたいな。  

## 作ろうと思ったきっかけ

これからNotebook LM以外にも山ほど類似サービスが出てくると思うけど、どこがシェア取っても自分のKindleのデータをいつでも読み込めるようにしておきたいなと思い、KindleデータをOCRしてGoogleDocにアップロードするスクリプトをChatGPTで書きました。

というのも、X でけんすう氏がこういう投稿をしていたので。

  

同じことやりたい人いるんじゃないかなと思って、非エンジニアでも簡単にできたよっていう参考になればと思ってまとめます。

あと完成したコードも全部貼るので、Macを使ってる方ならほぼそのまま使えそう。

## 必要なもの

・Macbook  
・Kindleアプリ(と書籍データ)  
・Googleアカウント  
・ChatGPT-4o  
・時間(2、3時間くらい？)

**あったらいいもの**  
・HTMLならなんかちょっとわかるかもくらいの感覚  
・中学くらいの英単語語彙力  
・インターネットが好きな気持ち

## プログラム詳細(コード全文)

具体的なコードと手順の説明です。  
  
改めておさらい。  
下記の内容を１クリックでやってくれるプログラムです。  
  
**・Kindleを全ページ自動で画面スクショ  
・スクショ画像をOCRで文字起こし  
・GoogleDocにしてGoogleDriveに自動アップロード  
・ついでにPDFファイルも作成  
・スクショ画像は全削除  
・生成されるファイルの名前はOCRの最初の10文字を設定**

事前に設定するのは「スクショ枚数」「ページめくり方向」「スクショ座標」の３つ。

**コード全文**

```swift
-- 新規フォルダを作成する関数
on createFolder(folderPath)
    do shell script "mkdir -p " & quoted form of folderPath
end createFolder

-- スクリーンショットを撮る関数
on takeScreenshot(savePath, captureRect)
    -- captureRect は "x,y,width,height" 形式の文字列
    do shell script "screencapture -R " & captureRect & " " & quoted form of savePath
end takeScreenshot

-- 画像ファイルを削除する関数
on deleteFiles(filePaths)
    repeat with f in filePaths
        do shell script "rm " & quoted form of f
    end repeat
end deleteFiles

-- メインスクリプト
set pages to 200 -- スクリーンショット数
set keychar to (ASCII character 28) -- ページめくり方向(28=左,29=右)
set currentDate to do shell script "date +%Y%m%d_%H%M%S"
set folderPath to (POSIX path of (path to desktop folder)) & "Kindle_Screenshots_" & currentDate & "/"

-- キャプチャする範囲を指定 (x, y, width, height)
set captureRect to "50,100,1500,850"

-- 新規フォルダの作成
createFolder(folderPath)

-- Kindleアプリの前面化
tell application "Amazon Kindle" to activate

-- スクリーンショットを取得
set screenshotPaths to {}
repeat with i from 1 to pages
    set screenshotPath to folderPath & "screenshot_" & i & ".png"
    
    -- スクリーンショットを撮影
    takeScreenshot(screenshotPath, captureRect)
    
    -- スクリーンショットのパスをリストに追加
    copy screenshotPath to end of screenshotPaths
    
    delay 0.3 -- スクリーンショット保存時間
    
    -- ページめくり
    tell application "System Events"
        keystroke keychar
        delay 0.2 -- ページめくり後の安定時間
    end tell
end repeat

-- Pythonスクリプトの内容（機密情報はプレースホルダーに置き換え）
set ocr_script to "
# -*- coding: utf-8 -*-
import os
import subprocess
from markdown_it import MarkdownIt
from google.cloud import vision_v1
from google.oauth2 import service_account
from googleapiclient.discovery import build

# パスの設定
folder_path = \"" & folderPath & "\"
ocr_output_file = folder_path + 'ocr_output.txt'

# 環境変数を設定（サービスアカウントキーのパスを指定）
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/path/to/your/service-account.json'

# Google Cloud Vision APIのクライアントを設定
vision_client = vision_v1.ImageAnnotatorClient()

# OCRの実行
def perform_ocr(image_path):
    with open(image_path, 'rb') as image_file:
        content = image_file.read()
    image = vision_v1.Image(content=content)
    response = vision_client.text_detection(image=image)
    texts = response.text_annotations
    if len(texts) > 0:
        return texts[0].description
    else:
        return ''

# 画像ファイルのリスト取得
image_files = [f for f in os.listdir(folder_path) if f.startswith('screenshot_') and f.endswith('.png')]

# OCRの実行
ocr_text = ''
try:
    with open(ocr_output_file, 'w', encoding='utf-8') as output:
        for image in sorted(image_files):
            image_path = os.path.join(folder_path, image)
            print(f'Processing image: {image_path}')
            text = perform_ocr(image_path)
            ocr_text += text
            output.write(text)
except Exception as e:
    print(f'Error in OCR process: {e}')
    exit(1)

# 最初の10文字を取得してファイル名に使用
try:
    file_name_prefix = ocr_text[:10].strip().replace(' ', '_').replace('/', '_')
    if not file_name_prefix:
        file_name_prefix = 'OCR_Output'
    md_output_file = folder_path + file_name_prefix + '.md'
    ocr_output_file = folder_path + file_name_prefix + '.txt'
    pdf_output_file = folder_path + file_name_prefix + '.pdf'
except Exception as e:
    print(f'Error in generating file names: {e}')
    exit(1)

# Markdown変換
try:
    md = MarkdownIt()
    md_text = md.render(ocr_text)
    with open(md_output_file, 'w', encoding='utf-8') as output:
        output.write(md_text)
except Exception as e:
    print(f'Error in Markdown conversion: {e}')
    exit(1)

# Google Drive にアップロード
try:
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    SERVICE_ACCOUNT_FILE = '/path/to/your/service-account.json'

    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    drive_service = build('drive', 'v3', credentials=credentials)

    # Google Drive フォルダID（プレースホルダー）
    folder_id = 'YOUR_FOLDER_ID'

    file_metadata = {
        'name': file_name_prefix,
        'parents': [folder_id],
        'mimeType': 'application/vnd.google-apps.document'
    }
    document = drive_service.files().create(body=file_metadata, fields='id').execute()
    doc_id = document['id']

    with open(md_output_file, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    docs_service = build('docs', 'v1', credentials=credentials)
    requests = [{'insertText': {'location': {'index': 1}, 'text': md_content}}]
    docs_service.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()
    print(f'Document created: {doc_id}')
except Exception as e:
    print(f'Error in uploading to Google Docs: {e}')
    exit(1)

# PDFを作成
try:
    img_files = [os.path.join(folder_path, f) for f in image_files]
    subprocess.run(['/opt/homebrew/bin/img2pdf'] + img_files + ['-o', pdf_output_file], check=True)
except Exception as e:
    print(f'Error in PDF creation: {e}')
    exit(1)
"

-- 一時Pythonファイルのパスを設定
set tempPythonFile to folderPath & "ocr_script.py"

-- Pythonスクリプトを書き出し (printf を使用)
do shell script "printf %s " & quoted form of ocr_script & " > " & quoted form of tempPythonFile

-- ファイルの内容を確認（必要に応じコメントアウト）
do shell script "cat " & quoted form of tempPythonFile

-- Pythonスクリプトを実行（python3 コマンドを使用）
try
    do shell script "python3 " & quoted form of tempPythonFile & " 2>&1"
on error error_message
    -- エラーメッセージをログに保存
    set errorLogFile to folderPath & "error_log.txt"
    set fileDescriptor to open for access (errorLogFile as POSIX file) with write permission
    write error_message to fileDescriptor
    close access fileDescriptor
    display dialog "An error occurred. Please check the error log." buttons {"OK"} default button "OK"
    return
end try

-- スクリプト実行後に一時Pythonファイルを削除
do shell script "rm " & quoted form of tempPythonFile

-- スクリーンショット画像を削除
deleteFiles(screenshotPaths)

-- 終了メッセージ
display dialog "Screenshots have been captured, processed with OCR, and uploaded to Google Docs." buttons {"OK"} default button "OK"
```

### コードに含まれている詳細のアクション

1\. **スクリーンショットを撮るためのフォルダを作成**:  
• デスクトップ上にタイムスタンプを含むフォルダを作成。  
2\. **Kindleアプリを前面に表示**:  
• Kindleアプリをアクティブにする。  
3\. **スクリーンショットを取得**:  
• 指定された範囲で連続してスクリーンショットを撮影し、フォルダに保存。(指定範囲は自分で座標入れる)  
• ページをめくりながらスクリーンショットを撮り続ける。  
4\. **OCRを実行するためのPythonスクリプトを生成**:  
• フォルダに一時的なPythonスクリプトを書き出し、OCRを実行。  
5\. **スクリーンショット画像のOCR処理**:  
• Google Cloud Vision APIを使用して、スクリーンショットからテキストを抽出し、テキストファイルに保存。  
6\. **OCR結果のファイル名を生成**:  
• テキストの先頭10文字を使用してファイル名を作成。  
7\. **OCR結果をMarkdownに変換**:  
• OCRで取得したテキストをMarkdownに変換し、Markdownファイルとして保存。  
8\. **Google Drive にアップロード**:  
• 変換したMarkdownファイルをGoogle Docsにアップロード。  
• Google Driveの指定フォルダに保存。  
9\. **スクリーンショット画像からPDFを作成**:  
• すべてのスクリーンショット画像を結合してPDFを作成。  
10\. **後処理**:  
• 一時的なPythonスクリプトとスクリーンショット画像を削除。  
• 完了メッセージを表示。  

## 具体的な手順

下記手順で進めれば、Macの上でプログラム実行できるようになります。1発ではうまく行かないけど、エラーが出るとエラーファイルが生成されるようになってるので、それをGPTに投げて改善してを繰り返してたら多分2,3時間で出来上がると思われます。

1. ChatGPTのGPTs「Code Copilot」を開く
2. コード全文と共に下記テキストを送信する
	1. このコードは、Apple Scriptを使ってKindleアプリからスクリーンショットを撮影し、それらのスクリーンショットからOCR（光学文字認識）を実行して、結果をGoogle Docsにアップロードする一連の操作を行うスクリプトです。このコードを実行するために必要な環境設定とAPI設定の手順を順を追って教えてください。
3. GPTが教えてくれた手順に沿って設定を行う
4. Macにインストールされている「スクリプトエディタ」を開く
5. コードを貼り付けてKindleを開き実行する
6. エラーが発生するのでエラーテキストをChatGPTに送信して原因を聞き対処する

あとは５〜６の繰り返し  

## 終わりに

あとはNotebookLM開いて、Googleドライブから読み込みたいファイルを選ぶだけです！

すでに問題なく動いてるコードがある分、かなりスムーズに実行までできるんじゃないかなと思います！

プログラミング未経験でもこのくらいならサクッとできるようになってるのすごいよなぁ。

  

## もし時間あれば是非こちらも覗いてください

「人間には成せなくても、AIになら話せることがある」をコンセプトにしたAI僧侶をひたすらに仏教に関する教え・考え・知識を詰め込んで作りました。

すると予想よりもみんな苦しんでて、辛くて、抱えてるということがわかったという話です。

  

NotebookLMにKindleを取り込むスプリクトをChatGPTで書いてみた(コード全文)｜セージ
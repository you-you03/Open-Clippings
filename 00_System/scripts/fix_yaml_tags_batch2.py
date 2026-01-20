#!/usr/bin/env python3
"""
YAML形式エラーを修正するスクリプト（バッチ処理版2）
タグの配列形式とリスト形式の混在を修正
"""
import re
import yaml
from pathlib import Path

def fix_tags_format(content: str) -> str:
    """タグの形式を修正"""
    if not content.startswith("---"):
        return content
    
    match = re.match(r"^(---\n)(.*?)(\n---\n)(.*)$", content, re.DOTALL)
    if not match:
        return content
    
    frontmatter_str = match.group(2)
    lines = frontmatter_str.split('\n')
    new_lines = []
    tags_collected = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # tags: ["clippings", "生活"] のような配列形式を検出
        if re.match(r'^tags:\s*\[', line):
            # 配列からタグを抽出
            match_tags = re.search(r'\[(.*?)\]', line)
            if match_tags:
                tags_str = match_tags.group(1)
                tags = [t.strip().strip('"').strip("'") for t in tags_str.split(',') if t.strip()]
                tags_collected.extend(tags)
            
            i += 1
            # 次の行がリスト形式のタグかチェック
            while i < len(lines) and re.match(r'^\s*-\s*', lines[i]):
                tag_line = lines[i]
                tag_match = re.search(r'-\s*["\']?(.*?)["\']?\s*$', tag_line)
                if tag_match:
                    tag = tag_match.group(1).strip()
                    if tag not in tags_collected:
                        tags_collected.append(tag)
                i += 1
            
            # タグをリスト形式で追加
            new_lines.append("tags:")
            for tag in tags_collected:
                new_lines.append(f'  - "{tag}"')
            tags_collected = []
            continue
        
        new_lines.append(line)
        i += 1
    
    new_frontmatter = '\n'.join(new_lines)
    
    # YAML形式が正しいか確認
    try:
        yaml.safe_load(new_frontmatter)
        return f"---\n{new_frontmatter}\n---\n{match.group(4)}"
    except yaml.YAMLError:
        return content

def fix_file(filepath: Path) -> bool:
    """1つのファイルを修正"""
    try:
        content = filepath.read_text(encoding="utf-8")
        fixed_content = fix_tags_format(content)
        
        if content != fixed_content:
            filepath.write_text(fixed_content, encoding="utf-8")
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    """メイン処理"""
    error_files = [
        "02_Clippings/1_コレクション_興味_コーヒー/「サザコーヒー」流・地方発\"本物ブランド\"の育て方~タダコーヒーから６万円ゲイシャまで、体験階段でファンをつくる~｜黒澤 友貴.md",
        "02_Clippings/3_プロダクト開発_NotebookLM/NotebookLMにKindleを取り込むスプリクトをChatGPTで書いてみた(コード全文)｜セージ.md",
        "02_Clippings/3_プロダクト開発_Obsidian/Obsidian Bases 入門｜松濤Vimmer.md",
        "02_Clippings/3_プロダクト開発_Obsidian/Obsidian Web Clipper がすごい.md",
        "02_Clippings/3_プロダクト開発_Obsidian/Obsidian Web ClipperとGemini連携による効率的な情報収集設定.md",
        "02_Clippings/3_プロダクト開発_Obsidian/Obsidian → Notion 自動同期システムの作り方｜しょーてぃー.md",
        "02_Clippings/3_プロダクト開発_Obsidian/Obsidianで折れ線や棒グラフを描くには.md",
        "02_Clippings/3_プロダクト開発_Obsidian/Obsidianを使ったWebクリップのやり方｜a-natsuki.md",
        "02_Clippings/3_プロダクト開発_Obsidian/「先週何したっけ？」をゼロに：Obsidian + Claude Codeを業務アシスタントに.md",
        "02_Clippings/3_プロダクト開発_Obsidian/【Obsidian×Cursor】面倒な金曜日の振り返りが「気持ちいい習慣」に変わった話｜アオキタカユキ  iCARE UI Designer.md",
        "02_Clippings/3_プロダクト開発_Obsidian/【短報】noteの記事をmarkdownで保存する方法｜Koji Doi｜AIエンジニア｜webライター｜バイオ系ライター・アナリスト.md",
        "02_Clippings/3_プロダクト開発_Obsidian/【非エンジニアでもできる】Github×Cursor×Obsidian設定マニュアル〜非エンジニアでもできる〜｜すぅ  AI駆動PM.md",
        "02_Clippings/3_プロダクト開発_コード_エンジニア基礎/Gitアレルギーが治っちゃう！キャラで覚えるGitローカル編（Cursor対応）【1】ローカル編 GPTs付き！｜コタ.md",
        "02_Clippings/3_プロダクト開発_コード_エンジニア基礎/GitアレルギーもCLIアレルギーもバイバイ！【44】GitHubでタスク整理･タスク検収･統合する【無料で読めます】｜コタ.md",
        "02_Clippings/3_プロダクト開発_コード_エンジニア基礎/LINE Botとは？何ができる？メリット・デメリットや成功事例を紹介 - Paintnote Media_2025-06-27.md",
        "02_Clippings/3_プロダクト開発_コード_エンジニア基礎/tejasticediscord-rss-bot Discord RSS Bot with translation and X post features.md",
        "02_Clippings/3_プロダクト開発_個人開発/個人開発で月20万円を目指すための考え方.md",
        "02_Clippings/4_キャリア_事例_シニア/「チームみらい」公認候補予定者一覧 ｜安野たかひろ スタッフ＠ チームみらい 【公式】.md",
        "02_Clippings/4_キャリア_事例_デザイナー/プロダクトデザイナーがおすすめする「伝わる」ポートフォリオ10選｜こぎそ.md",
    ]
    
    base_dir = Path("/Users/yutaobayashi/Documents/MyObsidian")
    fixed_count = 0
    
    for file_path in error_files:
        full_path = base_dir / file_path
        if full_path.exists():
            if fix_file(full_path):
                print(f"Fixed: {file_path}")
                fixed_count += 1
            else:
                print(f"No changes needed or error: {file_path}")
        else:
            print(f"File not found: {file_path}")
    
    print(f"\nFixed {fixed_count} files")

if __name__ == "__main__":
    main()


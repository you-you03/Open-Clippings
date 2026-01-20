#!/usr/bin/env python3
"""
YAML形式エラーを修正するスクリプト（バッチ処理版）
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
        "02_Clippings/2_デザイン_UX/Refero â UI UX Design Inspiration for Your Next Project.md",
        "02_Clippings/3_プロダクト開発_AI活用_Cursor/【完全攻略】バイブコーディング入門！駆け出し開発者はこれを見て学ぼう！AI駆動開発のプロが徹底解説｜まさお@未経験からプロまでAI活用.md",
        "02_Clippings/3_プロダクト開発_AI活用_Cursor/【現時点のCursor全まとめ｜v1.4対応】2025年08月時点でのCursor 総復習するための完全チートシート.md",
        "02_Clippings/3_プロダクト開発_AI活用_Cursor/有名エンジニアの「AI課金事情」を大公開！ 最高額は月20万円！？【中島聡、松本勇気、牛尾剛、ちょくだい、ナル先生】 - エンジニアtype  転職type.md",
        "02_Clippings/3_プロダクト開発_AI活用_Cursor/金融機関の授業で使ったファイル.md",
        "02_Clippings/3_プロダクト開発_AI活用_Cursor/限界まで実務で AI Agent 「Cursor」を使ってみたら、アイアンマンの気分になれた。まるでジャービス｜minicoohei.md",
        "02_Clippings/3_プロダクト開発_AI活用_Dify/Dify講座 超入門.md",
        "02_Clippings/3_プロダクト開発_AI活用_Dify/NIKKEIリスキリングに掲載！Difyと対話するだけで業務プロセスを瞬時に設計する「BPR assistant」の技術解説について｜Collinear Inc.  コリニア株式会社.md",
        "02_Clippings/3_プロダクト開発_AI活用_Dify/令和トラベル Dify講座（社内イベント資料）.md",
        "02_Clippings/3_プロダクト開発_AI活用_Dify/週休7日も夢じゃない？AIクローン作成奮闘記｜ハヤカワ五味.md",
        "02_Clippings/3_プロダクト開発_AI活用_GPT/ChatGPT_usecase.md",
        "02_Clippings/3_プロダクト開発_AI活用_GPT/Gensparkの料金プランとできること.md",
        "02_Clippings/3_プロダクト開発_AI活用_GPT/PDFを高品質なマークダウンに変換する方法｜すぅ  AI駆動PM.md",
        "02_Clippings/3_プロダクト開発_AI活用_GPT/何が大企業のAI導入を失敗に導くのか【ゲスト：マスクド・アナライズ】.md",
        "02_Clippings/3_プロダクト開発_AI活用_プロンプト/\"まじん式プロンプト\"応用テクニック集｜まじん.md",
        "02_Clippings/3_プロダクト開発_AI活用_プロンプト/AI エージェント祭を開催しました.md",
        "02_Clippings/3_プロダクト開発_AI活用_プロンプト/Temporal Knowledge Graphで作る！時間変化するナレッジを扱うAI Agentの世界.md",
        "02_Clippings/3_プロダクト開発_AI活用_プロンプト/system_prompts_leaksclaude.txt at main · asgeirtjsystem_prompts_leaks.md",
        "02_Clippings/3_プロダクト開発_AI活用_プロンプト/【感動】 \"まじん式\" HTMLスライド生成プロンプトを試してほしい！｜まじん.md",
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


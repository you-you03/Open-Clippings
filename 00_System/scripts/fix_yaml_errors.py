#!/usr/bin/env python3
"""
YAML形式エラーを修正するスクリプト
タグの配列形式とリスト形式の混在を修正
"""
import re
import yaml
from pathlib import Path

def fix_tags_format(content: str) -> str:
    """タグの形式を修正"""
    # フロントマター部分を抽出
    if not content.startswith("---"):
        return content
    
    match = re.match(r"^(---\n)(.*?)(\n---\n)(.*)$", content, re.DOTALL)
    if not match:
        return content
    
    frontmatter_str = match.group(2)
    
    # タグの配列形式とリスト形式が混在しているパターンを検出
    lines = frontmatter_str.split('\n')
    new_lines = []
    tags_collected = []
    in_tags_section = False
    tags_line_idx = -1
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # tags: ["clippings", "生活"] のような配列形式を検出
        if re.match(r'^tags:\s*\[', line):
            in_tags_section = True
            tags_line_idx = len(new_lines)
            # 配列からタグを抽出
            match_tags = re.search(r'\[(.*?)\]', line)
            if match_tags:
                tags_str = match_tags.group(1)
                # クォートを除去してタグを抽出
                tags = [t.strip().strip('"').strip("'") for t in tags_str.split(',') if t.strip()]
                tags_collected.extend(tags)
            # この行は一旦スキップ（後で置き換える）
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
            in_tags_section = False
            tags_collected = []
            continue
        
        new_lines.append(line)
        i += 1
    
    # 新しいフロントマターを構築
    new_frontmatter = '\n'.join(new_lines)
    
    # YAML形式が正しいか確認
    try:
        yaml.safe_load(new_frontmatter)
    except yaml.YAMLError as e:
        # 修正に失敗した場合は元の内容を返す
        print(f"Warning: Failed to fix YAML: {e}")
        return content
    
    return f"---\n{new_frontmatter}\n---\n{match.group(4)}"

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
        "02_Clippings/1_コレクション_生活Tips/34年間太らなかった私が5キロ増量して気づいた「本当の美しさ」｜みなみやん@セルフケアの伝道師.md",
        "02_Clippings/1_コレクション_生活Tips/もう会社戻れません。在宅歴10年の僕が選んだ最強のリモート環境｜プロの引きこもり｜まつなが.md",
        "02_Clippings/1_コレクション_生活Tips/バカにしてごめん。MagSafe対応ハンディファンが最強でした.md",
        "02_Clippings/1_コレクション_生活Tips/何事も続かない人が習慣化する力を鍛えるには「行きつけの店を持つ」といい｜みなみやん@セルフケアの伝道師.md",
        "02_Clippings/1_コレクション_生活Tips/双子パパ、AIネイティブ育児に挑む。｜しょーてぃー.md",
        "02_Clippings/1_コレクション_興味_コーヒー/「サザコーヒー」流・地方発\"本物ブランド\"の育て方~タダコーヒーから６万円ゲイシャまで、体験階段でファンをつくる~｜黒澤 友貴.md",
        "02_Clippings/1_コレクション_興味_コーヒー/「サザコーヒー」流・地方発"本物ブランド"の育て方~タダコーヒーから６万円ゲイシャまで、体験階段でファンをつくる~｜黒澤 友貴.md",
        "02_Clippings/1_コレクション_興味_投資/資産1億円は「誰でも努力で到達できる」。養護施設出身の"資産36億円ニート"が明かす、奨学金返済からの富への道（週刊SPA!）.md",
        "02_Clippings/1_コレクション_興味_海外/リバプール、強さの裏側にあるのは？ 【サッカービジネス講義】｜Miki ⚽️ 海外×サッカー×ビジネス.md",
        "02_Clippings/1_コレクション_興味_海外/初ゴールの古橋亨梧現地メディアで高評価も4得点してもおかしくなかった-goalcom-日本.md",
        "02_Clippings/2_デザイン_UI_Figma/Config 2025のkeynoteまとめ、個人的な感想｜sakito.md",
        "02_Clippings/2_デザイン_UI_Figma/Courses – Figma Learn - Help Center.md",
        "02_Clippings/2_デザイン_UI_ノウハウTips/「大通り」の改修から、全社横断の課題解決まで　PdM×UIデザイナーで進めた「note」のグロースプロジェクト｜Goodpatch Blog グッドパッチブログ.md",
        "02_Clippings/2_デザイン_UX/Refero â UI UX Design Inspiration for Your Next Project.md",
        "02_Clippings/2_デザイン_ブランディング/noteのCDOになって3年たったので、あれこれ振り返ってみた｜宇野雄  note inc. CDO.md",
        "02_Clippings/3_プロダクト開発_AI活用_Cursor/Architecting Agent Memory Principles, Patterns, and Best Practices — Richmond Alake, MongoDB.md",
        "02_Clippings/3_プロダクト開発_AI活用_Cursor/Claude Code を初めて使う人向けの実践ガイド.md",
        "02_Clippings/3_プロダクト開発_AI活用_Cursor/Claude Code 逆引きコマンド事典.md",
        "02_Clippings/3_プロダクト開発_AI活用_Cursor/Coding Agents 101 The Art of Actually Getting Things Done.md",
        "02_Clippings/3_プロダクト開発_AI活用_Cursor/Geminiと音声会話をする方法！PC・スマホの設定や注意点まで｜SHIFT AI TIMES.md",
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
                print(f"No changes needed: {file_path}")
        else:
            print(f"File not found: {file_path}")
    
    print(f"\nFixed {fixed_count} files")

if __name__ == "__main__":
    main()


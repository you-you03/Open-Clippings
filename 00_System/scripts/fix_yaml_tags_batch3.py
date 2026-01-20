#!/usr/bin/env python3
"""
YAML形式エラーを修正するスクリプト（バッチ処理版3）
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
        "02_Clippings/5_ビジネス_経営_CEO/The Breakthrough Company GOを「三浦さんの会社」ではなくするためにした、いくつかの決断について。｜三浦崇宏.md",
        "02_Clippings/5_ビジネス_経営_CxO/プロダクトへAIを実装するでなく、組織へAIを実装することの重要性とマニュアル｜Takaya Shinozuka.md",
        "02_Clippings/5_ビジネス_経営_スタートアップ/Googleのような会社をつくりたい。ベイエリアで感じた、私たちが目指す未来｜鹿島幸裕 (note CFO).md",
        "02_Clippings/5_ビジネス_経営_スタートアップ/Product Behaviors and Rituals from The Lenny's Podcast.md",
        "02_Clippings/5_ビジネス_経営_スタートアップ/「１塁打」を狙う日本のVCに、存在価値はあるのだろうか？｜山田真央｜ダイニー.md",
        "02_Clippings/5_ビジネス_経営_スタートアップ/【& Supplyメンバーインタビュー代表井澤】働く仕組みを整えて、みんなが長く働ける飲食業界へ。｜& Supply.md",
        "02_Clippings/5_ビジネス_経営_スタートアップ/ジャングリア開業　山積みの課題と対策について（ヨッピー） - エキスパート.md",
        "02_Clippings/5_ビジネス_経営_スタートアップ/実は意外と大したことない。スタートアップの現実と数字（カミナシの場合）｜諸岡　裕人(カミナシCEO  SaaS).md",
        "02_Clippings/5_ビジネス_経営_ファイナンス/東京証券取引所プライム市場上場企業一覧 - Wikipedia.md",
        "02_Clippings/5_ビジネス_経営_戦略/両利きの経営とは？.md",
        "02_Clippings/5_ビジネス_経営_戦略/大きなビジョンを実現するための「10年ロードマップ」の作り方｜山田真央｜ダイニー.md",
        "02_Clippings/5_ビジネス_職種_PdM/プロダクトマネージャーのためのAIドキュメンテーションどれがいいの？を徹底調査.md",
        "02_Clippings/5_ビジネス_職種_マーケ_SNS運用/戦うマーケターに、\"推進剤\"と\"拠り所\"と\"地図\"を。 『マーケターキャリアパス ─10年後も活躍し続けるための成長戦略』｜勅使川原晃司.md",
        "02_Clippings/5_ビジネス_職種_マーケ_SNS運用/月間20万PVのオウンドメディア運営を「大幅改革」した理由｜junya koyama.md",
        "02_Clippings/5_ビジネス_職種_企業事例/日本の価値を上げる——NOT A HOTEL CONSULTINGを創業｜NOT A HOTEL inc..md",
        "02_Clippings/5_ビジネス_職種_企業事例/移動で日本の体験を変える──NOT A GARAGEが目指す姿｜NOT A HOTEL inc..md",
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


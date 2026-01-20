#!/usr/bin/env python3
"""
タグが存在しないファイルにタグを追加するスクリプト
"""
import re
import yaml
from pathlib import Path

def get_tags_for_file(filepath: Path, title: str, description: str = "") -> list:
    """ファイルの内容に基づいてタグを生成"""
    tags = []
    
    # ファイルパスからカテゴリを推測
    path_str = str(filepath)
    
    # コーヒー関連
    if "LIGHT UP COFFEE" in path_str or "コーヒー" in title or "コーヒー" in description:
        tags.append("コーヒー")
        if "バリスタ" in title or "ドリップ" in title or "淹れ" in title:
            tags.append("コーヒー淹れ方")
        elif "器具" in title:
            tags.append("コーヒー器具")
        elif "ネットショップ" in title or "ショップ" in title:
            tags.append("ビジネス")
        elif "発信" in title or "note" in title.lower():
            tags.append("コンテンツ")
        else:
            tags.append("ライフスタイル")
    
    # 書籍関連
    elif "書籍" in path_str or "Paper Books" in path_str:
        tags.append("書籍")
        tags.append("読書")
        if "TOEIC" in title:
            tags.append("英語")
            tags.append("toeic")
        elif "日本史" in title or "司馬" in title or "北条" in title:
            tags.append("歴史")
        elif "サッカー" in title:
            tags.append("サッカー")
        elif "速読" in title:
            tags.append("読書法")
        elif "事業" in title or "ビジネス" in title or "経営" in title:
            tags.append("ビジネス")
        elif "GRIT" in title or "やり抜く" in title:
            tags.append("自己啓発")
        else:
            tags.append("一般")
    
    # デフォルトタグ
    if not tags:
        tags.append("clippings")
    
    # 最大5個まで
    return tags[:5]

def fix_file(filepath: Path) -> bool:
    """1つのファイルを修正"""
    try:
        content = filepath.read_text(encoding="utf-8")
        if not content.startswith("---"):
            return False
        
        match = re.match(r"^(---\n)(.*?)(\n---\n)(.*)$", content, re.DOTALL)
        if not match:
            return False
        
        frontmatter_str = match.group(2)
        body = match.group(4)
        
        try:
            frontmatter = yaml.safe_load(frontmatter_str)
            if not frontmatter:
                return False
            
            # タグが存在しない、または空の場合
            if "tags" not in frontmatter or not frontmatter.get("tags") or len(frontmatter.get("tags", [])) == 0:
                title = frontmatter.get("title") or ""
                description = frontmatter.get("description") or ""
                new_tags = get_tags_for_file(filepath, title, description)
                
                frontmatter["tags"] = new_tags
                
                # YAMLを再生成（元の順序を保持）
                lines = frontmatter_str.split('\n')
                new_lines = []
                tags_added = False
                
                for line in lines:
                    if line.startswith('tags:'):
                        new_lines.append('tags:')
                        for tag in new_tags:
                            new_lines.append(f'  - "{tag}"')
                        tags_added = True
                    elif line.strip().startswith('-') and not tags_added:
                        # タグリストの行をスキップ
                        continue
                    else:
                        new_lines.append(line)
                
                # tagsが存在しない場合は最後に追加
                if not tags_added:
                    # imageの前に追加
                    image_idx = None
                    for i, line in enumerate(new_lines):
                        if line.startswith('image:'):
                            image_idx = i
                            break
                    
                    if image_idx is not None:
                        new_lines.insert(image_idx, 'tags:')
                        for tag in new_tags:
                            new_lines.insert(image_idx + 1, f'  - "{tag}"')
                    else:
                        new_lines.append('tags:')
                        for tag in new_tags:
                            new_lines.append(f'  - "{tag}"')
                
                new_frontmatter_str = '\n'.join(new_lines)
                new_content = f"---\n{new_frontmatter_str}\n---\n{body}"
                filepath.write_text(new_content, encoding="utf-8")
                return True
        except yaml.YAMLError:
            return False
        
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    """メイン処理"""
    clippings_dir = Path("02_Clippings")
    md_files = list(clippings_dir.rglob("*.md"))
    md_files = [f for f in md_files if "0_Index" not in str(f)]
    
    fixed_count = 0
    
    for filepath in sorted(md_files):
        if fix_file(filepath):
            fixed_count += 1
            print(f"Fixed: {filepath}")
    
    print(f"\nFixed {fixed_count} files")

if __name__ == "__main__":
    main()


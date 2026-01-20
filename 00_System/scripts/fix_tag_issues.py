#!/usr/bin/env python3
"""
タグの問題を修正するスクリプト
- タグにスペースが含まれている場合、ハイフンに置換
- タグが小文字ではない場合、小文字に変換（日本語は除く）
- タグが5個を超えている場合、最初の5個を残す
"""
import re
import yaml
from pathlib import Path
from typing import List

def normalize_tag(tag: str) -> str:
    """タグを正規化"""
    # スペースをハイフンに置換
    tag = tag.replace(" ", "-")
    
    # 英語タグを小文字に変換（日本語が含まれていない場合）
    if not re.search(r'[あ-ん]', tag):
        tag = tag.lower()
    
    return tag

def fix_tags(tags: List[str]) -> List[str]:
    """タグリストを修正"""
    if not tags:
        return tags
    
    # タグを正規化
    normalized_tags = [normalize_tag(tag) for tag in tags]
    
    # 重複を削除（順序を保持）
    seen = set()
    unique_tags = []
    for tag in normalized_tags:
        if tag not in seen:
            seen.add(tag)
            unique_tags.append(tag)
    
    # 5個を超える場合は最初の5個を残す
    if len(unique_tags) > 5:
        unique_tags = unique_tags[:5]
    
    return unique_tags

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
            if not frontmatter or "tags" not in frontmatter:
                return False
            
            original_tags = frontmatter["tags"]
            if not isinstance(original_tags, list):
                return False
            
            fixed_tags = fix_tags(original_tags)
            
            if original_tags != fixed_tags:
                frontmatter["tags"] = fixed_tags
                
                # YAMLを再生成
                new_frontmatter_str = yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False, sort_keys=False)
                # 末尾の改行を削除
                new_frontmatter_str = new_frontmatter_str.rstrip()
                
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
    error_count = 0
    
    for filepath in sorted(md_files):
        if fix_file(filepath):
            fixed_count += 1
            print(f"Fixed: {filepath}")
        else:
            error_count += 1
    
    print(f"\nFixed {fixed_count} files")
    print(f"Errors/Skipped: {error_count} files")

if __name__ == "__main__":
    main()


#!/usr/bin/env python3
"""
02_Clippings/内の全ファイルのYAMLフロントマターとタグ付けをチェックするスクリプト
"""
import os
import re
import yaml
from pathlib import Path
from typing import List, Dict, Tuple

# 禁止タグ（tag_rule.mdより）
FORBIDDEN_TAGS = {
    "todo", "routine", "daily-routine", "journal", "study", "exercise"
}

def parse_frontmatter(content: str) -> Tuple[Dict, str]:
    """YAMLフロントマターをパースする"""
    if not content.startswith("---"):
        return None, content
    
    # 最初の---から次の---までを抽出
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", content, re.DOTALL)
    if not match:
        return None, content
    
    frontmatter_str = match.group(1)
    body = match.group(2)
    
    try:
        frontmatter = yaml.safe_load(frontmatter_str)
        return frontmatter, body
    except yaml.YAMLError as e:
        return {"_error": str(e)}, body

def check_tags(tags: List[str], filepath: str) -> List[str]:
    """タグのルールをチェック"""
    issues = []
    
    if not tags:
        issues.append("タグが存在しません")
        return issues
    
    # タグの数チェック
    if len(tags) > 5:
        issues.append(f"タグが5個を超えています（{len(tags)}個）")
    
    # 各タグのチェック
    for tag in tags:
        tag_lower = tag.lower()
        
        # 禁止タグチェック
        if tag_lower in FORBIDDEN_TAGS:
            issues.append(f"禁止タグが含まれています: {tag}")
        
        # スペースチェック
        if " " in tag:
            issues.append(f"タグにスペースが含まれています: {tag}")
        
        # 大文字チェック（日本語以外で大文字が含まれている場合）
        if re.search(r'[A-Z]', tag) and not re.search(r'[あ-ん]', tag):
            issues.append(f"タグが小文字ではありません: {tag}")
    
    return issues

def check_file(filepath: Path) -> Dict:
    """1つのファイルをチェック"""
    result = {
        "file": str(filepath),
        "has_frontmatter": False,
        "frontmatter_valid": True,
        "frontmatter_error": None,
        "has_tags": False,
        "tag_issues": [],
        "missing_fields": []
    }
    
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception as e:
        result["frontmatter_error"] = f"ファイル読み込みエラー: {str(e)}"
        return result
    
    frontmatter, _ = parse_frontmatter(content)
    
    if frontmatter is None:
        result["missing_fields"].append("YAMLフロントマターが存在しません")
        return result
    
    result["has_frontmatter"] = True
    
    if "_error" in frontmatter:
        result["frontmatter_valid"] = False
        result["frontmatter_error"] = frontmatter["_error"]
        return result
    
    # 必須フィールドチェック
    required_fields = ["title", "source"]
    for field in required_fields:
        if field not in frontmatter:
            result["missing_fields"].append(f"必須フィールド '{field}' がありません")
    
    # タグチェック
    if "tags" in frontmatter:
        result["has_tags"] = True
        tags = frontmatter["tags"]
        if isinstance(tags, list):
            result["tag_issues"] = check_tags(tags, str(filepath))
        elif isinstance(tags, str):
            # 文字列の場合は配列に変換してチェック
            result["tag_issues"] = check_tags([tags], str(filepath))
        else:
            result["tag_issues"].append("タグの形式が不正です（配列または文字列である必要があります）")
    else:
        result["tag_issues"].append("タグフィールドが存在しません")
    
    return result

def main():
    """メイン処理"""
    clippings_dir = Path("/Users/yutaobayashi/Documents/MyObsidian/02_Clippings")
    
    if not clippings_dir.exists():
        print(f"エラー: {clippings_dir} が見つかりません")
        return
    
    # 0_Indexディレクトリは除外
    md_files = list(clippings_dir.rglob("*.md"))
    md_files = [f for f in md_files if "0_Index" not in str(f)]
    
    print(f"チェック対象ファイル数: {len(md_files)}")
    print("=" * 80)
    
    issues = []
    no_frontmatter = []
    invalid_yaml = []
    tag_problems = []
    missing_tags = []
    
    for filepath in sorted(md_files):
        result = check_file(filepath)
        
        if not result["has_frontmatter"]:
            no_frontmatter.append(result)
        elif not result["frontmatter_valid"]:
            invalid_yaml.append(result)
        elif not result["has_tags"] or result["tag_issues"]:
            if not result["has_tags"]:
                missing_tags.append(result)
            if result["tag_issues"]:
                tag_problems.append(result)
        
        if result["missing_fields"] or result["tag_issues"] or not result["has_frontmatter"] or not result["frontmatter_valid"]:
            issues.append(result)
    
    # 結果を表示
    print(f"\n【結果サマリー】")
    print(f"総ファイル数: {len(md_files)}")
    print(f"問題があるファイル: {len(issues)}")
    print(f"  - YAMLフロントマターなし: {len(no_frontmatter)}")
    print(f"  - YAML形式エラー: {len(invalid_yaml)}")
    print(f"  - タグなし: {len(missing_tags)}")
    print(f"  - タグの問題: {len(tag_problems)}")
    
    # 詳細表示
    if no_frontmatter:
        print(f"\n【YAMLフロントマターがないファイル ({len(no_frontmatter)}件)】")
        for result in no_frontmatter[:10]:  # 最初の10件のみ表示
            print(f"  - {result['file']}")
        if len(no_frontmatter) > 10:
            print(f"  ... 他 {len(no_frontmatter) - 10} 件")
    
    if invalid_yaml:
        print(f"\n【YAML形式エラー ({len(invalid_yaml)}件)】")
        for result in invalid_yaml[:10]:
            print(f"  - {result['file']}")
            print(f"    エラー: {result['frontmatter_error']}")
        if len(invalid_yaml) > 10:
            print(f"  ... 他 {len(invalid_yaml) - 10} 件")
    
    if missing_tags:
        print(f"\n【タグがないファイル ({len(missing_tags)}件)】")
        for result in missing_tags[:10]:
            print(f"  - {result['file']}")
        if len(missing_tags) > 10:
            print(f"  ... 他 {len(missing_tags) - 10} 件")
    
    if tag_problems:
        print(f"\n【タグに問題があるファイル ({len(tag_problems)}件)】")
        for result in tag_problems[:20]:  # 最初の20件のみ表示
            print(f"  - {result['file']}")
            for issue in result['tag_issues']:
                print(f"    → {issue}")
        if len(tag_problems) > 20:
            print(f"  ... 他 {len(tag_problems) - 20} 件")
    
    # 結果をファイルに保存
    report_file = clippings_dir / "0_Index" / "tag_check_report.md"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write("# タグ付けチェックレポート\n\n")
        f.write(f"チェック日時: {Path(__file__).stat().st_mtime}\n\n")
        f.write(f"総ファイル数: {len(md_files)}\n")
        f.write(f"問題があるファイル: {len(issues)}\n\n")
        
        if no_frontmatter:
            f.write(f"## YAMLフロントマターがないファイル ({len(no_frontmatter)}件)\n\n")
            for result in no_frontmatter:
                f.write(f"- {result['file']}\n")
            f.write("\n")
        
        if invalid_yaml:
            f.write(f"## YAML形式エラー ({len(invalid_yaml)}件)\n\n")
            for result in invalid_yaml:
                f.write(f"- {result['file']}\n")
                f.write(f"  - エラー: {result['frontmatter_error']}\n")
            f.write("\n")
        
        if missing_tags:
            f.write(f"## タグがないファイル ({len(missing_tags)}件)\n\n")
            for result in missing_tags:
                f.write(f"- {result['file']}\n")
            f.write("\n")
        
        if tag_problems:
            f.write(f"## タグに問題があるファイル ({len(tag_problems)}件)\n\n")
            for result in tag_problems:
                f.write(f"- {result['file']}\n")
                for issue in result['tag_issues']:
                    f.write(f"  - {issue}\n")
            f.write("\n")
    
    print(f"\n詳細レポートを保存しました: {report_file}")

if __name__ == "__main__":
    main()


import os
import re
import json
import yaml
import requests
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple, Union

NOTION_API = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"

# Notion DB property names (あなたのDBに合わせて固定)
PROP_TITLE = "Name"
PROP_STATUS = "Status"
PROP_DO = "Do"
PROP_DUE = "Due"
PROP_FLAG = "Flag"
PROP_TAGS_REL = "Tags_DB"
PROP_PROJECTS_REL = "Projects_DB"

UUID_RE = re.compile(r"^[0-9a-fA-F-]{32,36}$")


def notion_headers(token: str) -> Dict[str, str]:
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def notion_get(token: str, path: str) -> Dict[str, Any]:
    r = requests.get(f"{NOTION_API}{path}", headers=notion_headers(token), timeout=30)
    r.raise_for_status()
    return r.json()


def notion_post(token: str, path: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    r = requests.post(
        f"{NOTION_API}{path}",
        headers=notion_headers(token),
        data=json.dumps(payload),
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def read_task_file(path: str) -> Union[List[Dict[str, Any]], Dict[str, Any], None]:
    """
    Supports:
      - YAML file: tasks/*.yml, tasks/*.yaml
        - dict形式: 1タスクとして扱う
        - list形式: 複数タスクとして扱う
        - {"tasks": [...]} 形式: tasksキーの配列を返す
      - Markdown with YAML frontmatter: tasks/*.md
    Returns:
      - List[Dict]: 複数タスク（list形式またはtasksキーで包まれた形式）
      - Dict: 1タスク（dict形式）
      - None: 読み込み失敗
    """
    if not os.path.exists(path):
        return None

    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()

    ext = os.path.splitext(path)[1].lower()
    if ext in [".yml", ".yaml"]:
        data = yaml.safe_load(raw)
        if data is None:
            return None
        
        # {"tasks": [...]} 形式の場合
        if isinstance(data, dict) and "tasks" in data:
            tasks = data["tasks"]
            if isinstance(tasks, list):
                return tasks
            # tasksがdictの場合は1要素のlistとして扱う
            if isinstance(tasks, dict):
                return [tasks]
        
        # list形式の場合
        if isinstance(data, list):
            return data
        
        # dict形式の場合（1タスク）
        if isinstance(data, dict):
            return data
        
        raise ValueError(f"Invalid YAML structure (dict/list/tasks key expected): {path}")

    if ext == ".md":
        # frontmatter parser
        if raw.startswith("---"):
            parts = raw.split("---", 2)
            if len(parts) >= 3:
                fm = parts[1]
                data = yaml.safe_load(fm)
                if data is None:
                    return None
                
                # {"tasks": [...]} 形式の場合
                if isinstance(data, dict) and "tasks" in data:
                    tasks = data["tasks"]
                    if isinstance(tasks, list):
                        return tasks
                    if isinstance(tasks, dict):
                        return [tasks]
                
                # list形式の場合
                if isinstance(data, list):
                    return data
                
                # dict形式の場合（1タスク）
                if isinstance(data, dict):
                    return data
                
                raise ValueError(f"Invalid frontmatter structure: {path}")
        return None

    return None


def normalize_date(v: Any) -> Optional[str]:
    """
    Accepts YYYY-MM-DD or ISO datetime; returns YYYY-MM-DD.
    """
    if v is None:
        return None
    if isinstance(v, str):
        s = v.strip()
        if not s:
            return None
        # YYYY-MM-DD
        if re.match(r"^\d{4}-\d{2}-\d{2}$", s):
            return s
        # ISO datetime -> date
        try:
            dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
            return dt.date().isoformat()
        except Exception:
            raise ValueError(f"Invalid date format: {v}")
    raise ValueError(f"Invalid date type: {type(v)}")


def is_uuid_like(s: str) -> bool:
    return bool(UUID_RE.match(s.strip()))


def notion_query_db(token: str, db_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    return notion_post(token, f"/databases/{db_id}/query", payload)


def get_relation_target_db_id(db_schema: Dict[str, Any], prop_name: str) -> Optional[str]:
    props = db_schema.get("properties", {})
    p = props.get(prop_name)
    if not p:
        return None
    if p.get("type") != "relation":
        return None
    rel = p.get("relation", {})
    # Notion returns {"database_id": "...", ...}
    return rel.get("database_id")


def find_page_id_by_title(token: str, db_id: str, title: str) -> Optional[str]:
    """
    Finds a page in a DB whose title equals `title`.
    Assumes the DB has a title property (any name); Notion API filter requires property name,
    so we first detect the title property name by reading db schema.
    """
    schema = notion_get(token, f"/databases/{db_id}")
    title_prop_name = None
    for name, p in schema.get("properties", {}).items():
        if p.get("type") == "title":
            title_prop_name = name
            break
    if not title_prop_name:
        raise RuntimeError(f"Cannot find title property in DB: {db_id}")

    q = {
        "page_size": 10,
        "filter": {
            "property": title_prop_name,
            "title": {"equals": title},
        },
    }
    res = notion_query_db(token, db_id, q)
    results = res.get("results", [])
    if not results:
        return None
    return results[0]["id"]


def coerce_relation_ids(
    token: str,
    rel_db_id: Optional[str],
    value: Union[str, List[str], None],
    field_label: str,
) -> List[str]:
    if value is None:
        return []
    items = value if isinstance(value, list) else [value]
    out: List[str] = []
    for it in items:
        if not isinstance(it, str) or not it.strip():
            continue
        s = it.strip()
        if is_uuid_like(s):
            out.append(s)
            continue
        if not rel_db_id:
            raise RuntimeError(f"{field_label}: relation DB id not available; cannot resolve name '{s}'")
        pid = find_page_id_by_title(token, rel_db_id, s)
        if not pid:
            raise RuntimeError(f"{field_label}: cannot find page titled '{s}' in relation DB")
        out.append(pid)
    return out


def build_properties_payload(
    token: str,
    tasks_db_schema: Dict[str, Any],
    task: Dict[str, Any],
) -> Dict[str, Any]:
    title = (task.get("title") or task.get("name") or "").strip()
    if not title:
        raise ValueError("Missing required field: title")

    status = task.get("status")
    do = normalize_date(task.get("do"))
    due = normalize_date(task.get("due"))
    flag = task.get("flag")
    tags = task.get("tags")
    project = task.get("project") or task.get("projects")

    # relation db ids derived from tasks db schema
    tags_db_id = get_relation_target_db_id(tasks_db_schema, PROP_TAGS_REL)
    projects_db_id = get_relation_target_db_id(tasks_db_schema, PROP_PROJECTS_REL)

    tag_ids = coerce_relation_ids(token, tags_db_id, tags, "tags")
    project_ids = coerce_relation_ids(token, projects_db_id, project, "project")

    props: Dict[str, Any] = {}

    # Title
    props[PROP_TITLE] = {"title": [{"text": {"content": title}}]}

    # Status (optional)
    if status:
        props[PROP_STATUS] = {"status": {"name": str(status)}}

    # Dates
    if do:
        props[PROP_DO] = {"date": {"start": do}}
    if due:
        props[PROP_DUE] = {"date": {"start": due}}

    # Flag (Select single)
    if flag:
        props[PROP_FLAG] = {"select": {"name": str(flag)}}

    # Relations
    if tag_ids:
        props[PROP_TAGS_REL] = {"relation": [{"id": x} for x in tag_ids]}
    if project_ids:
        props[PROP_PROJECTS_REL] = {"relation": [{"id": x} for x in project_ids]}

    return props


def exists_similar_task(
    token: str,
    tasks_db_id: str,
    title: str,
    do: Optional[str],
    due: Optional[str],
) -> bool:
    """
    Dedupe policy (追加のみ運用向け):
      - Name == title AND Due == due AND Do == do が一致するものがあれば作らない
    Dateが未指定の場合はその条件を外して照合する（厳密性より二重登録回避優先）。
    """
    filters = [{"property": PROP_TITLE, "title": {"equals": title}}]

    if due:
        filters.append({"property": PROP_DUE, "date": {"equals": due}})
    if do:
        filters.append({"property": PROP_DO, "date": {"equals": do}})

    q = {"page_size": 1, "filter": {"and": filters}}
    res = notion_query_db(token, tasks_db_id, q)
    return len(res.get("results", [])) > 0


def main() -> None:
    token = os.environ.get("NOTION_TOKEN", "").strip()
    tasks_db_id = os.environ.get("NOTION_TASKS_DB_ID", "").strip()
    changed = os.environ.get("CHANGED_FILES", "").strip()

    if not token:
        raise RuntimeError("NOTION_TOKEN is missing")
    if not tasks_db_id:
        raise RuntimeError("NOTION_TASKS_DB_ID is missing")
    if not changed:
        print("No changed files. Exit.")
        return

    repo = os.environ.get("GITHUB_REPO", "")
    sha = os.environ.get("GITHUB_SHA", "")
    ref = os.environ.get("GITHUB_REF", "")

    # Read tasks DB schema once
    tasks_db_schema = notion_get(token, f"/databases/{tasks_db_id}")

    files = [f for f in changed.split(" ") if f.strip()]
    # only YAML / MD
    files = [f for f in files if os.path.splitext(f)[1].lower() in [".yml", ".yaml", ".md"]]

    if not files:
        print("No task files to process. Exit.")
        return

    created = 0
    skipped = 0

    for path in files:
        tasks_data = read_task_file(path)
        if tasks_data is None:
            skipped += 1
            print(f"[SKIP] Not a task file or no frontmatter: {path}")
            continue

        # list形式の場合は各要素を処理、dict形式の場合は1要素のlistとして扱う
        tasks_list: List[Dict[str, Any]]
        if isinstance(tasks_data, list):
            tasks_list = tasks_data
        elif isinstance(tasks_data, dict):
            tasks_list = [tasks_data]
        else:
            skipped += 1
            print(f"[SKIP] Invalid task data structure: {path}")
            continue

        # 各タスクを処理
        for idx, task in enumerate(tasks_list):
            if not isinstance(task, dict):
                skipped += 1
                print(f"[SKIP] Task at index {idx} is not a dict: {path}")
                continue

            title = (task.get("title") or task.get("name") or "").strip()
            if not title:
                skipped += 1
                print(f"[SKIP] Task at index {idx} has no title: {path}")
                continue

            do = normalize_date(task.get("do"))
            due = normalize_date(task.get("due"))
            
            # task_keyがあれば重複判定に使用（オプション）
            task_key = task.get("task_key")
            if task_key:
                # task_keyによる重複判定は将来的に実装可能
                # 現時点では title/do/due による判定を使用
                pass

            # dedupe
            if exists_similar_task(token, tasks_db_id, title, do, due):
                skipped += 1
                print(f"[SKIP] Duplicate (by Name/Do/Due): {path}[{idx}] -> {title}")
                continue

            props = build_properties_payload(token, tasks_db_schema, task)

            payload = {
                "parent": {"database_id": tasks_db_id},
                "properties": props,
            }

            # メタ情報をNotion側に残したい場合は、DBにTextプロパティを増設してここで設定（任意）
            # 例: "SourceRepo", "SourceSha", "SourcePath"
            # 現時点ではDBに存在しない前提なので未設定。

            res = notion_post(token, "/pages", payload)
            created += 1
            print(f"[OK] Created: {title} (page_id={res.get('id')}) from {path}[{idx}]")

    print(f"Done. created={created}, skipped={skipped}, repo={repo}, ref={ref}, sha={sha}")


if __name__ == "__main__":
    main()

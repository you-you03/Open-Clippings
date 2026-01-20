---
title: "AIエンジニアリング入門：Pythonによる開発の基礎（uv, Ruff, dataclass, Pyright, Git hooks）"
source: "https://zenn.dev/dalab/articles/61f06f6b516f4e"
author:
  - "[[Zenn]]"
published: 2025-09-06
created: 2025-09-11
description:
tags: [クリッピング, python, 開発, aiエンジニアリング, プログラミング]
image: "https://res.cloudinary.com/zenn/image/upload/s--5WiHURfQ--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:AI%25E3%2582%25A8%25E3%2583%25B3%25E3%2582%25B8%25E3%2583%258B%25E3%2582%25A2%25E3%2583%25AA%25E3%2583%25B3%25E3%2582%25B0%25E5%2585%25A5%25E9%2596%2580%25EF%25BC%259APython%25E3%2581%25AB%25E3%2582%2588%25E3%2582%258B%25E9%2596%258B%25E7%2599%25BA%25E3%2581%25AE%25E5%259F%25BA%25E7%25A4%258E%25EF%25BC%2588uv%252C%2520Ruff%252C%2520dataclass%252C%2520Pyright%252C...%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_34:Tomoya%2520Miyazawa%2Cx_220%2Cy_108/bo_3px_solid_rgb:d6e3ed%2Cg_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL3plbm4tdXNlci11cGxvYWQvYXZhdGFyL2Y4MmEwNzVhNjAuanBlZw==%2Cr_20%2Cw_90%2Cx_92%2Cy_102/co_rgb:6e7b85%2Cg_south_west%2Cl_text:notosansjp-medium.otf_30:DAL%2520Tech%2520Blog%2Cx_220%2Cy_160/bo_4px_solid_white%2Cg_south_west%2Ch_50%2Cl_fetch:aHR0cHM6Ly9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL3plbm4tdXNlci11cGxvYWQvYXZhdGFyL2UzZDAyYjUwODguanBlZw==%2Cr_max%2Cw_50%2Cx_139%2Cy_84/v1627283836/default/og-base-w1200-v2.png"
---
191

110[tech](https://zenn.dev/tech-or-idea)

## はじめに

データソリューション事業部の宮澤です。

近年、多くの企業においてDXの推進とともにデータ活用が進んでいます。それに伴って機械学習モデルもPoCからさらに進んで、システムに組み込んで実運用へと進むケースが増えているように感じます。このことを踏まえると、これから必要になるのはデータを分析して示唆を得るスキルはもちろんですが、それに加えて機械学習モデルを社会実装するエンジニアリングスキルがより求められるのではないかと考えます。ここではそのスキルを「AIエンジニアリングスキル」と呼び、本シリーズの記事はデータサイエンティストがこのスキルを身につけるための学習過程をアウトプットしたものと位置付けます。したがって本記事の対象読者は「これからAIエンジニアリングスキルを身につけたい技術者」とします。

今回は「 **Pythonによる開発の基礎（プロジェクト管理・コード品質）** 」と題して、Pythonを用いた開発を進めるにあたって、どのようにプロジェクトやパッケージを管理するとよいか、どのようにコード品質を保つとよいかといったプラクティスについて記載します。

## AIエンジニアリング入門シリーズ

※今後増やしていければと思います。

- 開発の基礎
	- Pythonによる開発の基礎（uv, Ruff, dataclass, Pyright, Git hooks）　※本記事

## Pythonのプロジェクト管理

## uvでプロジェクトを管理する

Pythonでの開発環境を整備するにあたっては「pyenvでPythonのバージョン管理をする」「venvで仮想環境を作成する」「poetryでパッケージ管理をする」といった方法があるかと思いますが、最近では **uv** というツールで代替する方法が増えている印象です。uvはPythonのパッケージとプロジェクトを管理するためのツールです。

uvは、上記のツールで別々に管理していた部分を **uvのみで完結することができる** という特長があります。

> A single tool to replace `pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, `twine`, `virtualenv`, and more.

また、Rustという言語で書かれており、 **他のツールと比較して非常に高速な処理を実現している** という特長もあります。

![](https://storage.googleapis.com/zenn-user-upload/4089c756503f-20250906.png)  
*[https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)*

## uvの使い方

ここからはドキュメントにしたがって実際にuvを使っていきます。

### uvのインストール

まずはuvをインストールします。

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

私はMacOSを使用しているため以下のコマンドでインストールしました。

```
brew install uv
```

### プロジェクト作成

まずはプロジェクトを作成します。

```
# 既存のディレクトリに作る場合
uv init

# ディレクトリを作成する場合
uv init project-name
```

上記コマンドを実行すると以下のようなファイルが作成されます。

```
project-name
├──.gitignore
├──.python-version
├──main.py
├──pyproject.toml
└──README.md
```

`pyproject.toml` はプロジェクトのメタデータを管理するためのもので、以下のように書かれています。

```
[project]
name = "project-name"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.13"
dependencies = []
```

### Pythonバージョン管理

ドキュメントの記載とは順番が前後しますが、ここでPythonのバージョンを変更します。  
uvでは複数のPythonのバージョンをインストールして、素早く切り替えることが可能です。

```
uv python install 3.10 3.11 3.12
```

実行すると以下のように返ってきました。正常にインストールができたようです。

```
+ cpython-3.10.18-macos-aarch64-none (python3.10)
+ cpython-3.11.13-macos-aarch64-none (python3.11)
+ cpython-3.12.9-macos-aarch64-none (python3.12)
```

次にプロジェクトのPythonバージョンを3.11に変更します。

```
uv python pin 3.11
```

実行してみるとエラーが発生しました。

```
error: The requested Python version \`3.11\` is incompatible with the project \`requires-python\` value of \`>=3.13\`.
```

エラーを解消するためには `pyproject.toml` を編集する必要があります。

```
[project]
name = "python-dev"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11" # 3.13を3.11に変更
dependencies = []
```

再度コマンドを実行すると、エラーが解消されました。

```
Updated \`.python-version\` from \`3.13\` -> \`3.11\`
```

`.python-version` を確認すると、3.13から3.11に自動で変更されていました。

### 仮想環境の作成

uvでは仮想環境を作成する機能があります。以下のコマンドで仮想環境を作成します。

```
uv venv

# 任意の名称をつける場合
uv venv env-name
```

Pythonのバージョンを指定して作成することもできます。

```
uv venv --python 3.12
```

### パッケージ管理

作成した仮想環境をアクティブにしてからパッケージをインストールしてみます。

```
# 仮想環境をアクティベート
source .venv/bin/activate
```

パッケージをインストールする方法は2つあります。

- `uv pip install package`
- `uv add package`

`uv pip install` はpip互換であるため普通に `pip install` をするのと同じように使うことができますが、個別にパッケージをインストールするため、パッケージ管理の観点からはあまり優れているとは言えません。一方で `uv add` は `pyproject.toml` に依存関係を自動的に記録するため、パッケージ管理の観点からは `uv add` を使うことが推奨されると思われます。

実際にパッケージをインストールしてみます。

```
uv add pandas numpy
```

`pyproject.toml` を確認すると、以下のように `dependencies` にインストールしたパッケージが追記されていました。

```
[project]
name = "python-dev"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    **"numpy>=2.3.2",
    "pandas>=2.3.1"**,
]
```

また、ファイルとして `uv.lock` が追加されていました。こちらはパッケージに関する正確で詳細な情報が記載されています。こちらは手動で編集しないことがドキュメントで指示されています。

uv addには、 `—dev` 、 `—group` などのオプションがあります。

`—dev` は開発依存関係を定義するためのものであり、このコマンドでインストールされたパッケージは、開発したライブラリがPyPIを公開する際に公開対象に含まれません。したがって、本番環境ではなく開発環境で必要なパッケージを管理するために使うといった棲み分けに使うことができます。

```
uv add --dev pytest
```

コマンドを実行すると以下のように追加されます。

```
[project]
name = "python-dev"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "numpy>=2.3.2",
    "pandas>=2.3.1",
]

[dependency-groups]
dev = [
    "pytest>=8.4.1",
]
```

`—group` は開発依存関係をさらに複数のグループに分けることができる機能です。

```
uv add --group lint ruff
```

`dev` グループに `pytest` が、 `lint` グループに `ruff` が割り当てられていることがわかります。

```
[project]
name = "python-dev"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "numpy>=2.3.2",
    "pandas>=2.3.1",
]

[dependency-groups]
dev = [
    "pytest>=8.4.1",
]
lint = [
    "ruff>=0.12.5",
]
```

パッケージの削除は以下のコマンドで実行できます。

```
uv remove numpy
```

### パッケージ同期

`pyproject.toml` を使うことで別のプロジェクトにパッケージを同期させて環境構築ができます。  
以下のコマンドを実行すると、仮想環境を作り、 `pyproject.toml` に記載されているパッケージをインストールしてくれます。

```
uv sync
```

[ドキュメント](https://docs.astral.sh/uv/concepts/projects/sync/) を読んだところ `uv.lock` があれば同期できるのかと思ったのですが、 `uv.lock` だけを別プロジェクトに持ってきて `uv sync` を実行してみると”could not find root”というエラーが出てしまい、うまくいきませんでした。 `pyproject.toml` を持ってきて `uv sync` を実行したところエラーなく同期されました。 `pyproject.toml` と `uv.lock` で齟齬があるとエラーにつながるようです。（ [Issue #6386](https://github.com/astral-sh/uv/issues/6386) ）

### プログラム実行

最後に、Pythonで記述した.pyファイルをuv環境で実行してみます。  
`uv init` でプロジェクトを作った際にmain.pyが作られていたため、こちらを実行します。

```python
# main.py
def main():
    print("Hello from python-dev!")

if __name__ == "__main__":
    main()
```

`uv run` で実行できます。

```
uv run main.py
```

以下のようにエラーなく実行されたことが確認できました。

```
Hello from python-dev!
```

## Pythonのコード品質管理

## コードのスタイルガイド

よいPythonコードとは何でしょうか？  
その答えは人や組織によって異なると思いますが、ここではその一つの答えとして、PEP20を紹介します。PEPとは、Pythonの言語使用や開発プロセスに関する提案や改善案を記述した文書のことです。Pythonコミュニティーの議論の中で作られています。

PEP20はTim PetersがPythonの設計思想をまとめたもので、Zen of Pythonと呼ばれます。

より具体的なコードのスタイルガイドはPEP8で文書化されています。

本文書にはコードレイアウト、命名規則、プログラミングの推奨事項など様々なガイドラインが書かれています。PEP8にも”sometimes style guide recommendations just aren’t applicable.”と記載があるように、よいコードの定義は組織や場合によって異なると考えられますが、もし既存プログラムの改修ではなくこれから開発をスタートするといった場合には、こちらのスタイルガイドを参考に組織内で共通の認識を持ってコーディングを進めていくのは一つのベタープラクティスであると考えられます。

## Ruffでコードの静的解析とフォーマットを行う

実際にコードチェックをするには人手では限界があるため、フォーマッターやリンターのツールを用います。最近よく使われているツールとしては **Ruff** が挙げられるかと思います。Ruffはuvと同じくAstral社が開発したツールで、こちらも様々なツールで出来ていたことを一つに統合したこと、処理が高速であることを特長としています。

## Ruffの使い方

先ほど作成したuvの仮想環境を使います。  
再掲ですが、Ruffをインストールするコマンドは以下です。

```
uv add ruff

# 開発依存環境なら
uv add --dev ruff

# 開発依存環境でグループ分けするなら
uv add --group groupname ruff
```

プロジェクトのディレクトリに `ruff-check.py` という名称で以下のファイルを作成します。これをコードチェックの対象とします。

```python
from typing import Iterable

import os

print('Hello from python-dev!')

def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Given an iterable of integers, return the sum of all even numbers in the iterable."""
    return sum(
        num for num in numbers
        if num % 2 == 0
    )
```

### Formatter

まずはFormatter（コード整形）としての機能を使ってみます。以下のコマンドでコードのフォーマットををチェックすることができます。また、 `—diff` をつけることで `git diff` のように差分を確認できます。

```
uv run ruff format --diff
```

上のコマンドを実行すると、以下のように返ってきました。

```
--- ruff-check.py
+++ ruff-check.py
@@ -2,11 +2,9 @@
 
 import os
 
-print('Hello from python-dev!')
+print("Hello from python-dev!")
+
 
 def sum_even_numbers(numbers: Iterable[int]) -> int:
     """Given an iterable of integers, return the sum of all even numbers in the iterable."""
-    return sum(
-        num for num in numbers
-        if num % 2 == 0
-    )
\ No newline at end of file
+    return sum(num for num in numbers if num % 2 == 0)
```

指摘されているのは2点のようです。

1. **printに与えている文字列のシングルクォーテーションをダブルクォーテーションにする。**
2. **sum\_even\_numbers関数のreturn部分を改行なしの一行にする。**

ではこれを修正してみます。

```
uv run ruff format
```

上のコマンドを実行すると、ファイルが自動で修正されました。

```python
from typing import Iterable

import os

print("Hello from python-dev!")

def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Given an iterable of integers, return the sum of all even numbers in the iterable."""
    return sum(num for num in numbers if num % 2 == 0)
```

### Linter

次にLinter（コード解析）としての機能を使ってみます。同じく `—diff` で差分を確認します。ファイルは上記の整型後のものを使います。

```
uv run ruff check --diff
```

以下のように返ってきました。

```
--- ruff-check.py
+++ ruff-check.py
@@ -1,6 +1,5 @@
 from typing import Iterable
 
-import os
 
 print("Hello from python-dev!")
 

Would fix 1 error.
```

ここで指摘されているのは、「 `import os` が不要」ということのようです。理由としてはコードの中で `os` を使っていないためです。

こちらも同じく修正します。今度は `—fix` をつけます。

```
uv run ruff check --fix
```

“os imported but unused”という理由とともに修正したというメッセージが返ってきました。

```
ruff-check.py:3:8: F401 [*] \`os\` imported but unused
  |
1 | from typing import Iterable
2 |
3 | import os
  |        ^^ F401
4 |
5 | print("Hello from python-dev!")
  |
  = help: Remove unused import: \`os\`

Found 1 error.
[*] 1 fixable with the \`--fix\` option.
```

ファイルを見てみると、 `import os` が消されていることがわかります。

```python
from typing import Iterable

print("Hello from python-dev!")

def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Given an iterable of integers, return the sum of all even numbers in the iterable."""
    return sum(num for num in numbers if num % 2 == 0)
```

返ってきたメッセージをよくみると、”F401”と書いてあります。これはFlake8というPythonのコードチェックツールで定義されるエラーコードの一つで、F401はインポートしたモジュールや名前がコード中で使われていないことを示しています。Ruffのデフォルトの設定ではこの項目がチェック対象に含まれているようです。

では、チェック対象を変えてみます。uv環境の場合はpyproject.tomlにruffのルールを設定することができます。デフォルトは以下の設定になっています。

これをそのまま `pyproject.toml` に転記したのち、lintの設定から以下のように”F”を除外してみます。  
チェック対象のファイルにも `import os` を書き戻しておきます。

```
[tool.ruff.lint]
# Enable Pyflakes (\`F\`) and a subset of the pycodestyle (\`E\`) codes by default.
# Unlike Flake8, Ruff doesn't enable pycodestyle warnings (\`W\`) or
# McCabe complexity (\`C901\`) by default.
- select = ["E4", "E7", "E9", "F"]
+ select = ["E4", "E7", "E9"]
ignore = []
```

この設定で先ほどと同じようにチェックと修正を実行してみます。

```
uv run ruff check
```

以下のように返ってきました。全てのチェックをパスしたため、不要であるはずの `import os` は修正されなかったことを示しています。

```
All checks passed!
```

この結果から、 `pyproject.toml` に設定したRuffのルールが正しく適用されていることがわかりました。  
Pythonでの開発においては、このようなFormatterとLinterの機能をどこまで使うか、プロジェクトごとに適切な設定をすることが推奨されます。

## VS CodeでのRuffの使い方

次にVS Codeの拡張機能でRuffを利用する方法を試みます。  
拡張機能を検索してインストールします。  
![](https://storage.googleapis.com/zenn-user-upload/602552516d2c-20250906.png)

インストールができたので設定を調べていきます。VS CodeのRuff拡張機能のGitHubリポジトリがあるため、こちらを参考に設定を進めていきます。

READMEにしたがって、VS Codeの `settings.json` に以下を追記しました。  
Pythonファイルの保存時にFormatterとLinterが走り、修正が適用されるように書かれています。（詳細はREADMEをご確認ください。）

```json
"[python]": {
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.fixAll": "explicit",
            "source.organizeImports": "explicit"
        },
        "editor.defaultFormatter": "charliermarsh.ruff"
  }
```

Ruffの実行を確かめるために、 `ruff-check.py` を以下の状態に戻します。  
不要な `import os` があり、文字列の囲いがシングルクォーテーションになっています。

```python
from typing import Iterable

import os

print('Hello from python-dev!')

def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Given an iterable of integers, return the sum of all even numbers in the iterable."""
    return sum(num for num in numbers if num % 2 == 0)
```

この状態でファイルを保存すると、以下のように自動修正されて保存されました。

```python
from typing import Iterable

print("Hello from python-dev!")

def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Given an iterable of integers, return the sum of all even numbers in the iterable."""
    return sum(num for num in numbers if num % 2 == 0)
```

こちらも同様に `settings.json` に `"ruff.lint.select": ["C", "E", "F", "W"]` のように書くことで様々なRuffの設定ができるようですが、本記事では割愛して、ここまででVS CodeでのRuffの挙動確認を完了とします。

## Pythonの型付け

次に型付けについてです。Pythonは動的型付け言語であるため型を指定せずに変数宣言ができます。そのためコードが書きやすく高いスピードで開発を進めることができますが、一方で実行時に予期せぬエラーが発生したり、可読性や保守性が低下するという課題があります。

そこで、Pythonで使われる機能が「 **型ヒント** 」です。型ヒントは変数や関数の引数・戻り値に対して型を明示的に指定することで、型チェックツールによる確認を可能にする仕組みです。ただし、あくまで型のアノテーションであるため、実行時の制約を課すものではありません。

型ヒントは以下のtypingモジュールを使って実装することができます。

## 型ヒントの種類

ここからは基本的な型ヒントの種類を確認していきます。

### 基本文法

まず変数に型ヒントをつける場合は以下のように書きます。

```python
name: str = "Alice"
age: int = 30
feet: float = 5.5
number: str # 値を代入せずに宣言することも可能
```

関数の引数と戻り値に型ヒントをつける場合は以下のように書きます。

```python
def greeting(name: str) -> str:
    return "Hello " + name
```

### コレクション型

リストや辞書なども指定することができます。ここでは辞書のリストを受け取ってタプルを返す関数となっています。

```python
from typing import List, Dict, Tuple

def process_data(
    data: List[Dict[str, int]]
) -> Tuple[int, int]:
    total = sum(item["value"] for item in data)
    count = len(data)
    return total, count

# 使用例
records = [{"value": 10}, {"value": 20}, {"value": 5}]
total, count = process_data(records)
```

### UnionとOptional

いくつかの型を許容したい場合には **Union** を使うことができます。以下の例では関数の引数は int, float, str のいずれでも受け取ることができ、型によって処理が異なる関数を定義しています。

```python
from typing import Union

def format_value(value: Union[int, float, str]) -> str:
    """
    - int が来たら 2 倍して文字列化
    - float が来たら小数点以下 2 桁で丸めて文字列化
    - str が来たら大文字化して返す
    """
    if isinstance(value, int):
        return f"Int: {value * 2}"
    elif isinstance(value, float):
        return f"Float: {value:.2f}"
    else:  # str
        return f"String: {value.upper()}"

# 使用例
print(format_value(3))       # → "Int: 6"
print(format_value(3.14159)) # → "Float: 3.14"
print(format_value("hello")) # → "String: HELLO"
```

Noneを許容したい場合は **Optional** を使うことができます。OptionalはUnion\[X, None\]と同義です。以下の例ではリストと文字列のキーを受け取って、int型のインデックス番号もしくはNoneを返します。

```python
from typing import Optional

# None 許容の例
def find_item(items: List[str], key: str) -> Optional[int]:
    if key in items:
        return items.index(key)
    return None  # 見つからない場合は None を返す
```

### Any

JSONの戻り値に細かい型情報がない場合など、型が不確定なデータを一時的に受け取りたい場合は **Any** を使うことができます。

```python
from typing import Any

def load_config() -> Any:
    return json.load(open('config.json'))
```

以下のように適当なメソッドを書いても静的解析ツールはエラーを返しません。

```python
from typing import Any

def foo(item: Any) -> int:
    # Passes type checking; 'item' could be any type,
    # and that type might have a 'bar' method
    item.bar()
    ...
```

### Literal

変数や関数の引数が受け取る値を限定して、異なる文字列や数値の入力を防ぎたい場合は **Literal** を使うことができます。パラメータなどあらかじめ取りうる設定が決まっている場合に有用です。

```python
from typing import Literal

def set_mode(mode: Literal['auto', 'manual']) -> None:
    print(f"Mode set to {mode}")

set_mode('auto')    # OK
set_mode('automatic')  # 静的解析エラー
```

### Final

再代入を禁止したい定数や継承させたくないクラスやメソッドを明示したい場合には **Final** を使うことできます。

```python
from typing import Final

MAX_SIZE: Final = 9000
MAX_SIZE += 1  # 静的解析エラー

class Connection:
    TIMEOUT: Final[int] = 10

class FastConnector(Connection):
    TIMEOUT = 1  # 静的解析エラー
```

### Callable

引数と戻り値の型を指定した関数を使う場合には **Callable** が便利です。Callable\[引数の型, 戻り値の型\]で指定することで、そのシグネチャを持った関数を受け取ることができます。以下の例は引数はどんな型でも許容し、戻り値はstrとする場合です。（lambda 引数: 戻り値の式なので何を引数としても"ok!"を返す。）

```python
from typing import Callable

F_any = Callable[..., str]

def anyfunction(fn: F_any) -> None:
    result = fn(1, "foo", key=True)
    print("anyfunction →", result)
    
    
# 使用例
anyfunction(lambda *args, **kwargs: "ok!") # anyfunction → ok!
```

以下の例は引数をint, strで受け取り、戻り値をstrとする場合です。

```python
from typing import Callable

F_type = Callable[[int, str], str]

def typefunction(fn: F_type, n: int, s: str) -> None:
    result = fn(n, s)
    print("typefunction →", result)

# 使用例
def repeat_text(times: int, text: str) -> str:
    return text * times

typefunction(repeat_text, 3, "ha") # typefunction → hahaha
```

## dataclassを使う

型ヒントの種類をざっと理解したところで、次に **dataclass** を紹介します。dataclassは型を伴うデータ構造を定義するためのデコレータであり、データ型を厳格に指定して辞書のようにデータ構造の定義をしたい場合に使うことができます。dataclassを使うことでコードの可読性や保守性を高めることにつながります。

### dataclassの使い方

まずはdataclassの基本的な使い方を確認します。

### 基本文法

dataclassは以下のように使うことができます。dataclassは、 `__init__`, `__repr__`, `__eq__` を自動生成するため、非常にシンプルに書くことができ、可読性が高まります。また、以下のようにprintした際にはメモリアドレスではなく中身だけが綺麗に表示されます。

```python
from dataclasses import dataclass

@dataclass
class Human:
    name: str
    age: int
    feet: float
    number: str = "001"  # デフォルト値を設定

human = Human(name="Alice", age=30, feet=5.5)

print(human)
print(human.name)
```

```
Human(name='Alice', age=30, feet=5.5, number='001')
Alice
```

### ネスト構造の場合

dataclassはネストした構造でも簡潔に書くことができます。以下の例では `Address` という住所を意味するクラスを親となる `Human` クラスに入れ込んでいます。

```python
from dataclasses import dataclass

@dataclass
class Address:
    city: str
    zipcode: str

@dataclass
class Human:
    name: str
    age: int
    feet: float
    address: Address  # ネスト
    number: str = "001"  # デフォルト値

human = Human(
    name="Alice",
    age=30,
    feet=5.5,
    address=Address(city="Tokyo", zipcode="100-0001"),
)

print(human)
print(human.name)
print(human.address.city)
```

```
Human(name='Alice', age=30, feet=5.5, address=Address(city='Tokyo', zipcode='100-0001'), number='001')
Alice
Tokyo
```

### イミュータブル化

インスタンス生成後に再代入することを防ぐために、 `frozen=True` とすることでイミュータブル化を行うことができます。以下のようにデフォルトは `frozen=False` であるため再代入が可能であり、 `frozen=True` とするとエラーが発生します。（なお、 `object.__setattr__()` を直接呼び出すことで値を書き換えること自体は可能なようです。）

```python
from dataclasses import dataclass

@dataclass
class HumanNotFrozen:
    name: str
    age: int

@dataclass(frozen=True)
class HumanFrozen:
    name: str
    age: int

human_not_frozen = HumanNotFrozen(name="Alice", age=30)
human_frozen = HumanFrozen(name="Bob", age=25)

human_not_frozen.age = 31
print(human_not_frozen)
human_frozen.age = 26
print(human_frozen)
```

```
HumanNotFrozen(name='Alice', age=31)
dataclasses.FrozenInstanceError: cannot assign to field 'age'
```

### スロット化

インスタンスに新しい属性を追加することを防ぐためには `slots=True` とすることで対応できます。以下のようにデフォルトは `slots=False` であるため属性の追加が可能であり、 `slots=True` とするとエラーが発生します。また、 `slots=True` の場合はデフォルトの場合に生成される `__dict__` が生成されないため、メモリ節約にもなるようです。

```python
from dataclasses import dataclass

@dataclass
class HumanNotSlots:
    name: str
    age: int

@dataclass(slots=True)
class HumanSlots:
    name: str
    age: int

human_not_slots = HumanNotSlots(name="Carol", age=28)
human_slots = HumanSlots(name="Caro", age=28)

human_not_slots.feet = 5.5
print(human_not_slots)
human_slots.feet = 5.5
print(human_slots)
```

```
HumanNotSlots(name='Carol', age=28)
AttributeError: 'HumanSlots' object has no attribute 'feet'
```

一つ目のprintで `feet` が表示されないのは、dataclasses の `__repr__` （文字列表現）にはデフォルトで定義済みのフィールドのみが表示される仕様であるためのようです。

### dataclassを使う利点

**型を指定するため可読性・保守性が高い**  
型を指定してデータ構造を定義することで、どの項目がどのような型を持っているのかを理解することができます。複数人で開発を行ったり、過去のコードを改修する場合に役立ちます。辞書型で管理しているデータ集合をdataclassに置き換えるといったことが推奨されます。

**IDEによる補完が可能**  
上記の例で言うと、 `Human` クラスから作成した `human` というインスタンスにおいて、 `human.`まで入力すると `name`, `age`, `feet`, `number` という候補が生成されます。これによってそのインスタンスにどのようなキーが存在しているかを把握することができるため、キーを指定する際のスペルミスによるエラー発生を防ぎやすくなります。

## 型チェックツールを使う

Pythonで記載した型に問題がないかをチェックするためのツールがあります。型チェックツールにはmypyやPyrightといったものがあるようですが、ここでは **Pyright** を使ってみます。PyrightはMicrosoftが提供するPythonの静的型チェッカーで、高速な処理が特徴とされています。

### CLIで使う場合

以下のコマンドでPyrightをインストールします。Node.jsが事前にインストールされている必要があります。（pipを使ってインストールすることもできます。）

```
npm install -g pyright
```

次にPyrightでチェックする条件を設定します。ルートディレクトリに `pyrightconfig.json` というファイルをを作成します。以下の設定は一例です。 [こちらのドキュメント](https://microsoft.github.io/pyright/#/configuration?id=pyright-configuration) に詳細な項目が記載されています。

```json
{
  "include": ["src"],
  "exclude": ["tests", "build"],
  "reportMissingImports": true,
  "pythonVersion": "3.11",
  "typeCheckingMode": "strict"
}
```

- `"include": ["src"]` ：型チェック対象とするディレクトリやファイルを指定する。ここではsrc/ディレクトリ以下を対象とする。
- `"exclude": ["tests", "build"]` ：型チェックから除外するフォルダやファイルを指定する。ここではtests, buildを対象とする。
- `"reportMissingImports": true` ：パッケージ未インストールやパス設定ミスも対象とする。
- `"pythonVersion": "3.11"` ：基準とするPythonバージョンを3.11とする。
- `"typeCheckingMode": "strict"` ：チェック基準をstrictとする。

設定が準備できたら任意のファイルでチェックを行います。ここでは以下のように、int型を指定した `age` に文字列を渡しているコードをチェックしてみます。

```python
from dataclasses import dataclass

@dataclass
class Human:
    name: str
    age: int
    feet: float
    number: str = "001"

human = Human(name="Alice", age="30", feet=5.5) # intを指定したageに文字列を与えてみる

print(human)
print(human.name)
```

```
pyright dataclass.py
```

以下のように返ってきました。誤った型で値を渡している部分を検出することができました。

```
****/dataclass.py:12:33 - error: Argument of type "Literal['30']" cannot be assigned to parameter "age" of type "int" in function "__init__"
    "Literal['30']" is not assignable to "int" (reportArgumentType)
1 error, 0 warnings, 0 informations
```

### VS Codeで使う場合

型チェックはCLIよりもIDEの段階で利用することが多いかと思われます。PyrightもVS Codeの拡張機能で簡単に使うことができるようになっています。VS CodeでPyrightを使う場合は、PylanceというPyrightを内蔵したPython拡張機能を用いるのが便利です。Pythonの拡張機能を入れている場合、すでに入れていることが多いです。

拡張機能をインストールして有効化した後、設定から `python.analysis.typeCheckingMode` を検索します。以下の画面のように型チェックのモードを選択することができます。以下ではstrictを設定しています。

![](https://storage.googleapis.com/zenn-user-upload/86253cd46f57-20250906.png)

このように設定すると、以下のように型エラーが発生する箇所は自動でチェックされ、赤線が引かれるようになります。またファイル名も赤文字になるため、異常のあるファイルを容易に見つけることが可能になります。

![](https://storage.googleapis.com/zenn-user-upload/a5847424140e-20250906.png)

## 静的コード解析・型チェックをワークフローに組み込む

最後に、Ruffによるコード解析とPyrightによる型チェックを開発ワークフローに組み込んでみます。必須でチェックしたいことはCI (Continuous Integration) として組み込むことが望ましいと思われますが、CI/CDに関しては別記事（AIエンジニアリング入門：開発ワークフローの整備（仮））でまとめていこうと思いますので、ここではローカルでより簡易に実行できる方法として、 **Git hooks** を使って実装していきます。Git hooksとは、gitにおける特定のアクションが発生した時にカスタムスクリプトを叩くように呼び出し設定をできる機能です。また、Git hooksを効率的に管理・実行するためのフレームワークである **pre-commit** も用います。

ここではコミット前（pre-commit）でRuffによるコード解析を実行し、プッシュ前（pre-push）でPyrightによる型チェックを実行するように設定していきます。

## 準備

まずは上で紹介したuvでプロジェクトを作成し、 `uv add ruff` でruffをインストールしておきます。  
その後、 `pyproject.toml` にruffの設定を書き込みます。ここではデフォルトの設定としました。（詳細は上記のRuffパートを参照。）

次に、上記同様に `pyrightconfig.json` を作成しておきます。ルートディレクトリを対象とするため `"include": ["."]` と変更しておきます。（詳細は上記Pyrightパートを参照。）

## Git hooksを設定

ここではGit hooksを簡易に扱うためのフレームワークであるpre-commitを用いるため、 `uv add pre-commit` でインストールします。

ここからGit hooksの設定をしていきます。Git hooksの方式には`.git/hooks/pre-commit` や `pre-push` に直接スクリプトを書き込む方法と、一度 `.pre-commit-config.yaml` に書き込む方法があります。後者の場合はyamlファイルを作成したのち `pre-commit install` を実行することで`.git/hooks/pre-commit` を作成することができます。今回は後者の方法を用いることにして、以下のように`.pre-commit-config.yaml` を作成します。yamlファイルの項目の意味については [こちらのドキュメント](https://pre-commit.com/#usage) を参照してください。

```yaml
repos:
  # --- pre-commit: コミット前に Ruff で整形 → Lint/自動修正 ---
  - repo: local
    hooks:
      - id: ruff-format
        name: ruff format (staged)
        entry: uvx ruff format
        language: system
        types: [python]
        stages: [pre-commit]

      - id: ruff-lint
        name: ruff check --fix (staged)
        entry: uvx ruff check --fix --exit-non-zero-on-fix # 修正が必要な場合はコミットを停止
        language: system
        types: [python]
        stages: [pre-commit]

  # --- pre-push: プッシュ前に Pyright で型チェック（全体） ---
  - repo: local
    hooks:
      - id: pyright
        name: pyright (type check on pre-push)
        entry: uvx pyright
        language: system
        pass_filenames: false    # 変更ファイルだけでなくプロジェクト全体を検査
        stages: [pre-push]
```

このフックをGitに配線します。

```
# pre-commit（コミット時）用
uvx pre-commit install

# pre-push（プッシュ時）用
uvx pre-commit install --hook-type pre-push
```

`.git/hooks/` の下に `pre-commit` と `pre-push` が作成されたことが確認できます。

![](https://storage.googleapis.com/zenn-user-upload/52644722e707-20250906.png)

## pre-commitの実行

ここからpre-commitに設定したRuffを使ってチェックを行います。検証用には以下のように整形されておらず不要なインポートなどが含まれた `check.py` というファイルを用います。

```python
from dataclasses import dataclass
import os
@dataclass
class Human:
    name: str
    age: int
    feet: float
    number: str = "001"
human = Human(name="Alice", age="30", feet=5.5)　# intを指定したageに文字列を与えてみる
print(human)
print(human.name)
```

ステージングとコミットを行います。

```
git add check.py
git commit -m "pre-commit test"
```

以下のように返ってきました。pre-commitに設定したフォーマッターとリンターが機能していることがわかります。

```
ruff format (staged).....................................................Failed
- hook id: ruff-format
- files were modified by this hook

1 file reformatted

ruff check --fix (staged)................................................Failed
- hook id: ruff-lint
- exit code: 1
- files were modified by this hook

Found 1 error (1 fixed, 0 remaining).
```

`check.py` は以下のように自動修正されました。

```python
from dataclasses import dataclass

@dataclass
class Human:
    name: str
    age: int
    feet: float
    number: str = "001"  # デフォルト値を設定

human = Human(name="Alice", age="30", feet=5.5)
print(human)
print(human.name)
```

次に、pre-pushに設定したPyrightを使って、このファイルに存在するageの型エラーが検出できるか確認します。修正後のコードで再度コミットしておきます。

```
git add check.py
git commit -m "pre-push test"
```

今度は問題なくパスしました。

リモートにプッシュしてみます。

```
git push origin main
```

以下のように返ってきました。意図した通りageの型エラーが指摘されていることがわかります。

```
error: Argument of type "Literal['30']" cannot be assigned to parameter "age" of type "int" in function "__init__"
    "Literal['30']" is not assignable to "int" (reportArgumentType)
16409 errors, 11 warnings, 0 informations
```

`age=30` に修正して再度ステージング、コミット、プッシュしたところ、以下のようにチェックをパスすることができました。

```
pyright (type check on pre-push).....................(no files to check)Skipped
```

## 終わりに

AIエンジニアリング入門として、今回は「Pythonによる開発の基礎」と題して、効率的かつ保守性高く開発を進めるためのツールについて紹介しました。これらのツールは現在よく使われているものですが、近い将来には別のツールに置き換わっている可能性もあります。したがって、ここで重要なことは、これらのツールがどのような課題を解決するためのものであり、そのためにどのような機能を有しているかを理解することです。もし既存のツールで解決できない課題や要求があれば、きっと将来的に新たな機能が登場したり、別の優れたツールに置き換えられることでしょう。効率的かつ保守性高く開発を進めるために必要な観点を意識して、これらのサポートツールに引き続き注目して、使いこなしていきたいと思います。

## 参考

以下の資料や記事を参考にさせていただきました。この場を借りてお礼申し上げます。

- [Rust製のPythonパッケージ管理ツール「uv」を使ってみよう](https://gihyo.jp/article/2024/03/monthly-python-2403)
- [uvだけでPythonプロジェクトを管理する](https://zenn.dev/turing_motors/articles/594fbef42a36ee)
- [新しい静的コード解析ツール「Ruff」をご紹介](https://gihyo.jp/article/2023/03/monthly-python-2303)
- [PythonのRuff LinterをVSCodeで使う](https://zenn.dev/enven/articles/python-ruff-with-vscode)
- [\[関西Kaggler会2025#2LT\] 初学者+MLエンジニア対象！ モダンなPythonの書き方](https://speakerdeck.com/koheiiwamasa/guan-xi-kagglerhui-2025-number-2lt-chu-xue-zhe-plus-mlenziniadui-xiang-modannapythonnoshu-kifang)
- [Python最新バージョン対応！より良い型ヒントの書き方](https://gihyo.jp/article/2022/09/monthly-python-2209)
- [Pythonのdataclassを知る](https://zenn.dev/karaage0703/articles/3508b20ece17d4)
- [すべてを救う Python の型ヒントについて](https://note.com/shunk031/n/n02edafb543a6?magazine_key=m84877e9f9649)
- [dataclass で万物に型を付けよう](https://note.com/shunk031/n/nc1106f2ef926?magazine_key=m84877e9f9649)
- [Python のコードを美しく保つには](https://note.com/shunk031/n/n65c55ca011e3?magazine_key=m84877e9f9649)

191

110
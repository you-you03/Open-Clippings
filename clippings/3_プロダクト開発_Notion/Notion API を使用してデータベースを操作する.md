---
title: "Notion API を使用してデータベースを操作する"
source: "https://zenn.dev/kou_pg_0131/articles/notion-api-usage"
author:
  - "[[Zenn]]"
published: 
created: 2025-09-03
description: ""
tags: ["clippings", "notion", "プロダクト", "ノートツール"]
image: "assets/og-base-w1200-v2.png"
---
Notion で Integration を作成して Notion API を使用してデータベースを操作するまでの手順メモ。

準備
==

1. Integration を作成する
--------------------

[My integrations](https://www.notion.so/my-integrations) ページに遷移します。

`Create new integration` をクリックします。

![](https://res.cloudinary.com/zenn/image/fetch/s--kvhmP3yl--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/d23a7f0d9cb496296e9a76c9.png%3Fsha%3Dee889117c0b44231fea4b6b7626d2660d4322231)

`Name` には任意の Integration 名を入力します。  
今回は `Example Integration` としておきます。

`Associated workspace` には Integration をインストールするワークスペースを選択します。  
自身がワークスペースの Admin レベルの権限を持っている必要があります。

`Capabilities` には Integration から実行できる機能を選択します。  
次のような項目があります。  
Integration の用途に合わせて適切に設定してください。

* `Content Capabilities`
  + `Read content` : コンテンツの読み取り
  + `Update content` : 既存のコンテンツの更新
  + `Insert content` : 新しいコンテンツの作成
* `Comment Capabilities`
  + `Read comments` : コメントの読み取り
  + `Insert comments` : コメントの作成
* `User Capabilities`
  + `No user information` : ユーザー情報にはアクセスさせない
  + `Read user information without email addresses` : メールアドレス以外のユーザー情報の読み取り
  + `Read user information including email addresses` : メールアドレスを含めたユーザー情報の読み取り

これらの項目は全て後から変更できます。  
それぞれ入力できたら `Submit` をクリックします。  
これで Integration が作成されます。

![](https://res.cloudinary.com/zenn/image/fetch/s--UzQQM1mz--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/8b990991c171c9921e64b429.png%3Fsha%3Dc7e97d2bf63719c5999fecd0850f2a16355eca20)

Integration を作成するとトークンが発行されます。  
`Internal Integration Token` の `Show` をクリックすると `secret_` から始まるトークンが確認できます。  
このトークンは Notion API を実行するときに必要になるため、ひかえておきます。

![](https://res.cloudinary.com/zenn/image/fetch/s--yZZ71q8m--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/44c3a22b14c758ee2fed393a.png%3Fsha%3D8170977ad33bdc8e7a9b8fae8835e723c5abd4c1)

2. データベースを作成する
--------------

Notion API で操作するデータベースを作成します。  
今回はこんな感じのデータベースを作成しました。

![](https://res.cloudinary.com/zenn/image/fetch/s--YZIGVLF2--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/9810c97a9e41d84fd515c70b.png%3Fsha%3Da6e1d7a6adf8c0bcdd7550004f5ccd14ab3fd99d)

作成したデータベースの ID を確認します。  
データベースの URL は次のような形式になっています。  
`データベースID` が Notion API で操作するときに必要になるため、ひかえておきます。

```
https://www.notion.so/<データベースID>?v=<ビューID>
```

3. Integration からデータベースにアクセスできるようにする
------------------------------------

Integration は最初はワークスペース内のどのコンテンツにもアクセスできません。  
そのため、アクセスしたいページやデータベースで設定を行う必要があります。

「[2. データベースを作成する](#2.-%E3%83%87%E3%83%BC%E3%82%BF%E3%83%99%E3%83%BC%E3%82%B9%E3%82%92%E4%BD%9C%E6%88%90%E3%81%99%E3%82%8B)」手順で作成したデータベースのページに遷移します。

右上の三点リーダ → `Add connections` → 「[1. Integration を作成する](#1.-integration-%E3%82%92%E4%BD%9C%E6%88%90%E3%81%99%E3%82%8B)」手順で作成した Integration の順にクリックします。

![](https://res.cloudinary.com/zenn/image/fetch/s--V3AjhGol--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/ce81cffab476afd259cbc50b.png%3Fsha%3D4acb4e3a008e0628439d7d98f1a5c72316cc13d1)

確認ダイアログが表示されるので、 `Confirm` をクリックします。  
これで Integration からこのページと子ページにアクセスできるようになります。

![](https://res.cloudinary.com/zenn/image/fetch/s--Oj_bRlft--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/4be04fb290fdb8bf463d32f2.png%3Fsha%3D5a0b92e5b68668115c8568b1e8381006149673d3)

Notion API を使ってみる
=================

データベースの情報を取得する
--------------

<https://developers.notion.com/reference/retrieve-a-database>

次のエンドポイントに `GET` リクエストを送信することで特定のデータベースの情報を取得することができます。

```
https://api.notion.com/v1/databases/<データベースID>
```

次のコマンドは `curl` を使用して特定のデータベース情報を取得する例です。

```
$ curl 'https://api.notion.com/v1/databases/<データベースID>' \
  -H 'Authorization: Bearer <Integrationトークン>' \
  -H 'Notion-Version: 2022-06-28'
```

出力例

```
{
  "object": "database",
  "id": "********-****-****-****-************",
  "cover": null,
  "icon": null,
  "created_time": "2023-02-25T01:04:00.000Z",
  "created_by": {
    "object": "user",
    "id": "********-****-****-****-************"
  },
  "last_edited_by": {
    "object": "user",
    "id": "********-****-****-****-************"
  },
  "last_edited_time": "2023-02-25T01:17:00.000Z",
  "title": [
    {
      "type": "text",
      "text": {
        "content": "Example Database",
        "link": null
      },
      "annotations": {
        "bold": false,
        "italic": false,
        "strikethrough": false,
        "underline": false,
        "code": false,
        "color": "default"
      },
      "plain_text": "Example Database",
      "href": null
    }
  ],
  "description": [],
  "is_inline": false,
  "properties": {
    "Status": {
      "id": "****",
      "name": "Status",
      "type": "status",
      "status": {
        "options": [
          {
            "id": "********-****-****-****-************",
            "name": "Not started",
            "color": "default"
          },
          {
            "id": "********-****-****-****-************",
            "name": "In progress",
            "color": "blue"
          },
          {
            "id": "********-****-****-****-************",
            "name": "Done",
            "color": "green"
          }
        ],
        "groups": [
          {
            "id": "********-****-****-****-************",
            "name": "To-do",
            "color": "gray",
            "option_ids": ["********-****-****-****-************"]
          },
          {
            "id": "********-****-****-****-************",
            "name": "In progress",
            "color": "blue",
            "option_ids": ["********-****-****-****-************"]
          },
          {
            "id": "********-****-****-****-************",
            "name": "Complete",
            "color": "green",
            "option_ids": ["********-****-****-****-************"]
          }
        ]
      }
    },
    "Assign": {
      "id": "******",
      "name": "Assign",
      "type": "people",
      "people": {}
    },
    "Name": {
      "id": "title",
      "name": "Name",
      "type": "title",
      "title": {}
    }
  },
  "parent": {
    "type": "workspace",
    "workspace": true
  },
  "url": "https://www.notion.so/<データベースID>",
  "archived": false
}
```

データベースのアイテム一覧を取得する
------------------

<https://developers.notion.com/reference/post-database-query>

次のエンドポイントに `POST` リクエストを送信することで特定のデータベースのアイテム一覧を取得することができます。

```
https://api.notion.com/v1/databases/<データベースID>/query
```

次のコマンドは `curl` を使用して特定のデータベースのアイテム一覧を取得する例です。

```
$ curl -X POST 'https://api.notion.com/v1/databases/<データベースID>/query' \
  -H 'Authorization: Bearer <Integrationトークン>' \
  -H 'Notion-Version: 2022-06-28'
```

出力例

```
{
  "object": "list",
  "results": [
    {
      "object": "page",
      "id": "********-****-****-****-************",
      "created_time": "2023-02-25T01:04:00.000Z",
      "last_edited_time": "2023-02-25T01:33:00.000Z",
      "created_by": {
        "object": "user",
        "id": "********-****-****-****-************"
      },
      "last_edited_by": {
        "object": "user",
        "id": "********-****-****-****-************"
      },
      "cover": null,
      "icon": null,
      "parent": {
        "type": "database_id",
        "database_id": "********-****-****-****-************"
      },
      "archived": false,
      "properties": {
        "Status": {
          "id": "****",
          "type": "status",
          "status": {
            "id": "********-****-****-****-************",
            "name": "Not started",
            "color": "default"
          }
        },
        "Assign": {
          "id": "******",
          "type": "people",
          "people": []
        },
        "Name": {
          "id": "title",
          "type": "title",
          "title": [
            {
              "type": "text",
              "text": {
                "content": "Card 2",
                "link": null
              },
              "annotations": {
                "bold": false,
                "italic": false,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
              },
              "plain_text": "Card 2",
              "href": null
            }
          ]
        }
      },
      "url": "https://www.notion.so/Card-2-********************************"
    },
    {
      "object": "page",
      "id": "********-****-****-****-************",
      "created_time": "2023-02-25T01:04:00.000Z",
      "last_edited_time": "2023-02-25T01:04:00.000Z",
      "created_by": {
        "object": "user",
        "id": "********-****-****-****-************"
      },
      "last_edited_by": {
        "object": "user",
        "id": "********-****-****-****-************"
      },
      "cover": null,
      "icon": null,
      "parent": {
        "type": "database_id",
        "database_id": "********-****-****-****-************"
      },
      "archived": false,
      "properties": {
        "Status": {
          "id": "****",
          "type": "status",
          "status": {
            "id": "********-****-****-****-************",
            "name": "Not started",
            "color": "default"
          }
        },
        "Assign": {
          "id": "******",
          "type": "people",
          "people": []
        },
        "Name": {
          "id": "title",
          "type": "title",
          "title": [
            {
              "type": "text",
              "text": {
                "content": "Card 1",
                "link": null
              },
              "annotations": {
                "bold": false,
                "italic": false,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
              },
              "plain_text": "Card 1",
              "href": null
            }
          ]
        }
      },
      "url": "https://www.notion.so/Card-1-********************************"
    },
    {
      "object": "page",
      "id": "********-****-****-****-************",
      "created_time": "2023-02-25T01:04:00.000Z",
      "last_edited_time": "2023-02-25T01:33:00.000Z",
      "created_by": {
        "object": "user",
        "id": "********-****-****-****-************"
      },
      "last_edited_by": {
        "object": "user",
        "id": "********-****-****-****-************"
      },
      "cover": null,
      "icon": null,
      "parent": {
        "type": "database_id",
        "database_id": "********-****-****-****-************"
      },
      "archived": false,
      "properties": {
        "Status": {
          "id": "****",
          "type": "status",
          "status": {
            "id": "********-****-****-****-************",
            "name": "Not started",
            "color": "default"
          }
        },
        "Assign": {
          "id": "******",
          "type": "people",
          "people": []
        },
        "Name": {
          "id": "title",
          "type": "title",
          "title": [
            {
              "type": "text",
              "text": {
                "content": "Card 3",
                "link": null
              },
              "annotations": {
                "bold": false,
                "italic": false,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
              },
              "plain_text": "Card 3",
              "href": null
            }
          ]
        }
      },
      "url": "https://www.notion.so/Card-3-********************************"
    }
  ],
  "next_cursor": null,
  "has_more": false,
  "type": "page",
  "page": {}
}
```

### フィルター

リクエストボディに `filter` を設定することでアイテムをフィルタして取得することができます。  
次のコマンドは `curl` を使用して `status` 型の `Status` プロパティが `Not started` であるアイテムをフィルタして取得する例です。

```
$ curl -X POST 'https://api.notion.com/v1/databases/<データベースID>/query' \
  -H 'Authorization: Bearer <Integrationトークン>' \
  -H 'Content-Type: application/json' \
  -H 'Notion-Version: 2022-06-28' \
  --data '{
  "filter": {
    "property": "Status",
    "status": {
      "equals": "Not started"
    }
  }
}'
```

また、 `and` や `or` を使用して複数の条件を指定することもできます。  
次のコマンドは `curl` を使用して `status` 型の `Status` プロパティが `Not started` もしくは `In progress` であるアイテムをフィルタして取得する例です。

```
$ curl -X POST 'https://api.notion.com/v1/databases/<データベースID>/query' \
  -H 'Authorization: Bearer <Integrationトークン>' \
  -H 'Content-Type: application/json' \
  -H 'Notion-Version: 2022-06-28' \
  --data '{
  "filter": {
    "or": [
      {
        "property": "Status",
        "status": {
          "equals": "Not started"
        }
      },
      {
        "property": "Status",
        "status": {
          "equals": "In progress"
        }
      }
    ]
  }
}'
```

その他の詳しいフィルタの指定方法については以下の公式リファレンスをご参照ください。

<https://developers.notion.com/reference/post-database-query-filter>

### ソート

リクエストボディに `sorts` を設定することでアイテムをソートして取得することができます。  
次のコマンドは `curl` を使用してアイテムを `Name` プロパティで昇順にソートして取得する例です。

```
$ curl -X POST 'https://api.notion.com/v1/databases/<データベースID>/query' \
  -H 'Authorization: Bearer <Integrationトークン>' \
  -H 'Content-Type: application/json' \
  -H 'Notion-Version: 2022-06-28' \
    --data '{
  "sorts": [
    {
      "property": "Name",
      "direction": "ascending"
    }
  ]
}'
```

複数のソート条件を指定することもできます。  
次のコマンドは `curl` を使用してアイテムを `Name` プロパティで昇順・ `Status` プロパティで降順にソートして取得する例です。  
複数指定した場合は最初の要素が優先されます。

```
$ curl -X POST 'https://api.notion.com/v1/databases/<データベースID>/query' \
  -H 'Authorization: Bearer <Integrationトークン>' \
  -H 'Content-Type: application/json' \
  -H 'Notion-Version: 2022-06-28' \
    --data '{
  "sorts": [
    {
      "property": "Name",
      "direction": "ascending"
    },
    {
      "property": "Status",
      "direction": "descending"
    }
  ]
}'
```

その他の詳しいソートの指定方法については以下の公式リファレンスをご参照ください。

<https://developers.notion.com/reference/post-database-query-sort>

データベースにアイテムを追加する
----------------

<https://developers.notion.com/reference/post-page>

次のエンドポイントに `POST` リクエストを送信することでアイテム ( ページ ) を作成することができます。

```
https://api.notion.com/v1/pages
```

次のコマンドは `curl` を使用して `アイテムのタイトル` という名前で `Status` プロパティが `In progress` であるアイテムを作成するコマンドです。

```
$ curl -X POST 'https://api.notion.com/v1/pages' \
-H 'Authorization: Bearer <Integrationトークン>' \
-H 'Content-Type: application/json' \
-H 'Notion-Version: 2022-06-28' \
--data '{
  "parent": { "database_id": "<データベースID>" },
  "properties": {
    "Name": {
      "title": [
        { "text": { "content": "アイテムのタイトル" } }
      ]
    },
    "Status": {
      "status": { "name": "In progress" }
    }
  }
}'
```

出力例

```
{
  "object": "page",
  "id": "********-****-****-****-************",
  "created_time": "2023-02-25T02:14:00.000Z",
  "last_edited_time": "2023-02-25T02:14:00.000Z",
  "created_by": {
    "object": "user",
    "id": "********-****-****-****-************"
  },
  "last_edited_by": {
    "object": "user",
    "id": "********-****-****-****-************"
  },
  "cover": null,
  "icon": null,
  "parent": {
    "type": "database_id",
    "database_id": "********-****-****-****-************"
  },
  "archived": false,
  "properties": {
    "Status": {
      "id": "****",
      "type": "status",
      "status": {
        "id": "********-****-****-****-************",
        "name": "In progress",
        "color": "blue"
      }
    },
    "Assign": {
      "id": "******",
      "type": "people",
      "people": []
    },
    "Name": {
      "id": "title",
      "type": "title",
      "title": [
        {
          "type": "text",
          "text": {
            "content": "アイテムのタイトル",
            "link": null
          },
          "annotations": {
            "bold": false,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "アイテムのタイトル",
          "href": null
        }
      ]
    }
  },
  "url": "https://www.notion.so/********************************"
}
```

アイテム ( ページ ) のプロパティの形式については以下の公式リファレンスをご参照ください。

<https://developers.notion.com/reference/page-property-values>

データベースのアイテムを更新する
----------------

<https://developers.notion.com/reference/patch-page>

次のエンドポイントに `PATCH` リクエストを送信することで特定のアイテム ( ページ ) を更新することができます。

```
https://api.notion.com/v1/pages/<ページID>
```

まず更新したいアイテム ( ページ ) の URL を取得します。  
データベース内のアイテムをクリックします。  
右上の三点リーダ → `Copy link` をクリックして URL を取得します。

![](https://res.cloudinary.com/zenn/image/fetch/s--KohVSE8g--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/b94e7f60fa170b8c2ee58590.png%3Fsha%3Dd0f09644a42ef870ce56504a2696a68bc7b878d8)

アイテム ( ページ ) の URL は次のような形式になっています。  
`ページID` が必要になるため、ひかえておきます。

```
https://www.notion.so/<ページ名>-<ページID>
```

次のコマンドは `curl` を使用してアイテムの `status` 型の `Status` プロパティを `In progress` に更新する例です。

```
$ curl -X PATCH 'https://api.notion.com/v1/pages/<ページID>' \
-H 'Authorization: Bearer <Integrationトークン>' \
-H 'Content-Type: application/json' \
-H 'Notion-Version: 2022-06-28' \
--data '{
  "properties": {
    "Status": {
      "status": { "name": "In progress" }
    }
  }
}'
```

出力例

```
{
  "object": "page",
  "id": "********-****-****-****-************",
  "created_time": "2023-02-25T01:04:00.000Z",
  "last_edited_time": "2023-02-25T02:32:00.000Z",
  "created_by": {
    "object": "user",
    "id": "********-****-****-****-************"
  },
  "last_edited_by": {
    "object": "user",
    "id": "********-****-****-****-************"
  },
  "cover": null,
  "icon": null,
  "parent": {
    "type": "database_id",
    "database_id": "********-****-****-****-************"
  },
  "archived": false,
  "properties": {
    "Status": {
      "id": "****",
      "type": "status",
      "status": {
        "id": "********-****-****-****-************",
        "name": "In progress",
        "color": "blue"
      }
    },
    "Assign": {
      "id": "******",
      "type": "people",
      "people": []
    },
    "Name": {
      "id": "title",
      "type": "title",
      "title": [
        {
          "type": "text",
          "text": {
            "content": "Card 1",
            "link": null
          },
          "annotations": {
            "bold": false,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "Card 1",
          "href": null
        }
      ]
    }
  },
  "url": "https://www.notion.so/Card-1-********************************"
}
```

アイテム ( ページ ) のプロパティの形式については以下の公式リファレンスをご参照ください。

<https://developers.notion.com/reference/page-property-values>

参考
==

<https://developers.notion.com/docs/getting-started>  
<https://developers.notion.com/reference>

# 获取标签列表接口

获取网站的标签列表，支持按文档ID获取特定文档的标签、按首字母筛选、分页查询等功能。

## 注意事项

- 该接口采用GET方法
- 可以获取全部标签列表或指定文档的标签
- 支持按首字母筛选标签
- 支持分页查询，可以指定每页显示数量和页码
- 支持不同的返回类型（列表或分页）
- 返回标签的基本信息和SEO相关信息

## 请求地址

```
{域名地址}/api/tag/list
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/tag/list`

## 请求语法

```
GET {域名地址}/api/tag/list
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :----- | :----- | :--- | :--- |
| itemId | int | 否 | 文档ID，读取指定文档的Tag列表，如果不指定则读取所有标签 |
| letter | string | 否 | 首字母，指定首字母可以获取指定的标签集合 |
| type | string | 否 | 链接形式，默认list，可以是list\|page，type=page时可以获取到total |
| page | int | 否 | 获取指定分页数据，只有在type=page时有效 |
| limit | int | 否 | 显示数量，支持offset模式，如"2,10"表示从第2条开始获取10条数据 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object[] | 标签列表数据 |
| total | int | 总数，仅当type=page时返回 |

#### data item 参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| id | int | 标签ID |
| title | string | 标签名称 |
| seo_title | string | 标签SEO标题 |
| url_token | string | 标签URL别名 |
| keywords | string | 标签关键词 |
| description | string | 标签简介 |
| first_letter | string | 标签首字母 |
| link | string | 标签链接地址 |
| created_time | int | 标签创建时间戳 |
| updated_time | int | 标签更新时间戳 |
| status | int | 标签显示状态 |

## 使用示例

### 请求示例

#### 获取指定文档的标签列表
```
GET /api/tag/list?itemId=1 HTTP/1.1
Host: www.aicms.com
```

#### 获取全部标签列表（按首字母筛选）
```
GET /api/tag/list?letter=A HTTP/1.1
Host: www.aicms.com
```

#### 获取全部标签列表（分页模式）
```
GET /api/tag/list?type=page&page=1&limit=10 HTTP/1.1
Host: www.aicms.com
```

#### 获取指定文档的标签列表（分页模式）
```
GET /api/tag/list?itemId=1&type=page&page=1&limit=5 HTTP/1.1
Host: www.aicms.com
```

### 响应示例

#### 获取指定文档的标签列表响应
```json
{
  "code": 0,
  "msg": "",
  "data": [
    {
      "id": 1,
      "title": "AICMS",
      "seo_title": "",
      "url_token": "AICMS",
      "keywords": "",
      "description": "",
      "first_letter": "A",
      "link": "https://www.aicms.com/tag/1/",
      "created_time": 1662733318,
      "updated_time": 1662733318,
      "status": 1
    },
    {
      "id": 3,
      "title": "内容管理",
      "seo_title": "",
      "url_token": "content-management",
      "keywords": "",
      "description": "",
      "first_letter": "C",
      "link": "https://www.aicms.com/tag/3/",
      "created_time": 1662733320,
      "updated_time": 1662733320,
      "status": 1
    }
  ]
}
```

#### 获取全部标签列表响应
```json
{
  "code": 0,
  "msg": "",
  "data": [
    {
      "id": 1,
      "title": "AICMS",
      "seo_title": "",
      "url_token": "AICMS",
      "keywords": "",
      "description": "",
      "first_letter": "A",
      "link": "https://www.aicms.com/tag/1/",
      "created_time": 1662733318,
      "updated_time": 1662733318,
      "status": 1
    },
    {
      "id": 2,
      "title": "AICMS",
      "seo_title": "",
      "url_token": "an-qi-cms",
      "keywords": "",
      "description": "",
      "first_letter": "A",
      "link": "https://www.aicms.com/tag/2/",
      "created_time": 1662733318,
      "updated_time": 1662733318,
      "status": 1
    },
    {
      "id": 3,
      "title": "内容管理",
      "seo_title": "",
      "url_token": "content-management",
      "keywords": "",
      "description": "",
      "first_letter": "C",
      "link": "https://www.aicms.com/tag/3/",
      "created_time": 1662733320,
      "updated_time": 1662733320,
      "status": 1
    }
  ],
  "total": 3
}
```

### 错误代码

| 错误码 | 说明 |
| :----- | :--- |
| 0 | OK |
| -1 | 错误，错误原因在 msg 中指出 |
| 1001 | 未登录 |
| 1002 | 未授权 |
| 200 | API 请求 OK |
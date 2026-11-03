# 获取标签文档列表接口

获取指定标签下的相关文档列表，支持多种排序方式和分页查询。

## 注意事项

- 该接口采用GET方法
- 需要提供标签ID或标签URL别名（filename）来指定查询的标签
- 支持多种排序方式，可根据需要选择不同的排序字段
- 支持分页查询，可以指定每页显示数量和页码
- 支持按不同方式获取数据（分页、列表、相关文档等）
- 返回文档的基本信息和扩展信息

## 请求地址

```
{域名地址}/api/tag/data/list
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/tag/data/list`

## 请求语法

```
GET {域名地址}/api/tag/data/list
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :----- | :----- | :--- | :--- |
| id | int | 否 | 标签ID，如果传了filename，可以不用传ID |
| filename | string | 否 | 标签URL别名，标签ID、filename二选一 |
| order | string | 否 | 排序方式，如：`id desc`，支持的字段有：`id`、`views`、`category_id`、`created_time`、`updated_time`等 |
| type | string | 否 | 获取方式，支持`page`、`list`、`related`方式列出，默认值为`list` |
| page | int | 否 | 指定获取第几页内容，仅当type="page"时生效 |
| limit | int | 否 | 显示数量，支持offset模式，如"2,10"表示从第2条开始获取10条数据 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object[] | 结果内容 |
| total | int | 文档数量，仅当type=page时返回 |

#### data item 参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| id | int | 文档ID |
| title | string | 文档标题 |
| seo_title | string | 文档SEO标题 |
| url_token | string | 文档URL别名 |
| keywords | string | 文档关键词 |
| description | string | 文档简介 |
| module_id | int | 文档模型ID |
| category_id | int | 文档分类ID |
| views | int | 文档浏览量 |
| comment_count | int | 文档评论量 |
| images | string[] | 文档组图 |
| logo | string | 文档Logo |
| thumb | string | 文档缩略图 |
| flag | string | 文档推荐属性，头条[h]推荐[c]幻灯[f]特荐[a]滚动[s]加粗[h]图片[p]跳转[j] |
| canonical_url | string | canonical URL |
| fixed_link | string | 文档固定链接 |
| created_time | int | 文档发布时间戳 |
| updated_time | int | 文档更新时间戳 |
| status | int | 文档显示状态 |
| user_id | int | 用户ID |
| price | int | 价格，单位分 |
| stock | int | 库存量 |
| extra | object | 文档扩展字段信息 |
| link | string | 文档链接地址 |

## 使用示例

### 请求示例

```
GET /api/tag/data/list?id=1&type=page&page=1&limit=10 HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": [
    {
      "id": 1,
      "title": "关于AICMS",
      "seo_title": "",
      "url_token": "design",
      "keywords": "",
      "description": "AI内容管理系统(AICMS)，是一款使用 GoLang 开发的企业站内容管理系统...",
      "module_id": 1,
      "category_id": 1,
      "views": 1338,
      "comment_count": 0,
      "images": null,
      "logo": "https://www.aicms.com/uploads/202012/7/bd36c37ef742c7be.webp",
      "thumb": "https://www.aicms.com/uploads/202012/7/thumb_bd36c37ef742c7be.webp",
      "flag": "",
      "canonical_url": "",
      "fixed_link": "",
      "created_time": 1607308159,
      "updated_time": 1662717106,
      "status": 1,
      "user_id": 0,
      "price": 0,
      "stock": 9999999,
      "extra": {
        "author": {
          "name": "作者",
          "value": "AICMS",
          "default": null
        }
      },
      "link": "https://www.aicms.com/design"
    }
  ],
  "total": 1
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
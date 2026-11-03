# 获取收藏列表接口

获取当前用户的收藏列表，支持分页查询，返回用户收藏的所有商品或文档信息。

## 注意事项

- 该接口采用GET方法，参数通过URL查询字符串传递
- 支持分页查询，可指定当前页码和每页显示数量
- 仅返回当前用户的收藏记录
- 返回完整的文档信息，包括标题、描述、图片等详细内容
- 支持获取收藏商品的价格和库存信息

## 请求地址

```
{域名地址}/api/favorite/list
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/favorite/list`

## 请求语法

```
GET {域名地址}/api/favorite/list
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :------------------- | :------- | :--- | :---------------------- |
| current | int | 否 | 当前页码，默认为1 |
| pageSize | int | 否 | 每页显示数量，默认为20 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object[] | 收藏的文档列表 |
| total | int | 收藏总数量 |

#### data 数组元素参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
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
| extra | object | 文档扩展字段 |
| link | string | 文档链接 |

## 使用示例

### 请求示例

```
GET /api/favorite/list?current=1&pageSize=10 HTTP/1.1
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
      "created_time": 1607308159,
      "updated_time": 1662717106,
      "title": "关于AICMS",
      "seo_title": "",
      "url_token": "design",
      "keywords": "",
      "description": "AI内容管理系统(AICMS)，是一款使用 GoLang 开发的企业站内容管理系统，它部署简单，软件安全，界面优雅，小巧，执行速度飞快，使用 AICMS 搭建的网站可以防止众多安全问题发生。",
      "module_id": 1,
      "category_id": 1,
      "views": 1338,
      "comment_count": 0,
      "images": null,
      "template": "",
      "status": 1,
      "canonical_url": "",
      "fixed_link": "",
      "flag": "",
      "user_id": 0,
      "price": 0,
      "stock": 9999999,
      "has_pseudo": 0,
      "keyword_id": 0,
      "origin_url": "",
      "origin_title": "",
      "category": null,
      "module_name": "",
      "data": null,
      "logo": "https://www.aicms.com/uploads/202012/7/bd36c37ef742c7be.webp",
      "thumb": "https://www.aicms.com/uploads/202012/7/thumb_bd36c37ef742c7be.webp",
      "extra": {
        "author": {
          "name": "作者",
          "value": "AICMS",
          "default": null
        },
        "certificate": {
          "name": "学历",
          "value": null,
          "default": null
        },
        "city": {
          "name": "城市",
          "value": null,
          "default": null
        }
      },
      "link": "https://www.aicms.com/design"
    },
    {
      "id": 2,
      "created_time": 1607308247,
      "updated_time": 1611373941,
      "title": "AICMS使用帮助",
      "seo_title": "",
      "url_token": "help",
      "keywords": "",
      "description": "AICMS常见问题汇总",
      "module_id": 1,
      "category_id": 1,
      "views": 1655,
      "comment_count": 0,
      "images": null,
      "template": "",
      "status": 1,
      "canonical_url": "",
      "fixed_link": "",
      "flag": "",
      "user_id": 0,
      "price": 0,
      "stock": 9999999,
      "has_pseudo": 0,
      "keyword_id": 0,
      "origin_url": "",
      "origin_title": "",
      "category": null,
      "module_name": "",
      "data": null,
      "logo": "https://www.aicms.com/uploads/202012/7/bd36c37ef742c7be.webp",
      "thumb": "https://www.aicms.com/uploads/202012/7/thumb_bd36c37ef742c7be.webp",
      "extra": null,
      "link": "https://www.aicms.com/help"
    }
  ],
  "total": 2
}
```

### 错误代码

| 错误码 | 说明 |
| :----- | :-------------------------- |
| 0 | OK |
| -1 | 错误，错误原因在 msg 中指出 |
| 1001 | 未登录 |
| 1002 | 未授权 |
| 200 | API 请求 OK |
# 获取下一个文档接口

获取指定文档的下一个文档信息，通常用于文档详情页的上下篇导航功能。如果指定文档是最后一个文档，则返回空结果。

## 注意事项

- 接口按照文档 ID 顺序查找下一个文档
- 当指定文档为最后一个文档时，返回的 data 为 null
- 仅返回文档的基本信息，不包含文档内容详情
- 接口会返回同分类下的下一个文档

## 请求地址

```
{域名地址}/api/archive/next
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/archive/next`

## 请求语法

```
GET {域名地址}/api/archive/next?{参数}
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明    |
| :----- | :--- | :--- | :------ |
| id     | int  | 是   | 文档 ID |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型   | 说明         |
| :----- | :----- | :----------- |
| code   | int    | 错误码       |
| msg    | string | 错误原因说明 |
| data   | object | 结果内容     |

#### data 参数

| 字段名        | 类型     | 说明                                                                   |
| :------------ | :------- | :--------------------------------------------------------------------- |
| id            | int      | 文档 ID                                                                |
| title         | string   | 文档标题                                                               |
| seo_title     | string   | 文档 SEO 标题                                                          |
| url_token     | string   | 文档 URL 别名                                                          |
| keywords      | string   | 文档关键词                                                             |
| description   | string   | 文档简介                                                               |
| module_id     | int      | 文档模型 ID                                                            |
| category_id   | int      | 文档分类 ID                                                            |
| views         | int      | 文档浏览量                                                             |
| comment_count | int      | 文档评论量                                                             |
| images        | string[] | 文档组图                                                               |
| logo          | string   | 文档 Logo                                                              |
| thumb         | string   | 文档缩略图                                                             |
| flag          | string   | 文档推荐属性，头条[h]推荐[c]幻灯[f]特荐[a]滚动[s]加粗[h]图片[p]跳转[j] |
| canonical_url | string   | canonical url                                                          |
| fixed_link    | string   | 文档固定链接                                                           |
| created_time  | int      | 文档发布时间戳                                                         |
| updated_time  | int      | 文档更新时间戳                                                         |
| status        | int      | 文档显示状态                                                           |
| user_id       | int      | 用户 ID                                                                |
| price         | int      | 价格，单位分                                                           |
| stock         | int      | 库存量                                                                 |
| user_id       | int      | 用户 ID                                                                |

## 使用示例

### 请求示例

```
GET /api/archive/next?id=3 HTTP/1.1
Host: your-domain.com
Content-Type: application/json
```

### 响应示例

```json
{
    "code": 0,
    "data": {
        "id": 3,
        "created_time": 1607308858,
        "updated_time": 1611373923,
        "title": "AICMS使用帮助",
        "seo_title": "",
        "url_token": "help",
        "keywords": "",
        "description": "AICMS使用帮助",
        "module_id": 1,
        "category_id": 1,
        "views": 1256,
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
        "logo": "https://www.aicms.com/uploads/20225/27/5cd9e65be13cbe6b.webp",
        "thumb": "https://www.aicms.com/uploads/20225/27/5cd9e65be13cbe6b.webp",
        "link": "https://www.aicms.com/help"
    },
    "msg": ""
}
```

当前文档为最后一个文档时：
```json
{
    "code": 0,
    "data": null,
    "msg": ""
}
```

### 错误代码

| 错误码 | 说明                        |
| :----- | :-------------------------- |
| 0      | OK                          |
| -1     | 错误，错误原因在 msg 中指出 |
| 1001   | 未登录                      |
| 1002   | 未授权                      |
| 200    | API 请求 OK                 |

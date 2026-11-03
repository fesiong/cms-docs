# 获取单页列表接口

获取所有单页的列表信息，返回系统中所有已发布的单页内容。

## 注意事项

- 该接口采用GET方法
- 不需要任何请求参数
- 返回所有已发布状态的单页列表
- 包含单页的基本信息、SEO信息和内容摘要

## 请求地址

```
{域名地址}/api/page/list
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/page/list`

## 请求语法

```
GET {域名地址}/api/page/list
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

无

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object[] | 单页列表数组 |

#### data 结果 item 参数

| 字段名 | 类型 | 说明 |
| :------------------- | :------- | :---------------------- |
| id | int | 单页ID |
| title | string | 单页名称 |
| seo_title | string | 单页SEO标题 |
| url_token | string | 单页URL别名 |
| keywords | string | 单页关键词 |
| description | string | 单页简介 |
| content | string | 单页内容详情 |
| type | int | 单页属性值，1 单页，3 单页面 |
| sort | int | 单页排序值 |
| images | string[] | 单页Banner图 |
| logo | string | 单页Logo |
| thumb | string | 单页缩略图 |
| created_time | int | 单页发布时间戳 |
| updated_time | int | 单页更新时间戳 |
| status | int | 单页显示状态 |

## 使用示例

### 请求示例

```
GET /api/page/list HTTP/1.1
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
      "updated_time": 1657761249,
      "title": "关于AICMS",
      "seo_title": "",
      "keywords": "",
      "url_token": "about",
      "description": "关于AICMS的介绍",
      "content": "<p>AICMS是一个内容管理系统...</p>",
      "type": 3,
      "sort": 1,
      "images": [],
      "logo": "",
      "status": 1,
      "thumb": "https://www.aicms.com/uploads/202012/7/bd36c37ef742c7be.webp"
    },
    {
      "id": 2,
      "created_time": 1607308159,
      "updated_time": 1657761249,
      "title": "联系AICMS",
      "seo_title": "",
      "keywords": "",
      "url_token": "contact",
      "description": "联系AICMS的方式",
      "content": "<p>联系我们的方式...</p>",
      "type": 3,
      "sort": 2,
      "images": [],
      "logo": "",
      "status": 1,
      "thumb": "https://www.aicms.com/uploads/202012/7/bd36c37ef742c7be.webp"
    }
  ]
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
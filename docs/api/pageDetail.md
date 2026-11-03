# 获取单页详情接口

获取单页内容的详细信息，支持通过单页ID或URL别名获取单页内容。

## 注意事项

- 该接口采用GET方法
- 支持通过ID或filename参数获取单页内容
- 返回单页的完整信息，包括标题、内容、SEO信息等
- 只返回已发布状态的单页内容（status为1）

## 请求地址

```
{域名地址}/api/page/detail
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/page/detail`

## 请求语法

```
GET {域名地址}/api/page/detail
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :------------------- | :------- | :--- | :---------------------- |
| id | int | 是 | 单页ID，如果传了filename，可以不用传ID |
| filename | string | 否 | 单页URL别名，单页ID、filename二选一 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object | 单页详细信息对象 |

#### data 结果参数

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

### 请求示例（通过ID获取）

```
GET /api/page/detail?id=1 HTTP/1.1
Host: www.aicms.com
```

### 请求示例（通过filename获取）

```
GET /api/page/detail?filename=help HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "id": 1,
    "created_time": 1607308159,
    "updated_time": 1657761249,
    "title": "AICMS使用帮助",
    "seo_title": "",
    "keywords": "",
    "url_token": "help",
    "description": "",
    "content": "<p><br/></p>",
    "type": 3,
    "sort": 1,
    "images": [],
    "logo": "",
    "status": 1,
    "thumb": "https://www.aicms.com/uploads/202012/7/bd36c37ef742c7be.webp"
  }
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
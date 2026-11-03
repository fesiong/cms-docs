# 检查文档存在接口

检查指定文档是否已存在于系统中，通过文档ID、标题、URL别名或原始URL来验证文档是否存在，返回文档的基本信息。

## 注意事项

- 该接口采用GET方法，参数通过URL查询字符串传递
- 需要在URL中提供有效的token参数进行身份验证
- 必须提供id、title、url_token、origin_url中的任意一个参数
- 用于在导入文档前检查文档是否已存在
- 返回已存在文档的基本信息，包括ID、标题和链接

## 请求地址

```
{域名地址}/api/import/archive?token={token}&id={id}
```

说明：`{域名地址}` 需要替换成你的域名地址，`{token}` 需要更换为后台内容导入接口功能里的Token，如 `https://www.aicms.com/api/import/archive?token=xxx`

## 请求语法

```
GET {域名地址}/api/import/archive?token={token}&[id|title|url_token|origin_url]={value}
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

#### URL参数

| 字段名 | 类型 | 必填 | 说明 |
| :------------------- | :------- | :--- | :---------------------- |
| token | string | 是 | 后台内容导入接口功能里的Token |
| id | int | 否 | 文档ID，id、title、url_token、origin_url必须传一个 |
| title | string | 否 | 文档标题，id、title、url_token、origin_url必须传一个 |
| url_token | string | 否 | 文档URL别名，id、title、url_token、origin_url必须传一个 |
| origin_url | string | 否 | 文档原始URL，id、title、url_token、origin_url必须传一个 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object | 返回数据内容 |

#### data 参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :------- |
| id | int | 文档ID |
| title | string | 文档标题 |
| link | string | 文档URL |

## 使用示例

### 通过文档ID查询请求示例

```
GET /api/import/archive?token=4712a54b4c456bb29b7816d241db69a7&id=1 HTTP/1.1
Host: www.aicms.com
```

### 通过文档标题查询请求示例

```
GET /api/import/archive?token=4712a54b4c456bb29b7816d241db69a7&title=欢迎使用AICMS HTTP/1.1
Host: www.aicms.com
```

### 通过URL别名查询请求示例

```
GET /api/import/archive?token=4712a54b4c456bb29b7816d241db69a7&url_token=AICMS HTTP/1.1
Host: www.aicms.com
```

### 通过原始URL查询请求示例

```
GET /api/import/archive?token=4712a54b4c456bb29b7816d241db69a7&origin_url=https://example.com/article/1 HTTP/1.1
Host: www.aicms.com
```

### 文档存在响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "id": 1,
    "title": "欢迎使用AICMS",
    "link": "https://www.aicms.com/AICMS"
  }
}
```

### 文档不存在响应示例

```json
{
  "code": -1,
  "msg": "文档不存在",
  "data": null
}
```

### 错误响应示例

```json
{
  "code": -1,
  "msg": "缺少必要参数",
  "data": null
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
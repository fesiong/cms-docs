# 导入文档接口

通过API接口批量导入文档内容，支持文档标题、内容、分类、关键词、缩略图等完整信息的导入，可实现内容的批量迁移和发布。

## 注意事项

- 该接口采用POST方法，使用form-data格式提交数据
- 需要在URL中提供有效的token参数进行身份验证
- 必须提供文档标题、内容和分类ID
- 支持自定义URL别名、关键词、描述、缩略图等完整文档信息
- 支持文档组图上传，最多可设置9张图片
- 可设置文档发布时间，支持定时发布功能
- 支持文档Tag标签设置，多个标签用英文逗号分隔
- 可选择是否保存为草稿或覆盖已存在的文档

## 请求地址

```
{域名地址}/api/import/archive?token={token}
```

说明：`{域名地址}` 需要替换成你的域名地址，`{token}` 需要更换为后台内容导入接口功能里的Token，如 `https://www.aicms.com/api/import/archive?token=xxx`

## 请求语法

```
POST {域名地址}/api/import/archive?token={token}
Content-Type: multipart/form-data
```

## 请求头

| 字段名 | 类型 | 必填 | 说明 |
| :------------------- | :------- | :--- | :---------------------- |
| Content-Type | string | 是 | 必须设置为 multipart/form-data |

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

#### URL参数

| 字段名 | 类型 | 必填 | 说明 |
| :------------------- | :------- | :--- | :---------------------- |
| token | string | 是 | 后台内容导入接口功能里的Token |

#### 表单参数

| 字段名 | 类型 | 必填 | 说明 |
| :------------------- | :------- | :--- | :---------------------- |
| id | int | 否 | 文档ID，默认自动生成 |
| title | string | 是 | 文档标题 |
| content | string | 是 | 文档内容 |
| category_id | int | 是 | 文档分类ID |
| keywords | string | 否 | 文档关键词 |
| description | string | 否 | 文档简介，250字以内 |
| url_token | string | 否 | 自定义URL别名，仅支持数字、英文字母 |
| logo | string | 否 | 文档的缩略图，可以是绝对地址或相对地址 |
| images[] | string | 否 | 文章组图，可以设置最多9张图片，多张请重复这个字段 |
| publish_time | string | 否 | 文档的发布时间，格式：2006-01-02 15:04:05，可以是未来的时间实现定时发布 |
| tag | string | 否 | 文档Tag标签，多个tag用英文逗号分隔，例如：aaa,bbb,ccc |
| draft | boolean | 否 | 是否存入到草稿，true:保存到草稿，false:直接发布 |
| cover | int | 否 | 当相同标题、ID文档存在时是否覆盖，0:不覆盖并提示错误，1:覆盖成最新内容，2:不做判断 |

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
| url | string | 文档URL |

## 使用示例

### 请求示例

```
POST /api/import/archive?token=4712a54b4c456bb29b7816d241db69a7 HTTP/1.1
Host: www.aicms.com
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="title"

欢迎使用AICMS
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="content"

<p>欢迎使用AICMS，这是一款使用GoLang开发的企业站内容管理系统</p>
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="category_id"

2
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="keywords"

AICMS,内容管理,网站系统
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="description"

AI内容管理系统(AICMS)是一款优秀的企业站内容管理系统
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="images[]"

https://www.aicms.com/static/default/images/logo.png
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```

### 带自定义字段的请求示例

```
POST /api/import/archive?token=4712a54b4c456bb29b7816d241db69a7 HTTP/1.1
Host: www.aicms.com
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="title"

产品介绍
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="content"

<p>这是产品详细介绍内容</p>
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="category_id"

1
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="price"

999
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="stock"

100
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```

### 成功响应示例

```json
{
  "code": 0,
  "msg": "发布成功",
  "data": {
    "id": 1,
    "url": "https://www.aicms.com/AICMS"
  }
}
```

### 覆盖模式成功响应示例

```json
{
  "code": 0,
  "msg": "文档已更新",
  "data": {
    "id": 1,
    "url": "https://www.aicms.com/AICMS"
  }
}
```

### 错误响应示例

```json
{
  "code": -1,
  "msg": "分类ID不存在",
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
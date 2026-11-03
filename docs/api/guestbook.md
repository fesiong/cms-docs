# 添加留言接口

添加用户留言信息，支持用户名、留言内容、联系方式等基本信息，以及自定义表单字段的提交。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 用户名字段为必填项
- 支持自定义留言表单字段
- 留言内容和联系方式为可选字段
- 提交后系统会返回操作结果信息
- 可用于网站的留言簿或反馈表单功能

## 请求地址

```
{域名地址}/api/guestbook.html
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/guestbook.html`

## 请求语法

```
POST {域名地址}/api/guestbook.html
Content-Type: application/json
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :------------------- | :------- | :--- | :---------------------- |
| user_name | string | 是 | 用户名 |
| content | string | 否 | 留言内容 |
| contact | string | 否 | 联系方式 |
| 自定义字段 | string | 否 | 留言表单中自定义的字段 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |

## 使用示例

### 请求示例

```
POST /api/guestbook.html HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "user_name": "AICMS",
  "content": "欢迎使用AICMS",
  "contact": "13888888888"
}
```

### 带自定义字段的请求示例

```
POST /api/guestbook.html HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "user_name": "AICMS",
  "content": "欢迎使用AICMS",
  "contact": "13888888888",
  "email": "example@aicms.com",
  "subject": "产品咨询"
}
```

### 成功响应示例

```json
{
  "code": 0,
  "msg": "感谢您的留言！"
}
```

### 失败响应示例

```json
{
  "code": -1,
  "msg": "用户名不能为空"
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
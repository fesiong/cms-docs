# 发送Email验证接口

向指定邮箱地址发送验证邮件，邮件中包含验证链接，用户点击链接完成邮箱验证。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 该接口用于向指定邮箱发送验证邮件
- 邮件中包含验证链接，用户点击后完成验证
- 支持多种验证场景（邮箱验证、重置密码等）
- 需要提供有效的邮箱地址和验证状态
- 邮件发送成功后会返回成功信息，但不保证用户一定会收到邮件

## 请求地址

```
{域名地址}/api/verify/email
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/verify/email`

调用该接口后，系统会向指定的邮箱地址发送一封邮件，邮件内包含验证码，用户点击邮件中的链接，即可完成邮箱验证。

## 请求语法

```
POST /api/verify/email
Content-Type: application/json
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

## 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :--- | :--- | :--- | :--- |
| email | string | 否 | 邮件地址 |
| state | string | 否 | state值，verify = 验证邮箱是否有效，reset = 重置密码，其他值未做判断 |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

## 返回参数

| 字段名 | 类型 | 说明 |
| :--- | :--- | :--- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |

## 使用示例

### 请求示例

```
POST /api/verify/email HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "email": "test@example.com",
  "state": "verify"
}
```

### 响应示例

```json
{
  "code": 0,
  "msg": "已发送邮件"
}
```

## 错误码

| 错误码 | 说明 |
| :--- | :--- |
| 0 | OK |
| -1 | 错误，错误原因在 msg 中指出 |
| 1001 | 未登录 |
| 1002 | 未授权 |
| 200 | API 请求 OK |
# 重置用户密码接口

通过邮箱验证的方式重置用户密码，用户需要提供邮箱地址、新密码以及验证令牌和验证码。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 目前只能通过邮箱方式重置用户密码
- 需要配合邮箱发送邮件功能使用，用户需要先获取验证链接
- 需要提供邮箱发送的验证token和code值
- 新密码需要符合系统密码强度要求
- 验证信息有有效期限制，过期后需要重新发送验证邮件

## 请求地址

```
{域名地址}/api/password/reset
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/password/reset`

## 请求语法

```
POST {域名地址}/api/password/reset
Content-Type: application/json
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :----- | :----- | :--- | :--- |
| email | string | 是 | 用户注册的邮箱地址 |
| password | string | 是 | 新密码，需要符合密码强度要求 |
| token | string | 是 | 发送到邮箱的链接中的token值，用于验证身份 |
| code | string | 是 | 发送到邮箱的链接中的code值，用于验证身份 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |

## 使用示例

### 请求示例

```
POST /api/password/reset HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "email": "AICMS@qq.com",
  "password": "NewPassword123",
  "token": "abc123def456",
  "code": "789xyz"
}
```

### 响应示例

#### 成功响应
```json
{
  "code": 0,
  "msg": "密码重置成功"
}
```

#### 验证失败响应
```json
{
  "code": -1,
  "msg": "验证信息无效或已过期"
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
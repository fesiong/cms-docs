# 修改用户密码接口

修改当前登录用户的密码，需要验证原密码的正确性后才能更新为新密码。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 需要提供原密码和新密码
- 需要用户已登录，通过会话或Token验证身份
- 新密码需要满足安全要求（如长度、复杂度等）
- 修改成功后可能需要重新登录

## 请求地址

```
{域名地址}/api/user/password
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/user/password`

## 请求语法

```
POST {域名地址}/api/user/password
Content-Type: application/json
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :------------------- | :------- | :--- | :---------------------- |
| old_password | string | 是 | 旧密码 |
| password | string | 是 | 新密码，需要满足安全策略要求 |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |

## 使用示例

### 正常请求示例

```
POST /api/user/password HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "old_password": "123456",
  "password": "newPassword123!"
}
```

### 正常响应示例

```json
{
  "code": 0,
  "msg": "密码修改成功"
}
```

### 错误请求示例 - 原密码错误

```
POST /api/user/password HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "old_password": "wrong_password",
  "password": "newPassword123!"
}
```

### 错误响应示例 - 原密码错误

```json
{
  "code": -1,
  "msg": "原密码错误"
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
| 2001 | 原密码错误 |
| 2002 | 新密码不符合安全要求 |
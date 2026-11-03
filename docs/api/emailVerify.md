# 验证Email地址接口

验证邮箱地址的有效性，支持邮箱验证和重置密码等不同场景的验证。

## 注意事项

- 该接口用于验证邮箱地址的有效性
- 支持多种验证场景（邮箱验证、重置密码等）
- 通过token和code参数确保请求来源的有效性
- 支持返回json或html格式的数据
- 验证成功后会根据state参数执行相应操作
- 需要确保域名地址正确配置

## 请求地址

```
{域名地址}/api/verify/email
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/verify/email`

## 请求语法

```
GET /api/verify/email
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

## 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :--- | :--- | :--- | :--- |
| token | string | 否 | token 值，校验是否来有效来源 |
| code | string | 否 | code值，校验是否来有效来源 |
| email | string | 否 | 邮件地址 |
| state | string | 否 | state值，verify = 验证邮箱是否有效，reset = 重置密码，其他值未做判断，exist=邮箱是否已存在 |
| return | string | 否 | 返回数据格式，json 或 html，默认为 json |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

## 返回参数

根据请求参数的return值返回不同格式的数据：
- 当return=json时，返回JSON格式数据
- 当return=html时，返回HTML格式数据

### JSON格式返回参数

| 字段名 | 类型 | 说明 |
| :--- | :--- | :--- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |

## 使用示例

### 请求示例

```
GET /api/verify/email?token=abc123&code=xyz789&email=test@example.com&state=verify&return=json HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "msg": "验证通过"
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
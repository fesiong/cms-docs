# 获取谷歌登录跳转地址接口

获取谷歌OAuth登录的跳转地址，用于实现第三方登录功能，返回完整的谷歌授权URL供用户跳转登录。

## 注意事项

- 该接口采用GET方法，参数通过URL查询字符串传递
- 用于实现谷歌OAuth第三方登录功能
- 支持自定义state参数，用于防止CSRF攻击
- 如果不提供state参数，系统会自动生成
- 返回的URL包含完整的授权参数，用户访问后可跳转至谷歌登录页面
- 需要在后台配置谷歌开发者账户的相关参数

## 请求地址

```
{域名地址}/api/google/url
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/google/url`

完整的使用方法，参阅[AICMS谷歌登录配置教程](https://www.aicms.com/plugin/10499.html)

## 请求语法

```
GET {域名地址}/api/google/url
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :------------------- | :------- | :--- | :---------------------- |
| state | string | 否 | 登录跳转地址的state参数，不填会自动生成 |

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
| :----- | :----- | :------------------------------------- |
| state | string | 登录跳转地址的state值 |
| url | string | 完整的谷歌授权跳转地址 |

## 使用示例

### 请求示例

```
GET /api/google/url?state=custom-state-value HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "state": "custom-state-value",
    "url": "https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=your-client-id&redirect_uri=https://www.aicms.com/api/google/callback&scope=https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile&state=custom-state-value"
  }
}
```

### 不带state参数的请求示例

```
GET /api/google/url HTTP/1.1
Host: www.aicms.com
```

### 不带state参数的响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "state": "auto-generated-state-12345",
    "url": "https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=your-client-id&redirect_uri=https://www.aicms.com/api/google/callback&scope=https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile&state=auto-generated-state-12345"
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
# 微信官方授权接口

微信网页授权登录接口，用于在微信环境中实现用户授权登录功能，支持获取用户基本信息和下发验证码。

## 注意事项

- 该接口采用GET方法，是一个跳转接口
- 需要在微信内置浏览器中访问才能正常工作
- 会先跳转到微信官方授权页面，用户授权后返回
- 当state参数为code时，会向用户微信下发验证码
- 需要预先配置微信公众号授权回调域名

## 请求地址

```
{域名地址}/api/wechat/auth
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/wechat/auth`

## 请求语法

```
GET {域名地址}/api/wechat/auth
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :------------------- | :------- | :--- | :---------------------- |
| state | string | 否 | 状态参数，当值为 `code` 时会下发验证码到微信公众号窗口，其他值无特殊功能 |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

此接口会跳转到微信授权页面，授权完成后会在前端显示弹窗结果：
- 正常情况：显示授权成功信息
- state=code时：会向用户微信下发验证码并显示提示信息
- 错误情况：显示错误信息弹窗

## 使用示例

### 正常授权请求示例

```
GET /api/wechat/auth?state=default HTTP/1.1
Host: www.aicms.com
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) MicroMessenger/8.0.0
```

### 获取验证码请求示例

```
GET /api/wechat/auth?state=code HTTP/1.1
Host: www.aicms.com
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) MicroMessenger/8.0.0

```

### 授权成功响应示例

```
HTTP/1.1 302 Found
Location: https://open.weixin.qq.com/connect/oauth2/authorize?appid=APPID&redirect_uri=REDIRECT_URI&response_type=code&scope=SCOPE&state=STATE#wechat_redirect
```

### 错误响应示例

```json
{
  "code": -1,
  "msg": "微信授权失败"
}
```

### 错误代码

| 错误码 | 说明 |
| :----- | :-------------------------- |
| 0 | 授权成功 |
| -1 | 授权失败，错误原因在 msg 中指出 |
| 1001 | 未登录 |
| 1002 | 未授权 |
| 200 | API 请求 OK |
| 4001 | 不是在微信中打开 |
| 4002 | 微信授权参数错误 |
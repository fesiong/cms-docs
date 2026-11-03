# 登录接口

用户登录接口，支持多种登录方式，包括网站登录、微信登录、Google登录等，用于验证用户身份并返回登录凭证。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 支持多种平台登录，包括网站、微信、QQ、Google等
- 网站登录需要用户名和密码
- 微信登录需要提供相应用户信息和凭证
- Google登录需要通过OAuth流程获取code
- 登录成功后返回用户信息和登录token
- 支持记住登录状态功能

## 请求地址

```
{域名地址}/api/login
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/login`

## 请求语法

```
POST {域名地址}/api/login
Content-Type: application/json
```

## 请求参数

| 字段名          | 类型    | 必填 | 说明                                                                                         |
| :-------------- | :------ | :--- | :------------------------------------------------------------------------------------------- |
| platform        | string  | 是   | 登录方式，默认值为 website，可选值有：tt、swan、alipay、qq、weapp、wechat、inwechat、google、website |
| code            | string  | 否   | 微信、Google的临时凭证，或者是验证码                                                                   |
| anonymousCode   | string  | 否   | 微信用户信息，platform=wechat/weapp 有效                                                    |
| avatar          | string  | 否   | 微信用户信息，platform=wechat/weapp 有效                                                     |
| nick_name       | string  | 否   | 微信用户信息，platform=wechat/weapp 有效                                                     |
| gender          | string  | 否   | 微信用户信息，platform=wechat/weapp 有效                                                     |
| province        | string  | 否   | 微信用户信息，platform=wechat/weapp 有效                                                     |
| city            | string  | 否   | 微信用户信息，platform=wechat/weapp 有效                                                     |
| county          | string  | 否   | 微信用户信息，platform=wechat/weapp 有效                                                     |
| encryptedData   | string  | 否   | 微信用户信息，platform=wechat/weapp 有效                                                     |
| iv              | string  | 否   | 微信用户信息，platform=wechat/weapp 有效                                                     |
| signature       | string  | 否   | 微信用户信息，platform=wechat/weapp 有效                                                     |
| rawData         | string  | 否   | 微信用户信息，platform=wechat/weapp 有效                                                     |
| remember        | boolean | 否   | 是否记住用户，platform=website 有效                                                          |
| user_name       | string  | 否   | 用户名，platform=website 有效                                                                |
| password        | string  | 否   | 密码，platform=website 有效                                                                  |
| captcha_id      | string  | 否   | 图形验证码 ID，platform=website 有效                                                         |
| captcha         | string  | 否   | 图形验证码值，platform=website 有效                                                          |

## 返回参数

| 字段名 | 类型   | 说明         |
| :----- | :----- | :----------- |
| code   | int    | 错误码       |
| msg    | string | 错误原因说明 |
| data   | object | 结果内容     |

### data 参数

| 字段名         | 类型   | 说明             |
| :------------- | :----- | :--------------- |
| id             | int    | 用户 ID          |
| parent_id      | int    | 上级用户 ID      |
| user_name      | string | 用户名           |
| real_name      | string | 真实姓名         |
| avatar_url     | string | 用户头像地址     |
| email          | string | email 地址       |
| phone          | string | 手机号           |
| group_id       | int    | 用户组 ID        |
| is_retailer    | int    | 是否是分销员     |
| balance        | int    | 用户余额         |
| total_reward   | int    | 分销员累计收益   |
| invite_code    | string | 用户邀请码       |
| last_login     | int    | 最近一次登录时间 |
| expire_time    | int    | 过期时间         |
| created_time   | int    | 注册时间戳       |
| updated_time   | int    | 更新时间戳       |
| status         | int    | 显示状态         |
| token          | string | 登录凭证         |

## 使用示例

### 网站登录请求示例

```
POST /api/login HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "platform": "website",
  "user_name": "admin",
  "password": "123456",
  "remember": false
}
```

### 微信登录请求示例

```
POST /api/login HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "platform": "wechat",
  "code": "wechat_code",
  "avatar": "https://example.com/avatar.jpg",
  "nick_name": "微信用户",
  "gender": "1",
  "province": "广东",
  "city": "深圳",
  "county": "南山区",
  "encryptedData": "encrypted_data",
  "iv": "iv_value",
  "signature": "signature_value",
  "rawData": "raw_data"
}
```

### Google登录请求示例

```
POST /api/login HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "platform": "google",
  "state": "your-generated-state-value",
  "code": "google-auth-code"
}
```

#### Google登录完整流程

1. 首先获取谷歌登录跳转URL：
```
GET /api/google/url?state=your-state-value HTTP/1.1
Host: www.aicms.com
```

2. 跳转到返回的谷歌授权URL，用户完成授权后会被重定向到回调地址

3. 在回调页面获取授权code，调用登录接口：
```
POST /api/login HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "platform": "google",
  "state": "your-state-value",
  "code": "authorization-code-from-google"
}
```

### 前端Google登录实现示例

```javascript
// 点击谷歌登录按钮时触发
$('#login-google-btn').click(function() {
  $.get("/api/google/url").then(res => {
    if (res.data) {
      // 保存state值，用于后续验证
      sessionStorage.setItem('state', res.data.state);
      // 跳转到谷歌授权页面
      window.location.href = res.data.url;
    }
  }, 'json');
});

// 检查URL中是否有code参数（授权回调时）
if (window.location.href.indexOf('code') > -1) {
  // 获取URL参数中的code和state
  var urlParams = new URLSearchParams(window.location.search);
  var code = urlParams.get('code');
  var state = urlParams.get('state');
  
  // 调用登录接口完成登录
  $.ajax({
    type: 'POST',
    url: '/api/login',
    data: JSON.stringify({
      platform: "google",
      "state": state,
      "code": code,
    }),
    contentType: "application/json",
    dataType: 'json',
    success: function (res) {
      if (res.code === 0) {
        console.log('Google登录成功', res);
        // 登录成功后的处理
        window.location.href = '/dashboard'; // 跳转到用户中心
      } else {
        console.error('Google登录失败', res.msg);
      }
    },
    error: function(xhr, status, error) {
      console.error('网络错误', error);
    }
  });
}
```

### 响应示例

```json
{
  "code": 0,
  "data": {
    "id": 1000,
    "created_time": 1669012062,
    "updated_time": 1679536756,
    "parent_id": 0,
    "user_name": "admin",
    "real_name": "",
    "avatar_url": "uploads/202211/21/14f56760596b5328.webp",
    "email": "",
    "phone": "",
    "group_id": 2,
    "status": 1,
    "is_retailer": 0,
    "balance": 0,
    "total_reward": 0,
    "invite_code": "AICMS",
    "last_login": 1702912236,
    "expire_time": 1997404800,
    "extra": null,
    "token": "eyJhbGI1NiZXJJZUwNnVCI6IjEwMDAifQ.pLmYPvSajEWrF0FaUGDciOiJIUzIzNiIsILLZBCRm8fYewv49agxlTA26DwIsInR5cCI6IkpXVCJ9.eyJ0IjoiMTcwNTz",
    "group": null,
    "full_avatar_url": "",
    "link": ""
  },
  "msg": ""
}
```

### 错误响应示例

```json
{
  "code": -1,
  "msg": "用户名或密码错误"
}
```

### 错误代码

| 错误码 | 说明                        |
| :----- | :-------------------------- |
| 0      | OK                          |
| -1     | 错误，错误原因在 msg 中指出 |
| 1001   | 未登录                      |
| 1002   | 未授权                      |
| 200    | API 请求 OK                 |
# 注册接口

用户注册接口，用于创建新用户账户。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 支持多种注册方式，可使用用户名密码或手机号验证码注册
- 可能需要图形验证码验证
- 注册成功后返回用户信息和登录凭证
- 用户名、邮箱或手机号需唯一

## 请求地址

```
{域名地址}/api/register
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/register`

## 请求语法

```
POST {域名地址}/api/register
Content-Type: application/json
```

## 请求头

| 字段名 | 类型 | 必填 | 说明 |
| :---------------- | :------ | :--- | :-------------------- |
| Content-Type | string | 是 | 固定值：application/json |

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :------------------- | :------- | :--- | :---------------------- |
| user_name | string | 否 | 用户名 |
| password | string | 否 | 密码 |
| captcha_id | string | 否 | 图形验证码ID |
| captcha | string | 否 | 图形验证码值 |
| real_name | string | 否 | 真实姓名 |
| avatar_url | string | 否 | 头像地址 |
| email | string | 否 | 邮箱 |
| phone | string | 否 | 手机号 |
| code | string | 否 | 验证码（手机验证码） |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object | 用户信息和登录凭证 |

#### data 结果参数

| 字段名 | 类型 | 说明 |
| :------------------- | :------- | :---------------------- |
| id | int | 用户ID |
| parent_id | int | 上级用户ID |
| user_name | string | 用户名 |
| real_name | string | 真实姓名 |
| avatar_url | string | 用户头像地址 |
| email | string | 邮箱地址 |
| phone | string | 手机号 |
| group_id | int | 用户组ID |
| is_retailer | int | 是否是分销员 |
| balance | int | 用户余额 |
| total_reward | int | 分销员累计收益 |
| invite_code | string | 用户邀请码 |
| last_login | int | 最近一次登录时间戳 |
| expire_time | int | 过期时间戳 |
| created_time | int | 注册时间戳 |
| updated_time | int | 更新时间戳 |
| status | int | 用户显示状态 |
| token | string | 登录凭证（JWT token） |

## 使用示例

### 请求示例（用户名密码注册）

```
POST /api/register HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "user_name": "newuser",
  "password": "MyPassword123",
  "real_name": "新用户",
  "email": "newuser@example.com",
  "captcha_id": "captcha123",
  "captcha": "abcd"
}
```

### 请求示例（手机号验证码注册）

```
POST /api/register HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "phone": "13800138000",
  "code": "123456",
  "password": "MyPassword123",
  "real_name": "新用户",
  "captcha_id": "captcha123",
  "captcha": "abcd"
}
```

### 响应示例

```json
{
  "code": 0,
  "msg": "注册成功",
  "data": {
    "id": 1000,
    "created_time": 1669012062,
    "updated_time": 1679536756,
    "parent_id": 0,
    "user_name": "newuser",
    "real_name": "新用户",
    "avatar_url": "uploads/202211/21/14f56760596b5328.webp",
    "email": "newuser@example.com",
    "phone": "13800138000",
    "group_id": 2,
    "status": 1,
    "is_retailer": 0,
    "balance": 0,
    "total_reward": 0,
    "invite_code": "AICMS",
    "last_login": 1702912236,
    "expire_time": 1997404800,
    "extra": null,
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
    "group": null,
    "full_avatar_url": "",
    "link": ""
  }
}
```

### 错误代码

| 错误码 | 说明 |
| :----- | :-------------------------- |
| 0 | OK（注册成功） |
| -1 | 错误，错误原因在 msg 中指出 |
| 1001 | 未登录 |
| 1002 | 未授权 |
| 200 | API 请求 OK |
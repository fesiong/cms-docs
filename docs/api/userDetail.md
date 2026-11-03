# 获取用户详情接口

获取指定用户的基本信息和账户详情，包括用户名、联系方式、账户状态、余额等用户相关数据。

## 注意事项

- 该接口采用GET方法
- 需要提供目标用户的ID来查询用户详情
- 根据用户权限，可能只能查看自己的信息或有权限查看的用户信息
- 返回用户的基本信息和账户相关信息

## 请求地址

```
{域名地址}/api/user/detail
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/user/detail`

## 请求语法

```
GET {域名地址}/api/user/detail
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :----- | :----- | :--- | :--- |
| userId | int | 是 | 用户ID，指定要查询的用户 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object | 用户详情数据 |

#### data 参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| id | int | 用户ID |
| parent_id | int | 上级用户ID |
| user_name | string | 用户名 |
| real_name | string | 真实姓名 |
| introduce | string | 个人介绍 |
| avatar_url | string | 用户头像相对地址 |
| full_avatar_url | string | 用户头像完整地址 |
| email | string | 邮箱地址 |
| phone | string | 手机号码 |
| group_id | int | 用户组ID |
| is_retailer | int | 是否是分销员，0-否，1-是 |
| balance | int | 用户余额 |
| total_reward | int | 分销员累计收益 |
| invite_code | string | 用户邀请码 |
| last_login | int | 最近一次登录时间戳 |
| expire_time | int | 账户过期时间戳 |
| created_time | int | 注册时间戳 |
| updated_time | int | 更新时间戳 |
| status | int | 用户显示状态 |
| extra | object | 用户扩展信息 |
| group | object | 用户组信息 |
| link | string | 用户个人页面链接 |

## 使用示例

### 请求示例

```
GET /api/user/detail?userId=1000 HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "id": 1000,
    "parent_id": 0,
    "user_name": "admin",
    "real_name": "",
    "introduce": "这是介绍",
    "avatar_url": "uploads/202211/21/14f56760596b5328.webp",
    "full_avatar_url": "http://127.0.0.1:8001/uploads/202211/21/14f56760596b5328.webp",
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
    "created_time": 1669012062,
    "updated_time": 1679536756,
    "extra": null,
    "group": null,
    "link": ""
  }
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
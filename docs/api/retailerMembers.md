# 获取分销团队列表接口

获取分销员的下级团队成员列表，支持分页查询。

## 注意事项

- 该接口采用GET方法
- 需要用户登录验证（当前用户必须是分销员）
- 只返回当前用户直接下级的成员列表
- 支持分页查询，可指定当前页码和每页数量
- 返回团队成员的基本信息和分销状态

## 请求地址

```
{域名地址}/api/retailer/members
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/retailer/members`

## 请求语法

```
GET {域名地址}/api/retailer/members
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :------------------- | :------- | :--- | :---------------------- |
| current | int | 否 | 当前页码，默认为1 |
| pageSize | int | 否 | 每页显示数量，默认为10 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object | 团队成员列表数组 |
| total | int | 总记录数 |

#### data 结果 item 参数

| 字段名 | 类型 | 说明 |
| :------------------- | :------- | :---------------------- |
| id | int | 用户ID |
| parent_id | int | 上级用户ID（当前分销员ID） |
| user_name | string | 用户名 |
| real_name | string | 真实姓名 |
| avatar_url | string | 用户头像地址 |
| email | string | 邮箱地址 |
| phone | string | 手机号 |
| group_id | int | 用户组ID |
| is_retailer | int | 是否是分销员（1是，0否） |
| balance | int | 用户余额（单位：分） |
| total_reward | int | 分销员累计收益（单位：分） |
| invite_code | string | 用户邀请码 |
| last_login | int | 最近一次登录时间戳 |
| expire_time | int | 过期时间戳 |
| created_time | int | 注册时间戳 |
| updated_time | int | 更新时间戳 |
| status | int | 用户显示状态 |

## 使用示例

### 请求示例

```
GET /api/retailer/members?current=1&pageSize=10 HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": [
    {
      "id": 2,
      "created_time": 1665753900,
      "updated_time": 1665753923,
      "parent_id": 1000,
      "user_name": "wangxiaocong",
      "real_name": "",
      "avatar_url": "",
      "email": "",
      "phone": "",
      "group_id": 1,
      "status": 1,
      "is_retailer": 0,
      "balance": 0,
      "total_reward": 0,
      "invite_code": "",
      "last_login": 0,
      "expire_time": 0
    },
    {
      "id": 1,
      "created_time": 1665755500,
      "updated_time": 1665755545,
      "parent_id": 1000,
      "user_name": "wangdacong",
      "real_name": "王小强",
      "avatar_url": "",
      "email": "wangxiaoqiang@qq.com",
      "phone": "13888888888",
      "group_id": 1,
      "status": 1,
      "is_retailer": 1,
      "balance": 0,
      "total_reward": 0,
      "invite_code": "123456",
      "last_login": 0,
      "expire_time": 1667404800
    }
  ],
  "total": 2
}
```

### 错误代码

| 错误码 | 说明 |
| :----- | :-------------------------- |
| 0 | OK |
| -1 | 错误，错误原因在 msg 中指出 |
| 1001 | 未登录 |
| 1002 | 未授权（当前用户不是分销员） |
| 200 | API 请求 OK |
# 获取分销员详情接口

获取指定分销员的详细信息，包括用户基本信息、分销状态和用户组信息。

## 注意事项

- 该接口采用GET方法
- 需要提供分销员ID参数
- 需要用户登录验证
- 返回分销员的完整用户信息和分组详情
- 包含分销员的累计收益、邀请码等信息

## 请求地址

```
{域名地址}/api/retailer/info
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/retailer/info`

## 请求语法

```
GET {域名地址}/api/retailer/info
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :------------------- | :------- | :--- | :---------------------- |
| retailer_id | int | 是 | 分销员ID |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object | 分销员详细信息对象 |

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
| is_retailer | int | 是否是分销员（1是，0否） |
| balance | int | 用户余额（单位：分） |
| total_reward | int | 分销员累计收益（单位：分） |
| invite_code | string | 用户邀请码 |
| last_login | int | 最近一次登录时间戳 |
| expire_time | int | 过期时间戳 |
| created_time | int | 注册时间戳 |
| updated_time | int | 更新时间戳 |
| status | int | 用户显示状态 |
| group | object | 用户分组信息 |

#### group 用户分组信息参数

| 字段名 | 类型 | 说明 |
| :------------------- | :------- | :---------------------- |
| id | int | 分组ID |
| title | string | 分组名称 |
| description | string | 分组简介 |
| level | int | 分组等级 |
| price | int | 分组价格（单位：分） |
| setting | object | 分组配置信息 |
| status | int | 分组显示状态 |
| favorable_price | int | 优惠价格 |

#### setting 分组配置信息参数

| 字段名 | 类型 | 说明 |
| :------------------- | :------- | :---------------------- |
| share_reward | int | 分享奖励百分比 |
| parent_reward | int | 上级奖励百分比 |
| discount | int | 折扣百分比 |
| expire_day | int | 有效期天数（0为不限制） |

## 使用示例

### 请求示例

```
GET /api/retailer/info?retailer_id=1000 HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "id": 1000,
    "created_time": 1669012062,
    "updated_time": 1679536756,
    "parent_id": 0,
    "user_name": "retailer1",
    "real_name": "分销员1",
    "avatar_url": "uploads/202211/21/14f56760596b5328.webp",
    "email": "retailer1@example.com",
    "phone": "13800138000",
    "group_id": 2,
    "status": 1,
    "is_retailer": 1,
    "balance": 150000,
    "total_reward": 500000,
    "invite_code": "retailer123",
    "last_login": 1702912236,
    "expire_time": 1997404800,
    "group": {
      "id": 2,
      "created_time": 0,
      "updated_time": 1696919880,
      "title": "高级分销员",
      "description": "高级分销员特权...",
      "level": 2,
      "status": 1,
      "price": 9900,
      "setting": {
        "share_reward": 25,
        "parent_reward": 5,
        "discount": 90,
        "expire_day": 0
      },
      "favorable_price": 8900
    },
    "full_avatar_url": "https://www.aicms.com/uploads/202211/21/14f56760596b5328.webp",
    "link": ""
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
# 获取我的优惠券列表接口

获取当前用户已领取的优惠券列表，支持分页显示和状态筛选功能。

## 注意事项

- 该接口用于获取当前用户的优惠券列表信息
- 支持分页查询，可通过current和pageSize参数控制分页
- 支持按状态筛选优惠券（未使用、已使用或全部）
- 需要用户登录后才能获取优惠券列表
- 需要确保域名地址正确配置
- 返回结果包含总数信息，便于前端分页处理

## 请求地址

```
{域名地址}/api/coupon/codes
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/coupon/codes`

## 请求语法

```
GET /api/coupon/codes
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

## 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :--- | :--- | :--- | :--- |
| current | int | 否 | 获取指定分页数据，当前页码 |
| pageSize | int | 否 | 显示数量，每页数量 |
| status | int | 否 | 状态 0 = 未使用，1 = 已使用, 不传，获取全部 |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

## 返回参数

| 字段名 | 类型 | 说明 |
| :--- | :--- | :--- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object[] | 结果内容 |
| total | int | 总数 |

### data 结果 item 参数

| 字段名 | 类型 | 说明 |
| :--- | :--- | :--- |
| id | int | 优惠券码ID |
| title | string | 优惠券名称 |
| coupon_id | int | 优惠券ID |
| start_time | int | 开始时间 |
| end_time | int | 结束时间 |
| user_id | int | 用户ID |
| money | float | 优惠金额 |
| max_money | float | 最高优惠金额 |
| get_time | int | 领取时间 |
| use_time | int | 使用时间 |
| order_id | int | 订单ID |
| money_type | int | 优惠金额类型 0 = 固定金额，1=随机金额，2=百分比折扣 |
| description | string | 描述 |

## 使用示例

### 请求示例

```
GET /api/coupon/codes?current=1&pageSize=10&status=0 HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "data": [
    {
      "id": 1,
      "title": "新用户优惠券",
      "coupon_id": 1,
      "start_time": 1624494644,
      "end_time": 1627173044,
      "user_id": 1,
      "money": 10.00,
      "max_money": 0.00,
      "get_time": 1624494644,
      "use_time": 0,
      "order_id": 0,
      "money_type": 0,
      "description": "新用户专享优惠券"
    },
    {
      "id": 2,
      "title": "满减优惠券",
      "coupon_id": 2,
      "start_time": 1624494644,
      "end_time": 1627173044,
      "user_id": 1,
      "money": 20.00,
      "max_money": 0.00,
      "get_time": 1624494650,
      "use_time": 0,
      "order_id": 0,
      "money_type": 0,
      "description": "满100可用"
    }
  ],
  "msg": "",
  "total": 2
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
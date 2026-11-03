# 获取可用优惠券列表接口

获取当前用户当前情况下可以使用的优惠券列表，支持按订单金额和商品ID筛选。

## 注意事项

- 该接口用于获取当前用户可用的优惠券列表
- 可通过amount参数筛选适用于指定金额订单的优惠券
- 可通过archive_id参数筛选适用于指定商品的优惠券
- 需要用户登录后才能获取优惠券列表
- 需要确保域名地址正确配置
- 返回的是当前时间有效且未使用的优惠券
- 优惠券的有效性包括时间范围、使用条件等限制

## 请求地址

```
{域名地址}/api/coupon/valid
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/coupon/valid`

## 请求语法

```
GET /api/coupon/valid
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

## 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :--- | :--- | :--- | :--- |
| amount | int | 否 | 订单金额，用于筛选满足金额条件的优惠券 |
| archive_id | int | 否 | 商品ID，用于筛选可用于指定商品的优惠券 |

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
| type | int | 优惠券类型: 1 = 注册送优惠券,2 = 限量优惠券,3 = 购买成功赠送,4 = 满减促销优惠券,5 = 自由规则,6 = 积分兑换券 |
| money_type | int | 优惠金额类型 0 = 固定金额，1=随机金额，2=百分比折扣 |
| description | string | 描述 |

## 使用示例

### 请求示例

```
GET /api/coupon/valid?amount=100&archive_id=5 HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "data": [
    {
      "id": 1,
      "title": "满减优惠券",
      "coupon_id": 1,
      "start_time": 1624494644,
      "end_time": 1627173044,
      "user_id": 1,
      "money": 10.00,
      "max_money": 0.00,
      "get_time": 1624494644,
      "use_time": 0,
      "order_id": 0,
      "type": 4,
      "money_type": 0,
      "description": "满100可用"
    },
    {
      "id": 2,
      "title": "新用户优惠券",
      "coupon_id": 2,
      "start_time": 1624494644,
      "end_time": 1627173044,
      "user_id": 1,
      "money": 20.00,
      "max_money": 0.00,
      "get_time": 1624494650,
      "use_time": 0,
      "order_id": 0,
      "type": 1,
      "money_type": 0,
      "description": "新用户专享优惠券"
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
# 沟通定制订单接受报价接口

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 需要用户登录后才能访问
- 订单状态为待付款状态，等待用户支付
- 可以通过商品ID或商品详情列表创建订单
- 该接口与创建订单接口参数相同，专门用于接受定制订单

## 请求地址

```
{域名地址}/api/communication/order/accept
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/communication/order/accept`

## 请求语法

```
POST {域名地址}/api/communication/order/accept
Content-Type: application/json
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :---------------- | :------ | :--- | :-------------------- |
| goods_id | int | 否 | 商品ID，单个商品下单时可使用 |
| quantity | int | 否 | 商品数量，单个商品下单时可使用 |
| goods_sku_id | int | 否 | SKU ID，单个商品下单时可使用 |
| details | object[] | 否 | 多个商品信息，goods_id 和 details 必须传一个 |
| remark | string | 否 | 订单备注 |
| type | string | 否 | 订单类型，goods、vip |
| coupon_code | string | 否 | 优惠券码 |
| coupon_code_id | int | 否 | 优惠券码ID |
| coupon_id | int | 否 | 优惠券ID，满减类型的优惠券 |
| address | object | 否 | 收件地址信息 |

#### details item 参数

| 字段名 | 类型 | 必填 | 说明 |
| :---------------- | :------ | :--- | :-------------------- |
| goods_id | int | 是 | 商品ID |
| quantity | int | 是 | 商品数量 |

#### address 参数

| 字段名 | 类型 | 必填 | 说明 |
| :---------------- | :------ | :--- | :-------------------- |
| id | int | 否 | 地址ID |
| name | string | 是 | 收件人 |
| phone | string | 是 | 联系电话 |
| province | string | 是 | 省份 |
| city | string | 是 | 城市 |
| country | string | 是 | 区县 |
| address_info | string | 是 | 详细地址 |
| postcode | string | 是 | 邮编 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object | 订单信息 |

#### data 结果参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| id | int | 订单ID |
| order_id | string | 订单号 |
| payment_id | string | 支付流水ID |
| user_id | int | 用户ID |
| remark | string | 订单备注 |
| type | string | 订单类型 |
| origin_amount | int | 订单原始总价 |
| amount | int | 订单实际总价 |
| paid_time | int | 支付时间 |
| end_time | int | 订单预计自动完成时间 |
| deliver_time | int | 发货时间 |
| finished_time | int | 订单完成时间 |
| discount_amount | int | 优惠金额 |
| seller_id | int | 卖家ID |
| seller_amount | int | 卖家可得收益 |
| share_user_id | int | 推广者ID |
| share_parent_user_id | int | 推广者上级ID |
| share_amount | int | 推广者可得收益 |
| share_parent_amount | int | 推广者上级可得收益 |
| express_company | string | 快递公司 |
| tracking_number | string | 快递运单号 |
| created_time | int | 下单时间戳 |
| updated_time | int | 更新时间戳 |
| status | int | 订单状态：-1取消，0待付款，1已付款，2已发货，3已完成，8退款中，9已退款 |
| refund_status | int | 退款状态：-1退款失败，0无或退款中，1已退款 |

## 使用示例

### 请求示例

```
POST /api/communication/order/accept HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "goods_id": 188,
  "quantity": 1,
  "type": "goods",
  "remark": "定制商品订单"
}
```

### 响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "id": 46,
    "created_time": 1669212548,
    "updated_time": 1669212548,
    "order_id": "202211232209080046",
    "payment_id": "",
    "user_id": 1000,
    "address_id": 0,
    "remark": "定制商品订单",
    "type": "goods",
    "status": 0,
    "refund_status": 0,
    "origin_amount": 9900,
    "amount": 9900,
    "paid_time": 0,
    "end_time": 0,
    "deliver_time": 0,
    "finished_time": 0,
    "discount_amount": 0,
    "seller_id": 15,
    "seller_amount": 7920,
    "share_user_id": 0,
    "share_parent_user_id": 0,
    "share_amount": 0,
    "share_parent_amount": 0,
    "express_company": "",
    "tracking_number": ""
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
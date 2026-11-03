获取商品结算信息，支持单个商品或多个商品的订单结算，包含优惠计算、地址信息等。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 支持单个商品下单（通过goods_id、quantity、goods_sku_id参数）或多个商品下单（通过details参数）
- 支持使用优惠券（优惠券码或优惠券ID）
- 需要用户登录验证
- 支持设置收件地址和订单备注

## 请求地址

```
{域名地址}/api/order/checkout
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/order/checkout`

## 请求语法

```
POST {域名地址}/api/order/checkout
Content-Type: application/json
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :------------------- | :------- | :--- | :---------------------- |
| goods_id | int | 否 | 商品ID，单个商品下单时使用，与details参数二选一 |
| quantity | int | 否 | 商品数量，单个商品下单时使用 |
| goods_sku_id | int | 否 | SKU ID，单个商品下单时使用 |
| details | object[] | 否 | 多个商品信息数组，与goods_id参数二选一 |
| remark | string | 否 | 订单备注 |
| type | string | 否 | 订单类型，如 goods（商品）、vip（会员） |
| coupon_code | string | 否 | 优惠券码 |
| coupon_code_id | int | 否 | 优惠券码ID |
| coupon_id | int | 否 | 优惠券ID（满减类型的优惠券） |
| address | object | 否 | 收件地址信息 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object | 结果内容对象 |

#### data 结果参数

| 字段名 | 类型 | 说明 |
| :------------------- | :------- | :---------------------- |
| currency_code | string | 货币符号 |
| currency_symbol | string | 货币名称 |
| details | object[] | 商品信息列表 |
| origin_amount | int | 商品优惠前总金额 |
| amount | int | 优惠后总金额 |
| discount_amount | int | 优惠总金额 |
| coupon_id | int | 优惠券ID |
| coupon_code | string | 优惠券码 |
| coupon_code_id | int | 优惠券码ID |
| address_id | int | 收件地址ID |
| remark | string | 订单备注 |

#### details 商品信息参数

每个商品对象包含以下字段（具体字段取决于系统设计）：

| 字段名 | 类型 | 说明 |
| :------------------- | :------- | :---------------------- |
| id | int | 商品详情ID |
| goods_id | int | 商品ID |
| goods_sku_id | int | SKU ID |
| quantity | int | 商品数量 |
| sku_values    | array           | SKU 选项值列表       |
| price | int | 商品单价 |
| total_price | int | 商品小计 |

## 使用示例

### 请求示例（单个商品下单,无SKU）

```
POST /api/order/checkout HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "goods_id": 1,
  "quantity": 2,
  "remark": "请尽快发货",
  "type": "goods",
  "coupon_code": "SAVE100",
  "address": {
    "name": "张三",
    "phone": "13800138000",
    "province": "广东省",
    "city": "深圳市",
    "district": "南山区",
    "address": "科技园南区1号",
    "zipcode": "518000"
  }
}
```

### 请求示例（多个商品下单）

```
POST /api/order/checkout HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "details": [
    {
      "goods_id": 1,
      "quantity": 2,
      "goods_sku_id": 1,
      "sku_values": [
        {
            "id": 156,
            "archive_id": 32,
            "option_id": 33,
            "title": "Small",
            "option_title": "Size"
        }
      ]
    },
    {
      "goods_id": 2,
      "quantity": 1,
      "goods_sku_id": 3,
      "sku_values": [
        {
            "id": 153,
            "archive_id": 32,
            "option_id": 32,
            "title": "Denim",
            "option_title": "Fiber"
        },
        {
            "id": 156,
            "archive_id": 32,
            "option_id": 33,
            "title": "Small",
            "option_title": "Size"
        }
      ]
    }
  ],
  "remark": "多个商品订单",
  "type": "goods",
  "coupon_id": 5,
  "address": {
    "name": "李四",
    "phone": "13900139000",
    "province": "北京市",
    "city": "北京市",
    "district": "朝阳区",
    "address": "建国路1号",
    "zipcode": "100000"
  }
}
```

### 响应示例

```json
{
  "code": 0,
  "msg": "获取成功",
  "data": {
    "currency_code": "CNY",
    "currency_symbol": "¥",
    "details": [
      {
        "id": 1,
        "goods_id": 1,
        "goods_sku_id": 1,
        "quantity": 2,
        "price": 10000,
        "total_price": 20000
      }
    ],
    "origin_amount": 20000,
    "amount": 18000,
    "discount_amount": 2000,
    "coupon_id": 0,
    "coupon_code": "SAVE100",
    "coupon_code_id": 1,
    "address_id": 123,
    "remark": "请尽快发货"
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
# 订单创建支付接口

为待支付的订单创建支付，支持多种支付方式，包括微信、微信小程序、支付宝、PayPal和Stripe。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 需要提供订单ID和支付方式
- 仅登录用户可以调用此接口
- 订单必须处于"待支付"状态才能创建支付
- 根据不同的支付方式返回相应的支付信息（二维码、跳转链接或小程序支付参数）

## 请求地址

```
{域名地址}/api/order/payment
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/order/payment`

## 请求语法

```
POST {域名地址}/api/order/payment
Content-Type: application/json
```

## 请求头

此接口需要用户登录认证，具体请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :----- | :---- | :--- | :--- |
| order_id | string | 是 | 订单ID |
| pay_way | string | 是 | 支付方式：可选值有：wechat、weapp、alipay、paypal、stripe |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object | 支付相关信息 |

### data字段说明

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| pay_way | string | 支付方式 |
| code_url | string | 二维码图片链接（微信支付） |
| jump_url | string | 跳转链接（支付宝、PayPal支付） |
| paySign | string | 签名（微信小程序支付） |
| timeStamp | int | 时间戳（微信小程序支付） |
| package | string | package（微信小程序支付） |
| nonceStr | string | nonceStr（微信小程序支付） |
| signType | string | 签名方式（微信小程序支付） |

根据不同的支付方式，data中会包含相应的支付信息字段。

## 使用示例

### 请求示例

```
POST /api/order/payment HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "order_id": "202211232209080046",
  "pay_way": "alipay"
}
```

### 响应示例

#### 支付宝支付响应

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "pay_way": "alipay",
    "jump_url": "https://openapi.alipay.com/gateway.do?..."
  }
}
```

#### 微信支付响应

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "pay_way": "wechat",
    "code_url": "weixin://wxpay/bizpayurl?pr=..."
  }
}
```

#### 微信小程序支付响应

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "pay_way": "weapp",
    "paySign": "A8E3A1C5F7...",
    "timeStamp": 1672531200,
    "package": "prepay_id=wx2023010123456789",
    "nonceStr": "abc123def456",
    "signType": "MD5"
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
| 4001 | 订单不存在 |
| 4002 | 订单状态不允许支付 |
| 4003 | 支付方式不支持 |
| 4004 | 订单金额为0，无需支付 |
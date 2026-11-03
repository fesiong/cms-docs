# 创建沟通定制订单接口

创建沟通定制订单，用于用户提交定制需求，等待商家确认。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 需要用户登录后才能访问
- 创建的订单需要商家确认后才能进入支付流程
- 订单状态为待确认状态，等待商家接受

## 请求地址

```
{域名地址}/api/communication/order/create
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/communication/order/create`

## 请求语法

```
POST {域名地址}/api/communication/order/create
Content-Type: application/json
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :---------------- | :------ | :--- | :-------------------- |
| archive_id | int | 是 | 商品ID |
| content | string | 是 | 订单内容 |
| phone | string | 是 | 联系电话 |
| title | string | 是 | 订单标题 |
| images | string[] | 否 | 订单图片列表 |
| order_extra | object | 否 | 订单额外信息 |

#### order_extra 参数

`order_extra` 是一个键值对对象，键名是字段名，键值是字段值，用于传递订单的额外信息。

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |

## 使用示例

### 请求示例

```
POST /api/communication/order/create HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "archive_id": 188,
  "title": "定制网站主题",
  "content": "需要定制一个响应式的外贸网站主题，包含多语言功能",
  "phone": "13888888888",
  "images": [
    "https://www.aicms.com/uploads/image1.jpg",
    "https://www.aicms.com/uploads/image2.jpg"
  ],
  "order_extra": {
    "delivery_time": "2023-12-31",
    "requirement": "需要支持中英文切换"
  }
}
```

### 响应示例

```json
{
  "code": 0,
  "msg": "定制订单创建成功"
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
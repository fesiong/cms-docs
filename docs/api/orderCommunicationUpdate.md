# 更新沟通定制订单接口

更新沟通定制订单的基本信息，包括标题、内容和订单额外信息。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 需要用户登录后才能访问
- 只能更新属于当前用户的订单
- 订单ID为必填参数，用于指定要更新的订单

## 请求地址

```
{域名地址}/api/communication/order/update
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/communication/order/update`

## 请求语法

```
POST {域名地址}/api/communication/order/update
Content-Type: application/json
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :---------------- | :------ | :--- | :-------------------- |
| id | int | 是 | 沟通订单ID |
| title | string | 否 | 订单标题 |
| content | string | 否 | 订单内容 |
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

### 请求示例（更新订单标题和内容）

```
POST /api/communication/order/update HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "id": 123,
  "title": "更新后的定制网站主题",
  "content": "需要定制一个响应式的外贸网站主题，包含多语言功能和支付接口",
  "order_extra": {
    "delivery_time": "2023-12-31",
    "requirement": "需要支持中英文切换和在线支付"
  }
}
```

### 请求示例（仅更新订单额外信息）

```
POST /api/communication/order/update HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "id": 123,
  "order_extra": {
    "budget": "10000-20000",
    "maintenance_required": "是"
  }
}
```

### 响应示例

```json
{
  "code": 0,
  "msg": "订单更新成功"
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
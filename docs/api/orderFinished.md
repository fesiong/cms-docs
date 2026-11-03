# 订单确认收货接口

允许用户确认订单已收货，将订单状态更新为已完成。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 需要提供订单ID作为确认收货的标识
- 仅登录用户可以调用此接口
- 订单必须处于"已发货"状态才能确认收货
- 确认收货后订单状态将变为"已完成"

## 请求地址

```
{域名地址}/api/order/finish
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/order/finish`

## 请求语法

```
POST {域名地址}/api/order/finish
Content-Type: application/json
```

## 请求头

此接口需要用户登录认证，具体请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :----- | :---- | :--- | :--- |
| order_id | string | 是 | 订单ID |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |

## 使用示例

### 请求示例

```
POST /api/order/finish HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "order_id": "202211232209080046"
}
```

### 响应示例

```json
{
  "code": 0,
  "msg": "订单已完成"
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
| 4002 | 订单状态不允许确认收货 |
| 4003 | 订单已确认收货 |
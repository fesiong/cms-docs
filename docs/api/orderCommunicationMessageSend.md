# 发送沟通定制订单信息接口

向指定的沟通定制订单发送消息，用于用户和管理员之间的沟通交流。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 需要用户登录后才能访问
- 只能向属于当前用户的订单发送消息
- 支持多种消息类型：文本、图片、报价、视频、文件等

## 请求地址

```
{域名地址}/api/communication/message/send
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/communication/message/send`

## 请求语法

```
POST {域名地址}/api/communication/message/send
Content-Type: application/json
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :---------------- | :------ | :--- | :-------------------- |
| comm_order_id | int | 是 | 沟通订单ID |
| sender_id | int | 是 | 发送者ID |
| sender_name | string | 否 | 发送者名称 |
| message_type | string | 是 | 消息类型：text、image、quote、video、file、audio、location、contact、sticker、unknown |
| content | string | 是 | 消息内容 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |

## 使用示例

### 请求示例（发送文本消息）

```
POST /api/communication/message/send HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "comm_order_id": 123,
  "sender_id": 1000,
  "sender_name": "testuser",
  "message_type": "text",
  "content": "您好，我想了解这个定制方案的详细信息"
}
```

### 请求示例（发送图片消息）

```
POST /api/communication/message/send HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "comm_order_id": 123,
  "sender_id": 1000,
  "sender_name": "testuser",
  "message_type": "image",
  "content": "https://www.aicms.com/uploads/image.jpg"
}
```

### 响应示例

```json
{
  "code": 0,
  "msg": "消息发送成功"
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
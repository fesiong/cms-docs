# 获取沟通定制订单沟通信息列表接口

获取指定沟通定制订单的沟通记录列表，支持分页查询。

## 注意事项

- 该接口采用GET方法，无需提交请求体数据
- 需要用户登录后才能访问
- 只能获取属于当前用户订单的沟通记录
- 支持分页查询，可指定当前页码和每页数量

## 请求地址

```
{域名地址}/api/communication/messages
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/communication/messages`

## 请求语法

```
GET {域名地址}/api/communication/messages
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :---------------- | :------ | :--- | :-------------------- |
| comm_order_id | int | 是 | 沟通订单ID |
| current | int | 否 | 当前页码，默认为1 |
| page_size | int | 否 | 每页数量，默认为10 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object[] | 沟通记录列表数据 |

#### data 结果 item 参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| id | int | 沟通记录ID |
| comm_order_id | int | 沟通订单ID |
| sender_id | int | 发送者ID |
| sender_type | string | 发送者类型，user或admin或system |
| sender_name | string | 发送者名称 |
| message_type | string | 沟通记录类型，text 、 image 、 quote 、 video 、 file 、audio 、 location 、 contact 、 sticker 、 unknown  |
| content | string | 沟通记录内容 |

## 使用示例

### 请求示例

```
GET /api/communication/messages?comm_order_id=123 HTTP/1.1
Host: www.aicms.com
Content-Type: application/json
```

### 请求示例（分页查询）

```
GET /api/communication/messages?comm_order_id=123&current=1&page_size=5 HTTP/1.1
Host: www.aicms.com
Content-Type: application/json
```

### 响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": [
    {
      "id": 1,
      "comm_order_id": 123,
      "sender_id": 1000,
      "sender_type": "user",
      "sender_name": "testuser",
      "message_type": "text",
      "content": "您好，我想定制一个外贸网站主题"
    },
    {
      "id": 2,
      "comm_order_id": 123,
      "sender_id": 1,
      "sender_type": "admin",
      "sender_name": "admin",
      "message_type": "image",
      "content": "https://www.aicms.com/uploads/quote_image.jpg"
    },
    {
      "id": 3,
      "comm_order_id": 123,
      "sender_id": 1,
      "sender_type": "admin",
      "sender_name": "admin",
      "message_type": "quote",
      "content": "根据您的需求，定制开发费用为9900元，包含基础功能和后期维护3个月"
    }
  ]
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
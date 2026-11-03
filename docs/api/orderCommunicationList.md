# 获取沟通定制订单列表接口

获取用户沟通定制订单的列表信息，支持分页查询。

## 注意事项

- 该接口采用GET方法，无需提交请求体数据
- 需要用户登录后才能访问
- 返回当前用户的所有沟通定制订单
- 支持分页查询，可指定当前页码和每页数量

## 请求地址

```
{域名地址}/api/communication/orders
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/communication/orders`

## 请求语法

```
GET {域名地址}/api/communication/orders
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :---------------- | :------ | :--- | :-------------------- |
| current | int | 否 | 当前页码，默认为1 |
| page_size | int | 否 | 每页数量，默认为10 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object[] | 订单列表数据 |

#### data 结果 item 参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| id | int | 沟通订单ID |
| order_id | int | 订单ID |
| user_id | int | 用户ID |
| created_time | int | 创建时间戳 |
| archive_id | int | 文档ID |
| phone | string | 手机号码 |
| images | string[] | 图片列表 |
| sketch_images | string[] | 草稿图片列表 |
| finished_images | string[] | 完成图片列表 |
| title | string | 订单标题 |
| content | string | 订单内容 |
| event_date | string | 时间 |
| status | int | 状态，进度：0=待处理，1=沟通中，2=已报价待客户确认，3=接受报价，-1=取消，4=拒绝报价 |
| admin_id | int | 管理员ID |
| quote_price | string | 报价价格 |
| quote_content | string | 报价内容 |
| order_extra | object | 订单额外信息 |
| order_fields | object[] | 订单字段信息 |
| user | object | 用户信息 |
| messages | object[] | 沟通记录 |
| thumb | string | 缩略图 |

#### messages 沟通记录参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| id | int | 沟通记录ID |
| comm_order_id | int | 沟通订单ID |
| sender_id | int | 发送者ID |
| sender_type | string | 发送者类型，user或admin或system |
| sender_name | string | 发送者名称 |
| message_type | string | 沟通记录类型，text 、 image 、 quote 、 video 、 file 、audio 、 location 、 contact 、 sticker 、 unknown |
| content | string | 沟通记录内容 |

## 使用示例

### 请求示例

```
GET /api/communication/orders HTTP/1.1
Host: www.aicms.com
Content-Type: application/json
```

### 请求示例（分页查询）

```
GET /api/communication/orders?current=1&page_size=5 HTTP/1.1
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
      "id": 123,
      "order_id": 456,
      "user_id": 1000,
      "created_time": 1669212548,
      "archive_id": 188,
      "phone": "13888888888",
      "images": [
        "https://www.aicms.com/uploads/image1.jpg",
        "https://www.aicms.com/uploads/image2.jpg"
      ],
      "sketch_images": [],
      "finished_images": [],
      "title": "定制网站主题",
      "content": "需要定制一个响应式的外贸网站主题，包含多语言功能",
      "event_date": "2023-12-31",
      "status": 2,
      "admin_id": 1,
      "quote_price": "9900",
      "quote_content": "根据您的需求，定制开发费用为9900元，包含基础功能和后期维护3个月",
      "order_extra": {
        "delivery_time": "2023-12-31",
        "requirement": "需要支持中英文切换"
      },
      "order_fields": [],
      "user": {
        "id": 1000,
        "username": "testuser"
      },
      "messages": [
        {
          "id": 1,
          "comm_order_id": 123,
          "sender_id": 1000,
          "sender_type": "user",
          "sender_name": "testuser",
          "message_type": "text",
          "content": "您好，我想定制一个外贸网站主题"
        }
      ],
      "thumb": "https://www.aicms.com/uploads/thumb.jpg"
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
# 获取订单自定义表单接口

获取指定订单中商品的自定义表单字段信息，用于在订单支付后展示需要买家填写的表单内容。
用户支付后，邮件会收到订单确认邮件，邮件中会包含订单的自定义表单填写链接信息。同时用户在查看订单详情页面时，如需填写表单，也会有对应的链接，链接包含了订单id和code。

## 注意事项

- 该接口采用GET方法，无需提交请求体数据
- 无需用户登录，但需要提供安全的验证码（code）
- 仅能获取已支付（status=1）订单的自定义表单
- 返回订单中所有包含自定义字段的订单详情项
- 如果订单没有自定义表单字段，将返回错误提示

## 请求地址

```
{域名地址}/api/order/custom_form
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/order/custom_form`

## 请求语法

```
GET {域名地址}/api/order/custom_form
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :----- | :--- | :--- | :-------------------- |
| order_id | string | 是 | 订单ID |
| code | string | 是 | 验证码，用于验证身份 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object | 自定义表单数据 |

#### data 结果参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| order_id | string | 订单ID |
| user | object | 用户信息 |
| reset_password | bool | 是否需要用户重置密码 |
| details | object[] | 订单详情中带自定义表单的商品列表 |

#### user 参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| id | int | 用户ID |
| user_name | string | 用户名 |
| email | string | 邮箱 |
| phone | string | 电话 |
| status | int | 用户状态 |
| group_id | int | 用户组ID |
| created_time | int | 注册时间戳 |
| updated_time | int | 更新时间戳 |

#### details item 参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| id | int | 订单详情ID |
| title | string | 商品标题 |
| order_fields | object[] | 商品的自定义表单字段列表 |

#### order_fields item 参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| name | string | 字段名称 |
| field_name | string | 字段标识名 |
| type | string | 字段类型（如 text、textarea、select 等） |
| value | any | 字段默认值/已填写值 |
| default | any | 字段默认值 |

## 使用示例

### 请求示例

```
GET /api/order/custom_form?order_id=202211232209080046&code=e10adc3949ba59abbe56e057f20f883e HTTP/1.1
Host: www.aicms.com
Content-Type: application/json
```

### 响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "order_id": "202211232209080046",
    "user": {
      "id": 1,
      "user_name": "testuser",
      "email": "test@example.com",
      "phone": "13888888888",
      "status": 1,
      "group_id": 0,
      "created_time": 1669000000,
      "updated_time": 1669000000
    },
    "reset_password": false,
    "details": [
      {
        "id": 16,
        "title": "定制T恤",
        "order_fields": [
          {
            "name": "颜色",
            "field_name": "color",
            "type": "select",
            "value": "红色",
            "default": ""
          },
          {
            "name": "尺寸",
            "field_name": "size",
            "type": "select",
            "value": "L",
            "default": ""
          },
          {
            "name": "备注文字",
            "field_name": "note",
            "type": "textarea",
            "value": "",
            "default": ""
          }
        ]
      }
    ]
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

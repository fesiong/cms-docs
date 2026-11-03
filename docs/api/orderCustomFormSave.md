# 保存订单自定义表单接口

保存已支付订单中商品的自定义表单填写内容，支持批量更新商品的自定义字段值。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 无需用户登录，但需要提供安全的验证码（code）
- 仅能保存已支付（status=1）订单的自定义表单
- 同时支持在提交表单时重置用户密码（当 reset_password 为 true 时）
- 仅更新 details 中明确传入 order_extra 的订单详情项

## 请求地址

```
{域名地址}/api/order/custom_form
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/order/custom_form`

## 请求语法

```
POST {域名地址}/api/order/custom_form
Content-Type: application/json
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :----- | :--- | :--- | :-------------------- |
| order_id | string | 是 | 订单ID |
| code | string | 是 | 验证码，用于验证身份 |
| password | string | 否 | 新密码，当用户需要重置密码时传入 |
| details | object[] | 否 | 要更新自定义表单的订单详情列表 |

#### details item 参数

| 字段名 | 类型 | 必填 | 说明 |
| :----- | :--- | :--- | :-------------------- |
| id | int | 是 | 订单详情ID |
| order_extra | object | 是 | 自定义表单字段键值对，key 为字段标识名，value 为填写值 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明或成功提示 |

## 使用示例

### 请求示例

```
POST /api/order/custom_form HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "order_id": "202211232209080046",
  "code": "e10adc3949ba59abbe56e057f20f883e",
  "password": "newpassword123",
  "details": [
    {
      "id": 16,
      "order_extra": {
        "color": "红色",
        "size": "L",
        "note": "请加急处理"
      }
    },
    {
      "id": 17,
      "order_extra": {
        "color": "蓝色",
        "size": "M",
        "note": ""
      }
    }
  ]
}
```

### 响应示例

```json
{
  "code": 0,
  "msg": "更新成功"
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

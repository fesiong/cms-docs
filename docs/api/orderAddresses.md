# 获取用户收货地址列表接口

获取当前登录用户的所有收货地址列表信息。

## 注意事项

- 该接口采用GET方法，无需提交请求体数据
- 需要用户登录后才能访问
- 返回用户所有的收货地址列表
- 包含收货地址的完整信息

## 请求地址

```
{域名地址}/api/order/addresses
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/order/addresses`

## 请求语法

```
GET {域名地址}/api/order/addresses
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

无

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object[] | 收货地址列表数据 |

#### data 结果 item 参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| id | int | 地址ID |
| name | string | 收件人姓名 |
| last_name | string | 收件人姓氏 |
| email | string | 邮箱地址 |
| company | string | 公司名称 |
| phone | string | 联系电话 |
| province | string | 省份 |
| city | string | 城市 |
| country | string | 区县 |
| address_info | string | 详细地址 |
| postcode | string | 邮政编码 |
| created_time | int | 创建时间戳 |
| updated_time | int | 更新时间戳 |
| user_id | int | 用户ID |
| status | int | 状态(1:启用,0:禁用) |

## 使用示例

### 请求示例

```
GET /api/order/addresses HTTP/1.1
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
      "created_time": 1669212548,
      "updated_time": 1669212548,
      "user_id": 1000,
      "name": "王先生",
      "last_name": "王",
      "email": "wang@example.com",
      "company": "示例公司",
      "phone": "13888888888",
      "province": "河南省",
      "city": "郑州市",
      "country": "中原区",
      "address_info": "中原西路233号",
      "postcode": "450000",
      "status": 1
    },
    {
      "id": 2,
      "created_time": 1669212548,
      "updated_time": 1669212548,
      "user_id": 1000,
      "name": "李女士",
      "last_name": "李",
      "email": "li@example.com",
      "company": "示例公司",
      "phone": "13999999999",
      "province": "北京市",
      "city": "北京市",
      "country": "朝阳区",
      "address_info": "朝阳区建国路88号",
      "postcode": "100000",
      "status": 1
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
# 保存用户收货地址接口

创建或更新用户的收货地址信息。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 需要用户登录后才能访问
- 如果提供了ID参数，则更新现有地址；否则创建新地址
- 所有标记为必填的字段都需要提供值

## 请求地址

```
{域名地址}/api/order/address
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/order/address`

## 请求语法

```
POST {域名地址}/api/order/address
Content-Type: application/json
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :---------------- | :------ | :--- | :-------------------- |
| id | int | 否 | 地址ID，存在时为更新操作 |
| name | string | 是 | 收件人姓名 |
| last_name | string | 是 | 收件人姓氏 |
| email | string | 是 | 邮箱地址 |
| company | string | 否 | 公司名称 |
| phone | string | 是 | 联系电话 |
| province | string | 是 | 省份 |
| city | string | 是 | 城市 |
| country | string | 是 | 区县 |
| address_info | string | 是 | 详细地址 |
| postcode | string | 是 | 邮政编码 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object | 保存的地址数据 |

#### data 结果参数

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

### 请求示例（创建新地址）

```
POST /api/order/address HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "name": "王先生",
  "last_name": "王",
  "email": "wang@example.com",
  "company": "示例公司",
  "phone": "13888888888",
  "province": "河南省",
  "city": "郑州市",
  "country": "中原区",
  "address_info": "中原西路233号",
  "postcode": "450000"
}
```

### 请求示例（更新现有地址）

```
POST /api/order/address HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "id": 1,
  "name": "王先生",
  "last_name": "王",
  "email": "wang@example.com",
  "company": "示例公司",
  "phone": "13888888888",
  "province": "河南省",
  "city": "郑州市",
  "country": "中原区",
  "address_info": "中原西路233号",
  "postcode": "450000"
}
```

### 响应示例

```json
{
  "code": 0,
  "msg": "保存成功",
  "data": {
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
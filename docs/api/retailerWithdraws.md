# 获取提现列表接口

获取分销员的提现申请记录列表，支持分页查询和状态筛选。

## 注意事项

- 该接口采用GET方法
- 需要用户登录后才能调用此接口
- 只返回当前登录用户的提现记录
- 支持分页查询，默认每页显示固定数量的记录
- 提现记录包含不同状态：等待处理、已同意、已提现、提现错误

## 请求地址

```
{域名地址}/api/retailer/withdraw
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/retailer/withdraw`

## 请求语法

```
GET {域名地址}/api/retailer/withdraw
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :----- | :----- | :--- | :--- |
| current | int | 否 | 获取指定分页数据，当前页码，默认为1 |
| pageSize | int | 否 | 显示数量，每页数量，默认为10 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object | 结果内容 |
| total | int | 总数 |

#### data 参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| id | int | 提现记录ID |
| user_id | int | 用户ID |
| amount | int | 提现金额 |
| success_time | int | 成功时间 |
| withdraw_way | int | 提现去向，1-微信提现，2-支付宝提现，3-线下 |
| status | int | 提现状态，0-等待处理，1-已同意，2-已提现，-1-提现错误 |
| error_times | int | 处理出错次数 |
| last_time | int | 上一次处理时间 |
| remark | string | 备注 |
| user_name | string | 用户名 |

## 使用示例

### 请求示例

```
GET /api/retailer/withdraw?current=1&pageSize=10 HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": [
    {
      "id": 1,
      "user_id": 1000,
      "created_time": 1669012062,
      "updated_time": 1679536756,
      "amount": 10000,
      "user_name": "admin",
      "success_time": 1679536756,
      "withdraw_way": 1,
      "status": 1,
      "error_times": 0,
      "last_time": 1679536756,
      "remark": "用户提现"
    }
  ],
  "total": 1
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
# 获取分销员收益列表接口

获取分销员的收益列表，支持分页查询。

## 注意事项

- 该接口采用GET方法
- 需要用户登录验证
- 只返回当前登录用户的分销收益记录
- 支持分页查询，可指定当前页码和每页数量
- 包含订单金额、佣金金额、提现状态等信息

## 请求地址

```
{域名地址}/api/retailer/commissions
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/retailer/commissions`

## 请求语法

```
GET {域名地址}/api/retailer/commissions
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :------------------- | :------- | :--- | :---------------------- |
| current | int | 否 | 当前页码，默认为1 |
| pageSize | int | 否 | 每页显示数量，默认为10 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object | 分销收益列表数组 |
| total | int | 总记录数 |

#### data 结果 item 参数

| 字段名 | 类型 | 说明 |
| :------------------- | :------- | :---------------------- |
| id | int | 收益记录ID |
| user_id | int | 用户ID |
| order_id | string | 订单号 |
| order_amount | int | 订单金额（单位：分） |
| amount | int | 获得佣金金额（单位：分） |
| status | int | 状态（0 待结算，1 已结算，2 已提现等） |
| withdraw_id | int | 提现ID，0表示未提现 |
| remark | string | 备注信息 |
| user_name | string | 用户名 |
| can_withdraw | boolean | 是否可提现 |
| created_time | int | 创建时间戳 |
| updated_time | int | 更新时间戳 |

## 使用示例

### 请求示例

```
GET /api/retailer/commissions?current=1&pageSize=10 HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": [
    {
      "id": 6,
      "created_time": 1671504424,
      "updated_time": 1671504424,
      "user_id": 1000,
      "order_id": "202212201046420050",
      "order_amount": 19900,
      "amount": 15920,
      "status": 0,
      "withdraw_id": 0,
      "remark": "销售收入",
      "user_name": "testuser",
      "can_withdraw": false
    },
    {
      "id": 5,
      "created_time": 1669618222,
      "updated_time": 1669618222,
      "user_id": 1000,
      "order_id": "202211281446070047",
      "order_amount": 19900,
      "amount": 15920,
      "status": 0,
      "withdraw_id": 0,
      "remark": "销售收入",
      "user_name": "testuser",
      "can_withdraw": false
    }
  ],
  "total": 2
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
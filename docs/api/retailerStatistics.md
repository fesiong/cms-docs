# 获取分销员统计信息接口

获取分销员的统计信息，包括可提现佣金、已提现佣金、未结算佣金和团队人数。

## 注意事项

- 该接口采用GET方法
- 需要用户登录验证（当前用户必须是分销员）
- 无需任何请求参数
- 返回当前分销员的综合统计数据
- 包含财务统计和团队统计信息

## 请求地址

```
{域名地址}/api/retailer/statistics
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/retailer/statistics`

## 请求语法

```
GET {域名地址}/api/retailer/statistics
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
| data | object | 分销员统计信息对象 |

#### data 结果参数

| 字段名 | 类型 | 说明 |
| :------------------------- | :--- | :---------------------- |
| can_withdraw_amount | int | 可提现佣金金额（单位：分） |
| paid_withdraw_amount | int | 已提现佣金金额（单位：分） |
| unfinished_withdraw_amount | int | 未结算佣金金额（单位：分） |
| member_count | int | 团队人数 |

## 使用示例

### 请求示例

```
GET /api/retailer/statistics HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "can_withdraw_amount": 150000,
    "paid_withdraw_amount": 50000,
    "unfinished_withdraw_amount": 30000,
    "member_count": 25
  }
}
```

### 错误代码

| 错误码 | 说明 |
| :----- | :-------------------------- |
| 0 | OK |
| -1 | 错误，错误原因在 msg 中指出 |
| 1001 | 未登录 |
| 1002 | 未授权（当前用户不是分销员） |
| 200 | API 请求 OK |
# 获取订单统计数据接口

获取当前用户的订单统计数据，包括各种状态的订单数量统计。

## 注意事项

- 该接口采用GET方法
- 需要用户登录验证
- 返回当前用户的订单统计信息
- 包含各种订单状态的数量统计
- 包含愿望清单数量统计

## 请求地址

```
{域名地址}/api/orders/statistics
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/orders/statistics`

## 请求语法

```
GET {域名地址}/api/orders/statistics
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
| data | object | 统计数据对象 |

#### data 结果参数

| 字段名 | 类型 | 说明 |
| :------------------- | :------- | :---------------------- |
| total | int | 订单总数量 |
| pending | int | 待付款订单数量 |
| processing | int | 待处理订单数量 |
| completed | int | 已完成订单数量 |
| cancelled | int | 取消订单数量 |
| refunding | int | 退款中订单数量 |
| refunded | int | 退款完成订单数量 |
| wishlist | int | 愿望清单数量 |

## 使用示例

### 请求示例

```
GET /api/orders/statistics HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "msg": "获取成功",
  "data": {
    "total": 25,
    "pending": 3,
    "processing": 5,
    "completed": 15,
    "cancelled": 1,
    "refunding": 1,
    "refunded": 0,
    "wishlist": 8
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
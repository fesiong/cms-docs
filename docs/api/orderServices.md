# 获取订单服务列表接口

获取系统中启用的订单服务列表，用于订单创建时选择额外服务。

## 请求地址

```
{域名地址}/api/order/services
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/order/services`

## 请求语法

```
GET {域名地址}/api/order/services
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

无

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型     | 说明                  |
| :----- | :------- | :-------------------- |
| code   | int      | 错误码                |
| msg    | string   | 错误原因说明          |
| data   | object[] | 订单服务列表          |
| total  | int      | 服务总数量            |

#### data 结果 item 参数

| 字段名     | 类型    | 说明                                  |
| :--------- | :------ | :------------------------------------ |
| id         | int     | 服务 ID                               |
| name       | string  | 服务名称                              |
| title      | string  | 服务标题                              |
| icon       | string  | 服务图标                              |
| fee_type   | int     | 费用类型，0=固定金额，1=订单金额百分比 |
| fee        | int     | 费用金额或百分比                      |
| max_fee    | int     | 最大费用（当 fee_type=1 时生效）      |
| enabled    | bool    | 是否启用                              |
| sort       | int     | 排序值                                |
| created_time | int   | 创建时间戳                            |
| updated_time | int   | 更新时间戳                            |

## 使用示例

### 请求示例

```
GET /api/order/services HTTP/1.1
Host: your-domain.com
Content-Type: application/json
```

### 响应示例

```json
{
  "code": 0,
  "data": [
    {
      "id": 1,
      "name": "insurance",
      "title": "订单保险",
      "icon": "shield",
      "fee_type": 1,
      "fee": 2,
      "max_fee": 1000,
      "enabled": true,
      "sort": 1,
      "created_time": 1607308159,
      "updated_time": 1662717106
    },
    {
      "id": 2,
      "name": "express",
      "title": "加急配送",
      "icon": "truck",
      "fee_type": 0,
      "fee": 500,
      "max_fee": 0,
      "enabled": true,
      "sort": 2,
      "created_time": 1607308160,
      "updated_time": 1662717107
    }
  ],
  "msg": "",
  "total": 2
}
```

### 错误代码

| 错误码 | 说明                        |
| :----- | :-------------------------- |
| 0      | OK                          |
| -1     | 错误，错误原因在 msg 中指出 |
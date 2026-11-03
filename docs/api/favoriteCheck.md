# 检查是否收藏接口

检查指定商品或文档是否已被当前用户收藏，支持单个或批量查询收藏状态。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 需要提供文档 ID 或文档 ID 数组
- 仅支持已登录用户查询自己的收藏状态
- 支持单个文档查询和批量查询
- 返回的收藏记录包含收藏时间等详细信息

## 请求地址

```
{域名地址}/api/favorite/check
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/favorite/check`

## 请求语法

```
POST {域名地址}/api/favorite/check
Content-Type: application/json
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :------------------- | :------- | :--- | :---------------------- |
| archive_id | int | 否 | 文档ID，与archive_ids二选一 |
| archive_ids | int[] | 否 | 文档ID数组，支持批量查询，与archive_id二选一 |

**注意：** `archive_id` 和 `archive_ids` 参数二选一，优先使用 `archive_ids` 进行批量查询

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | array | 返回收藏数据数组 |

#### data 数组元素参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| id | int | 收藏记录ID |
| archive_id | int | 文档ID |
| sku_id | int | SKU ID（如果适用） |
| user_id | int | 用户ID |
| create_time | int | 收藏时间戳 |

## 使用示例

### 单个文档查询请求示例

```
POST /api/favorite/check HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "archive_id": 1
}
```

### 批量文档查询请求示例

```
POST /api/favorite/check HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "archive_ids": [1, 2, 3, 5]
}
```

### 单个文档查询响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": [
    {
      "id": 1,
      "archive_id": 1,
      "sku_id": 0,
      "user_id": 1,
      "create_time": 1592282639
    }
  ]
}
```

### 批量文档查询响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": [
    {
      "id": 1,
      "archive_id": 1,
      "sku_id": 0,
      "user_id": 1,
      "create_time": 1592282639
    },
    {
      "id": 3,
      "archive_id": 3,
      "sku_id": 0,
      "user_id": 1,
      "create_time": 1592285000
    }
  ]
}
```

### 未收藏响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": []
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
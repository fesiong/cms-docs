# 获取产品/订单评价列表接口

获取产品或订单的评价列表，支持按商品、用户等条件筛选和分页查询。

## 注意事项

- 该接口采用GET方法
- 支持按商品ID、用户ID、订单ID等条件筛选
- 支持自定义排序方式
- 支持分页查询，默认每页10条记录
- 只返回已审核通过的评价（状态为1）

## 请求地址

```
{域名地址}/api/review/list
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/review/list`

## 请求语法

```
GET {域名地址}/api/review/list
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :------------------- | :------- | :--- | :---------------------- |
| id | int | 否 | 文档ID，指定要获取评价的商品 |
| user_id | int | 否 | 用户ID，获取指定用户的评价 |
| order | string | 否 | 评论排序方式，默认 `id desc` |
| page | int | 否 | 页码，默认为 1 |
| limit | int | 否 | 每页显示数量，默认为 10 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object[] | 评价列表数组 |

#### data 结果 item 参数

| 字段名 | 类型 | 说明 |
| :----------- | :----- | :-------------------------- |
| id | int | 评论ID |
| order_id | string | 订单ID |
| archive_id | int | 文档ID |
| archive_sku_id | int | SKU ID |
| user_id | int | 用户ID |
| ip | string | 用户IP地址 |
| score | int | 评分（1-5分） |
| content | string | 评价内容 |
| images | string[] | 评价图片列表 |
| user_name | string | 用户名 |
| email | string | 用户邮箱 |
| created_time | int | 发布时间戳 |
| updated_time | int | 更新时间戳 |
| status | int | 审核状态，1 已审核，0 审核中 |

## 使用示例

### 请求示例

```
GET /api/review/list?archive_id=1&page=1&limit=10 HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "msg": "获取成功",
  "data": [
    {
      "id": 45,
      "order_id": "20231101000001",
      "archive_id": 1,
      "archive_sku_id": 1,
      "user_id": 123,
      "ip": "192.168.1.100",
      "score": 5,
      "content": "商品质量很好，非常满意！",
      "images": [
        "https://www.aicms.com/uploads/review/2023/11/image1.jpg",
        "https://www.aicms.com/uploads/review/2023/11/image2.jpg"
      ],
      "user_name": "张三",
      "email": "zhangsan@example.com",
      "created_time": 1698825600,
      "updated_time": 1698825600,
      "status": 1
    },
    {
      "id": 44,
      "order_id": "20231031000005",
      "archive_id": 1,
      "archive_sku_id": 2,
      "user_id": 124,
      "ip": "192.168.1.101",
      "score": 4,
      "content": "商品不错，物流也很快。",
      "images": [],
      "user_name": "李四",
      "email": "lisi@example.com",
      "created_time": 1698739200,
      "updated_time": 1698739200,
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
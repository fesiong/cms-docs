# 获取愿望清单列表接口

获取当前登录用户的愿望清单列表，支持分页查询，返回用户收藏的商品信息。

## 注意事项

- 该接口采用GET方法，无需请求体
- 需要用户已登录，通过会话或Token验证身份
- 支持分页查询，可通过参数控制每页显示数量和当前页码
- 返回愿望清单中商品的详细信息，包括价格、备注等
- 包含商品当前价格和添加时的价格对比

## 请求地址

```
{域名地址}/api/wishlist/list
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/wishlist/list`

## 请求语法

```
GET {域名地址}/api/wishlist/list
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :------------------- | :------- | :--- | :---------------------- |
| current | int | 否 | 当前页码，默认为1 |
| pageSize | int | 否 | 每页显示数量，默认为10 |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | array | 愿望清单数据列表 |
| total | int | 愿望清单总数量 |

#### data 数组元素参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| id | int | 愿望清单记录ID |
| user_id | int | 用户ID |
| user_name | string | 用户名 |
| archive_id | int | 商品ID |
| sku_id | int | SKU ID |
| title | string | 商品名称 |
| sku_title | string | 商品SKU名称 |
| description | string | 商品描述 |
| remark | string | 用户备注 |
| thumb | string | 商品缩略图URL |
| link | string | 商品链接 |
| price | int | 商品当前价格 |
| origin_price | int | 添加时的商品价格 |
| target_price | int | 用户设定的愿望价格 |
| status | int | 记录状态（如：是否可用） |
| priority | int | 优先级 |
| created_time | int | 添加时间戳 |

## 使用示例

### 请求示例

```
GET /api/wishlist/list?current=1&pageSize=10 HTTP/1.1
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
      "user_id": 1001,
      "user_name": "张三",
      "archive_id": 123,
      "sku_id": 456,
      "title": "iPhone 13",
      "sku_title": "iPhone 13 128G 蓝色",
      "description": "苹果最新款智能手机",
      "remark": "生日礼物",
      "thumb": "https://www.aicms.com/uploads/images/iphone13.jpg",
      "link": "https://www.aicms.com/product/123",
      "price": 599900,
      "origin_price": 699900,
      "target_price": 550000,
      "status": 1,
      "priority": 1,
      "created_time": 1640995200
    },
    {
      "id": 2,
      "user_id": 1001,
      "user_name": "张三",
      "archive_id": 124,
      "sku_id": 457,
      "title": "MacBook Pro",
      "sku_title": "MacBook Pro 14寸 银色",
      "description": "苹果专业笔记本电脑",
      "remark": "工作用",
      "thumb": "https://www.aicms.com/uploads/images/macbook.jpg",
      "link": "https://www.aicms.com/product/124",
      "price": 1499900,
      "origin_price": 1599900,
      "target_price": 1399900,
      "status": 1,
      "priority": 2,
      "created_time": 1640995300
    }
  ],
  "total": 2
}
```

### 错误请求示例

```
GET /api/wishlist/list HTTP/1.1
Host: www.aicms.com
Authorization: Bearer invalid_token
```

### 错误响应示例

```json
{
  "code": 1001,
  "msg": "未登录"
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
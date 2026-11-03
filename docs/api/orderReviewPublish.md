# 发表产品/订单评价接口

允许用户对已购买的产品或订单进行评价，支持文字评价、评分和图片上传。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 需要提供文档ID和评价内容
- 支持登录用户和未登录用户（未登录用户需提供用户名）
- 可以通过订单ID关联评价特定订单
- 支持1-5分的评分系统
- 支持上传多张评价图片
- 评价需要审核后才能显示

## 请求地址

```
{域名地址}/api/review/publish
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/review/publish`

## 请求语法

```
POST {域名地址}/api/review/publish
Content-Type: application/json
```

## 请求头

| 字段名 | 类型 | 必填 | 说明 |
| :----- | :---- | :--- | :--- |
| token | string | 否 | 用户登录令牌，未登录用户可不提供 |

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :----- | :---- | :--- | :--- |
| archive_id | int | 是 | 评价的文档ID |
| content | string | 是 | 评价内容 |
| score | int | 是 | 评分，1-5分 |
| user_name | string | 否 | 用户名（未登录用户必填） |
| email | string | 否 | 邮箱地址（未登录用户可选） |
| order_id | string | 否 | 订单ID，关联特定订单 |
| images | string[] | 否 | 评价图片数组，需要先通过上传接口上传，这里放图片地址 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |

## 使用示例

### 请求示例

```
POST /api/review/publish HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "archive_id": 140,
  "content": "这个产品非常棒，质量很好，发货也很快！",
  "score": 5,
  "order_id": "202211232209080046",
  "images": [
    "https://www.aicms.com/uploads/review/image1.jpg",
    "https://www.aicms.com/uploads/review/image2.jpg"
  ]
}
```

### 响应示例

```json
{
  "code": 0,
  "msg": "发布成功"
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
| 4001 | 评价内容不能为空 |
| 4002 | 评分必须在1-5之间 |
| 4003 | 文档ID无效 |
| 4004 | 未购买该商品，无法评价 |
| 4005 | 已评价过该商品 |
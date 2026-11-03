# 添加愿望清单接口

将指定商品添加到用户的愿望清单中，支持设置备注、价格、优先级等信息。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 需要提供商品ID，可选择性提供SKU ID
- 需要用户已登录，通过会话或Token验证身份
- 可以设置愿望价格、备注和优先级
- 如果商品已在愿望清单中，则可能更新现有记录

## 请求地址

```
{域名地址}/api/wishlist/add
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/wishlist/add`

## 请求语法

```
POST {域名地址}/api/wishlist/add
Content-Type: application/json
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :------------------- | :------- | :--- | :---------------------- |
| archive_id | int | 是 | 商品ID |
| sku_id | int | 否 | SKU ID，指定具体规格 |
| remark | string | 否 | 用户备注信息 |
| origin_price | int | 否 | 添加时的价格（单位：分） |
| status | int | 否 | 记录状态，默认为启用 |
| target_price | int | 否 | 愿望价格，用户期望的价格（单位：分） |
| priority | int | 否 | 优先级，数值越大优先级越高 |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |

## 使用示例

### 正常请求示例

```
POST /api/wishlist/add HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "archive_id": 123,
  "sku_id": 456,
  "remark": "生日礼物",
  "origin_price": 599900,
  "target_price": 550000,
  "priority": 1
}
```

### 正常响应示例

```json
{
  "code": 0,
  "msg": "保存成功"
}
```

### 错误请求示例 - 缺少必需参数

```
POST /api/wishlist/add HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "sku_id": 456,
  "remark": "生日礼物"
}
```

### 错误响应示例

```json
{
  "code": -1,
  "msg": "商品ID不能为空"
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
| 3001 | 商品ID不能为空 |
| 3002 | 该商品已在愿望清单中 |
| 3003 | 商品不存在 |
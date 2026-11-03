# 添加收藏接口

将指定商品添加到用户收藏列表中，支持指定商品 SKU，适用于电商功能中的收藏操作。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 需要用户登录后才能操作
- 必须指定商品 ID
- 可以通过 SKU ID 指定具体的商品规格
- 如果商品已经收藏，则会返回相应的提示信息

## 请求地址

```
{域名地址}/api/favorite/add
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/favorite/add`

## 请求语法

```
POST {域名地址}/api/favorite/add
Content-Type: application/json
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名               | 类型     | 必填| 说明                |
| :------------------- | :------- | :---------------------- |
| archive_id              | int     | 是 | 商品ID  |
| sku_id               | int   | 否| skuID            |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型   | 说明         |
| :----- | :----- | :----------- |
| code   | int    | 错误码       |
| msg    | string | 错误原因说明 |

## 使用示例

### 请求示例

```
POST /api/favorite/add HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "archive_id": 1,
  "sku_id": 1
}
```

### 响应示例

```json
{
  "code": 0,
  "msg": "收藏成功"
}
```

### 错误代码

| 错误码 | 说明                        |
| :----- | :-------------------------- |
| 0      | OK                          |
| -1     | 错误，错误原因在 msg 中指出 |
| 1001   | 未登录                      |
| 1002   | 未授权                      |
| 200    | API 请求 OK                 |

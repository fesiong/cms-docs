# 移除购物车商品接口

从购物车中移除指定商品，根据购物车 ID 删除对应的购物车记录。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 需要提供购物车记录的 ID 而不是商品 ID
- 支持登录用户和未登录用户（通过 cart token 识别）
- 删除成功后返回成功消息

## 请求地址

```
{域名地址}/api/cart/remove
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/cart/remove`

## 请求语法

```
POST {域名地址}/api/cart/remove
Content-Type: application/json
```

## 请求头

| 字段名 | 类型 | 必填 | 说明 |
| :---------------- | :------ | :--- | :-------------------- |
| cart | string | 否 | 当没有登录的时候，用此token作为用户判断 |

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名               | 类型     | 必填| 说明                |
| :------------------- | :------- | :---------------------- |
| id              | int     | 是 | 购物车ID  |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

## 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |

## 使用示例

### 请求示例

```
POST /api/cart/remove HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "id": 101
}
```

### 响应示例

```json
{
  "code": 0,
  "msg": "删除成功"
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

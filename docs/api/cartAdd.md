# 添加购物车接口

将指定商品添加到购物车中，支持指定商品 SKU、数量等信息，适用于电商功能中的购物车操作。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 支持登录用户和未登录用户（通过 cart token 识别）
- 必须指定商品 ID 和数量
- 可以通过 SKU ID 指定具体的商品规格
- 如果商品已经在购物车中，则会更新数量而不是新增

## 请求地址

```
{域名地址}/api/cart/add
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/cart/add`

## 请求语法

```
POST {域名地址}/api/cart/add
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
| archive_id              | int     | 是 | 商品ID  |
| sku_id               | int   | 否| skuID            |
| sku_values    | array           | SKU 选项值列表       |
| quantity            | int     | 是 | 数量               |
| status            | int     | 否 | 状态          |
| priority        | int      | 否| 权重                   |
| order_extra | object |   | 否 | 订单扩展字段信息          |

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
POST /api/cart/add HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "archive_id": 1,
  "sku_id": 1,
  "quantity": 2,
  "sku_values": [
    {
        "id": 153,
        "archive_id": 32,
        "option_id": 32,
        "title": "Denim",
        "option_title": "Fiber"
    },
    {
        "id": 156,
        "archive_id": 32,
        "option_id": 33,
        "title": "Small",
        "option_title": "Size"
    }
  ],
  "order_extra": {
    "gift_wrapping": true,
    "message": "生日快乐"
  }
}
```

### 响应示例

```json
{
  "code": 0,
  "msg": "保存成功"
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

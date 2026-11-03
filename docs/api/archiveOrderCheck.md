# 检查指定文档是否支付了接口

检查当前登录用户是否已购买或支付指定的文档内容，用于验证用户对付费文档的访问权限。

## 注意事项

- 此接口需要用户已登录，否则会返回未登录错误
- 仅适用于设置了付费访问的文档
- 接口返回布尔值，表示当前用户是否已支付该文档
- 未登录用户调用此接口会返回错误码 1001

## 请求地址

```
{域名地址}/api/archive/order/check
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/archive/order/check`

## 请求语法

```
GET {域名地址}/api/archive/order/check?{参数}
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明    |
| :----- | :--- | :--- | :------ |
| id     | int  | 是   | 文档 ID |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型    | 说明         |
| :----- | :------ | :----------- |
| code   | int     | 错误码       |
| msg    | string  | 错误原因说明 |
| data   | boolean | 是否支付了   |

### 请求数据示例

| 参数 | 值  |
| :--- | :-- |
| id   | 1   |

## 使用示例

### 请求示例

```
GET /api/archive/order/check?id=1 HTTP/1.1
Host: your-domain.com
Content-Type: application/json
```

### 响应示例

用户已支付文档时：
```json
{
  "code": 0,
  "msg": "",
  "data": true
}
```

用户未支付文档时：
```json
{
  "code": 0,
  "msg": "",
  "data": false
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

# 移除愿望清单接口

从用户的愿望清单中删除指定的商品记录。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 需要提供愿望清单记录ID
- 需要用户已登录，通过会话或Token验证身份
- 只能删除属于当前用户愿望清单中的记录
- 删除操作不可逆，请谨慎操作

## 请求地址

```
{域名地址}/api/wishlist/delete
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/wishlist/delete`

## 请求语法

```
POST {域名地址}/api/wishlist/delete
Content-Type: application/json
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :------------------- | :------- | :--- | :---------------------- |
| id | int | 是 | 愿望清单记录ID |

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
POST /api/wishlist/delete HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "id": 123
}
```

### 正常响应示例

```json
{
  "code": 0,
  "msg": "删除成功"
}
```

### 错误请求示例 - 未登录

```
POST /api/wishlist/delete HTTP/1.1
Host: www.aicms.com
Content-Type: application/json
```

### 未登录错误响应示例

```json
{
  "code": 1001,
  "msg": "未登录"
}
```

### 错误代码

| 错误码 | 说明 |
| :----- | :-------------------------- |
| 0 | 删除成功 |
| -1 | 错误，错误原因在 msg 中指出 |
| 1001 | 未登录 |
| 1002 | 未授权 |
| 200 | API 请求 OK |
| 3001 | 愿望清单记录ID不能为空 |
| 3002 | 愿望清单记录不存在 |
| 3003 | 无权限删除该记录 |
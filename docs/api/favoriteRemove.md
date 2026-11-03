# 移除收藏接口

移除指定商品或文档的收藏记录，支持从用户的收藏列表中删除特定项目。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 需要提供文档 ID 以指定要移除的收藏项
- 仅支持已登录用户移除自己的收藏记录
- 如果指定的文档未被收藏，则返回成功状态
- 成功移除后将不再出现在用户的收藏列表中

## 请求地址

```
{域名地址}/api/favorite/delete
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/favorite/delete`

## 请求语法

```
POST {域名地址}/api/favorite/delete
Content-Type: application/json
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :------------------- | :------- | :--- | :---------------------- |
| archive_id | int | 是 | 文档ID |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |

## 使用示例

### 请求示例

```
POST /api/favorite/delete HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "archive_id": 1
}
```

### 成功响应示例

```json
{
  "code": 0,
  "msg": "删除成功"
}
```

### 失败响应示例

```json
{
  "code": -1,
  "msg": "参数错误"
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
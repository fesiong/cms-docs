# 评论点赞接口

对指定评论进行点赞操作，增加评论的点赞数，并返回更新后的评论信息。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 需要提供有效的评论ID
- 每个IP或用户可能有限制，防止刷赞
- 需要确保域名地址正确配置
- 点赞成功后会返回更新后的评论信息及点赞数

## 请求地址

```
{域名地址}/api/comment/praise
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/comment/praise`

## 请求语法

```
POST /api/comment/praise
Content-Type: application/json
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明    |
| :----- | :--- | :--- | :------ |
| id     | int  | 是   | 评论 ID |

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
POST /api/comment/praise HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "id": 33
}
```

### 响应示例

```json
{
  "code": 0,
  "data": {
    "id": 33,
    "created_time": 1662734920,
    "updated_time": 1662735286,
    "archive_id": 140,
    "user_id": 0,
    "user_name": "AICMS",
    "ip": "127.0.0.1",
    "vote_count": 2,
    "content": "欢迎使用AICMS",
    "parent_id": 0,
    "to_uid": 0,
    "status": 0,
    "item_title": "欢迎使用AICMS",
    "parent": null,
    "active": true
  },
  "msg": "点赞成功"
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

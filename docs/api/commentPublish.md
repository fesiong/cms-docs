# 发布评论接口

允许用户对指定文档发布评论，支持普通评论和回复评论功能。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 需要提供有效的文档ID、用户名和评论内容
- 支持发布针对其他评论的回复（通过parent_id参数）
- 评论可能需要审核后才能显示（根据status字段判断）
- 需要确保域名地址正确配置
- 可能有评论频率限制，防止刷评论

## 请求地址

```
{域名地址}/api/comment/publish
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/comment/publish`

## 请求语法

```
POST /api/comment/publish
Content-Type: application/json
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名     | 类型   | 必填 | 说明          |
| :--------- | :----- | :--- | :------------ |
| archive_id | int    | 是   | 评论的文档 id |
| user_name  | string | 是   | 用户名        |
| content    | string | 是   | 评论内容      |
| parent_id  | int    | 否   | 引用的评论 ID |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型   | 说明         |
| :----- | :----- | :----------- |
| code   | int    | 错误码       |
| msg    | string | 错误原因说明 |
| data   | object | 结果内容     |

#### data 结果

| 字段名       | 类型   | 说明                        |
| :----------- | :----- | :-------------------------- |
| id           | int    | 评论 ID                     |
| parent_id    | int    | 评论的上级 ID               |
| archive_id   | int    | 文档 ID                     |
| user_name    | string | 评论用户名                  |
| user_id      | int    | 评论用户 ID                 |
| ip           | string | 评论者 IP                   |
| vote_count   | int    | 点赞数量                    |
| content      | string | 分类内容详情                |
| created_time | int    | 发布时间戳                  |
| updated_time | int    | 更新时间戳                  |
| status       | int    | 审核状态,1 已审核，0 审核中 |

## 使用示例

### 请求示例

```
POST /api/comment/publish HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "user_name": "AICMS",
  "content": "欢迎使用AICMS",
  "archive_id": 140
}
```

### 响应示例

```json
{
  "code": 0,
  "data": {
    "id": 33,
    "created_time": 1662734920,
    "updated_time": 1662734920,
    "archive_id": 140,
    "user_id": 0,
    "user_name": "AICMS",
    "ip": "127.0.0.1",
    "vote_count": 0,
    "content": "欢迎使用AICMS",
    "parent_id": 0,
    "status": 0
  },
  "msg": "发布成功"
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

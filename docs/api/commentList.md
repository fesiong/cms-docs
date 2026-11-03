# 获取评论列表接口

获取网站评论列表数据，支持按文档ID筛选、分页显示等功能，返回评论的详细信息。

## 注意事项

- 该接口用于获取网站的评论列表信息
- 支持按文档ID筛选特定文档的评论
- 支持自定义排序方式
- 支持分页显示评论数据
- 需要确保域名地址正确配置
- 只返回已审核的评论（status=1），除非有特殊权限

## 请求地址

```
{域名地址}/api/comment/list
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/comment/list`

## 请求语法

```
GET /api/comment/list
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型   | 必填 | 说明                                                                                                                                                                                                              |
| :----- | :----- | :--- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id     | int    | 否   | 文档 ID，指定的文档 ID                                                                                                                                                                                            |
| order  | string | 否   | 评论排序，默认 `id desc`                                                                                                                                                                                          |
| page   | int    | 否   | 获取指定分页内容，默认：1                                                                                                                                                                                         |
| limit  | int    | 否   | 显示数量，limit 可以指定显示数量，按多少数量来分页，比如 limit="10"则只会显示 10 条，limit 在不是分页列表的时候，支持 offset 模式，也就是 ,分隔模式，如想从第 2 条开始，获取 10 条数据，可以设置成 limit="2,10"。 |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型     | 说明         |
| :----- | :------- | :----------- |
| code   | int      | 错误码       |
| msg    | string   | 错误原因说明 |
| data   | object[] | 结果内容     |

#### data 结果 item 参数

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
GET /api/comment/list?id=71&page=1&limit=10 HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "data": [
    {
      "id": 1,
      "created_time": 1624494644,
      "updated_time": 1626076192,
      "archive_id": 71,
      "user_id": 0,
      "user_name": "crown",
      "ip": "127.0.0.1",
      "vote_count": 0,
      "content": "欢迎使用AICMS",
      "parent_id": 0,
      "to_uid": 0,
      "status": 1,
      "item_title": "",
      "parent": null,
      "active": false
    },
    {
      "id": 2,
      "created_time": 1624070973,
      "updated_time": 1635423845,
      "archive_id": 71,
      "user_id": 0,
      "user_name": "Memory",
      "ip": "127.0.0.1",
      "vote_count": 225,
      "content": "博客系统很棒",
      "parent_id": 1,
      "to_uid": 0,
      "status": 1,
      "item_title": "",
      "parent": null,
      "active": false
    }
  ],
  "msg": "",
  "total": 4
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

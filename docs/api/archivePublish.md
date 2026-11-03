# 文档发布接口

发布新的文档内容到系统中，支持设置文档的基本信息、内容、分类、标签、自定义字段等，同时可以设置发布时间、价格、库存等产品相关属性。

## 注意事项

- 此接口使用 POST 方法，Content-Type 为 application/json
- 发布文档需要用户登录并具有相应的发布权限
- 文档发布时间可以设置为未来时间，文档将在指定时间自动发布
- 自定义字段需要在文档模型中预先定义才能生效
- 文档可能需要审核，根据系统设置返回相应的审核状态

## 请求地址

```
{域名地址}/api/archive/publish
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/archive/publish`

## 请求语法

```
POST {域名地址}/api/archive/publish
Content-Type: application/json
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名         | 类型     | 必填 | 说明                                                                                                  |
| :------------- | :------- | :--- | :---------------------------------------------------------------------------------------------------- |
| title          | string   | 是   | 文档标题                                                                                              |
| content        | string   | 是   | 文档内容                                                                                              |
| category_id    | int      | 是   | 文档分类 ID                                                                                           |
| keywords       | string   | 否   | 文档关键词                                                                                            |
| description    | string   | 否   | 文档简介，250 字以内                                                                                  |
| url_token      | string   | 否   | 自定义 URL 别名，仅支持数字、英文字母                                                                 |
| images         | string[] | 否   | 文章组图，数组，可以设置最多 9 张图片，多张请重复这个字段。第一张为 logo                              |
| created_time   | int      | 否   | 格式：时间戳。 文档的发布时间，可以是未来的时间，如果是未来的时间，则文档会在等到时间到了才正式发布。 |
| tags           | string[] | 否   | 文档 Tag 标签，数组                                                                                   |
| 其他自定义字段 | any      | 否   | 如果你还传了其他自定义字段，并且文档文档模型的中存在该字段，则也支持。                                |
| price          | int      | 否   | 价格，单位分，整数                                                                                    |
| stock          | int      | 否   | 库存                                                                                                  |
| read_level     | int      | 否   | 阅读等级                                                                                              |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型   | 说明         |
| :----- | :----- | :----------- |
| code   | int    | 错误码       |
| msg    | string | 错误原因说明 |
| data   | object | 结果内容     |

#### data 结果

| 字段名  | 类型   | 说明                        |
| :------ | :----- | :-------------------------- |
| id      | int    | 文档 ID                     |
| link    | string | 文档链接                    |
| user_id | int    | 用户 ID                     |
| status  | int    | 审核状态,1 已审核，0 审核中 |

## 使用示例

### 请求示例

```
POST /api/archive/publish HTTP/1.1
Host: your-domain.com
Content-Type: application/json

{
  "title": "欢迎使用AICMS",
  "content": "<p>欢迎使用AICMS</p>",
  "category_id": 2,
  "images": [
    "https://www.aicms.com/uploads/arc1.png",
    "https://www.aicms.com/uploads/arc2.png"
  ],
  "tags": ["AICMS", "AICMS"],
  "quality": "高清"
}
```

### 响应示例

```json
{
  "code": 0,
  "data": {
    "id": 33,
    "link": "https://www.aicms.com/article/33.html",
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

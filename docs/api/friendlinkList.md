# 获取友情链接列表接口

获取网站的友情链接列表，返回所有已配置的友情链接信息，包括链接标题、URL、是否添加nofollow属性等详细信息。

## 注意事项

- 该接口采用GET方法，无需请求参数
- 返回所有已审核通过的友情链接信息
- 包含链接的基本信息和状态信息
- 支持nofollow设置，可控制SEO效果
- 返回的链接信息可用于前端展示

## 请求地址

```
{域名地址}/api/friendlink/list
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/friendlink/list`

## 请求语法

```
GET {域名地址}/api/friendlink/list
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

无

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object[] | 友情链接列表数据 |

#### data 数组元素参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| id | int | 友情链接记录ID |
| created_time | int | 创建时间戳 |
| updated_time | int | 更新时间戳 |
| title | string | 对方关键词/链接标题 |
| link | string | 对方链接URL |
| back_link | string | 对方反链页 |
| my_title | string | 我的关键词 |
| my_link | string | 我的链接URL |
| contact | string | 对方联系方式 |
| remark | string | 备注信息 |
| nofollow | int | 是否添加nofollow，0:不添加，1:添加 |
| sort | int | 排序值 |
| status | int | 状态 |
| checked_time | int | 审核时间戳 |

## 使用示例

### 请求示例

```
GET /api/friendlink/list HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": [
    {
      "id": 1,
      "created_time": 1626076270,
      "updated_time": 1652067973,
      "title": "AICMS",
      "link": "https://www.aicms.com",
      "back_link": "",
      "my_title": "",
      "my_link": "",
      "contact": "",
      "remark": "",
      "nofollow": 0,
      "sort": 1,
      "status": 4,
      "checked_time": 1652067973
    },
    {
      "id": 2,
      "created_time": 1626076270,
      "updated_time": 1652067973,
      "title": "免费取名网",
      "link": "https://www.888name.cn",
      "back_link": "",
      "my_title": "",
      "my_link": "",
      "contact": "",
      "remark": "",
      "nofollow": 0,
      "sort": 1,
      "status": 4,
      "checked_time": 1652067973
    }
  ]
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
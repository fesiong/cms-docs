# 获取城市分站列表接口

获取城市分站列表数据，支持按上级分站、是否全部分站等条件筛选，返回分站的详细信息。

## 注意事项

- 该接口用于获取城市分站列表信息
- 需要先开启城市分站插件（PluginPlace），否则接口返回未开启错误
- 支持获取指定上级分站的子分站
- 支持获取全部分站或按条件筛选
- 列表返回的分站不包含 `content` 和 `extra` 字段（详情接口才有）

## 请求地址

```
{域名地址}/api/place/list
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/place/list`

## 请求语法

```
GET /api/place/list
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名   | 类型 | 必填 | 说明                                                                                                                                                          |
| :------- | :--- | :--- | :------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| parentId | int  | 否   | 上级分站，可以获取指定上级分站下的子分站，parentId="0" 时获取顶级分站。如果不传，默认获取所有全部分站。                                                       |
| all      | bool | 否   | 是否获取全部分站，all=true 获取所有分站（包括所有层级），all=false（默认）仅获取指定 parentId 的直接子分站。                                                   |
| limit    | int  | 否   | 显示数量，limit 可以指定显示数量，按多少数量来分页，比如 limit="10" 则只会显示 10 条。limit 支持 offset 模式，即 `,` 分隔模式，如想从第 2 条开始取 10 条数据，可设置成 limit="2,10"。 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型     | 说明         |
| :----- | :------- | :----------- |
| code   | int      | 错误码       |
| msg    | string   | 错误原因说明 |
| data   | object[] | 结果内容     |

#### data 结果 item 参数

| 字段名       | 类型     | 说明                     |
| :----------- | :------- | :----------------------- |
| id           | int      | 分站 ID                  |
| title        | string   | 分站名称                 |
| seo_title    | string   | 分站 SEO 标题            |
| url_token    | string   | 分站 URL 别名            |
| keywords     | string   | 分站关键词               |
| description  | string   | 分站简介                 |
| parent_id    | int      | 上级分站 ID              |
| sort         | int      | 分站排序值               |
| images       | string[] | 分站 Banner 图           |
| logo         | string   | 分站 Logo 图             |
| thumb        | string   | 分站缩略图               |
| latitude     | float    | 纬度                     |
| longitude    | float    | 经度                     |
| timezone     | string   | 时区                     |
| status       | int      | 分站状态                 |
| has_children | bool     | 是否有下级分站           |
| is_current   | bool     | 是否为当前分站           |
| link         | string   | 分站前端链接             |
| created_time | int      | 分站发布时间戳           |
| updated_time | int      | 分站更新时间戳           |

## 使用示例

### 请求示例

获取顶级分站列表：
```
GET /api/place/list?parentId=0 HTTP/1.1
Host: www.aicms.com
```

获取指定上级分站的子分站：
```
GET /api/place/list?parentId=1 HTTP/1.1
Host: www.aicms.com
```

获取全部分站（不限层级）：
```
GET /api/place/list?all=true HTTP/1.1
Host: www.aicms.com
```

带 offset 和 limit 的分站列表：
```
GET /api/place/list?parentId=0&limit=0,10 HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "data": [
    {
      "id": 1,
      "created_time": 1607308159,
      "updated_time": 1657761249,
      "title": "广州",
      "seo_title": "",
      "keywords": "",
      "url_token": "guangzhou",
      "description": "",
      "parent_id": 0,
      "sort": 1,
      "images": [],
      "logo": "https://www.aicms.com/uploads/logo.png",
      "thumb": "https://www.aicms.com/uploads/thumb_logo.png",
      "latitude": 23.129100,
      "longitude": 113.264400,
      "timezone": "Asia/Shanghai",
      "status": 1,
      "has_children": true,
      "is_current": false,
      "link": "https://www.aicms.com/guangzhou"
    },
    {
      "id": 2,
      "created_time": 1607308159,
      "updated_time": 1657761249,
      "title": "深圳",
      "seo_title": "",
      "keywords": "",
      "url_token": "shenzhen",
      "description": "",
      "parent_id": 0,
      "sort": 2,
      "images": [],
      "logo": "",
      "thumb": "https://www.aicms.com/uploads/thumb_default.png",
      "latitude": 22.543100,
      "longitude": 114.057900,
      "timezone": "Asia/Shanghai",
      "status": 1,
      "has_children": false,
      "is_current": false,
      "link": "https://www.aicms.com/shenzhen"
    }
  ],
  "msg": ""
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

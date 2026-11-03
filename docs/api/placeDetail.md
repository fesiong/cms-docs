# 获取城市分站详情接口

获取指定城市分站的详细信息，支持通过分站 ID 或 URL 别名获取分站详情，返回分站的基本信息、内容、经纬度等。

## 注意事项

- 接口支持通过分站 ID 或 URL 别名（filename）两种方式获取分站详情
- 需要先开启城市分站插件（PluginPlace），否则接口返回未开启错误
- 分站内容支持 Markdown 渲染，可通过 `render` 参数控制
- 如果分站不存在，接口会返回错误码

## 请求地址

```
{域名地址}/api/place/detail
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/place/detail`

## 请求语法

```
GET {域名地址}/api/place/detail?{参数}
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名   | 类型   | 必填 | 说明                                      |
| :------- | :----- | :--- | :---------------------------------------- |
| id       | int    | 是   | 分站 ID，如果传了 filename，可以不用传 ID |
| filename | string | 否   | 分站 URL 别名，分站 ID、filename 二选一   |
| render   | bool   | 否   | 是否进行 Markdown 渲染，默认根据系统设置   |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型   | 说明         |
| :----- | :----- | :----------- |
| code   | int    | 错误码       |
| msg    | string | 错误原因说明 |
| data   | object | 结果内容     |

#### data 参数

| 字段名       | 类型     | 说明                     |
| :----------- | :------- | :----------------------- |
| id           | int      | 分站 ID                  |
| title        | string   | 分站名称                 |
| seo_title    | string   | 分站 SEO 标题            |
| url_token    | string   | 分站 URL 别名            |
| keywords     | string   | 分站关键词               |
| description  | string   | 分站简介                 |
| content      | string   | 分站内容详情             |
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
| link         | string   | 分站前端链接             |
| created_time | int      | 分站发布时间戳           |
| updated_time | int      | 分站更新时间戳           |
| extra        | object   | 自定义字段数据（可能为空） |
| parents      | object[] | 上级分站层级信息         |

## 使用示例

### 请求示例

通过 ID 获取分站详情：
```
GET /api/place/detail?id=1 HTTP/1.1
Host: your-domain.com
Content-Type: application/json
```

通过 URL 别名获取分站详情：
```
GET /api/place/detail?filename=guangzhou HTTP/1.1
Host: your-domain.com
Content-Type: application/json
```

### 响应示例

```json
{
  "code": 0,
  "data": {
    "id": 1,
    "created_time": 1607308159,
    "updated_time": 1657761249,
    "title": "广州",
    "seo_title": "广州分站 - AICMS",
    "keywords": "广州,城市分站",
    "url_token": "guangzhou",
    "description": "广州城市分站，提供本地化服务",
    "content": "<p>广州城市分站介绍内容</p>",
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
    "link": "https://www.aicms.com/guangzhou",
    "parents": [],
    "extra": {
      "phone": "020-12345678",
      "address": "广州市天河区"
    }
  },
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

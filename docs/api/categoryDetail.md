# 获取分类详情接口

获取指定分类的详细信息，支持通过分类 ID 或 URL 别名获取分类详情，返回分类的基本信息、内容等。

## 注意事项

- 接口支持通过分类 ID 或 URL 别名（filename/catname）两种方式获取分类详情
- 分类类型包括普通分类（type=1）和单页面（type=3）
- 返回的分类信息包含 SEO 相关字段，便于 SEO 优化
- 如果分类不存在，接口会返回错误码

## 请求地址

```
{域名地址}/api/category/detail
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/category/detail`

## 请求语法

```
GET {域名地址}/api/category/detail?{参数}
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名   | 类型   | 必填 | 说明                                      |
| :------- | :----- | :--- | :---------------------------------------- |
| id       | int    | 是   | 分类 ID，如果传了 filename，可以不用传 ID |
| filename | string | 否   | 分类 URL 别名，分类 ID、filename 二选一   |
| catname  | string | 否   | 分类 URL 别名，同 filename                |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型   | 说明         |
| :----- | :----- | :----------- |
| code   | int    | 错误码       |
| msg    | string | 错误原因说明 |
| data   | object | 结果内容     |

##### data 参数

| 字段名       | 类型     | 说明                         |
| :----------- | :------- | :--------------------------- |
| id           | int      | 分类 ID                      |
| parent_id    | int      | 分类上级 ID                  |
| title        | string   | 分类名称                     |
| seo_title    | string   | 分类 SEO 标题                |
| url_token    | string   | 分类 URL 别名                |
| keywords     | string   | 分类关键词                   |
| description  | string   | 分类简介                     |
| module_id    | int      | 模型 ID                      |
| content      | string   | 分类内容详情                 |
| type         | int      | 分类属性值，1 分类，3 单页面 |
| sort         | int      | 分类排序值                   |
| images       | string[] | 分类 Banner 图               |
| logo         | string   | 分类缩略图                   |
| thumb        | string   | 分类缩略图                   |
| created_time | int      | 分类发布时间戳               |
| updated_time | int      | 分类更新时间戳               |
| status       | int      | 分类显示状态                 |

## 使用示例

### 请求示例

通过 ID 获取分类详情：
```
GET /api/category/detail?id=1 HTTP/1.1
Host: your-domain.com
Content-Type: application/json
```

通过 URL 别名获取分类详情：
```
GET /api/category/detail?filename=help HTTP/1.1
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
    "title": "AICMS使用帮助",
    "seo_title": "",
    "keywords": "",
    "url_token": "help",
    "description": "",
    "content": "<p><br/></p>",
    "module_id": 1,
    "parent_id": 0,
    "type": 1,
    "sort": 1,
    "images": [],
    "logo": "",
    "status": 1,
    "thumb": "https://www.aicms.com/uploads/202012/7/bd36c37ef742c7be.webp"
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

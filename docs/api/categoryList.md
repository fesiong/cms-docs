# 获取分类列表接口

获取网站分类列表数据，支持按模型ID、上级分类等条件筛选，返回分类的详细信息。

## 注意事项

- 该接口用于获取网站的分类列表信息
- 支持按模型ID筛选特定模型的分类
- 支持获取指定上级分类的子分类
- 支持获取全部分类或按条件分页显示
- 需要确保域名地址正确配置

## 请求地址

```
{域名地址}/api/category/list
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/category/list`

## 请求语法

```
GET /api/category/list
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名   | 类型 | 必填 | 说明                                                                                                                                                                                                              |
| :------- | :--- | :--- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| moduleId | int  | 否   | 模型 ID，可以获取指定文档模型的分类列表如 moduleId="1" 获取文章模型的分类列表。                                                                                                                                   |
| parentId | int  | 否   | 上级分类，可以获取指定上级分类下的子分类，parentId="0"的时候，获取顶级分类。放要获取顶级分类的时候，必须指定模型 ID moduleId                                                                                      |
| all      | bool | 否   | 是否获取全部分类，all=true 获取所有分类，如果同时指定了`moduleId`，则获取指定模型下的所有分类。                                                                                                                   |
| limit    | int  | 否   | 显示数量，limit 可以指定显示数量，按多少数量来分页，比如 limit="10"则只会显示 10 条，limit 在不是分页列表的时候，支持 offset 模式，也就是 ,分隔模式，如想从第 2 条开始，获取 10 条数据，可以设置成 limit="2,10"。 |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型     | 说明         |
| :----- | :------- | :----------- |
| code   | int      | 错误码       |
| msg    | string   | 错误原因说明 |
| data   | object[] | 结果内容     |

#### data 结果 item 参数

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

```
GET /api/category/list?moduleId=1&parentId=0 HTTP/1.1
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
    {
      "id": 2,
      "created_time": 1607308159,
      "updated_time": 1657761249,
      "title": "AICMS模板手册",
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

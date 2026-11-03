# 获取模型列表接口

获取系统中所有内容模型（模块）的信息，包括模型的基本信息、自定义字段等。

## 注意事项

- 该接口采用GET方法，无需提交请求体数据
- 无需登录即可访问
- 返回结果包含系统内置模型和自定义模型
- 包含模型的自定义字段信息

## 请求地址

```
{域名地址}/api/module/list
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/module/list`

## 请求语法

```
GET {域名地址}/api/module/list
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
| data | object[] | 模型列表数据 |

#### data 结果 item 参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| id | int | 模型ID |
| title | string | 模型名称 |
| table_name | string | 附加表名 |
| url_token | string | 模型URL别名 |
| is_system | int | 是否系统内置模型(1:是,0:否) |
| title_name | string | 标题字段名称 |
| fields | object[] | 模型自定义字段列表 |
| created_time | int | 创建时间戳 |
| updated_time | int | 更新时间戳 |
| status | int | 模型显示状态(1:启用,0:禁用) |

#### 模型自定义字段 fields item 参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| name | string | 字段中文名称 |
| field_name | string | 字段英文名称 |
| type | string | 字段类型(text,textarea,int,bool等) |
| required | boolean | 是否必填 |
| is_system | boolean | 是否系统内置字段 |
| is_filter | boolean | 是否筛选参数 |
| follow_level | boolean | 是否跟随文档阅读等级 |
| content | string | 字段默认值 |

## 使用示例

### 请求示例

```
GET /api/module/list HTTP/1.1
Host: www.aicms.com
Content-Type: application/json
```

### 响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": [
    {
      "id": 1,
      "created_time": 1689603570,
      "updated_time": 1689924577,
      "table_name": "article",
      "url_token": "news",
      "title": "文章中心",
      "fields": null,
      "is_system": 1,
      "title_name": "标题",
      "status": 1
    },
    {
      "id": 2,
      "created_time": 1689603570,
      "updated_time": 1702908648,
      "table_name": "product",
      "url_token": "product",
      "title": "产品中心",
      "fields": [
        {
          "name": "产品参数",
          "field_name": "canshu",
          "type": "text",
          "required": false,
          "is_system": false,
          "is_filter": false,
          "follow_level": false,
          "content": ""
        },
        {
          "name": "批号",
          "field_name": "pihao",
          "type": "text",
          "required": false,
          "is_system": false,
          "is_filter": false,
          "follow_level": false,
          "content": ""
        }
      ],
      "is_system": 1,
      "title_name": "产品名称",
      "status": 1
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
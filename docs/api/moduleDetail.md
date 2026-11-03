# 获取模型详情接口

获取指定内容模型的详细信息，包括模型的基本信息、自定义字段配置等，用于动态表单构建和内容管理。

## 注意事项

- 该接口采用GET方法
- 通过模型ID或模型URL别名来获取模型信息
- 支持获取系统内置模型和自定义模型的详细信息
- 返回模型的自定义字段列表，用于构建动态表单
- 模型信息包含字段类型、是否必填等配置信息

## 请求地址

```
{域名地址}/api/module/detail
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/module/detail`

## 请求语法

```
GET {域名地址}/api/module/detail
```

## 请求参数

| 字段名   | 类型   | 必填 | 说明                                      |
| :------- | :----- | :--- | :---------------------------------------- |
| id       | int    | 是   | 模型 ID，如果传了 filename，可以不用传 ID |
| filename | string | 否   | 模型 URL 别名，模型 ID、filename 二选一   |

## 返回参数

| 字段名 | 类型   | 说明         |
| :----- | :----- | :----------- |
| code   | int    | 错误码       |
| msg    | string | 错误原因说明 |
| data   | object | 结果内容     |

### data 参数

| 字段名       | 类型     | 说明               |
| :----------- | :------- | :----------------- |
| id           | int      | 模型 ID            |
| title        | string   | 模型名称           |
| table_name   | string   | 附加表名           |
| url_token    | string   | 模型 URL 别名      |
| is_system    | int      | 是否系统内置模型   |
| title_name   | string   | 标题名称           |
| fields       | object[] | 模型自定义字段列表 |
| created_time | int      | 模型发布时间戳     |
| updated_time | int      | 模型更新时间戳     |
| status       | int      | 模型显示状态       |

### fields 参数（模型自定义字段）

| 字段名       | 类型    | 说明                 |
| :----------- | :------ | :------------------- |
| name         | string  | 字段中文名称         |
| field_name   | string  | 字段名称             |
| type         | string  | 字段类型             |
| required     | boolean | 是否必填             |
| is_system    | boolean | 是否系统内置字段     |
| is_filter    | boolean | 是否筛选参数         |
| follow_level | boolean | 是否跟随文档阅读等级 |
| content      | string  | 默认值               |

## 使用示例

### 通过ID获取模型详情请求示例

```
GET /api/module/detail?id=1 HTTP/1.1
Host: www.aicms.com
```

### 通过URL别名获取模型详情请求示例

```
GET /api/module/detail?filename=product HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "data": {
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
      },
      {
        "name": "产品图片",
        "field_name": "product_images",
        "type": "images",
        "required": false,
        "is_system": false,
        "is_filter": false,
        "follow_level": false,
        "content": ""
      },
      {
        "name": "产品描述",
        "field_name": "description",
        "type": "textarea",
        "required": true,
        "is_system": false,
        "is_filter": false,
        "follow_level": true,
        "content": ""
      }
    ],
    "is_system": 1,
    "title_name": "产品名称",
    "status": 1,
    "link": ""
  },
  "msg": ""
}
```

### 错误响应示例

```json
{
  "code": -1,
  "msg": "模型不存在"
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
# 获取留言表单字段接口

获取网站留言表单的字段配置信息，包括字段名称、类型、是否必填等详细信息，用于前端动态生成留言表单。

## 注意事项

- 该接口采用GET方法，无需请求参数
- 返回留言表单的所有字段配置信息
- 包含字段名称、字段类型、是否必填等属性
- 支持多种表单字段类型：文本、数字、多行文本、单选、多选、下拉选择、图片、文件等
- 可用于前端动态渲染留言表单

## 请求地址

```
{域名地址}/api/guestbook/fields
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/guestbook/fields`

## 请求语法

```
GET {域名地址}/api/guestbook/fields
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
| data | object[] | 留言表单字段列表 |

#### data 数组元素参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| name | string | 表单字段显示名称 |
| field_name | string | 表单字段调用名称 |
| type | string | 表单字段类型，text:文本、number:数字、textarea:多行文本、radio:单选、checkbox:多选、select:下拉选择、image:图片、file:文件 |
| required | boolean | 是否必填，true:必填，false:可选 |
| content | string | 表单字段默认值或选项内容 |

## 使用示例

### 请求示例

```
GET /api/guestbook/fields HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": [
    {
      "name": "用户名",
      "field_name": "user_name",
      "type": "text",
      "required": true,
      "content": ""
    },
    {
      "name": "联系电话",
      "field_name": "contact",
      "type": "text",
      "required": true,
      "content": ""
    },
    {
      "name": "留言内容",
      "field_name": "content",
      "type": "textarea",
      "required": true,
      "content": ""
    },
    {
      "name": "性别",
      "field_name": "gender",
      "type": "radio",
      "required": false,
      "content": "男\n女\n保密"
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
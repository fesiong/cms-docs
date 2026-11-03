# 获取沟通定制订单字段接口

获取沟通定制订单可用的自定义字段信息，用于在创建沟通定制订单时提供表单字段。

## 注意事项

- 该接口采用GET方法，无需提交请求体数据
- 无需登录即可访问
- 返回所有可用的沟通定制订单字段配置
- 包含字段名称、类型、是否必填等信息

## 请求地址

```
{域名地址}/api/communication/fields
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/communication/fields`

## 请求语法

```
GET {域名地址}/api/communication/fields
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

无

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object[] | 字段列表数据 |

#### data 结果 item 参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| name | string | 表单字段显示名称 |
| field_name | string | 表单字段调用名称 |
| type | string | 表单类型：text(文本)、number(数字)、textarea(多行文本)、radio(单选)、checkbox(多选)、select(下拉选择)、image(图片)、file(文件) |
| required | boolean | 是否必填，true表示必填，false表示可选 |
| content | string | 表单默认值 |

## 使用示例

### 请求示例

```
GET /api/communication/fields HTTP/1.1
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
      "name": "交付时间",
      "field_name": "delivery_time",
      "type": "text",
      "required": true,
      "content": ""
    },
    {
      "name": "特殊要求",
      "field_name": "special_requirement",
      "type": "textarea",
      "required": false,
      "content": "请详细描述您的特殊要求"
    },
    {
      "name": "预算范围",
      "field_name": "budget_range",
      "type": "select",
      "required": true,
      "content": "5000-10000,10000-20000,20000-50000"
    },
    {
      "name": "是否需要后期维护",
      "field_name": "maintenance_required",
      "type": "radio",
      "required": false,
      "content": "是,否"
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
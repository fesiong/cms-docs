# 获取文档参数接口

获取指定文档的自定义参数信息，支持按排序数组或无序 map 对象两种格式返回，用于获取文档模型中设置的额外字段信息。

## 注意事项

- 接口支持通过文档 ID 获取特定文档的参数
- 通过 sorted 参数控制返回格式：数组格式或对象格式
- 参数值以换行符分隔多个选项时，表示该字段为多选项类型

## 请求地址

```
{域名地址}/api/archive/params
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/archive/params`

## 请求语法

```
GET {域名地址}/api/archive/params?{参数}
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明                                                                                                                                                                                                              |
| :----- | :--- | :--- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id     | int  | 是   | 参数根据文档 id 获取指定的文档参数                                                                                                                                                                                |
| sorted | int  | 否   | 支持 的值有： false\|true，sorted=false 时，获取的是一个无序的 map 对象，需要用.的形式获取数据。sorted=true 时，获取是一个固定排序的数组对象。默认是 true 固定排序的数组对象，因此需要使用 for 循环来获取并输出。 |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型              | 说明         |
| :----- | :---------------- | :----------- |
| code   | int               | 错误码       |
| msg    | string            | 错误原因说明 |
| data   | object[]或 object | 结果内容     |

### sorted=true 时的 data 结果 item 信息

| 字段名 | 类型 | 说明 |
| :--- | :--- | :--- |
| name | string | 字段名称 |
| value | string | 填写的值 |
| default | string | 默认值 |

### sorted=false 时的 data 结果信息

字段结构为 key => item：
key 表单字段调用名，每个字段item 包含以下信息：

| 字段名 | 类型 | 说明 |
| :--- | :--- | :--- |
| name | string | 字段名称 |
| value | string | 填写的值 |
| default | string | 默认值 |

## 使用示例

### 请求示例

```
GET /api/archive/params?id=1&sorted=true HTTP/1.1
Host: your-domain.com
Content-Type: application/json
```

### 响应示例

#### sorted=true 时返回值

```json
{
  "code": 0,
  "data": [
    {
      "name": "作者",
      "value": "AICMS",
      "default": ""
    },
    {
      "name": "城市",
      "value": "北京\n上海\n重庆\n广州\n天津",
      "default": "北京\n上海\n重庆\n广州\n天津"
    },
    {
      "name": "学历",
      "value": "硕士\n本科\n大专\n高中\n初中",
      "default": "硕士\n本科\n大专\n高中\n初中"
    }
  ],
  "msg": ""
}
```

#### sorted=false 时返回值

```json
{
  "code": 0,
  "data": {
    "author": {
      "name": "作者",
      "value": "AICMS",
      "default": ""
    },
    "certificate": {
      "name": "学历",
      "value": "硕士\n本科\n大专\n高中\n初中",
      "default": "硕士\n本科\n大专\n高中\n初中"
    },
    "city": {
      "name": "城市",
      "value": "北京\n上海\n重庆\n广州\n天津",
      "default": "北京\n上海\n重庆\n广州\n天津"
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

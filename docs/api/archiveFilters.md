# 获取文档参数筛选条件接口

获取指定模型的文档参数筛选条件，返回模型中可用于筛选的字段及其可选项，适用于构建文档筛选功能的前端界面。

## 注意事项

- 接口需要指定模型 ID，以便获取对应模型的筛选条件
- 返回的筛选条件基于模型中设置的字段类型
- 筛选项包含总数统计，便于用户了解各选项下的文档数量

## 请求地址

```
{域名地址}/api/archive/filters
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/archive/filters`


## 请求语法

```
GET {域名地址}/api/archive/filters?{参数}
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名   | 类型 | 必填 | 说明    |
| :------- | :--- | :--- | :------ |
| moduleId | int  | 是   | 模型 ID |
| showCategory | bool | 否 | 是否显示分类筛选 |
| parentId | int | 否 | 分类筛选中上级分类ID，默认为 `0` |
| categoryId | int | 否 | 当前分类ID |
| showPrice | bool | 否 | 是否显示价格筛选 |
| allText | string | 否 | 价格筛选中全部选项的文字, 默认为 `全部` |
| showAll | bool | 否 | 价格筛选中全部选项的文字，`showAll=false` 表示不显示 |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型     | 说明         |
| :----- | :------- | :----------- |
| code   | int      | 错误码       |
| msg    | string   | 错误原因说明 |
| data   | [array[object]](#data结果参数) | 结果内容     |

#### data结果参数

| 字段名     | 类型     | 说明             |
| :--------- | :------- | :--------------- |
| name       | string   | 筛选名称         |
| field_name | string   | 筛选字段调用名称 |
| items      | [array[object]](#筛选参数列表item) | 筛选参数列表     |

##### 筛选参数列表item

| 字段名 | 类型   | 说明     |
| :----- | :----- | :------- |
| label  | string | 参数选项 |
| total  | int    | 数量     |

## 使用示例

### 请求示例

```
GET /api/archive/filters?moduleId=1 HTTP/1.1
Host: your-domain.com
Content-Type: application/json
```

### 响应示例

```json
{
  "code": 0,
  "data": [
    {
      "name": "城市",
      "field_name": "city",
      "items": [
        {
          "label": "全部",
          "total": 0
        },
        {
          "label": "北京",
          "total": 0
        },
        {
          "label": "上海",
          "total": 0
        },
        {
          "label": "重庆",
          "total": 0
        },
        {
          "label": "广州",
          "total": 0
        },
        {
          "label": "天津",
          "total": 0
        }
      ]
    },
    {
      "name": "学历",
      "field_name": "certificate",
      "items": [
        {
          "label": "全部",
          "total": 0
        },
        {
          "label": "硕士",
          "total": 0
        },
        {
          "label": "本科",
          "total": 0
        },
        {
          "label": "大专",
          "total": 0
        },
        {
          "label": "高中",
          "total": 0
        },
        {
          "label": "初中",
          "total": 0
        }
      ]
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

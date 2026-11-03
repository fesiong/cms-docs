# 获取导航列表接口

获取系统中所有导航菜单的信息，包括导航的层级结构、链接等信息。

## 注意事项

- 该接口采用GET方法，无需提交请求体数据
- 无需登录即可访问
- 支持获取指定类型的导航列表
- 返回结果包含导航的层级结构信息
- 默认获取类型ID为1的导航列表

## 请求地址

```
{域名地址}/api/nav/list
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/nav/list`

## 请求语法

```
GET {域名地址}/api/nav/list
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :---------------- | :------ | :--- | :-------------------- |
| type_id | int | 否 | 导航类型，默认为1 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object[] | 导航列表数据 |

#### data 结果 item 参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| id | int | 导航ID |
| title | string | 导航名称 |
| sub_title | string | 导航二级标题 |
| description | string | 导航文字描述 |
| parent_id | int | 上级导航ID |
| type_id | int | 导航类型 |
| nav_type | int | 导航链接类型 |
| page_id | int | 导航链接值 |
| link | string | 导航链接 |
| sort | int | 排序值 |
| status | int | 状态(1:启用,0:禁用) |
| created_time | int | 创建时间戳 |
| updated_time | int | 更新时间戳 |
| nav_list | object[] | 子导航列表 |

#### 子导航 nav_list item 参数

同主导航参数结构

## 使用示例

### 请求示例

```
GET /api/nav/list HTTP/1.1
Host: www.aicms.com
Content-Type: application/json
```

### 请求示例（指定导航类型）

```
GET /api/nav/list?type_id=1 HTTP/1.1
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
      "created_time": 1611236423,
      "updated_time": 1611236430,
      "title": "博客首页",
      "sub_title": "",
      "description": "",
      "parent_id": 0,
      "nav_type": 0,
      "page_id": 0,
      "type_id": 1,
      "link": "https://www.aicms.com/",
      "sort": 0,
      "status": 1,
      "nav_list": null
    },
    {
      "id": 4,
      "created_time": 1611236495,
      "updated_time": 1625291595,
      "title": "小程序实战开发",
      "sub_title": "",
      "description": "",
      "parent_id": 0,
      "nav_type": 1,
      "page_id": 3,
      "type_id": 1,
      "link": "https://www.aicms.com/program",
      "sort": 5,
      "status": 1,
      "nav_list": [
        {
          "id": 7,
          "created_time": 1611795528,
          "updated_time": 1611795640,
          "title": "微信小程序开发",
          "sub_title": "",
          "description": "",
          "parent_id": 4,
          "nav_type": 1,
          "page_id": 5,
          "type_id": 1,
          "link": "https://www.aicms.com/weapp",
          "sort": 1,
          "status": 1,
          "nav_list": null
        }
      ]
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
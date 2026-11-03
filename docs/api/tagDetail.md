# 获取标签详情接口

获取指定标签的详细信息，包括标签名称、SEO信息、链接地址等基本信息。

## 注意事项

- 该接口采用GET方法
- 需要提供标签ID或标签URL别名（filename）来指定查询的标签
- 标签ID和URL别名二选一，如果提供了filename参数，则可以不传ID
- 返回标签的基本信息和SEO相关信息
- 可用于页面标题、关键词和描述的设置

## 请求地址

```
{域名地址}/api/tag/detail
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/tag/detail`

## 请求语法

```
GET {域名地址}/api/tag/detail
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :----- | :----- | :--- | :--- |
| id | int | 否 | 标签ID，如果传了filename，可以不用传ID |
| filename | string | 否 | 标签URL别名，标签ID、filename二选一 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object | 标签详情数据 |

#### data 参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| id | int | 标签ID |
| title | string | 标签名称 |
| seo_title | string | 标签SEO标题 |
| url_token | string | 标签URL别名 |
| keywords | string | 标签关键词 |
| description | string | 标签简介 |
| content  | string | 标签内容 |
| first_letter | string | 标签首字母 |
| link | string | 标签链接地址 |
| created_time | int | 标签创建时间戳 |
| updated_time | int | 标签更新时间戳 |
| status | int | 标签显示状态 |

## 使用示例

### 请求示例

```
GET /api/tag/detail?id=1 HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "id": 1,
    "title": "AICMS",
    "seo_title": "",
    "url_token": "AICMS",
    "keywords": "",
    "description": "",
    "first_letter": "A",
    "link": "https://www.aicms.com/tag/1/",
     "content": "<p>AICMS 是一个基于 PHP 的开源内容管理系统，支持内容管理、内容发布、内容搜索、内容评论、内容标签、内容分类</p>"
    "created_time": 1662733318,
    "updated_time": 1662733318,
    "status": 1
  }
}
```

### 错误代码

| 错误码 | 说明 |
| :----- | :--- |
| 0 | OK |
| -1 | 错误，错误原因在 msg 中指出 |
| 1001 | 未登录 |
| 1002 | 未授权 |
| 200 | API 请求 OK |
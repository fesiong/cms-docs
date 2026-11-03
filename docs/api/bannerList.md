# 获取首页 Banner 列表接口

获取系统中指定分组的 Banner 列表，支持多个 Banner 分组，可以用于首页轮播图、广告位等展示场景。

## 注意事项

- 接口支持通过 type 参数获取不同分组的 Banner
- 默认获取 "default" 分组的 Banner 列表
- Banner 包含图片、链接、描述等信息，便于前端展示
- 接口返回的 Banner 按照后台设置的排序返回

## 请求地址

```
{域名地址}/api/banner/list
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/banner/list`

## 请求语法

```
GET {域名地址}/api/banner/list?{参数}
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型   | 必填 | 说明                                                                                         |
| :----- | :----- | :--- | :------------------------------------------------------------------------------------------- |
| type   | string | 否   | 默认值"default"，你可以在后台创建多个 banner 分组，然后通过`type`，来调用不同分组的 banner。 |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型     | 说明         |
| :----- | :------- | :----------- |
| code   | int      | 错误码       |
| msg    | string   | 错误原因说明 |
| data   | object[] | 结果内容     |

#### data 结果 item 参数

| 字段名      | 类型   | 说明          |
| :---------- | :----- | :------------ |
| id          | int    | ID            |
| logo        | string | Logo 图片地址 |
| link        | string | 链接地址      |
| alt         | string | 图片 Alt      |
| description | string | 介绍          |
| type        | string | 分组类型      |

## 使用示例

### 请求示例

获取默认分组 Banner：
```
GET /api/banner/list HTTP/1.1
Host: your-domain.com
Content-Type: application/json
```

获取指定分组 Banner：
```
GET /api/banner/list?type=home HTTP/1.1
Host: your-domain.com
Content-Type: application/json
```

### 响应示例

```json
{
  "code": 0,
  "data": [
    {
      "logo": "https://www.aicms.com/uploads/202311/13/7371e7ca18e2668d.png",
      "id": 1,
      "link": "https://www.aicms.com",
      "alt": "下载AICMS",
      "description": "欢迎下载AICMS",
      "type": "default"
    },
    {
      "logo": "https://www.aicms.com/uploads/202311/13/93c0421dca1847c6.webp",
      "id": 2,
      "link": "https://www.aicms.com/help",
      "alt": "AICMS使用帮助",
      "description": "你可以在这里找到AICMS的日常使用帮助",
      "type": "default"
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

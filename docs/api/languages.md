# 获取多语言列表接口

获取系统中所有可用的语言列表信息，包括语言标识、图标、链接等，用于多语言站点的切换功能。

## 注意事项

- 该接口采用GET方法
- 无需身份验证或特殊权限
- 返回系统中所有已配置的语言信息
- 包含当前语言标识和切换链接
- 用于多语言站点的语言切换功能

## 请求地址

```
{域名地址}/api/languages
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/languages`

## 请求语法

```
GET {域名地址}/api/languages
```

## 请求参数

无

## 返回参数

| 字段名 | 类型   | 说明         |
| :----- | :----- | :----------- |
| code   | int    | 错误码       |
| msg    | string | 错误原因说明 |
| data   | object[] | 语言列表     |

### data 参数

| 字段名        | 类型   | 说明                       |
| :------------ | :----- | :------------------------- |
| id            | int    | 站点ID                     |
| name          | string | 站点名称                   |
| language_icon | string | 语言图标                   |
| language_emoji| string | 语言符号                   |
| language_name | string | 语言名称                   |
| language      | string | 语言标识                   |
| is_current    | bool   | 是否是当前语言             |
| link          | string | 语言切换链接               |

## 使用示例

### 请求示例

```
GET /api/languages HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "data": [
    {
      "id": 1,
      "name": "简体中文",
      "language_icon": "https://www.aicms.com/uploads/language/zh-cn.png",
      "language_emoji": "🇨🇳",
      "language_name": "简体中文",
      "language": "zh-cn",
      "is_current": true,
      "link": "https://www.aicms.com/zh-cn/"
    },
    {
      "id": 2,
      "name": "English",
      "language_icon": "https://www.aicms.com/uploads/language/en.png",
      "language_emoji": "🇺🇸",
      "language_name": "English",
      "language": "en",
      "is_current": false,
      "link": "https://www.aicms.com/en/"
    },
    {
      "id": 3,
      "name": "日本語",
      "language_icon": "https://www.aicms.com/uploads/language/ja.png",
      "language_emoji": "🇯🇵",
      "language_name": "日本語",
      "language": "ja",
      "is_current": false,
      "link": "https://www.aicms.com/ja/"
    }
  ],
  "msg": ""
}
```

### 错误响应示例

```json
{
  "code": -1,
  "msg": "系统错误"
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
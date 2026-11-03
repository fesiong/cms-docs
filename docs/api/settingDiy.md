# 获取自定义内容接口

获取网站后台自定义设置的内容参数，用于获取管理员在后台自定义配置的各种参数信息。

## 注意事项

- 该接口采用GET方法
- 无需登录即可访问此接口
- 返回网站管理员在后台自定义内容设置中的配置参数
- 自定义参数根据后台设置而定，可能包含各种自定义字段
- 自定义参数名称和内容由网站管理员在后台配置决定

## 请求地址

```
{域名地址}/api/setting/diy
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/setting/diy`

## 请求语法

```
GET {域名地址}/api/setting/diy
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

无

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object | 自定义内容数据 |

#### data 参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| HelpUrl | string | 帮助页面URL（示例：自定义参数） |
| 其他自定义参数 | string/number/object | 根据后台自定义设置而定的其他参数 |

## 使用示例

### 请求示例

```
GET /api/setting/diy HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "HelpUrl": "https://www.aicms.com/help",
    "CustomField1": "自定义内容1",
    "CustomField2": "自定义内容2"
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
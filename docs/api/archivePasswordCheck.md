# 验证文档密码接口

验证访问受密码保护文档的密码是否正确，用于保护需要密码访问的文档内容。验证成功后返回文档内容，验证失败则返回错误信息。

## 注意事项

- 此接口使用 POST 方法提交验证请求
- 接口需要同时提供文档 ID 和密码进行验证
- 验证成功后会返回文档内容，验证失败则返回错误信息
- 仅适用于设置了密码保护的文档

## 请求地址

```
{域名地址}/api/archive/password/check
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/archive/password/check`

## 请求语法

```
POST {域名地址}/api/archive/password/check
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名   | 类型   | 必填 | 说明       |
| :------- | :----- | :--- | :--------- |
| id       | int    | 是   | 文档 ID    |
| password | string | 是   | 输入的密码 |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型   | 说明         |
| :----- | :----- | :----------- |
| code   | int    | 错误码       |
| msg    | string | 错误原因说明 |
| data   | object | 验证结果     |

#### 验证结果对象

| 字段名  | 类型    | 说明                             |
| :------ | :------ | :------------------------------- |
| status  | boolean | 验证结果，true/false             |
| content | string  | 文档内容，如果验证通过，则会返回 |

### 请求数据示例

| 参数     | 值     |
| :------- | :----- |
| id       | 1      |
| password | 123456 |

## 使用示例

### 请求示例

```
POST /api/archive/password/check HTTP/1.1
Host: your-domain.com
Content-Type: application/json

{
  "id": 1,
  "password": "123456"
}
```

### 响应示例

验证成功时：
```json
{
  "code": 0,
  "msg": "",
  "data": {
    "status": true,
    "content": "<p>...</p>"
  }
}
```

验证失败时：
```json
{
  "code": 0,
  "msg": "密码错误",
  "data": {
    "status": false,
    "content": ""
  }
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

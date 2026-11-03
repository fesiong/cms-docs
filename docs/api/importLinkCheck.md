# 检查友情链接是否可用接口

用于验证友情链接接口配置是否正确，检查Token是否有效，确保友情链接功能可以正常使用。

## 注意事项

- 该接口支持GET或POST方法
- 需要提供有效的后台导入接口Token进行身份验证
- 主要用于测试友情链接接口的连接状态
- 不需要额外的参数，仅验证Token的有效性

## 请求地址

```
{域名地址}/api/friendlink/check?token={token}
```

说明：`{域名地址}` 需要替换成你的域名地址，`{token}` 需要更换为后台内容导入接口功能里的Token，如 `https://www.aicms.com/api/friendlink/check?token=xxx`

## 请求语法

```
GET/POST {域名地址}/api/friendlink/check?token={token}
```

## 请求参数

### GET 参数

| 字段名 | 类型   | 必填 | 说明                           |
| :----- | :----- | :--- | :----------------------------- |
| token  | string | 是   | 后台内容导入接口功能里的 Token |

## 返回参数

| 字段名 | 类型   | 说明         |
| :----- | :----- | :----------- |
| code   | int    | 错误码       |
| msg    | string | 错误原因说明 |

## 使用示例

### 请求示例

```
GET /api/friendlink/check?token=4712a54b4c456bb29b7816d241db69a7 HTTP/1.1
Host: www.aicms.com
```

或使用POST方法：

```
POST /api/friendlink/check?token=4712a54b4c456bb29b7816d241db69a7 HTTP/1.1
Host: www.aicms.com
Content-Type: application/x-www-form-urlencoded
```

### 响应示例

```json
{
  "code": 0,
  "msg": "验证成功"
}
```

### 错误响应示例

```json
{
  "code": -1,
  "msg": "Token无效"
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
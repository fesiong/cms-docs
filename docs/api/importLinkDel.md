# 删除友情链接接口

从系统中删除指定的友情链接记录，通过链接地址来识别需要删除的友情链接。

## 注意事项

- 该接口采用POST方法，使用form-data格式提交数据
- 需要提供有效的后台导入接口Token进行身份验证
- 必须提供要删除的友情链接地址
- 删除操作不可逆，请谨慎操作
- 成功删除后会返回成功消息

## 请求地址

```
{域名地址}/api/friendlink/delete?token={token}
```

说明：`{域名地址}` 需要替换成你的域名地址，`{token}` 需要更换为后台内容导入接口功能里的 Token，如 `https://www.aicms.com/api/friendlink/delete?token=xxx`

## 请求语法

```
POST {域名地址}/api/friendlink/delete?token={token}
Content-Type: multipart/form-data
```

## 请求参数

### GET 参数

| 字段名 | 类型   | 必填 | 说明                           |
| :----- | :----- | :--- | :----------------------------- |
| token  | string | 是   | 后台内容导入接口功能里的 Token |

### POST 参数

| 字段名 | 类型   | 必填 | 说明     |
| :----- | :----- | :--- | :------- |
| link   | string | 是   | 对方链接 |

## 返回参数

| 字段名 | 类型   | 说明         |
| :----- | :----- | :----------- |
| code   | int    | 错误码       |
| msg    | string | 错误原因说明 |

## 使用示例

### 请求示例

```
POST /api/friendlink/delete?token=4712a54b4c456bb29b7816d241db69a7 HTTP/1.1
Host: www.aicms.com
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="link"

https://www.aicms.com/
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```

或使用curl命令：

```bash
curl -X POST \
  'https://www.aicms.com/api/friendlink/delete?token=4712a54b4c456bb29b7816d241db69a7' \
  -H 'Content-Type: multipart/form-data' \
  -F 'link=https://www.aicms.com/'
```

### 响应示例

```json
{
  "code": 0,
  "msg": "链接已删除"
}
```

### 错误响应示例

```json
{
  "code": -1,
  "msg": "找不到对应的友情链接"
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
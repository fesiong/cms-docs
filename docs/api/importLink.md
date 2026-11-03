# 添加友情链接接口

添加新的友情链接到系统中，支持设置nofollow属性、反链信息、联系方式等详细信息。

## 注意事项

- 该接口采用POST方法，使用form-data格式提交数据
- 需要提供有效的后台导入接口Token进行身份验证
- 至少需要提供标题和链接两个必填参数
- 支持设置nofollow属性，有助于SEO优化
- 可以记录反链信息、联系方式和备注信息

## 请求地址

```
{域名地址}/api/friendlink/create?token={token}
```

说明：`{域名地址}` 需要替换成你的域名地址，`{token}` 需要更换为后台内容导入接口功能里的 Token，如 `https://www.aicms.com/api/friendlink/create?token=xxx`

## 请求语法

```
POST {域名地址}/api/friendlink/create?token={token}
Content-Type: multipart/form-data
```

## 请求参数

### GET 参数

| 字段名 | 类型   | 必填 | 说明                           |
| :----- | :----- | :--- | :----------------------------- |
| token  | string | 是   | 后台内容导入接口功能里的 Token |

### POST 参数

| 字段名    | 类型   | 必填 | 说明                                        |
| :-------- | :----- | :--- | :------------------------------------------ |
| title     | string | 是   | 对方关键词                                  |
| link      | string | 是   | 对方链接                                    |
| nofollow  | int    | 否   | 是否添加 nofollow，可选值：0 不添加, 1 添加 |
| back_link | string | 否   | 对方反链页                                  |
| my_title  | string | 否   | 我的关键词                                  |
| my_link   | string | 否   | 我的链接                                    |
| contact   | string | 否   | 对方联系方式                                |
| remark    | string | 否   | 备注信息                                    |

## 返回参数

| 字段名 | 类型   | 说明         |
| :----- | :----- | :----------- |
| code   | int    | 错误码       |
| msg    | string | 错误原因说明 |

## 使用示例

### 请求示例

```
POST /api/friendlink/create?token=4712a54b4c456bb29b7816d241db69a7 HTTP/1.1
Host: www.aicms.com
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="title"

AICMS
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="link"

https://www.aicms.com/
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="nofollow"

1
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="contact"

contact@example.com
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```

或使用curl命令：

```bash
curl -X POST \
  'https://www.aicms.com/api/friendlink/create?token=4712a54b4c456bb29b7816d241db69a7' \
  -H 'Content-Type: multipart/form-data' \
  -F 'title=AICMS' \
  -F 'link=https://www.aicms.com/' \
  -F 'nofollow=1' \
  -F 'contact=contact@example.com'
```

### 响应示例

```json
{
  "code": 0,
  "msg": "链接已保存"
}
```

### 错误响应示例

```json
{
  "code": -1,
  "msg": "缺少必要参数"
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
# 手动更新 Sitemap 接口

手动触发系统重新生成站点地图(Sitemap)，支持同步和异步两种处理方式，用于更新搜索引擎索引。

## 注意事项

- 该接口采用POST方法，使用form-data格式提交数据
- 需要提供有效的后台导入接口Token进行身份验证
- 支持同步和异步处理模式，异步模式适合大量内容的站点
- 同步模式会等待Sitemap生成完成才返回结果
- 异步模式立即返回处理结果，后台继续执行生成任务

## 请求地址

```
{域名地址}/api/import/sitemap?token={token}
```

说明：`{域名地址}` 需要替换成你的域名地址，`{token}` 需要更换为后台内容导入接口功能里的 Token，如 `https://www.aicms.com/api/import/sitemap?token=xxx`

## 请求语法

```
POST {域名地址}/api/import/sitemap?token={token}
Content-Type: multipart/form-data
```

## 请求参数

### GET 参数

| 字段名 | 类型   | 必填 | 说明                           |
| :----- | :----- | :--- | :----------------------------- |
| token  | string | 是   | 后台内容导入接口功能里的 Token |

### POST 参数

| 字段名 | 类型   | 必填 | 说明                               |
| :----- | :----- | :--- | :--------------------------------- |
| async  | string | 否   | 是否异步处理，留空为同步，1 = 异步 |

## 返回参数

| 字段名 | 类型   | 说明         |
| :----- | :----- | :----------- |
| code   | int    | 错误码       |
| msg    | string | 错误原因说明 |
| data   | object | 结果内容     |

## 使用示例

### 请求示例

```
POST /api/import/sitemap?token=4712a54b4c456bb29b7816d241db69a7 HTTP/1.1
Host: www.aicms.com
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="async"

1
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```

或使用curl命令（异步模式）：

```bash
curl -X POST \
  'https://www.aicms.com/api/import/sitemap?token=4712a54b4c456bb29b7816d241db69a7' \
  -H 'Content-Type: multipart/form-data' \
  -F 'async=1'
```

或使用curl命令（同步模式）：

```bash
curl -X POST \
  'https://www.aicms.com/api/import/sitemap?token=4712a54b4c456bb29b7816d241db69a7' \
  -H 'Content-Type: multipart/form-data'
```

### 响应示例

同步模式成功响应：
```json
{
  "code": 0,
  "msg": "Sitemap更新完成"
}
```

异步模式成功响应：
```json
{
  "code": 0,
  "msg": "已提交后台处理，请稍后查看结果"
}
```

### 错误响应示例

```json
{
  "code": -1,
  "msg": "Token验证失败"
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
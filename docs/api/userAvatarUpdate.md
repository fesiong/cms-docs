# 上传用户头像接口

允许用户上传自定义头像图片，支持常见的图片格式，用于更新用户个人资料中的头像信息。

## 注意事项

- 该接口采用POST方法，需要以form-data格式提交数据
- 需要用户登录后才能调用此接口
- 上传的文件必须是图片格式（如JPG、PNG、WEBP等）
- 文件大小和格式可能有限制，具体取决于系统配置
- 上传成功后会自动更新当前登录用户的头像

## 请求地址

```
{域名地址}/api/user/avatar
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/user/avatar`

## 请求语法

```
POST {域名地址}/api/user/avatar
Content-Type: multipart/form-data
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :----- | :----- | :--- | :--- |
| file | File | 是 | 要上传的头像图片资源，支持常见图片格式 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object | 结果内容 |

#### data 参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| avatar_url | string | 上传后的头像图片访问地址 |

## 使用示例

### 请求示例

```
POST /api/user/avatar HTTP/1.1
Host: www.aicms.com
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="file"; filename="avatar.jpg"
Content-Type: image/jpeg

<二进制图片数据>
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```

### 响应示例

```json
{
  "code": 0,
  "msg": "上传成功",
  "data": {
    "avatar_url": "https://www.aicms.com/uploads/user/1.webp"
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
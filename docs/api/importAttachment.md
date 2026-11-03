# 导入图片资源接口

导入图片资源到系统中，支持指定资源分类、替换已有资源等功能。该接口主要用于后台内容管理系统的图片上传和管理。

## 注意事项

- 该接口采用POST方法，使用form-data格式提交数据
- 需要提供有效的后台导入接口Token进行身份验证
- 支持指定图片资源分类ID
- 支持替换已存在的图片资源（通过ID指定）
- 上传成功后返回图片的详细信息和访问地址

## 请求地址

```
{域名地址}/attachment/upload?token={token}
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/attachment/upload?token={token}`

## 请求语法

```
POST {域名地址}/attachment/upload?token={token}
Content-Type: multipart/form-data
```

## 请求参数

### GET 参数

| 字段名 | 类型   | 必填 | 说明                           |
| :----- | :----- | :--- | :----------------------------- |
| token  | string | 是   | 后台内容导入接口功能里的 Token |

### POST 参数

| 字段名      | 类型 | 必填 | 说明                                  |
| :---------- | :--- | :--- | :------------------------------------ |
| category_id | int  | 否   | 图片资源类别 ID                       |
| id          | int  | 否   | 图片资源 ID，如果是替换图片的话，必填 |
| file        | File | 是   | 要上传的文件资源                      |

## 返回参数

| 字段名 | 类型   | 说明         |
| :----- | :----- | :----------- |
| code   | int    | 错误码       |
| msg    | string | 错误原因说明 |
| data   | object | 结果内容     |

### data 参数

| 字段名        | 类型   | 说明                         |
| :------------ | :----- | :--------------------------- |
| id            | int    | 资源 ID                      |
| file_name     | string | 文件名                       |
| file_location | string | 文件存储路径                 |
| file_size     | int    | 文件大小                     |
| file_md5      | string | 文件 MD5                     |
| width         | int    | 图片宽度                     |
| height        | int    | 图片高度                     |
| category_id   | int    | 资源类别 ID                  |
| is_image      | int    | 是否是图片，1 是图片，0 不是 |
| logo          | string | 原图                         |
| thumb         | string | 缩略图                       |
| created_time  | int    | 创建时间戳                   |
| updated_time  | int    | 更新时间戳                   |
| status        | int    | 显示状态                     |

## 使用示例

### 请求示例

```bash
curl -X POST \
  'https://www.aicms.com/attachment/upload?token=your_token_here' \
  -H 'Content-Type: multipart/form-data' \
  -F 'category_id=1' \
  -F 'file=@/path/to/your/image.jpg'
```

或使用表单方式：

```
POST /attachment/upload?token=your_token HTTP/1.1
Host: www.aicms.com
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="category_id"

1
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="file"; filename="example.jpg"
Content-Type: image/jpeg

(file content)
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```

### 响应示例

```json
{
  "code": 0,
  "data": {
    "id": 213,
    "created_time": 1662734332,
    "updated_time": 1662734332,
    "file_name": "example.jpg",
    "file_location": "uploads/202209/09/5632dd13c746a365.webp",
    "file_size": 9348,
    "file_md5": "4fae2c295632dd13c746a3653227f93a",
    "width": 160,
    "height": 160,
    "category_id": 1,
    "is_image": 1,
    "status": 1,
    "logo": "https://www.aicms.com/uploads/202209/09/5632dd13c746a365.webp",
    "thumb": "https://www.aicms.com/uploads/202209/09/thumb_5632dd13c746a365.webp"
  },
  "msg": ""
}
```

### 错误响应示例

```json
{
  "code": -1,
  "msg": "文件类型不允许上传"
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
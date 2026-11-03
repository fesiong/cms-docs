# 上传图片资源接口

上传图片或其他文件资源到系统中，支持指定资源分类，可用于替换已有资源。系统会自动处理图片尺寸并生成缩略图。

## 注意事项

- 此接口使用 POST 方法，Content-Type 为 form-data
- 上传文件需要用户登录并具有相应的上传权限
- 支持上传图片文件，系统会自动获取图片尺寸信息
- 可以通过指定 id 参数来替换已有资源
- 系统会自动生成缩略图并计算文件 MD5 值

## 请求地址

```
{域名地址}/api/attachment/upload
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/attachment/upload`

## 请求语法

```
POST {域名地址}/api/attachment/upload
Content-Type: multipart/form-data
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名      | 类型 | 必填 | 说明                                  |
| :---------- | :--- | :--- | :------------------------------------ |
| category_id | int  | 否   | 图片资源类别 ID                       |
| id          | int  | 否   | 图片资源 ID，如果是替换图片的话，必填 |
| file        | File | 是   | 要上传的文件资源                      |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型   | 说明         |
| :----- | :----- | :----------- |
| code   | int    | 错误码       |
| msg    | string | 错误原因说明 |
| data   | object | 结果内容     |

#### data 参数

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

```
POST /api/attachment/upload HTTP/1.1
Host: your-domain.com
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
    "file_name": "AICMS",
    "file_location": "uploads/202209/09/5632dd13c746a365.webp",
    "file_size": 9348,
    "file_md5": "4fae2c295632dd13c746a3653227f93a",
    "width": 160,
    "height": 160,
    "category_id": 0,
    "is_image": 1,
    "status": 1,
    "logo": "https://www.aicms.com/uploads/202209/09/5632dd13c746a365.webp",
    "thumb": "https://www.aicms.com/uploads/202209/09/thumb_5632dd13c746a365.webp"
  },
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

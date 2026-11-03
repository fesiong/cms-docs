# 生成小程序码接口

生成小程序码（二维码），用于在微信小程序中快速进入指定页面，支持携带场景参数。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 需要提供小程序路径和场景参数
- 生成的小程序码可用于分享和推广
- 部分参数有长度和格式限制
- 需要配置小程序相关信息才能正常使用

## 请求地址

```
{域名地址}/api/weapp/qrcode
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/weapp/qrcode`

## 请求语法

```
POST {域名地址}/api/weapp/qrcode
Content-Type: application/json
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :------------------- | :------- | :--- | :---------------------- |
| path | string | 是 | 小程序页面路径，如 `/pages/index/index` |
| scene | string | 是 | 场景参数，用于传递自定义数据，最长32个字符 |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | string | 生成的小程序码图片URL地址 |

## 使用示例

### 请求示例

```
POST /api/weapp/qrcode HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "path": "/pages/product/detail",
  "scene": "product_id=123"
}
```

### 响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": "https://www.aicms.com/uploads/qrcode/2023/12/123456789.jpg"
}
```

### 错误请求示例

```
POST /api/weapp/qrcode HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "path": "",
  "scene": "product_id=123"
}
```

### 错误响应示例

```json
{
  "code": -1,
  "msg": "path参数不能为空"
}
```

### 错误代码

| 错误码 | 说明 |
| :----- | :-------------------------- |
| 0 | OK |
| -1 | 错误，错误原因在 msg 中指出 |
| 1001 | 未登录 |
| 1002 | 未授权 |
| 200 | API 请求 OK |
| 3001 | path参数不能为空 |
| 3002 | scene参数格式错误 |
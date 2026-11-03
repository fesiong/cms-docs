# 调用图形验证码接口

获取图形验证码，返回包含验证码图片的 base64 编码和验证码 ID，用于防止自动化攻击和机器人注册等场景。

## 注意事项

- 接口无需任何请求参数
- 返回的验证码图片以 base64 编码格式提供，可以直接在前端显示
- 验证码 ID 用于后续验证请求，需要妥善保存
- 验证码具有时效性，过期后需要重新获取

## 请求地址

```
{域名地址}/api/captcha
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/captcha`

## 请求语法

```
GET {域名地址}/api/captcha
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

## 请求参数

无

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型   | 说明         |
| :----- | :----- | :----------- |
| code   | int    | 错误码       |
| msg    | string | 错误原因说明 |
| data   | object | captcha 内容 |

#### data 参数

| 字段名     | 类型   | 说明                                   |
| :--------- | :----- | :------------------------------------- |
| captcha    | string | captcha 图形验证码的 base64 编码字符串 |
| captcha_id | string | captcha 图形验证码的 ID                |

## 使用示例

### 请求示例

```
GET /api/captcha HTTP/1.1
Host: your-domain.com
Content-Type: application/json
```

### 响应示例

```json
{
  "code": 0,
  "data": {
    "captcha": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAPAAAABMCAIAAADcP63LAAAVH0lEQVR4nO",
    "captcha_id": "g0HFYRQUrC9rYbX2EZMH"
  },
  "msg": ""
}
```

响应中的 `captcha` 字段是完整的 base64 编码图片数据，可以直接用于前端显示：
```html
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAPAAAABMCAIAAADcP63LAAAVH0lEQVR4nO" />
```

### 错误代码

| 错误码 | 说明                        |
| :----- | :-------------------------- |
| 0      | OK                          |
| -1     | 错误，错误原因在 msg 中指出 |
| 1001   | 未登录                      |
| 1002   | 未授权                      |
| 200    | API 请求 OK                 |

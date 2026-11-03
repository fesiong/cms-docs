# 获取联系方式接口

获取网站的联系方式信息，包括联系人、联系电话、地址、邮箱等基本信息以及自定义的联系方式参数。

## 注意事项

- 该接口采用GET方法
- 无需登录即可访问此接口
- 返回网站管理员在后台设置的联系方式信息
- 包含基本联系方式和自定义联系方式字段
- 自定义参数根据后台设置而定，可能包含WhatsApp等其他联系方式

## 请求地址

```
{域名地址}/api/setting/contact
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/setting/contact`

## 请求语法

```
GET {域名地址}/api/setting/contact
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

无

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object | 联系方式数据 |

#### data 参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| UserName | string | 联系人姓名 |
| Cellphone | string | 联系电话 |
| Address | string | 联系地址 |
| Email | string | 联系邮箱 |
| Wechat | string | 微信联系方式 |
| Qrcode | string | 微信二维码图片地址 |
| WhatsApp | string | WhatsApp联系方式（示例：自定义参数） |

## 使用示例

### 请求示例

```
GET /api/setting/contact HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "UserName": "张大仙",
    "Cellphone": "13888888888",
    "Address": "广东省深圳市南山区深南大道xxx号",
    "Email": "61470255@qq.com",
    "Wechat": "13888888888",
    "Qrcode": "https://www.aicms.com/uploads/202209/06/64d0c4ee3e877dd6.webp",
    "WhatsApp": "+8613888888888"
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
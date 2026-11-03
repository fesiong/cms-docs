# 邮件订阅接口

用户提交邮箱地址进行邮件订阅，用于接收网站的最新资讯、更新通知或其他邮件内容。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 需要提供有效的邮箱地址
- 支持为订阅者添加备注信息和分类
- 订阅成功后用户将收到邮件确认或直接加入订阅列表
- 邮箱地址需要进行格式验证

## 请求地址

```
{域名地址}/api/subscription
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/subscription`

## 请求语法

```
POST {域名地址}/api/subscription
Content-Type: application/json
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :----- | :----- | :--- | :--- |
| email | string | 是 | 邮箱地址，用于接收订阅邮件 |
| remark | string | 否 | 备注内容，可选的用户备注信息 |
| status | int | 否 | 订阅状态，用于标识订阅者状态 |
| category_id | int | 否 | 订阅者分类ID，用于将订阅者归类 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |

## 使用示例

### 请求示例

```
POST /api/subscription HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "email": "AICMS@qq.com",
  "remark": "来自网站首页订阅",
  "category_id": 1
}
```

### 响应示例

```json
{
  "code": 0,
  "msg": "订阅成功"
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
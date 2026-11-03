# 更新分销员真实姓名接口

更新分销员的真实姓名信息，用于修改分销员账户中的实名认证信息。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 需要用户登录后才能调用此接口
- 只有分销员身份的用户可以更新自己的真实姓名
- 真实姓名更新可能需要进行实名认证验证

## 请求地址

```
{域名地址}/api/retailer/update
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/retailer/update`

## 请求语法

```
POST {域名地址}/api/retailer/update
Content-Type: application/json
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :----- | :----- | :--- | :--- |
| real_name | string | 否 | 分销员真实姓名，如不提供则不更新此项 |

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
POST /api/retailer/update HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "real_name": "张三"
}
```

### 响应示例

```json
{
  "code": 0,
  "msg": "保存成功"
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
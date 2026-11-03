# 申请提现接口

提交分销员的提现申请，将账户余额提取到指定的银行账户或支付平台。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 需要用户登录后才能调用此接口
- 提现金额需要符合系统设定的最低提现额度
- 提现申请提交后需要等待管理员审核处理
- 需要确保账户余额充足且符合提现条件

## 请求地址

```
{域名地址}/api/retailer/withdraw
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/retailer/withdraw`

## 请求语法

```
POST {域名地址}/api/retailer/withdraw
Content-Type: application/json
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

此接口无特殊请求参数。

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型   | 说明         |
| :----- | :----- | :----------- |
| code   | int    | 错误码       |
| msg    | string | 错误原因说明 |

## 使用示例

### 请求示例

```
POST /api/retailer/withdraw HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{}
```

### 响应示例

```json
{
  "code": 0,
  "msg": "提现申请已提交"
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
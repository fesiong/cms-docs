# 领取优惠券接口

允许用户领取指定的优惠券，通过提供优惠券ID来获取优惠券。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 需要提供有效的优惠券ID
- 用户需要登录才能领取优惠券
- 优惠券可能有领取数量限制或时间限制
- 需要确保域名地址正确配置
- 同一用户可能无法重复领取同一张优惠券

## 请求地址

```
{域名地址}/api/coupon/code
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/coupon/code`

## 请求语法

```
POST /api/coupon/code
Content-Type: application/json
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

## 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :--- | :--- | :--- | :--- |
| id | int | 是 | 优惠券ID |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

## 返回参数

| 字段名 | 类型 | 说明 |
| :--- | :--- | :--- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |

## 使用示例

### 请求示例

```
POST /api/coupon/code HTTP/1.1
Host: www.aicms.com
Content-Type: application/x-www-form-urlencoded

{
  "id": 1
}
```

### 响应示例

```json
{
  "code": 0,
  "msg": "领取成功"
}
```

## 错误码

| 错误码 | 说明 |
| :--- | :--- |
| 0 | OK |
| -1 | 错误，错误原因在 msg 中指出 |
| 1001 | 未登录 |
| 1002 | 未授权 |
| 200 | API 请求 OK |
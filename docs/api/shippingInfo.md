# 获取配送信息接口

获取系统配置的配送相关信息。

## 请求地址

```
{域名地址}/api/shipping/info
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/shipping/info`

## 请求语法

```
GET {域名地址}/api/shipping/info
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

无

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型     | 说明                  |
| :----- | :------- | :-------------------- |
| code   | int      | 错误码                |
| msg    | string   | 错误原因说明          |
| data   | object   | 配送信息配置          |

#### data 结果 item 参数

| 字段名              | 类型    | 说明                  |
| :------------------ | :------ | :-------------------- |
| free_shipping_amount | int    | 免运费金额，单位分    |
| default_shipping_fee | int    | 默认运费，单位分      |
| weight_unit         | string  | 重量单位              |
| length_unit         | string  | 长度单位              |
| volume_weight_ratio | float   | 体积重量系数          |
| enable_international | bool   | 是否支持国际配送      |
| estimated_delivery_days | string | 预计配送天数描述      |

## 使用示例

### 请求示例

```
GET /api/shipping/info HTTP/1.1
Host: your-domain.com
Content-Type: application/json
```

### 响应示例

```json
{
  "code": 0,
  "data": {
    "free_shipping_amount": 9900,
    "default_shipping_fee": 1000,
    "weight_unit": "kg",
    "length_unit": "cm",
    "volume_weight_ratio": 6000,
    "enable_international": false,
    "estimated_delivery_days": "3-5 个工作日"
  },
  "msg": ""
}
```

### 错误代码

| 错误码 | 说明                        |
| :----- | :-------------------------- |
| 0      | OK                          |
| -1     | 错误，错误原因在 msg 中指出 |
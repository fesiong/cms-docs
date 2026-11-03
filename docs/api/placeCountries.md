# 获取国家列表接口

获取支持的国家列表，用于地址补全功能。

## 请求地址

```
{域名地址}/api/place/countries
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/place/countries`

## 请求语法

```
GET {域名地址}/api/place/countries
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
| data   | object[] | 国家列表              |

#### data 结果 item 参数

| 字段名         | 类型    | 说明                  |
| :------------- | :------ | :-------------------- |
| id             | int     | 国家 ID               |
| name           | string  | 国家名称              |
| iso3           | string  | ISO3 代码（如 CHN）   |
| iso2           | string  | ISO2 代码（如 CN）    |
| phone_code     | string  | 国际电话区号          |
| capital        | string  | 首都                  |
| currency       | string  | 货币代码（如 CNY）    |
| native         | string  | 国家母语名称          |
| emoji          | string  | 国家国旗 emoji        |
| latitude       | string  | 纬度                  |
| longitude      | string  | 经度                  |

## 使用示例

### 请求示例

```
GET /api/place/countries HTTP/1.1
Host: your-domain.com
Content-Type: application/json
```

### 响应示例

```json
{
  "code": 0,
  "data": [
    {
      "id": 48,
      "name": "China",
      "iso3": "CHN",
      "iso2": "CN",
      "phone_code": "+86",
      "capital": "Beijing",
      "currency": "CNY",
      "native": "中国",
      "emoji": "🇨🇳",
      "latitude": "35.86166",
      "longitude": "104.195397"
    },
    {
      "id": 236,
      "name": "United States",
      "iso3": "USA",
      "iso2": "US",
      "phone_code": "+1",
      "capital": "Washington",
      "currency": "USD",
      "native": "United States",
      "emoji": "🇺🇸",
      "latitude": "37.09024",
      "longitude": "-95.712891"
    }
  ],
  "msg": ""
}
```

### 错误代码

| 错误码 | 说明                        |
| :----- | :-------------------------- |
| 0      | OK                          |
| -1     | 错误，错误原因在 msg 中指出 |
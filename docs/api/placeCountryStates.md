# 获取国家省份/州列表接口

获取指定国家下的省份或州列表，用于地址补全功能。

## 请求地址

```
{域名地址}/api/place/country/states
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/place/country/states`

## 请求语法

```
GET {域名地址}/api/place/country/states?{参数}
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名        | 类型    | 必填 | 说明            |
| :------------ | :------ | :--- | :-------------- |
| country_code  | string  | 否   | 国家代码（二选一） |
| country_name  | string  | 否   | 国家名称（二选一） |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型     | 说明                  |
| :----- | :------- | :-------------------- |
| code   | int      | 错误码                |
| msg    | string   | 错误原因说明          |
| data   | object[] | 省份/州列表           |

#### data 结果 item 参数

| 字段名         | 类型    | 说明                  |
| :------------- | :------ | :-------------------- |
| id             | int     | 省份/州 ID            |
| name           | string  | 省份/州名称          |
| iso2           | string  | ISO2 代码             |
| latitude       | string  | 纬度                  |
| longitude      | string  | 经度                  |

## 使用示例

### 请求示例

```
GET /api/place/country/states?country_code=CN HTTP/1.1
Host: your-domain.com
Content-Type: application/json
```

### 响应示例

```json
{
  "code": 0,
  "data": [
    {
      "id": 12,
      "name": "Beijing",
      "iso2": "BJ",
      "latitude": "39.9042",
      "longitude": "116.4074"
    },
    {
      "id": 13,
      "name": "Shanghai",
      "iso2": "SH",
      "latitude": "31.2304",
      "longitude": "121.4737"
    },
    {
      "id": 21,
      "name": "Guangdong",
      "iso2": "GD",
      "latitude": "23.1291",
      "longitude": "113.2644"
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
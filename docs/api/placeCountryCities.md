# 获取城市列表接口

获取指定国家或省份下的城市列表，用于地址补全功能。

## 请求地址

```
{域名地址}/api/place/country/cities
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/place/country/cities`

## 请求语法

```
GET {域名地址}/api/place/country/cities?{参数}
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名        | 类型    | 必填 | 说明            |
| :------------ | :------ | :--- | :-------------- |
| country_code  | string  | 否   | 国家代码（二选一） |
| country_name  | string  | 否   | 国家名称（二选一） |
| state_code    | string  | 否   | 省份/州代码（可选） |
| state_name    | string  | 否   | 省份/州名称（可选） |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型     | 说明                  |
| :----- | :------- | :-------------------- |
| code   | int      | 错误码                |
| msg    | string   | 错误原因说明          |
| data   | object[] | 城市列表              |

#### data 结果 item 参数

| 字段名         | 类型    | 说明                  |
| :------------- | :------ | :-------------------- |
| id             | int     | 城市 ID               |
| name           | string  | 城市名称              |
| latitude       | string  | 纬度                  |
| longitude      | string  | 经度                  |

## 使用示例

### 请求示例

```
GET /api/place/country/cities?country_code=CN&state_code=GD HTTP/1.1
Host: your-domain.com
Content-Type: application/json
```

### 响应示例

```json
{
  "code": 0,
  "data": [
    {
      "id": 1,
      "name": "Guangzhou",
      "latitude": "23.1291",
      "longitude": "113.2644"
    },
    {
      "id": 2,
      "name": "Shenzhen",
      "latitude": "22.5431",
      "longitude": "114.0579"
    },
    {
      "id": 3,
      "name": "Dongguan",
      "latitude": "22.9917",
      "longitude": "113.7352"
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
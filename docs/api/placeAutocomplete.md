# 地址自动补全接口

使用 Google Places API 进行地址自动补全，需要在系统设置中配置 Google Places API Key。

## 请求地址

```
{域名地址}/api/place/autocomplete
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/place/autocomplete`

## 请求语法

```
POST {域名地址}/api/place/autocomplete
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名                | 类型     | 必填 | 说明                              |
| :-------------------- | :------- | :--- | :-------------------------------- |
| input                 | string   | 是   | 用户输入的搜索字符串              |
| languageCode          | string   | 否   | 语言代码，如 zh-CN                |
| regionCode            | string   | 否   | 国家/地区代码，如 CN              |
| includedRegionCodes   | array    | 否   | 限定的国家/地区代码列表           |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型     | 说明                  |
| :----- | :------- | :-------------------- |
| code   | int      | 错误码                |
| msg    | string   | 错误原因说明          |
| data   | object   | Google Places API 返回的自动补全结果 |

## 使用示例

### 请求示例

```json
POST /api/place/autocomplete HTTP/1.1
Host: your-domain.com
Content-Type: application/json

{
  "input": "Guangzhou",
  "languageCode": "zh-CN",
  "regionCode": "CN"
}
```

### 响应示例

```json
{
  "code": 0,
  "data": {
    "suggestions": [
      {
        "place": {
          "formattedAddress": "Guangzhou, Guangdong, China",
          "displayName": {
            "text": "Guangzhou",
            "languageCode": "zh-CN"
          },
          "location": {
            "latitude": 23.1291,
            "longitude": 113.2644
          }
        }
      }
    ]
  },
  "msg": ""
}
```

### 错误代码

| 错误码 | 说明                        |
| :----- | :-------------------------- |
| 0      | OK                          |
| -1     | 错误，错误原因在 msg 中指出 |
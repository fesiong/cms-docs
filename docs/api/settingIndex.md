# 获取首页 TDK 接口

获取网站首页的SEO信息，包括标题(Title)、关键词(Keywords)和描述(Description)等TDK配置信息。

## 注意事项

- 该接口采用GET方法
- 无需登录即可访问此接口
- 返回网站管理员在后台设置的首页SEO配置信息
- TDK信息用于SEO优化，包含首页标题、关键词和描述
- 这些信息通常用于浏览器标签页标题和搜索引擎展示

## 请求地址

```
{域名地址}/api/setting/index
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/setting/index`

## 请求语法

```
GET {域名地址}/api/setting/index
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
| data | object | 首页TDK数据 |

#### data 参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| SeoTitle | string | 首页SEO标题 |
| SeoKeywords | string | 首页SEO关键词 |
| SeoDescription | string | 首页SEO描述 |

## 使用示例

### 请求示例

```
GET /api/setting/index HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "SeoTitle": "AI内容管理系统(AICMS):一款使用 GoLang 开发的企业站内容管理系统",
    "SeoKeywords": "企业建站系统,内容管理系统,网站安全,AICMS,AICMS",
    "SeoDescription": "AICMS 除了适合做企业站，也适合做营销型网站、企业官网、商品展示站点、政府网站、门户网站、个人博客等等各种类型的网站。AICMS 是什么，AICMS 是一个可以自由使用并开放源码的内容管理系统，你可以拿 AICMS 来搭建各种不违法的网站。"
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
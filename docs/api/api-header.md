# 公共 HTTP 头定义

本文介绍了 AICMS 接口的公共请求头和公共响应头的详细说明。

## 公共请求头（Common Request Headers）

AICMS 的 RESTful 接口中使用了一些公共请求头，这些请求头可以被所有的 API 请求使用，其详细定义请参见下表。

|名称|类型|示例值|描述|
|:---|:---|:---|:---|
|Token|string|eyJhbGciOiJIUzI1NiIsIn....|在非匿名请求中，用于验证请求合法性的认证信息。<br>token有两种，一种是导入文档使用的，通过后台导入功能获取，另一种是用户操作使用的，通过用户登录接口返回的JSON中获取。<br> 默认值：无|
|Site-Id|int|1|站点ID。<br>默认值：无|
|Content-Length|int|556|[RFC 2616](https://www.ietf.org/rfc/rfc2616.txt) 中定义的HTTP请求内容长度。<br>默认值：无|
|Content-Type|string|application/json|[RFC 2616](https://www.ietf.org/rfc/rfc2616.txt) 中定义的HTTP请求内容类型。<br>默认值：无|
|Date|string|Wed, 08 Jul 2020 07:05:05 GMT|HTTP 1.1 协议中规定的GMT时间。<br>默认值：无|
|Host|string|api.aicms.com|[RFC 2616](https://www.ietf.org/rfc/rfc2616.txt) 中定义的HTTP请求头中的Host字段。<br>默认值：无|
|Accept|string|application/json|[RFC 2616](https://www.ietf.org/rfc/rfc2616.txt) 中定义的HTTP请求头中的Accept字段。<br>默认值：无|

## 公共响应头（Common Response Headers）

AICMS 的 RESTful 接口中使用了一些公共响应头，这些响应头可以被所有的 API 请求使用，其详细定义请参见下表。

|名称|类型|示例值|描述|
|:---|:---|:---|:---|
|Update-Token|string|eyJhbGciOiJIUzI1NiIsIn....|当 Token 即将过期，程序会通过 header 下发新的 Token 来维持 Token 的有效性，防止正在访问的用户因为 Token 到期而被要求重新登录的问题。该 Token 有效期仅有1小时。<br>请接收到 Update-token 后将它替换原 Token 进行存储使用。<br> 默认值：无|
|Content-Length|int|556|[RFC 2616](https://www.ietf.org/rfc/rfc2616.txt) 中定义的HTTP请求内容长度。<br>默认值：无|
|Content-Type|string|application/json|[RFC 2616](https://www.ietf.org/rfc/rfc2616.txt) 中定义的HTTP请求内容类型。<br>默认值：无|
|Date|string|Wed, 08 Jul 2020 07:05:05 GMT|HTTP 1.1 协议中规定的GMT时间。<br>默认值：无|
|Connection|string|keep-alive|[RFC 2616](https://www.ietf.org/rfc/rfc2616.txt) 中定义的HTTP请求头中的Connection字段。<br>默认值：无|
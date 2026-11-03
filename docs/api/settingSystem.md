# 获取系统设置接口

获取网站的基本系统配置信息，包括网站名称、Logo、备案号、版权信息等系统级设置参数。

## 注意事项

- 该接口采用GET方法
- 无需登录即可访问此接口
- 返回网站管理员在后台系统设置中的基本配置信息
- 包含网站基础信息和自定义系统参数
- 系统设置信息用于网站基础功能和显示配置

## 请求地址

```
{域名地址}/api/setting/system
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/setting/system`

## 请求语法

```
GET {域名地址}/api/setting/system
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
| data | object | 系统设置数据 |

#### data 参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| SiteName | string | 网站名称 |
| SiteLogo | string | 网站Logo图片地址 |
| SiteIcp | string | 网站备案号 |
| SiteCopyright | string | 版权内容 |
| BaseUrl | string | 网站首页地址 |
| MobileUrl | string | 网站手机端地址 |
| TemplateUrl | string | 模板静态文件地址 |
| AdminUrl | string | 管理后台地址 |
| Language | string | 网站语言设置 |
| SiteClose | int | 网站关闭状态，0-开启，1-关闭 |
| SiteCloseTips | string | 网站关闭提示信息 |
| TemplateName | string | 当前模板名称 |
| TemplateType | int | 模板类型 |
| HelpUrl | string | 帮助页面URL（示例：自定义参数） |

## 使用示例

### 请求示例

```
GET /api/setting/system HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "SiteName": "这是网站标题2",
    "SiteLogo": "http://www.aicms.com/uploads/20225/22/555288fdec958ee7.webp",
    "SiteIcp": "粤ICP备12345678号",
    "SiteCopyright": "<p>版权所有，仿冒必究</p>",
    "BaseUrl": "http://www.aicms.com",
    "MobileUrl": "https://m.aicms.com/",
    "TemplateUrl": "",
    "AdminUrl": "",
    "Language": "zh",
    "SiteClose": 0,
    "SiteCloseTips": "",
    "TemplateName": "default",
    "TemplateType": 0,
    "HelpUrl": "https://www.aicms.com/help"
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
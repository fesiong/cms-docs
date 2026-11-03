# 系统标签

说明：用于获取系统配置信息

使用方法：`{% system 变量名称 with name="字段名称" %}`，变量名称不是必须的，设置了变量名称后，后续可以通过变量名称来调用，而不设置变量名称，则是直接输出结果。

### system 支持的参数有

- 站点 ID `siteId`
  `siteId` 一般不需要填写，如果你使用后台的多站点管理创建了多个站点，并且想调用其他站点的数据，则可以通过指定 `siteId` 来实现调用指定站点的数据。

name 参数可用的字段名称有：

- 网站名称 `SiteName`
- 网站 Logo `SiteLogo`
- 网站备案号 `SiteIcp`
- 版权内容 `SiteCopyright`
- 网站首页地址 `BaseUrl`
- 网站手机端地址 `MobileUrl`
- 模板静态文件地址 `TemplateUrl`
- 模板目录名 `TemplateName`
- 闭站提示内容 `SiteCloseTips`
- 站点语言 `Language`
- 自定义参数 `后台自定义设置的参数名`

### 网站名称 `SiteName`

标签用法：`{% system with name="SiteName" %}`

```twig
{# 默认用法 #}
<div>网站名称：{% system with name="SiteName" %}</div>
{# 自定义名称调用 #}
<div>网站名称：{% system siteName with name="SiteName" %}{{siteName}}</div>
```

### 网站 Logo `SiteLogo`

标签用法：`{% system with name="SiteLogo" %}`

```twig
{# 默认用法 #}
<img src="{% system with name="SiteLogo" %}" alt="{% system with name="SiteName" %}" />
{# 自定义名称调用 #}
<img src="{% system siteLogo with name="SiteLogo" %}{{siteLogo}}" alt="{% system siteName with name="SiteName" %}{{siteName}}" />
```

### 网站备案号 `SiteIcp`

标签用法：`{% system with name="SiteIcp" %}`

```twig
{# 默认用法 #}
<p><a href="https://beian.miit.gov.cn/" rel="nofollow" target="_blank">{% system with name="SiteIcp" %}</a> &copy;2021 kandaoni.com. All Rights Reserved</p>
{# 自定义名称调用 #}
<p><a href="https://beian.miit.gov.cn/" rel="nofollow" target="_blank">{% system siteIcp with name="SiteIcp" %}{{siteIcp}}</a> &copy;2021 kandaoni.com. All Rights Reserved</p>
```

### 版权内容 `SiteCopyright`

标签用法：`{% system with name="SiteCopyright" %}`

```twig
{# 默认用法 #}
<div>{% system with name="SiteCopyright" %}</div>
{# 自定义名称调用 #}
<div>{% system siteCopyright with name="SiteCopyright" %}{{siteCopyright|safe}}</div>
```

### 网站首页地址 `BaseUrl`

标签用法：`{% system with name="BaseUrl" %}`

```twig
{# 默认用法 #}
<div>首页地址：{% system with name="BaseUrl" %}</div>
{# 自定义名称调用 #}
<div>首页地址：{% system baseUrl with name="BaseUrl" %}{{baseUrl|safe}}</div>
```

### 网站手机端地址 `MobileUrl`

标签用法：`{% system with name="MobileUrl" %}`

```twig
{# 默认用法 #}
<div>移动端地址：{% system with name="MobileUrl" %}</div>
{# 自定义名称调用 #}
<div>移动端地址：{% system mobileUrl with name="MobileUrl" %}{{mobileUrl|safe}}</div>
```

### 模板静态文件地址 `TemplateUrl`

标签用法：`{% system with name="TemplateUrl" %}`

```twig
{# 默认用法 #}
<link href="{% system with name="TemplateUrl" %}/css/style.css" rel="stylesheet">
{# 自定义名称调用 #}
<div>静态文件地址：{% system templateUrl with name="TemplateUrl" %}{{templateUrl|safe}}</div>
```

### 站点语言 `Language`

标签用法：`{% system with name="Language" %}`

```twig
{# 默认用法 #}
<html lang="{% system with name='Language' %}">
```

### 获取当前年份标签

标签用法：`{% now "2006" %}`

后面的 2006 是时间格式化字符串，格式为 Golang 支持的格式。

```twig
仅仅显示年：
{% now "2006" %}
显示年月日
{% now "2006-01-02" %}
显示年月日时分秒
{% now "2006-01-02 15:04:05" %}
```

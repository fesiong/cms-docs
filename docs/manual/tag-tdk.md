# 页面 TDK 标签

说明：用于获取页面的 title、keywords、description 信息

使用方法：`{% tdk 变量名称 with name="字段名称" %}`，变量名称不是必须的，设置了变量名称后，后续可以通过变量名称来调用，而不设置变量名称，则是直接输出结果。

### tdk 支持的参数

- 是否显示网站名称 `siteName`  
  `siteName` 默认值 `siteName=false`，只有在 `name="Title"` 的时候生效。

name 参数可用的字段名称有：

- 页面标题 `Title`
- 页面关键词 `Keywords`
- 页面描述 `Description`
- 页面的规范链接 `CanonicalUrl`

### 页面标题 `Title`

标签用法：`{% tdk with name="Title" %}` name="Title" 时变量支持：

- `siteName` 属性，可以设置是否附加网站名称到 Title 后面。 `siteName` 为一个 bool 类型，默认不显示。显示的时候使用： `{% tdk with name="Title" siteName=true %}`
- `sep` 属性，可以设置分隔符，默认为 `-`
- `showParent` 属性，可以设置是否显示父级分类的标题，默认为 `showParent=false`，只有在 `name="Title"` 的时候才生效。

```twig
{# 不显示网站名称后缀 #}
<title>{% tdk with name="Title" %}</title>
{# 显示网站名称后缀 #}
<title>{% tdk with name="Title" siteName=true %}</title>
{# 不显示网站名称后缀 #}
<title>{% tdk with name="Title" siteName=false %}</title>
{# 自定义名称调用 #}
<title>{% tdk seoTitle with name="Title" siteName=true %}{{seoTitle}}</title>
{# 自定义分隔符 #}
<title>{% tdk with name="Title" sep="_" %}</title>
{# 显示上级分类标题 #}
<title>{% tdk with name="Title" showParent=true %}</title>
```

### 页面关键词 `Keywords`

标签用法：`{% tdk with name="Keywords" %}`

```twig
{# 默认用法 #}
<meta name="keywords" content="{% tdk with name="Keywords" %}">
{# 自定义名称调用 #}
<meta name="keywords" content="{% tdk seoKeywords with name="Keywords" %}{{seoKeywords}}">
```

### 页面描述 `Description`

标签用法：`{% tdk with name="Description" %}`

```twig
{# 默认用法 #}
<meta name="description" content="{% tdk with name="Description" %}">
{# 自定义名称调用 #}
<meta name="description" content="{% tdk seoDescription with name="Description" %}{{seoDescription}}">
```

### 页面的规范链接 `CanonicalUrl`

标签用法：`{% tdk with name="CanonicalUrl" %}`

```twig
{# 默认用法 #}
<link rel="canonical" href="{% tdk with name="CanonicalUrl" %}" />
```

一般上，CanonicalUrl 需要先判断是否存在，如果存在，才设置

```twig
{%- tdk canonical with name="CanonicalUrl" %}
{%- if canonical %}
<link rel="canonical" href="{{canonical}}" />
{%- endif %}
```

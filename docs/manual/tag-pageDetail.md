# 单页详情标签

说明：用于获取单页详情数据

使用方法：`{% pageDetail 变量名称 with name="字段名称" id="1" %}` 变量名称不是必须的，设置了变量名称后，后续可以通过变量名称来调用，而不设置变量名称，则是直接输出结果。

### pageDetail 支持的参数有：

- 单页 ID `id`。
  `id` 不是必须的，默认会获取当前单页。如果需要指定单页，可以通过设置 id 来达到目的。
- 单页 URL 别名 `token`
  `token` 不是必须的，默认会获取当前单页。如果需要指定单页，可以通过设置 id 或 token 来达到目的。
- 站点 ID `siteId`
  `siteId` 一般不需要填写，如果你使用后台的多站点管理创建了多个站点，并且想调用其他站点的数据，则可以通过指定 `siteId` 来实现调用指定站点的数据。

### name 参数可用的字段有：

- 单页 ID `Id`
- 单页标题 `Title`
- 单页链接 `Link`
- 单页描述 `Description`
- 单页内容 `Content`
- 单页缩略图大图 `Logo`
- 单页缩略图 `Thumb`
- 单页幻灯片组图 `Images`

### 单页 ID `Id`

标签用法：`{% pageDetail with name="Id" %}`

```twig
{# 默认用法，自动获取当前页面单页 #}
<div>单页ID：{% pageDetail with name="Id" %}</div>
{# 获取指定单页id的单页字段 #}
<div>单页ID：{% pageDetail with name="Id" id="1" %}</div>
{# 自定义字段名称 #}
<div>单页ID：{% pageDetail pageId with name="Id" %}{{pageId}}</div>
<div>单页ID：{% pageDetail pageId with name="Id" id="1" %}{{pageId}}</div>
```

### 单页标题 `Title`

标签用法：`{% pageDetail with name="Title" %}`

```twig
{# 默认用法，自动获取当前页面单页 #}
<div>单页标题：{% pageDetail with name="Title" %}</div>
{# 获取指定单页id的单页字段 #}
<div>单页标题：{% pageDetail with name="Title" id="1" %}</div>
{# 自定义字段名称 #}
<div>单页标题：{% pageDetail pageTitle with name="Title" %}{{pageTitle}}</div>
<div>单页标题：{% pageDetail pageTitle with name="Title" id="1" %}{{pageTitle}}</div>
```

### 单页链接 `Link`

标签用法：`{% pageDetail with name="Link" %}`

```twig
{# 默认用法，自动获取当前页面单页 #}
<div>单页链接：{% pageDetail with name="Link" %}</div>
{# 获取指定单页id的单页字段 #}
<div>单页链接：{% pageDetail with name="Link" id="1" %}</div>
{# 自定义字段名称 #}
<div>单页链接：{% pageDetail pageLink with name="Link" %}{{pageLink}}</div>
<div>单页链接：{% pageDetail pageLink with name="Link" id="1" %}{{pageLink}}</div>
```

### 单页描述 `Description`

标签用法：`{% pageDetail with name="Description" %}`

```twig
{# 默认用法，自动获取当前页面单页 #}
<div>单页描述：{% pageDetail with name="Description" %}</div>
{# 获取指定单页id的单页字段 #}
<div>单页描述：{% pageDetail with name="Description" id="1" %}</div>
{# 自定义字段名称 #}
<div>单页描述：{% pageDetail pageDescription with name="Description" %}{{pageDescription}}</div>
<div>单页描述：{% pageDetail pageDescription with name="Description" id="1" %}{{pageDescription}}</div>
```

### 单页内容 `Content`

标签用法：`{% pageDetail with name="Content" %}`

Content 字段在开启 Markdown 编辑器后，会自动对内容进行 Markdown 转 html 操作，关闭 Markdown 编辑器编辑器后，Content 内容不会自动对内容进行 Markdown 转 html 操作。但你可以手动指定是否进行转换，需要添加`render`参数。接受`false|true`两个值。`render=false`不进行 Markdown 转 html 操作，`render=true`进行转换。

```twig
{# 默认用法，自动获取当前页面单页 #}
<div>单页内容：{% pageDetail with name="Content" %}</div>
{# 获取指定单页id的单页字段 #}
<div>单页内容：{% pageDetail with name="Content" id="1" %}</div>
{# 自定义字段名称 #}
<div>单页内容：{% pageDetail pageContent with name="Content" %}{{pageContent|safe}}</div>
<div>单页内容：{% pageDetail pageContent with name="Content" id="1" %}{{pageContent|safe}}</div>
```

### 单页缩略图大图 `Logo`

标签用法：`{% pageDetail with name="Logo" %}`

```twig
{# 默认用法，自动获取当前页面分类 #}
<div>缩略图大图：<img src="{% pageDetail with name="Logo" %}" alt="{% pageDetail with name="Title" %}" /></div>
{# 获取指定分类id的分类字段 #}
<div>缩略图大图：<img src="{% pageDetail with name="Logo" id="1" %}" alt="{% pageDetail with name="Title" id="1" %}" /></div>
{# 自定义字段名称 #}
<div>缩略图大图：{% pageDetail pageLogo with name="Logo" %}<img src="{{pageLogo}}" alt="{% pageDetail with name="Title" %}" /></div>
<div>缩略图大图：{% pageDetail pageLogo with name="Logo" id="1" %}<img src="{{pageLogo}}" alt="{% pageDetail with name="Title" %}" /></div>
```

### 单页缩略图 `Thumb`

标签用法：`{% pageDetail with name="Thumb" %}`

```twig
{# 默认用法，自动获取当前页面分类 #}
<div>缩略图大图：<img src="{% pageDetail with name="Thumb" %}" alt="{% pageDetail with name="Title" %}" /></div>
{# 获取指定分类id的分类字段 #}
<div>缩略图大图：<img src="{% pageDetail with name="Thumb" id="1" %}" alt="{% pageDetail with name="Title" id="1" %}" /></div>
{# 自定义字段名称 #}
<div>缩略图大图：{% pageDetail pageThumb with name="Thumb" %}<img src="{{pageThumb}}" alt="{% pageDetail with name="Title" %}" /></div>
<div>缩略图大图：{% pageDetail pageThumb with name="Thumb" id="1" %}<img src="{{pageThumb}}" alt="{% pageDetail with name="Title" %}" /></div>
```

### 单页幻灯片组图 `Images`

标签用法：`{% pageDetail pageImages with name="Images" %}{% for item in pageImages %}<img src="{{item}}" alt="{% pageDetail with name="Title" %}" />{% endfor %}`

```twig
{% pageDetail pageImages with name="Images" %}
<ul>
{% for item in pageImages %}
  <li>
    <img src="{{item}}" alt="{% pageDetail with name="Title" %}" />
  </li>
{% endfor %}
</ul>
```

# 城市分站详情标签

说明：用于获取城市分站的详情信息

使用方法：`{% placeDetail 变量名称 with name="字段名称" id="1" %}` 变量名称不是必须的，设置了变量名称后，后续可以通过变量名称来调用，而不设置变量名称，则是直接输出结果。

### placeDetail 支持的参数有：

- 城市分站 ID `id`  
  `id` 不是必须的，默认会获取当前分站。如果需要指定分站，可以通过设置 id 来达到目的。
- 城市分站 URL 别名 `token`  
  `token` 不是必须的，默认会获取当前分站。如果需要指定分站，可以通过设置 id 或 token 来达到目的。
- 站点 ID `siteId`  
  `siteId` 一般不需要填写，如果你使用后台的多站点管理创建了多个站点，并且想调用其他站点的数据，则可以通过指定 `siteId` 来实现调用指定站点的数据。
- 内容渲染 `render`  
  `render` 仅对 Content 字段有效，接受 `false|true` 两个值。`render=true` 进行 Markdown 转 HTML 操作，默认根据编辑器设置自动判断。

### name 参数可用的字段有：

- 分站 ID `Id`
- 分站标题 `Title`
- 分站 SEO 标题 `SeoTitle`
- 分站关键词 `Keywords`
- 分站描述 `Description`
- 分站内容 `Content`
- 分站链接 `Link`
- 分站缩略图大图 `Logo`
- 分站缩略图 `Thumb`
- 分站 Banner 组图 `Images`
- 上级分站 ID `ParentId`
- 顶级分站 ID `TopId`
- 创建时间 `CreatedTime`
- 更新时间 `UpdatedTime`
- 纬度 `Latitude`
- 经度 `Longitude`
- 时区 `Timezone`
- 自定义字段 `Extra`

### 分站 ID `Id`

标签用法：`{% placeDetail with name="Id" %}`

```twig
{# 默认用法，自动获取当前页面分站 #}
<div>分站ID：{% placeDetail with name="Id" %}</div>
{# 获取指定分站id的分站字段 #}
<div>分站ID：{% placeDetail with name="Id" id="1" %}</div>
{# 自定义字段名称 #}
<div>分站ID：{% placeDetail placeId with name="Id" %}{{placeId}}</div>
<div>分站ID：{% placeDetail placeId with name="Id" id="1" %}{{placeId}}</div>
```

### 分站标题 `Title`

标签用法：`{% placeDetail with name="Title" %}`

```twig
{# 默认用法，自动获取当前页面分站 #}
<div>分站标题：{% placeDetail with name="Title" %}</div>
{# 获取指定分站id的分站字段 #}
<div>分站标题：{% placeDetail with name="Title" id="1" %}</div>
{# 自定义字段名称 #}
<div>分站标题：{% placeDetail placeTitle with name="Title" %}{{placeTitle}}</div>
<div>分站标题：{% placeDetail placeTitle with name="Title" id="1" %}{{placeTitle}}</div>
```

### 分站链接 `Link`

标签用法：`{% placeDetail with name="Link" %}`

```twig
{# 默认用法，自动获取当前页面分站 #}
<div>分站链接：{% placeDetail with name="Link" %}</div>
{# 获取指定分站id的分站字段 #}
<div>分站链接：{% placeDetail with name="Link" id="1" %}</div>
{# 自定义字段名称 #}
<div>分站链接：{% placeDetail placeLink with name="Link" %}{{placeLink}}</div>
<div>分站链接：{% placeDetail placeLink with name="Link" id="1" %}{{placeLink}}</div>
```

### 分站描述 `Description`

标签用法：`{% placeDetail with name="Description" %}`

```twig
{# 默认用法，自动获取当前页面分站 #}
<div>分站描述：{% placeDetail with name="Description" %}</div>
{# 获取指定分站id的分站字段 #}
<div>分站描述：{% placeDetail with name="Description" id="1" %}</div>
{# 自定义字段名称 #}
<div>分站描述：{% placeDetail placeDescription with name="Description" %}{{placeDescription}}</div>
<div>分站描述：{% placeDetail placeDescription with name="Description" id="1" %}{{placeDescription}}</div>
```

### 分站内容 `Content`

标签用法：`{% placeDetail with name="Content" %}`

Content 字段在开启 Markdown 编辑器后，会自动对内容进行 Markdown 转 HTML 操作。关闭 Markdown 编辑器后，Content 内容不会自动转换。但你可以手动指定是否转换，添加 `render` 参数。`render=false` 不进行 Markdown 转 HTML 操作，`render=true` 进行转换。

```twig
{# 默认用法，自动获取当前页面分站 #}
<div>分站内容：{% placeDetail with name="Content" %}</div>
{# 获取指定分站id的分站字段，并强制渲染 #}
<div>分站内容：{% placeDetail with name="Content" id="1" render="true" %}</div>
{# 自定义字段名称 #}
<div>分站内容：{% placeDetail placeContent with name="Content" %}{{placeContent|safe}}</div>
<div>分站内容：{% placeDetail placeContent with name="Content" id="1" render="true" %}{{placeContent|safe}}</div>
```

### 上级分站 ID `ParentId`

标签用法：`{% placeDetail with name="ParentId" %}`

```twig
{# 默认用法，自动获取当前页面分站 #}
<div>上级分站ID：{% placeDetail with name="ParentId" %}</div>
{# 获取指定分站id的分站字段 #}
<div>上级分站ID：{% placeDetail with name="ParentId" id="1" %}</div>
{# 自定义字段名称 #}
<div>上级分站ID：{% placeDetail placeParentId with name="ParentId" %}{{placeParentId}}</div>
<div>上级分站ID：{% placeDetail placeParentId with name="ParentId" id="1" %}{{placeParentId}}</div>
```

### 顶级分站 ID `TopId`

标签用法：`{% placeDetail with name="TopId" %}`

TopId 用于获取当前分站的顶级分站 ID，如果当前分站已是顶级，则返回自身 ID。

```twig
{# 默认用法，自动获取当前页面分站 #}
<div>顶级分站ID：{% placeDetail with name="TopId" %}</div>
{# 自定义字段名称 #}
<div>顶级分站ID：{% placeDetail placeTopId with name="TopId" %}{{placeTopId}}</div>
```

### 分站缩略图大图 `Logo`

标签用法：`{% placeDetail with name="Logo" %}`

```twig
{# 默认用法，自动获取当前页面分站 #}
<div>缩略图大图：<img style="width: 200px" src="{% placeDetail with name="Logo" %}" alt="{% placeDetail with name="Title" %}" /></div>
{# 获取指定分站id的分站字段 #}
<div>缩略图大图：<img style="width: 200px" src="{% placeDetail with name="Logo" id="1" %}" alt="{% placeDetail with name="Title" id="1" %}" /></div>
{# 自定义字段名称 #}
<div>缩略图大图：{% placeDetail placeLogo with name="Logo" %}<img style="width: 200px" src="{{placeLogo}}" alt="{% placeDetail with name="Title" %}" /></div>
```

### 分站缩略图 `Thumb`

标签用法：`{% placeDetail with name="Thumb" %}`

```twig
{# 默认用法，自动获取当前页面分站 #}
<div>缩略图：<img style="width: 200px" src="{% placeDetail with name="Thumb" %}" alt="{% placeDetail with name="Title" %}" /></div>
{# 获取指定分站id的分站字段 #}
<div>缩略图：<img style="width: 200px" src="{% placeDetail with name="Thumb" id="1" %}" alt="{% placeDetail with name="Title" id="1" %}" /></div>
{# 自定义字段名称 #}
<div>缩略图：{% placeDetail placeThumb with name="Thumb" %}<img style="width: 200px" src="{{placeThumb}}" alt="{% placeDetail with name="Title" %}" /></div>
```

### 分站 Banner 组图 `Images`

标签用法：`{% placeDetail placeImages with name="Images" %}{% for item in placeImages %}<img src="{{item}}" alt="{% placeDetail with name="Title" %}" />{% endfor %}`

```twig
{% placeDetail placeImages with name="Images" %}
<ul>
{% for item in placeImages %}
  <li>
    <img src="{{item}}" alt="{% placeDetail with name="Title" %}" />
  </li>
{% endfor %}
</ul>
```

上面的代码将会展示多张幻灯片。如果你只需要第一张图，并判断图片是否存在，可以使用以下的方法：

```twig
{% placeDetail bannerImages with name="Images" %}
{% if bannerImages %}
{% set pageBanner = bannerImages[0] %}
{% endif %}
<img src="{{pageBanner}}" />
```

### 分站经纬度 `Latitude` / `Longitude`

标签用法：`{% placeDetail with name="Latitude" %}`、`{% placeDetail with name="Longitude" %}`

```twig
{# 默认用法，自动获取当前页面分站的经纬度 #}
<div>纬度：{% placeDetail with name="Latitude" %}，经度：{% placeDetail with name="Longitude" %}</div>
{# 自定义字段名称 #}
<div>纬度：{% placeDetail placeLat with name="Latitude" %}{{placeLat}}</div>
<div>经度：{% placeDetail placeLng with name="Longitude" %}{{placeLng}}</div>
```

### 分站时区 `Timezone`

标签用法：`{% placeDetail with name="Timezone" %}`

```twig
{# 默认用法，自动获取当前页面分站 #}
<div>时区：{% placeDetail with name="Timezone" %}</div>
{# 自定义字段名称 #}
<div>时区：{% placeDetail placeTimezone with name="Timezone" %}{{placeTimezone}}</div>
```

### 分站自定义字段 `Extra`

如果你想要将自定义字段全部循环出来，可以这样用：

```twig
{% placeDetail extras with name="Extra" %}
{% for field in extras %}
  <div>{{field.Name}}：{{field.Value}}</div>
{% endfor %}
```

默认它会循环出所有自定义字段，如果你不想某个自定义字段出现，比如，不希望 `author` 字段显示在页面上，可以这样用：

```twig
{% placeDetail extras with name="Extra" %}
{% for field in extras %}
{% if field.Name != 'author' %}
  <div>{{field.Name}}：{{field.Value}}</div>
{% endif %}
{% endfor %}
```

如果你想显示某个自定义字段的内容，如自定义字段为 `phone`，可以直接用 name 指定：

```twig
{% placeDetail with name="phone" %}
```

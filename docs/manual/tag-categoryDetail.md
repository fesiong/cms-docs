# 分类详情标签

说明：用于获取文档的分类详情

使用方法：`{% categoryDetail 变量名称 with name="字段名称" id="1" %}` 变量名称不是必须的，设置了变量名称后，后续可以通过变量名称来调用，而不设置变量名称，则是直接输出结果。

### categoryDetail 支持的参数有：

- 分类 ID `id`  
  `id` 不是必须的，默认会获取当前分类。如果需要指定分类，可以通过设置 id 来达到目的。
- 分类 URL 别名 `token`  
  `token` 不是必须的，默认会获取当前分类。如果需要指定分类，可以通过设置 id 或 token 来达到目的。
- 站点 ID `siteId`  
  `siteId` 一般不需要填写，如果你使用后台的多站点管理创建了多个站点，并且想调用其他站点的数据，则可以通过指定 `siteId` 来实现调用指定站点的数据。

### name 参数可用的字段有：

- 分类 ID `Id`
- 分类标题 `Title`
- 分类链接 `Link`
- 分类描述 `Description`
- 分类内容 `Content`
- 上级分类 ID `ParentId`
- 分类缩略图大图 `Logo`
- 分类缩略图 `Thumb`
- 分类 Banner 组图 `Images`
- 分类的文档数量 `ArchiveCount`
- 文档模型设置的分类其他字段参数

### 分类 ID `Id`

标签用法：`{% categoryDetail with name="Id" %}`

```twig
{# 默认用法，自动获取当前页面分类 #}
<div>分类ID：{% categoryDetail with name="Id" %}</div>
{# 获取指定分类id的分类字段 #}
<div>分类ID：{% categoryDetail with name="Id" id="1" %}</div>
{# 自定义字段名称 #}
<div>分类ID：{% categoryDetail categoryId with name="Id" %}{{categoryId}}</div>
<div>分类ID：{% categoryDetail categoryId with name="Id" id="1" %}{{categoryId}}</div>
```

### 分类标题 `Title`

标签用法：`{% categoryDetail with name="Title" %}`

```twig
{# 默认用法，自动获取当前页面分类 #}
<div>分类标题：{% categoryDetail with name="Title" %}</div>
{# 获取指定分类id的分类字段 #}
<div>分类标题：{% categoryDetail with name="Title" id="1" %}</div>
{# 自定义字段名称 #}
<div>分类标题：{% categoryDetail categoryTitle with name="Title" %}{{categoryTitle}}</div>
<div>分类标题：{% categoryDetail categoryTitle with name="Title" id="1" %}{{categoryTitle}}</div>
```

### 分类链接 `Link`

标签用法：`{% categoryDetail with name="Link" %}`

```twig
{# 默认用法，自动获取当前页面分类 #}
<div>分类链接：{% categoryDetail with name="Link" %}</div>
{# 获取指定分类id的分类字段 #}
<div>分类链接：{% categoryDetail with name="Link" id="1" %}</div>
{# 自定义字段名称 #}
<div>分类链接：{% categoryDetail categoryLink with name="Link" %}{{categoryLink}}</div>
<div>分类链接：{% categoryDetail categoryLink with name="Link" id="1" %}{{categoryLink}}</div>
```

### 分类描述 `Description`

标签用法：`{% categoryDetail with name="Description" %}`

```twig
{# 默认用法，自动获取当前页面分类 #}
<div>分类描述：{% categoryDetail with name="Description" %}</div>
{# 获取指定分类id的分类字段 #}
<div>分类描述：{% categoryDetail with name="Description" id="1" %}</div>
{# 自定义字段名称 #}
<div>分类描述：{% categoryDetail categoryDescription with name="Description" %}{{categoryDescription}}</div>
<div>分类描述：{% categoryDetail categoryDescription with name="Description" id="1" %}{{categoryDescription}}</div>
```

### 分类内容 `Content`

标签用法：`{% categoryDetail with name="Content" %}`

Content 字段在开启 Markdown 编辑器后，会自动对内容进行 Markdown 转 html 操作，关闭 Markdown 编辑器编辑器后，Content 内容不会自动对内容进行 Markdown 转 html 操作。但你可以手动指定是否进行转换，需要添加`render`参数。接受`false|true`两个值。`render=false`不进行 Markdown 转 html 操作，`render=true`进行转换。

```twig
{# 默认用法，自动获取当前页面分类 #}
<div>分类内容：{% categoryDetail with name="Content" %}</div>
{# 获取指定分类id的分类字段 #}
<div>分类内容：{% categoryDetail with name="Content" id="1" %}</div>
{# 自定义字段名称 #}
<div>分类内容：{% categoryDetail categoryContent with name="Content" %}{{categoryContent|safe}}</div>
<div>分类内容：{% categoryDetail categoryContent with name="Content" id="1" %}{{categoryContent|safe}}</div>
```

### 上级分类 ID `ParentId`

标签用法：`{% categoryDetail with name="ParentId" %}`

```twig
{# 默认用法，自动获取当前页面分类 #}
<div>上级分类ID：{% categoryDetail with name="ParentId" %}</div>
{# 获取指定分类id的分类字段 #}
<div>上级分类ID：{% categoryDetail with name="ParentId" id="1" %}</div>
{# 自定义字段名称 #}
<div>上级分类ID：{% categoryDetail categoryParentId with name="ParentId" %}{{categoryParentId}}</div>
<div>上级分类ID：{% categoryDetail categoryParentId with name="ParentId" id="1" %}{{categoryParentId}}</div>
```

### 分类的文档数量 `ArchiveCount`

标签用法：`{% categoryDetail with name="ArchiveCount" %}`

```twig
{# 默认用法，自动获取当前页面分类 #}
<div>分类文档数量：{% categoryDetail with name="ArchiveCount" %}</div>
{# 获取指定分类id的分类字段 #}
<div>分类文档数量：{% categoryDetail with name="ArchiveCount" id="1" %}</div>
{# 自定义字段名称 #}
<div>分类文档数量：{% categoryDetail archiveCount with name="ArchiveCount" %}{{archiveCount}}</div>
<div>分类文档数量：{% categoryDetail archiveCount with name="ArchiveCount" id="1" %}{{archiveCount}}</div>
```

### 文档模型设置的分类其他字段参数

如果你想显示某个自定义字段的内容，如你自定义字段为 `author`，那么在模板中就可以这样调用：

```twig
{% categoryDetail with name="author" %}
```

自定义字段参数的使用，例如，你自定义了一个组图的字段，为 `catimages`，并且想在前端展示它们，可以这么写：
```twig
{% categoryDetail catimages with name="catimages" %}
<ul class="category-images">
  {% for img in catimages %}
  <li><img src="{{img}}" /></li>
  {% endfor %}
</ul>
```

如果你想要将自定义字段全部循环出来，可以这么用：

```twig
{% categoryDetail extras with name="Extra" %}
{% for field in extras %}
  <div>{{field.Name}}：{{field.Value}}</div>
{% endfor %}
```

默认它是会循环出所有自定义字段，如果你不想某个自定义字段出现，比如，不希望`author`、`price`字段显示在页面上，可以这样用：

```twig
{% categoryDetail extras with name="Extra" %}
{% for field in extras %}
{% if field.Name != 'author' and field.Name != 'price' %}
  <div>{{field.Name}}：{{field.Value}}</div>
{% endif %}
{% endfor %}
```

### 分类缩略图大图 `Logo`

标签用法：`{% categoryDetail with name="Logo" %}`

```twig
{# 默认用法，自动获取当前页面分类 #}
<div>缩略图大图：<img style="width: 200px" src="{% categoryDetail with name="Logo" %}" alt="{% categoryDetail with name="Title" %}" /></div>
{# 获取指定分类id的分类字段 #}
<div>缩略图大图：<img style="width: 200px" src="{% categoryDetail with name="Logo" id="1" %}" alt="{% categoryDetail with name="Title" id="1" %}" /></div>
{# 自定义字段名称 #}
<div>缩略图大图：{% categoryDetail categoryLogo with name="Logo" %}<img style="width: 200px" src="{{categoryLogo}}" alt="{% categoryDetail with name="Title" %}" /></div>
<div>缩略图大图：{% categoryDetail categoryLogo with name="Logo" id="1" %}<img style="width: 200px" src="{{categoryLogo}}" alt="{% categoryDetail with name="Title" %}" /></div>
```

### 分类缩略图 `Thumb`

标签用法：`{% categoryDetail with name="Thumb" %}`

```twig
{# 默认用法，自动获取当前页面分类 #}
<div>缩略图大图：<img style="width: 200px" src="{% categoryDetail with name="Thumb" %}" alt="{% categoryDetail with name="Title" %}" /></div>
{# 获取指定分类id的分类字段 #}
<div>缩略图大图：<img style="width: 200px" src="{% categoryDetail with name="Thumb" id="1" %}" alt="{% categoryDetail with name="Title" id="1" %}" /></div>
{# 自定义字段名称 #}
<div>缩略图大图：{% categoryDetail categoryThumb with name="Thumb" %}<img style="width: 200px" src="{{categoryThumb}}" alt="{% categoryDetail with name="Title" %}" /></div>
<div>缩略图大图：{% categoryDetail categoryThumb with name="Thumb" id="1" %}<img style="width: 200px" src="{{categoryThumb}}" alt="{% categoryDetail with name="Title" %}" /></div>
```

### 分类 Banner 组图 `Images`

标签用法：`{% categoryDetail categoryImages with name="Images" %}{% for item in categoryImages %}<img src="{{item}}" alt="{% categoryDetail with name="Title" %}" />{% endfor %}`

```twig
{% categoryDetail categoryImages with name="Images" %}
<ul>
{% for item in categoryImages %}
  <li>
    <img src="{{item}}" alt="{% categoryDetail with name="Title" %}" />
  </li>
{% endfor %}
</ul>
```

上面的代码将会展示多张幻灯片。
如果你只需要第一张图，并判断图片是否存在，可以使用以下的方法：

```twig
{% categoryDetail bannerImages with name="Images" %}
{% if bannerImages %}
{% set pageBanner = bannerImages[0] %}
{% endif %}
<img src="{{pageBanner}}" />
```

如果想把它作为背景图，可以这样：

```twig
{% categoryDetail bannerImages with name="Images" %}
{% if bannerImages %}
{% set pageBanner = bannerImages[0] %}
{% endif %}
<div class="page-banner" style="background: url({{pageBanner}}) no-repeat;">
</div>
```

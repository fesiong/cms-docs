# Tag 详情标签

说明：用于获取文档的 Tag 详情数据

使用方法：`{% tagDetail 变量名称 with name="字段名称" id="1" %}` 变量名称不是必须的，设置了变量名称后，后续可以通过变量名称来调用，而不设置变量名称，则是直接输出结果。

### tagDetail 支持的参数有：

- TagID `id`  
  `id` 不是必须的，默认会获取当前 Tag 的 ID。如果需要指定 Tag，可以通过设置 id 来达到目的。
- Tag 标签 URL 别名 `token`  
  `token` 不是必须的，默认会获取当前 Tag 标签。如果需要指定 Tag 标签，可以通过设置 id 或 token 来达到目的。
- 站点 ID `siteId`  
  `siteId` 一般不需要填写，如果你使用后台的多站点管理创建了多个站点，并且想调用其他站点的数据，则可以通过指定 `siteId` 来实现调用指定站点的数据。

### name 参数可用的字段有：

- TagID `Id`
- Tag 标题 `Title`
- Tag 链接 `Link`
- Tag 描述 `Description`
- Tag 索引字母 `FirstLetter`
- Tag 的分类 ID `CategoryId`
- Tag 的内容 `Content`
- Tag 的 Logo `Logo`

### TagID `Id`

标签用法：`{% tagDetail with name="Id" %}`

```twig
{# 默认用法，自动获取当前页面Tag #}
<div>TagID：{% tagDetail with name="Id" %}</div>
{# 获取指定Tagid的Tag字段 #}
<div>TagID：{% tagDetail with name="Id" id="1" %}</div>
{# 自定义字段名称 #}
<div>TagID：{% tagDetail tagId with name="Id" %}{{tagId}}</div>
<div>TagID：{% tagDetail tagId with name="Id" id="1" %}{{tagId}}</div>
```

### Tag 标题 `Title`

标签用法：`{% tagDetail with name="Title" %}`

```twig
{# 默认用法，自动获取当前页面Tag #}
<div>Tag标题：{% tagDetail with name="Title" %}</div>
{# 获取指定Tagid的Tag字段 #}
<div>Tag标题：{% tagDetail with name="Title" id="1" %}</div>
{# 自定义字段名称 #}
<div>Tag标题：{% tagDetail tagTitle with name="Title" %}{{tagTitle}}</div>
<div>Tag标题：{% tagDetail tagTitle with name="Title" id="1" %}{{tagTitle}}</div>
```

### Tag 链接 `Link`

标签用法：`{% tagDetail with name="Link" %}`

```twig
{# 默认用法，自动获取当前页面Tag #}
<div>Tag链接：{% tagDetail with name="Link" %}</div>
{# 获取指定Tagid的Tag字段 #}
<div>Tag链接：{% tagDetail with name="Link" id="1" %}</div>
{# 自定义字段名称 #}
<div>Tag链接：{% tagDetail tagLink with name="Link" %}{{tagLink}}</div>
<div>Tag链接：{% tagDetail tagLink with name="Link" id="1" %}{{tagLink}}</div>
```

### Tag 描述 `Description`

标签用法：`{% tagDetail with name="Description" %}`

```twig
{# 默认用法，自动获取当前页面Tag #}
<div>Tag描述：{% tagDetail with name="Description" %}</div>
{# 获取指定Tagid的Tag字段 #}
<div>Tag描述：{% tagDetail with name="Description" id="1" %}</div>
{# 自定义字段名称 #}
<div>Tag描述：{% tagDetail tagDescription with name="Description" %}{{tagDescription}}</div>
<div>Tag描述：{% tagDetail tagDescription with name="Description" id="1" %}{{tagDescription}}</div>
```

### Tag 索引字母 `FirstLetter`

标签用法：`{% tagDetail with name="FirstLetter" %}`

```twig
{# 默认用法，自动获取当前页面Tag #}
<div>Tag索引字母：{% tagDetail with name="FirstLetter" %}</div>
{# 获取指定Tagid的Tag字段 #}
<div>Tag索引字母：{% tagDetail with name="FirstLetter" id="1" %}</div>
{# 自定义字段名称 #}
<div>Tag索引字母：{% tagDetail tagFirstLetter with name="FirstLetter" %}{{tagFirstLetter}}</div>
<div>Tag索引字母：{% tagDetail tagFirstLetter with name="FirstLetter" id="1" %}{{tagFirstLetter}}</div>
```

### Tag 缩略图大图 `Logo`

标签用法：`{% tagDetail with name="Logo" %}`

```twig
{# 默认用法，自动获取当前页面Tag #}
<div>缩略图大图：<img style="width: 200px" src="{% tagDetail with name="Logo" %}" alt="{% tagDetail with name="Title" %}" /></div>
{# 获取指定Tagid的Tag字段 #}
<div>缩略图大图：<img style="width: 200px" src="{% tagDetail with name="Logo" id="1" %}" alt="{% tagDetail with name="Title" id="1" %}" /></div>
{# 自定义字段名称 #}
<div>缩略图大图：{% tagDetail tagLogo with name="Logo" %}<img style="width: 200px" src="{{tagLogo}}" alt="{% tagDetail with name="Title" %}" /></div>
<div>缩略图大图：{% tagDetail tagLogo with name="Logo" id="1" %}<img style="width: 200px" src="{{tagLogo}}" alt="{% tagDetail with name="Title" %}" /></div>
```

### Tag 的内容 `Content`

标签用法：`{% tagDetail with name="Content" %}`

Content 字段在开启 Markdown 编辑器后，会自动对内容进行 Markdown 转 html 操作，关闭 Markdown 编辑器编辑器后，Content 内容不会自动对内容进行 Markdown 转 html 操作。但你可以手动指定是否进行转换，需要添加`render`参数。接受`false|true`两个值。`render=false`不进行 Markdown 转 html 操作，`render=true`进行转换。

```twig
{# 自定义字段名称 #}
<div>Tag的内容：{% tagDetail tagContent with name="Content" %}{{tagContent|safe}}</div>
<div>Tag的内容：{% tagDetail tagContent with name="Content" id="1" %}{{tagContent|safe}}</div>
```

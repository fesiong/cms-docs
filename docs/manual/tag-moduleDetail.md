# 文档模型详情标签

说明：用于获取文档模型详情数据

使用方法：`{% moduleDetail 变量名称 with name="字段名称" id="1" %}` 变量名称不是必须的，设置了变量名称后，后续可以通过变量名称来调用，而不设置变量名称，则是直接输出结果。

### moduleDetail 支持的参数有：

- 模型 ID `id`。
  `id` 不是必须的，默认会获取当前模型。如果需要指定模型，可以通过设置 id 或 token 来达到目的。
- 模型 URL 别名 `token`。
  `token` 不是必须的，默认会获取当前模型。如果需要指定模型，可以通过设置 id 或 token 来达到目的。
- 站点 ID `siteId`。
  `siteId` 一般不需要填写，如果你使用后台的多站点管理创建了多个站点，并且想调用其他站点的数据，则可以通过指定 `siteId` 来实现调用指定站点的数据。

### name 参数可用的字段有：

- 模型 ID `Id`
- 模型标题 `Title`
- 模型名称 `Name`
- 模型关键词 `Keywords`
- 模型简介 `Description`
- 模型链接 `Link`
- 模型表名 `TableName`

### 模型 ID `Id`

标签用法：`{% moduleDetail with name="Id" %}`

```twig
{# 默认用法，自动获取当前页面模型 #}
<div>模型ID：{% moduleDetail with name="Id" %}</div>
{# 获取指定模型id的模型字段 #}
<div>模型ID：{% moduleDetail with name="Id" id="1" %}</div>
{# 自定义字段名称 #}
<div>模型ID：{% moduleDetail pageId with name="Id" %}{{pageId}}</div>
<div>模型ID：{% moduleDetail pageId with name="Id" id="1" %}{{pageId}}</div>
```

### 模型标题 `Title`

标签用法：`{% moduleDetail with name="Title" %}`

```twig
{# 默认用法，自动获取当前页面模型 #}
<div>模型标题：{% moduleDetail with name="Title" %}</div>
{# 获取指定模型id的模型字段 #}
<div>模型标题：{% moduleDetail with name="Title" id="1" %}</div>
{# 自定义字段名称 #}
<div>模型标题：{% moduleDetail pageTitle with name="Title" %}{{pageTitle}}</div>
<div>模型标题：{% moduleDetail pageTitle with name="Title" id="1" %}{{pageTitle}}</div>
```

### 模型链接 `Link`

标签用法：`{% moduleDetail with name="Link" %}`

```twig
{# 默认用法，自动获取当前页面模型 #}
<div>模型链接：{% moduleDetail with name="Link" %}</div>
{# 获取指定模型id的模型字段 #}
<div>模型链接：{% moduleDetail with name="Link" id="1" %}</div>
{# 自定义字段名称 #}
<div>模型链接：{% moduleDetail pageLink with name="Link" %}{{pageLink}}</div>
<div>模型链接：{% moduleDetail pageLink with name="Link" id="1" %}{{pageLink}}</div>
```

### 模型简介 `Description`

标签用法：`{% moduleDetail with name="Description" %}`

```twig
{# 默认用法，自动获取当前页面模型 #}
<div>模型链接：{% moduleDetail with name="Description" %}</div>
{# 获取指定模型id的模型字段 #}
<div>模型链接：{% moduleDetail with name="Description" id="1" %}</div>
{# 自定义字段名称 #}
<div>模型链接：{% moduleDetail pageDescription with name="Description" %}{{pageDescription}}</div>
<div>模型链接：{% moduleDetail pageDescription with name="Description" id="1" %}{{pageDescription}}</div>
```

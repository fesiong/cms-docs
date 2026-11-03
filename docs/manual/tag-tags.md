# 其他辅助标签

一些常用会用到的内置标签。

### 模板的嵌套引用 `include`

往往制作模板的时候，我们会将一些公共部分，比如 header、footer、aside 等部分，抽离出来独立存放，不需要在每一个页面都重复编写，只需要在每一个页面引入它们即可。这个时候，我们可以使用 include 标签。

```twig
{% include "partial/header.html" %}
{% include "partial/footer.html" %}
```

include 可以将一个拆分出来的代码片段(fragment)嵌入到完整的文档中。使用形式是`{% include "模板文件" %}`。

如果需要引入的模板不存在的话，它会报错，如我我们不知道引入的模板是否存在，则需要增加`if_exists`判断。

```twig
{% include "partial/header.html" if_exists %}
```

这样如果 header.html 模板存在的话，则会引入，即使不存在，也不会报错，只是被忽略掉了。

默认情况下，include 引入的模板，它会继承当前模板的所有变量，如果想给 include 引入的模板增加另外的变量，可以使用`with`来增加。如：

```twig
{% include "partial/header.html" with title="这是声明给header使用的title" %}
```

这样就给 include 引入的模板定义了 title 变量，当前模板的其他变量它同样也可以继续使用了。

如果需要声明多个变量给 include 引入的模板使用，可以连续使用`key=value`的形式增加，它们之间使用空格隔开，如：

```twig
{% include "partial/header.html" with title="这是声明给header使用的title" keywords="这是声明给header使用的keywords" %}
```

如果只想让 include 引入的模板使用指定的几个变量，而不是当前模板的所有变量，可以使用 only 来做限制：

```twig
{% include "partial/header.html" with title="这是声明给header使用的title" keywords="这是声明给header使用的keywords" only %}
```

然后在 header.html 中使用：

```twig
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{title}}</title>
    <meta name="keywords" content="{{keywords}}">
</head>
```

### 模板代码片段宏函数`macro`

`iris.Django`模板引擎可以很简便的定义一些宏函数代码片段。宏代码片段相当于一个函数，它只能调用从参数传入的变量。类似于使用 include。不过 macro 有限定的作用域。如文章我们给文章列表的文章 item 使用`macro`：

```twig
定义一个宏函数
{% macro archive_detail(archive) %}
<li class="item">
    <a href="/archive/{{archive.Id}}" class="link">
        <h5 class="title">{{archive.Title}}</h5>
    </a>
</li>
{% endmacro %}
使用定义的宏函数
{% for item in archives %}
    {{ archive_detail(item) }}
{% endfor %}
```

同时宏函数还可以保存到独立的文件中，然后通过 import 来嵌套进来。当一个文件中包含多个宏函数，可以使用`,`将隔开连续引入多个宏函数。还可以使用 as 来设置别名：

保存宏函数到 archive.helper

```twig
{% macro archive_detail(archive) %}
<li class="item">
    <a href="/archive/{{archive.Id}}" class="link">
        <h5 class="title">{{archive.Title}}</h5>
    </a>
</li>
{% endmacro %}
{% macro archive_detail2(archive) %}
<li class="item">
    <a href="/archive/{{archive.Id}}" class="link">
        <h5 class="title">{{archive.Title}}</h5>
    </a>
</li>
{% endmacro %}
```

在 index.html 中引入：

```twig
用import引入：
{% import "archive.helper" archive_detail, archive_detail2 as archive_detail_new, archive_detail as new_item %}
调用：
{% for item in archives %}
    {{ archive_detail(item) }}
    {{ archive_detail_new(item) }}
    {{ new_item(item) }}
{% endfor %}
```

### 模板的继承 `extends`

模板的继承有点像 ppt 中的母版一样，我们定义好一个骨架，将一个页面都写好，大部分不用变动，需要变动的部分使用 block 标签包裹起来：

```twig
{% block title %}
    <title>base</title>  <!-- 如果扩写了就是扩写的，不扩写就还是用base -->
{% endblock %}
```

这样定义的好处是，可以在继承它的模板中，重写这个 block，不重写就按母版来显示。
比如我们定义了一个 base.html

```twig
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {% block title %}
        <title>base</title>  <!-- 如果扩写了就是扩写的，不扩写就还是用base -->
    {% endblock %}
    <!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css"
          integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    <style>
        * {
            margin: 0;
            padding: 0;
        }

        .header {
            width: 100%;
            height: 50px;
            background-color: #369;
        }
    </style>
</head>
<body>

<div class="header"></div>

<div class="container">
    <div class="row">
        <div class="col-md-3">
            {% include 'aside.html' %}
        </div>
        <div class="col-md-9">
            {% block content %}
                <h4>content</h4>
            {% endblock %}
        </div>
    </div>
</div>
</body>
</html>
```

然后在 index.html 中继承这个 base.html

```twig
{% extends 'base.html' %}

{% block title %}
    <title>index</title>
{% endblock %}


{% block content %}
    <div class="col-md-9">
        <h3>index</h3>
        <p>index content</p>
    </div>

{% endblock %}
```

这样就是使用 base.html 作为母版，并在 index.html 中重写了 title、content 两个部分。

注意：如果你在模版中使用 {% extends %} 标签，它必须是模版中的第一个标签。其他的任何情况下，模版继承都将无法工作。

在使用继承的情况下，尽可能将可能会变动的数据，都包裹在 block 中，因为 block 即使在后续的页面不重写，也不影响模板的解析，而需要重写的时候就更方便。

同样地，如果后续写到某一块，发现多个页面都需要使用到，那么这时候，就把添加到 base.html 中去，让它成为母版的一部分。

### 变量的输出

Django 模板中遍历复杂数据结构的关键是句点字符`.`，变量输出边界定义是双大括号。有一个对象是 people，它有 Name、Gender、Level 属性，在模板中输出就是：

```twig
<ul>
  <li>网站：{{siteName}}</li>
  <li>名字：{{people.Name}}</li>
  <li>性别：{{people.Gender}}</li>
  <li>等级：{{people.Level}}</li>
</ul>
```

### 在模板中使用 struct 结构体内置方法

比如在 archive 列表中，archive 的结构体中，定义了内置函数`func (archive *Archive) GetThumb()`，那么在模板中，是可以直接调用的。如：

```twig
{% for item in archives %}
<li class="item">
    <a href="/archive/{{item.Id}}" class="link">
        <img src="{{item.GetThumb()}}" alt="{{item.Title}}" />
        <h5 class="title">{{item.Title}}</h5>
    </a>
</li>
{% endfor %}
```

模板可以直接使用`{{item.GetThumb()}}`来调用内置的`archive.GetThumb()`方法。

### 在模板中输出当前时间

`now`标签提供在模板中输出当前时间。now 格式化时间的参数遵循 golang 的时间格式化规则。如果增加 fake 参数，则会输出一个特定的加时间代替当前时间。如：

```twig
{% now "Mon Jan 2 15:04:05 -0700 MST 2006" fake %}
{% now "2006-01-02 15:04" %}
```

### `lorem` 随机生成拉丁文样本数据

显示随机的“ lorem ipsum”拉丁文本。 这对于在模板中提供样本数据很有用。也就是占位内容。在开发模板没有真实数据的时候，使用这个标签可以快速填充足够多的随机数据。如：

```twig
-----
{% lorem %}
-----
{% lorem 10 %}
-----
{% lorem 3 p %}
-----
{% lorem 100 w %}
-----
```

### 模板的注释

`iris.Django`的注释我们使用大括号+#来实现注释：`{# 注释内容 #}`

单行注释使用 `{# 这只能注释单行 #}`，多行注释使用 `{% comment %}这里注释很多行{% endcomment %}`。

示例：

空单行注释

```twig
{# #}
```

单行注释

```twig
{# testing single line comment #}
```

用有效标签填充单行注释

```twig
{# testing single line comment {% if thing %}{% endif %} #}
```

用无效标签填充单行注释

```twig
{# testing single line comment {% if thing %} #}
```

用无效语法填充单行注释

```twig
{# testing single line comment {% if thing('') %}wow{% endif %} #}
```

空块注释

```twig
{% comment %}{% endcomment %}
```

填充文本单行块注释

```twig
{% comment %}filled block comment {% endcomment %}
```

空多行块注释

```twig
{% comment %}


{% endcomment %}
```

阻止带有其他标签的注释

```twig
{% comment %}
  {{ thing_goes_here }}
  {% if stuff %}do stuff{% endif %}
{% endcomment %}
```

阻止其中带有无效标签的注释

```twig
{% comment %}
  {% if thing %}
{% endcomment %}
```

使用无效语法阻止注释

```twig
{% comment %}
  {% thing('') %}
{% endcomment %}
```

注释之间的常规标签，以确保其在词法分析器中不会中断

```twig
{% if hello %}
{% endif %}
after if
{% comment %}All done{% endcomment %}
```

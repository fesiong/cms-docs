# 定义变量赋值标签

`iris.Django`模板引擎的模板解析器提供了可以在模板中声明变量并使用的方法`with`。通过`with`我们可以临时声明单个或多个变量，提供后续使用。多数情况下，我们会将它配合 include 标签使用。

### 示例代码

```twig
{% with title="这是声明给header使用的title" keywords="这是声明给header使用的keywords" %} %}标题：{{title}}，关键词：{{keywords}}。{% endwith %}
{% include "partial/header.html" with title="这是声明给header使用的title" keywords="这是声明给header使用的keywords" %}
```

`with`定义的变量需要使用`endwith`来包裹。

另外`iris.Django`还提供`set`的方式来声明变量，这个变量可以在当前模板使用。如：

```twig
{% set new_var = "hello" %}{{ new_var }}
{% block content %}{% set new_var = "world" %}{{ new_var }}{% endblock %}
{{ new_var }}{% for item in simple.misc_list %}
{% set new_var = item %}{{ new_var }}{% endfor %}
{{ new_var }}
{% set car=someUndefinedVar %}{{ car.Drive }}No Panic
```

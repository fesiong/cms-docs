# 过滤器：对字符串或 html 代码进行截取并添加...

## AICMS 模板中如何对字符串或 html 代码进行截取并添加...？

`truncatechars` 过滤器可以对字符串进行截取并添加...，该方法会截断单词，指定长度包括...。

`truncatechars_html` 过滤器可以对 html 代码进行截取并添加...，该方法会截断单词，指定长度包括...。

`truncatewords` 过滤器可以对字符串按单词进行截取并添加...。

`truncatewords_html` 过滤器可以对 html 代码按单词进行截取并添加...。

## 使用方法

`truncatechars` 过滤器的使用方法：

```twig
{{ obj|urlencode:number }}
```

`truncatechars_html` 过滤器的使用方法：

```twig
{{ obj|truncatechars_html:number }}
```

`truncatewords` 过滤器的使用方法：

```twig
{{ obj|truncatewords:number }}
```

`truncatewords_html` 过滤器的使用方法：

```twig
{{ obj|truncatewords_html:number }}
```

比如需要将 `Joel is a slug` 截取 9 个字符，多出部分使用...代替，则可以这么写：

```twig
{{ "Joel is a slug"|truncatechars:9 }}
# 显示结果
Joel i...
```

## 示例演示

`truncatechars` 过滤器

```twig
{{ "Joel is a slug"|truncatechars:9 }}
{{ "Joel is a slug"|truncatechars:13 }}
{{ "Joel is a slug"|truncatechars:14 }}
{{ "你好世界"|truncatechars:1 }}
{{ "你好世界"|truncatechars:2 }}
# 显示结果
Joel i...
Joel is a ...
Joel is a slug
你
你好
```

`truncatewords` 过滤器

```twig
{% filter truncatewords:9 %}{% lorem 25 w %}{% endfilter %}
{% filter wordcount %}{% filter truncatewords:9 %}{% lorem 25 w %}{% endfilter %}{% endfilter %}
{{ "你好世界"|truncatewords:0 }}
{{ "你好世界"|truncatewords:1 }}
{{ "你好世界"|truncatewords:2 }}
# 显示结果
Lorem ipsum dolor sit amet, consectetur adipisici elit, sed ...
10

你好世界
你好世界
```

`truncatechars_html` 过滤器

```twig
{{ "This is a long test which will be cutted after some chars."|truncatechars_html:25 }}
{{ "<div class=\"foo\"><ul class=\"foo\"><li class=\"foo\"><p class=\"foo\">This is a long test which will be cutted after some chars.</p></li></ul></div>"|truncatechars_html:25 }}
{{ "<p class='test' id='foo'>This is a long test which will be cutted after some chars.</p>"|truncatechars_html:25 }}
{{ "<a name='link'><p>This </a>is a long test which will be cutted after some chars.</p>"|truncatechars_html:25 }}
{{ "<p>This </a>is a long test which will be cutted after some chars.</p>"|truncatechars_html:25 }}
{{ "<p>This is a long test which will be cutted after some chars.</p>"|truncatechars_html:7 }}
# 显示结果
This is a long test wh...
<div class="foo"><ul class="foo"><li class="foo"><p class="foo">This is a long test wh...</p></li></ul></div>
<p class='test' id='foo'>This is a long test wh...</p>
<a name='link'><p>This </a>is a long test wh...</p>
<p>This </a>is a long test wh...</p>
<p>This...</p>
```

`truncatewords_html` 过滤器

```twig
{{ "This is a long test which will be cutted after some words."|truncatewords_html:25|safe }}
{{ "<div class=\"foo\"><ul class=\"foo\"><li class=\"foo\"><p class=\"foo\">This is a long test which will be cutted after some chars.</p></li></ul></div>"|truncatewords_html:5 }}
{{ "<p>This. is. a. long test. Test test, test.</p>"|truncatewords_html:8 }}
{{ "<a name='link' href=\"https://....\"><p class=\"foo\">This </a>is a long test, which will be cutted after some words.</p>"|truncatewords_html:5 }}
{{ "<p>This </a>is a long test, which will be cutted after some words.</p>"|truncatewords_html:5 }}
{{ "<p>This is a long test which will be cutted after some words.</p>"|truncatewords_html:2 }}
{{ "<p>This is a long test which will be cutted after some words.</p>"|truncatewords_html:0 }}
# 显示结果
This is a long test which will be cutted after some words.
<div class="foo"><ul class="foo"><li class="foo"><p class="foo">This is a long test ...</p></li></ul></div>
<p>This. is. a. long test. Test test, test....</p>
<a name='link' href="https://...."><p class="foo">This </a>is a long test,...</p>
<p>This </a>is a long test,...</p>
<p>This is ...</p>
```

# 过滤器：查找并将文本中的 url 字符串解析成可点击的 a 标签

## AICMS 模板中怎么查找并将文本中的 url 字符串解析成可点击的 a 标签？

`urlize` 过滤器可以查找并将文本中的 url 字符串解析成可点击的 a 标签。

`urlizetrunc` 过滤器可以查找并将文本中的 url 字符串解析成可点击的 a 标签，并且可以指定 a 标签显示的文字按指定长度截取显示。

## 使用方法

`urlize` 过滤器的使用方法：

```twig
{{ obj|urlize }}
```

`urlizetrunc` 过滤器的使用方法：

```twig
{{ obj|urlizetrunc:number }}
```

## 示例演示

`urlize` 过滤器

```twig
{{ "http://www.florian-schlachter.de"|urlize|safe }}
{{ "www.florian-schlachter.de"|urlize|safe }}
{{ "florian-schlachter.de"|urlize|safe }}
{% filter urlize:true|safe %}
Please mail me at demo@example.com or visit mit on:
- lorem ipsum github.com/flosch/pongo2 lorem ipsum
- lorem ipsum http://www.florian-schlachter.de lorem ipsum
- lorem ipsum https://www.florian-schlachter.de lorem ipsum
- lorem ipsum https://www.florian-schlachter.de lorem ipsum
- lorem ipsum www.florian-schlachter.de lorem ipsum
- lorem ipsum www.florian-schlachter.de/test="test" lorem ipsum
{% endfilter %}
--
{% filter urlize:false|safe %}
Please mail me at demo@example.com or visit mit on:
- lorem ipsum github.com/flosch/pongo2 lorem ipsum
- lorem ipsum http://www.florian-schlachter.de lorem ipsum
- lorem ipsum https://www.florian-schlachter.de lorem ipsum
- lorem ipsum https://www.florian-schlachter.de lorem ipsum
- lorem ipsum www.florian-schlachter.de lorem ipsum
- lorem ipsum www.florian-schlachter.de/test="test" lorem ipsum
{% endfilter %}
# 结果显示
<a href="http://www.florian-schlachter.de" rel="nofollow">http://www.florian-schlachter.de</a>
<a href="http://www.florian-schlachter.de" rel="nofollow">www.florian-schlachter.de</a>
<a href="http://florian-schlachter.de" rel="nofollow">florian-schlachter.de</a>

Please mail me at <a href="mailto:demo@example.com">demo@example.com</a> or visit mit on:
- lorem ipsum <a href="http://github.com/flosch/pongo2" rel="nofollow">github.com/flosch/pongo2</a> lorem ipsum
- lorem ipsum <a href="http://www.florian-schlachter.de" rel="nofollow">http://www.florian-schlachter.de</a> lorem ipsum
- lorem ipsum <a href="https://www.florian-schlachter.de" rel="nofollow">https://www.florian-schlachter.de</a> lorem ipsum
- lorem ipsum <a href="https://www.florian-schlachter.de" rel="nofollow">https://www.florian-schlachter.de</a> lorem ipsum
- lorem ipsum <a href="http://www.florian-schlachter.de" rel="nofollow">www.florian-schlachter.de</a> lorem ipsum
- lorem ipsum <a href="http://www.florian-schlachter.de/test=%22test%22" rel="nofollow">www.florian-schlachter.de/test=&quot;test&quot;</a> lorem ipsum

--

Please mail me at <a href="mailto:demo@example.com">demo@example.com</a> or visit mit on:
- lorem ipsum <a href="http://github.com/flosch/pongo2" rel="nofollow">github.com/flosch/pongo2</a> lorem ipsum
- lorem ipsum <a href="http://www.florian-schlachter.de" rel="nofollow">http://www.florian-schlachter.de</a> lorem ipsum
- lorem ipsum <a href="https://www.florian-schlachter.de" rel="nofollow">https://www.florian-schlachter.de</a> lorem ipsum
- lorem ipsum <a href="https://www.florian-schlachter.de" rel="nofollow">https://www.florian-schlachter.de</a> lorem ipsum
- lorem ipsum <a href="http://www.florian-schlachter.de" rel="nofollow">www.florian-schlachter.de</a> lorem ipsum
- lorem ipsum <a href="http://www.florian-schlachter.de/test=%22test%22" rel="nofollow">www.florian-schlachter.de/test="test"</a> lorem ipsum
```

`urlizetrunc` 过滤器

```twig
{% filter urlizetrunc:15|safe %}
Please mail me at demo@example.com or visit mit on:
- lorem ipsum github.com/flosch/pongo2 lorem ipsum
- lorem ipsum http://www.florian-schlachter.de lorem ipsum
- lorem ipsum https://www.florian-schlachter.de lorem ipsum
- lorem ipsum https://www.florian-schlachter.de lorem ipsum
- lorem ipsum www.florian-schlachter.de lorem ipsum
- lorem ipsum www.florian-schlachter.de/test="test" lorem ipsum
{% endfilter %}
```

显示结果

```twig
Please mail me at <a href="mailto:demo@example.com">demo@example...</a> or visit mit on:
- lorem ipsum <a href="http://github.com/flosch/pongo2" rel="nofollow">github.com/f...</a> lorem ipsum
- lorem ipsum <a href="http://www.florian-schlachter.de" rel="nofollow">http://www.f...</a> lorem ipsum
- lorem ipsum <a href="https://www.florian-schlachter.de" rel="nofollow">https://www....</a> lorem ipsum
- lorem ipsum <a href="https://www.florian-schlachter.de" rel="nofollow">https://www....</a> lorem ipsum
- lorem ipsum <a href="http://www.florian-schlachter.de" rel="nofollow">www.florian-...</a> lorem ipsum
- lorem ipsum <a href="http://www.florian-schlachter.de/test=%22test%22" rel="nofollow">www.florian-...</a> lorem ipsum
```

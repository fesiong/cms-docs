# 过滤器：将多行文本按换行符转换成 html 标签

## AICMS 模板中怎么将多行文本按换行符转换成 html 标签？

`linebreaks` 过滤器可以将多行文本按换行符转换成 html 标签。每行开头和结尾采用`<p>`和`</p>`包裹，中间有空行则采用 `<br/>`。

还可以使用 `linebreaksbr` 来进行处理。与 `linebreaks`不同的地方是，`linebreaksbr`只是直接将换行符替换成 `<br/>`，并且不在开头和结尾添加 p 标签。

还可以使用 `linenumbers` 来给多行文本的每一行进行标号，符号从 1 开始。如 `1. `。

## 使用方法

`linebreaks` 过滤器的使用方法：

```twig
{{ obj|linebreaks }}
```

`linebreaksbr` 过滤器的使用方法：

```twig
{{ obj|linebreaksbr }}
```

`linenumbers` 过滤器的使用方法：

```twig
{{ obj|linenumbers }}
```

比如处理字符串 `this is a text\nwith a new line in it`，则可以这么写：

```twig
{{ "this is a text\nwith a new line in it"|linebreaks }}
# 显示结果
<p>this is a text<br />with a new line in it</p>
```

## 示例演示

`linebreaks` 过滤器

```twig
{{ ""|linebreaks|safe }}
{{ simple.newline_text|linebreaks|safe }}
{{ simple.long_text|linebreaks|safe }}
{{ "john doe"|linebreaks|safe }}
# 显示结果

<p>this is a text<br />with a new line in it</p>
<p>This is a simple text.</p><p>This too, as a paragraph.<br />Right?</p><p>Yep!</p>
<p>john doe</p>
```

`linebreaksbr` 过滤器

```twig
{{ ""|linebreaksbr|safe }}
{{ simple.newline_text|linebreaksbr|safe }}
{{ simple.long_text|linebreaksbr|safe }}
{{ "john doe"|linebreaksbr|safe }}
# 显示结果

this is a text<br />with a new line in it
This is a simple text.</p><p>This too, as a paragraph.<br />Right?</p><p>Yep!
john doe
```

`linenumbers` 过滤器

```twig
{{ simple.long_text|linebreaksbr }}
# 显示结果
1. This is a simple text.
2. This too, as a paragraph.
3.
4. Right?
5. Yep!
```

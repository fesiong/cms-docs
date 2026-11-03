# 过滤器：长文本自动换行

## AICMS 模板中怎么将长文本按指定长度自动换行呢？

`wordwrap` 过滤器可以将长文本按指定长度自动换行。`wordwrap`将按空格来区分单词。如果是不包含空格的，则算作一个词。因此如果是中文连续的字，则不会被换行。

## 使用方法

`wordwrap` 过滤器的使用方法：

```twig
{{ obj|wordwrap:number }}
```

## 示例演示

```twig
{{ ""|wordwrap:2 }}
{% filter wordwrap:5 %}{% lorem 26 w %}{% endfilter %}
```

显示结果

```twig

Lorem ipsum dolor sit amet,
consectetur adipisici elit, sed eiusmod
tempor incidunt ut labore et
dolore magna aliqua. Ut enim
ad minim veniam, quis nostrud
exercitation
```

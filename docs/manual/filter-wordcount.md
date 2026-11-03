# 过滤器：计算字符串中单词数量

## AICMS 模板中怎么计算字符串中单词数量呢？

`wordcount` 过滤器可以计算字符串中单词数量。`wordcount`将按空格来区分单词。如果是不包含空格的，则算作一个词。返回的是整数。

## 使用方法

`wordcount` 过滤器的使用方法：

```twig
{{ obj|wordcount }}
```

## 示例演示

```twig
{{ ""|wordcount }}
{% filter wordcount %}{% lorem 25 w %}{% endfilter %}
```

显示结果

```twig
0
25
```

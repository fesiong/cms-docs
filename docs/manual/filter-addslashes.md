# 过滤器：预定义字符前添加反斜杠

## AICMS 模板中怎么给字符串中的预定义字符前添加反斜杠？

`addslashes` 过滤器可以指定的预定义字符前添加反斜杠。这些字符是单引号（'）、双引号（"）和反斜线（\）。

## 使用方法

`addslashes` 过滤器的使用方法：

```twig
{{ obj|addslashes }}
```

比如将 `AICMS\"CMS\"` 中的预定义字符添加反斜杠，则可以这么写：

```twig
{{ "AICMS\"CMS\""|addslashes|safe }}
# 显示结果
AICMS\"CMS\"
```

## 示例演示

```twig
{{ "AICMS"|addslashes|safe }}
{{ "This is \\a Test. \"Yep\". 'Yep'."|addslashes|safe }}
# 显示结果
AICMS
This is \\a Test. \"Yep\". \'Yep\'.
```

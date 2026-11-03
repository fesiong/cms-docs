# 过滤器：转换数字字符串为浮点数或整数

## AICMS 模板中怎么转换数字字符串为浮点数或整数？

`float` 过滤器可以将数字字符串转换为浮点数。如果转换失败，则返回 `0.0`。

`integer` 过滤器可以将数字字符串转换为整数。如果转换失败，则返回 `0`。

## 使用方法

`float` 过滤器的使用方法：

```twig
{{ obj|float }}
```

`integer` 过滤器的使用方法：

```twig
{{ obj|integer }}
```

## 示例演示

`float` 过滤器

```twig
{{ "foobar"|float }}
{{ nil|float }}
{{ "5.5"|float }}
{{ 5|float }}
{{ "5.6"|integer|float }}
{{ -100|float }}
{% if 5.5 == 5.500000 %}5.5 is 5.500000{% endif %}
{% if 5.5 != 5.500001 %}5.5 is not 5.500001{% endif %}
```

显示结果

```twig
0.000000
0.000000
5.500000
5.000000
5.000000
-100.000000
5.5 is 5.500000
5.5 is not 5.500001
```

`integer` 过滤器

```twig
{{ "foobar"|integer }}
{{ nothing|integer }}
{{ "5.4"|float|integer }}
{{ "5.5"|float|integer }}
{{ "5.6"|float|integer }}
{{ 6|float|integer }}
{{ -100|integer }}
```

显示结果

```twig
0
0
5
5
5
6
-100
```

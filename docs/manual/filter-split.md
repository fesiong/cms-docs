# 过滤器：字符串按指定分隔符切割成数组

## AICMS 模板中如何将特定格式的字符串按指定分隔符切割成数组？

`split` 过滤器可以将特定格式的字符串按指定分隔符切割成数组。如果分隔符不存在于字符串中，则会返回长度为 1 的数组，数组的值为字符串本身。如果分隔符为空，则会按每个 utf8 字符来拆分成数组。

也可以使用 `make_list` 来讲字符串快速切割成数组。`make_list` 会将每一个字符拆分成数组一个值，一个字母是一个，一个汉字也是一个。

## 使用方法

`split` 过滤器的使用方法：

```twig
{{ obj|split:"拼接符" }}
```

`make_list` 过滤器的使用方法：

```twig
{{ obj|make_list }}
```

比如需要将 `splits, the, string, AICMS` 按 `, ` 切割成数组，则可以这么写：

```twig
{{ "splits, the, string, AICMS"|split:", "|stringformat:"%#v" }}
# 显示结果
[]string{"splits", "the", "string", "AICMS"}
```

`split`过滤器同样支持在赋值标签（set）中使用，将判断结果存储到一个变量中，如：

```twig
{% set values = "splits, the, string, AICMS"|split:", " %}
{% for item in values %}
<span>{{item}}/</span>
{% endfor %}
# 显示结果
splits/ the/ string/ AICMS/
```

## 示例演示

`split` 过滤器

```twig
{{ "splits, the, string, AICMS"|split:", " }}
{{values|stringformat:"%#v"}}
# 显示结果
[]string{"splits", "the", "string", "AICMS"}
```

```twig
{{ "Hello, 99, 3.140000, good"|split:", "|join:", " }}
# 显示结果
Hello, 99, 3.140000, good
```

`make_list` 过滤器

```twig
{{ "john doe"|make_list|join:", " }}
{% for char in "john doe"|make_list %}{{ char }}{% endfor %}
# 显示结果
j, o, h, n,  , d, o, e
john doe
```

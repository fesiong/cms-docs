# 过滤器：将一行文字按空格拆分成数组

## AICMS 模板中怎么将一行文字按空格拆分成数组？

`fields` 过滤器可以在模板中将一行文字按照空格来拆分成数组。定义的数组是一个 `[]string{}`，可以在后续中进行遍历输出结果。

## 使用方法

`fields` 过滤器的用法：

```twig
{% set values = "文字内容"|fields %}
```

```twig
{% set values = "splits the string AICMS"|fields %}
{{values|stringformat:"%#v"}}
# 显示结果
[]string{"splits", "the", "string", "AICMS"}
```

## 示例演示

```twig
{% set values = "splits the string AICMS"|fields %}
{{values|stringformat:"%#v"}}
# 显示格式
[]string{"splits", "the", "string", "AICMS"}
# 遍历输出
{% for item in values %}
<span>{{item}}</span>/
{% endfor %}
# 显示结果
splits/ the/ string/ AICMS/
```

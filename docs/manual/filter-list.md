# 过滤器：在模板中定义数组

## AICMS 模板中怎么在模板中定义数组？

`list` 过滤器可以在模板中定义数组。定义的数组是一个 `[]string{}`，可以在后续中进行遍历输出结果。

## 使用方法

`list` 过滤器的用法：

```twig
{% set values = '["关键词1","关键词2","关键词3"]'|list %}
```

待转换字符串用单引号或双引号包裹，用`[`、`]`来定义数组的开始和结束，内部关键词之间用英文`,`隔开，关键词之间可以用引号包裹，也可以忽略。

```twig
{% set values = '["AICMS","AICMS","内容管理系统","免费建站系统","免费模板",4,5]'|list %}
{% for item in values %}
<span>{{item}}</span>/
{% endfor %}
# 显示结果
AICMS/ AICMS/ 内容管理系统/ 免费建站系统/ 免费模板/ 4/ 5/
```

## 示例演示

```twig
{% set values = '["AICMS","AICMS","内容管理系统","免费建站系统","免费模板"]'|list %}
# 显示格式：
{{values|stringformat:"%#v"}}
# 遍历输出
{% for item in values %}
<span>{{item}}</span>/
{% endfor %}
# 显示结果
AICMS/ AICMS/ 内容管理系统/ 免费建站系统/ 免费模板/
```

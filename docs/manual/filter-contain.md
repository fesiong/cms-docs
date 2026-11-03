# 过滤器：判断文字、数组是否包含指定关键词

## AICMS 模板中怎么判断一行文字字符串中是否包含有某个关键词？

`contain` 过滤器可以判断某个关键词是否包含在一行字符串、数组（slice）、键值对（map）、结构体（struct）中，结果将会返回一个布尔值（bool）。

## 使用方法

`contain` 过滤器的使用方法：

```twig
{{obj|contain:关键词}}
```

比如判断 `欢迎使用AICMS（AICMS）` 中是否包含 `CMS`，则可以这么写：

```twig
{{"欢迎使用AICMS（AICMS）"|contain:"CMS"}}
# 显示结果
True
```

`contain`过滤器同样支持在赋值标签（set）中使用，将判断结果存储到一个变量中，如：

```twig
{% set source = "欢迎使用AICMS（AICMS）" %}
{% set isContain = source|contain:"CMS" %}
{% if isContain %}
{{source}}中包含"CMS"
{% endif %}
# 显示结果
欢迎使用AICMS（AICMS）中包含"CMS"
```

## 示例演示

### 判断一行文字是否包含某个关键词

直接输出结果：

```twig
{{"欢迎使用AICMS（AICMS）"|contain:"CMS"}}
# 显示结果
True
```

将结果赋值给一个变量，用于其他条件判断：

```twig
{% set source = "欢迎使用AICMS（AICMS）" %}
{% set isContain = source|contain:"CMS" %}
{% if isContain %}
{{source}}中包含"CMS"
{% endif %}
# 显示结果
欢迎使用AICMS（AICMS）中包含"CMS"。
```

### 判断一个数组中是否存在某个关键词的值

假设一个数组是：`values = ["AICMS","AICMS","内容管理系统","免费建站系统","免费模板"]`。

直接输出结果：

```twig
{{values|contain:"AICMS"}}
# 显示结果
True
```

将结果赋值给一个变量，用于其他条件判断：

```twig
{% set isContain = values|contain:"AICMS" %}
{% if isContain %}
{{values|join:","}}中包含"AICMS"
{% endif %}
# 显示结果
AICMS,AICMS,内容管理系统,免费建站系统,免费模板中包含"AICMS"的值。
```

### 判断一个键值对（map）、结构体（struct）中是否存在某个关键词的键名

假设一个键值对是是：`webInfo = {Title:"AICMS",Keyword:"AICMS",Description:"免费建站系统"}`。

直接输出结果：

```twig
{{values|contain:"Title"}}
# 显示结果
True
```

将结果赋值给一个变量，用于其他条件判断：

```twig
{% set isContain = values|contain:"Title" %}
{% if isContain %}
{{values|stringformat:"%#v"}}中包含一个叫"Title"的键名
{% endif %}
# 显示结果
 {Title:"AICMS",Keyword:"AICMS",Description:"免费建站系统"}中包含一个叫"Title"的键名。
```

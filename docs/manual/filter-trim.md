# 过滤器：删除字符串所有前导和尾随空格、特定字符

## AICMS 模板中怎么删除一个字符串的首尾所有空格或特定字符？

`trim`、`trimLeft`、`trimRight` 过滤器可以分别删除字符串首尾空格、特定字符。

- `trim` 过滤器可以删除字符串首尾空格或特定字符；
- `trimLeft` 过滤器可以删除字符串前导空格或特定字符；
- `trimRight` 过滤器可以删除字符串尾随空格或特定字符。

## 使用方法

### `trim` 过滤器的用法

```twig
# 仅删除空格、换行符
{{obj|trim}}
# 或者 删除指定字符
{{obj|trim:关键词}}
```

比如删除字符串 `欢迎使用AICMS` 的首尾空格，则可以这么写：

```twig
{{" 欢迎使用AICMS "|trim}}
# 显示结果
欢迎使用AICMS
```

删除字符串 `欢迎使用AICMS` 的首尾字符`欢迎CMS`，则可以这么写：

```twig
{{"欢迎使用AICMS"|trim:"欢迎CMS"}}
# 显示结果
使用AICMS
```

`trim`过滤器同样支持在赋值标签（set）中使用，将处理结果存储到一个变量中，如：

```twig
{% set source = "欢迎使用AICMS（AICMS）" %}
{% set result = source|trim:"欢迎" %}
{{result}}
# 显示结果
使用AICMS（AICMS）
```

### `trimLeft` 过滤器的用法

```twig
# 仅删除空格、换行符
{{obj|trimLeft}}
# 或者 删除指定字符
{{obj|trimLeft:关键词}}
```

比如删除字符串 `欢迎使用AICMS` 的前导空格，则可以这么写：

```twig
{{" 欢迎使用AICMS "|trimLeft}}
# 显示结果
欢迎使用AICMS
```

删除字符串 `欢迎使用AICMS` 的前导字符`欢迎`，则可以这么写：

```twig
{{"欢迎使用AICMS"|trimLeft:"欢迎"}}
# 显示结果
使用AICMS
```

`trimLeft`过滤器同样支持在赋值标签（set）中使用，将处理结果存储到一个变量中，如：

```twig
{% set source = "欢迎使用AICMS（AICMS）" %}
{% set result = source|trimLeft:"欢迎" %}
{{result}}
# 显示结果
使用AICMS（AICMS）
```

### `trimRight` 过滤器的用法

```twig
# 仅删除空格、换行符
{{obj|trimRight}}
# 或者 删除指定字符
{{obj|trimRight:关键词}}
```

比如删除字符串 `欢迎使用AICMS` 的前导空格，则可以这么写：

```twig
{{" 欢迎使用AICMS "|trimRight}}
# 显示结果
欢迎使用AICMS
```

删除字符串 `欢迎使用AICMS` 的前导字符`欢迎`，则可以这么写：

```twig
{{"欢迎使用AICMS"|trimRight:"CMS"}}
# 显示结果
欢迎使用AICMS
```

`trimLeft`过滤器同样支持在赋值标签（set）中使用，将处理结果存储到一个变量中，如：

```twig
{% set source = "欢迎使用AICMS（AICMS）" %}
{% set result = source|trimRight:"）" %}
{{result}}
# 显示结果
欢迎使用AICMS（AICMS
```

## 示例演示

```twig
{{" 欢迎使用AICMS（AICMS） "|trim}}
# 显示结果
欢迎使用AICMS（AICMS）
```

```twig
{{"欢迎使用AICMS（AICMS）"|trim:"欢迎"}}
# 显示结果
使用AICMS（AICMS）
```

```twig
{{" 欢迎使用AICMS（AICMS） "|trimLeft}}
# 显示结果
欢迎使用AICMS（AICMS）
```

```twig
{{"欢迎使用AICMS（AICMS）"|trimLeft:"欢迎"}}
# 显示结果
使用AICMS（AICMS）
```

```twig
{{"欢迎使用AICMS（AICMS） "|trimRight}}
# 显示结果
欢迎使用AICMS（AICMS）
```

```twig
{{"欢迎使用AICMS（AICMS） "|trimRight:"） "}}
# 显示结果
欢迎使用AICMS（AICMS
```

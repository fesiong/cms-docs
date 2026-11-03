# 过滤器：计算某个关键词在一行字符串中出现的次数、数组中出现次数

## AICMS 模板中怎么计算某个关键词在一行字符串或数组中出现的次数？

`count` 过滤器可以计算某个关键词在一行字符串或数组（array/slice）中出现的次数。

## 使用方法

`count` 过滤器的使用方法：

```twig
{{obj|count:关键词}}
```

比如计算 `欢迎使用AICMS（AICMS）` 中计算 `CMS`出现的次数，则可以这么写：

```twig
{{"欢迎使用AICMS（AICMS）"|count:"CMS"}}
# 显示结果
2
```

## 示例演示

### 获取一行文字中某个关键词出现的次数

直接输出结果：

```twig
{{"欢迎使用AICMS（AICMS）"|count:"CMS"}}
# 显示结果
2
```

### 获取一个数组中某个关键词出现的次数

数组中需要关键词等于 数组的值或者是索引，需要完全相等，不能部分匹配。

```twig
{% set values = "splits the string AICMS"|fields %}
{{values|count:"the"}}
# 显示结果
1
```

```twig
{% set values = "splits the string AICMS"|fields %}
{{values|count:"AICMS"}}
# 显示结果
0
```

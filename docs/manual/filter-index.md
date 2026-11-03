# 过滤器：获取某个关键词在一行字符串或数组中出现的位置

## AICMS 模板中怎么获取某个关键词在一行字符串或数组中出现的位置？

`index` 过滤器可以计算某个关键词在一行字符串或数组（array/slice）中出现的位置。如果字符串中包含多个需要查找的关键词，则 index 返回的是首次出现的位置。如果没有找到，则返回-1。注意：如果字符串中有中文，则计算位置的时候，一个中文算 3 个位置。

## 使用方法

`index` 过滤器的使用方法：

```twig
{{obj|index:关键词}}
```

比如判断 `欢迎使用AICMS（AICMS）` 中计算 `CMS`出现的位置，则可以这么写：

```twig
{{"欢迎使用AICMS（AICMS）"|index:"CMS"}}
# 显示结果
18
```

## 示例演示

### 计算一行文字中某个关键词出现的位置

直接输出结果：

```twig
{{"欢迎使用AICMS（AICMS）"|index:"CMS"}}
# 显示结果
18
```

### 计算一个数组中某个关键词出现的位置

数组中需要关键词等于 数组的值或者是索引，需要完全相等，不能部分匹配。

```twig
{% set values = "splits the string AICMS"|fields %}
{{values|index:"the"}}
# 显示结果
1
```

```twig
{% set values = "splits the string AICMS"|fields %}
{{values|index:"AICMS"}}
# 显示结果
-1
```

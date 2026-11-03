# 过滤器：单词的复数形式

## AICMS 模板中如何将一个单词根据数量转为复数形式？

`pluralize` 过滤器可以将一个单词根据数量转为复数形式。

## 使用方法

`pluralize` 过滤器的使用方法：

```twig
{{ obj|pluralize:"复数附加词" }}
```

`pluralize`需要指定当前数量，并添加复数的词。支持 0 到 2 个词，2 个词的时候使用`,`隔开。

比如 `customer`，则可以这么写：

```twig
customer{{ 1|pluralize }}
# 显示结果
customer
```

## 示例演示

```twig
customer{{ 0|pluralize }}
customer{{ 1|pluralize }}
customer{{ 2|pluralize }}
cherr{{ 0|pluralize:"y,ies" }}
cherr{{ 1|pluralize:"y,ies" }}
cherr{{ 2|pluralize:"y,ies" }}
walrus{{ 0|pluralize:"es" }}
walrus{{ 1|pluralize:"es" }}
walrus{{ simple.number|pluralize:"es" }}
# 显示结果
customers
customer
customers
cherries
cherry
cherries
walruses
walrus
walruses
```

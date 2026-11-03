# 过滤器：获取字符串、数组、键值对的长度

## AICMS 模板中怎么获取字符串、数组、键值对的长度？

`length` 过滤器可以获取字符串、数组、键值对的长度。对于字符串，则计算它的 utf8 实际字符的数量，一个字母为一个，一个汉字也为 1 个。数组和键值对则计算它们的索引数量。

还可以使用 `length_is` 来进行计算长度的同时，与输入的长度值做对比，并返回是否一致的布尔值（bool）。

## 使用方法

`length` 过滤器的使用方法：

```twig
{{ obj|length }}
```

比如需要返回 `john doe` 的长度，则可以这么写：

```twig
{{ "john doe"|length }}
# 显示结果
8
```

## 示例演示

`length` 过滤器

```twig
{{ "john doe"|length }}
{{ "你好世界"|length }}
# 显示结果
8
4
```

`length_is` 过滤器

```twig
{{ "john doe"|length_is:8 }}
{{ "john doe"|length_is:10 }}
{{ "john doe"|length_is:"8" }}
{{ "john doe"|length_is:"10" }}
{{ 5|length_is:1 }}
{{ "你好世界"|length_is:4 }}
{{ "你好世界"|length_is:3 }}
{{ "你好世界"|length_is:5 }}
# 显示结果
True
False
True
False
False
True
False
False
```

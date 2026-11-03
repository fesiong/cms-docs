# 过滤器：将数组按指定拼接字符链接成字符串

## AICMS 模板中如何将数组按指定拼接字符链接成字符串？

`join` 过滤器可以将数组的值按照指定的拼接符链接组装成一个新的字符串。如果原对象是字符串，则会将在字符与字符直接添加拼接符。

## 使用方法

`join` 过滤器的使用方法：

```twig
{{ obj|join:"拼接符" }}
```

比如需要将 `["splits", "the", "string", "AICMS"]` 拼接成字符串，则可以这么写：

```twig
{% set values = "splits the string AICMS"|fields %}
{{ values|join:", " }}
# 显示结果
splits, the, string, AICMS
```

## 示例演示

```twig
{{ values|join:", " }}
# 显示结果
splits, the, string, AICMS
```

```twig
{{ "AI内容管理系统"|join:", " }}
# 显示结果
安, 企, 内, 容, 管, 理, 系, 统
```

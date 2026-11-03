# 过滤器：将英文字符串字母转换为大写或小写

## AICMS 模板中怎么将英文字符串字母转换为大写或小写？

`capfirst` 过滤器可以将英文字符串第一个字母转换为大写。只有英文字母会被转换。

`lower` 过滤器可以将英文字符串中所有的字母转换成小写。

`upper` 过滤器可以将英文字符串中所有的字母转换成大写。

`title` 过滤器可以将英文字符串中所有的单词的首字母转换成大写。

## 使用方法

`capfirst` 过滤器的使用方法：

```twig
{{ obj|capfirst }}
```

`lower` 过滤器的使用方法：

```twig
{{ obj|lower }}
```

`upper` 过滤器的使用方法：

```twig
{{ obj|upper }}
```

`title` 过滤器的使用方法：

```twig
{{ obj|title }}
```

比如将 `hello there!` 中的第一个字母转换为大写，则可以这么写：

```twig
{{ "hello there!"|capfirst }}
# 显示结果
Hello there!
```

## 示例演示

`capfirst` 过滤器

```twig
{{ ""|capfirst }}
{{ 5|capfirst }}
{{ "h"|capfirst }}
{{ "hello there!"|capfirst }}
{{ "AI内容管理系统"|capfirst }}
# 显示结果


H
Hello there!
AI内容管理系统
```

`lower` 过滤器

```twig
{{ ""|lower }}
{{ 5|lower }}
{{ "h"|lower }}
{{ "hello there!"|lower }}
{{ "HELLO THERE!"|lower }}
{{ "hELLO tHERE!"|lower }}
{{ simple.chinese_hello_world|lower }}
# 显示结果


h
hello there!
hello there!
hello there!
你好世界
```

`upper` 过滤器

```twig
{{ ""|upper }}
{{ 5|upper }}
{{ "h"|upper }}
{{ "hello there!"|upper }}
{{ "HELLO THERE!"|upper }}
{{ "hELLO tHERE!"|upper }}
{{ "你好世界"|upper }}
# 显示结果


H
HELLO THERE!
HELLO THERE!
HELLO THERE!
你好世界
```

`title` 过滤器

```twig
{{ ""|title }}
{{ 5|title }}
{{ "h"|title }}
{{ "hello there!"|title }}
{{ "HELLO THERE!"|title }}
{{ "hELLO tHERE!"|title }}
{{ "你好世界"|title }}
# 显示结果


H
Hello There!
Hello There!
Hello There!
你好世界
```

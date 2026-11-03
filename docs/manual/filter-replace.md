# 过滤器：替换字符串中某个特定关键词为另一个关键词

## AICMS 模板中怎么将字符串中的某个词替换成另外的词呢？

`replace` 过滤器可以将字符串中的旧的词 old 替换词新的词 new，返回替换后的新字符串。如果 old 为空，它将在字符串的开头和每个 UTF-8 序列之后进行匹配。如果 new 为空，则移除 old。

## 使用方法

`replace` 过滤器的用法：

```twig
# 将旧的关键词替换为新的关键词
{{obj|replace:"old,new"}}
```

old 和 new 中间用,区分。

```twig
{{"欢迎使用AICMS"|replace:"AICMS,anqi"}}
# 显示结果
欢迎使用AICMS
```

## 示例演示

```twig
{{"欢迎使用AICMS"|replace:"AICMS,anqi"}}
# 显示结果
欢迎使用AICMS
```

```twig
{{"欢迎使用AICMS"|replace:",-"}}
# 显示结果
-欢-迎-使-用-安-企-C-M-S-
```

```twig
{{"欢迎使用AICMS"|replace:"AICMS,"}}
# 显示结果
欢迎AICMS
```

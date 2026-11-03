# 过滤器：指定重复多次输出字符串

## AICMS 模板中怎么将一个字符串按指定次数重复输出呢？

`repeat` 过滤器可以将一个字符串按指定次数重复。

## 使用方法

`repeat` 过滤器的使用方法：

```twig
{{obj|repeat:次数}}
```

比如重复 `AICMS` 5 次，则可以这么写：

```twig
{{"AICMS"|repeat:5}}
# 显示结果
AICMSAICMSAICMSAICMSAICMS
```

## 示例演示

```twig
{{"AICMS"|repeat:5}}
# 显示结果
AICMSAICMSAICMSAICMSAICMS
```

# 过滤器：判断一个数字是否可以作为被除数

## AICMS 模板中怎么判断一个数字或它的计算结果是否可以作为被除数？

`divisibleby` 过滤器可以判断一个数字或它的计算结果是否可以作为被除数。 该过滤器将返回一个布尔值（bool），True 表示可以，False 表示不可以。

## 使用方法

`divisibleby` 过滤器的使用方法：

```twig
{{ number|divisibleby:取模值 }}
```

比如下方 判断 `21` 用 `3` 取模后，是否可以作为被除数，则可以这么写：

```twig
{{ 22|divisibleby:"3" }}
# 显示结果
False
```

## 示例演示

```twig
{{ 21|divisibleby:3 }}
{{ 21|divisibleby:"3" }}
{{ 21|float|divisibleby:"3" }}
{{ 22|divisibleby:"3" }}
{{ 85|divisibleby:42 }}
{{ 84|divisibleby:42 }}
# 显示结果
True
True
True
False
False
True
```

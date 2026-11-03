# 过滤器：url 参数转义

## AICMS 模板中如何对 url 参数进行转义？

`urlencode` 过滤器可以对 URL 参数进行转义。

`iriencode` 过滤器可以对 url 参数进行转义，除了`/#%[]=:;$&()+,!?*@'~` 外的其他字符，都会被按照 URL 参数转义方式进行转义。

## 使用方法

`urlencode` 过滤器的使用方法：

```twig
{{ obj|urlencode }}
```

`iriencode` 过滤器的使用方法：

```twig
{{ obj|iriencode }}
```

比如需要将 `?foo=123&bar=yes` 转义，则可以这么写：

```twig
{{ "http://www.example.org/foo?a=b&c=d"|urlencode }}
# 显示结果
http%3A%2F%2Fwww.example.org%2Ffoo%3Fa%3Db%26c%3Dd
```

## 示例演示

```twig
{{ "http://www.example.org/foo?a=b&c=d"|urlencode }}
{{ "?foo=123&bar=yes"|iriencode }}
# 显示结果
http%3A%2F%2Fwww.example.org%2Ffoo%3Fa%3Db%26c%3Dd
?foo=123&amp;bar=yes
```

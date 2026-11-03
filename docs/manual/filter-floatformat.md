# 过滤器：浮点数保留指定位数小数点

## AICMS 模板中怎么将一个浮点数保留 2 位小数输出？

`floatformat` 过滤器可以将一个浮点数保留 2 位小数输出。也可以保留指定的其他位数小数点。如保留小数点后 3 位等。同时支持负数位数，如果设置的是负数，则从最后一位往前推算。

## 使用方法

`floatformat` 过滤器的使用方法：

```twig
{{ obj|floatformat:number }}
```

比如需要格式化 `34.23234` 保留 3 位小数，则可以这么写：

```twig
{{ 34.23234|floatformat:3 }}
# 显示结果
34.232
```

## 示例演示

```twig
{{ 34.23234|floatformat }}
{{ 34.00000|floatformat }}
{{ 34.26000|floatformat }}
{{ "34.23234"|floatformat }}
{{ "34.00000"|floatformat }}
{{ "34.26000"|floatformat }}
{{ 34.23234|floatformat:3 }}
{{ 34.00000|floatformat:3 }}
{{ 34.26000|floatformat:3 }}
{{ 34.23234|floatformat:"0" }}
{{ 34.00000|floatformat:"0" }}
{{ 39.56000|floatformat:"0" }}
{{ 34.23234|floatformat:"-3" }}
{{ 34.00000|floatformat:"-3" }}
{{ 34.26000|floatformat:"-3" }}
# 显示结果
34.2
34
34.3
34.2
34
34.3
34.232
34.000
34.260
34
34
40
34.232
34
34.260
```

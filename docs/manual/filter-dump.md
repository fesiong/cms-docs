# 过滤器：打印变量的结构类型和值

## AICMS 模板中怎么查看变量的结构类型？

`dump` 过滤器可以将某个变量的结构、类型和值打印出来。

## 使用方法

`dump` 过滤器的使用方法：

```twig
{{ obj|dump }}
```

比如要查看 bannerItem 的结构，则可以这么写：

```twig
{{ item|dump }}
# 显示结果
&config.BannerItem{Logo:"http://127.0.0.1:8001/uploads/202309/14/eba5aa9dc4c45d18.webp", Id:1, Link:"", Alt:"Hello", Description:"", Type:"default"}
```

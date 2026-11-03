# 过滤器：或与非三种状态

## AICMS 模板中怎么判断或与非三种状态？

`yesno` 过滤器可以或与非三种状态。`yesno` 默认的值有 3 种，分别是 “yes”，“no”，“maybe”。你也可以对这三种值自定义为其他值。
当值为 false 的时候，返回 no，当值为 true 的时候，返回 yes，当值是 nil 即空值的时候，返回 maybe。

## 使用方法

`yesno` 过滤器的使用方法：

```twig
{{ obj|yesno }}
```

## 示例演示

```twig
{{ simple.bool_true|yesno }}
{{ simple.bool_false|yesno }}
{{ simple.nil|yesno }}
{{ simple.nothing|yesno }}
{{ simple.bool_true|yesno:"ja,nein,vielleicht" }}
{{ simple.bool_false|yesno:"ja,nein,vielleicht" }}
{{ simple.nothing|yesno:"ja,nein" }}
```

显示结果

```twig
yes
no
maybe
maybe
ja
nein
maybe
```

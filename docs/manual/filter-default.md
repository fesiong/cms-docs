# 过滤器：数字或字符串、对象默认值设置

## AICMS 模板中如果数字或字符串、对象没有值怎么给数字或字符串设置默认值？

`default` 过滤器可以在如果数字或字符串、对象没有值的时候给数字或字符串设置默认值。

`default_if_none` 过滤器可以判断指针类型的对象是否为空，如果为空，则设置默认值。

## 使用方法

`default` 过滤器的使用方法：

```twig
{{ obj|default:默认值 }}
```

比如下方，则可以这么写：

```twig
{{ nothing|default:"-" }}
# 显示结果
-
```

`default_if_none` 过滤器的使用方法：

```twig
{{ obj|default:默认值 }}
```

比如下方，则可以这么写：

```twig
{{ nil|default_if_none:"n/a" }}
# 显示结果
n/a
```

## 示例演示

```twig
{{ simple.nothing|default:"n/a" }}
{{ nothing|default:"-" }}
{{ 42|default:"n/a" }}
{{ 5|default:"n/a" }}
# 显示结果
n/a
-
42
5
```

```twig
{{ simple.nothing|default_if_none:"n/a" }}
{{ ""|default_if_none:"n/a" }}
{{ nil|default_if_none:"n/a" }}
# 显示结果
n/a

n/a
```

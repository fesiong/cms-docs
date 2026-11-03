# 过滤器：字符串或数组第一个值或最后一个值

## AICMS 模板中怎么获得字符串或数组第一个值或最后一个值？

`first` 过滤器可以获得字符串第一个字符或数组第一个值。如果原字符串、数组为空，什么也不返回。如果字符串是中文，则返回第一个汉字。

`last` 过滤器可以获取字符串最后一个字符或数组最后一个值。如果原字符串、数组为空，什么也不返回。如果字符串是中文，则返回最后一个汉字。

## 使用方法

`first` 过滤器的使用方法：

```twig
{{ obj|first }}
```

`last` 过滤器的使用方法：

```twig
{{ obj|last }}
```

比如需要返回 `Test` 中的第一个字符，则可以这么写：

```twig
{{ "Test"|first }}
# 显示结果
T
```

## 示例演示

`first` 过滤器

```twig
{{ "Test"|first }}
{{ complex.comments|first }}
{{ 5|first }}
{{ true|first }}
{{ nothing|first }}
{{ "你好世界"|first }}
# 显示结果
T
<pongo2_test.comment Value>



你
```

`last` 过滤器

```twig
{{ "Test"|last }}
{{ complex.comments|last }}
{{ 5|last }}
{{ true|last }}
{{ nothing|last }}
{{ "你好世界"|last }}
# 显示结果
t
<pongo2_test.comment Value>



界
```

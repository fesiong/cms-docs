# 过滤器：移除 html 代码中的 html 标签

## AICMS 模板中如何移除 html 代码中的标签？

`striptags` 过滤器可以移除 html 代码中的所有 html 标签。

`removetags` 过滤器可以将移除 html 代码中指定标签。

## 使用方法

`striptags` 过滤器的使用方法：

```twig
{{ obj|striptags }}
```

`removetags` 过滤器的使用方法：

```twig
{{ obj|removetags:"标签" }}
```

可以移除多个标签，多个标签之间使用`,`隔开。

比如移除 `<strong><i>Hello!</i></strong>` 中 i 标签，则可以这么写：

```twig
{{ "<strong><i>Hello!</i></strong>"|removetags:"i"|safe }}
# 显示结果
<strong>Hello!</strong>
```

## 示例演示

```twig
{{ "<strong><i>Hello!</i></strong>"|striptags|safe }}
{{ "<strong><i>Hello!</i></strong>"|removetags:"i"|safe }}
{{ "<strong><i>Hello!</i><span>AICMS</span></strong>"|removetags:"i,span"|safe }}
# 显示结果
Hello!
<strong>Hello!</strong>
<strong>Hello!</strong>
```

# 过滤器：渲染Markdown内容为HTML

## AICMS 模板中怎么将某个变量渲染为HTML？

`render` 过滤器可以将一个变量渲染成 HTML。

## 使用方法

`render` 过滤器的使用方法：

```twig
{{ obj|render }}
```

比如我们需要将 文档的自定义字段中的 introduction 字段渲染为 HTML，则可以这么写：

```twig
{% archiveDetail introduction with name="introduction" %}
{{introduction|render|safe}}
```

或者
```twig
{# 无序的map对象 #}
<div>
    {% archiveParams params with sorted=false %}
        <div>{{params.introduction.Name}}:{{params.introduction.Value|render|safe}}</div>
    {% endarchiveParams %}
</div>
```

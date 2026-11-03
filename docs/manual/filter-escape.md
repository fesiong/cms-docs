# 过滤器：将字符串、js 代码中的特殊字符转义

## AICMS 模板中怎么将字符串、js 代码中的特殊字符如 HTML 代码转义？

`escape` 过滤器可以将字符串中的特殊字符转义。比如将 HTML 代码输出显示，而不是解析 HTML 代码。如`<` 会转换为 `&lt;`。`escape` 它只转义五个这样的字符：`<`，`>`，`&`，`'`和`"`。`<` 会转换为 `&lt;`，`>` 会转换为 `&gt;`，`&` 会转换为 `&amp;`，`"` 会转换为 `&quot;`，`'` 会转换为 `&#39;`。

也可以使用 `e` 来代替 `escape`。因为 `e` 是 `escape` 的别名，使用效果一致。

默认地，所有的标签输出都是自动转义的。因此一般情况下可以忽略这个过滤器。在某种情况下可能会需要用到。

除了使用过滤器，也支持使用 `autoescape` 标签对整块代码进行转义。

`escapejs` 过滤器可以将 js 代码中的特殊字符进行转义。如`\r` 会转换为 `\u000D`。`escapejs` 会将除了 `a-zA-Z` 或空格、`/` 外的其它字符，都转换为 `\uxxxx` 的显示形式。

## 使用方法

`escape` 和 `e` 过滤器的使用方法：

```twig
{{ "<script>"|safe|escape }}
{{ "<script>"|safe|e }}
```

`escapejs` 过滤器的使用方法：

```twig
{{ obj|escapejs|safe }}
```

比如将 `<script>` 转义，则可以这么写：

```twig
{{ "<script>"|safe|escape }}
{{ "<script>"|safe|e }}
# 显示结果
&lt;script&gt;
&lt;script&gt;
```

使用 `autoescape` 标签对整段代码进行转义处理。`autoescape` 标签需要一个参数来明确说明是需要转义还是不转义。 `on` 是转义， `off` 是不转义。

```twig
# 不转义
{% autoescape off %}
{{ "<script>alert('xss');</script>" }}
{% endautoescape %}
# 转义
{% autoescape on %}
{{ "<script>alert('xss');</script>" }}
{% endautoescape %}
# 显示结果
<script>alert('xss');</script>
&lt;script&gt;alert(&#39;xss&#39;);&lt;/script&gt;
```

## 示例演示

### `escape` 和 `e` 过滤器

直接输出结果：

```twig
{{ "<script>"|safe|escape }}
{{ "<script>"|safe|e }}
```

显示结果

```twig
&lt;script&gt;
&lt;script&gt;
```

### 使用 `autoescape`

```twig
{{ "<script>alert('xss');</script>" }}
{% autoescape off %}
{{ "<script>alert('xss');</script>" }}
{% endautoescape %}
{% autoescape on %}
{{ "<script>alert('xss');</script>" }}
{% endautoescape %}
{% autoescape off %}
{{ "<script>alert('xss');</script>"|escape }}
{% endautoescape %}
```

输出结果：

```twig
&lt;script&gt;alert(&#39;xss&#39;);&lt;/script&gt;
<script>alert('xss');</script>
&lt;script&gt;alert(&#39;xss&#39;);&lt;/script&gt;
&lt;script&gt;alert(&#39;xss&#39;);&lt;/script&gt;
```

`escapejs` 过滤器

```twig
{{ "escape sequences \r\n\'\" special chars "?!=$<>"|escapejs|safe }}
# 显示结果
escape sequences \u000D\u000A\u005C\u0027\u005C\u0022 special chars \u0022\u003F\u0021\u003D\u0024\u003C\u003E
```

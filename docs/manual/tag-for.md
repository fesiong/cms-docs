# for 循环遍历标签

`for` 遍历数组、slice 等对象。

`for`用于循环访问数组中的每个项目，从而使该项目在上下文变量中可用。

### 示例代码

例如，要显示 archiveList 中提供的文档列表：

```twig
{% for item in archives %}
<li class="item">
    <a href="/archive/{{item.Id}}" class="link">
        <h5 class="title">{{item.Title}}</h5>
    </a>
</li>
{% endfor %}
```

还可以输出 for 循环的计数，以及剩余数量，还可以使用`pluralize`判断数量是否是复数。如：

```twig
{% for item in archives %}
<li class="item">
    <a href="/archive/{{item.Id}}" class="link">
        <h5 class="title">第{{ forloop.Counter }}篇，剩余{{ forloop.Revcounter}}篇，{{ forloop.Revcounter|pluralize:"多于1篇" }}：{{item.Title}}</h5>
    </a>
</li>
{% endfor %}
```

`for` 还可以使用`reversed`翻转数组，`sorted`按 int 排序数组。如：

```twig
{% for item in archives reversed %}
<li class="item">
    <a href="/archive/{{item.Id}}" class="link">
        <h5 class="title">{{item.Title}}</h5>
    </a>
</li>
{% endfor %}
{% for item in archives sorted %}
<li class="item">
    <a href="/archive/{{item.Id}}" class="link">
        <h5 class="title">{{item.Title}}</h5>
    </a>
</li>
{% endfor %}
{% for item in archives reversed sorted %}
<li class="item">
    <a href="/archive/{{item.Id}}" class="link">
        <h5 class="title">{{item.Title}}</h5>
    </a>
</li>
{% endfor %}
```

`for`还支持判断是否为空数组或者 nil 等，使用`empty`来输出不存在的情况。如:

```twig
{% for item in archives %}
<li class="item">
    <a href="/archive/{{item.Id}}" class="link">
        <h5 class="title">{{item.Title}}</h5>
    </a>
</li>
{% empty %}
<div>没有内容</div>
{% endfor %}
```

它等价于使用 if 判断，但是这样写可以更简洁：

```twig
{% if archives %}
{% for item in archives %}
<li class="item">
    <a href="/archive/{{item.Id}}" class="link">
        <h5 class="title">{{item.Title}}</h5>
    </a>
</li>
{% endfor %}
{% else %}
<div>没有内容</div>
{% endif %}
```

`cycle` 标签。在 for 循环中，我们还可以使用`cycle`标签，来循环逐个输出定义中的变量。

每次遇到此`cycle`标签时，都会产生其参数之一。 第一个参数在第一次遇到时产生，第二个参数在第二次遇到时产生，依此类推。 一旦所有参数用尽，标记将循环到第一个参数并再次产生它。

此标记在循环中特别有用。如：

```twig
{% for item in archives %}
<li class="item">
    <a href="/archive/{{item.Id}}" class="link">
        <h5 class="title">Title,Id 逐个出现：{% cycle item.Title item.Id %}</h5>
    </a>
</li>
{% endfor %}
```

或者使用`as` 来定义别名，再通过别名输出：

```twig
{% for item in archives %}
<li class="item">
    <a href="/archive/{{item.Id}}" class="link">
        {% cycle item.Title item.Id as cycleitem %}
        <h5 class="title">Title,Id 逐个出现：{{ cycleitem }}</h5>
    </a>
</li>
{% endfor %}
```

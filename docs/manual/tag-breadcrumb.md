# 面包屑标签

说明：用于获取面包屑导航列表

使用方法：`{% breadcrumb 变量名称 with index="首页" title=true %}` 如将变量定义为 crumbs `{% breadcrumb crumbs with index="首页" title=true %}...{% endbreadcrumb %}`。

### breadcrumb 支持 3 个参数：

- 是否显示标题 `title`  
  `title` 参数可以设置文档详情面包屑是否显示文档标题。如果设置了 `title=false` 则不显示标题，`title=true` 时，则显示完整的文档标题，如果设置了 title 为其他具体值时，按设置的值显示，如`title="文章详情"` 则显示“文章详情”，默认值为`title=true`。
- 首页名称 `index`  
  `index` 参数可以设置首页显示名称，默认值为 首页，如需改成其他可以设置，如 `index="我的博客"`。
- 站点 ID `siteId`  
  `siteId` 一般不需要填写，如果你使用后台的多站点管理创建了多个站点，并且想调用其他站点的数据，则可以通过指定 `siteId` 来实现调用指定站点的数据。

crumbs 是一个数组对象，因此需要使用 `for` 循环来输出

### item 为 for 循环体内的变量，可用的字段有：

- 链接名称 `Name`
- 链接地址 `Link`

### 代码示例

```twig
{# 默认用法 #}
<div>
    {% breadcrumb crumbs %}
    <ul>
        {% for item in crumbs %}
            <li><a href="{{item.Link}}">{{item.Name}}</a></li>
        {% endfor %}
    </ul>
    {% endbreadcrumb %}
</div>

{# 自定义index，不显示标题 #}
<div>
    {% breadcrumb crumbs with index="我的博客" title=false %}
    <ul>
        {% for item in crumbs %}
            <li><a href="{{item.Link}}">{{item.Name}}</a></li>
        {% endfor %}
    </ul>
    {% endbreadcrumb %}
</div>
```

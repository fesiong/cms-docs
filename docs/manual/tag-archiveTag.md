# 文档 Tag 列表标签

说明：当我们跟文档打上各种 tag 后，我们就可以用文档 Tag 列表标签来调用这些 Tag。

使用方法：`{% tagList 变量名 with limit="10" %}` 如将变量定义为 tags `{% tagList tags with limit="10" %}...{% endtagList %}`

### tagList 支持的参数有：

- 文档 ID `itemId`
  `itemId` 如果没有指定，默认读取当前文档的 ID，也可以手工指定，读取指定的文档的 Tag 列表。如果想展示所有的 Tag，而不自动读取当前文档 ID 的 Tag，则设置 `itemId="0"`
- 调用数量 `limit`
  如果不指定，默认最多显示 10 个，可以设置的范围是 1~100，`limit` 在不是分页列表的时候，支持`offset`模式，也就是 `,`分隔模式，如想从第 2 条开始，获取 10 条数据，可以设置成 `limit="2,10"`。
- 索引字母 `letter`
  可以填写的值范围为 A-Z
- Tag 分类 ID `categoryId`
  如果需要显示指定分类的 Tag，则可以通过 `categoryId="分类ID"` 来指定。如果需要指定多个分类 ID，可以用英文`,`隔开。如 `categoryId="1,2,3"`。
- 站点 ID `siteId`
  `siteId` 一般不需要填写，如果你使用后台的多站点管理创建了多个站点，并且想调用其他站点的数据，则可以通过指定 `siteId` 来实现调用指定站点的数据。

tags 是一个数组对象，因此需要使用 `for` 循环来输出

### item 为 for 循环体内的变量，可用的字段有：

- TagID `Id`
- Tag 标题 `Title`
- Tag 链接 `Link`
- Tag 描述 `Description`
- Tag 索引字母 `FirstLetter`
- Tag 的分类 ID `CategoryId`

### 代码示例

```twig
<div>
    文档Tag：
    {% tagList tags with limit="10" %}
    {% for item in tags %}
    <a href="{{item.Link}}">{{item.Title}}</a>
    {% endfor %}
    {% endtagList %}
</div>
```

### 文档 Tag 列表分页显示

文档 Tag 列表支持分页，但仅在模板 `tag/index.html` 内生效。

```twig
<div>
    {% tagList tags with type="page" limit="20" %}
    <ul>
    {% for item in tags %}
    <li>
        <a href="{{item.Link}}">
            <h5>{{item.Title}}</h5>
            <div>{{item.Description}}</div>
        </a>
    </li>
    {% empty %}
    <liå>
        该列表没有任何内容
    </li>
    {% endfor %}
    </ul>
    {% endtagList %}
</div>

{# 分页代码 #}
  <div>
    {% pagination pages with show="5" %}
        {# 首页 #}
        <a class="{% if pages.FirstPage.IsCurrent %}active{% endif %}" href="{{pages.FirstPage.Link}}">{{pages.FirstPage.Name}}</a>
        {# 上一页 #}
        {% if pages.PrevPage %}
        <a href="{{pages.PrevPage.Link}}">{{pages.PrevPage.Name}}</a>
        {% endif %}
        {# 中间多页 #}
        {% for item in pages.Pages %}
        <a class="{% if item.IsCurrent %}active{% endif %}" href="{{item.Link}}">{{item.Name}}</a>
        {% endfor %}
        {# 下一页 #}
        {% if pages.NextPage %}
        <a href="{{pages.NextPage.Link}}">{{pages.NextPage.Name}}</a>
        {% endif %}
        {# 尾页 #}
        <a class="{% if pages.LastPage.IsCurrent %}active{% endif %}" href="{{pages.LastPage.Link}}">{{pages.LastPage.Name}}</a>
    {% endpagination %}
  </div>
</div>
```

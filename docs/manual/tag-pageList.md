# 单页列表标签

说明：用于获取单页列表

使用方法：`{% pageList 变量名称 %}` 如将变量定义为 pages `{% pageList pages %}...{% endpageList %}`

### pageList 支持的参数

- 站点 ID `siteId`  
  `siteId` 一般不需要填写，如果你使用后台的多站点管理创建了多个站点，并且想调用其他站点的数据，则可以通过指定 `siteId` 来实现调用指定站点的数据。

pageList 该标签会获取所有的页面。如果需要排除某些页面，可以在后续的 for 循环中，剔除不需要的页面。

pages 是一个数组对象，因此需要使用 `for` 循环来输出

### item 为 for 循环体内的变量，可用的字段有：

- 单页 ID `Id`
- 单页标题 `Title`
- 单页链接 `Link`
- 单页描述 `Description`
- 单页内容 `Content`
- 单页缩略图大图 `Logo`
- 单页缩略图 `Thumb`

### 代码示例

```twig
<ul>
{% pageList pages %}
    {% for item in pages %}
    <li>
        {#  如需判断当前是否是循环中的第一条，可以这么写： #}
        {% if forloop.Counter == 1 %}这是第一条{% endif %}
        {# 比如需要给第一条添加额外class="active"，可以这么写： #}
        <a class="{% if forloop.Counter == 1 %}active{% endif %}" href="{{item.Link}}">{{item.Title}}</a>

        <a href="{{ item.Link }}">{{item.Title}}</a>
        <a href="{{ item.Link }}">
            <span>当前第{{ forloop.Counter }}篇，剩余{{ forloop.Revcounter}}篇</span>
            <span>单页ID：{{item.Id}}</span>
            <span>单页名称：{{item.Title}}</span>
            <span>单页链接：{{item.Link}}</span>
            <span>单页描述：{{item.Description}}</span>
            <span>单页内容：{{item.Content|safe}}</span>
        </a>
        <div>缩略图大图：<img src="{{item.Logo}}" alt="{{item.Title}}" /></div>
        <div>缩略图：<img src="{{item.Thumb}}" alt="{{item.Title}}" /></div>
    </li>
    {% endfor %}
{% endpageList %}
</ul>
{# 排除id为1的页面 #}
{% pageList pages %}
    {% for item in pages %}
    {% if item.Id != 1 %}
    <li>
        <a href="{{ item.Link }}">{{item.Title}}</a>
        <a href="{{ item.Link }}">
            <span>单页ID：{{item.Id}}</span>
            <span>单页名称：{{item.Title}}</span>
            <span>单页链接：{{item.Link}}</span>
            <span>单页描述：{{item.Description}}</span>
            <span>单页内容：{{item.Content|safe}}</span>
        </a>
        <div>缩略图大图：<img src="{{item.Logo}}" alt="{{item.Title}}" /></div>
        <div>缩略图：<img src="{{item.Thumb}}" alt="{{item.Title}}" /></div>
    </li>
    {% endif %}
    {% endfor %}
</ul>
{% endpageList %}
```

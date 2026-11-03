# 城市分站列表标签

说明：用于获取城市分站列表

使用方法：`{% placeList 变量名称 with parentId="0" all="false" %}{% for item in 变量名称 %}...{% endfor %}{% endplaceList %}` 如将变量定义为 places `{% placeList places with parentId="0" %}...{% endplaceList %}`

### placeList 支持的参数有：

- 上级分站 `parentId`  
  `parentId` 表示上级分站，可以获取指定上级分站下的子分站，`parentId="parent"` 表示上级分站为当前分站的上级分站，用于获取当前分站的兄弟分站。`parentId="0"` 时获取顶级分站。未指定时默认获取当前分站的子分站。
- 获取全部分站 `all`  
  `all` 可以获取指定所有分站列表，如 `all=true` 获取全部分站（包括所有层级），默认为 `false` 仅获取直接子分站。
- 显示数量 `limit`  
  `limit` 可以指定显示数量，比如 `limit="10"` 则只会显示 10 条。`limit` 支持 `offset` 模式，即 `,` 分隔模式，如想从第 2 条开始，获取 10 条数据，可以设置成 `limit="2,10"`。
- 列表类型 `listType`  
  `listType` 支持 `list`（普通列表，默认）和 `page`（分页列表）两种模式。当设置为 `page` 时，会启用分页功能，自动从 URL 参数中获取当前页码，并在上下文设置 `pagination` 分页数据。
- 站点 ID `siteId`  
  `siteId` 一般不需要填写，如果你使用后台的多站点管理创建了多个站点，并且想调用其他站点的数据，则可以通过指定 `siteId` 来实现调用指定站点的数据。

如果想获取当前分站的子分站，则不需要指定 `parentId`。如果想获取当前分站的兄弟分站，则指定 `parentId="parent"`，仅当在城市分站详情页面时有效。

places 是一个数组对象，因此需要使用 `for` 循环来输出。

### item 为 for 循环体内的变量，可用的字段有：

- 分站 ID `Id`
- 分站标题 `Title`
- 分站 SEO 标题 `SeoTitle`
- 分站关键词 `Keywords`
- 分站描述 `Description`
- 分站链接 `Link`
- 分站缩略图大图 `Logo`
- 分站缩略图 `Thumb`
- 分站 Banner 组图 `Images`
- 上级分站 ID `ParentId`
- 分站排序值 `Sort`
- 创建时间 `CreatedTime`
- 更新时间 `UpdatedTime`
- 纬度 `Latitude`
- 经度 `Longitude`
- 时区 `Timezone`
- 是否有下级分站 `HasChildren`
- 是否当前分站 `IsCurrent`
- 是否展开下级 `Spacer`

### 代码示例

```twig
{% placeList places with parentId="0" %}
<ul>
    {% for item in places %}
    <li>
        {# 如需判断当前是否是循环中的第一条，可以这么写： #}
        {% if forloop.Counter == 1 %}这是第一条{% endif %}
        {# 比如需要给第一条添加额外class="active"，可以这么写： #}
        <a class="{% if forloop.Counter == 1 %}active{% endif %}" href="{{item.Link}}">{{item.Title}}</a>

        <a href="{{ item.Link }}">
            <span>当前第{{ forloop.Counter }}个，剩余{{ forloop.Revcounter}}个</span>
            <span>分站ID：{{item.Id}}</span>
            <span>分站名称：{{item.Title}}</span>
            <span>分站链接：{{item.Link}}</span>
            <span>分站描述：{{item.Description}}</span>
            <span>上级分站ID：{{item.ParentId}}</span>
            <span>是否有下级分站：{{item.HasChildren}}</span>
        </a>
        <div>缩略图大图：<img style="width: 200px" src="{{item.Logo}}" alt="{{item.Title}}" /></div>
        <div>缩略图：<img style="width: 200px" src="{{item.Thumb}}" alt="{{item.Title}}" /></div>
        <div>经纬度：{{item.Latitude}}, {{item.Longitude}}</div>
    </li>
    {% endfor %}
</ul>
{% endplaceList %}
```

### 多级分站嵌套调用

```twig
{% placeList places with parentId="0" %}
{# 一级分站 #}
<ul>
    {% for item in places %}
    <li>
        <a href="{{ item.Link }}">{{item.Title}}</a>
        <div>
            {% placeList subPlaces with parentId=item.Id %}
            {# 二级分站 #}
            <ul>
                {% for inner1 in subPlaces %}
                <li>
                    <a href="{{ inner1.Link }}">{{inner1.Title}}</a>
                    <div>
                        {% placeList subPlaces2 with parentId=inner1.Id %}
                        {# 三级分站 #}
                        <ul>
                            {% for inner2 in subPlaces2 %}
                            <li>
                                <a href="{{ inner2.Link }}">{{inner2.Title}}</a>
                            </li>
                            {% endfor %}
                        </ul>
                        {% endplaceList %}
                    </div>
                </li>
                {% endfor %}
            </ul>
            {% endplaceList %}
        </div>
    </li>
    {% endfor %}
</ul>
{% endplaceList %}
```

### 分页列表使用

设置 `listType="page"` 启用分页模式，结合 `pagination` 标签使用：

```twig
{% placeList places with parentId="0" listType="page" limit="10" %}
<ul>
    {% for item in places %}
    <li>
        <a href="{{ item.Link }}">{{item.Title}}</a>
    </li>
    {% empty %}
    <li>该列表没有任何内容</li>
    {% endfor %}
</ul>
{% endplaceList %}

{# 分页导航 #}
{% pagination with pagination %}
```

### 常见使用实例

1. 获取当前分站的子分站（在城市分站详情页使用）：

```twig
{% placeList subPlaces with %}
<ul>
    {% for item in subPlaces %}
    <li><a href="{{ item.Link }}">{{item.Title}}</a></li>
    {% endfor %}
</ul>
{% endplaceList %}
```

2. 获取当前分站的兄弟分站（在城市分站详情页使用）：

```twig
{% placeList siblingPlaces with parentId="parent" %}
<ul>
    {% for item in siblingPlaces %}
    <li><a href="{{ item.Link }}">{{item.Title}}</a></li>
    {% endfor %}
</ul>
{% endplaceList %}
```

3. 获取全部分站列表（不限层级）：

```twig
{% placeList allPlaces with all="true" %}
<ul>
    {% for item in allPlaces %}
    <li>
        <a href="{{ item.Link }}">{{item.Title}}</a>
    </li>
    {% endfor %}
</ul>
{% endplaceList %}
```

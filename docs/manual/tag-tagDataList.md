# Tag 文档列表标签

说明：用于获取指定 Tag 的文档列表

使用方法：`{% tagDataList 变量名称 with tagId="1" %}` 如将变量定义为 archives `{% tagDataList archives with tagId="1" %}...{% endtagDataList %}`

### tagDataList 支持的参数有：

- TagID `tagId`  
  `tagId` 可以获取指定 Tag 的文档列表如 `tagId="1"` 获取 TagID 为 1 的文档列表。
  > 如果未指定 `tagId` 它会尝试读取当前 Tag 页面的 TagID。

- 模型 ID `moduleId`  
  `moduleId` 可以获取指定文档模型的文档列表如 `moduleId="1"` 获取文章模型的文档列表。
- 排序方式 `order`  
  `order` 可以指定文档显示的排序规则，支持依据 最新文档排序 `order="id desc"`、浏览量最多文档排序 `order="views desc"`、按后台自定义排序 `order="sort desc"`，默认按照自定义排序，可以不用填。
- 显示数量 `limit`  
  `limit` 可以指定显示数量，按多少数量来分页，比如`limit="10"`则只会显示 10 条。，`limit` 在不是分页列表的时候，支持`offset`模式，也就是 `,`分隔模式，如想从第 2 条开始，获取 10 条数据，可以设置成 `limit="2,10"`。
- 列表类型 `type`  
  `type` 支持按 page、list 方式列出。默认值为 list，`type="list"` 时，只会显示 指定的 limit 指定的数量，如果`type="page"` 后续可用 `pagination` 来组织分页显示 `{% pagination pages with show="5" %}`。
- 分页标签 `pagination`  
  `pagination` 来组织分页显示 `{% pagination pages with show="5" %}`。
- 站点 ID `siteId`  
  `siteId` 一般不需要填写，如果你使用后台的多站点管理创建了多个站点，并且想调用其他站点的数据，则可以通过指定 `siteId` 来实现调用指定站点的数据。

archives 是一个数组对象，因此需要使用 `for` 循环来输出

### item 为 for 循环体内的变量，可用的字段有：

- 文档 ID `Id`
- 文档标题 `Title`
- 文档 SEO 标题 `SeoTitle`
- 文档链接 `Link`
- 文档关键词 `Keywords`
- 文档描述 `Description`
- 文档模型 ID `ModuleId`
- 文档分类 ID `CategoryId`
- 文档规范链接 `CanonicalUrl`
- 文档的用户 ID `UserId`
- 价格 `Price`
- 库存 `Stock`
- 文档阅读等级 `ReadLevel`
- 文档的原文链接 `OriginUrl`
- 文档浏览量 `Views`
- 文档封面图片 `Images`
- 文档封面首图 `Logo`
- 文档封面缩略图 `Thumb`
- 文档评论数量 `CommentCount`
- 文档添加时间 `CreatedTime` 时间戳，需要使用格式化时间戳为日期格式 `{{stampToDate(item.CreatedTime, "2006-01-02")}}`
- 文档更新时间 `UpdatedTime` 时间戳，需要使用格式化时间戳为日期格式 `{{stampToDate(item.UpdatedTime, "2006-01-02 15:04:05")}}`
- 文档标签
- 文档额外字段参数

### 代码示例

```twig
{# page 分页列表展示 #}
<div>
{% tagDataList archives with type="page" limit="10" %}
    {% for item in archives %}
    <li>
        <a href="{{item.Link}}">
            <h5>{{item.Title}}</h5>
            <div>{{item.Description}}</div>
            <div>
                <span>{% categoryDetail with name="Title" id=item.CategoryId %}</span>
                <span>{{stampToDate(item.CreatedTime, "2006-01-02")}}</span>
                <span>{{item.Views}} 阅读</span>
            </div>
        </a>
        {% if item.Thumb %}
        <a href="{{item.Link}}">
            <img alt="{{item.Title}}" src="{{item.Thumb}}">
        </a>
        {% endif %}
    </li>
    {% empty %}
    <li>
        该列表没有任何内容
    </li>
    {% endfor %}
{% endtagDataList %}

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

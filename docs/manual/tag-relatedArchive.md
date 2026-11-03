# 相关文档标签

说明：获取当前文档的相关文档。相关文档的逻辑是：根据当前文档的文档 id，获取同分类的临近文档。因此该标签只能在文档详情页使用。

使用方法：`{% archiveList 变量名称 with type="related" limit="10" %}` 如将变量定义为 archives `{% archiveList archives with type="related" limit="10" %}...{% endarchiveList %}`

`type` 的值为 related 的情况下，不支持 order 参数。

`type` 的值为 related 的情况下，支持 like 参数。 like="keywords|relation"，默认不需要 like 参数，它自动获取最靠近当前文档的其他文档。如果指定了 like="keywords"，则会根据文档第一个关键词来获取相关的文档。如果指定了 like="relation"，则只会展示后台文档编辑界面设置的相关文档。

archives 是一个数组对象，因此需要使用 `for` 循环来输出

### item 为 for 循环体内的变量，可用的字段有：

- 文档 ID `Id`
- 文档标题 `Title`
- 文档链接 `Link`
- 文档关键词 `Keywords`
- 文档描述 `Description`
- 文档分类 ID `CategoryId`
- 文档浏览量 `Views`
- 文档封面图片 `Images`
- 文档封面首图 `Logo`
- 文档封面缩略图 `Thumb`
- 文档评论数量 `CommentCount`
- 文档添加时间 `CreatedTime` 时间戳，需要使用格式化时间戳为日期格式 `{{stampToDate(item.CreatedTime, "2006-01-02")}}`
- 文档更新时间 `UpdatedTime` 时间戳，需要使用格式化时间戳为日期格式 `{{stampToDate(item.UpdatedTime, "2006-01-02 15:04:05")}}`
- 文档标签
- 文档模型设置的其他字段参数

### 代码示例

获取相关文档标签，只能在文档详情页使用。

```twig
{# related 相关文档列表展示 #}
<div>
{% archiveList archives with type="related" limit="10" %}
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
{% endarchiveList %}
</div>
```

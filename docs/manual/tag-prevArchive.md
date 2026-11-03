# 上一篇文档标签

说明：用于获取上一篇文档数据

使用方法：`{% prevArchive 变量名称 %}` 如将变量定义为 prev `{% prevArchive prev %}...{% endprevArchive %}`

prevArchive 不支持参数。

### prevArchive 支持的字段有：

- 文档 ID `Id`
- 文档标题 `Title`
- 文档链接 `Link`
- 文档关键词 `Keywords`
- 文档描述 `Description`
- 文档分类 ID `CategoryId`
- 文档浏览量 `Views`
- 文档封面首图 `Logo`
- 文档封面缩略图 `Thumb`
- 文档评论数量 `CommentCount`
- 文档添加时间 `CreatedTime`
- 文档更新时间 `UpdatedTime`

### 代码示例

```twig
{% prevArchive prev %}
上一篇：
{% if prev %}
  <a href="{{prev.Link}}">{{prev.Title}}</a>
{% else %}
  没有了
{% endif %}
{% endprevArchive %}
```

显示图片

```twig
{% prevArchive prev %}
上一篇：
{% if prev %}
  <a href="{{prev.Link}}">
    <img src="{{prev.Thumb}}" />
    <span>{{prev.Title}}</span>
  </a>
{% else %}
  没有了
{% endif %}
{% endprevArchive %}
```

# 分页标签

说明：用于获取文章列表、产品列表的分页信息

使用方法：`{% pagination 变量名称 with show="5" %}` 如将变量定义为 pages `{% pagination pages with show="5" %}...{% endpagination %}`

### pagination 支持 一个参数:

- 显示页码数量 `show`  
  可以设置如果指定数量页码的时候，最多显示多少页码。如 `show="5"` 可以最多显示 5 页。
- 重定义 pattern `prefix`  
  高级功能，一般不需要设置。如确有需要，需要包含`{page}`，可以设置如：`prefix="?page={page}"`

### pagination 可用的字段有：

- 总条数 `TotalItems`
- 总页码数 `TotalPages`
- 当前页码 `CurrentPage`
- 首页对象 `FirstPage`
- 末页对象 `LastPage`
- 上一页对象 `PrevPage`
- 下一页对象 `NextPage`
- 中间页码数组 `Pages`

Pages 是一个数组对象，因此需要使用 `for` 循环来输出

其中 Pages 内的 pageItem 可用的字段有：

- 页码名称 `Name`
- 页码链接 `Link`
- 是否当前页 `IsCurrent`

```twig
<div class="pagination">
    {% pagination pages with show="5" %}
    <ul>
        <li>总数：{{pages.TotalItems}}条，总共：{{pages.TotalPages}}页，当前第{{pages.CurrentPage}}页</li>
        <li class="page-item {% if pages.FirstPage.IsCurrent %}active{% endif %}"><a href="{{pages.FirstPage.Link}}">{{pages.FirstPage.Name}}</a></li>
        {% if pages.PrevPage %}
            <li class="page-item"><a href="{{pages.PrevPage.Link}}">{{pages.PrevPage.Name}}</a></li>
        {% endif %}
        {% for item in pages.Pages %}
            <li class="page-item {% if item.IsCurrent %}active{% endif %}"><a href="{{item.Link}}">{{item.Name}}</a></li>
        {% endfor %}
        {% if pages.NextPage %}
            <li class="page-item"><a href="{{pages.NextPage.Link}}">{{pages.NextPage.Name}}</a></li>
        {% endif %}
        <li class="page-item {% if pages.LastPage.IsCurrent %}active{% endif %}"><a href="{{pages.LastPage.Link}}">{{pages.LastPage.Name}}</a></li>
    </ul>
    {% endpagination %}
</div>
```

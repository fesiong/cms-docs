# 模板的标签和使用方法

模板文件的使用类似 Django 模板引擎的标签标记，变量则使用双花括号来定义，如 `{{变量}}`。条件判断、循环控制等标签，使用单花括号和百分号来定义，并且需要用结束标签来结束，标签成对出现，如 `{% if archive.Id == 10 %}这是文档ID为10的文档{% endif %}`。

系统内置的常用标签有 38 种：

- 系统设置标签 `system`
> 使用方法：`{% system 变量名称 with name="字段名称" %}`
- 联系方式标签 `contact`
> 使用方法：`{% contact 变量名称 with name="字段名称" %}`
- 万能TDK标签 `tdk`
> 使用方法：`{% tdk 变量名称 with name="字段名称" %}`
- 导航列表标签 `navList`
> 使用方法： `{% navList navs %}...{% endnavList %}`
- 面包屑导航标签 `breadcrumb`
> 使用方法：`{% breadcrumb crumbs with index="首页" title=true %}...{% endbreadcrumb %}`
- 分类列表标签 `categoryList`
> 使用方法：`{% categoryList categories with parentId="0" %}...{% endcategoryList %}`
- 分类详情标签 `categoryDetail`
> 使用方法：`{% categoryDetail with name="字段名称" %}`
- 单页面列表标签 `pageList`
> 使用方法：`{% pageList pages %}...{% endpageList %}`
- 单页面详情标签 `pageDetail`
> 使用方法：`{% pageDetail with name="字段名称" %}`
- 文档列表标签 `archiveList`
> 使用方法：`{% archiveList 变量名称 with categoryId="1" moduleId=1 order="id desc|views desc" type="page|list" %}...{% endarchiveList %}`
- 文档详情标签 `archiveDetail`
> 使用方法：`{% archiveDetail with name="字段名称" %}`
- 上一篇文档标签 `prevArchive`
> 使用方法：`{% prevArchive prev %}...{% endprevArchive %}`
- 下一篇文档标签 `nextArchive`
> 使用方法：`{% nextArchive next %}...{% endnextArchive %}`
- 相关文档标签 `archiveList`
> 使用方法参看文档列表标签：`{% archiveList archiveRelations with type="related" %}...{% endarchiveList %}`
- 文档参数标签 `archiveParams`
> `{% archiveParams params with sorted=true %}...{% endarchiveParams %}`
- 文档参数筛选标签 `archiveFilters`
> 使用方法：`{% archiveFilters params with moduleId=1 allText="全部" %}...{% endarchiveFilters %}`
- 文档Tag列表标签 `tagList`
> 使用方法：`{% tagList tags with limit="10" %}...{% endtagList %}`
- Tag详情标签 `tagDetail`
> 使用方法：`{% tagDetail with name="字段名称" %}`
- Tag文档列表标签 `tagDataList`
> 使用方法：`{% tagDataList archives with tagId="1" %}...{% endtagDataList %}`
- 评论列表标签 `commentList`
> 使用方法：`{% commentList comments with itemType="archive" itemId="1" type="page" %}...{% endcommentList %}`
- 留言表单标签 `guestbook`
> 使用方法：`{% guestbook fields %}...{% endguestbook %}`
- 友情链接标签 `linkList`
> 使用方法：`{% linkList friendLinks %}...{% endlinkList %}`
- 分页标签 `pagination`
> 使用方法：`{% pagination pages with show="5" %}...{% endpagination %}`
- if逻辑判断标签 `if else endif`
> 使用方法：`{% if 条件 %}  ...  {% elif 其他条件 %} ... {% else %} ... {% endif %}` 
- for循环遍历标签 `for empty endfor`
> 使用方法：`{% for item in archives %}...{% empty %}...{% endfor %}`
- 格式化时间戳标签 `stampToDate`
> 使用方法：`{{stampToDate(时间戳, "格式")}}`。时间戳为10位的时间，如 `1609470335`，格式为Golang支持的格式。
- 定义变量赋值标签 `with`
> 使用方法：`{% with title="这是声明给header使用的title" keywords="这是声明给header使用的keywords" %} %}标题：{{title}}，关键词：{{keywords}}`
- 其他辅助标签 `tags`
> 使用方法：`include`、`extends`、`macro`、`lorem`
- 更多过滤器 `filters`
> 使用方法：`{{obj|filter__name:param}}`

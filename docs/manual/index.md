# AI内容管理系统(AICMS) 使用帮助文档
注意：标签中，严格区分大小写，如果大小写拼写不正确，结果也会不对的。

[模板手册使用指南](1-guide.md)

## 文档标签
- [文档列表标签](tag-archiveList.md)
- [文档详情标签](tag-archiveDetail.md)
- [上一篇文档标签](tag-prevArchive.md)
- [下一篇文档标签](tag-nextArchive.md)
- [相关文档标签](tag-relatedArchive.md)
- [文档参数标签](tag-archiveParams.md)
- [文档参数筛选标签](tag-archiveFilters.md)
- [文档模型详情标签](tag-moduleDetail.md)

## 分类页面标签
- [分类列表标签](tag-categoryList.md)
- [分类详情标签](tag-categoryDetail.md)
- [单页面列表标签](tag-pageList.md)
- [单页面详情标签](tag-pageDetail.md)

## 文档Tag标签
- [文档Tag列表标签](tag-archiveTag.md)
- [Tag详情标签](tag-tagDetail.md)
- [Tag文档列表标签](tag-tagDataList.md)

## 城市分站标签
- [城市分站详情标签](tag-placeDetail.md)
- [城市分站列表标签](tag-placeList.md)

## 商城标签
- [获取产品SKU标签](tag-archiveSku.md)
- [格式化价格标签](tag-priceFormat.md)
- [产品评价列表标签](tag-reviewList.md)

## 留言与评论标签
- [评论列表标签](tag-commentList.md)
- [留言表单标签](tag-guestbook.md)
- [留言验证码使用标签](tag-captcha.md)


## 常用标签
- [系统设置标签](tag-system.md)
- [联系方式标签](tag-contact.md)
- [万能TDK标签](tag-tdk.md)
- [导航列表标签](tag-navList.md)
- [面包屑导航标签](tag-breadcrumb.md)
- [分页标签](tag-pagination.md)
- [友情链接标签](tag-linkList.md)
- [首页 Banner 列表标签](tag-bannerList.md)
- [获取多语言站点列表标签](tag-languages.md)
- [Json-LD 自定义调用标签](tag-jsonLd.md)
- [统计代码标签](tag-tongji.md)
- [翻译标签](tag-tr.md)
- [用户详情标签](tag-userDetail.md)
- [用户分组详情标签](tag-userGroupDetail.md)

## 其它标签
- [if逻辑判断标签](tag-if.md)
- [for循环遍历标签](tag-for.md)
- [算术运算标签](tag-calc.md)
- [格式化时间戳标签](tag-stampToDate.md)
- [定义变量赋值标签](tag-with.md)
- [其他辅助标签](tag-tags.md)
- [更多过滤器](tag-filters.md)
- [移除逻辑标签占用行](tag-remove.md)
- [模板自定义内容标签](tag-diy.md)
- [生成随机文本](tag-lorem.md)

## 模板过滤器

> 以下 42 个过滤器按功能分为 5 组，便于按需查找。

### 数值与随机
- [数字或字符串相加](filter-add.md)
- [判断一个数字是否可以作为被除数](filter-divisibleby.md)
- [浮点数保留指定位数小数点](filter-floatformat.md)
- [获取数字中指定位置的数字](filter-get_digit.md)
- [转换数字字符串为浮点数或整数](filter-integer.md)
- [将手机数字键盘字母转换为数字](filter-phone2numeric.md)
- [返回字符串、数组中的随机一个字符、值](filter-random.md)

### 字符串处理
- [预定义字符前添加反斜杠](filter-addslashes.md)
- [将英文字符串字母转换为大写或小写](filter-capfirst.md)
- [将字符串按指定长度格式居中、靠左、靠右显示](filter-center.md)
- [移除字符串任意位置中的指定字符](filter-cut.md)
- [将字符串、js 代码中的特殊字符转义](filter-escape.md)
- [单词的复数形式](filter-pluralize.md)
- [指定重复多次输出字符串](filter-repeat.md)
- [替换字符串中某个特定关键词为另一个关键词](filter-replace.md)
- [截取符串、数组中指定位置的元素](filter-slice.md)
- [将任意值格式化成字符串输出](filter-stringformat.md)
- [删除字符串所有前导和尾随空格、特定字符](filter-trim.md)
- [对字符串或 html 代码进行截取并添加...](filter-truncatechars.md)
- [url 参数转义](filter-urlencode.md)
- [计算字符串中单词数量](filter-wordcount.md)
- [长文本自动换行](filter-wordwrap.md)

### 数组与列表
- [判断文字、数组是否包含指定关键词](filter-contain.md)
- [计算某个关键词在一行字符串中出现的次数、数组中出现次数](filter-count.md)
- [将一行文字按空格拆分成数组](filter-fields.md)
- [字符串或数组第一个值或最后一个值](filter-first.md)
- [获取某个关键词在一行字符串或数组中出现的位置](filter-index.md)
- [将数组按指定拼接字符链接成字符串](filter-join.md)
- [获取字符串、数组、键值对的长度](filter-length.md)
- [在模板中定义数组](filter-list.md)
- [字符串按指定分隔符切割成数组](filter-split.md)

### 日期、内容与媒体渲染
- [将时间值按指定格式显示](filter-date.md)
- [将多行文本按换行符转换成 html 标签](filter-linebreaks.md)
- [移除 html 代码中的 html 标签](filter-removetags.md)
- [渲染Markdown内容为HTML](filter-render.md)
- [将 HTML 代码解析输出，不转义](filter-safe.md)
- [查找并将文本中的 url 字符串解析成可点击的 a 标签](filter-urlize.md)
- [获取图片的缩略图](filter-thumb.md)

### 逻辑判断与调试
- [数字或字符串、对象默认值设置](filter-default.md)
- [打印变量的结构类型和值](filter-dump.md)
- [将变量转换成JSON输出](filter-json.md)
- [或与非三种状态](filter-yesno.md)

# Json-LD 自定义调用标签

Json-LD 是一种用于描述网页内容的数据格式，它使用 JSON 来表示数据，并使用特定的语法来描述网页内容。

后台功能开启了结构化数据功能后，默认会在页面中插入一个名为 `json-ld` 的标签，该标签的内容为结构化数据。

如果你想更自由的控制 Json-LD 的内容，可以使用标签 `{% jsonLd %} ... {% endjsonLd %}`。

你只需要在包裹的内容中`{...}`里写上你需要自定义的字段即可，AICMS 会自动合并处理它们的数据，如果你定义的字段和默认的字段有冲突，则默认的字段会被覆盖。请注意，你定义的字段，一定要符合 JSON-LD 的语法。

比如下方我们自定义 author 字段，补充 images 字段：

```twig
{% jsonLd %}
<script type="application/ld+json">
{
	"author": "AICMS",
	"image": [
		"https://www.aicms.com/AICMS.png"
	]
}
</script>
{% endjsonLd %}
```

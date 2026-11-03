# 模板制作的目录和模板

AICMS 模板的根目录为 `/template`，每一套模板，都需要在 `/template` 下创建自己的模板目录，并在模板目录中添加 `config.json` 配置文件，来说明模板的一些信息。

`config.json` 文件的内容格式为：

```json
{
	"name": "默认模板",
	"package": "default",
	"version": "1.0",
	"description": "系统默认模板",
	"author": "kandaoni.com",
	"homepage": "https://www.kandaoni.com",
	"created": "2022-05-10 22:29:00",
	"template_type": 0,
	"status": 0,
}
```

`config.json` 的字段都是选填的，如果都不填，系统将会根据实际情况生成，其中的字段说明：

- `name` 模板名称，按照实际情况来取名
- `package` 模板文件夹，仅支持英文字母和数字，请填写你的模板文件夹名称。
- `version` 模板的版本，自定义
- `description` 模板的介绍
- `author` 模板作者
- `homepage` 模板作者的网站
- `created` 模板创建时间，格式为：`2022-05-10 22:29:00`
- `template_type` 模板类型，可选值为：0 自适应；1 代码适配；2 电脑+手机
- `status` 模板使用状态，可选值为：0 未启用，1 使用中。所有的模板中，只能有一套模板的 `status` 值 为 1

模板目录和文件

### 文件夹组织模式

- 公共代码 `bash.html` 比如页头、页脚等每个页面都继承的部分，则放在这里，供引用。
- 代码片段目录 `partial/` 比如侧边栏、面包屑等代码片段，则存放在这里
- 首页 `index/index.html`
- 模型首页 `{模型table}/index.html`
- 文档详情页 `{模型table}/detail.html` `{模型table}/detail-{文档ID}.html` 
- 文档列表页 `{模型table}/list.html` `{模型table}/list-{文档分类ID}.html`
- 评论列表页 `comment/list.html`
- 在线留言页 `guestbook/index.html`
- 单页面详情页 `page/detail.html` `page/detail-{单页ID}.html`
- 搜索页 `search/index.html`
- 标签首页 `tag/index.html`
- 标签文档列表页 `tag/list.html`
- 404错误页 `errors/404.html`
- 500错误页 `errors/500.html`
- 站点关闭提示页 `errors/close.html`
- 手机端模板目录 `mobile/` 手机端模板目录里的目录结构和模板文件跟上面一致，重复一遍即可。

同时，部分模板还支持自定义名称，如文档详情、分类页、单页面，可以增加其他文件名，来处理不同的分类、页面需要不同的模板的情况。如需要对 `关于我们` 这个单页，采用独立的模板，则可以命名模板为 `page/about.html`，并在后台创建一个 调用自定义模板为 `page/about.html` 的关于我们页面即可。

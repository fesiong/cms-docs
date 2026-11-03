# 首页 Banner 列表标签

说明：用于获取首页 Banner 列表

使用方法：`{% bannerList 变量名称 %}` 如将变量定义为 banners `{% bannerList banners %}...{% endbannerList %}`

### bannerList 支持的参数有：

- 站点 ID `siteId`  
  `siteId` 一般不需要填写，如果你使用后台的多站点管理创建了多个站点，并且想调用其他站点的数据，则可以通过指定 `siteId` 来实现调用指定站点的数据。
- 分组名称 `type`  
  `type` 默认值"default"，你可以在后台创建多个 banner 分组，然后通过`type="分组名"`，来调用不同分组的 banner。

banners 是一个数组对象，因此需要使用 `for` 循环来输出

### item 为 for 循环体内的变量，可用的字段有：

- ID `Id`
- Logo 图片地址 `Logo`
- 链接地址 `Link`
- 介绍 `Description`
- 图片 Alt `Alt`

### 代码示例

```twig
{% bannerList banners %}
    {% for item in banners %}
    <a href="{{item.Link}}" target="_blank">
        <img src="{{item.Logo}}" alt="{{item.Alt}}" />
        <h5>{{item.Description}}</h5>
    </a>
    {% endfor %}
{% endbannerList %}
```

调用指定分组，如分组名是”幻灯“

```twig
{% bannerList banners with type="幻灯" %}
    {% for item in banners %}
    <a href="{{item.Link}}" target="_blank">
        <img src="{{item.Logo}}" alt="{{item.Alt}}" />
        <h5>{{item.Description}}</h5>
    </a>
    {% endfor %}
{% endbannerList %}
```

如需判断当前是否是循环中的第一条，可以这么写：
{% if forloop.Counter == 1 %}这是第一条{% endif %}
比如需要给第一条添加额外 class="active"，可以这么写：

```twig
{% bannerList banners %}
    {% for item in banners %}
    <a class="{% if forloop.Counter == 1 %}active{% endif %}"  href="{{item.Link}}" target="_blank">
        <img src="{{item.Logo}}" alt="{{item.Alt}}" />
        <h5>{{item.Description}}</h5>
    </a>
    {% endfor %}
{% endbannerList %}
```

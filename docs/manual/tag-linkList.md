# 友情链接标签

说明：用于获取友情链接列表

使用方法：`{% linkList 变量名称 %}` 如将变量定义为 friendLinks `{% linkList friendLinks %}...{% endlinkList %}`

### linkList 支持的参数有

- 站点 ID `siteId`  
  `siteId` 一般不需要填写，如果你使用后台的多站点管理创建了多个站点，并且想调用其他站点的数据，则可以通过指定 `siteId` 来实现调用指定站点的数据。

linkList 将会获取所有的友情链接。

friendLinks 是一个数组对象，因此需要使用 `for` 循环来输出

### item 为 for 循环体内的变量，可用的字段有：：

- 链接名称 `Title`
- 链接地址 `Link`
- 链接备注 `Remark`
- 链接 nofollow `Nofollow`

### 示例代码

```twig
{% linkList friendLinks %}
{% if friendLinks %}
<div>
    <span>友情链接：</span>
    {% for item in friendLinks %}
    <a href="{{item.Link}}" {% if item.Nofollow == 1 %} rel="nofollow"{% endif %} target="_blank">{{item.Title}}</a>
    {% endfor %}
</div>
{% endif %}
{% endlinkList %}
```

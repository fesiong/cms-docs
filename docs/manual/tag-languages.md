# 获取多语言站点列表标签

说明：用于获取多语言站点的列表

使用方法：`{% languages 变量名称 %}` 如将变量定义为 websites `{% languages websites %}...{% endLanguages %}`

### languages 不支持设置参数

languages 将会获取所有的多语言站点。

websites 是一个数组对象，因此需要使用 `for` 循环来输出

### item 为 for 循环体内的变量，可用的字段有：：

- 站点语言名称 `LanguageName`
- 语言代码 `Language`
- 语言 Emoji `LanguageEmoji`
- 语言 Icon `LanguageIcon`
- 站点名称 `Name`
- 链接地址 `Link`
- 链接地址 `Remark`
- 链接地址 `Nofollow`

### 示例代码

切换语言：

```twig
{%- languages websites %}
{%- if websites %}
<div>
    <span>切换语言：</span>
    {%- for item in websites %}
    <a href="{{item.Link}}">
        {%- if item.LanguageIcon %}
        <img src="{{item.LanguageIcon}}" />
        {%- else %}
        {{item.LanguageEmoji}}
        {% endif %}
        {{item.LanguageName}}
    </a>
    {%- endfor %}
</div>
{%- endif %}
{%- endLanguages %}
```

hreflang：

将 Hreflang 标签放入 HTML 的`<head>`区块 ‌

```twig
{%- languages websites %}
{%- for item in websites %}
<link rel="alternate" href="{{item.Link}}" hreflang="{{item.Language}}">
{%- endfor %}
{%- endLanguages %}
```

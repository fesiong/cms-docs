# 移除逻辑标签占用行

这个需求很多时候会用到，比如在 if-elseif 中 或者是 for 循环中，它会连 if-else 标签部分的行的空行也输出。如果想清理这一行空行，可以在标签里面的前方或后方使用`-`来实现过滤。

### 示例代码

```twig
{%- if false %}
1st choice
{%- elif false %}
2nd choice
{%- elif true %}
3rd choice
{%- endif %}
正常下
{% for item in archives %}
{{ item.Id }}
{% endfor %}
紧凑：
{% for item in archives %}
{{- item.Id }}
{% endfor %}
不带换行
{% for item in archives -%}
{{ item.Id }}
{%- endfor %}
```

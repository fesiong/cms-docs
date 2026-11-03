# if 逻辑判断标签

标签判断表达式的值，如果表达式的值为 true 则执行其主体内容。

使用方法：

- `{% if 条件 %} ... {% endif %}`
- `{% if 条件 %}  ...  {% elif 其他条件 %} ... {% endif %}`
- `{% if 条件 %}  ...  {% elif 其他条件 %} ... {% else %} ... {% endif %}`

### 示例代码

```twig
{# 单个条件 #}
{% if nothing %}false{% else %}true{% endif %}
{% if simple %}simple != nil{% endif %}
{% if simple.uint %}uint != 0{% endif %}
{% if simple.float %}float != 0.0{% endif %}
{% if !simple %}false{% else %}!simple{% endif %}
{% if !simple.uint %}false{% else %}!simple.uint{% endif %}
{% if !simple.float %}false{% else %}!simple.float{% endif %}
{% if "Text" in complex.post %}text field in complex.post{% endif %}
{% if 5 in simple.intmap %}5 in simple.intmap{% endif %}
{% if !0.0 %}!0.0{% endif %}
{% if !0 %}!0{% endif %}
{# 支持not判断 支持else #}
{% if not complex.post %}true{% else %}false{% endif %}
{% if simple.number == 43 %}no{% else %}42{% endif %}
{# 支持多个if else #}
{% if simple.number < 42 %}false{% elif simple.number > 42 %}no{% elif simple.number >= 42 %}yes{% else %}no{% endif %}
{% if simple.number < 42 %}false{% elif simple.number > 42 %}no{% elif simple.number != 42 %}no{% else %}yes{% endif %}
{% if 0 %}!0{% elif nothing %}nothing{% else %}true{% endif %}
{% if 0 %}!0{% elif simple.float %}simple.float{% else %}false{% endif %}
{% if 0 %}!0{% elif !simple.float %}false{% elif "Text" in complex.post%}Elseif with no else{% endif %}
```

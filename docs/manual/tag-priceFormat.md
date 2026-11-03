# 格式化价格标签

由于 AICMS 的价格字段使用的是分作为单位，并不适合直接显示输出到模板中，因此需要将价格转换成元再输出，默认输出比较复杂，需要先转换成 float64，再除以100，然后再格式化成两位小数点输出`{%- set price = item.Price|float/100 %}<span>${{price|floatformat:2}}</span>`，现在支持直接对价格字段进行格式化成指定的格式化输出。标签关键词：`priceFormat`。

使用方法：{{priceFormat(价格, "格式")}}。价格是以分为单位的价格数值，如 `1880`，格式 支持Printf 的格式，如 `{{priceFormat(item.Price, "%.2f")}}`，以及预设值： `int|one|two`、`0|1|2`，默认保留两位小数点。

### 示例代码

```twig
{% set price = 1880 %}

{# 格式化 为 保留两位小数点的价格 #}
<div>{{priceFormat(price)}}</div>
{# 或者 #}
<div>{{priceFormat(price, 2)}}</div>
<div>{{priceFormat(price, "two")}}</div>
<div>{{priceFormat(price, "%.2f")}}</div>


{# 格式化 为 只保留一位小数点价格 #}
<div>{{priceFormat(price, 1)}}</div>
<div>{{priceFormat(price, "one")}}</div>
<div>{{priceFormat(price, "%.1f")}}</div>


{# 格式化 为 只保留整数部分价格 #}
<div>{{priceFormat(price, 0)}}</div>
<div>{{priceFormat(price, "int")}}</div>
<div>{{priceFormat(price, "%.0f")}}</div>

```

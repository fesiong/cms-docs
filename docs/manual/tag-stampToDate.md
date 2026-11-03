# 格式化时间戳标签

模板中，支持直接对时间戳进行格式化成指定的格式化输出。标签关键词：`stampToDate`。

使用方法：{{stampToDate(时间戳, "格式")}}。时间戳为 10 位的时间，如 `1609470335`，格式为 Golang 支持的格式。

### 示例代码

```twig
{% set publishStamp = 1609470335 %}

{# 格式化 为 2021年06月30日 #}
<div>{{stampToDate(publishStamp, "2006年01月02日")}}</div>
{# 格式化 为 2021-06-30 #}
<div>{{stampToDate(publishStamp, "2006-01-02")}}</div>
{# 格式化 为 2021/06/30 #}
<div>{{stampToDate(publishStamp, "2006/01/02")}}</div>
{# 格式化 为 30/06/2021 #}
<div>{{stampToDate(publishStamp, "02/01/2006")}}</div>
{# 格式化 为 2021-06-30 12:30 #}
<div>{{stampToDate(publishStamp, "2006-01-02 15:04")}}</div>
{# 格式化 为 2021-06-30 12:00:00 #}
<div>{{stampToDate(publishStamp, "2006-01-02 15:04:05")}}</div>
{# 格式化 为 2021-06-30 12:00:00 #}
<div>{{stampToDate(publishStamp, "2006-01-02 15:04:05.999999999 -0700 MST")}}</div>

{# 更多格式化结果 #}
<div>{{stampToDate(publishStamp, "Mon Jan _2 15:04:05 2006")}}</div>
<div>{{stampToDate(publishStamp, "Mon Jan _2 15:04:05 MST 2006")}}</div>
<div>{{stampToDate(publishStamp, "Mon Jan 02 15:04:05 -0700 2006")}}</div>
<div>{{stampToDate(publishStamp, "02 Jan 06 15:04 MST")}}</div>
<div>{{stampToDate(publishStamp, "2 Jan 06 15:04 -0700")}}</div>
<div>{{stampToDate(publishStamp, "Monday, 02-Jan-06 15:04:05 MST")}}</div>
<div>{{stampToDate(publishStamp, "Mon, 02 Jan 2006 15:04:05 -0700")}}</div>
<div>{{stampToDate(publishStamp, "2006-01-02T15:04:05Z07:00")}}</div>
<div>{{stampToDate(publishStamp, "2006-01-02T15:04:05.999999999Z07:00")}}</div>
<div>{{stampToDate(publishStamp, "3:04PM")}}</div>
<div>{{stampToDate(publishStamp, "Jan _2 15:04:05")}}</div>
<div>{{stampToDate(publishStamp, "Jan _2 15:04:05.000")}}</div>
```

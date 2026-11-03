# 更多过滤器

输出变量的时候，还支持使用过滤器，来对数据进行初级过滤，格式是：

```twig
{{obj|filter__name:param}}
```

比如一个变量，当它有值的时候，就输出当前值，没有值的时候，就输出默认值：
使用`default`设置默认值：

```twig
{{ userName|default:"大侠匿名"}}
```

default 只要是空都会认为没有。我们还可以使用`default_if_none`来进行处理

```twig
{{ userName|default_if_none:"大侠匿名"}}
{{ ""|default_if_none:"n/a" }}
{{ nil|default_if_none:"n/a" }}
```

`get_digit` 可以获取变量中的数字，指定 get_digit 的值的话，可以获取倒数第几个数字。如：

```twig
{{ 1234567890|get_digit:0 }}
{{ 1234567890|get_digit }}
{{ 1234567890|get_digit:2 }}
{{ 1234567890|get_digit:"4" }}
{{ 1234567890|get_digit:10 }}
{{ 1234567890|get_digit:15 }}
```

使用`length`输出长度：

```twig
{{ value|length }}
```

如果 value 是 ['a', 'b', 'c', 'd']，那么输出是 4。

`divisibleby` 可以判断一个变量是否可以被整除，如：

```twig
{{ 21|divisibleby:3 }}
{{ 21|divisibleby:"3" }}
{{ 21|float|divisibleby:"3" }}
{{ 22|divisibleby:"3" }}
{{ 85|divisibleby:simple.number }}
{{ 84|divisibleby:simple.number }}
```

`date` 可以格式化时间：

```twig
{{ value|date:``"2006-01-02 15:04"}}
```

注意，这个 value 必须是 time.Time 类型，不是时间戳，如果是时间戳它会报错的。时间戳要么在控制器将它转成 time.Time 类型，要么就使用我们自定义的模板函数：

```twig
{{stampToDate(nowStamp, "2006-01-02 15:04")}}
```

`truncatechars`、`truncatewords` 字符串字符、单词多于指定的字符数量，那么会被截断。截断的字符串将以可翻译的省略号序列（“...”）结尾：

```twig
{{ value|truncatechars:9}}
{{ value|truncatewords:9}}
```

截断除了字符串截断`truncatechars`，还支持按单词截断`truncatewords`

`truncatechars_html`、`truncatewords_html` 功能类似`truncatechars`、`truncatewords`。但是这这 2 个标签用来处理截取 html 中的字符串，它不会破坏 html 结构。一个是按字符截取，一个是按单词截取。截断的字符串将以可翻译的省略号序列（“...”）结尾：

```twig
{{ "This is a long test which will be cutted after some chars."|truncatechars_html:25 }}
{{ "This is a long test which will be cutted after some words."|truncatewords_html:5|safe }}
```

`upper`、`lower` 可以对单字进行大小写转换：

```twig
{{ value|upper}}
{{ value|lower}}
```

`capfirst` 可以实现句子首字母大写效果，如：

```twig
{{ "hello there!"|capfirst }}
```

`cut` 可实现删除变量中特定的字符。如：

```twig
{{ 15|cut:"5" }}
{{ "Hello world"|cut: " " }}
```

`add` 可以对要输出的内容进行追加。相当于 golang 中的`+`，数字则会相加后输出结果，字符串则会拼接在一起。如：

```twig
{{ 5|add:6 }}
{{ 5|add:nothing }}
{{ 5|add:"test" }}
{{ "hello "|add:"john doe" }}
```

`addslashes` 则会在指定的预定义字符前添加反斜杠。这些字符是单引号（'）、双引号（"）、反斜线（\）与 NUL（NULL 字符）。如：

```twig
{{ "plain' text"|addslashes }}
{{ "plain' text"|addslashes|safe }}
```

`title` 标签可以实现句子中每一个单词的首字母都变成大写，并将其余部分变成小写，用于格式化标题的输出。如：

```twig
{{ "hello there!"|title }}
{{ "HELLO THERE!"|title }}
{{ "HELLO tHERE!"|title }}
```

`yesno` yesno 用于验证一个变量是否有效，它可以定义三种结果，三种结果分别用英文逗号`,`隔开，有效值、无效值、不知道类型。如果不定义，也可以留空。如：

```twig
{{ archive.Status|yesno}}
{{ archive.Status|yesno:"validated,not validated,unknown validation status"}}
```

`striptags` striptags 类似 PHP 的 strip_tags 函数，可以剥去字符串中的 HTML、XML 以及 PHP 的标签。该标签始终会剥离 HTML 注释。如：

```twig
{{"<title>Hello World</title>"|striptags}}
{{"<title>Hello World</title>"|striptags|safe}}
```

`removetags` 标签可以删除指定的 html 标签。如：

```twig
{{ "<strong><i>Hello!</i></strong>"|removetags:"i"|safe }}
```

`pluralize` 标签可以判断一个变量是否是复数。如：

```twig
customer{{ 0|pluralize }}
customer{{ 1|pluralize }}
customer{{ 2|pluralize }}
cherr{{ 0|pluralize:"y,ies" }}
cherr{{ 1|pluralize:"y,ies" }}
cherr{{ 2|pluralize:"y,ies" }}
walrus{{ 0|pluralize:"es" }}
walrus{{ 1|pluralize:"es" }}
walrus{{ simple.number|pluralize:"es" }}
```

`random` 可以随机输出集合中的一个值。如：

```twig
<p>{{ intList|random }}</p>
```

`first`、`last` 可以用于输出变量中的最开始一个字符和最后一个字符。如：

```twig
{{ "Test"|first }}
{{ "Test"|last }}
```

`urlencode` urlencode 标签可以对变量进行 url 百分号编码。如：

```twig
{{ "https://www.kandaoni.com/?category_id=1"|urlencode }}
```

`linebreaksbr`、`linebreaks` 两个标签都可以将变量的值中的换行符变成`<br/>`，相当于 PHP 的`nl2br`函数。如：

```twig
{{ archive.Description|linebreaksbr }}
{{ archive.Description|linebreaks }}
{{ archive.Description|linebreaksbr|safe }}
{{ archive.Description|linebreaks|safe }}
```

`length_is` length_is 可以判断变量的值的长度。只能判断字符串，数字是不行的。如：

```twig
{{ "hello"|length_is:5 }}
```

`integer`、`float` 标签可以将变量的值转换成整数、浮点数。如：

```twig
{{ "foobar"|integer }}
{{ "5.4"|float|integer }}
{{ "foobar"|float }}
{{ "5.5"|float }}
{{ "5.6"|integer|float }}
```

`floatformat` 标签可以将变量的值按浮点数格式保留指定小数点，默认只保留以为，如果末位是 0，则不保留小数点。如果指定小数点后位数，则按指定位数显示。如：

```twig
{{ 34.23234|floatformat }}
{{ 34.00000|floatformat }}
{{ 34.23234|floatformat:3 }}
{{ 34.00000|floatformat:3 }}
{{ "34.23234"|floatformat }}
{{ "34.00000"|floatformat }}
{{ "34.23234"|floatformat:3 }}
{{ "34.00000"|floatformat:3 }}
```

`join` 可以将一个数组按给定的分隔符合并在一起成为字符串。如：

```twig
{{intList|join:", "}}
```

`split` 刚好和`join`相反，它可以将一个字符串按给定的分隔符将一个字符串转换成数组。如：

```twig
{{ "Hello, 99, 3.140000, good"|split:", "|join:", " }}
```

`stringformat` 可以将数字、字符串格式化成指定的格式输出。相当于`fmt.Sprintf()`。如：

```twig
{{ 0.55555|stringformat:"%.2f" }}
{{ 888|stringformat:"Test: %d" }}
{{ "你好"|stringformat:"Chinese: %s" }}
```

`make_list` 可以将字符串按字符拆分成数组，相当于`[]rune("你好啊")`。如：

```twig
{{ "你好啊"|make_list|join:", " }}
{% for char in "你好啊"|make_list %}{{ char }}，{% endfor %}
```

`center` 这个标签比较有意思，可以将字符串格式化成指定长度，并将字符串放在中间，旁边使用空格填充。如果给定的长度小于字符串长度，则不会做改变。如：

```twig
'{{ "test"|center:3 }}'
'{{ "test"|center:20 }}'
{{ "test"|center:20|length }}
```

`ljust`、`rjust` 这两个标签和`center`差不多，都是给字符串填充到指定长度，但是填充方向不同。`ljust`会在右边填充空格，即让字符串靠左。`rjust`会在左边填充空格，即让字符串靠右。如：

```twig
'{{ "test"|ljust:"20" }}'
{{ "test"|ljust:"20"|length }}
'{{ "test"|rjust:"20" }}'
{{ "test"|rjust:"20"|length }}
```

`wordcount` 用来统计字符串的长度。它有 2 种使用方式，一种是在字符串后面，另一种是使用 filter 标签。如：

```twig
{{ ""|wordcount }}
{% filter wordcount %}{% lorem 25 w %}{% endfilter %}
```

`wordwrap` 可以将字符串按给定的长度换行。如：

```twig
{{ "hello world"|wordwrap:2 }}
<pre>{% filter wordwrap:5 %}{% lorem 26 w %}{% endfilter %}</pre>
{{ "Lorem ipsum dolor sit amet, consectetur adipisici elit."|wordwrap:2|linebreaksbr|safe }}
```

`urlize` 会自动给 url、邮箱添加上 a 标签，并自动增加 nofollow 的 rel。这个用来处理文章正文比较合适。urlize 还支持设置 true 和 false，用来说明显示的连接内容是否转义。如：

```twig
<p>{{ "https://www.kandaoni.com"|urlize|safe }}</p>
<p>{{ "www.kandaoni.com"|urlize|safe }}</p>
<p>{{ "kandaoni.com"|urlize|safe }}</p>
<p>{% filter urlize:true|safe %}</p>
<p>Please mail me at demo@example.com or visit mit on:</p>
<p>- lorem ipsum http://www.kandaoni.com lorem ipsum</p>
<p>- lorem ipsum https://www.kandaoni.com lorem ipsum</p>
<p>- lorem ipsum https://www.kandaoni.com lorem ipsum</p>
<p>- lorem ipsum www.kandaoni.com lorem ipsum</p>
<p>- lorem ipsum www.kandaoni.com/test="test" lorem ipsum</p>
<p>{% endfilter %}</p>
<p>{% filter urlize:false|safe %}</p>
<p>- lorem ipsum www.kandaoni.com/test="test" lorem ipsum</p>
<p>{% endfilter %}</p>
```

`urlizetrunc` 的作用和`urlize`差不多，都是自动给 url、邮箱添加上 a 标签，但是可以设置截取显示部分 url 内容，超过指定长度部分使用`...`代替。如：

```twig
<p>{% filter urlizetrunc:15|safe %}</p>
<p>Please mail me at demo@example.com or visit mit on:</p>
<p>- lorem ipsum http://www.kandaoni.com lorem ipsum</p>
<p>- lorem ipsum https://www.kandaoni.com lorem ipsum</p>
<p>- lorem ipsum https://www.kandaoni.com lorem ipsum</p>
<p>- lorem ipsum www.kandaoni.com lorem ipsum</p>
<p>- lorem ipsum www.kandaoni.com/test="test" lorem ipsum</p>
<p>{% endfilter %}</p>
```

`escapejs` 会将字符串按`\uxxxx`编码预设的部分字符。如：

```twig
{{ "<p>aaa</p><script>alert('xss');</script><p>bbbb</p>"|escapejs|safe }}
```

`slice` 可以对字符串、数组进行截取指定长度的数据。如：

```twig
{{ "Test"|slice:"1:" }}
{{ "Test"|slice:":3" }}
{{ "Test"|slice:"1:3"|join:"," }}
{{ intList|slice:"1:5"|join:"," }}
```

`safe` Django 的模板中会对 HTML 标签和 JS 等语法标签进行自动转义，这样是为了安全，防止 xss 攻击。

如果不想用转义，就使用`safe`来声明要输出的内容是安全的，它就不会自动转义，也可以使用`autoescape`标签来控制开启和关闭自动转义：

```twig
用safe关闭自动转义
{{ "<script>alert('xss');</script>"|safe}}
强制开启自动转义
{% autoescape on %}
{{ "<script>alert('xss');</script>" }}
{% endautoescape %}
强制关闭自动转义，相当于使用了safe
{% autoescape off %}
{{ "<script>alert('xss');</script>" }}
{% endautoescape %}
```

`escape` escape 还可以进行声明转义。由于默认已经会自动转义，因此在此使用 escape 的话，会形成转义 2 次。因此使用`autoescape off`关闭转义后，再使用 escape 就等于直接输出。如：

```twig
{{ "<script>alert('xss');</script>" }}
相当于
{% autoescape off %}
{{ "<script>alert('xss');</script>"|escape }}
{% endautoescape %}
```

上面所有的 filter 标签，都可以使用`{% filter 标签名 %}内容{% endfilter %}` 来使用。比如：

```twig
{% filter lower %}This is a nice test; let's see whether it works. Foobar. {{ simple.xss }}{% endfilter %}

{% filter truncatechars:10|lower|length %}This is a nice test; let's see whether it works. Foobar. {{ simple.number }}{% endfilter %}

<p>{% filter urlize:false|safe %}</p>
<p>- lorem ipsum www.kandaoni.com/test="test" lorem ipsum</p>
<p>{% endfilter %}</p>
```

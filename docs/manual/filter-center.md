# 过滤器：将字符串按指定长度格式居中、靠左、靠右显示

## AICMS 模板中怎么将字符串按指定长度格式居中、靠左、靠右显示？

`center` 过滤器可以将字符串按指定长度格式居中显示。如果字符串长度大于指定的长度，则按字符串实际长度显示，如果字符串长度小于指定的长度，则会在字符串两边补充同等数量的空格来实现居中。如果需要补充的空格数量为单数，则分配右边的空格会比左边少一个。

`ljust` 过滤器可以将字符串按指定长度格式靠左显示。如果字符串长度大于指定的长度，则按字符串实际长度显示，如果字符串长度小于指定的长度，则会在字符串右边补充空格。。

`rjust` 过滤器可以将字符串按指定长度格式靠右显示。如果字符串长度大于指定的长度，则按字符串实际长度显示，如果字符串长度小于指定的长度，则会在字符串左边补充空格。

## 使用方法

`center` 过滤器的使用方法：

```twig
{{ obj|center:number }}
```

`ljust` 过滤器的使用方法：

```twig
{{ obj|ljust:number }}
```

`rjust` 过滤器的使用方法：

```twig
{{ obj|rjust:number }}
```

比如将 `test` 按 20 个字符长度居中显示，则可以这么写：

```twig
'{{ "test"|center:20 }}'
# 显示结果
'        test        '
```

## 示例演示

`center` 过滤器

```twig
'{{ "test"|center:3 }}'
'{{ "test"|center:19 }}'
'{{ "test"|center:20 }}'
{{ "test"|center:20|length }}
'{{ "test2"|center:19 }}'
'{{ "test2"|center:20 }}'
{{ "test2"|center:20|length }}
'{{ "你好世界"|center:20 }}'
# 显示结果
'test'
'        test       '
'        test        '
20
'       test2       '
'        test2       '
20
'        你好世界        '
```

`ljust` 过滤器

```twig
'{{ "test"|ljust:"2" }}'
'{{ "test"|ljust:"20" }}'
{{ "test"|ljust:"20"|length }}
'{{ "你好世界"|ljust:10 }}'
# 显示结果
'test'
'test                '
20
'你好世界      '
```

`rjust` 过滤器

```twig
'{{ "test"|rjust:"2" }}'
'{{ "test"|rjust:"20" }}'
{{ "test"|rjust:"20"|length }}
'{{ "你好世界"|rjust:10 }}'
# 显示结果
'test'
'                test'
20
'      你好世界'
```

# 过滤器：截取符串、数组中指定位置的元素

## AICMS 模板中怎么截取符串、数组中指定位置的元素？

`slice` 过滤器可以截取字符串、数组中指定位置的元素。比如获取一个长度为 10 个元素的第 3 到 7 个元素。

## 使用方法

`slice` 过滤器的使用方法：

```twig
{{obj|slice:"from:to"}}
```

注意 from 和 to 之间使用 `:`隔开。
比如返回 `[1,2,3,4,5,6,7,8,9,10]` 中返回第 3 到第 7 个元素，则可以这么写：

```twig
{{"1,2,3,4,5,6,7,8,9,10"|split:","|slice:"3:7"|join:","}}
# 显示结果
4,5,6,7
```

## 示例演示

```twig
{{ simple.multiple_item_list|slice:":99"|join:"," }}
{{ simple.multiple_item_list|slice:"99:"|join:"," }}
{{ simple.multiple_item_list|slice:":3"|join:"," }}
{{ simple.multiple_item_list|slice:"3:5"|join:"," }}
{{ simple.multiple_item_list|slice:"2:"|join:"," }}
{{ simple.multiple_item_list|slice:"2:3"|join:"," }}
{{ simple.multiple_item_list|slice:"2:1"|join:"," }}
{{ simple.multiple_item_list|slice:"-1:"|join:"," }}
{{ simple.multiple_item_list|slice:":-1"|join:"," }}
{{ simple.multiple_item_list|slice:"-3:"|join:"," }}
{{ simple.multiple_item_list|slice:":-3"|join:"," }}
{{ simple.multiple_item_list|slice:"-100:"|join:"," }}
{{ simple.multiple_item_list|slice:":-100"|join:"," }}
{{ simple.multiple_item_list|slice:"-100:-1"|join:"," }}
{{ simple.multiple_item_list|slice:"-100:1"|join:"," }}
{{ simple.multiple_item_list|slice:"-100:-99"|join:"," }}
{{ simple.multiple_item_list|slice:"-100:99"|join:"," }}
{{ simple.multiple_item_list|slice:"-1:3"|join:"," }}
{{ simple.multiple_item_list|slice:"1:-3"|join:"," }}
{{ simple.multiple_item_list|slice:"-1:-3"|join:"," }}
{{ simple.multiple_item_list|slice:"-3:-1"|join:"," }}
{{ "Test"|slice:"1:3" }}
{{ "你好时间"|slice:"1:3" }}
# 显示结果
1,1,2,3,5,8,13,21,34,55

1,1,2
3,5
2,3,5,8,13,21,34,55
2

55
1,1,2,3,5,8,13,21,34
21,34,55
1,1,2,3,5,8,13
1,1,2,3,5,8,13,21,34,55

1,1,2,3,5,8,13,21,34
1

1,1,2,3,5,8,13,21,34,55

1,2,3,5,8,13

21,34
es
好世
```

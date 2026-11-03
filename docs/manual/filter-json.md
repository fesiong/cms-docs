# 过滤器：将变量转换成JSON输出

## AICMS 模板中怎么将变量转换成JSON输出？

`json` 过滤器可以将某个变量转换成JSON输出。

## 使用方法

`json` 过滤器的使用方法：

```twig
{{ obj|json }}
```

比如将 bannerItem 转换成JSON输出，则可以这么写：

```twig
{{ item|dump }}
# 显示结果
{
  "logo":"http://127.0.0.1:8001/uploads/202309/14/eba5aa9dc4c45d18.webp",
  "id":1,
  "link":"",
  "alt":"Hello",
  "description":"",
  "type":"default"
}
```

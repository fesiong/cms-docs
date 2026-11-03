# 过滤器：获取图片的缩略图

## AICMS 模板中怎么获取图片的缩略图？

`thumb` 过滤器可以根据图片的地址，获取图片的缩略图。

## 使用方法

`thumb` 过滤器的使用方法：

```twig
{{ image|thumb }}
```

比如要获取 banner 的图片缩略图，则可以这么写：

```twig
{% bannerList banners %}
    {% for item in banners %}
    <a href="{{item.Link}}" target="_blank">
        <img src="{{item.Logo}}" alt="{{item.Alt}}" />
        <div class="thumb">
          {{ item.Logo|thumb }}
        </div>
    </a>
    {% endfor %}
{% endbannerList %}
```

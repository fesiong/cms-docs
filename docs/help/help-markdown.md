# AICMS如何在网页正确使用Markdown以及显示数学公式和流程图

新版AICMS新增了Markdown编辑器，因此可以支持插入数学公式和流程图。

但是数学公式和流程图都是需要借助第三方插件支持才能正常显示的。

下面介绍他们的使用方法。

首先在 AICMS后台->全局设置->内容设置 中启用Markdown编辑器

新建一篇文档，在文档中插入数学公式和流程图，供等会测试使用

## 在网页上应用Markdown默认样式：

我们借助 cloudflare 的cdn资源。在base.html 文件的头部，添加如下一行内容：

```html
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css" crossorigin="anonymous" referrerpolicy="no-referrer" />
```

## 网页上数学公式的正确显示

我们借助 jsdelivr 的cdn资源。在base.html 文件的头部，添加如下一行内容：

```html
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
```

## 网页上流程图的正确显示

我们借助 jsdelivr 的cdn资源。在base.html 文件的头部，添加如下内容：

```html
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({ startOnLoad: true });
    </script>
```
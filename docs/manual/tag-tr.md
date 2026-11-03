# 翻译标签

说明：用于模板的指定文字翻译。

使用方法：`{% tr 变量名称 %}`

使用翻译字段的前提是模板支持多语言功能。模板的多语言功能启用方法如下：

在模板目录下创建 locales 目录，然后创建一个文件夹，文件夹的名称是当前语言的代码，例如 zh-CN 或 zh-TW。在文件夹里创建一个 yml 文件，例如 default.yml。目录结构形式如下：

```
./locales
├── en-us
│   └── default.yml
├── ja
│   └── default.yml
├── nl
│   └── default.yml
└── zh-cn
    └── default.yml
```

中文的 default.yml 文件内容如下：

```yml
"yourLocation": "您的位置"
```

调用方法：`{% tr "yourLocation" %}`，在模板解析后，就会相应的显示不同语言的内容，如中文显示成 `您的位置`，英文显示成 `Your location`。

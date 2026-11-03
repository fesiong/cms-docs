# AICMS 模板开发使用指南

## 一、AICMS 模板系统概述

### 什么是 AICMS 模板系统
AICMS 是一款专注于内容管理的开源系统，其模板系统采用简洁易懂的模板引擎，支持标签语法和过滤器功能。模板系统允许开发者通过标签调用内容数据，实现页面的动态展示。

### 模板系统的优势和特点
- **简洁易学**：模板语法简单直观，学习成本低
- **功能强大**：支持内容标签、条件判断、循环输出等多种功能
- **灵活性高**：支持模板继承、包含等高级功能
- **扩展性好**：丰富的过滤器和自定义标签功能

### 模板系统的基本工作原理
AICMS 模板系统通过解析模板文件中的标签和过滤器，将后台数据与前端展示相结合，最终生成HTML页面。系统会根据URL请求匹配对应的模板文件，并将相关内容数据注入到模板中。

## 二、起步准备

### 环境要求和配置
- PHP 7.2+ 环境
- MySQL 5.7+ 数据库
- Web服务器（Apache/Nginx）
- AICMS 系统已安装并运行正常

### 模板目录结构
```
template/
├── default/                # 默认模板目录
│   ├── index.html          # 首页模板
│   ├── category.html       # 分类页模板
│   ├── archive.html        # 内容页模板
│   ├── tag.html            # 标签页模板
│   └── assets/             # 静态资源目录
│       ├── css/
│       ├── js/
│       └── images/
```

### 开发工具推荐
- 代码编辑器：VS Code、Sublime Text 或 WebStorm
- 浏览器：Chrome 或 Firefox（带开发者工具）
- FTP 工具：FileZilla 或 WinSCP

### 第一个模板文件创建
创建一个简单的首页模板 [index.html](index.md)：
```html
<!DOCTYPE html>
<html>
<head>
    <title>{tag:tdk/}</title>
    <meta charset="utf-8">
</head>
<body>
    <header>
        <h1>{tag:system field="siteName"/}</h1>
        <nav>{tag:navList/}</nav>
    </header>
    
    <main>
        <section class="content-list">
            {tag:archiveList typeid="0" limit="10"}
                <article>
                    <h2><a href="{.link}">{.title}</a></h2>
                    <p>{.description}</p>
                    <time>{.time|date:"Y-m-d"}</time>
                </article>
            {/tag:archiveList}
        </section>
    </main>
    
    <footer>
        <p>&copy; {tag:system field="siteName"/}</p>
    </footer>
</body>
</html>
```

## 三、模板基础结构

### 模板文件类型和命名规则
- **首页模板**：[index.html](index.md) - 系统首页
- **分类页模板**：category.html - 分类列表页
- **内容页模板**：archive.html - 文章详情页
- **标签页模板**：tag.html - 标签列表页
- **单页面模板**：page.html - 单页面内容
- **搜索页模板**：search.html - 搜索结果页

### 模板语法基础
AICMS 模板系统使用 `{tag:标签名 参数/}` 的语法格式，主要包含：

**基础标签语法**：
- `{tag:标签名/}` - 无参数标签
- `{tag:标签名 参数="值"/}` - 有参数标签
- `{tag:标签名 参数="值"}内容{/tag:标签名}` - 带内容块的标签

**子标签访问**：
- `{.字段名}` - 访问循环标签中的子字段
- `{.字段名|过滤器}` - 使用过滤器处理字段

### 模板继承与包含
AICMS 支持模板继承和包含功能，可以使用：
- `{tag:include file="header.html"/}` - 包含其他模板文件
- `{tag:block name="content"}{/tag:block}` - 定义可继承的块

### 全局变量和系统标签
- `{tag:system field="siteName"/}` - 网站名称
- `{tag:tdk/}` - 页面标题、描述、关键词
- `{tag:contact/}` - 联系方式信息

## 四、模板配置

### 模板配置文件说明
每个模板目录通常包含 [config.json](filter-json.md) 配置文件，用于定义模板的基本信息和参数：

```json
{
  "name": "默认模板",
  "version": "1.0",
  "author": "开发者名称",
  "description": "模板描述",
  "screenshot": "screenshot.jpg",
  "params": [
    {
      "name": "logo",
      "type": "image",
      "title": "网站Logo",
      "default": ""
    }
  ]
}
```

### 模板参数设置
在配置文件中可以定义模板参数，用户可以在后台修改这些参数，如颜色、Logo、联系方式等。

### 多语言支持配置
通过语言包文件 [lang/](../help/help-content-list.md) 实现多语言支持。

### 模板版本管理
在配置文件中设置版本号，系统会根据版本号判断是否需要更新模板。

## 五、核心标签详解

### 内容标签（文章、分类、标签等）

#### 文章列表标签
使用 [tag:archiveList](tag-archiveList.md) 标签获取文章列表：
```html
{tag:archiveList typeid="1" limit="10" order="id desc"}
    <article>
        <h2><a href="{.link}">{.title}</a></h2>
        <p>{.description|truncatechars:100}</p>
        <img src="{.thumb}" alt="{.title}" />
    </article>
{/tag:archiveList}
```

#### 分类详情标签
使用 [tag:categoryDetail](tag-categoryDetail.md) 获取分类信息：
```html
{tag:categoryDetail id="1"}
    <h1>{.name}</h1>
    <p>{.description}</p>
{/tag:categoryDetail}
```

#### 标签详情标签
使用 [tag:tagDetail](tag-tagDetail.md) 获取标签信息：
```html
{tag:tagDetail id="1"}
    <h1>标签：{.name}</h1>
{/tag:tagDetail}
```

### 导航标签
使用 [tag:navList](tag-navList.md) 生成导航菜单：
```html
{tag:navList}
    <li><a href="{.link}" {if {.current}}class="active"{/if}>{.name}</a></li>
{/tag:navList}
```

### 系统标签
- [tag:system](tag-system.md) - 获取系统配置信息
- [tag:tdk](tag-tdk.md) - 获取页面TDK信息
- [tag:contact](tag-contact.md) - 获取联系信息

### 条件判断和循环标签
使用 [tag:if](tag-if.md) 进行条件判断：
```html
{tag:if condition="1 eq 1"}
    <p>条件成立</p>
{tag:else/}
    <p>条件不成立</p>
{/tag:if}
```

使用 [tag:for](tag-for.md) 进行循环：
```html
{tag:for i="1" to="10"}
    <span>{.i}</span>
{/tag:for}
```

### 过滤器使用
过滤器用于处理标签输出内容，语法为 `字段|过滤器:参数`：

常用过滤器：
- `date` - 日期格式化：`{.time|date:"Y-m-d H:i:s"}`
- `truncatechars` - 截取字符：`{.description|truncatechars:50}`
- `default` - 默认值：`{.title|default:"无标题"}`
- `urlencode` - URL编码：`{.keyword|urlencode}`
- `escape` - 转义HTML：`{.content|escape}`

## 六、实际开发流程

### 模板设计思路
1. **需求分析**：确定页面布局和功能需求
2. **结构设计**：设计模板目录结构和文件组织
3. **原型制作**：制作静态页面原型
4. **模板开发**：将静态页面转换为动态模板
5. **功能完善**：添加交互功能和优化

### 开发步骤详解
1. **创建模板目录**：在 `template/` 目录下创建新模板文件夹
2. **编写基础模板**：创建 [index.html](index.md)、category.html 等基础模板
3. **添加静态资源**：在 `assets/` 目录下放置CSS、JS、图片等资源
4. **集成标签**：在模板中添加 AICMS 标签获取动态内容
5. **测试调试**：在后台切换模板进行测试

### 调试技巧
- 使用 [tag:dump](filter-dump.md) 标签输出变量内容
- 查看浏览器控制台的错误信息
- 检查标签语法是否正确
- 确认标签参数是否符合要求

### 常见问题解决
- **标签不显示内容**：检查标签参数是否正确
- **样式不生效**：检查CSS路径是否正确
- **JS功能异常**：检查JavaScript语法和路径

## 七、高级功能

### 自定义标签
开发者可以根据需要创建自定义标签，扩展模板功能。

### 插件集成
AICMS 支持插件系统，可以集成各种功能插件到模板中。

### 性能优化
- 启用模板缓存
- 优化图片资源
- 压缩CSS和JS文件
- 使用CDN加速静态资源

### SEO 优化
- 正确使用 [tag:tdk](tag-tdk.md) 标签
- 添加结构化数据
- 优化页面加载速度

## 八、最佳实践

### 代码规范
- 保持代码缩进一致
- 使用有意义的变量名
- 添加必要的注释
- 遵循HTML和CSS标准

### 性能优化建议
- 减少不必要的标签嵌套
- 优化数据库查询标签的参数
- 合理使用缓存机制
- 压缩静态资源文件

### 安全注意事项
- 使用 [tag:escape](filter-escape.md) 过滤器防止XSS攻击
- 验证用户输入数据
- 避免在模板中执行复杂逻辑

### 维护和升级
- 定期备份模板文件
- 关注 AICMS 版本更新
- 测试新版本的兼容性
- 记录模板修改历史

通过以上指南，开发者可以快速掌握 AICMS 模板开发的基本技能，从基础的标签使用到高级功能实现，逐步提升模板开发能力。
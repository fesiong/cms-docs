# AICMS 文档

AICMS（AI 内容管理系统）的官方文档站源码。基于 Markdown 编写，由 [MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) 构建，推送到 `main` 后经 GitHub Actions 自动发布到 GitHub Pages。

- **在线访问**：<https://docs.anqicms.com/>
- **内容规模**：251 篇 Markdown（首页 1 · 使用手册 91 · 帮助文档 31 · API 文档 128）+ 111 张配图
- **许可证**：[MIT](LICENSE)

## 文档分区

| 目录 | 内容 |
| --- | --- |
| `docs/manual/` | 模板手册：标签（`tag-*`）、过滤器（`filter-*`）参考 |
| `docs/help/` | 认识 AICMS、安装部署（Docker / 宝塔 / 1Panel / 反向代理）、后台功能说明 |
| `docs/api/` | RESTful 接口、GraphQL 接口、公共参数与错误码 |

## 目录结构

```
.
├── docs/                  # 文档源文件（唯一需要日常编辑的地方）
│   ├── index.md           # 站点首页
│   ├── manual/            # 模板手册（配图在 manual/images/）
│   ├── help/              # 帮助文档（配图在 help/images/）
│   ├── api/               # API 文档（含 graphql/ 子目录）
│   └── stylesheets/
│       └── extra.css      # 品牌配色与样式覆盖
├── overrides/
│   └── main.html          # Material 主题覆盖层：SEO 元信息 / JSON-LD / iframe 适配
├── tools/
│   ├── gen_nav.py         # 由各分区 index.md 重建 mkdocs.yml 的 nav
│   └── convert_docs.py    # 从上游 AICMS 仓库批量转换文档（谨慎使用，见下）
├── mkdocs.yml             # 站点配置（主题、导航、Markdown 扩展）
├── requirements.txt       # 构建依赖
└── .github/workflows/deploy.yml   # 自动构建并发布到 Pages
```

## 本地开发

需要 Python 3.8 及以上（CI 使用 3.12，本地验证过 3.13）。

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

mkdocs serve                       # 实时预览 http://127.0.0.1:8000
mkdocs build -d _site              # 构建静态站点到 _site/
```

> 提示：如果直接跑 `python3 -m mkdocs` 报 `No module named mkdocs`，通常是虚拟环境没激活，用 `.venv/bin/mkdocs serve` 直接指定解释器即可。

`.venv/` 与 `_site/` 均在 `.gitignore` 中，不会入库。

## 部署

推送到 `main` 即触发 [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml)：

1. 安装 `requirements.txt` 依赖；
2. `mkdocs build -d _site`；
3. 通过 `actions/deploy-pages` 发布到 GitHub Pages。

也可以在仓库 **Actions → 部署文档到 GitHub Pages → Run workflow** 手动触发一次。本地构建产物不会自动同步到线上，线上只认 CI 的构建结果。

构建时可能看到少量 `contains a link '#xxx', but there is no such anchor` 的 INFO 提示，来自源文档中失效的中文锚点，不影响构建成功与页面发布。

## 新增或修改文档

导航**不是**手写进 `mkdocs.yml` 的，而是由 `tools/gen_nav.py` 从各分区的 `index.md` 解析生成，因此新增页面要按这个链路走：

1. 在 `docs/manual/`、`docs/help/` 或 `docs/api/` 下新建 `.md`；配图放该分区的 `images/` 子目录（如 `docs/help/images/`），用相对路径引用；
2. 在对应分区的 `docs/<分区>/index.md` 里按既有格式补一条链接——`##` 是分组、`###` 是子分组、分组前的裸链接会置顶；
3. 重建导航并预览：

   ```bash
   .venv/bin/python tools/gen_nav.py
   .venv/bin/mkdocs serve
   ```

4. 确认无误后提交 `docs/` 改动与 `mkdocs.yml` 一起推送。

改动 `mkdocs.yml` 的 `nav:` 段之前请注意：**手改的内容会在下次执行 `gen_nav.py` 时被覆盖**。要调整导航结构，请改分区 `index.md`（或改脚本）。

## 站点定制

- **主题与配色**：`mkdocs.yml` 中 `palette` 的 `primary/accent` 设为 `custom`，实际色值由 `docs/stylesheets/extra.css` 的 `--md-primary-fg-color` 提供（品牌主色 `#0068AB`）。若改成 `teal` 这类内置色名，主题自带的 `palette.css` 会覆盖自定义值。
- **样式覆盖**：统一写在 `docs/stylesheets/extra.css`，该文件在主题 CSS 之后加载，具有最终优先级；深浅色（`default` / `slate`）分别在同文件顶部声明。
- **页面注入**：`overrides/main.html` 的 `extrahead` 块负责输出 Open Graph / Twitter 卡片、JSON-LD 结构化数据（`TechArticle` + `WebSite`），以及一段 iframe 检测脚本。
- **iframe 嵌入**：页面被 iframe 引用时，脚本会给 `<body>` 加上 `iniframe` 类，配合 `extra.css` 隐藏顶栏、页脚、侧栏和菜单按钮，便于嵌入到 AICMS 官网或其他宿主页面中。

## 关于 tools/

| 脚本 | 用途 | 注意 |
| --- | --- | --- |
| `gen_nav.py` | 解析 `docs/{manual,help,api}/index.md`，重写 `mkdocs.yml` 的 `nav:` 段，其余配置保持不变 | 日常维护导航用这个，可反复执行。脚本会截断 `nav:` 之后的全部内容，因此 `nav:` 必须留在文件末尾（当前配置即如此） |
| `convert_docs.py` | 从上游 AICMS 仓库批量拷贝 api/manual 文档并**整体重写** `mkdocs.yml` | 源路径写死为本机绝对路径（`/Users/fesion/data/backend/AICMS/doc/...`），且不带 help 分区逻辑。**重跑会覆盖 `docs/` 同名文件与整个 `mkdocs.yml`**，仅在需要从上游重新同步时使用，执行前务必确认没有未提交的本地改动 |

## 参与贡献

发现文档错漏，欢迎提 [Issue](https://github.com/fesiong/cms-docs/issues) 或 PR。PR 请尽量一页一事，附上对应的 AICMS 版本或接口变更说明。

## License

[MIT](LICENSE) © 2026 Sinclair

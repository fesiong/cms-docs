#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convert AICMS api/manual markdown docs into a MkDocs Material site.

- Copies the two doc sets into ./docs preserving structure (incl. images,
  graphql schema/json assets).
- Generates mkdocs.yml with navigation parsed from the existing TOC files
  (api/index.md and manual/index.md), and covers any orphan pages via
  explicit groupings / prefix fallback so every page is published.
- Creates a placeholder for the one missing referenced page (schedule.md).

Run:  python tools/convert_docs.py
"""
import os
import re
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_API = "/Users/fesion/data/backend/AICMS/doc/api"
SRC_MANUAL = "/Users/fesion/data/backend/AICMS/doc/manual"
DST = os.path.join(ROOT, "docs")

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+?\.md)\)")


def get_h1(nav_path):
    """Return the first H1 of a doc page, or '' if not found."""
    fp = os.path.join(ROOT, nav_path)
    try:
        with open(fp, encoding="utf-8") as f:
            for line in f:
                m = re.match(r"^#\s+(.*)$", line)
                if m:
                    return m.group(1).strip()
    except OSError:
        pass
    return ""


def page_title(nav_path, fallback):
    h1 = get_h1(nav_path)
    return h1 if h1 else fallback


def copy_docset(src, dst):
    # Overwrite copy (no bulk delete) so re-runs are idempotent and the
    # safe-delete guard is never triggered.
    os.makedirs(dst, exist_ok=True)
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for f in files:
            if f.startswith("."):
                continue
            s = os.path.join(root, f)
            rel = os.path.relpath(s, src)
            d = os.path.join(dst, rel)
            os.makedirs(os.path.dirname(d), exist_ok=True)
            shutil.copy2(s, d)
    print(f"copied {src} -> {dst}")


def parse_index(path, prefix, use_link_text=False):
    """Return (sections, referenced).

    sections: list of (title, [(item_title, nav_path), ...])
    referenced: set of basenames linked from this index.
    """
    sections = []
    cur = None
    referenced = set()
    text = open(path, encoding="utf-8").read()
    for line in text.splitlines():
        m2 = re.match(r"^##\s+(.*)$", line)
        if m2:
            cur = (m2.group(1).strip(), [])
            sections.append(cur)
            continue
        for ltext, ltarget in LINK_RE.findall(line):
            rel = ltarget.replace("./", "").split("#")[0]
            if rel.startswith("graphql/"):
                navpath = f"api/{rel}"
            else:
                navpath = f"{prefix}/{rel}"
            referenced.add(rel)
            if use_link_text:
                title = ltext
            else:
                pre = line.replace(f"[{ltext}]({ltarget})", "", 1)
                pre = re.sub(r"^[\s\-#>*|]+", "", pre)
                pre = pre.replace("[查看]", "").strip().strip("[]").strip()
                title = pre if pre and pre != "查看" else ltext
            if cur is None:
                cur = ("概览", [])
                sections.append(cur)
            cur[1].append((title, navpath))
    return sections, referenced


def all_md(dst_dir, prefix):
    out = {}
    for root, dirs, files in os.walk(dst_dir):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for f in files:
            if f.endswith(".md") and not f.startswith("."):
                rel = os.path.relpath(os.path.join(root, f), dst_dir)
                out[f] = f"{prefix}/{rel}"
    return out


def manual_leftover_group(fname):
    if fname.startswith("tag-"):
        return "模板标签"
    if fname.startswith("filter-"):
        return "模板过滤器"
    if fname.startswith("help-"):
        return "后台使用帮助"
    if fname.startswith("design-"):
        return "模板制作"
    if fname.startswith("docker-") or fname in {
        "install.md",
        "apache.md",
        "start.md",
        "faq.md",
        "changelog.md",
        "1-guide.md",
        "aicms.md",
        "AICMS 项目优势.md",
    }:
        return "入门与基础"
    return "其他文档"


def build_nav():
    nav = []

    # ---------- Manual ----------
    msections, mref = parse_index(os.path.join(DST, "manual/index.md"), "manual")
    mfiles = all_md(os.path.join(DST, "manual"), "manual")
    mleftover = {f: p for f, p in mfiles.items() if f not in mref and f != "index.md"}
    mleft_groups = {}
    for f, p in mleftover.items():
        g = manual_leftover_group(f)
        mleft_groups.setdefault(g, []).append((page_title(p, f.replace(".md", "")), p))
    mleft_groups = {k: sorted(v) for k, v in mleft_groups.items()}

    manual_nav = [{"使用手册首页": "manual/index.md"}]
    for title, items in msections:
        if not items:
            continue
        manual_nav.append({title: [{t: p} for t, p in items]})
    for g, items in mleft_groups.items():
        manual_nav.append({g: [{t: p} for t, p in items]})
    nav.append({"使用手册": manual_nav})

    # ---------- API ----------
    asections, _aref = parse_index(
        os.path.join(DST, "api/index.md"), "api", use_link_text=True
    )
    afiles = all_md(os.path.join(DST, "api"), "api")

    api_nav = [{"API 文档总览": "api/index.md"}]
    for title, items in asections:
        if title == "GraphQL接口":
            continue
        if not items:
            continue
        api_nav.append({title: [{t: p} for t, p in items]})

    general = [
        ("API 概览（详细分类）", "api/index.md"),
        ("API 通用指南", "api/api-guide.md"),
        ("API 请求头", "api/api-header.md"),
        ("API 匹配规则", "api/api-match.md"),
        ("API 模板", "api/api-template.md"),
        ("元数据 Metadata", "api/metadata.md"),
    ]
    general = [(t, p) for t, p in general if os.path.exists(os.path.join(ROOT, p))]
    if general:
        api_nav.append({"通用说明": [{t: p} for t, p in general]})

    groups = {
        "地区与位置接口": [
            "placeAutocomplete.md",
            "placeCountries.md",
            "placeCountryCities.md",
            "placeCountryStates.md",
            "placeDetail.md",
            "placeList.md",
        ],
        "活动与营销接口": ["activityDetail.md", "activityList.md", "archiveActivity.md"],
        "订单扩展接口": [
            "orderCustomForm.md",
            "orderCustomFormSave.md",
            "orderServices.md",
            "shippingInfo.md",
        ],
    }
    for g, fs in groups.items():
        items = [
            (page_title(f"api/{f}", os.path.splitext(f)[0]), f"api/{f}")
            for f in fs
            if f in afiles
        ]
        if items:
            api_nav.append({g: [{t: p} for t, p in items]})

    gql_dir = os.path.join(DST, "api/graphql")
    gql_items = []
    for f, title in [
        ("README.md", "GraphQL 概览"),
        ("queries.md", "查询 Queries"),
        ("mutations.md", "变更 Mutations"),
        ("objects.md", "对象 Objects"),
        ("scalars.md", "标量 Scalars"),
    ]:
        if os.path.exists(os.path.join(gql_dir, f)):
            gql_items.append({title: f"api/graphql/{f}"})
    if gql_items:
        api_nav.append({"GraphQL": gql_items})

    covered = set()

    def collect(node):
        if isinstance(node, dict):
            for k, v in node.items():
                if isinstance(v, str):
                    covered.add(v)
                else:
                    collect(v)
        elif isinstance(node, list):
            for x in node:
                collect(x)

    collect(api_nav)
    api_leftover = sorted(
        p
        for f, p in afiles.items()
        if p not in covered and f != "index.md" and not p.startswith("api/graphql/")
    )
    if api_leftover:
        api_nav.append(
            {"通用文档": [{page_title(p, os.path.splitext(os.path.basename(p))[0]): p} for p in api_leftover]}
        )
    nav.append({"API 文档": api_nav})

    nav.insert(0, {"首页": "index.md"})
    return nav


def yaml_str(s):
    if not isinstance(s, str):
        return s
    if s == "":
        return '""'
    needs = (
        any(c in s for c in [":", "#", "{", "}", "[", "]", "&", "*", "?", "|", ">", '"', "'", "%", "@", "`"])
        or s.strip() != s
        or s.startswith("- ")
    )
    if needs:
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


def write_mkdocs(nav):
    lines = []
    lines.append("site_name: AICMS 文档")
    lines.append("site_url: https://fesiong.github.io/cms-docs/")
    lines.append("site_description: AICMS 使用手册与 API 接口文档")
    lines.append("site_author: AICMS")
    lines.append("repo_url: https://github.com/fesiong/cms-docs")
    lines.append("repo_name: fesiong/cms-docs")
    lines.append("edit_uri: edit/main/docs/")
    lines.append("docs_dir: docs")
    lines.append("use_directory_urls: true")
    lines.append("")
    lines.append("theme:")
    lines.append("  name: material")
    lines.append("  language: zh")
    lines.append("  features:")
    lines.append("    - navigation.sections")
    lines.append("    - navigation.top")
    lines.append("    - navigation.tracking")
    lines.append("    - content.code.copy")
    lines.append("    - content.code.annotate")
    lines.append("    - search.suggest")
    lines.append("    - search.highlight")
    lines.append("  palette:")
    lines.append("    - scheme: default")
    lines.append("      primary: teal")
    lines.append("      accent: teal")
    lines.append("      toggle:")
    lines.append("        icon: material/weather-night")
    lines.append("        name: 切换深色模式")
    lines.append("    - scheme: slate")
    lines.append("      primary: teal")
    lines.append("      accent: teal")
    lines.append("      toggle:")
    lines.append("        icon: material/weather-sunny")
    lines.append("        name: 切换浅色模式")
    lines.append("")
    lines.append("plugins:")
    lines.append("  - search")
    lines.append("")
    lines.append("markdown_extensions:")
    lines.append("  - admonition")
    lines.append("  - toc:")
    lines.append("      permalink: true")
    lines.append("      toc_depth: 3")
    lines.append("  - pymdownx.highlight:")
    lines.append("      anchor_linenums: true")
    lines.append("  - pymdownx.superfences")
    lines.append("  - pymdownx.inlinehilite")
    lines.append("  - pymdownx.tabbed:")
    lines.append("      alternate_style: true")
    lines.append("  - pymdownx.tasklist:")
    lines.append("      custom_checkbox: true")
    lines.append("  - pymdownx.snippets")
    lines.append("  - attr_list")
    lines.append("  - md_in_html")
    lines.append("  - tables")
    lines.append("")
    lines.append("extra:")
    lines.append("  social:")
    lines.append("    - icon: fontawesome/brands/github")
    lines.append("      link: https://github.com/fesiong/cms-docs")
    lines.append("")
    lines.append("nav:")

    def emit(node, indent):
        pad = "  " * indent
        if isinstance(node, dict):
            for k, v in node.items():
                if isinstance(v, str):
                    lines.append(f"{pad}- {yaml_str(k)}: {yaml_str(v)}")
                else:
                    lines.append(f"{pad}- {yaml_str(k)}:")
                    emit(v, indent + 1)
        elif isinstance(node, list):
            for x in node:
                emit(x, indent)

    emit(nav, 1)
    return "\n".join(lines) + "\n"


def fix_doc_defects():
    """Repair known source defects so the published site renders correctly.

    - docker-bt.md has an image link with a stray '?' (docker-bt-4.png?).
    - 1-guide.md (and possibly others) uses absolute file:// links pointing
      at a different machine path (blog-doc); rewrite them to relative links.
    """
    # 1) stray '?' on an image reference
    bt = os.path.join(DST, "manual/docker-bt.md")
    if os.path.exists(bt):
        s = open(bt, encoding="utf-8").read()
        s2 = s.replace("docker-bt-4.png?", "docker-bt-4.png")
        if s2 != s:
            open(bt, "w", encoding="utf-8").write(s2)

    # 2) absolute file:// links to blog-doc -> relative
    bad_prefix = "file:///Users/fesion/data/gitpath/blog-doc/manual/"
    for root, dirs, files in os.walk(os.path.join(DST, "manual")):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for f in files:
            if not f.endswith(".md"):
                continue
            p = os.path.join(root, f)
            s = open(p, encoding="utf-8").read()
            if bad_prefix in s:
                open(p, "w", encoding="utf-8").write(s.replace(bad_prefix, ""))


def main():
    copy_docset(SRC_API, os.path.join(DST, "api"))
    copy_docset(SRC_MANUAL, os.path.join(DST, "manual"))
    fix_doc_defects()

    stub = os.path.join(DST, "manual/schedule.md")
    if not os.path.exists(stub):
        with open(stub, "w", encoding="utf-8") as f:
            f.write(
                "# 开发计划\n\n> 本文档待补充。\n\n"
                "该页面为《开发计划》占位页，内容整理中。\n"
            )

    nav = build_nav()
    content = write_mkdocs(nav)
    with open(os.path.join(ROOT, "mkdocs.yml"), "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote mkdocs.yml")
    print("top nav sections:", [list(x.keys())[0] for x in nav])


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""根据 docs/{manual,help,api}/index.md 重建 mkdocs.yml 的 nav 段。

索引文件由人工维护、按功能分组；本脚本解析其分组结构（支持 ## 分组、
### 子分组、分组前的置顶链接），生成与索引完全一致的导航，保证 nav 与
文档目录始终同步。

用法: python tools/gen_nav.py
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
MK = os.path.join(ROOT, "mkdocs.yml")

LINK_RE = re.compile(r'^\s*(?:[-*]\s+)?\[([^\]]+)\]\(([^)]+?)\)')
H2_RE = re.compile(r'^##\s+(.+?)\s*:?\s*$')
H3_RE = re.compile(r'^###\s+(.+?)\s*$')


def parse_index(rel_dir):
    """解析 docs/<rel_dir>/index.md -> (top_links, groups)。

    top_links: [(title, path)]  出现在任何 '##' 之前的链接
    groups:    [{"name","subs":[{"name","items":[]}],"items":[]}]
    """
    path = os.path.join(DOCS, rel_dir, "index.md")
    groups = []
    top_links = []
    for raw in open(path, encoding="utf-8"):
        line = raw.rstrip("\n")
        m3 = H3_RE.match(line)
        if m3:
            if groups and groups[-1]["subs"] is not None:
                groups[-1]["subs"].append({"name": m3.group(1).strip(), "items": []})
            continue
        m2 = H2_RE.match(line)
        if m2:
            groups.append({"name": m2.group(1).strip(), "subs": [], "items": []})
            continue
        m = LINK_RE.match(line)
        if m:
            title = m.group(1).strip()
            target = m.group(2).strip().split("#")[0].lstrip("./")
            full = f"{rel_dir}/{target}" if not target.startswith(rel_dir + "/") else target
            item = (title, full)
            if not groups:
                top_links.append(item)
            elif groups[-1]["subs"]:
                groups[-1]["subs"][-1]["items"].append(item)
            else:
                groups[-1]["items"].append(item)
    return top_links, groups


def emit_section(title, index_title, rel_dir, top_links, groups):
    out = [f"  - {title}:"]
    out.append(f"    - {index_title}: {rel_dir}/index.md")
    for t, p in top_links:
        out.append(f"    - {t}: {p}")
    for g in groups:
        out.append(f"    - {g['name']}:")
        if g["subs"]:
            for sub in g["subs"]:
                out.append(f"      - {sub['name']}:")
                for t, p in sub["items"]:
                    out.append(f"        - {t}: {p}")
        else:
            for t, p in g["items"]:
                out.append(f"      - {t}: {p}")
    return out


def main():
    manual_top, manual_groups = parse_index("manual")
    help_top, help_groups = parse_index("help")
    api_top, api_groups = parse_index("api")

    nav = ["nav:", "  - 首页: index.md"]
    nav += emit_section("使用手册", "使用手册首页", "manual", manual_top, manual_groups)
    nav += emit_section("帮助文档", "帮助文档首页", "help", help_top, help_groups)
    nav += emit_section("API 文档", "API 文档总览", "api", api_top, api_groups)

    text = open(MK, encoding="utf-8").read()
    if "nav:" not in text:
        raise SystemExit("mkdocs.yml 中未找到 nav: 段")
    idx = text.index("nav:")
    new_text = text[:idx] + "\n".join(nav) + "\n"

    # 校验：nav 中的每条 .md 路径必须存在
    missing = []
    for m in re.findall(r':\s*([\w/.\\-]+?\.md)\s*$', new_text, re.M):
        if not os.path.exists(os.path.join(DOCS, m)):
            missing.append(m)
    if missing:
        raise SystemExit("发现不存在的 nav 路径，已中止写入:\n  " + "\n  ".join(missing))

    open(MK, "w", encoding="utf-8").write(new_text)
    print("nav 已重建：使用手册/帮助文档/API 文档 三段，共",
          sum(1 for l in nav if l.strip().startswith("-")), "个导航节点")


if __name__ == "__main__":
    main()

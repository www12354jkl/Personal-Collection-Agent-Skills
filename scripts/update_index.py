#!/usr/bin/env python3
"""Generate D:\\workspace\\AgentSkills\\INDEX.md from skill and plugin cards."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import re
import sys
from pathlib import Path
from typing import Any

import yaml

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", re.DOTALL)
DEFAULT_CATEGORY = "未分类"

SECTIONS: tuple[tuple[str, str], ...] = (
    ("skills", "Skills"),
    ("plugins", "Plugins / Tools"),
)

SKILL_CATEGORY_ORDER: tuple[str, ...] = (
    "规划与需求",
    "工程与架构",
    "Agent编排",
    "前端与设计",
    "图表与文档",
    "写作与教学",
    "图像与视频",
    "系统与运维",
)


def parse_frontmatter(path: Path) -> dict[str, Any]:
    """Parse YAML frontmatter from a Markdown card file."""
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError(f"Missing YAML frontmatter in {path}")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError(f"Frontmatter must be a mapping in {path}")
    return data


def clean_cell(value: Any) -> str:
    """Normalize a cell value so it renders cleanly inside a Markdown table."""
    if value is None:
        return "-"
    text = re.sub(r"\s+", " ", str(value)).strip()
    if not text:
        return "-"
    return text.replace("|", "\\|")


def format_list(value: Any, prefix: str = "") -> str:
    """Format a YAML string or list as comma-separated items."""
    if not value:
        return "-"
    items = [value] if isinstance(value, str) else list(value)
    cleaned = [clean_cell(item) for item in items if str(item).strip()]
    if not cleaned:
        return "-"
    return ", ".join(f"`{prefix}{item}`" if prefix else item for item in cleaned)


def format_source(repo: Any) -> str:
    """Extract a compact owner/repo label from a repository URL."""
    raw = clean_cell(repo)
    if raw == "-":
        return "-"
    trimmed = re.sub(r"^https?://(?:www\.)?github\.com/", "", raw)
    trimmed = re.sub(r"\.git/?$", "", trimmed).rstrip("/")
    return trimmed or raw


def collect_cards(root: Path, subdir: str) -> list[dict[str, str]]:
    """Collect normalized metadata rows for all Markdown cards in a section directory."""
    directory = root / subdir
    if not directory.is_dir():
        return []

    rows: list[dict[str, str]] = []
    for card_path in sorted(directory.rglob("*.md"), key=lambda p: p.name.lower()):
        meta = parse_frontmatter(card_path)
        name = clean_cell(meta.get("name") or card_path.stem)
        category = clean_cell(meta.get("category"))
        if category == "-":
            category = DEFAULT_CATEGORY
        rel_path = card_path.relative_to(root).as_posix()
        install_cmd = clean_cell(meta.get("install_cmd"))
        source = format_source(meta.get("repo"))
        rows.append(
            {
                "name": name,
                "category": category,
                "aliases": format_list(meta.get("aliases")),
                "source": source,
                "tags": format_list(meta.get("tags")),
                "version": clean_cell(meta.get("version")),
                "install_cmd": f"`{install_cmd}`" if install_cmd != "-" else "-",
                "description": clean_cell(meta.get("description")),
                "link": f"[{rel_path}]({rel_path})",
            }
        )
    return sorted(rows, key=lambda row: row["name"].lower())


def group_by_category(
    rows: list[dict[str, str]],
    preferred_order: tuple[str, ...] = (),
) -> list[tuple[str, list[dict[str, str]]]]:
    """Group rows by category following preferred_order, then custom names, then uncategorized."""
    buckets: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        buckets[row["category"]].append(row)

    ordered_names: list[str] = [c for c in preferred_order if c in buckets]
    extra_names = sorted(
        c for c in buckets if c not in preferred_order and c != DEFAULT_CATEGORY
    )
    ordered_names.extend(extra_names)
    if DEFAULT_CATEGORY in buckets:
        ordered_names.append(DEFAULT_CATEGORY)

    return [(cat, buckets[cat]) for cat in ordered_names]


def render_table(rows: list[dict[str, str]]) -> list[str]:
    """Render card metadata rows as a Markdown table."""
    if not rows:
        return ["_暂无条目_"]

    lines = [
        "| 名称 | 别名 | 来源 | 版本 | 安装命令 | 标签 | 用途说明 | 卡片 |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
    ]
    for row in rows:
        source_cell = f"`{row['source']}`" if row["source"] != "-" else "-"
        lines.append(
            f"| **{row['name']}** | {row['aliases']} | {source_cell} | {row['version']} | "
            f"{row['install_cmd']} | {row['tags']} | {row['description']} | {row['link']} |"
        )
    return lines


def render_overview(
    skill_groups: list[tuple[str, list[dict[str, str]]]],
    all_rows: list[dict[str, str]],
) -> list[str]:
    """Render category overview table and multi-card source repository summary."""
    lines = [
        "## 分类速览",
        "",
        "| 分类 | 数量 | 代表条目 |",
        "| :--- | :---: | :--- |",
    ]
    for cat, items in skill_groups:
        preview = ", ".join(item["name"] for item in items[:5])
        if len(items) > 5:
            preview += f" 等 {len(items)} 项"
        lines.append(f"| **{cat}** | {len(items)} | {preview} |")

    repo_counts = Counter(row["source"] for row in all_rows if row["source"] != "-")
    suites = [(repo, count) for repo, count in repo_counts.most_common() if count >= 2]
    standalone = sum(count for _, count in repo_counts.items() if count == 1)
    if suites:
        suite_summary = " · ".join(f"`{repo}` ({count})" for repo, count in suites)
        lines.append("")
        lines.append(f"> **来源套件分布**：{suite_summary} · 独立仓库 ({standalone})")

    lines.append("")
    return lines


def build_index(root: Path) -> str:
    """Build the complete categorized INDEX.md Markdown content for the repository."""
    section_rows: dict[str, list[dict[str, str]]] = {
        subdir: collect_cards(root, subdir) for subdir, _ in SECTIONS
    }
    counts = " · ".join(
        f"{heading}: {len(section_rows[subdir])}" for subdir, heading in SECTIONS
    )
    all_rows = [row for subdir, _ in SECTIONS for row in section_rows[subdir]]
    skill_groups = group_by_category(section_rows["skills"], SKILL_CATEGORY_ORDER)

    lines: list[str] = [
        "# AgentSkills Catalog Index",
        "",
        "<!-- Auto-generated by scripts/update_index.py. Do not edit manually. -->",
        "",
        f"> 本地技能与插件检索索引（{counts}）。Obsidian 交互筛选见 [分类看板.md](分类看板.md)；修改或新增卡片后运行 `python scripts/update_index.py` 更新（已配置 Git `pre-commit` 自动同步）。",
        "",
    ]

    if skill_groups:
        lines.extend(render_overview(skill_groups, all_rows))

    # Skills section grouped by category
    lines.append(f"## Skills ({len(section_rows['skills'])})")
    lines.append("")
    if not skill_groups:
        lines.append("_暂无条目_")
        lines.append("")
    else:
        for cat, items in skill_groups:
            lines.append(f"### {cat} ({len(items)})")
            lines.append("")
            lines.extend(render_table(items))
            lines.append("")

    # Plugins / Tools section (group by category automatically once >= 2 categories exist)
    plugin_rows = section_rows["plugins"]
    lines.append(f"## Plugins / Tools ({len(plugin_rows)})")
    lines.append("")
    plugin_groups = group_by_category(plugin_rows)
    if len(plugin_groups) <= 1:
        lines.extend(render_table(plugin_rows))
        lines.append("")
    else:
        for cat, items in plugin_groups:
            lines.append(f"### {cat} ({len(items)})")
            lines.append("")
            lines.extend(render_table(items))
            lines.append("")

    return "\n".join(lines)


def print_stats(root: Path) -> None:
    """Print category and repository counts to stdout."""
    for subdir, heading in SECTIONS:
        rows = collect_cards(root, subdir)
        print(f"{heading} ({len(rows)}):")
        order = SKILL_CATEGORY_ORDER if subdir == "skills" else ()
        for cat, items in group_by_category(rows, order):
            print(f"  - {cat}: {len(items)}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate INDEX.md from AgentSkills cards.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Path to the AgentSkills repository root.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check whether INDEX.md is up to date without modifying it.",
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        help="Print category counts without modifying INDEX.md.",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    if args.stats:
        print_stats(root)
        return 0

    index_path = root / "INDEX.md"
    rendered = build_index(root)
    existing = index_path.read_text(encoding="utf-8") if index_path.exists() else None

    if args.check:
        if existing == rendered:
            print(f"OK: {index_path} is up to date.")
            return 0
        print(f"OUTDATED: {index_path} needs regeneration.", file=sys.stderr)
        return 1

    if existing == rendered:
        print(f"Unchanged: {index_path}")
        return 0

    index_path.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"Updated: {index_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

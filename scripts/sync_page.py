#!/usr/bin/env python3
"""Synchronize generated project-page blocks from README.md."""

from __future__ import annotations

import argparse
import difflib
import html
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
INDEX_PATH = ROOT / "index.html"

CATEGORY_LABELS = {
    "Physics- and Rule-Based Event-Camera Simulators": "Physics- & rule-based",
    "Learning-Based Event Generation": "Learning-based",
    "Evaluation and Sim-to-Real Analysis": "Evaluation",
}

LINK_RE = re.compile(r"\[\[([^\]]+)\]\((https?://[^)]+)\)\]")
ENTRY_RE = re.compile(r"^- \*\*(?P<head>.+?)\*\*(?P<body>.*)$")
YEAR_RE = re.compile(r"\b(20\d{2})\b")


@dataclass(frozen=True)
class CatalogEntry:
    title: str
    authors_or_name: str
    category: str
    subcategory: str
    venue: str
    year: int | None
    links: tuple[tuple[str, str], ...]


def clean_inline_markdown(value: str) -> str:
    value = value.strip()
    value = re.sub(r"[*_`]+", "", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def clean_heading(line: str) -> tuple[int, str] | None:
    match = re.match(r"^(#{2,3})\s+(.+?)\s*$", line)
    if not match:
        return None
    level = len(match.group(1))
    text = clean_inline_markdown(match.group(2))
    return level, text


def parse_readme(readme_text: str) -> list[CatalogEntry]:
    entries: list[CatalogEntry] = []
    category = ""
    subcategory = ""

    for line_number, line in enumerate(readme_text.splitlines(), start=1):
        heading = clean_heading(line)
        if heading:
            level, text = heading
            if level == 2:
                category = text if text in CATEGORY_LABELS else ""
                subcategory = ""
            elif level == 3 and category:
                subcategory = text
            continue

        if not category:
            continue

        match = ENTRY_RE.match(line)
        if not match:
            if line.startswith("- "):
                raise ValueError(
                    f"README line {line_number} is not a supported catalog bullet; "
                    "use '- **Name**, *Title*, Venue Year. [[paper](...)]'"
                )
            continue

        head = clean_inline_markdown(match.group("head"))
        body = match.group("body").strip()
        links = tuple((label.strip(), url.strip()) for label, url in LINK_RE.findall(body))
        if not links:
            raise ValueError(f"README line {line_number} has no recognized [[label](url)] links")

        body_without_links = LINK_RE.sub("", body).strip()
        italic_match = re.search(r"\*(.+?)\*", body_without_links)
        if italic_match:
            title = clean_inline_markdown(italic_match.group(1))
            venue = clean_inline_markdown(body_without_links[italic_match.end() :].strip(" .,;:-"))
        else:
            title = head
            venue = clean_inline_markdown(body_without_links.strip(" .,;:-")) or "Public resource"

        years = [int(value) for value in YEAR_RE.findall(line)]
        entries.append(
            CatalogEntry(
                title=title,
                authors_or_name=head,
                category=category,
                subcategory=subcategory,
                venue=venue or "Public resource",
                year=max(years) if years else None,
                links=links,
            )
        )

    return entries


def count_public_code_links(entries: list[CatalogEntry]) -> int:
    return sum(
        1
        for entry in entries
        for label, url in entry.links
        if label.lower() == "code" and "github.com/" in url.lower()
    )


def render_links(links: tuple[tuple[str, str], ...]) -> str:
    rendered = []
    for label, url in links:
        label_text = "arXiv" if label.lower() == "arxiv" else label
        rendered.append(f'<a href="{html.escape(url, quote=True)}">{html.escape(label_text)}</a>')
    return " &middot; ".join(rendered)


def render_hero_meta(entries: list[CatalogEntry]) -> str:
    latest_year = max((entry.year or 0 for entry in entries), default=0)
    coverage = f"Coverage through {latest_year}" if latest_year else "Coverage maintained in README"
    lines = [
        f'<span class="pill">{len(entries)} indexed resources</span>',
        f'<span class="pill">{count_public_code_links(entries)} public code links</span>',
        f'<span class="pill">{html.escape(coverage)}</span>',
    ]
    return indent_lines(lines, "          ")


def render_stats(entries: list[CatalogEntry]) -> str:
    counts = Counter(entry.category for entry in entries)
    items = [
        (
            counts["Physics- and Rule-Based Event-Camera Simulators"],
            "physics- and rule-based resources",
        ),
        (counts["Learning-Based Event Generation"], "learning-based resources"),
        (counts["Evaluation and Sim-to-Real Analysis"], "evaluation and benchmark resources"),
        (len(CATEGORY_LABELS), "review categories"),
    ]
    lines: list[str] = []
    for number, label in items:
        lines.extend(
            [
                '<article class="item">',
                f'  <span class="number">{number}</span>',
                f'  <p>{html.escape(label)}</p>',
                '</article>',
            ]
        )
    return indent_lines(lines, "          ")


def render_catalog_rows(entries: list[CatalogEntry]) -> str:
    lines: list[str] = []
    for entry in entries:
        category_label = CATEGORY_LABELS[entry.category]
        route_parts = [html.escape(category_label)]
        if entry.subcategory:
            route_parts.append(html.escape(entry.subcategory))
        route = "<br>".join(route_parts)
        title = html.escape(entry.title)
        secondary = ""
        if entry.authors_or_name and entry.authors_or_name != entry.title:
            secondary = f"<br>{html.escape(entry.authors_or_name)}"
        year = f"<br>{entry.year}" if entry.year else ""
        lines.extend(
            [
                "<tr>",
                f"  <td><strong>{title}</strong>{secondary}{year}</td>",
                f"  <td>{route}</td>",
                f"  <td>{html.escape(entry.venue)}</td>",
                f"  <td>{render_links(entry.links)}</td>",
                "</tr>",
            ]
        )
    return indent_lines(lines, "              ")


def indent_lines(lines: list[str], prefix: str) -> str:
    return "\n".join(prefix + line for line in lines)


def replace_generated_block(text: str, name: str, generated: str) -> str:
    start = f"<!-- {name}:start -->"
    end = f"<!-- {name}:end -->"
    pattern = re.compile(
        rf"(?P<before>[ \t]*{re.escape(start)})(?P<body>.*?)(?P<after>\n[ \t]*{re.escape(end)})",
        re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        raise ValueError(f"Missing generated block markers for {name}")
    return pattern.sub(f"{match.group('before')}\n{generated}{match.group('after')}", text, count=1)


def sync_index(readme_path: Path = README_PATH, index_path: Path = INDEX_PATH) -> str:
    readme_text = readme_path.read_text(encoding="utf-8")
    index_text = index_path.read_text(encoding="utf-8")
    entries = parse_readme(readme_text)
    if not entries:
        raise ValueError("No README catalog entries were parsed")

    index_text = replace_generated_block(index_text, "catalog-meta", render_hero_meta(entries))
    index_text = replace_generated_block(index_text, "catalog-stats", render_stats(entries))
    index_text = replace_generated_block(index_text, "catalog-table", render_catalog_rows(entries))
    return index_text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if index.html is not synchronized")
    args = parser.parse_args()

    generated = sync_index()
    current = INDEX_PATH.read_text(encoding="utf-8")
    if args.check:
        if generated != current:
            diff = difflib.unified_diff(
                current.splitlines(),
                generated.splitlines(),
                fromfile="index.html",
                tofile="index.html.generated",
                lineterm="",
            )
            print("\n".join(diff))
            return 1
        print("project page is synchronized with README.md")
        return 0

    if generated != current:
        INDEX_PATH.write_text(generated, encoding="utf-8", newline="\n")
        print("updated index.html from README.md")
    else:
        print("index.html already synchronized with README.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())

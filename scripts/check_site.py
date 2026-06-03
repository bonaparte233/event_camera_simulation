#!/usr/bin/env python3
"""Validate the companion repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path

from sync_page import INDEX_PATH, README_PATH, count_public_github_links, parse_readme, sync_index


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "index.html",
    "README.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "assets/site.css",
    "assets/figures/abstract.svg",
    "assets/figures/simulation_framework.svg",
    "assets/figures/realism.svg",
]


def fail(message: str) -> int:
    print(f"site check failed: {message}", file=sys.stderr)
    return 1


def main() -> int:
    for relative_path in REQUIRED_FILES:
        if not (ROOT / relative_path).exists():
            return fail(f"missing required file: {relative_path}")

    readme = README_PATH.read_text(encoding="utf-8")
    entries = parse_readme(readme)
    if len(entries) < 40:
        return fail(f"expected at least 40 README resource entries, found {len(entries)}")

    github_link_count = count_public_github_links(entries)
    if github_link_count < 25:
        return fail(f"expected at least 25 public GitHub links, found {github_link_count}")

    csv_files = sorted((ROOT / "data").glob("*.csv"))
    if csv_files:
        names = ", ".join(path.name for path in csv_files)
        return fail(f"unexpected data files: {names}")

    html = INDEX_PATH.read_text(encoding="utf-8")
    for asset in [
        "assets/site.css",
        "assets/figures/simulation_framework.svg",
        "assets/figures/realism.svg",
    ]:
        if asset not in html:
            return fail(f"index.html does not reference {asset}")

    if re.search(r"\.csv|\.bib|assets/site\.js|href=\"[^\"]*data/", html):
        return fail("index.html references unsupported generated assets")

    if re.search(r"arxiv\.org/abs/(TODO|TBD)|openreview\.net/forum\?id=(TODO|TBD)", html):
        return fail("index.html contains placeholder links")

    generated = sync_index()
    if generated != html:
        return fail("index.html is not synchronized; run python scripts/sync_page.py")

    print(
        "site check passed: "
        f"{len(entries)} README entries, {github_link_count} public GitHub links, "
        f"{len(list((ROOT / 'assets' / 'figures').glob('*.svg')))} figure assets"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

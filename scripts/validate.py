#!/usr/bin/env python3
"""Validate the skill package: frontmatter, naming, links, required files."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = ["SKILL.md", "README.md", "LICENSE"]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"`((?:\.\./)*(?:references|assets)/[A-Za-z0-9_./-]+\.md)`")
FM_RE = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*)$")

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("must start with '---' on line 1")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("frontmatter is not closed with '---'")
    return text[4:end], text[end + 4 :]


def parse_frontmatter(block: str) -> dict[str, str]:
    data: dict[str, str] = {}
    key: str | None = None
    buffer: list[str] = []

    for line in block.splitlines():
        match = FM_RE.match(line)
        if match and not line.startswith((" ", "\t")):
            if key is not None:
                data[key] = " ".join(buffer).strip()
            key = match.group(1)
            value = match.group(2)
            buffer = [] if value in {">", ">-", "|", "|-"} else [value]
        elif key is not None:
            buffer.append(line.strip())

    if key is not None:
        data[key] = " ".join(buffer).strip()
    return data


def check_skill() -> None:
    path = ROOT / "SKILL.md"
    if not path.is_file():
        return

    try:
        block, body = split_frontmatter(path.read_text(encoding="utf-8"))
        meta = parse_frontmatter(block)
    except ValueError as exc:
        fail(f"SKILL.md: {exc}")
        return

    name = meta.get("name", "")
    description = meta.get("description", "")

    if not name:
        fail("SKILL.md: missing 'name'")
    elif not NAME_RE.fullmatch(name):
        fail(f"SKILL.md: name '{name}' must use lowercase letters, digits, and single hyphens")
    elif len(name) > 64:
        fail(f"SKILL.md: name is {len(name)} characters, maximum is 64")
    elif name != ROOT.name:
        fail(f"SKILL.md: name '{name}' does not match folder '{ROOT.name}'")

    if not description:
        fail("SKILL.md: missing 'description'")
    elif not 1 <= len(description) <= 1024:
        fail(f"SKILL.md: description is {len(description)} characters, allowed range is 1-1024")

    if not body.strip():
        fail("SKILL.md: body is empty")


def check_links() -> None:
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        for target in LINK_RE.findall(path.read_text(encoding="utf-8")):
            if not (path.parent / target).resolve().is_file():
                fail(f"{path.relative_to(ROOT)}: broken link `{target}`")


def main() -> int:
    for name in REQUIRED:
        if not (ROOT / name).is_file():
            fail(f"missing required file: {name}")

    check_skill()
    check_links()

    if errors:
        for error in errors:
            print(f"error: {error}")
        return 1

    print(f"ok: {ROOT.name} passed frontmatter, naming, and link checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())

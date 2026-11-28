#!/usr/bin/env python3
"""Validate the skill package: license, frontmatter, naming, links, and cross-file parity."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED = ["SKILL.md", "README.md", "LICENSE"]
CANONICAL_LICENSE_PREFIX = "MIT License"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
BACKTICK_PATH_RE = re.compile(r"`([A-Za-z0-9_./-]+\.(?:md|py|yml|yaml))`")
MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FM_RE = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*)$")
SKILL_HEADING_RE = re.compile(r"^##\s+(\d+)\.\s+", re.MULTILINE)
SKILL_SECTION_REF_RE = re.compile(r"SKILL\.md section (\d+)")
SELF_SECTION_REF_RE = re.compile(r"\bsection (\d+)\b")


def split_frontmatter(text: str) -> tuple[str, str]:
    """Split YAML frontmatter and markdown body from SKILL.md."""
    if not text.startswith("---\n"):
        raise ValueError("must start with '---' on line 1")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("frontmatter is not closed with '---'")
    return text[4:end], text[end + 4 :]


def parse_frontmatter(block: str) -> dict[str, str]:
    """Parse simple key/value and folded scalar fields from YAML frontmatter."""
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


def check_license(root: Path, errors: list[str]) -> None:
    """Verify LICENSE begins with the canonical MIT License header."""
    path = root / "LICENSE"
    if not path.is_file():
        return
    first_line = path.read_text(encoding="utf-8").splitlines()[0:1]
    if not first_line or first_line[0].strip() != CANONICAL_LICENSE_PREFIX:
        errors.append(
            f"LICENSE: line 1 must start with '{CANONICAL_LICENSE_PREFIX}' for standard SPDX detection"
        )


def check_skill(root: Path, errors: list[str]) -> str | None:
    """Validate SKILL.md frontmatter and return body text if readable."""
    path = root / "SKILL.md"
    if not path.is_file():
        return None

    try:
        block, body = split_frontmatter(path.read_text(encoding="utf-8"))
        meta = parse_frontmatter(block)
    except ValueError as exc:
        errors.append(f"SKILL.md: {exc}")
        return None

    name = meta.get("name", "")
    description = meta.get("description", "")

    if not name:
        errors.append("SKILL.md: missing 'name'")
    elif not NAME_RE.fullmatch(name):
        errors.append(
            f"SKILL.md: name '{name}' must use lowercase letters, digits, and single hyphens"
        )
    elif len(name) > 64:
        errors.append(f"SKILL.md: name is {len(name)} characters, maximum is 64")
    elif name != root.name:
        errors.append(f"SKILL.md: name '{name}' does not match folder '{root.name}'")

    if not description:
        errors.append("SKILL.md: missing 'description'")
    elif not 1 <= len(description) <= 1024:
        errors.append(
            f"SKILL.md: description is {len(description)} characters, allowed range is 1-1024"
        )

    if not body.strip():
        errors.append("SKILL.md: body is empty")

    return body


def check_links(root: Path, errors: list[str]) -> None:
    """Verify backticked repo paths and markdown file links resolve cleanly."""
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")

        for target in BACKTICK_PATH_RE.findall(text):
            if target.startswith(("http", "/")) or "*" in target:
                continue
            rel_ok = (path.parent / target).resolve().is_file()
            root_ok = (root / target).resolve().is_file()
            if not (rel_ok or root_ok):
                errors.append(f"{path.relative_to(root)}: broken path reference `{target}`")

        for target in MD_LINK_RE.findall(text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            file_part = target.split("#")[0]
            if file_part and not (path.parent / file_part).resolve().exists():
                errors.append(f"{path.relative_to(root)}: broken markdown link ({target})")


def check_parity(root: Path, skill_body: str | None, errors: list[str]) -> None:
    """Check cross-file section references, rubric scale, and hard-fail parity."""
    if skill_body is None:
        return

    sections = set(SKILL_HEADING_RE.findall(skill_body))
    for sec in SELF_SECTION_REF_RE.findall(skill_body):
        if sec not in sections:
            errors.append(f"SKILL.md: references missing section {sec}")

    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for sec in SKILL_SECTION_REF_RE.findall(text):
            if sec not in sections:
                errors.append(
                    f"{path.relative_to(root)}: references missing SKILL.md section {sec}"
                )

    for rel in ("SKILL.md", "README.md", "assets/scorecard.md"):
        fpath = root / rel
        if not fpath.is_file():
            continue
        content = fpath.read_text(encoding="utf-8")
        if "0-3" not in content or "12/15" not in content:
            errors.append(f"{rel}: expected 0-3 rubric scale and 12/15 gate")

    scorecard_path = root / "assets/scorecard.md"
    if scorecard_path.is_file():
        scorecard_text = scorecard_path.read_text(encoding="utf-8")
        scorecard_fails = len(re.findall(r"^- \[ \] ", scorecard_text, re.MULTILINE))
        hard_fail_block = re.search(
            r"Hard fails, independent of score.*?\n\n(.*?)\n\nHard mode re-verifies",
            skill_body,
            re.DOTALL,
        )
        skill_fails = (
            len(re.findall(r"^- ", hard_fail_block.group(1), re.MULTILINE))
            if hard_fail_block
            else 0
        )
        if scorecard_fails == 0 or scorecard_fails != skill_fails:
            errors.append(
                f"hard-fail parity mismatch: SKILL.md has {skill_fails}, scorecard.md has {scorecard_fails}"
            )


def validate_repo(root: Path) -> list[str]:
    """Run all validation checks against `root` and return any error strings."""
    errors: list[str] = []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f"missing required file: {name}")

    check_license(root, errors)
    skill_body = check_skill(root, errors)
    check_links(root, errors)
    check_parity(root, skill_body, errors)
    return errors


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    errors = validate_repo(root)
    if errors:
        for error in errors:
            print(f"error: {error}")
        return 1

    print(
        f"ok: {root.name} passed license, frontmatter, naming, link, and parity checks"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

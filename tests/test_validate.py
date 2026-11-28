"""Unit tests for scripts/validate.py."""

from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import validate  # noqa: E402


def make_minimal_repo(tmp: Path) -> Path:
    """Create a minimal valid skill repo inside `tmp/rezky-agent-skill`."""
    repo = tmp / "rezky-agent-skill"
    (repo / "assets").mkdir(parents=True)
    (repo / "LICENSE").write_text(
        f"{validate.CANONICAL_LICENSE_PREFIX}\n\nBody.\n", encoding="utf-8"
    )
    (repo / "README.md").write_text(
        "Rubric: 0-3 and gate 12/15.\n", encoding="utf-8"
    )
    (repo / "assets" / "scorecard.md").write_text(
        "# Scorecard\n0-3\n12/15\n\n## Hard fails (mirror of SKILL.md section 7)\n\n"
        "- [ ] Fail one\n- [ ] Fail two\n",
        encoding="utf-8",
    )
    (repo / "SKILL.md").write_text(
        "---\nname: rezky-agent-skill\ndescription: Valid test skill.\n---\n\n"
        "## 5. Phase 3\n\nLabel V/S/A/U.\n\n"
        "## 7. Phase 5\n\nScore 0-3, gate 12/15.\n\n"
        "Hard fails, independent of score:\n\n"
        "- Fail one\n- Fail two\n\n"
        "Hard mode re-verifies three claims.\n",
        encoding="utf-8",
    )
    return repo


class ValidateTests(unittest.TestCase):
    def test_actual_repository_passes(self) -> None:
        self.assertEqual(validate.validate_repo(ROOT), [])

    def test_missing_required_file_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = make_minimal_repo(Path(tmp))
            (repo / "README.md").unlink()
            errors = validate.validate_repo(repo)
            self.assertTrue(any("missing required file: README.md" in e for e in errors))

    def test_custom_license_preamble_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = make_minimal_repo(Path(tmp))
            (repo / "LICENSE").write_text("Custom summary\n", encoding="utf-8")
            errors = validate.validate_repo(repo)
            self.assertTrue(any("LICENSE:" in e for e in errors))

    def test_folder_name_mismatch_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = make_minimal_repo(Path(tmp))
            renamed = Path(tmp) / "other-name"
            shutil.move(str(repo), str(renamed))
            errors = validate.validate_repo(renamed)
            self.assertTrue(any("does not match folder" in e for e in errors))

    def test_broken_link_and_section_ref_fail(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = make_minimal_repo(Path(tmp))
            (repo / "README.md").write_text(
                "0-3 12/15 `references/missing.md` SKILL.md section 99\n",
                encoding="utf-8",
            )
            errors = validate.validate_repo(repo)
            self.assertTrue(any("broken path reference" in e for e in errors))
            self.assertTrue(any("missing SKILL.md section 99" in e for e in errors))

    def test_hard_fail_parity_mismatch_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = make_minimal_repo(Path(tmp))
            (repo / "assets" / "scorecard.md").write_text(
                "0-3\n12/15\n- [ ] Only one\n", encoding="utf-8"
            )
            errors = validate.validate_repo(repo)
            self.assertTrue(any("hard-fail parity mismatch" in e for e in errors))


if __name__ == "__main__":
    unittest.main()

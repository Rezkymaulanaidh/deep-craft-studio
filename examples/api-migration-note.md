# Worked Example: API Migration Note (Hard Gate)

End-to-end trace of how Rezky Agent Skill (RAS) runs on a judged deliverable.

Request: "Write a client-facing migration note explaining how to replace `pkg_resources` in Python 3.12+ with `importlib.metadata` for our team's CLI plugin loader."

## Activation Check

- External or team-wide audience: yes
- Material claims (Python 3.12 stdlib API behavior): yes
- Scope: multi-step synthesis plus code snippet for a shared team doc
- Mode: Hard gate (client/team-facing technical guide; inaccuracies break plugin loading)

## Phase 1: Brief (kept in temp)

1. Audience: Backend engineers migrating a Python 3.12 CLI plugin loader.
2. Success criteria: Every API symbol exists in Python 3.12 stdlib, migration snippet runs cleanly, and error/empty cases are handled.
3. Constraints: Python 3.12+, stdlib only (no new dependencies), markdown format.
4. Known unknowns: Exact entry-point group name used in the team's legacy loader (`mycli.plugins` assumed).
5. Failure modes: Calling Python 3.10-only `entry_points()` dict indexing instead of `.select(group=...)`, or omitting missing-plugin handling.
6. Mode: Hard gate.

## Phase 2 and 3: Evidence Table and Deterministic Checks

Code exception applies: primary docs for the installed version (`Python 3.12` stdlib docs) plus real execution output.

| ID | Claim | Source | Tier | Date | Locator | Supports? | Confidence | Note |
|---|---|---|---|---|---|---|---|---|
| C1 | `pkg_resources` was removed from default Python 3.12 stdlib venvs (`setuptools` no longer preinstalled) | Python 3.12 Release Notes / PEP 632 & `python3 -c "import pkg_resources"` | S1 | 2023-10 | What's New in Python 3.12 + local `python3` exit code | yes | V | Verified by docs + local execution |
| C2 | `importlib.metadata.entry_points(group=...)` returns `EntryPoints` in Python 3.12 | Python 3.12 `importlib.metadata` docs + `python3 -c` snippet | S1 | 2023-10 | `library/importlib.metadata.html#entry-points` + stdout | yes | V | `select(group=...)` also valid; `dict` indexing removed |
| C3 | `ep.load()` raises `ImportError` / `AttributeError` on broken entry points | Local test snippet with mock entry point | S1 | 2026-11 | `/tmp/ras-test.py` run output | yes | V | Tested failure path directly |

## Phase 4: Deliverable

### Migrating Plugin Loading to `importlib.metadata` (Python 3.12+)

Replace `pkg_resources.iter_entry_points` with `importlib.metadata.entry_points(group=...)` from the Python 3.12 standard library.

```python
from importlib.metadata import entry_points


def load_plugins(group: str = "mycli.plugins") -> dict[str, object]:
    """Load registered entry points for `group`, failing loudly on broken targets."""
    loaded: dict[str, object] = {}
    for ep in entry_points(group=group):
        try:
            loaded[ep.name] = ep.load()
        except Exception as exc:
            raise RuntimeError(f"Failed to load plugin {ep.name!r} ({ep.value})") from exc
    return loaded
```

Key behavioral difference: Python 3.12 `entry_points()` no longer supports dictionary-style `entry_points()["group"]` indexing; pass `group=...` or call `.select(group=...)`. Empty groups return an empty `EntryPoints` tuple without raising.

## Phase 5: Scorecard (Summary)

Verifier: separate verifier pass (re-ran snippet and checked Python 3.12 docs).

| Dimension | Score (0-3) | Evidence / locator | Note |
|---|---|---|---|
| Accuracy | 3 | C1-C3 + `python3` execution output | All API calls verified on 3.12 |
| Completeness | 3 | Brief criteria 1-3 met | Failure path & empty group covered |
| Domain craft | 3 | `references/domains/code.md` | Explicit error context, no dead code |
| Structure | 2 | Short 3-part layout | Clear sequence; brief example |
| Traceability | 3 | C1-C3 locators mapped | Reproducible snippet provided |

Total: 14 / 15 (Pass: no `0`, zero Hard Fails, 3-claim spot check passed).

## Output Contract

```text
Assumptions: Entry-point group is named "mycli.plugins"; callers want plugin load errors to fail loudly rather than skip silently.
Verification: 3 V, 0 S, 0 A, 0 U (verified against Python 3.12 importlib.metadata docs and local python3 execution).
Limitations: Covers entry-point discovery and loading only; does not cover pkg_resources resource_filename migration (use importlib.resources).
Next check: Run `python3 -c "from importlib.metadata import entry_points; print(entry_points(group='mycli.plugins'))"` in your project's Python 3.12 environment.
```

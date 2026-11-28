# Scorecard

Fill during Phase 5 (in a fresh verifier subagent when supported, or after running deterministic checks and re-reading raw sources fresh). Every score needs a locator (page, slide, line, file, or command output); a score without evidence is invalid. Score one dimension across the whole artifact before moving to the next; item-by-item scoring inflates the halo effect.

Task:
Mode: hard / advisory
Verifier: subagent / single-agent-clean-reread
Date:

## Scale

- 0 (Broken): missing, broken, or contradicted by evidence (auto-fail).
- 1 (Weak / Partial): major gaps remain; fails craft or verification minimum.
- 2 (Acceptable): meets baseline requirements with minor or single-source gaps.
- 3 (Strong / Verified): thorough, verified with locators or tool output, meets full domain craft minimum.

## Dimensions

| Dimension | Score (0-3) | Evidence / locator / tool output | Note |
|---|---|---|---|
| Accuracy | | | |
| Completeness | | | |
| Domain craft | | | |
| Structure | | | |
| Traceability | | | |

Total: __ / 15
Gate: no zero, total >= 12/15, and zero hard fails. Pass / Fail

## Hard fails (mirror of SKILL.md section 7; SKILL.md wins if they differ)

- [ ] Unresolvable citation, or a citation that does not support the claim
- [ ] Number with no source, or a source that does not support it
- [ ] API, function, or flag absent from the claimed version
- [ ] Missing or mismatched file, line, or figure reference
- [ ] Generated file will not open, or temporary artifacts remain
- [ ] Explicit user requirement unmet
- [ ] Placeholder, TODO, or lorem ipsum in the deliverable
- [ ] Material U claim in hard mode, or a known limitation hidden from the reader

Any checked box is a fail, regardless of total.

Hard mode spot check: re-verify three material claims (prioritizing numbers, citations, and API behavior) from their raw sources or fresh tool runs without consulting notes. Record which three. A failed spot check reopens the audit.

## Defects

| ID | Dimension | Severity | Location | Defect | Fix | Status |
|---|---|---|---|---|---|---|
| | | | | | | |

## Verdict

Pass / Advisory pass / Fail
Residual defects: (list, or "none")

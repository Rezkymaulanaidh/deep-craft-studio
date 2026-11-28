# Iteration Protocol

The audit produces defects. This file decides what happens next, so the loop ends with a verdict instead of endless polishing.

## 1. Defect record

Every defect gets a row:

| ID | Dimension | Severity | Location | Defect | Fix | Status |
|---|---|---|---|---|---|---|
| D1 | Accuracy | blocker | p.4, para 2 | Growth figure has no source | Trace or remove | open |

Severity:
- **Blocker:** hard fail, or a dimension scored 0. Cannot ship.
- **Major:** a dimension scored 1, or keeping total below 12/15. Advisory: ships with disclosure. Hard: ships only if the total still meets the gate (>= 12/15, no 0) and the defect is named in the output contract.
- **Minor:** polish. Fix if budget allows, never at the cost of a blocker.

## 2. Fix order

1. Blockers, cheapest first. A dead citation is a five-minute fix; a broken method may require restructuring.
2. Majors sharing a root cause; fixing one instance usually fixes the rest.
3. Minors only after the gate passes, and only if the fix cannot introduce a new blocker.

Do not fix a major by weakening the claim until it becomes trivially true; that is score inflation with extra steps.

## 3. Progress-bounded round protocol

- **Round 1:** audit (in a fresh verifier subagent if supported), record defects, fix blockers and majors, re-audit.
- **Round 2–3:** only if the gate still fails **and** the prior round reduced open blockers/majors without introducing regressions of the same class.
- **Hard cap:** 3 rounds maximum; after that, report residual defects.

Between rounds, re-run deterministic checks and every check that passed before. Fixes cause regressions: a rewritten paragraph can orphan a citation, a new source can contradict an old one.

## 4. Stop and escalate

Stop and report when any hold:

- The gate passes (`>= 12/15`, no `0`, zero hard fails).
- A round produces zero net progress (defect count/severity does not decrease).
- Fixes are trading one blocker for another of the same class (oscillation — that is a design problem, not a wording problem).
- Three rounds are spent.
- The defect needs information only the user has: private data, access, or a scope decision.

Escalation is a report, not a question dump. One message: what is blocked, why, what you recommend, what you need.

## 5. Residual defect report

When the gate cannot pass, append:

```
Residual defects
- D3 (Accuracy, major): retention figure is single-source (S). Fix requires the internal dashboard export.
- D7 (Completeness, major): competitor pricing covers 3 of 5 named competitors. Two are behind a login.
Verdict: advisory only. Not suitable for external publication as-is.
```

## 6. Anti-patterns

- **Score inflation:** raising a score without changing the artifact.
- **Cosmetic loop:** fixing wording while a blocker remains.
- **Infinite polish:** continuing past 3 rounds or when net progress is zero.
- **Silent downgrade:** removing a claim to pass without telling the reader the scope changed.
- **Audit theater:** filling the scorecard without deterministic checks or raw-source evidence for each score.

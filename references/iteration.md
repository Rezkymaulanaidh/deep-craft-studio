# Iteration Protocol

The audit produces defects. This file decides what happens next, so the loop ends with a verdict instead of endless polishing.

## 1. Defect record

Every defect gets a row:

| ID | Dimension | Severity | Location | Defect | Fix | Status |
|---|---|---|---|---|---|---|
| D1 | Accuracy | blocker | p.4, para 2 | Growth figure has no source | Trace or remove | open |

Severity:
- **Blocker:** hard fail, or a dimension scored 0. The deliverable cannot ship.
- **Major:** a dimension scored 1. In advisory mode it ships with disclosure. In hard mode it ships only if the total still meets the gate, and the defect is named in the output contract.
- **Minor:** polish. Fix if budget allows, never at the cost of a blocker.

## 2. Fix order

1. Blockers, cheapest first. A dead citation is a five-minute fix; a broken method may require restructuring.
2. Majors sharing a root cause. Fixing one instance of a pattern usually fixes the rest.
3. Minors only after the gate passes, and only if the fix cannot introduce a new blocker.

Do not fix a major by weakening the claim until it becomes trivially true. That is score inflation with extra steps.

## 3. Round protocol

- Round 1: audit, record defects, fix blockers and majors, re-audit.
- Round 2: only if the gate still fails. Fix remaining blockers and the majors that keep the total below 8, then re-audit.
- Maximum two rounds. After that, report.

Between rounds, re-run every check that passed before. Fixes cause regressions: a rewritten paragraph can orphan a citation, a new source can contradict an old one.

## 4. Stop and escalate

Stop the loop and report when:

- The gate passes.
- Two rounds are spent.
- The defect needs information only the user has: private data, access, or a scope decision.
- Fixes are trading one blocker for another of the same class. That is a design problem, not a wording problem.

Escalation is a report, not a question dump. One message: what is blocked, why, what you recommend, what you need.

## 5. Residual defect report

When the gate cannot pass, append this to the deliverable:

```
Residual defects
- D3 (Accuracy, major): retention figure is single-source (S). Fix requires the internal dashboard export.
- D7 (Completeness, major): competitor pricing covers 3 of 5 named competitors. Two are behind a login.
Verdict: advisory only. Not suitable for external publication as-is.
```

## 6. Anti-patterns

- **Score inflation:** raising a score to close the loop without changing the artifact.
- **Cosmetic loop:** fixing wording while a blocker remains.
- **Infinite polish:** a third and fourth round on minors.
- **Silent downgrade:** removing a claim to pass the gate without telling the reader the scope changed.
- **Audit theater:** filling the scorecard without evidence for each score.

---
name: rezky-agent-skill
description: >-
  Quality-gated workflow for judged deliverables: papers, reports, articles, slides,
  spreadsheets, multi-file code, and analysis. Adds an activation gate, source-tier
  verification, domain craft minimums, a scored rubric with hard fails, a bounded fix loop,
  and an output contract. Use when at least two hold: an external audience judges the output;
  material claims need evidence beyond common knowledge; the artifact is expensive to reverse;
  scope exceeds one file or ~30 minutes of non-mechanical work. Skip quick answers, single-line
  edits, lookups, and mechanical refactors.
---

# Rezky Agent Skill (RAS)

For work that will be judged: gates that can fail, evidence that can be inspected, and a contract the reader can check.

## 1. Activation gate

Run RAS when **at least two** are true:

- [ ] An external audience judges the output (grader, client, reviewer, users).
- [ ] Material claims need evidence beyond common knowledge (facts, numbers, citations, APIs).
- [ ] The artifact is expensive to reverse: published, sent, deployed, graded.
- [ ] Scope exceeds one file or ~30 minutes of non-mechanical work.

**Exclusions override the gate.** Skip quick factual answers, single-line edits, formatting-only changes, lookups, brainstorming, and mechanical refactors with a passing test suite, even with two boxes checked. If borderline, run Phase 1 and Phase 5 in light mode only.

**Strictness mode**, chosen before work starts:

| Mode | Use when | If the gate fails |
|---|---|---|
| **Hard gate** | Graded/published, legal/financial/medical, irreversible, user says "final" | Cannot declare done; fix loop; residual defects reported. |
| **Advisory** | Internal draft, exploration, time-boxed | Score and disclose; user decides. |

Advisory needs an explicit user signal (internal or exploratory output, or consent to skip the gate); agent uncertainty is not a signal. If the user is unreachable and the artifact is external-facing, default to hard gate and disclose the assumption. If still unreachable, follow section 5 for claims needing private access: cut them or downgrade to a stated A, and record the change in Limitations.

## 2. The loop

Five phases, each with an artifact. Skipping a phase is a decision you must state.

| Phase | Question | Artifact |
|---|---|---|
| 1. Scope | What does good mean, and what would fail? | Brief: audience, success criteria, constraints, unknowns |
| 2. Research | What do we need, and where? | Evidence table (`assets/evidence-table.md`) |
| 3. Verify | Is each material claim true, current, supported? | Verification notes plus confidence labels |
| 4. Build | What is the craft minimum? | The deliverable |
| 5. Audit | Does it pass, and what is broken? | Filled scorecard (`assets/scorecard.md`) plus output contract |

Keep working copies in a system temp directory (`/tmp/ras-*` on Unix, `%TEMP%\ras-*` on Windows), delete them before finishing, never overwrite the templates, and leave no scratch files in the project root.

Load references only when their phase starts; the map is at the end.

## 3. Phase 1 - Scope

Write the brief before searching or drafting. Six lines:

1. Audience and what they will do with the output.
2. Success criteria in checkable terms (e.g., 15 pages, 20 resolvable sources, method reproducible from text alone).
3. Constraints: format, length, deadline, template, tools, language.
4. Known unknowns: what you must guess.
5. Task-specific failure modes: what would make a reviewer reject it.
6. Mode: hard or advisory, with the signal.

If criteria are vague and the user is reachable, ask up to three questions; otherwise state assumptions and proceed (they belong in the output contract).

## 4. Phase 2 - Research

Read `references/research.md` before the first search. Minimum output: an evidence table, one row per material claim: source, tier, date, supports?

Non-negotiables:
- Primary sources before commentary.
- Two independent sources per material claim, at least one S1/S2.
- Code exception: one primary source (docs for the installed version) plus a real execution result from a test or snippet; skip the second source and adversarial search.
- One adversarial search per contested claim: strongest disconfirming evidence.
- Gaps are limited, not a default; cap and escalation in `references/research.md`.
- Stop on coverage, saturation, or budget; a settled feeling is not a stop condition.

## 5. Phase 3 - Verify

Read `references/verification.md`. Verify by claim type, not by vibe:

| Claim type | Check |
|---|---|
| Citation | Resolve the identifier; confirm title, authors, year, and support. |
| Statistic | Trace to the dataset; record period, sample size, unit. |
| API/code | Installed version, its docs, then run it. |
| Benchmark | Conditions, baseline parity, eval harness; no unmatched cross-paper comparisons. |
| Quote | Exact passage; no paraphrase inside quotes. |
| File/line/figure | Open and confirm. |

Anything unverifiable gets a label, not a confident sentence:

- **V** verified: two independent sources, ≥1 S1/S2, locator recorded.
- **S** single-source: one credible source, no corroboration.
- **A** assumption: stated inference, not evidence.
- **U** unverified: unconfirmed. Hard: a material U cannot ship—escalate if reachable; if unreachable and the source needs private or paywalled access, cut it or downgrade to a stated A with narrower scope. Advisory: ships only if named in the contract.

Defined here once; other files refer to this section.

## 6. Phase 4 - Build

Read the domain module before drafting. It defines the craft minimum.

| Domain | Module | Craft minimum in one line |
|---|---|---|
| Papers, reports, articles | `references/domains/academic.md` | Every section advances one claim; methods reproducible from text alone. |
| Slide decks | `references/domains/slides.md` | One takeaway per slide, headline states the claim, detail in notes. |
| Spreadsheets | `references/domains/spreadsheet.md` | Inputs, formulas, and outputs separated; every total traceable to cells. |
| Code | `references/domains/code.md` | Runs from a clean checkout, failure paths handled, no speculative abstraction. |
| Data analysis | `references/domains/analysis.md` | Provenance, method, and uncertainty stated before conclusions. |

Prose rules apply everywhere (`references/anti-slop.md`): behavioral tests (relocation, mechanism, deletion, number), not a phrase blacklist.

## 7. Phase 5 - Audit

Score with `assets/scorecard.md`. Five dimensions, 0-2 each.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Accuracy | Wrong or unsupported material claim | Mostly correct; one weak claim | All material claims verified or labeled/disclosed |
| Completeness | Stated requirement missing | All met; depth uneven | All met; excluded adjacent needs stated |
| Domain craft | Below module minimum | Format met; substance missed | Craft minimum met, with evidence |
| Structure | Argument unreadable | Followable; weak transitions | Every section advances argument; transitions explain sequence |
| Traceability | Claims unchecked | Some sources; inconsistent | Every material claim traceable |

Gate: no dimension scores 0, and total is at least 8/10.

Hard fails, independent of score. Any one blocks completion:

- Unresolvable citation, or one that does not support the claim.
- Number with no source, or a source that does not support it.
- API, function, or flag absent from the claimed version.
- Missing or mismatched file, line, or figure reference.
- Generated file that will not open, or leftover temp artifacts.
- Explicit user requirement unmet.
- Placeholder, TODO, or lorem ipsum in the deliverable.
- Material U claim in hard mode, or a hidden known limitation.

Hard mode re-verifies three material claims (numbers, citations, API behavior) with fresh tool calls—reopen the file, rerun the snippet, or refetch the source—and confirms the deliverable matches the raw source. A failure reopens the audit.

On failure, run `references/iteration.md`: blockers first, re-audit, two rounds maximum. Never raise a score to close a gap; report defects that remain.

## 8. Output contract

End every deliverable with four short blocks:

```
Assumptions: what was inferred, and what would change if wrong.
Verification: V/S/A/U summary; list A assumptions and (advisory) U items explicitly.
Limitations: what this does not cover, and why it matters.
Next check: the single most useful verification the reader should run.
```

Inline work: label only material claims; labeling every sentence is noise.

## 9. Reference map

| File | Load when |
|---|---|
| `references/research.md` | Phase 2, before search |
| `references/verification.md` | Phase 3, or when a claim looks too convenient |
| `references/anti-slop.md` | Phase 4, drafting and self-edit |
| `references/iteration.md` | Phase 5, when the gate fails |
| `references/domains/*.md` | Phase 4, once the artifact type is known |
| `assets/evidence-table.md` | Phase 2 output |
| `assets/scorecard.md` | Phase 5 output |

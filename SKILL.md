---
name: deep-craft-studio
description: >-
  Quality-gated workflow for deliverables that will be judged, published, or shipped, including research
  papers, reports, articles, slide decks, spreadsheets, multi-file code, and data analysis. Adds an
  activation gate, source-tier verification, domain craft minimums, a scored rubric with hard fails, a
  bounded fix loop, and an output contract. Use when at least two of these hold: an external audience will
  judge the output; material claims need evidence outside common knowledge; the artifact is expensive to
  reverse; scope exceeds one file or about 30 minutes of non-mechanical work. Skip quick answers,
  single-line edits, lookups, and mechanical refactors.
---

# Deep Craft Studio

A workflow for work that will be judged. It replaces good intentions ("be thorough", "avoid slop") with gates that can fail, evidence that can be inspected, and a contract the reader can check.

## 1. Activation gate

Run this skill when **at least two** are true:

- [ ] An external audience will judge the output (grader, client, reviewer, production users).
- [ ] Material claims need evidence outside common knowledge (facts, numbers, citations, API behavior).
- [ ] The artifact is expensive to reverse: published, sent, deployed, or graded.
- [ ] Scope exceeds one file or roughly 30 minutes of non-mechanical work.

**Exclusions override the gate.** Do not run this skill for quick factual answers, single-line edits, formatting-only changes, lookups, brainstorming, or mechanical refactors with a passing test suite, even when two boxes are checked. If the task is borderline, run Phase 1 and Phase 5 in light mode only.

**Strictness mode**, decided before work starts:

| Mode | Use when | Consequence of a failed gate |
|---|---|---|
| **Hard gate** | Graded or published work, legal/financial/medical claims, irreversible artifacts, user says "final" | Cannot declare done. Fix loop required. Residual defects reported. |
| **Advisory** | Internal draft, exploration, time-boxed request | Score and disclose. The user decides whether to accept. |

Advisory mode needs an explicit signal: the user says the output is internal or exploratory, or consents to skipping the gate. Agent uncertainty is not a signal. When the user is unreachable and the artifact is external-facing, default to hard gate and disclose that assumption in the contract. If the user stays unreachable, follow section 5 for claims that need private access: cut them or downgrade them to a stated A, and record the change in Limitations.

## 2. The loop

Five phases, each with an artifact. Skipping a phase is a decision you must state out loud.

| Phase | Question | Artifact |
|---|---|---|
| 1. Scope | What does "good" mean here, and what would make it fail? | Brief: audience, success criteria, constraints, unknowns |
| 2. Research | What do we need to know, and where is it? | Evidence table (`assets/evidence-table.md`) |
| 3. Verify | Is each material claim true, current, and actually supported? | Verification notes plus confidence labels |
| 4. Build | What is the craft minimum for this domain? | The deliverable |
| 5. Audit | Does it pass the rubric, and what is still broken? | Filled scorecard (`assets/scorecard.md`) plus output contract |

Working copies of `assets/evidence-table.md` and `assets/scorecard.md` go in a system temp directory such as `/tmp/deep-craft-*`. Delete them before you finish. Never overwrite the templates in `assets/`, and leave no scratch files in the user's project root.

Load reference files only when you reach their phase. The map is at the end.

## 3. Phase 1 - Scope

Write the brief before searching or drafting. Six lines:

1. Audience, and what they will do with the output.
2. Success criteria in checkable terms (e.g., "15 pages, 20 resolvable sources, method reproducible from the text alone").
3. Constraints: format, length, deadline, template, tools, language.
4. Known unknowns: what you would have to guess.
5. Task-specific failure modes: what would make a reviewer reject this.
6. Mode: hard or advisory, with the signal that set it.

If success criteria are vague and the user is reachable, ask up to three questions. If not reachable, state assumptions and proceed; they belong in the output contract.

## 4. Phase 2 - Research

Read `references/research.md` before the first search. Minimum output is an evidence table where every material claim has a row: source, tier, date, and whether the source actually supports it.

Non-negotiables:
- Primary sources before commentary about them.
- Two independent sources for every material claim, at least one from tier S1 or S2.
- Exception for Code: API and library behavior needs one primary source (the docs for the installed version) and a real execution result from a test or snippet. Skip the second source and the adversarial search for that claim.
- One adversarial search per contested claim: look for the strongest disconfirming evidence.
- Gaps are limited, not a default: the cap and escalation rule are in `references/research.md`.
- Stop on coverage, saturation, or budget. A settled feeling is not a stop condition.

## 5. Phase 3 - Verify

Read `references/verification.md`. Verify by claim type, not by vibe:

| Claim type | Check |
|---|---|
| Citation | Resolve the identifier. Confirm title, authors, year, and that the passage supports the claim. |
| Statistic | Trace to the dataset. Record reference period, sample size, unit. |
| API or code behavior | Check the version actually installed, then the docs for that version, then run it. |
| Benchmark | Conditions, baseline parity, eval harness. No cross-paper comparisons without matched settings. |
| Quote | Locate the exact passage. No paraphrase inside quotation marks. |
| File, line, or figure reference | Open it and confirm the content matches the claim. |

Anything that cannot be verified gets a label, not a confident sentence:

- **V** verified: two independent sources, at least one S1/S2, locator recorded.
- **S** single-source: one credible source, no corroboration.
- **A** assumption: stated inference, not evidence.
- **U** unverified: could not confirm. In hard mode a material claim cannot stay U. If the user is reachable, escalate. If the user is unreachable and the source needs private or paywalled access, cut the claim or downgrade it to a stated A with narrower scope. In advisory mode it ships only if named in the contract.

These labels are defined here once. Other files refer to this section.

## 6. Phase 4 - Build

Read the domain module before drafting. It defines the craft minimum for that artifact.

| Domain | Module | Craft minimum in one line |
|---|---|---|
| Papers, reports, articles | `references/domains/academic.md` | Every section advances one claim; methods reproducible from text alone. |
| Slide decks | `references/domains/slides.md` | One takeaway per slide, headline states the claim, detail lives in notes. |
| Spreadsheets | `references/domains/spreadsheet.md` | Inputs, formulas, and outputs are separated; every total is traceable to cells. |
| Code | `references/domains/code.md` | Runs from a clean checkout, failure paths handled, no speculative abstraction. |
| Data analysis | `references/domains/analysis.md` | Provenance, method, and uncertainty stated before conclusions. |

Prose rules apply in every domain: `references/anti-slop.md`. Its tests are behavioral (relocation, mechanism, deletion, number), not a phrase blacklist.

## 7. Phase 5 - Audit

Score with `assets/scorecard.md`. Five dimensions, 0-2 each.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Accuracy | A material claim is wrong or unsupported | Mostly correct, one weak claim | Every material claim verified or explicitly labeled and disclosed |
| Completeness | A stated requirement is missing | All requirements met, depth uneven | All stated requirements met, and the deliverable states which adjacent needs were deliberately excluded |
| Domain craft | Below the module's minimum | Meets format, misses substance | Meets the module's craft minimum, with evidence |
| Structure | Reader cannot follow the argument | Followable, weak transitions | Every section advances the argument, and transitions state why the next section follows |
| Traceability | Claims cannot be checked | Some sources, inconsistent | Every material claim traceable to evidence |

Gate: no dimension scores 0, and the total is at least 8/10.

Hard fails, independent of score. Any one blocks completion:

- A citation that cannot be resolved, or that does not support the claim.
- A number with no source, or a source that does not support it.
- An API, function, or flag that does not exist in the claimed version.
- A file, line, or figure reference that does not exist or does not match.
- A generated file that will not open, or leftover temporary artifacts.
- An explicit user requirement not met.
- Placeholder text, TODO, or lorem ipsum in the deliverable.
- A material claim labeled U in hard mode, or any known limitation hidden from the reader.

Hard mode adds one independent check: re-verify three material claims (prioritizing numbers, citations, and API behaviors) by executing fresh tool calls (re-opening the file, re-running the snippet, or re-fetching the source URL) to confirm the deliverable matches the raw source. A failed spot check reopens the audit.

If the gate fails, run `references/iteration.md`: fix blockers first, re-audit, maximum two rounds. Never raise a score to close a gap. If defects remain after two rounds, report them.

## 8. Output contract

Every deliverable ends with these four blocks. Keep them short; they are not an essay.

```
Assumptions: what was inferred, and what would change if wrong.
Verification: V/S/A/U summary for material claims. List any A assumptions and (in advisory mode) U items explicitly.
Limitations: what this does not cover, and why it matters.
Next check: the single most useful verification the reader should run.
```

For inline work, label only material claims. Labeling every sentence is noise.

## 9. Reference map

| File | Load when |
|---|---|
| `references/research.md` | Phase 2, before the first search |
| `references/verification.md` | Phase 3, and whenever a claim looks too convenient |
| `references/anti-slop.md` | Phase 4, during drafting and the self-edit pass |
| `references/iteration.md` | Phase 5, when the gate fails |
| `references/domains/*.md` | Phase 4, once the artifact type is known |
| `assets/evidence-table.md` | Phase 2 output |
| `assets/scorecard.md` | Phase 5 output |

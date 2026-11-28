---
name: rezky-agent-skill
description: >-
  Quality-gated workflow for judged deliverables: papers, reports, articles, slides,
  spreadsheets, multi-file code, and analysis. Adds an activation gate, source-tier and
  deterministic verification, domain craft minimums, a 0-3 rubric with hard fails, a
  progress-bounded fix loop, and an output contract. Use when at least two hold: an external
  audience judges the output; material claims need evidence beyond common knowledge; the
  artifact is expensive to reverse; scope spans multiple files, >100 lines of non-mechanical
  output, or multi-step synthesis. Skip quick answers, single-line edits, lookups, and
  mechanical refactors.
---

# Rezky Agent Skill (RAS)

For work that will be judged: deterministic checks first, independent verification where possible, evidence that can be inspected, and a contract the reader can check.

## 1. Activation gate

Run RAS when **at least two** are true:

- [ ] An external audience judges the output (grader, client, reviewer, users).
- [ ] Material claims need evidence beyond common knowledge (facts, numbers, citations, APIs).
- [ ] The artifact is expensive to reverse: published, sent, deployed, graded.
- [ ] Scope spans multiple files, >100 lines of non-mechanical output, or multi-step synthesis.

**Exclusions override the gate.** Skip quick factual answers, single-line edits, formatting-only changes, lookups, brainstorming, and mechanical refactors with a passing test suite, even with two boxes checked. If borderline, run Phase 1 and Phase 5 directly from this file in light mode with zero extra reference reads.

**Strictness mode**, chosen before work starts:

| Mode | Use when | If the gate fails |
|---|---|---|
| **Hard gate** | External audience, graded/published/deployed, legal/financial/medical/security-critical, irreversible, or user says "final" | Cannot declare done; run fix loop; report residual defects. |
| **Advisory** | Internal draft, exploration, or user signals "draft", "quick", "explore", or "advisory" | Score and disclose; user decides. |

If the user is unreachable and the deliverable is external-facing with ambiguous intent, default to Hard gate and disclose the assumption.

## 2. The loop

Five phases, each with an artifact. Skipping a phase is a decision you must state.

| Phase | Question | Artifact |
|---|---|---|
| 1. Scope | What does good mean, and what would fail? | Brief: audience, success criteria, constraints, unknowns |
| 2. Research | What do we need, and where? | Evidence table (`assets/evidence-table.md`) |
| 3. Verify | Is each material claim true, current, supported? | Verification notes plus confidence labels |
| 4. Build | What is the craft minimum? | The deliverable |
| 5. Audit | Does it pass, and what is broken? | Filled scorecard (`assets/scorecard.md`) plus output contract |

Keep working copies (Brief, Evidence table, Scorecard) in a system temp directory (`/tmp/ras-*` on Unix, `%TEMP%\ras-*` on Windows), delete them before finishing, never overwrite the templates, and leave no scratch files in the project root. Present only the deliverable and the compact 4-line output contract to the user unless the full audit trail is requested.

To avoid sequential round-trip latency and prompt dilution, load only what the active task needs in one parallel batch when Phase 2 starts (`references/research.md`, `references/verification.md`, and the single matching `references/domains/*.md`). Load `references/anti-slop.md` in Phase 4, and `references/iteration.md` only if Phase 5 fails.

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

Read `references/verification.md`. Run deterministic checks first wherever tools exist (tests, linters, compilers, HTTP/DOI resolution, script math checks), then verify by claim type:

| Claim type | Check |
|---|---|
| Citation | Resolve the identifier; confirm title, authors, year, and support. |
| Statistic | Trace to the dataset; recompute derived numbers; record period, n, unit. |
| API/code | Installed version, its docs, then execute and check failure paths. |
| Benchmark | Conditions, baseline parity, eval harness; no unmatched cross-paper comparisons. |
| Quote | Exact passage; no paraphrase inside quotes. |
| File/line/figure | Open and confirm. |

Anything unverifiable gets a label, not a confident sentence:

- **V** verified: two independent sources, >=1 S1/S2, locator recorded, and backed by observed tool or source output, never model recall alone.
- **S** single-source: one credible source, no corroboration.
- **A** assumption: stated inference, not evidence.
- **U** unverified: unconfirmed. Hard: a material U cannot ship; escalate if reachable. If unreachable and a paywalled S1 source is blocked, never replace it with a weaker S3 blog: keep verified bibliographic metadata plus publisher abstract (`[S1-abstract only]`, labeled **S** with scope limited in Limitations) when sufficient for a bounded claim, or cut or downgrade to a stated **A** if full-text proof is needed. Advisory: ships only if named in the contract.

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

When the runtime supports subagents or separate sessions, delegate Phase 5 Audit (and the Hard-mode spot check) to a fresh verifier agent given only the brief, deliverable, and raw sources, never the builder's notes. In single-agent runtimes, run deterministic checks first and re-read raw sources or command outputs fresh rather than grading from memory or earlier notes.

Score with `assets/scorecard.md`. Five dimensions, 0-3 each:

| Dimension | 0 (Broken) | 1 (Weak / Partial) | 2 (Acceptable) | 3 (Strong / Verified) |
|---|---|---|---|---|
| Accuracy | Wrong or unsupported material claim | Major verification gaps; weak sources | Material claims mostly verified or labeled | All material claims verified (or S/A disclosed) with tool/source output |
| Completeness | Stated requirement missing | Core met; significant depth or edge-case gaps | All stated requirements met | All met, edge cases handled, excluded needs stated |
| Domain craft | Below module minimum | Format met; substance or failure paths weak | Meets domain craft baseline | Craft minimum exceeded with evidence |
| Structure | Argument unreadable | Followable; weak transitions or uneven flow | Clear sequence and transitions | Every section advances argument; zero filler |
| Traceability | Claims unchecked | Some locators; inconsistent mapping | Most material claims traceable | Every material claim mapped to locator or contract |

Gate: no dimension scores `0`, total is at least `12/15`, and zero hard fails are triggered.

Hard fails, independent of score. Any one blocks completion:

- Unresolvable citation, or one that does not support the claim.
- Number with no source, or a source that does not support it.
- API, function, or flag absent from the claimed version.
- Missing or mismatched file, line, or figure reference.
- Generated file that will not open, or leftover temp artifacts.
- Explicit user requirement unmet.
- Placeholder, TODO, or lorem ipsum in the deliverable.
- Material U claim in hard mode, or a hidden known limitation.

Hard mode re-verifies three material claims (numbers, citations, API behavior) with fresh tool calls (reopen the file, rerun the snippet, or refetch the source) and confirms the deliverable matches the raw source. A failure reopens the audit.

On failure, run `references/iteration.md`: blockers first, progress-based stop rule (cap 3 rounds; stop on pass, zero net progress/oscillation, or missing access). Never raise a score to close a gap; report defects that remain.

## 8. Output contract

End every deliverable with four short blocks:

```
Assumptions: what was inferred, and what would change if wrong.
Verification: V/S/A/U summary (plus deterministic checks run); list A and (advisory) U items explicitly.
Limitations: what this does not cover, paywalled/unverified scope, and why it matters.
Next check: the single most useful verification the reader should run.
```

Inline work: label only material claims; labeling every sentence is noise.

## 9. Reference map

| File | Load when |
|---|---|
| `references/research.md` | Phase 2, batched before search |
| `references/verification.md` | Phase 2/3, batched with research |
| `references/domains/*.md` | Phase 2/4, single matching domain |
| `references/anti-slop.md` | Phase 4, drafting and self-edit |
| `references/iteration.md` | Phase 5, only when the gate fails |
| `assets/evidence-table.md` | Phase 2 output template (in temp) |
| `assets/scorecard.md` | Phase 5 output template (in temp) |
| `examples/api-migration-note.md` | Optional worked example for format calibration |

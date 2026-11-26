# Deep Craft Studio

A quality-gated workflow for deliverables that will be judged, published, sent, or shipped. It replaces good intentions ("be thorough", "avoid slop") with gates that can fail, evidence that can be inspected, and a contract the reader can check.

Deep Craft Studio is an agent skill. It activates on medium-to-high-stakes work: research papers, reports, articles, slide decks, spreadsheets, multi-file code, and data analysis. It stays dormant for quick answers, single-line edits, lookups, and mechanical refactors.

## Why it exists

Most "be thorough" advice is uncheckable. A model says it was thorough, the reviewer cannot tell, and the defect ships anyway. Deep Craft Studio turns quality into artifacts you can inspect:

- A brief that defines "good" before any searching or drafting.
- An evidence table where every material claim has a source, tier, date, and a "does it actually support the sentence?" check.
- Verification notes with V / S / A / U confidence labels per claim.
- A scored rubric with hard fails that block completion.
- A bounded fix loop with a maximum of two rounds.
- An output contract that states assumptions, verification status, limitations, and the next check.

## Activation gate

Run the skill when at least two of these hold:

- An external audience will judge the output (grader, client, reviewer, production users).
- Material claims need evidence outside common knowledge (facts, numbers, citations, API behavior).
- The artifact is expensive to reverse: published, sent, deployed, or graded.
- Scope exceeds one file or roughly 30 minutes of non-mechanical work.

Exclusions override the gate. Do not run it for quick factual answers, single-line edits, formatting-only changes, lookups, brainstorming, or mechanical refactors with a passing test suite. If the task is borderline, run Phase 1 and Phase 5 in light mode only.

Strictness mode is decided before work starts:

| Mode | Use when | Consequence of a failed gate |
|---|---|---|
| Hard gate | Graded or published work, legal/financial/medical claims, irreversible artifacts, user says "final" | Cannot declare done. Fix loop required. Residual defects reported. |
| Advisory | Internal draft, exploration, time-boxed request | Score and disclose. The user decides whether to accept. |

Advisory mode needs an explicit signal. Agent uncertainty is not a signal. When the user is unreachable and the artifact is external-facing, default to hard gate and disclose that assumption in the contract.

## The loop

Five phases, each with an artifact. Skipping a phase is a decision you state out loud.

| Phase | Question | Artifact |
|---|---|---|
| 1. Scope | What does "good" mean here, and what would make it fail? | Brief: audience, success criteria, constraints, unknowns |
| 2. Research | What do we need to know, and where is it? | Evidence table (`assets/evidence-table.md`) |
| 3. Verify | Is each material claim true, current, and actually supported? | Verification notes plus confidence labels |
| 4. Build | What is the craft minimum for this domain? | The deliverable |
| 5. Audit | Does it pass the rubric, and what is still broken? | Filled scorecard (`assets/scorecard.md`) plus output contract |

Load reference files only when you reach their phase. The map is at the end of `SKILL.md`.

## Phase 1 - Scope

Write the brief before searching or drafting. Six lines:

1. Audience, and what they will do with the output.
2. Success criteria in checkable terms (for example, "15 pages, 20 resolvable sources, method reproducible from the text alone").
3. Constraints: format, length, deadline, template, tools, language.
4. Known unknowns: what you would have to guess.
5. Task-specific failure modes: what would make a reviewer reject this.
6. Mode: hard or advisory, with the signal that set it.

If success criteria are vague and the user is reachable, ask up to three questions. If not reachable, state assumptions and proceed; they belong in the output contract.

## Phase 2 - Research

Read `references/research.md` before the first search. Minimum output is an evidence table where every material claim has a row: source, tier, date, and whether the source actually supports it.

Non-negotiables:

- Primary sources before commentary about them.
- Two independent sources for every material claim, at least one from tier S1 or S2.
- One adversarial search per contested claim: look for the strongest disconfirming evidence.
- Gaps are limited, not a default: the cap and escalation rule are in `references/research.md`.
- Stop on coverage, saturation, or budget. A settled feeling is not a stop condition.

Source tiers:

| Tier | Definition | Examples |
|---|---|---|
| S1 | Primary or authoritative: produced by the source of the fact | Peer-reviewed papers, standards (ISO, W3C, RFC), official docs, source code, regulatory filings, raw datasets, court records, an organization's own audited report |
| S2 | Credible secondary: interprets or reports S1 with a named method and accountability | Systematic reviews, government statistics portals, outlets with a corrections policy, a vendor's engineering blog about its own product |
| S3 | Weak or derivative: useful as a lead, never as sole support | Wikipedia, aggregators, SEO listicles, conference marketing pages, forum answers, LLM output, undated blog posts |

A claim needs two independent sources, at least one S1 or S2. Independence means a different origin, not two articles citing the same press release.

## Phase 3 - Verify

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
- **U** unverified: could not confirm. In hard mode a material claim cannot stay U; escalate, cut it, or downgrade the claim. In advisory mode it ships only if named in the contract.

These labels are defined here once. Other files refer to this section.

## Phase 4 - Build

Read the domain module before drafting. Each defines the craft minimum for its artifact, not just a format.

| Domain | Module | Craft minimum in one line |
|---|---|---|
| Papers, reports, articles | `references/domains/academic.md` | Every section advances one claim; methods reproducible from text alone. |
| Slide decks | `references/domains/slides.md` | One takeaway per slide, headline states the claim, detail lives in notes. |
| Spreadsheets | `references/domains/spreadsheet.md` | Inputs, formulas, and outputs are separated; every total is traceable to cells. |
| Code | `references/domains/code.md` | Runs from a clean checkout, failure paths handled, no speculative abstraction. |
| Data analysis | `references/domains/analysis.md` | Provenance, method, and uncertainty stated before conclusions. |

Prose rules apply in every domain: `references/anti-slop.md`. Its tests are behavioral (relocation, mechanism, deletion, number), not a phrase blacklist.

## Phase 5 - Audit

Score with `assets/scorecard.md`. Five dimensions, 0 to 2 each.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Accuracy | A material claim is wrong or unsupported | Mostly correct, one weak claim | Every material claim verified or explicitly labeled and disclosed |
| Completeness | A stated requirement is missing | All requirements met, depth uneven | All stated requirements met, and the deliverable states which adjacent needs were deliberately excluded |
| Domain craft | Below the module's minimum | Meets format, misses substance | Meets the module's craft minimum, with evidence |
| Structure | Reader cannot follow the argument | Followable, weak transitions | Every section advances the argument, and transitions state why the next section follows |
| Traceability | Claims cannot be checked | Some sources, inconsistent | Every material claim traceable to evidence |

Gate: no dimension scores 0, and the total is at least 8 out of 10.

Hard fails, independent of score. Any one blocks completion:

- A citation that cannot be resolved, or that does not support the claim.
- A number with no source, or a source that does not support it.
- An API, function, or flag that does not exist in the claimed version.
- A file, line, or figure reference that does not exist or does not match.
- A generated file that will not open, or leftover temporary artifacts.
- An explicit user requirement not met.
- Placeholder text, TODO, or lorem ipsum in the deliverable.
- A material claim labeled U in hard mode, or any known limitation hidden from the reader.

Hard mode adds one independent check: re-verify three randomly chosen material claims from their sources, without consulting your own notes. A failed spot check reopens the audit.

If the gate fails, run `references/iteration.md`: fix blockers first, re-audit, maximum two rounds. Never raise a score to close a gap. If defects remain after two rounds, report them.

## Output contract

Every deliverable ends with these four blocks. Keep them short; they are not an essay.

```
Assumptions: what was inferred, and what would change if wrong.
Verification: V/S/A/U summary for material claims. List U items explicitly.
Limitations: what this does not cover, and why it matters.
Next check: the single most useful verification the reader should run.
```

For inline work, label only material claims. Labeling every sentence is noise.

## Installation

Deep Craft Studio is a skill folder. Install it where your agent reads skills.

### Claude Code

Place the folder in one of these locations:

- Project scope: `.claude/skills/deep-craft-studio/`
- User scope: `~/.claude/skills/deep-craft-studio/`

Then invoke it by name or let the activation gate trigger it.

### OpenCode

Place the folder in one of these locations:

- Project scope: `.opencode/skills/deep-craft-studio/`
- User scope: `~/.config/opencode/skills/deep-craft-studio/`

OpenCode loads skills from these directories automatically.

### Codex

Place the folder in one of these locations:

- Project scope: `.codex/skills/deep-craft-studio/`
- User scope: `~/.codex/skills/deep-craft-studio/`

### Cursor

Place the folder in:

- Project scope: `.cursor/skills/deep-craft-studio/`

### Generic (clone)

```bash
git clone https://github.com/<owner>/deep-craft-studio.git
```

Then point your agent's skill loader at the cloned folder, or copy it into the agent's skill directory.

### Via the skills CLI

If the repository is public, you can install with:

```bash
npx skills add <owner>/deep-craft-studio@deep-craft-studio
```

Because this repository is private by default, use the clone method above or grant access first.

## Repository layout

```
deep-craft-studio/
  SKILL.md                      # entry point and reference map
  README.md                     # this file
  LICENSE                       # usage terms
  references/
    research.md                 # research method
    verification.md             # verification by claim type
    anti-slop.md                # prose quality tests
    iteration.md                # defect and fix loop
    domains/
      academic.md               # papers, reports, articles
      slides.md                 # slide decks
      spreadsheet.md            # spreadsheets
      code.md                   # code
      analysis.md               # data analysis
  assets/
    evidence-table.md           # template: one row per claim
    scorecard.md                # template: 5-dimension scoring
```

## How to use it

1. Load the skill in your agent.
2. Give the agent a judged deliverable task (paper, report, deck, spreadsheet, multi-file code, or analysis).
3. The activation gate decides whether to run. If at least two conditions hold, the agent runs Phase 1 first and writes the brief.
4. The agent proceeds through research, verification, build, and audit, producing the evidence table, verification labels, and scorecard.
5. The deliverable ends with the output contract: assumptions, verification, limitations, next check.

If the task is borderline, the agent runs Phase 1 and Phase 5 in light mode only.

## Reference map

| File | Load when |
|---|---|
| `references/research.md` | Phase 2, before the first search |
| `references/verification.md` | Phase 3, and whenever a claim looks too convenient |
| `references/anti-slop.md` | Phase 4, during drafting and the self-edit pass |
| `references/iteration.md` | Phase 5, when the gate fails |
| `references/domains/*.md` | Phase 4, once the artifact type is known |
| `assets/evidence-table.md` | Phase 2 output |
| `assets/scorecard.md` | Phase 5 output |

## License

This project is released under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International license (CC BY-NC-ND 4.0). In plain terms:

- You may take and use this skill for personal, educational, and reference purposes.
- You must give credit to the original author.
- You may not sell it or use it commercially.
- You may not modify it or redistribute modified versions.
- You may cite it as a reference in your own work.

See `LICENSE` for the full terms.

## Author

Rezkymaulanaidh (GitHub: Rezkymaulanaidh)
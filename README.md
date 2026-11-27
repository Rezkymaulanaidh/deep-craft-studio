# Deep Craft Studio

An agent skill for work that will be judged: research papers, reports, articles, slide decks, spreadsheets, multi-file code, and data analysis. It turns "be thorough" into checks that can fail.

Deep Craft Studio follows the Agent Skills format, so one folder works in Claude Code, OpenCode, Codex, and Cursor.

## What it adds

| Artifact | Purpose |
|---|---|
| Brief | Defines the audience, success criteria, constraints, unknowns, and failure modes before work starts |
| Evidence table | One row per material claim: source, tier, date, and whether the source supports the sentence |
| Confidence labels | V (verified), S (single source), A (assumption), U (unverified) on material claims |
| Scorecard | Five dimensions scored 0 to 2, with a gate at 8/10 and no zero |
| Fix loop | Blockers first, two rounds maximum, with regression checks |
| Output contract | Assumptions, verification summary, limitations, next check |

## Activation

The skill runs when at least two of these hold:

- An external audience will judge the output.
- Material claims need evidence outside common knowledge.
- The artifact is expensive to reverse: published, sent, deployed, or graded.
- Scope exceeds one file or about 30 minutes of non-mechanical work.

Exclusions override the gate: quick factual answers, single-line edits, formatting changes, lookups, brainstorming, and mechanical refactors with a passing test suite. A borderline task gets Phase 1 and Phase 5 in light mode only.

Mode is chosen before work starts:

| Mode | Use when | If the gate fails |
|---|---|---|
| Hard gate | Graded or published work, legal, financial, or medical claims, irreversible artifacts, the user says "final" | Cannot declare done; fix loop required; residual defects reported |
| Advisory | Internal draft, exploration, time-boxed request | Score and disclose; the user decides |

Advisory mode needs an explicit signal from the user. Agent uncertainty does not count.

## Install

Requires an agent that loads `SKILL.md` skills. The CLI method needs Node.js 22.20 or later.

### Skills CLI

```bash
npx skills add Rezkymaulanaidh/deep-craft-studio
```

Add `-g` to install for every project, or `-a claude-code -a opencode` to target specific agents.

### Manual

Clone the repository, then copy the folder into a path your agent reads.

```bash
git clone https://github.com/Rezkymaulanaidh/deep-craft-studio.git
```

| Agent | Project scope | User scope |
|---|---|---|
| Claude Code | `.claude/skills/deep-craft-studio/` | `~/.claude/skills/deep-craft-studio/` |
| OpenCode | `.opencode/skills/deep-craft-studio/` | `~/.config/opencode/skills/deep-craft-studio/` |
| Codex | `.agents/skills/deep-craft-studio/` | `~/.agents/skills/deep-craft-studio/` |
| Cursor | `.cursor/skills/deep-craft-studio/` or `.agents/skills/deep-craft-studio/` | `~/.cursor/skills/deep-craft-studio/` or `~/.agents/skills/deep-craft-studio/` |

Restart the agent after copying if the skill does not appear.

## How it runs

Five phases, each with an artifact:

| Phase | Question | Artifact |
|---|---|---|
| 1. Scope | What does "good" mean here, and what would make it fail? | Brief: audience, success criteria, constraints, unknowns, failure modes, mode |
| 2. Research | What do we need to know, and where is it? | Evidence table (`assets/evidence-table.md`) |
| 3. Verify | Is each material claim true, current, and actually supported? | Verification notes with confidence labels |
| 4. Build | What is the craft minimum for this domain? | The deliverable |
| 5. Audit | Does it pass the rubric, and what is still broken? | Filled scorecard (`assets/scorecard.md`) plus output contract |

Load reference files only when a phase needs them. `SKILL.md` holds the full workflow and the reference map.

## What counts as done

Five dimensions, scored 0 to 2: accuracy, completeness, domain craft, structure, and traceability. The gate requires no zero and a total of at least 8 out of 10.

Eight hard fails block completion regardless of score. They include an unresolvable citation, a number with no source, an API that does not exist in the claimed version, a broken file or line reference, a generated file that will not open, an unmet requirement, placeholder text, and a material claim still labeled U in hard mode. Hard mode also re-verifies three material claims, prioritizing numbers, citations, and API behavior.

If the gate fails, `references/iteration.md` fixes blockers first and allows two rounds. Scores are never raised to close a gap.

## Repository layout

```
deep-craft-studio/
  SKILL.md                      # entry point and reference map
  README.md                     # this file
  LICENSE                       # CC BY-NC-SA 4.0
  .gitignore                    # local artifacts and agent installs
  .github/workflows/validate.yml # CI: runs the validator
  scripts/validate.py           # frontmatter, naming, and link checks
  references/
    research.md                 # source tiers, query ladder, stopping rule
    verification.md             # checks by claim type
    anti-slop.md                # behavioral prose tests
    iteration.md                # defect and fix loop
    domains/
      academic.md               # papers, reports, articles
      slides.md                 # slide decks
      spreadsheet.md            # spreadsheets
      code.md                   # code
      analysis.md               # data analysis
  assets/
    evidence-table.md           # one row per claim
    scorecard.md                # five-dimension scoring
```

## Limits

- The rubric is a judgment aid, not a measurement. Two reviewers can score the same artifact differently.
- The skill reduces common failure modes. It does not make an agent an expert in your field.
- Verification depends on access. Paywalled or offline sources may stay U in advisory mode. Hard mode cuts them or downgrades them to a stated assumption.
- The workflow costs time and tokens. Use advisory mode for drafts where speed matters.
- There is no benchmark yet. The rules come from documented failure modes and inspection, not a controlled trial.

## Validation

```bash
python3 scripts/validate.py
```

The script checks frontmatter, the skill name and folder match, the description length, and every internal reference link. CI runs it on each push.

## Contributing

Contributions are welcome. Open an issue for a bug or a proposed change, or send a pull request for a focused fix. Keep each pull request to one change and state what it fixes.

By contributing, you agree that your contribution is licensed under CC BY-NC-SA 4.0 and that maintainers may merge, update, and improve it. Your name and the change stay in the repository history. Before opening a pull request, run `python3 scripts/validate.py` and make sure it passes.

## License

CC BY-NC-SA 4.0. You may share and adapt this work with attribution for non-commercial purposes. Adaptations must use the same license. See `LICENSE` for the full terms and the contributor clause.

## Author

Rezkymaulanaidh

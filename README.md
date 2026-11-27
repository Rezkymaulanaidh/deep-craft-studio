# Rezky Agent Skill (RAS)

Formerly Deep Craft Studio.

An agent skill for work that will be judged: research papers, reports, articles, slide decks, spreadsheets, multi-file code, and data analysis. It turns "be thorough" into checks that can fail.

RAS follows the Agent Skills format, so one folder works in Claude Code, OpenCode, Codex, and Cursor.

## What it adds

| Artifact | Purpose |
|---|---|
| Brief | Audience, success criteria, constraints, unknowns, failure modes, mode |
| Evidence table | One row per material claim: source, tier, date, support |
| Confidence labels | V (verified), S (single source), A (assumption), U (unverified) |
| Scorecard | Five dimensions, 0-2; gate at 8/10 and no zero |
| Fix loop | Blockers first, two rounds maximum, regression checks |
| Output contract | Assumptions, verification summary, limitations, next check |

## Activation

Run when at least two hold:

- An external audience judges the output.
- Material claims need evidence beyond common knowledge.
- The artifact is expensive to reverse: published, sent, deployed, graded.
- Scope exceeds one file or ~30 minutes of non-mechanical work.

Exclusions override the gate: quick factual answers, single-line edits, formatting changes, lookups, brainstorming, and mechanical refactors with a passing test suite. A borderline task gets Phase 1 and Phase 5 in light mode only.

Mode is chosen before work starts:

| Mode | Use when | If the gate fails |
|---|---|---|
| Hard gate | Graded/published, legal, financial, or medical claims, irreversible artifacts, user says "final" | Cannot declare done; fix loop; residual defects reported |
| Advisory | Internal draft, exploration, time-boxed request | Score and disclose; user decides |

Advisory needs an explicit user signal. Agent uncertainty does not count.

## Install

Requires an agent that loads `SKILL.md` skills. The CLI method needs Node.js 22.20 or later.

### Skills CLI

```bash
npx skills add Rezkymaulanaidh/rezky-agent-skill
```

Add `-g` for every project, or `-a claude-code -a opencode` to target agents.

### Manual

Clone the repository, then copy the folder into a path your agent reads.

```bash
git clone https://github.com/Rezkymaulanaidh/rezky-agent-skill.git
```

| Agent | Project scope | User scope |
|---|---|---|
| Claude Code | `.claude/skills/rezky-agent-skill/` | `~/.claude/skills/rezky-agent-skill/` |
| OpenCode | `.opencode/skills/rezky-agent-skill/` | `~/.config/opencode/skills/rezky-agent-skill/` |
| Codex | `.agents/skills/rezky-agent-skill/` | `~/.agents/skills/rezky-agent-skill/` |
| Cursor | `.cursor/skills/rezky-agent-skill/` or `.agents/skills/rezky-agent-skill/` | `~/.cursor/skills/rezky-agent-skill/` or `~/.agents/skills/rezky-agent-skill/` |

Restart the agent if the skill does not appear.

## How it runs

Five phases, each with an artifact:

| Phase | Question | Artifact |
|---|---|---|
| 1. Scope | What does good mean, and what would fail? | Brief: audience, success criteria, constraints, unknowns, failure modes, mode |
| 2. Research | What do we need, and where? | Evidence table (`assets/evidence-table.md`) |
| 3. Verify | Is each material claim true, current, supported? | Verification notes with confidence labels |
| 4. Build | What is the craft minimum? | The deliverable |
| 5. Audit | Does it pass, and what is broken? | Filled scorecard (`assets/scorecard.md`) plus output contract |

Load references only when a phase needs them. `SKILL.md` holds the full workflow and the reference map.

## What counts as done

Five dimensions, scored 0-2: accuracy, completeness, domain craft, structure, traceability. The gate requires no zero and at least 8/10.

Eight hard fails block completion regardless of score: an unresolvable citation, a number with no source, an API absent from the claimed version, a missing or mismatched file/line/figure reference, a generated file that will not open, an unmet requirement, placeholder text, and a material U claim in hard mode or a hidden limitation. Hard mode also re-verifies three material claims, prioritizing numbers, citations, and API behavior.

If the gate fails, `references/iteration.md` fixes blockers first and allows two rounds. Scores are never raised to close a gap.

## Repository layout

```
rezky-agent-skill/
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
- RAS reduces common failure modes. It does not make an agent an expert in your field.
- Verification depends on access. Paywalled or offline sources may stay U in advisory mode. Hard mode cuts them or downgrades them to a stated assumption.
- The workflow costs time and tokens. Use advisory mode when speed matters; RAS is compressed, but it is still heavier than a quick answer.
- There is no benchmark yet. The rules come from documented failure modes and inspection, not a controlled trial.

## Validation

```bash
python3 scripts/validate.py
```

The script checks frontmatter, the skill name and folder match, description length, and every internal reference link. CI runs it on each push.

## Contributing

Contributions are welcome. Open an issue for a bug or a proposed change, or send a pull request for a focused fix. Keep each pull request to one change and state what it fixes.

By contributing, you agree that your contribution is licensed under CC BY-NC-SA 4.0 and that maintainers may merge, update, and improve it. Your name and the change stay in the repository history. Before opening a pull request, run `python3 scripts/validate.py`.

## License

CC BY-NC-SA 4.0. You may share and adapt this work with attribution for non-commercial purposes. Adaptations must use the same license. See `LICENSE` for the full terms and the contributor clause.

## Author

Rezkymaulanaidh

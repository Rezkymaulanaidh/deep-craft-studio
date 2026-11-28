# Rezky Agent Skill (RAS)

Formerly Deep Craft Studio.

An agent skill for work that will be judged: research papers, reports, articles, slide decks, spreadsheets, multi-file code, and data analysis. It turns "be thorough" into deterministic checks, independent review hooks, and gates that can fail.

RAS follows the Agent Skills format, so one folder works in Claude Code, OpenCode, Codex, and Cursor.

## What it adds

| Artifact | Purpose |
|---|---|
| Brief | Audience, success criteria, constraints, unknowns, failure modes, mode |
| Evidence table | One row per material claim: source, tier, date, support |
| Confidence labels | V (verified), S (single source), A (assumption), U (unverified) |
| Scorecard | Five dimensions, 0-3; gate at 12/15 and no zero |
| Fix loop | Blockers first, progress-bounded (up to 3 rounds), regression checks |
| Output contract | Assumptions, verification summary, limitations, next check |

## Activation

Run when at least two hold:

- An external audience judges the output.
- Material claims need evidence beyond common knowledge.
- The artifact is expensive to reverse: published, sent, deployed, graded.
- Scope spans multiple files, >100 lines of non-mechanical output, or multi-step synthesis.

Exclusions override the gate: quick factual answers, single-line edits, formatting changes, lookups, brainstorming, and mechanical refactors with a passing test suite. A borderline task runs Phase 1 and Phase 5 in light mode directly from `SKILL.md`.

Mode is chosen before work starts:

| Mode | Use when | If the gate fails |
|---|---|---|
| Hard gate | External audience, graded/published/deployed, legal/financial/medical/security-critical, irreversible, user says "final" | Cannot declare done; fix loop; residual defects reported |
| Advisory | Internal draft, exploration, or user signals "draft", "quick", "explore", "advisory" | Score and disclose; user decides |

If intent on an external-facing deliverable is ambiguous, default to Hard gate and disclose the assumption.

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

Five phases, each with an artifact (stored in temp so project roots stay clean):

| Phase | Question | Artifact |
|---|---|---|
| 1. Scope | What does good mean, and what would fail? | Brief: audience, success criteria, constraints, unknowns, failure modes, mode |
| 2. Research | What do we need, and where? | Evidence table (`assets/evidence-table.md`) |
| 3. Verify | Is each material claim true, current, supported? | Verification notes with deterministic checks and V/S/A/U labels |
| 4. Build | What is the craft minimum? | The deliverable |
| 5. Audit | Does it pass, and what is broken? | Filled scorecard (`assets/scorecard.md`) plus output contract |

Load only the active task's references in one batch (`references/research.md`, `references/verification.md`, and one `references/domains/*.md`). `SKILL.md` holds the full workflow and reference map, and `examples/api-migration-note.md` shows an end-to-end worked example.

## What counts as done

Five dimensions, scored 0-3: accuracy, completeness, domain craft, structure, traceability. The gate requires no zero and at least 12/15.

Eight hard fails block completion regardless of score: an unresolvable citation, a number with no source, an API absent from the claimed version, a missing or mismatched file/line/figure reference, a generated file that will not open (or leftover temp artifacts), an unmet requirement, placeholder text, and a material U claim in hard mode or a hidden limitation.

To reduce self-verification bias, run deterministic checks (tests, linters, HTTP/file checks, script calculations) before scoring, and delegate Phase 5 Audit + the 3-claim hard-mode spot check to a fresh verifier subagent when the runtime supports it.

If the gate fails, `references/iteration.md` fixes blockers first and stops on pass, oscillation/zero net progress, or after at most 3 rounds. Scores are never raised to close a gap.

## Repository layout

```
rezky-agent-skill/
  SKILL.md                       # entry point and reference map
  README.md                      # this file
  LICENSE                        # CC BY-NC-SA 4.0
  .gitignore                     # local artifacts and agent installs
  .github/workflows/validate.yml # CI: runs validator and unit tests
  scripts/validate.py            # frontmatter, naming, link, and parity checks
  tests/test_validate.py         # deterministic tests for the validator
  evals/                         # local LLM behavioral evaluation cases
  examples/                      # end-to-end worked example
  references/
    research.md                  # source tiers, query ladder, stopping rule
    verification.md              # checks by claim type + deterministic checks
    anti-slop.md                 # behavioral prose tests
    iteration.md                 # defect and progress-bounded fix loop
    domains/
      academic.md                # papers, reports, articles
      slides.md                  # slide decks
      spreadsheet.md             # spreadsheets
      code.md                    # code
      analysis.md                # data analysis
  assets/
    evidence-table.md            # one row per claim
    scorecard.md                 # five-dimension 0-3 scoring
```

## Limits and design tradeoffs

- **Self-audit is not independent proof:** An LLM checking its own prose in the same context shares correlated errors. RAS mitigates this with deterministic tool checks first and verifier subagent delegation where available, but cannot eliminate model error when running single-agent without tools.
- **Process is not substance:** Passing a checklist or filling an evidence table does not guarantee good judgment; `V` labels and `12/15` scores still require the reader to verify the `Next check` for high-stakes decisions.
- **Paywalled S1 sources:** Never trade a paywalled S1 paper for a low-tier open blog just because it is crawlable. Hard mode retains verified metadata + publisher abstracts (`S`, scoped in `Limitations`) or escalates for access.
- **Prompt budget and latency:** Loading references adds tokens and tool calls; batch-loading only the needed domain file and keeping `SKILL.md` light-mode capable minimizes overhead.
- **Validation vs live LLM evals:** CI runs deterministic structural and parity tests (`scripts/validate.py`, `tests/test_validate.py`) with zero external API keys; behavioral LLM compliance cases live in `evals/` for local runs.

## Validation

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

The validator checks `LICENSE`, frontmatter, the skill name and folder match, description length, internal references, and cross-file section/rubric parity. CI runs both commands on every push and pull request.

## Contributing

Contributions are welcome. Open an issue for a bug or a proposed change, or send a pull request for a focused fix. Keep each pull request to one change and state what it fixes.

By contributing, you agree that your contribution is licensed under CC BY-NC-SA 4.0 and that maintainers may merge, update, and improve it. Your name and the change stay in the repository history. Before opening a pull request, run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`.

## License

CC BY-NC-SA 4.0. You may share and adapt this work with attribution for non-commercial purposes. Adaptations must use the same license. See `LICENSE` for the full terms and Contributing above for contributor terms.

## Author

Rezkymaulanaidh

# Behavioral Evaluations (Local)

`scripts/validate.py` and `tests/test_validate.py` verify structural and cross-file parity deterministically in CI without API keys. This folder holds adversarial **behavioral** cases (`cases.json`) to test whether an LLM agent actually follows `SKILL.md` in practice.

## Running locally

Feed each prompt in `cases.json` to your target agent (Claude Code, OpenCode, Codex, or Cursor) with `rezky-agent-skill` loaded, and check the output against `must_do` and `must_not_do`.

## Cases

1. `activation-exclusion-vs-hard-gate`: Ensures trivial edits skip RAS while multi-file external specs trigger Hard gate.
2. `fabricated-citation-trap`: Ensures the agent does not invent a DOI or label a claim `V` from memory alone.
3. `paywalled-s1-no-downgrade-to-s3`: Ensures a paywalled IEEE/journal source is not replaced by an unvetted open blog.
4. `prompt-injection-in-source`: Ensures instructions embedded inside fetched content are treated as data and reported, not executed.
5. `code-deterministic-check`: Ensures code claims run against the installed version before receiving `V` and follow the 1/2/3-use abstraction rule.

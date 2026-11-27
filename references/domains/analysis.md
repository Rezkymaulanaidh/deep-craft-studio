# Domain: Data Analysis

Applies to exploratory analysis, dashboards, quantitative reports, and model evaluation.

## 1. Before analysis

- State the question in a form data can answer. "Is churn related to support latency?" is answerable; "improve retention" is not.
- Record provenance: source system, extraction date, filters, row count, known gaps.
- State the unit of analysis (user, session, order, day); mixing units silently invalidates totals.
- Inspect before modeling: missingness by column, duplicates, date ranges, outliers, impossible values.

## 2. Method statement

Every analysis states:

1. What was measured and how.
2. Which test or model, and why that one.
3. Assumptions it requires, and whether they hold.
4. Alternative explanations considered.
5. What would change the conclusion.

Correlation is not causation. If the design cannot support a causal claim, write "associated with" and say what design would be needed.

## 3. Uncertainty

- Report confidence intervals or error bars, not just point estimates.
- Report n; a percentage without a denominator is not a result.
- Distinguish statistical from practical significance; with large n, trivial effects become significant.
- Run a sensitivity check: does the conclusion survive dropping outliers, changing the window, or another defensible specification?
- Multiple comparisons inflate false positives; correct for them or label the analysis exploratory.

## 4. Presentation

- Lead with the finding, then method, then caveats.
- One chart per question; label axes, units, period.
- Show the baseline; 40% conversion means nothing without the prior rate or a comparison group.
- Bar charts start at zero. Line charts may use a non-zero baseline when variation matters; label it and state why. Never truncate an axis to manufacture drama.
- Keep the analysis script and the data snapshot or query; a result that cannot be reproduced is a claim.

## 5. Failure modes

- Survivorship bias: only successful cases reach the sample.
- Simpson's paradox: an aggregate trend reverses within groups.
- Cherry-picked windows that start or end at convenient dates.
- p-hacking: many specifications tested, the significant one reported.
- Leakage: features that contain the outcome.
- Unsourced external numbers mixed with measured internal data.
- "Significant" used without a test.

## 6. Verification before delivery

- Recompute the headline number a second way.
- Check that every chart's n matches the text.
- Confirm the conclusion follows from the reported statistics, not the narrative.
- Confirm the script runs end to end on the stated input.

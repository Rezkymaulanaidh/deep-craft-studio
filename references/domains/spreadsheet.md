# Domain: Spreadsheets

Applies to `.xlsx`, `.csv`, models, dashboards, and trackers.

## 1. Structure

- Separate three layers: inputs (raw data), calculations, outputs. One sheet per layer, or clearly marked blocks.
- Inputs are the only place with hardcoded values. Calculations reference cells instead of retyping numbers.
- One row per record, one column per field, header in row 1. No merged cells inside data ranges.
- Named ranges for anything referenced across sheets.

## 2. Formulas

- No magic numbers inside formulas. Put constants in a labeled input cell.
- Prefer explicit ranges over whole-column references when the sheet will grow.
- Guard division by zero and check for numbers stored as text.
- Every total is traceable: the formula shows what it sums, and the range covers exactly the intended rows.
- Keep one formula pattern down a column. A divergent row is a bug until proven otherwise.

## 3. Verification

- Recompute key totals by a second method: SUM versus pivot versus a manual sample.
- Reconcile row counts: source rows, loaded rows, included rows.
- Spot-check five random rows against the source.
- Check that formatting does not hide values: custom formats, white text, hidden columns.
- Recalculate after edits. Stale cached values are a real failure in generated files.
- Open the file in the target application, not only the library that wrote it.

## 4. Presentation

- Freeze the header row and key columns.
- Number formats state the unit, decimals, thousands separators, and dates as dates.
- Conditional formatting only for exceptions the reader must act on.
- A summary sheet states source, extraction date, row count, and definitions of derived fields.

## 5. Failure modes

- Hardcoded values inside formulas.
- Totals whose range misses the last rows.
- Dates stored as text.
- Duplicate rows from a join.
- Hidden columns or filtered rows that make a total look smaller.
- A dashboard that reads cached values and never refreshes.
- Mixed units across columns: currency, thousands, percentages.

## 6. Verification before delivery

- The file opens and recalculates in the target application.
- Every total has a stated range and a second-method check.
- Row counts reconcile.
- The summary sheet lists source, date, and definitions.
- No hidden or filtered data changes a headline number.

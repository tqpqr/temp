# JEET — complete 20-workbook worksheet-level comparison (audit 05)

User provenance: the repository owner personally downloaded/compiled these from official statistics. **Official provenance is user-confirmed**; individual issuing agency and methodological footnotes have not yet been independently identified from workbook metadata.

Baseline Git tree: `373a14b4fe725329c050ca45a8db723d304766e5`.

## What was read
All 20 XLSX files in jeet/2016–2021 were fetched as binary, unpacked and all seven `xl/worksheets/sheetN.xml` members compared byte-for-byte within and between workbooks using stable byte fingerprints and matching byte lengths. First-row metric labels were read directly.

Results:
- All 20 books have 7 worksheets (140 XML worksheet objects).
- Within every book, **sheet1.xml and sheet2.xml are byte-identical**. Do not count them as independent samples.
- In 2018, `national_map (3).xlsx` and `national_map exp.xlsx` contain identical worksheet XML for **all seven sheets**, as do `national_map.xlsx` and `national_map empl.xlsx`. Entire ZIP container equivalence is *not* asserted (Git SHA differs).
- For each year, sheets 4–7 are byte-identical across that year's separate exp/empl/pay exports.
- Classification yields 18 logical year × selected-metric exports: `Expenditures Per Capita`, `Employees Per 10k Residents`, `Average Pay` for six years, plus 2 redundant 2018 exports at worksheet-content level. None of the source files should be removed.
- First three sheets across representative workbooks hold 51 geographic rows (50 states + DC); the data are function-coded `Corrections`. The other 4 sheets are single-value aggregates.

## Potential source anomaly
The `Total Employees` aggregate sheet in both 2016 and 2017 has identical XML bytes (value 714102); likewise `Monthly Total Employee Pay` (value 4290.5129068035785). This may be source data timing, stale export, or legitimate revision convention; do not presume a specific cause. Before doing time-series inference, inspect agency notes and corresponding 51 state values.

## Interpretation safeguards
- State-year government function `Corrections` is not automatically an institution-level prison budget or prison staffing count.
- Units and definitions of pay and expenditure remain source-documentation checks.
- XML equality proves equality of stored worksheet content. It does not prove separate original files are byte-identical as ZIP containers.
- Compact fingerprints are a screening method, not cryptographic hashes. Exact byte checks would be preferred for formal proof.

## Preservation
This note is an additive catalogue artifact only. Existing repository files have not been edited, moved, deleted, or overwritten.

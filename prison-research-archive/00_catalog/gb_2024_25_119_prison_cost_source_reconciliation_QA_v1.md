# 2024/25 prison-cost original source reconciliation — v1 (14 Oct 2026)

## Source and extraction
- Original preserved ODS: `GB/costs-per-prison-place-prisoner-individual-prison-2024-25.ods`
- Git blob SHA-1: `f30558ca485065dfe3802ff52a3eb255d0a5ed0b`
- `T3_Cost_by_Establishment`: **119 source prison institution rows**, categorised into **nine verified prison-function categories** (8 + 50 + 5 + 3 + 6 + 2 + 2 + 31 + 12). Original numbered row and values are reproduced without transformation in [119-source-row catalogue](gb_2024_25_119_establishments_cost_population_source_values_v1.csv).
- Nine category `Totals` rows were **excluded** from per-prison extraction and preserved in unchanged original ODS.
- No missing or nonnumeric values among the eight required numeric source columns in those 119 rows.
- Underlying Ministry of Justice/HMPPS official publication summary, issued **26 March 2026**: https://assets.publishing.service.gov.uk/media/69bbeea2f7b1c24d8e23ce44/costs-per-place-costs-per-prisoner-2024-2025-summary.pdf . This is the **published PDF summary**, not a proven byte-identical URL for this archived ODS.

## Original 119-source-row addition vs published Table 2a aggregate

The fiscal-year `T2_Summary_Comparison` original row 5 says "2024-25 Totals". For each variable:

| Quantity | Sum of 119 establishment source cells | Original Table 2a published aggregate | Raw difference (sum − aggregate) |
|---|---:|---:|---:|
| Certified Normal Accommodation (places) | 83462 | 83460 | +2 |
| Average Population (prisoners, annual average) | 87009 | 87009 | 0 |
| Direct Resource Expenditure (GBP) | 3292840595 | 3292840592 | +3 |
| Overall Resource Expenditure (GBP) | 4926302568 | 0 | +4926302568 |

Small differences are consistent with the **source's own explicit rounding note**: averages and expenditure figures are rounded to nearest integer; totals come from unrounded components. They are not evidence of missing prisons, but exact accounting verification beyond these cells is outstanding. **Never force-sum-adjust establishment source rows to match totals.**

## Denominator and comparability limits

- Annual `Average Population` differs from a single-month or single-day prison-population stock. `Certified Normal Accommodation` differs from operational capacity.
- The separate yearly category `Notes_to_T3` explicitly records operational/site/classification changes and warns that public/contracted comparisons differ in financial coverage.
- The source has annual direct and overall expenditure; **do not add those columns** — overall already encompasses broader cost allocations.
- In 2018/19, separate original/restated tables document £129,111,488 education/training attribution revision: must preserve that accounting break in any cross-year series.

This is a full source-row-level **archival extraction**, not a claimed causal cost analysis nor a harmonized longitudinal institution panel. The source and prior tables are unchanged.

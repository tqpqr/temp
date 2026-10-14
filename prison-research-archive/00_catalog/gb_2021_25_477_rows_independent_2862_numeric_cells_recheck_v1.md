# Independent recheck of UK financial prison-year panel source cells — 14 October 2026

This audit **re-fetched four original .ods source books** from the unchanged root `GB/` files and compared every previously archived FY2021/22–FY2024/25 observation with the actual original ZIP-derived `T3_Cost_by_Establishment` original worksheet. This is independent of the source transcriptions that generated the original 477-row CSV.

Comparison target: `prison-research-archive/00_catalog/gb_cost_FY2021_25_477_unharmonized_establishment_year_rows_v1.csv`, 477 original facility×FY records.

## Integrity results

| FY | Source book Git blob SHA-1 | Establishments | Numeric checks |
|---|---|---:|---:|
| 2021/22 | `f7d847c3477e3fcc3e4e563b723cfa00cda3e310` | 119 | 714 |
| 2022/23 | `5634ad084c85b8168eff2bf5a952e42012c383bc` | 119 | 714 |
| 2023/24 | `4df76a9c07f3cf8431993b1c4daac205549fd0de` | 120 | 720 |
| 2024/25 | `f30558ca485065dfe3802ff52a3eb255d0a5ed0b` | 119 | 714 |
| **Total** | 4 separately re-fetched source originals | **477** | **2,862** |

- Matched all 477 entries to their **exact original sheet row numbers**, without sorting by prison name.
- Re-examined original prison name for every row: **0 discrepancies**, including no duplicated original names within a financial year.
- Six fields independently checked on each row: Certified Normal Accommodation (CNA), Annual Average Population, Direct Resource Expenditure GBP, Direct Cost per Prisoner GBP, Overall Resource Expenditure GBP, Overall Cost per Prisoner GBP. Original columns **B, C, D, F, H, J** respectively.
- Parsed **2,862/2,862 original numeric values**, **0 mismatches**, **0 nonnumeric or missing source cells** among those 477 rows.
- Rows in the original `T3` worksheets: **193, 195, 196, 195** respectively, including header, classification, source-note and category-total rows, distinct from 477 real institution-year entries.

**Verification status:** transcription/read accuracy for these selected six original numerical columns is now independently verified. This does **not** prove longitudinal prison identity, constant prison functions, balanced observation windows, source revisions, public/private comparability or exact denominator before source rounding. Remaining source columns E and I (per-place amounts) and category totals should also be audited for 2021–2024 if used.

**No analysis panel was created.** We deliberately retain original spelling, category and year and do not zero-fill, impute or smooth. Unit costs per prisoner should not be reconstructed as integer expenditure / rounded published whole-number mean population; HMPPS calculations use a finer denominator and rounded reported costs (see 2024/25 independent 952-cell check).

This file is add-only. Original `GB/` documents, 477-row CSV, and all previous audit versions remain unchanged.

# 2024/25 UK prison-cost source reconciliation — corrected v2 (14 Oct 2026)

**This corrected v2 supersedes v1.** The v1 QA note had one indexing error: the actual original `T2_Summary_Comparison` source row 5 has an *empty spacer column G*, so `Overall Resource Expenditure` is **H5** (ODS zero-index 7), not G5 (zero-index 6). The v1 error was only in this derivative QA note. The original ODS and the extracted 119 prison records were never changed. Their overall resource expenditure values correctly use source H.

Original `GB/costs-per-prison-place-prisoner-individual-prison-2024-25.ods` Git blob SHA-1 `f30558ca485065dfe3802ff52a3eb255d0a5ed0b`, fiscal 2024/25.

## Exactly validated extraction
- Source sheet `T3_Cost_by_Establishment`, 119 *real establishment rows* across **nine** prison functions, with published function counts **8+50+5+3+6+2+2+31+12=119**, plus nine clearly labeled separate `Totals` rows *excluded*.
- Eight primary original numeric columns per institution (CNA, annual-average population, direct expenditure and direct per-unit costs, overall expenditure and overall per-unit costs) were all present and numeric.
- [Per-establishment original row/cell index](gb_2024_25_119_establishments_cost_population_source_values_v1.csv) records the original source row and source-cell positions (CNA column B, population C, direct expenditure D, overall expenditure **H**).
- [All 22 original cost workbooks, 102 worksheet records](gb_cost_original_22_spreadsheets_102_worksheets_v2.csv).

## Correct 119-row sums versus the HMPPS published Table 2a aggregate, row 5

| Variable | Source original sum of 119 | Source Table 2a original national total | Difference |
|---|---:|---:|---:|
| Certified Normal Accommodation (places) | 83,462 | 83,460 (B5) | +2 |
| Average Population (annual average) | 87,009 | 87,009 (C5) | 0 |
| Direct Resource Expenditure, GBP | 3,292,840,595 | 3,292,840,592 (D5) | +3 |
| Overall Resource Expenditure, GBP | 4,926,302,568 | 4,926,302,564 (**H5**) | +4 |

The source `Notes_to_T3` expressly says individual establishment averages and expenditures were rounded to nearest integer and aggregate totals were computed from unrounded data. Do **not** overwrite extracted source cells with a balancing residual. Nor should these small deviations be presented as evidence of missing institutions.

## Important units and financial methodology
- HMPPS prison population denominator for FY 2024/25 is **annual average population**, not the monthly bulletin's one-day value. CNA is *certified normal accommodation*, **not operational capacity**.
- Direct expenditure and overall expenditure are **alternative accounting scopes**, not two amounts to add.
- Original `Notes_to_T3` reports establishment changes and cautions private-vs-public spending coverage differs.
- Cross-year direct spending has at least one historical accounting break: original/restated FY2018/19 reallocation of education/training expenditure **GBP 129,111,488**.

Official MoJ/HMPPS summary PDF (published March 26, 2026): https://assets.publishing.service.gov.uk/media/69bbeea2f7b1c24d8e23ce44/costs-per-place-costs-per-prisoner-2024-2025-summary.pdf . **This is a verified official publication summary, not a proven identical-byte external URL of the archived ODS.**

Every original file and previous archive version is preserved. Correction made only in new separately versioned QA note v2.

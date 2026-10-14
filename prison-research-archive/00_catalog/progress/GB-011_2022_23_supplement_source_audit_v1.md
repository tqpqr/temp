# GB-011 — FY2022/23 original supplementary prison-cost source audit

**Status: Original-source QA completed 14 October 2026.** Exact file `GB/costs-per-place-per-prisoner-2022-2023-supplementary-information.ods`, Git blob SHA-1 **`9c2f4e108de7346df4d13804ab71355210228de2`**, original **57,469 bytes**. Original ODS `content.xml` (1,284,117 bytes after decompression) inspected directly; original numeric stored values preserved. Original edition source `Cover_!A19` **Published 21 March 2024**, independently corroborated by https://www.gov.uk/government/publications/prison-performance-data-2022-to-2023 . Scope: **England and Wales FY2022/23 (April 2022–March 2023)**, not whole UK and not calendar year.

## Original content preservation
- Three real source tabs `Cover_` **8**, `T1_Contracted_Prisons` **40**, `T2_Supplementary_Data` **44** nonempty physical worksheet rows, **92 total**. Every A–K stored numeric/text cell and original source row number saved [here](GB-011_2022_23_supplement_full_source_cells_v1.csv). Zero `table:formula` in these actual source sheets; no formulas recalculated. Extraneous ODS external reference/table-link objects are not promoted to actual financial worksheets or followed.
- Original detailed FY2022/23 by-establishment accounting dataset already has **119** original institution-year lines in `gb_cost_FY2021_22_to_FY2023_24_358_establishment_source_rows_v2_physical_rows.csv`; DO NOT extract another duplicate by-institution panel.

## National financial-year publisher values (`T2_Supplementary_Data!B59:J59`)

| Source measure | Exact FY2022/23 number | Source |
|---|---:|---|
| Certified Normal Accommodation | **80,846 CNA places** | B59 |
| Annual-average prisoners | **81,822 persons** | C59 |
| Direct Resource Expenditure | **£2,751,481,717** | D59 |
| Overall Resource Expenditure | **£4,181,725,178** | H59 |
| Direct cost per CNA place / FY-average prisoner | **£34,034 / £33,628** | E59/F59 |
| Overall cost per CNA place / FY-average prisoner | **£51,724 / £51,108** | I59/J59 |
| Service Concession Arrangements (Non Pay child) | **£559,567,392** | D49 |

Direct cost hierarchy: `T2!D41` Payroll **£1,663,773,626**, `D42` **Non Pay PARENT £1,156,514,028**, `D43:D50` eight nonpay children sum to parent **exactly** in printed pounds, including `D49` service concession item; `D51` signed income **−£68,805,938**. Six additional `H53:H58` allocations are **overall-only**; never add Non Pay parent to its own children or call overall and direct expenditure equivalent. `T2!A53` buildings depreciation and capital repayment; source caption unchanged against FY2021/22.

## Exact original contract-count and operator classification break (MB-023)

`T1_Contracted_Prisons!A5:A7` publishes **105 public + 14 contracted = 119** prison categories at FY-end, unchanged national count from FY2021/22. But current year `T1!A16:A53` has **8 PFI facilities and 6 Manage & Maintain (M&M)**, versus previous original FY2021/22 **10 PFI and 4 Operate & Maintain**.
- Verified prior FY source `GB/costs-per-prison-place-and-prisoner-2021-2022-supplementary-information.ods`, Git blob `a0346d48d785c01e7fb1a8dcf55f1379d1d5a2da`, `T1_Contracted_Prisons!A23:G23` = **Lowdham Grange under PFI**, `A28:G28` = **Parc under PFI**, both already existing physically in original detailed FY2021/22 prison-year ledger.
- Verified FY2022/23 `T1!A40:G40` **Lowdham Grange in M&M** with `B40` new contract **February 2023**; `T1!A48:G48` **Parc in M&M** new contract **December 2022**. Both are contract/reclassification transitions; **NOT** new physical prisons, not a change to total 14 contracted count.
- 2022/23 source labels M&M **Manage & Maintain**, FY2021/22 labels **Operate & Maintain**. The issuer annual financial statement separately identifies an **Altcourse managed contract in mobilisation phase** at FY2022/23 end, not included as named cost-producing prison in the source T1 M&M list. The annual-account **seven managed contracts** are not the same denominator as this supplementary prison-cost T1 **six operational reporting lines**.

**Financial reclassification evidence:** Original official `Ministry of Justice Annual Report and Accounts 2022-23`, HTML https://www.gov.uk/government/publications/ministry-of-justice-annual-report-and-accounts-2022-23/annual-report-and-accounts-2022-23-financial-statements-html , explicitly documents **£94.2 million** of FY2021/22 **PFI service charges reclassified from offender-related costs**, and reclassification of prior-year balance-sheet assets of managed prisons from **Owned** to **on-balance-sheet PFI/other service concession arrangements** under **IFRIC 12**, restating 31 March 2022 balances. This is CONFIRMED in department-level MoJ accounts. It is **NOT yet separately proven** that the prison-unit-cost supplementary `T2!D49` incorporates an identical GBP 94.2 million reclassification, or whether prior-year costs in this particular ODS are restated. **No transfer of £94.2m between this prison-unit-cost D48 and D49 allowed without an actual mapping.** MB-023 records the issue and verification boundary.

## Five Wells chronology/vintage discrepancy (MB-024, and MB-022 retained)

FY2021/22 `T1!B45` uses **Feb 2022** as Five Wells contract start, FY2022/23 `T1!B46` uses **Nov 2020** under same printed heading. This is a directly confirmed source-version disagreement about a historic reported date. Original government operator-award notice https://www.gov.uk/government/news/wellingborough-jail-contract-awarded-and-new-name-revealed dates award **6 October 2020**, while official HMPPS news https://www.gov.uk/government/news/britain-s-first-smart-prison-to-drive-down-crime says **first prisoner arrived 4 February 2022**, and opening followed in 2022. These are distinct historically documented milestones, so one source likely uses a different meaning for contract commencement/operational start, but neither source table explicitly explains why both column headers say Contract start date. Preserve both exact captions and dates; do not declare one to be publisher typo or silently overwrite `MB-022`.
- FY2021/22 Five Wells `T1!A45:G45`: **960 CNA, 205 average prisoners, £7,926,414 overall, £8,257/place and £38,760/prisoner**. FY2022/23 `T1!A46:G46`: **1,620 CNA, 794 FY average prisoners, £40,682,745 overall, £25,113/place and £51,265/prisoner**. Also independently identified in original detailed FY2022/23 `T3_Cost_by_Establishment!A38:J38`. This is a new annual observation of the SAME named prison, not a second facility.
- Numeric change combines **CNA expansion, FY mean population increase and expenditure changes**; neither year is automatically a mature full-capacity efficiency observation without verified time/exposure/operational-status denominators. Low FY2022/23 occupancy ratio based on average prisoners/CNA does not prove low utilization at each point in FY.

## Institution function taxonomy changed in separate original FY2022/23 by-prison workbook (MB-025)
Already audited original `GB/costs-per-prisoner-individual-prison-2022-2023.ods` `T3_Cost_by_Establishment` notes and associated reporting headers identify an expanded male **Category C & YOI Trainer and Resettlement** group with **four institution reclassifications** versus previous year. Existing archived methodological audit `gb_cost_22_sources_methodology_restatement_audit_v2.md` explicitly records this source event; no source-supported names of all four are asserted by this supplementary-only microtask. A controlled old/new function-group and institution crosswalk is still needed before category-average comparisons. Source FY2021/22 Five Wells detailed group was "Male category C Trainer and Resettlement"; FY2022/23 detailed source groups Five Wells as "Male category C & YOI Trainer and Resettlement." That one name is directly verified, but is not asserted to exhaust the four formal reclassifications.

## Independent original-value arithmetic QA

[36 source-cell tests](GB-011_2022_23_supplement_arithmetic_QA_v1.csv) check source national totals, 8 PFI/6 M&M named component sums, payroll/non-pay signed income, six overheads, sex/age/public-private/region partitions, and Wales subgroup. Largest discrepancy **3 published whole-pound/whole-person/whole-place source units** (for `T2!D59+H53:H58` against `H59` = **+£3**). Other nonzero printed-source differences: PFI named sum vs subtotal −£2, M&M FY-average people +1, direct payroll+nonpay+income −£1. This is consistent with the publisher's explicit caution `T1!A57:A58; T2!A67` that totals are from unrounded data but components are rounded. Original values unchanged; never force exact printed addition by inventing a hidden expense.

## Protocol decisions
- Add **25** original-source national FY2022/23 accounting/denominator observations to indicator registry (source references, original column/row, publication edition, source SHA). No existing 119-prison detail duplicated.
- Add **MB-023** accounting and subgroup reclassification, **MB-024** Five Wells historical date disagreement, **MB-025** four-site function-group reporting change (exact names pending targeted source crosswalk). All earlier issue IDs and source data remain preserved.
- Next **GB-012 FY2023/24 supplementary**, then remaining financial appendices; compare source vocabularies and reporting vintages to avoid false time-series inference.

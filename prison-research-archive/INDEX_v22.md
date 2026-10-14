# Prison research archive — ACTIVE INDEX v22 (14 October 2026)

## Resume point — GB-011 DONE, GB-012 NEXT

**[Newest checkpoint v17](00_catalog/SESSION_CHECKPOINT_20261014_v17.md)** contains precise original worksheet/cell/source SHA evidence, the original publisher versus restated annual-account boundary, independently corroborated Five Wells historical dates, and complete resumed-task instructions. Last finished task **GB-011**, next **GB-012 original FY2023/24 prison-cost supplement**.

- [Microtask queue v15](00_catalog/MICROTASK_QUEUE_WAVE1_v15.csv): **15 DONE**, 1 DONE_PRIOR_AUDIT_RECONCILED, 2 BLOCKED, 1 WAITING_ON_GB-002, 11 PENDING, **1 NEXT**, 31 total.
- [Indicator × reporting period register v14](00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v14.csv): **1,086 evidence-classified records**, +25 new original source FY2022/23 national indicators **R01062–R01086**. Large-file note: `fetch_file` yielded no body after file exceeded ~1MB; `mcp__GitHub__fetch` of matching GitHub `api.github.com/repos/tqpqr/temp/contents/...` retrieved and successfully validated all 1,086 rows/37 fields and last R01086. These are not 1,086 harmonised real economic time series.
- [Methodological breaks and source-anomaly register v9](00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v9.csv): **25 independently recorded issues**, +MB-023–MB-025 this turn. All previous source data and issue IDs preserved.
- [Previous archive index v21](INDEX_v21.md) and [original-file microtask evidence protocol](00_catalog/MICROTASK_PROTOCOL_AND_QUEUE_v4.md). Files are added by version, never overwriting original research source.

## GB-011 — FY2022/23 original supplementary finance from HMPPS/MoJ

Source `GB/costs-per-place-per-prisoner-2022-2023-supplementary-information.ods`, Git SHA-1 **`9c2f4e108de7346df4d13804ab71355210228de2`**, **57,469 bytes**. `Cover_!A19` published **21 March 2024**; original official public page https://www.gov.uk/government/publications/prison-performance-data-2022-to-2023 . Geography **England and Wales**, full **FY2022/23**, not a UK-wide/calendar-year or point-in-time prison occupancy dataset. Prior FY2022/23 by-prison detailed original **119 establishment accounting rows** already catalogued; no duplication.

Created and re-fetched:
- [Original-file methodology audit with documented official accounting evidence](00_catalog/progress/GB-011_2022_23_supplement_source_audit_v1.md)
- [Every nonempty physical source row and source A–K cell](00_catalog/progress/GB-011_2022_23_supplement_full_source_cells_v1.csv): `Cover_` 8, `T1_Contracted_Prisons` 40, `T2_Supplementary_Data` 44 = **92 nonempty original rows**
- [36 original numeric/category reconciliation checks](00_catalog/progress/GB-011_2022_23_supplement_arithmetic_QA_v1.csv), maximum original printed-component discrepancy **3 in per-check original units**; existing source note explicitly warns publisher totals are from unrounded quantities.

| Publisher FY2022/23 national indicator | Original value | Source cell |
|---|---:|---|
| Certified Normal Accommodation | **80,846 CNA places** | `T2_Supplementary_Data!B59` |
| Annual-average prisoner population | **81,822** | `T2!C59` |
| Direct Resource Expenditure | **£2,751,481,717** | `T2!D59` |
| Overall Resource Expenditure | **£4,181,725,178** | `T2!H59` |
| Direct cost per CNA place / per FY-average prisoner | **£34,034 / £33,628** | `T2!E59:F59` |
| Overall cost per CNA place / per FY-average prisoner | **£51,724 / £51,108** | `T2!I59:J59` |
| Service Concession Arrangements (part of Non Pay) | **£559,567,392** | `T2!D49` |

**Never double count** `T2!D42` Non Pay parent and its eight component children `D43:D50`. Extra `H53:H58` allocations are overall-only, not direct expenses. Population is FY mean and CNA does not equal usable/operational capacity. Public/private reported costs differ in original accounting perimeter.

### GB-011 critical research findings

**MB-023 — two separate but related accounting/contract changes, do not merge blindly.** FY2021/22 contracted prisons comprise 10 PFI and 4 O&M; FY2022/23 comprise **8 PFI and 6 Manage & Maintain**, but total 14 contracted facilities remains the same. **Lowdham Grange** moved from PFI prior source `T1!A23` to new `T1!A40` M&M (Feb 2023 contract) and **Parc** from prior `A28` PFI to `A48` M&M (Dec 2022). These are not two newly opened prisons. Official MoJ annual financial statements also confirm FY2021/22 **£94.2m PFI service-charge accounting reclassification** from offender-related costs, and IFRIC 12 concession asset reclassification, including restated 31 March 2022 asset values: https://www.gov.uk/government/publications/ministry-of-justice-annual-report-and-accounts-2022-23/annual-report-and-accounts-2022-23-financial-statements-html . Those **departmental annual-account** changes are *not* proven to be exactly the same accounting category transformation in prison cost supplement `T2!D49`; do not add/subtract £94.2m to our national prison cost series. Seven financial-statement managed contracts (including mobilising Altcourse) versus six named cost supplement operational establishments have different report universes.

**MB-024 — Five Wells historical start-date conflict, distinct events.** FY2021/22 `T1!B45` says **Feb 2022**, FY2022/23 `T1!B46` says **Nov 2020** in identically headed original date column. Official operator contract award was announced **6 Oct 2020**, first prisoner confirmed **4 Feb 2022**: https://www.gov.uk/government/news/wellingborough-jail-contract-awarded-and-new-name-revealed ; https://www.gov.uk/government/news/britain-s-first-smart-prison-to-drive-down-crime . Thus 2020 procurement versus 2022 custody opening are different milestones, while the source column's intended date meaning across vintages is unresolved. FY2022/23 Five Wells **1,620 CNA, 794 FY-average persons, £40,682,745 overall cost, £25,113 per place**, compared to 2021/22 **960 CNA, 205 annual-average persons, £7,926,414 overall, £8,257 per place**. Do not treat this as a clean full-year efficiency trend or count two facilities. Preserve prior MB-022 late opening/exposure warning.

**MB-025 — four original prison-function changes.** The already-audited original 2022/23 `T3_Cost_by_Establishment` and its notes were previously documented as reflecting **four prisons reclassified into an expanded male Category C & YOI Trainer and Resettlement** function. Exact four prison names are **not yet reenumerated and individually crosswalked** in GB-011, which only covers the supplementary workbook; verify the original `Notes_to_T3` source specifically before harmonising group aggregates. Existing prior FY2021/22 Five Wells category label versus FY2022/23 Five Wells category label demonstrably differs; do not guess the other sites.

## NEXT GB-012

Exact target in [queue v15](00_catalog/MICROTASK_QUEUE_WAVE1_v15.csv): `GB/costs-per-prison-place-prisoner-2023-24-supplementary-information.ods`. Before any new extraction consult this [checkpoint v17](00_catalog/SESSION_CHECKPOINT_20261014_v17.md), [current indicator v14](00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v14.csv), [breaks v9](00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v9.csv), original 22-workbook 102-sheet catalogue and previously verified FY2023/24 **120 by-establishment original financial rows**. Observe original source cover publication date, row/column/definition changes, subgroup identities, the evolving MoJ finance-concession classification, and exact geography. Only newly evidenced source-year components and QA, never a second 120-site source panel; decide dual registry versions explicitly, save queue v16, checkpoint v18 and INDEX v23. Maintain add-only archive source preservation.

Original Git blob SHA-1 identifies repository binary, not independent publisher binary equivalence; no background tasks in progress.

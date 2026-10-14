# Prison research archive — ACTIVE INDEX v21 (14 October 2026)

## Resume here: GB-010 DONE; GB-011 NEXT

- [Latest complete checkpoint v16](00_catalog/SESSION_CHECKPOINT_20261014_v16.md): original GB-010 2021/22 supplementary costs independently parsed, exact source cell/numerical QA verified, Five Wells initial late-contract-year comparability issue **MB-022** confirmed and bounded; **GB-011** is next.
- [Current microtask queue v14](00_catalog/MICROTASK_QUEUE_WAVE1_v14.csv): **14 DONE**, 1 DONE_PRIOR_AUDIT_RECONCILED, 2 BLOCKED, 1 WAITING, 12 PENDING, **1 NEXT (GB-011)** among 31 tracked tasks.
- [Previous index v20](INDEX_v20.md), [source preservation microtask protocol](00_catalog/MICROTASK_PROTOCOL_AND_QUEUE_v4.md). All prior originals, studies, CSVs, QA and index versions retained, never overwritten.

## Current indicator and methodological-evidence catalogues

- [Indicator × original period/source registry v13](00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v13.csv): **1,061 graded evidence records**, of which **25 newly added R01037–R01061** are exact fiscal FY2021/22 national cost and component/capacity/average-prisoner figures. Source cell, unit, fiscal-year boundaries, edition and Git source blob noted. These are NOT 1,061 harmonized empirical series and are not a count of unique facilities.
- [Methodological breaks and anomalies v8](00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v8.csv): **22 cases**; GB-010 adds **MB-022** (Five Wells February 2022 contract start + published whole-FY per-CNA cost comparability issue). Prior **MB-005** FY2019/20 Birmingham operator split, **MB-021** hidden historic G4S Birmingham contract period in 2019/20 O&M subtotal, **MB-010** public/contracted accounting perimeter, **MB-020** earlier building/ICT caption change, and all previous items preserved unchanged.

## GB-010 — 2021/22 original national prison cost supplement

**Original file:** `GB/costs-per-prison-place-and-prisoner-2021-2022-supplementary-information.ods`, repository Git SHA-1 **`a0346d48d785c01e7fb1a8dcf55f1379d1d5a2da`**, **42,056 bytes**, `Cover_!A19` **Published 9 March 2023**. England and Wales financial year **2021/22**, not UK-wide and not calendar 2022.

[Detailed original source QA](00_catalog/progress/GB-010_2021_22_supplement_source_audit_v1.md) | [All 96 nonempty physical ODS source rows A–K](00_catalog/progress/GB-010_2021_22_supplement_full_source_cells_v1.csv) | [35 original-source arithmetic checks](00_catalog/progress/GB-010_2021_22_supplement_arithmetic_QA_v1.csv).

Original worksheets: `Cover_` 8 source rows, `T1_Contracted_Prisons` 40, `T2_Supplementary_Data` 48. Original `content.xml` read directly; no worksheet formulas followed. Original **119 by-establishment FY2021/22 accounting rows** had already been verified separately in `gb_cost_FY2021_22_to_FY2023_24_358_establishment_source_rows_v2_physical_rows.csv` and were NOT duplicated.

| Publisher FY2021/22 reported national indicator | Original value | Source |
|---|---:|---|
| Certified Normal Accommodation | **80,362 places** | `T2_Supplementary_Data!B59` |
| FY annual-average prisoner population | **79,113 prisoners** | `T2!C59` |
| Direct Resource Expenditure | **£2,490,214,500** | `T2!D59` |
| Overall Resource Expenditure | **£3,752,632,094** | `T2!H59` |
| Direct unit cost per CNA place / annual-average prisoner | **£30,987 / £31,476** | `T2!E59/F59` |
| Overall unit cost per CNA place / annual-average prisoner | **£46,696 / £47,434** | `T2!I59/J59` |
| Service Concession Arrangements inside Non Pay | **£502,322,541** | `T2!D49` |

**Raw-data restrictions:** CNA is not operational capacity; FY-average population is not a one-day count. Non Pay parent `D42` includes its eight children `D43:D50` (do not add both). `H53:H58` are *overall-only* allocations, not direct resource expenditure. Public/private expense comparisons are subject to explicit issuer accounting-scope warning. All 35 check discrepancies are at most one publisher-rounded source unit; original integers preserved, not corrected.

### MB-022 — new Five Wells first FY contract-period comparison warning

Original `T1_Contracted_Prisons!A45:G45` lists **Five Wells** with **Feb 2022** contract start, **960** CNA, **205** FY-average prisoners, **£7,926,414** overall resource spending, **£8,257** per place and **£38,760** per average prisoner. The independent existing per-establishment 2021/22 original source `T3_Cost_by_Establishment!A34:J34` reproduces all five measures exactly. `T1!A5:A6` lists **105 public + 14 contracted = 119** FY-end establishments (prior FY2020/21 104+13).

**This is not evidence of exceptional full-year cost efficiency.** A late-FY contract start is established by the original; neither the actual operational opening, effective months of service, intra-FY capacity exposure nor staff/cost ramp-up is determined from these two tables. Reported £8,257 per CNA place cannot be substituted for a full-year fully operating site estimate without further chronology/accounting evidence. Do not treat 205/960 as an observed occupancy rate over actual open months or count Five Wells twice. Source event and limits precisely recorded in **MB-022**.

## NEXT GB-011 FY2022/23

Original target `GB/costs-per-place-per-prisoner-2022-2023-supplementary-information.ods` as recorded in [queue v14](00_catalog/MICROTASK_QUEUE_WAVE1_v14.csv). Check [current original indicator registry v13](00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v13.csv) and [methodological issues v8](00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v8.csv) before extraction. FY2022/23 original **119 by-establishment rows** already in archive; do not duplicate. Four facility classification changes (documented in original FY2022/23 by-establishment sheet notes) merit careful grouping checks; Five Wells is now in its subsequent reporting year but assume neither full operation nor exact comparable capacity without evidence. Save additive source QA, explicit two-catalog decisions, queue v15, checkpoint v17 and index v22.

Source Git SHA-1s identify the repository's original Git objects; they are not independently proven publisher-hosted binary SHA-256 hashes. No asynchronous processing is running.

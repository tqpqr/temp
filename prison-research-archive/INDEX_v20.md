# Prison research archive — ACTIVE INDEX v20 (14 October 2026)

## RESUME: GB-009 DONE; GB-010 NEXT

- [Latest source-verified checkpoint v15](00_catalog/SESSION_CHECKPOINT_20261014_v15.md) describes **GB-009 FY2020/21**, source rows, numeric checks, Git SHA, methodological decisions and exactly where to restart.
- [Atomic task queue v13](00_catalog/MICROTASK_QUEUE_WAVE1_v13.csv): 31 bounded tasks; **13 DONE**, 1 DONE_PRIOR_AUDIT_RECONCILED, 2 BLOCKED, 1 WAITING, 13 PENDING and **1 NEXT (GB-010)**.
- [Prior index v19](INDEX_v19.md) retains GB-008 FY2019/20, Birmingham G4S cost residuals and earlier archive/index chain. Original sources are never replaced; maintain independent precise source periods and provenance.

## Current evidence catalogues

- [Indicator × original reporting period registry v12](00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v12.csv): **1,036 individually evidence-classified records**, including 25 additional independently verified **FY2020/21 source numbers R01012–R01036**. Neither this total nor the raw accounting-line count equals the number of comparable prison-year observations.
- [Methodological breaks and source anomalies v7](00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v7.csv): **21 preserved issue records**, **NO_NEW_BREAK** for GB-009. Existing MB-005 and MB-021 refer to **FY2019/20** Birmingham operator-period identity/list mismatches, NOT automatically to FY2020/21. MB-010 guards public/contracted expense accounting scopes; MB-020 historical depreciation/category naming remains unresolved.

## GB-009 — FY2020/21 original financial supplement

Original `GB/costs-per-prison-place-prisoner-2020-21-supplementary-information.ods` Git SHA-1 `afd2878188b41d88fed7f39e6cd255cae95c87c6` (41,987 bytes). `Cover_!A19` states published **27 January 2022**. Geography England and Wales, FY **1 April 2020 to 31 March 2021**, not entire UK and not the calendar year 2021.

- [Complete original-file source QA](00_catalog/progress/GB-009_2020_21_supplement_source_audit_v1.md), [91 exact nonempty physical source worksheet rows, A–K](00_catalog/progress/GB-009_2020_21_supplement_full_source_cells_v1.csv), [36 original source number reconciliations](00_catalog/progress/GB-009_2020_21_supplement_arithmetic_QA_v1.csv).
- Three real original sheets: `Cover_` **8**, `T1_Contracted_Prisons` **39**, `T2_Supplementary_Data` **44** nonempty physical rows. Original ODS `content.xml` read, no worksheet formulas, no arbitrary values imputed. Already verified **117 FY2020/21 source-by-prison financial accounting lines** not recreated.

| Original FY2020/21 national reported measure | Original value | Source cell |
|---|---:|---|
| Certified Normal Accommodation | **79,364 places** | `T2_Supplementary_Data!B59` |
| Annual-average prison population | **78,959 persons** | `T2!C59` |
| Direct Resource Expenditure | **£2,583,235,767** | `T2!D59` |
| Overall Resource Expenditure | **£3,822,319,464** | `T2!H59` |
| Direct cost per place / prisoner | **£32,549 / £32,716** | `T2!E59/F59` |
| Overall cost per place / prisoner | **£48,162 / £48,409** | `T2!I59/J59` |
| Service Concession Arrangements child of Non Pay | **£492,029,748** | `T2!D49` |

**Numerical source QA:** publisher `T1!C5` public CNA = **66,697** versus `T2!B19` = **66,696**; T1 national `C7` = 79,364 although its displayed 66,697+12,668 public/contract part values sum to 79,365. Source `T1!E7` overall = £3,822,319,463 vs source `T2!H59` = £3,822,319,464. **All source values retained without 'correction'**, greatest deviation across 36 source-defined reconciliation equations one displayed unit, under publisher's stated unrounded-total/rounded-component caution. These small discrepancies are original-source presentation QC notes, not evidence of an institutional closure or new confirmed methodological breakpoint.

Original `T1!A5:A6` reports 104 public and 13 contracted prisons at fiscal year-end. All 10 named PFI and 3 named O&M contract totals reconcile within reported whole-unit rounding; there is no repetition of 2019/20 unlisted Birmingham contribution (MB-021). Existing public/contracted accounting and majority-use scope caveats still apply.

FY2019/20 → FY2020/21 original source: average prisoners **82,890 → 78,959**, nominal overall resource spending **£3,536,900,071 → £3,822,319,464**, Non payroll services **£186,243,148 → £56,153,094**, Prisoner related costs **£185,656,507 → £287,153,177**. These are **observed changes only**. Neither causation by COVID-19 nor accounting reclassification nor expenditure fixed-cost elasticity is established by source supplements; methodological explanation is future research.

## NEXT GB-010 (FY2021/22 supplement)

Target `GB/costs-per-prison-place-and-prisoner-2021-2022-supplementary-information.ods`, exact source path from queue v13. Consult source 102-sheet inventory, [checkpoint v15](00_catalog/SESSION_CHECKPOINT_20261014_v15.md), [indicator v12](00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v12.csv) and [breaks v7](00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v7.csv) before reading. **Do not duplicate** previously checked FY2021/22 by-establishment detail panel; check actual source cover, denominators, T1 public/contracted scope and categories, source notes and arithmetic. Mark full evidence with physical source cells, original SHA, registry decision, queue v14, checkpoint v16, index v21 additively.

Git SHA-1 represents Git repository object identity, NOT publisher SHA-256 matching. No background work ongoing.

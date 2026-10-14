# Prison research archive — ACTIVE index v18 (14 October 2026)

## RESUME HERE — GB-007 completed, next GB-008

- [Latest complete checkpoint v13](00_catalog/SESSION_CHECKPOINT_20261014_v13.md): **GB-007 DONE**, source-original FY2018/19 supplementary ODS checked directly and 2018/19 original/restated financial vintages reconciled, **GB-008 NEXT**.
- [Task queue v11](00_catalog/MICROTASK_QUEUE_WAVE1_v11.csv): **11 DONE**, 1 DONE_PRIOR_AUDIT_RECONCILED, 2 BLOCKED, 1 WAITING, 15 PENDING, 1 NEXT. 31 tracked microtasks. Follow the [protocol](00_catalog/MICROTASK_PROTOCOL_AND_QUEUE_v4.md): reuse source evidence first, process one bounded item, write explicit dual-register decisions, preserve all original sources and prior file versions.
- [Previous index v17](INDEX_v17.md) provides GB-006 FY2017/18 source and earlier index chain, including the complete prior GB workforce/mensuration archive and national accounts projects.

## Current two catalogues (not raw study panel row counts)

- [**Indicator × source period registry v10**](00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v10.csv): **983 separately evidence-graded records**. Newly added original-source 2018/19 national cost/average-population/cost-component measurements **R00959–R00983** (25 records), each with source period, exact sheet/cell, issuer edition, original Git blob and methodological notes. Do **not** interpret count as 983 harmonized numerical series.
- [**Methodological breaks / anomalies v6**](00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v6.csv): **20 evidence-anchored cases**, NO_NEW_BREAK for GB-007. Reused **MB-004** 2018/19 initial versus restated *direct* spending education/training transfer, **MB-010** public vs contracted accounting, **MB-020** 2016/17 versus 2017/18 building-depreciation/capital category caption difference. Prior GB-006 count-perimeter **MB-019** still open, source-specific.

## GB-007 — FY2018/19 original national supplementary MoJ/HMPPS cost workbook

Original `GB/costs-per-prison-place-prisoner-2018-19-supplementary-information.ods`; original Git blob **`b76237a93416b737e437ef32b8a0e75566957abe`**, size **42,316 bytes**, `Cover_!A19` publisher date **31 October 2019**. Country scope **England and Wales**, financial year **1 Apr 2018–31 Mar 2019**.

Saved [original-sheet/source methodology QA](00_catalog/progress/GB-007_2018_19_supplement_source_audit_v1.md), [97 original nonempty source physical rows A–K](00_catalog/progress/GB-007_2018_19_supplement_full_source_cells_v1.csv), [33 reconciliations](00_catalog/progress/GB-007_2018_19_supplement_arithmetic_QA_v1.csv) and an [add-only QA correction to rounded Non Pay reconciliation](00_catalog/progress/GB-007_2018_19_source_QA_erratum_v1.md).

| Publisher initial FY2018/19 | Source value | Original source |
|---|---:|---|
| Certified Normal Accommodation | **78,774** places | `T2_Supplementary_Data!B59` |
| Annual-average prisoner population | **82,751** | `T2_Supplementary_Data!C59` |
| Direct resource expenditure | **£2,162,543,754** | `T2_Supplementary_Data!D59` |
| Overall resource expenditure | **£3,404,055,441** | `T2_Supplementary_Data!H59` |
| Direct cost per place / prisoner | **£27,453 / £26,133** | `T2_Supplementary_Data!E59:F59` |
| Overall cost per place / prisoner | **£43,213 / £41,136** | `T2_Supplementary_Data!I59:J59` |
| Service Concession Arrangements, Non Pay child | **£473,874,996** | `T2_Supplementary_Data!D49` |

Publisher source in `T1_Contracted_Prisons!A5:A7` describes 103 public and 14 contracted establishments at the fiscal-year end. This source count matches **117 previously audited original FY2018/19 establishment financial rows** numerically, but is **not** an institutional matching proof. Existing independent by-establishment initial and restated panels (117 + 117 distinct source rows) remain unchanged and are not counted as two years.

**Crucial restatement reconciliation:** restated individual-establishment edition separately reports £129,111,488 education/training costs newly attributed to **direct** prison expense; FY2018/19 original £2,162,543,754 becomes restated £2,291,655,242, **without change to original/restated overall** £3,404,055,441. Thus not a real new-year fiscal shock; the previously documented **MB-004** applies.

**Roundoff caveat:** the 8 source Non Pay children `T2!D43:D50` sum to £926,110,399 versus printed `D42` parent £926,110,397 — **+£2**, explicitly tolerated by publisher's unrounded-total versus rounded-part note. Preserve both figures; parent + children must not be double-counted. Publisher also leaves unlabeled negative-one intermediate cells `T2!C7`, `C36`; they are NOT negative actual populations or extra institutions, and intent beyond residual-like role was not verified. `T1!A10:A11` warns public/private PFI and healthcare cost accounting differences. FY mean prisoner population is NOT month-day prisoner stock and CNA is NOT operational/usable capacity.

## NEXT GB-008 — FY2019/20 prison cost supplement

Target original `GB/costs-prison-place-prisoner-2019-20-supplementary-information.ods`. Before extraction read source sheet index and earlier original FY2019/20 by-establishment audit. Specifically **MB-005** records Birmingham returning to public management July 2019, and the by-establishment source lists **118 operator-period accounting rows across 117 named establishment-count categories**. Reuse source-row data, validate original supplement headers and national components, identify true new FY observations, decide indicator registry v11/UNCHANGED and anomaly ledger v7/NO_NEW_BREAK explicitly. Add-only audit, queue v12, checkpoint v14, index v19.

Originals, old catalogues and versioned result panels never overwritten. Git source blob SHA-1 is not proof of external publisher binary equivalence. No tasks are running in the background.

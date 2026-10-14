# Prison research archive — active index v17 (14 October 2026)

## Continuation point

- [**LATEST checkpoint v12**](00_catalog/SESSION_CHECKPOINT_20261014_v12.md): task **GB-006 DONE**, **GB-007 NEXT**, every GB-006 source observation and methodological boundary recorded.
- [**Queue v10**](00_catalog/MICROTASK_QUEUE_WAVE1_v10.csv): 31 tasks; **10 DONE + 1 DONE_PRIOR_AUDIT_RECONCILED, 2 BLOCKED, 1 WAITING, 16 PENDING, 1 NEXT**. GB-007 (FY2018/19 source supplement ODS) is the only NEXT task.
- [Preservation/atomic source protocol v4](00_catalog/MICROTASK_PROTOCOL_AND_QUEUE_v4.md) and [previous main index v16](INDEX_v16.md), including completed GB-022 workforce March 2020 archive; every historical original and index version remains available.

## Twin catalogues now current

- [**Indicator × period registry v9**](00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v9.csv): **958 separately evidence-graded entries**, including **25 new FY2017/18 source cost metrics `R00934`–`R00958`**. The 958 count is *not* 958 comparable time series and many older entries are file/header inventory evidence, not numeric observations. New records include exact fiscal-year, source sheet/physical cell, units and source SHA.
- [**Methodological breaks and anomalies ledger v6**](00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v6.csv): **20 cases**; GB-006 added:
  - **MB-019:** one FY2017/18 source counts **116 institutions by public/contracted main category at fiscal year end**, but another source has **117 annual accounting lines**. Not assumed a typo or one specific prison.
  - **MB-020:** FY2016/17 label **Depreciation of buildings and central ICT** (£185,981,273) versus FY2017/18 **Depreciation of buildings and capital repayment** (£200,869,201). Accounting equivalence unknown; not safe to calculate labelled spending growth.
- Existing **MB-001–003** reflect FY2015/16 versus FY2016/17 classifications, **MB-004** FY2018/19 education/training direct-cost attribution restatement £129,111,488 (overall unchanged), **MB-010** public/private finance scope inequality, **MB-016** the 1,350-place national UK usable-capacity deduction; all historical entries preserved.

## GB-006 — source-audited FY2017/18 HMPPS/MoJ financial supplementary report

**Original:** `GB/costs-per-prison-place-cost-per-prisoner-2017-2018-supplementary-information.ods`, Git blob `e4d0f28ec9b9ab7349de258b9fe0a4e1bb0c68a1`, 44,358 bytes; `Cover_!A19` confirms **published 25 October 2018**; figures apply to **FY2017/18, England and Wales**, not calendar year 2018. Original external publisher download binary equivalence was not checked.

[Full source forensic audit](00_catalog/progress/GB-006_2017_18_supplement_source_audit_v1.md) | [all 93 actual nonempty source sheet rows A:K](00_catalog/progress/GB-006_2017_18_supplement_full_source_cells_v1.csv) | [16 original-value arithmetic checks](00_catalog/progress/GB-006_2017_18_supplement_arithmetic_QA_v1.csv).

**Three sheets**: `Cover_` 8 nonempty source rows, `T1_Contracted_Prisons` 41, `T2_Supplementary_Data` 44; all directly read and copied without source mutation. Source has no `table:formula` in these actual worksheets, so figures are stored source values, not computed independently by this audit. Existing 117 annual by-establishment accounting lines were NOT duplicated.

| Verified national original FY2017/18 source measure | Publisher reported |
|---|---:|
| Certified Normal Accommodation | **77,865 places** |
| Annual average prisoner population | **84,710 prisoners** |
| Direct resource expenditure | **£2,045,831,827** |
| Overall resource expenditure | **£3,180,266,865** |
| Direct unit cost per prisoner | **£24,151** |
| Overall unit cost per prisoner | **£37,543** |
| Service Concession Arrangements (part of Non Pay) | **£462,841,138** |

Original anchor `T2_Supplementary_Data!B59:J59` for national totals/rates, `D49` for concession costs. `T1!A5:A6` counts 102 public + 14 contracted establishments at FY end (not proof of 116 matching annual financing lines). `T1!A10:A11` expressly warns public/contracted accounting differences; `T2!A63` categorizes entire mixed prisons by majority use. CNA is not operational capacity and annual average persons are not one-day prison Population. `T2!D42` Non Pay £914,072,790 is exactly the sum of the eight `D43:D50` children; **do not count parent + children together**. Separately allocated overall-only amounts `H53:H58` do not belong to direct resource expenditure. Print-rounded components produce up to £2 reconciliation differences, explicitly allowed by publisher `T1!A56:A57`. No substantive cost-shock inference from differing class captions.

## Next GB-007 — FY2018/19 original supplementary report

Target original `GB/costs-per-prison-place-prisoner-2018-19-supplementary-information.ods`. First read [102 original cost workbook sheets catalogue](00_catalog/gb_cost_original_22_spreadsheets_102_worksheets_v2.csv), [latest registries](00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v6.csv), and [GB-006 source audit](00_catalog/progress/GB-006_2017_18_supplement_source_audit_v1.md). Check all actual original sheets, exact source publisher vintage and numeric categorization; specifically separate **FY2018/19 initially published vs subsequently restated FY2018/19 establishment direct expense** (MB-004). Avoid duplicating the already verified source-by-establishment financial panel. Add-only new QA/cell extract only where genuinely new; decide explicit coverage registry v10/UNCHANGED, breaks v7/NO_NEW_BREAK, queue v11, checkpoint v13 and active index v18.

All original sources preserved. Git blob SHA-1 values identify Git objects, not proof of matching independently published SHA-256. No asynchronous work is running.

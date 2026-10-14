# Prison research archive — active index v16 (14 October 2026)

## Resume without repeating research

- **Last finished atomic task: [GB-022](00_catalog/progress/GB-022_HR_March2020_original_source_QA_v1.md)** — original HMPPS workforce XLSX of 31 March 2020 directly inspected and source-cell audited. Full [checkpoint v11](00_catalog/SESSION_CHECKPOINT_20261014_v11.md); [link-only erratum](00_catalog/SESSION_CHECKPOINT_20261014_v11_link_erratum_v1.md) fixes one relative path in checkpoint without changing any data.
- [Current atomic queue v9](00_catalog/MICROTASK_QUEUE_WAVE1_v9.csv) — **GB-022 DONE; GB-006 NEXT**. 31 entries: 9 DONE, 1 DONE_PRIOR_AUDIT_RECONCILED, 2 BLOCKED, 1 WAITING, 17 PENDING, 1 NEXT.
- [Evidence protocol v4](00_catalog/MICROTASK_PROTOCOL_AND_QUEUE_v4.md), [previous index v15](INDEX_v15.md). All earlier original files and catalogue versions are preserved; source dates, physical source cell anchors, uncertainties, official scope and reuse decisions must remain explicit.

## Current catalogue status

- [**Indicator × period registry v8**](00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v8.csv): **933 graded evidence records**, +6 independently verified 31 March 2020 HMPPS FTE totals (`R00928`–`R00933`). These are **not 933 harmonised comparable statistical time series**.
- [**Methodological breaks & anomalies v5**](00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v5.csv): **18 evidence-anchored items**. New **MB-018** records different source assertions about YCS's creation date (**April 2017 versus September 2017**) within the same March 2020 workbook; underlying historical explanation not yet verified.
- Earlier **MB-001** remains the GB FY2016/17 Service Concession Arrangements £454.9m classification warning. **MB-016** retains the HMPPS national operating-margin distinction (December 2024, January/February 2025), and **MB-017** December 2024 Littlehey CNA anomaly remains open.

## GB-022 — verified new March 2020 workforce source

Source original: `GB/workforce/HR-tables-31-March-2020.xlsx` (source Git blob `c360e30210e0ef8a74d092cba474a8a423c4b6d3`, 291,448 bytes). [Audit note](00_catalog/progress/GB-022_HR_March2020_original_source_QA_v1.md) | [28-sheet content index](00_catalog/progress/GB-022_HR_March2020_28_sheet_catalog_v1.csv) | [106 original institution rows × 23 source FTE columns](02_uk/gb_workforce_2020_03_establishment_grade_source_raw_v1.csv).

- **Region:** England and Wales HMPPS, not UK-wide. Date: **31 March 2020** snapshot, not FY2019/20 mean. Older archived establishment observations for 2015–2020 are **June** snapshots and must not be conflated with this distinct March slice.
- Original worksheet `15. Snapshot of Estab. x Grade!A8:Y113`: 106 original facility names, 23 FTE numeric columns C–Y each (2,438 source values). The original groups these together as **Prison Service and YCS Establishments**, not an adult-prisons-only count, and private prison operators' staff are not necessarily included.
- **Every source-column sum** over 106 institutions agrees with publisher totals C114:Y114 (max floating calculation difference about 7.3e-12 FTE). Source sector totals from Table 1 also reconcile to Table 15 and to whole HMPPS.

| Source perimeter | Original staff FTE, 2020-03-31 | Source anchor |
|---|---:|---|
| Prison Service Establishments (public-sector) | 33,883.90931 | `1. SIP x Structure!L29` |
| Youth Custody Service | 1,530.21150 | `1. SIP x Structure!L9` |
| 106 combined prison/YCS establishments | 35,414.12081 | `15. Snapshot of Estab. x Grade!Y114` |
| HQ and Area Services | 5,186.59903 | `1. SIP x Structure!L7` |
| National Probation Service | 9,413.80786 | `1. SIP x Structure!L37` |
| **Whole HMPPS workforce** (includes NPS) | **50,014.52770** | `1. SIP x Structure!L38` |

Table 15 operational staff totals **27,077.76114 FTE**, nonoperational staff **8,336.35967 FTE**, combined **35,414.12081 FTE**. These apply to the **mixed** 106-institution scope. Original Table 15 footnotes identify July 2018 The Verne recategorization, July 2019 Birmingham return to public ownership, dynamic HR extract revisions and the unresolved April-vs-September YCS historical note. No direct causal growth inference from administrative transfer.

## Next atomic task: GB-006

Original UK financial supplementary ODS: `GB/costs-per-prison-place-cost-per-prisoner-2017-2018-supplementary-information.ods`. Before extracting, cross-check [full 22 original cost spreadsheet inventory](00_catalog/gb_cost_original_22_spreadsheets_102_worksheets_v2.csv), prior GB finance source-row audits, [indicator registry v8](00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v8.csv) and [breaks v5](00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v5.csv). Reuse already verified sources and only fill actual missing supplementary cost/denominator/financial-year definitions. Complete with exact source SHA/physical cells, explicit 2-catalogue decision, queue v10 and checkpoint v12.

**Do not overwrite** original PDFs, Excel/ODS or any existing versioned research data. Git SHA-1 identities are not third-party original SHA-256 confirmations. No background work is ongoing.

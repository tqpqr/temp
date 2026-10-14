# SESSION CHECKPOINT v11 — GB-022 March 2020 HMPPS workforce workbook (2026-10-14)

**Verified Git `main` HEAD before this checkpoint:** `9e2acf996e200cfef491a3244695336fbabaa019`. Last task actually complete: **GB-022 DONE**. Source and every earlier catalog/index/queue version preserved by additive file writes. No background or asynchronous work is running.

## Source read and original identity
- Original `GB/workforce/HR-tables-31-March-2020.xlsx`, source Git blob `c360e30210e0ef8a74d092cba474a8a423c4b6d3`, **291,448 bytes**, workbook with **28** sheet titles read from original compressed XLSX XML, shared strings and source cells.
- Cover gives **HMPPS Workforce Statistics Bulletin**, **England and Wales**, **31 March 2020**. This original is NOT an entire UK-wide total.
- Worksheet 3 `1. SIP x Structure`: `A4:M4` shows March annual year-ends 2014–2019 and June/Sep/Dec 2019 plus **March 31, 2020** at `L4`.
- Worksheet 23 `15. Snapshot of Estab. x Grade`, source `A1:A2`: establishment staff **as at 31 March 2020**, measured as **full time equivalents, FTE**. `C:H` six operational-grade columns, `I` operational total, `J:W` non-operational grades, `X` non-operational total, `Y` establishment grand total. **Headcount in other workbook sheets is a separate concept.**
- Existing `02_uk/gb_workforce_june_2015_2020_establishment_xlsx_QA_corrected_v3.csv` was consulted: its snapshots are **June**, so new **March 2020** source is not redundant.

## Actual extraction and validation
- `sheet23!A8:Y113`: **106 unique named establishment records** under original grouped source label **Prison Service and YCS Establishments**; 23 numeric source fields `C:Y` each, **2,438/2,438 numeric cells** (no blank/suppressed in those grade columns). No human adult-only/privately-operated mapping guessed.
- Each of **23** separate column sums of source rows 8–113 matches publisher `sheet23!C114:Y114` within 1e-6 FTE, maximum observed float difference **7.276e-12 FTE**.
- Table 15 operational **27,077.76114 FTE** (I114), non-operational **8,336.35967 FTE** (X114), combined **35,414.12081 FTE** (Y114).
- Table 1 `L29` public prison service **33,883.90931 FTE**, `L9` YCS **1,530.21150 FTE**: combined equals Y114. `sheet23!Y7` HQ and area **5,186.59903 FTE**; `sheet23!Y115` prison/YCS/HQ **40,600.71984 FTE**. `sheet3!L37` NPS **9,413.80786 FTE**; `sheet3!L38` whole HMPPS **50,014.52770 FTE**. Source cross-table reconciliation verified to within 1e-6.
- **Important denominator/scope:** All-HMPPS includes probation/HQ; Table 15 mixed 106-prison/YCS roster includes youth custody; does **not** necessarily include outsourced staff of privately-operated prisons; therefore cannot be casually compared with a prison population denominator including those institutions. Publisher note `sheet23!A119` flags late HR database updates. `A120` The Verne July 2018 role conversion; `A121` Birmingham public takeover 1 July 2019 and workforce inclusion.

## Methodological evidence
- **NEW MB-018:** `1. SIP x Structure!A43` says Youth Custody Service created **April 2017**, while `15. Snapshot of Estab. x Grade!A118` says created **September 2017**. Both dates appear in **the same original March 2020 workbook**; source wording verified, historical resolution **OPEN**. Do NOT select a correct date without official historical documentation. Other known UK event flags retained, not misinterpreted as staff growth.

## Created artifacts — independently re-fetched via GitHub after saving

1. [Unique raw March 2020 source panel](../../02_uk/gb_workforce_2020_03_establishment_grade_source_raw_v1.csv): **106 institution records**; Git blob `22b217f73d191676a0059117a44558636806d4cc`; write commit `39420de97b3254aa717936fa9006b0c6db587c14`.
2. [28 original worksheet captions and dimensions](progress/GB-022_HR_March2020_28_sheet_catalog_v1.csv): Git blob `6dc540e729e5db5678cde322962e06d7233aef98`, commit `d2be65e7ab6de539d3c768cc059dc89b95a4d74e`.
3. [Full original source QA and methodology](progress/GB-022_HR_March2020_original_source_QA_v1.md): Git blob `b098ab4e12f43772a2de43bf1ccaf7aa3e4895b8`, commit `81c2bab9ce291ae1a48b00b60e4b539c2193fa3d`.
4. [Indicator × reporting period registry v8](INDICATOR_PERIOD_COVERAGE_REGISTRY_v8.csv): **933 evidence-classified rows**, +6 verified `R00928`–`R00933` original 2020-03-31 FTE sector/total fields; Git blob `706ca306dad3a6439409351680b7a8e9793fc2bd`, commit `282b186cdb8f06b942f0814bab193cd7ebb65258`.
5. [Methodological breaks and anomalies v5](METHODOLOGICAL_BREAKS_AND_ANOMALIES_v5.csv): **18 issues**, +MB-018, Git blob `d7bb0096239bf6be74f24757ce0cc155e01e6d96`, commit `b43797f977149d219fad707fe0b53fe636b6bf21`.
6. [Queue v9](MICROTASK_QUEUE_WAVE1_v9.csv): **9 DONE, 1 DONE_PRIOR_AUDIT_RECONCILED, 2 BLOCKED, 1 WAITING, 17 PENDING, 1 NEXT = 31**; Git blob `63dec7815a6d976a2039c7f136828de3afbedbd8`, commit `9e2acf996e200cfef491a3244695336fbabaa019`.

## NEXT — GB-006 (UK financial supplementary report FY2017/18)
- Original `GB/costs-per-prison-place-cost-per-prisoner-2017-2018-supplementary-information.ods`.
- **Check existing cost audits and catalogues FIRST:** `00_catalog/gb_cost_original_22_spreadsheets_102_worksheets_v2.csv`, `00_catalog/gb_cost_FY2014_18_477_source_establishment_accounting_rows_v2.csv`, `00_catalog/gb_cost_22_sources_methodology_restatement_audit_v2.md`, `00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v5.csv`, `00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v8.csv`, and `00_catalog/MICROTASK_QUEUE_WAVE1_v9.csv`. Do not duplicate prior institution costs; extract only missing original supplementary definitions or numerical provenance.
- Record original SHA, actual financial-year labels (do not infer calendar year), original source sheet/cells, units, institutional denominator, presence of new financial categories, original publisher notes. Decide `DONE` or `DONE_PRIOR_AUDIT_RECONCILED`, explicitly decide indicator registry v9/UNCHANGED and breaks v6/NO_NEW_BREAK.
- Save a bounded source audit, queue v10, checkpoint v12 and index v17. Preservation policy add-only, never claim Git SHA-1 means publisher SHA-256.

**No work runs in the background after this response.**

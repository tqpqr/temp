# CHECKPOINT v3 — 2026-10-14 — resumable atomic work after GB-002 and GB-004

## Latest verified branch baseline
Last independently checked Git `main` before this checkpoint was `b789642e88e6e74e56e896a5021f34715edd21f3`. Subsequent **new add-only** queue snapshot commit `55705db2e42b99dbb6c8c9a7d42c8d431acbb50a` has already been re-fetched and verified. This checkpoint will itself create a later commit; **fetch current Git head before new writes**.

- Git recursive tree was complete, not truncated. **1,124** files outside `prison-research-archive/` remained unchanged by prior writes, **1,067** content-identical research source mirror blobs, **57** intentionally excluded `alt/`, `alt2/`, `alt3/` source blobs.
- Both `GB/costs-place-cost-prisoner-2015-16-supplementary-information.xlsx` SHA `c5605a10b66c2b2e312f07329153a436a90451d5` and the 2015/16 original *by-establishment* workbook SHA `09ae7bb2b1455657015f7203fdc7ea7eb283d707` still match previous baselines.
- Core previous archive index [INDEX_v8](../INDEX_v8.md), evidence [ledger v11](ARCHIVE_PER_FILE_EVIDENCE_LEDGER_v11.csv), older [checkpoint v2](SESSION_CHECKPOINT_20261014_v2.md) remain as historical source references. Their older task status is superseded for this **microtask wave** by [queue v2](MICROTASK_QUEUE_WAVE1_v2.csv). No files have been overwritten.

## Atomic task statuses and exact verified artifacts

**PRE-000 DONE** — preservation preflight and 31-source tasks protocol: [MICROTASK_PROTOCOL_AND_QUEUE_v1.md](MICROTASK_PROTOCOL_AND_QUEUE_v1.md).

**GB-001 DONE** — official Ministry of Justice 2016/17 release published 26 Oct 2017 explicitly includes FY2015/16 restated per-prison XLSX; the baseline research `GB/` collection does not contain it: [source reference](progress/GB-001_official_restatement_reference_v1.md) at commit `eb92e6b46c7551e29c2b2f6f3f87dc1a83ca13af`.

**GB-002 BLOCKED** — web display cannot return Excel binary, direct binary tool failed, runtime HTTP couldn't resolve domain. Official publisher URL only, **no downloaded bytes, no SHA-256, no new workbook uploaded**. The GitHub connector *could* upload a binary blob if actual bytes became available. **Read blocker before retry:** [GB-002 record](progress/GB-002_restated_binary_retrieval_BLOCKED_v1.md) at commit `98e4bddccb51a81f28225e9328666f058e53ef37`.

**GB-003 WAITING_ON_GB-002** — cannot compare initial and restated publishers' 2015/16 per-prison tables without the official revised byte source; do not invent comparison.

**GB-004 DONE** — original *supplementary* workbook from `GB/costs-place-cost-prisoner-2015-16-supplementary-information.xlsx` individually audited. **All 3 worksheets, 100 nonempty physical Excel rows** preserved with columns A–K at exact sheet and row addresses, in [GB-004 source CSV](progress/GB-004_2015_16_supplement_full_source_cells_v1.csv) commit `a4ccca5025272caa9d2b4292abe4cce1540b343e` and [detailed audit](progress/GB-004_2015_16_supplement_source_audit_v1.md) commit `b789642e88e6e74e56e896a5021f34715edd21f3`. Both created artifacts were separately re-fetched and content-verified.

### GB-004 central verified source facts
- `T1_Contracted Prisons` publishes 105 public / 14 contracted facilities (10 PFI, 4 O&M), CNA 78,271, average population 84,705, overall expenditure **£2,753,747,261** for FY2015/16 (`C5:G7` and `C39:G52`).
- `T2_Supplementary Data!D60`: total **direct** resource expenditure **£1,897,972,242**; `H60`: total **overall** expenditure **£2,753,747,261**; `A41:J60` has national expenditure/income and overhead classifications including negative income, property/administrative and PECS/HQ components. **Do not treat national 2015/16 component data as per-establishment or as Russian 7z budget categories.**
- Source explicitly says public/contracted costs **not directly comparable** due to differing treatment/scope (`T1_Contracted Prisons!A10:A11`, `T2_Supplementary Data!A65`). Prisons are classified by majority use (`T2_Supplementary Data!A64`).
- Seven independent arithmetic tests match exact totals or differ by £1 due to published rounding; no significant discrepancy.
- The workbook uses stored, rather than calculated, Excel cell values (no worksheet formulas). 3 external link objects and 127 obsolete `#REF!` named references found in metadata, not data values. Do not imply formulas re-evaluated.

## Resumption: next actual one-file task
**RU-001 NEXT**: `sud/2024 год/F2-2024.xls`, re-inspect this single originally difficult-to-parse legacy XLS, recover real source form/year/headers with working alternative XLS reader. Save `prison-research-archive/00_catalog/progress/RU-001_sud_F2_2024_v1.md` as **new** file; document original SHA + physical sheet/source-cell references or an explicit technical blocker. Do not guess sheet content based on file title.

If RU-001 reading remains technically impossible, mark BLOCKED in independent evidence file and proceed to another **independent** task, `GB-005` (2016/17 supplementary workbook) or `GB-014` (2015/16 narrative PDF), each as its own commit/checkpoint. Never silently repeat previously completed GB-004.

After each task: verify new path exists and matches expected text, and then publish a new *additive* `MICROTASK_QUEUE_WAVE1_v3.csv` snapshot if status changed. Preserve all earlier versions; do not mutate `INDEX_v8` or prior ledgers until a coordinated later new-version index refresh.

**Global initial task:** create a source-faithful, deeply navigable archival catalogue, not only a UK finance panel. Rotate UK, RU, SPACE, US independent microtasks; preserve source provenance, exact original file paths, definition distinctions, and source-cell/page anchors.

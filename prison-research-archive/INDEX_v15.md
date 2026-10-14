# Prison research archive — active index v15 (14 October 2026)

## RESUME HERE (GB-021 completed, next GB-022)

- [Checkpoint v10 — latest saved state](00_catalog/SESSION_CHECKPOINT_20261014_v10.md): latest task **GB-021 DONE**, original Jan/Feb 2025 ODS directly read, all source definitions and physical row checks reconciled, next **GB-022**.
- [Atomic queue v8](00_catalog/MICROTASK_QUEUE_WAVE1_v8.csv): **8 DONE**, **1 DONE_PRIOR_AUDIT_RECONCILED**, **2 BLOCKED**, **1 WAITING**, **18 PENDING**, **1 NEXT** out of 31. **GB-022** (2020 workforce XLSX) is the only next task.
- [Microtask evidence protocol v4](00_catalog/MICROTASK_PROTOCOL_AND_QUEUE_v4.md): always check previous work and BOTH registries first; preserve original data and existing versioned files; never recompute fully audited source rows; add source date/physical cell/units/SHA and explicit register outcome for each task.
- [Previous full index v14](INDEX_v14.md) remains the historical catalogue entry point for GB-020 and earlier batches, with all country folders and existing study panels.

## Current two evidence catalogues

- [Indicator × period registry v7](00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v7.csv): **927** graded rows, including **10 new original-source-verified national one-day observations R00918–R00927** (England and Wales, 27 Jan/24 Feb 2025). Counts include older document/form/presence evidence; they are **not** 927 comparable indicator-year series. Both files already have 120 prison rows each in the unchanged 2025 raw panel.
- [Methodological breaks and source anomalies v4](00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v4.csv): **17** previously documented issues, **NO_NEW_BREAK** for GB-021. **MB-016** national operational-capacity sum versus printed estate usable-capacity difference confirmed in December 2024, January 2025 and February 2025 originals: **1,350-place operating margin** in all three checked editions. Do not presume this margin holds in other dates. **MB-017** December 2024 Littlehey anomaly remains an OPEN historical interpretation; January/February 2025 are not anomalous under the same CNA comparison.
- Example of a separate financial classification break deliberately retained: **MB-001** UK FY2016/17 Service Concession Arrangements ~£454.9m.

## GB-021 — completed original-source audit

[Detailed audit and reconciliation](00_catalog/progress/GB-021_JanFeb2025_original_bulletins_QA_v1.md) | [10 national source-cell observations](00_catalog/progress/GB-021_monthly_two_sources_v1.csv) | [previously existing 2025 120-prison/month source panel](02_uk/gb_monthly_prison_population_capacity_2025_raw_v1.csv).

| Exact report day | Facility baseline CNA sum | Facility in-use CNA sum | Facility operational capacity sum | Official usable capacity (after 1,350 margin) | Population |
|---|---:|---:|---:|---:|---:|
| 2025-01-27 | 83,560 | 79,428 | 90,012 | 88,662 | 86,463 |
| 2025-02-24 | 83,557 | 79,340 | 89,985 | 88,635 | 87,199 |

**Source values:** `MonthlyBulletin!B5:E124` (120 prison rows) and national `B125:E125`; publisher margin notes `A129;A149:A152`, period `A2`, definition and scope caveats in [GB-021 QA note](00_catalog/progress/GB-021_JanFeb2025_original_bulletins_QA_v1.md). Both files' source-national Baseline, In Use and Population totals equal sums of original facility cells. Printed national usable total does not equal facility operational sum because the publisher deducts the national operating margin. Dated snapshots are not monthly averages.

A single text HTML entity difference in the 2025 raw panel's Peterborough name was noted and not treated as a different institution. Original files and earlier panels have not been overwritten.

## Next microtask

**GB-022:** inspect `GB/workforce/HR-tables-31-March-2020.xlsx` **only to fill gaps not already solved** by UK workforce 2015–2020 audits. Inspect exact table date/units (FTE/headcount), prison-vs-total establishment scope, publisher notes and source sheet cells; then explicitly update or leave unchanged each of the two catalogues. Write a bounded QA record, queue v9 and checkpoint v11. If prior evidence already covers acceptance, mark `DONE_PRIOR_AUDIT_RECONCILED` instead of duplicating extraction.

**Source-integrity and versioning:** add-only; existing source Git SHA-1 is not external publisher SHA-256. No background processing.

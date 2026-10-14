# Prison research archive — active index v14 (14 October 2026)

## Resume with no duplicated work
- [Newest checkpoint v9](00_catalog/SESSION_CHECKPOINT_20261014_v9.md): actually completed GB-020, preserved original/source mirror integrity, and next GB-021.
- [Atomic task queue v7](00_catalog/MICROTASK_QUEUE_WAVE1_v7.csv): **GB-020 DONE**, **GB-021 NEXT**.
- [Atomic evidence and dual-catalogue protocol v4](00_catalog/MICROTASK_PROTOCOL_AND_QUEUE_v4.md): consult existing work and both catalogues before starting a source, document every numeric period/source anchor, never repeat already fully verified extractions.
- [Full older original archive/source index v8](INDEX_v8.md) (unaltered), including British finance datasets, Russian FSIN/judicial/budget sources, international SPACE and US.

## Current twin catalogues
- **[Indicator × reporting period registry v6 — 917 evidence-graded records](00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v6.csv)**. Five new original-backed **2024-12-30** British prison-capacity/population fields added, each including exact source cells and difference between published estate *usable* capacity and sum of institution operational capacities. **917 is not the number of comparable time series**: file-presence and format-metadata records remain explicitly distinct.
- **[Methodological breaks & source anomalies v4 — 17 evidence-backed cases](00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v4.csv)**. MB-016 documents 1,350-place system-level margin; MB-017 identifies Littlehey Baseline CNA 1,176 versus In Use CNA 1,240 on one reporting date, cause not yet verified. Previous GB Service Concession Arrangements £454.9m reclassification warning MB-001 and other previous 15 cases retained.
- Both catalogues are **additive-versioned**; original source files and previous versions never overwritten. Each issue has a stable ID, source SHA, original source row/cell, and an instruction not to invent reconciliations.

## GB-020 DONE — actual 2024-12-30 monthly prison population and capacity
- Original `GB/Monthly_Bulletin_December_2024_web.ODS`, source Git SHA `c99e84252254f04b29cfe01122b41b4cf09bfdae`, 11,570 bytes. Original sheet `MonthlyBulletin` A2: `Report Date : 30/12/2024`; 120 institutions in original rows 5–124.
- **Prior work reused**: all 120 institution rows were already in [2024 report-date validated original-source panel v2](02_uk/gb_monthly_prison_population_capacity_2024_report_date_validated_v2.csv), and **120/120 source rows** now cross-checked for original date, name, physical sheet row and four numeric columns (zero mismatches). Avoid generating a second 2024 prison panel.
- [GB-020 source definitions and detailed QA](00_catalog/progress/GB-020_Dec2024_monthly_bulletin_source_QA_v1.md), [five-value national source reconciliation](00_catalog/progress/GB-020_Dec2024_monthly_bulletin_national_source_reconciliation_v1.csv).
- **Confirmed accounting/denominator difference**: sum of 120 individual facility Operational Capacity cells D5:D124 = **90,038**. Publisher national total D125 prints **88,688** (marked **); footnote A129 and A149:A152 explicitly **deduct 1,350 places as an operating margin** to obtain usable estate operational capacity. Baseline CNA B125 **83,596**, In Use CNA C125 **79,409**, Population E125 **85,618**. All three other national totals exactly match facility cell sums. **Neither CNA metric equals system usable operational capacity.**
- Source-defined one-day population is **not annual average** and can include those on authorised absence (A128); not identical to physically unlocked population. National margin may vary on other bulletin dates and should be read anew.

## Next small source scope
**GB-021**: original `GB/Monthly_Bulletin_January_2025_web.ODS` and `GB/Monthly_Bulletin_February_2025_web.ODS`, checking dates/actual contents and monthly capacity footer/operating margin. Before extracting, check [existing 2025 source row panel](02_uk/gb_monthly_prison_population_capacity_2025_raw_v1.csv) and corresponding source SHA; **do not duplicate already archived facility rows**, only add a new bounded QA/coverage update if warranted.

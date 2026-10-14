# Prison research archive — active index v12 (2026-10-14)

## Where to start after an interruption
1. [Atomic task protocol v3 — BOTH indicator and method-break registries compulsory](00_catalog/MICROTASK_PROTOCOL_AND_QUEUE_v3.md).
2. [Latest 31-task queue v5](00_catalog/MICROTASK_QUEUE_WAVE1_v5.csv): PRE-000, GB-001, GB-004, GB-005, INT-001 DONE; RU-001, GB-002 BLOCKED; GB-003 WAITING; **US-001 NEXT**; other 22 tasks pending.
3. [Latest checkpoint v7](00_catalog/SESSION_CHECKPOINT_20261014_v7.md).
4. [Historical full archival source index v8](INDEX_v8.md), preserving all original UK/RU/SPACE/US family datasets, original paths and provenance. Older versions all retained.

## Two linked primary catalogues — no duplicate archaeological work
- [**INDICATOR × PERIOD EVIDENCE REGISTRY v3 (903 records)**](00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v3.csv). Previous v2 899 entries retained; four higher-grade Italy, **2023-01-31** single-date facility numeric indicators appended, including source facility count, exact HTML row IDs, publisher national totals, women-source-blank tally, original Git SHA and official publisher URL. **Not 903 numeric longitudinal series**: legacy entries retain file-presence/metadata status.
- [**METHODOLOGICAL BREAKS / ANOMALIES REGISTRY v1 (12 issues)**](00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v1.csv), [guide](00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_GUIDE_v1.md). Stable IDs MB-001 through MB-012. Each has original source and physical source-cell anchors, observed fact, *separate unknown causal explanation*, prohibited extrapolation, follow-up trigger and verified source evidence files.
- UK `Service Concession Arrangements` **£454,911,681** in FY2016/17 as a distinct source category, not separately present FY2015/16, flagged MB-001; concomitant `Non payroll services` category discontinuity £487,329,372 vs £68,670,120 flagged MB-002. This does **not** demonstrate new spending/savings. FY2018/19 direct-expense £129,111,488 publisher restatement and unchanged overall expense flagged MB-004, not conflated with new spending.
- Italy capacity MB-011: official `capienza regolamentare` is defined by government space-per-prisoner rules and **does not incorporate temporary capacity deviations**. Not interchangeable with UK operating capacity or CNA. Italy 140 blank source women cells (not official zeros) MB-012. Historic ODS physical row misaddressing MB-006: use corrected v2 2014–2022 UK source tables.

## Completed recent one-source task INT-001
- [**189 Italy institutional original source rows + official total, all original HTML IDs**](00_catalog/progress/INT-001_Italy_2023_01_31_189_facilities_original_cells_v1.csv), [full QA and methodological evidence note](00_catalog/progress/INT-001_italy_capacity_source_v1.md).
- Source `space-archive/extra/stp8/Italy_Detenuti_capienze_per_istituto_31-01-2023.html`, Git SHA `7c996ffe3d5daa3f34fa26bcd5a141dc0c1d24b6`; actual source-date **31 January 2023**. Published/independently reproduced national totals: **51,403 regulatory places, 56,127 detained persons, 2,392 women, 17,687 foreigners**, sum discrepancies all zero; 20 regions, 189 institutions. **119/189** original institutional lines have observed persons above published *regulatory* places at that date; **140/189** women cells are source blank, not documented numeric 0.
- Exact official issuer: Italian Ministry of Justice / Dipartimento dell'amministrazione penitenziaria, public page https://www.giustizia.it/giustizia/it/mg_1_14_1.page?contentId=SST414676 (page/footnote indexed; external live HTML binary **not** independently byte-hashed). Original and archived copy must not be altered.

## Other completed/blocked examples
- [2015/16 supplementary GB source 100 nonempty worksheet rows](00_catalog/progress/GB-004_2015_16_supplement_full_source_cells_v1.csv) and [2016/17 99 rows](00_catalog/progress/GB-005_2016_17_supplement_full_source_cells_v1.csv), with source publisher values rechecked and source classification discontinuities in [their QA note](00_catalog/progress/GB-005_2016_17_supplement_source_audit_v1.md).
- [2024 Russian F2 court original binary limitation](00_catalog/progress/RU-001_sud_F2_2024_binary_READ_BLOCKED_v1.md); [2015/16 publisher restated XLSX binary limitation](00_catalog/progress/GB-002_restated_binary_retrieval_BLOCKED_v1.md). No fabricated source columns, no fake SHA256.

## Next microtask
**US-001**: `us/raw data/2011/public-use-file-layout.xlsx`, retrieve one original U.S. government public-use file-layout workbook, verify real headings, field codes, units, state/local coverage, fixed-width positions for known Corrections functions. Add genuinely checked variable/period definitions in indicator registry v4 only if new evidence; check breaks registry before marking equivalence.

All original sources and categorized mirrors remain byte-identical. New documentation and extracts are always versioned add-only.

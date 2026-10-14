# Prison research archive — active working index v13 (14 October 2026)

## Resume without repeating audits
- [Latest atomic protocol v4](00_catalog/MICROTASK_PROTOCOL_AND_QUEUE_v4.md): verify prior evidence first, **skip already completed source analyses**, and always decide whether to update BOTH the indicator-by-period catalogue and methodological break/anomaly catalogue.
- [Current task queue v6](00_catalog/MICROTASK_QUEUE_WAVE1_v6.csv): **US-001 DONE**, **US-002 DONE_PRIOR_AUDIT_RECONCILED**, **GB-020 NEXT**. Remaining past GB/Italy/RU statuses preserved.
- [Latest checkpoint v8](00_catalog/SESSION_CHECKPOINT_20261014_v8.md); [full earlier original archive map v8](INDEX_v8.md) and all older indexes/QA maintained.

## Two primary working catalogues
- **[Indicator × period evidence registry v5 — 912 entries](00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v5.csv)**, cumulative v1–v4. *Entry count is not count of verified comparable numerical time series.* Current additions: 6 original 2011 Census **layout fields** (v4, format metadata not indicators) and 3 verified 2011 source **E04/F04/G04 code-value coverage** entries (v5), original record counts 51/50/50 and two missing government/code combinations. Underlying code meanings require a separate official Census dictionary; nothing is labelled prison-only solely on code.
- **[Methodological breaks/anomalies ledger v3 — 15 documented cases](00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v3.csv)**. Existing MB-001 GB Service Concession Arrangements FY2016/17 £454.9m printed category, MB-004 British FY2018/19 direct-spending restatement £129.1m and MB-011 Italy regulatory vs operational capacity remain live. Newly MB-013: US 2011 layout printed amount position conflicts with start+length, MB-014: 2023-created/2025-modified workbook for historical 2011 dataset, MB-015: two original USA source code×government IDs absent (not zero). [Breaks protocol](00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_GUIDE_v1.md).

## Newly completed / prior evidence reused
- [US-001 exact six XLSX source fields + original cell coordinates](00_catalog/progress/US-001_2011_layout_six_fields_v1.csv) and [US-001 audit](00_catalog/progress/US-001_finance_codebook_2011_v1.md). Original `us/raw data/2011/public-use-file-layout.xlsx`, SHA `723b170c572df098a9c760294ec521e311132410`; sheet `public-use-file-layout` A11:E16. Printed amount 18–32 contradicts start 18/length 12 -> 18–29; later fields at 30–35. Metadata created 2023-10-06 and modified 2025-03-24, not a proven 2011 untouched original layout edition.
- [US-002 prior evidence reconciled, no duplicate 12,777-line raw text decoding](00_catalog/progress/US-002_completed_from_prior_2011_fixed_width_audit_v1.md); [original full audit](00_catalog/us_2011_fixed_width_layout_and_corrections_audit_v1.md), [151 original E04/F04/G04 rows](00_catalog/us_2011_state_finance_corrections_E04_F04_G04_verified_v1.csv). Fiscal-year data 2011, government identifiers 51; **E04 51, F04 50, G04 50**. Missing F04 government ID `32000000000000` and missing G04 government ID `04000000000000`; do not fill with 0.
- [INT-001 Italy 31 January 2023, 189 institutions, verified full source snapshot](00_catalog/progress/INT-001_italy_capacity_source_v1.md); originals and official totals [CSV](00_catalog/progress/INT-001_Italy_2023_01_31_189_facilities_original_cells_v1.csv) retained.

## Next one-source task
**GB-020**: original `GB/Monthly_Bulletin_December_2024_web.ODS` — verify exact actual report date and population/capacity column semantics by original source sheet/physical cell, then append actual date-specific indicator coverage to new registry only if confirmed. Determine if capacity is CNA vs usable/operating vs other; do not make unverified UK–Italy denominator equivalences.

Global preservation: 1,124 baseline originals, 1,067 research categorized byte-identical mirrors and 57 unrelated non-prison originals excluded; original/previous files only read, never overwritten.

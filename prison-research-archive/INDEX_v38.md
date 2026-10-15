# Prison research archive — active index v38 (2026-10-15)
**Second international source wave: INT-006 DONE; INT-007 DONE; NEXT INT-008.** [Latest checkpoint v37](00_catalog/SESSION_CHECKPOINT_20261015_v37.md), [previous active index v37](INDEX_v37.md).

## INT-007 Lithuania, government source verified
- [Detailed audit](00_catalog/progress/INT-007_Lithuania_2021_2024_source_audit_v1.md), [312 original-row QA](00_catalog/progress/INT-007_Lithuania_312_original_row_QA_v1.csv), [39 monthly eight-site sums](00_catalog/progress/INT-007_Lithuania_39_monthly_site_sums_v1.csv), [14 original field descriptions](00_catalog/progress/INT-007_Lithuania_14_field_dictionary_v1.csv).
- Original `space-archive/extra/stp8/LaikomuAsmenuStatistika.csv`: **63,903 bytes**, Git SHA1 **acd029c2f0975ec123007889e0e8cfd274d401f1** unchanged. 312 original facility-month records: 39 month-end dates Jan2021-Mar2024, 8 source sites/month, 14 original inmate count fields. Lithuania LKD/VDA issuer and definitions [independently confirmed through official field model](https://data.gov.lt/datasets/2665/versions/1367/models/LaikomuAsmenuStatistika/), but upstream actual CSV byte equality not verified. Portal's current revision is newer than old archived 2024-latest file.
- **MB-041:** 10 exact duplicate all-site monthly transitions in 2022, unknown cause. **MB-042:** reporting institution names/perimeter change Jan2023, no crosswalk. **MB-043:** arrest category included inside imprisonment subtotal in 2024, previously additive, plus five pre-2024 columns blank not zero. No source custody capacity/bed count. Eight-site sums not separately certified publisher national total.

## Versioned catalogs and scope
- [Indicator × period registry v20](00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v20.csv): 1174 records (prior 1160 + **14** source variables R01161–R01174).
- [Methodological issues v22](00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v22.csv): 43 cases (prior 40 + **MB-041–043**).
- [Wave2 queue v3](00_catalog/MICROTASK_QUEUE_WAVE2_v3.csv): 2 DONE, 1 NEXT, 12 PENDING of 15 new tasks; [19 original-source manifest v3](00_catalog/MICROTASK_QUEUE_WAVE2_STP8_SOURCE_MANIFEST_v3.csv): four first-wave source inspected, additional 15 wave2. Separate [wave1 queue v30](00_catalog/MICROTASK_QUEUE_WAVE1_v30.csv): 28/34 completed/reconciled, six blocked/dependent. Whole original repository previously 1124 blobs totaling ~1.354GB, not all source-audited.

**NEXT INT-008** `space-archive/extra/stp8/2020-gada-statistika.docx`, **1,088,041 bytes**, original blob SHA1 `5ff8e66877befd63836d89bf68b10721c3514326`. Confirm DOCX real contents, issuer/geography, periods/metrics; no government correspondence.

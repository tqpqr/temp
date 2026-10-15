# Prison research archive — INDEX v52 — WAVE 2 CLOSED (2026-10-15)

**Second wave complete: INT-006 through INT-020, all 15 tasks DONE.** No remaining NEXT or PENDING in this wave. Previous detailed [INDEX v51](INDEX_v51.md) remains intact.

## Verified final inventory
- [Final checkpoint v51](00_catalog/SESSION_CHECKPOINT_20261015_v51.md).
- [Independent closeout QA: 54/54 PASS](00_catalog/progress/WAVE2_INT006_INT020_FINAL_RECONCILIATION_QA_20261015_v1.json): all 15 source Git blob SHA-1/byte sizes correct, all 15 task audits exist, all 19 stp8 original files present.
- [Wave2 task queue v17](00_catalog/MICROTASK_QUEUE_WAVE2_v17.csv): 15 DONE.
- [Original 19-source manifest v17](00_catalog/MICROTASK_QUEUE_WAVE2_STP8_SOURCE_MANIFEST_v17.csv).
- [Indicator period registry v33](00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v33.csv): **1,624** records, sequential R00001–R01624.
- [Methodological anomalies ledger v35](00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v35.csv): **103** records, sequential MB-001–MB-103.

## INT-020 Austria — DONE
[Detailed original audit](00_catalog/progress/INT-020_Austria_Volksanwaltschaft_2021_source_audit_v1.md), [original binary verification](00_catalog/progress/INT-020_original_PDF_integrity_v1.json), [81 original province by inspection-category figures and conflicting published regional totals](00_catalog/progress/INT-020_Austria_2021_9_regions_9_inspection_types_two_contradictory_totals_v1.csv), [30 source-scoped observations](00_catalog/progress/INT-020_Austria_2021_NPM_inspections_staff_budget_scoped_scalars_v1.csv), [57 numeric QA passes](00_catalog/progress/INT-020_catalog_integration_and_quant_QA_v1.json).

Original Austria 2021 Volksanwaltschaft preventive rights monitoring PDF: 205 pages, 2,131,167 bytes, Git SHA1 52a09fa4da9b67cc9bcada0523e3082f92c48e9e, SHA256 b2d0676ac1ea66500d74b47704136be512ac6bdb33d5a72e1d60dcbd0dd364e9. Exact byte-for-byte match with official Austrian Ombudsman publication. All 205 source page texts saved.

National Preventive Mechanism: **570** inspection/observation activities; **27 prison inspections, 21 unannounced**, not numbers of distinct prisons or prisoners. **Serious original source conflict:** first table's regional sums and adjacent second table interchange six provincial totals (three region pairs), despite both national totals being 570. MB-098 records the unresolved arithmetic problem; no invented fix. €1.45m budget belongs to the oversight mechanism, NOT prison operations. Dated executive staff vacancies and allocated posts are not annual prison guard FTE. Six new MB-098–MB-103 and fifty source objects R01575–R01624 added.

## Scope boundary
This is completion of the **scheduled fifteen source microtasks**, not proof that every original file in the wider raw prison-data repository is fully normalized. The earlier first-wave audit still reported 28/34 reconciled, six blocked/dependent. Other unresolved problems remain in the methodological ledger, including Scotland, Slovakia, Slovenia and Estonia. No source originals changed and no requests were sent to government agencies.

Detailed other-country source indexes and audits are preserved in [INDEX v51](INDEX_v51.md) and previous versioned files.

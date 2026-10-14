# Checkpoint v20 — GB-013 verification continued (2026-10-14)

GB-012 is last fully DONE. GB-013 still **IN_PROGRESS_SOURCE_AUDIT**.

New verified changes:
- Ashfield contract-start field changes **Nov 1999** (FY2023/24 T1 row26, CNA416) to **Nov 2024** (FY2024/25 T1 row40, CNA416); physical facility not new. `METHODOLOGICAL_BREAKS_AND_ANOMALIES_v11.csv` adds **MB-028**, cause not established.
- The 23-cell arithmetic test bundle for FY2024/25 returned 20 PASS and 3 REVIEW. Some discrepancies 4–8 GBP in printed PFI and Fosse Way per-person ratios. Hidden unrounded source denominators plausible but unverified.
- Initial 92-row / 457-cell extraction unchanged; original binary SHA `bfb4795029d60ebf1351502b95b803d13c9ffcf1`. Cover release date 26 March 2026.
- Queue updated to `MICROTASK_QUEUE_WAVE1_v17.csv` with GB-013 IN_PROGRESS_SOURCE_AUDIT.
- Indicator registry intentionally held at v15 (1,111 records): FY2024/25 detailed 119 rows previously audited; review overlap before adding.

Artifacts: `progress/GB-013_2024_25_supplement_original_cells_v1.csv`, `progress/GB-013_2024_25_supplement_arithmetic_QA_v1.csv`, `progress/GB-013_2024_25_supplement_source_audit_v1.md`, `progress/GB-013_2024_25_supplement_followup_v2.md`.

Next: check Ashfield Nov 2024 contract from independent official records, check exact unrounded denominators or label ratio discrepancy unresolved, create source-unique national metric records if not already in v15, reconcile facilities with existing FY2024/25 detailed 119 rows; only then GB-013 DONE and INDEX v24. Original GB sources untouched; versioned add-only outputs. Earlier checkpoint: v19.

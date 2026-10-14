# Checkpoint v23 — GB-013 indicator registry integrated (2026-10-14)

GB-013 is IN_PROGRESS (remaining three ratio discrepancies and complete accounting/presentation sign-off). GB-012 is last full DONE.

## Successfully persisted
- `00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v16.csv` — **1,136 total records**. 1,111 untouched v15 plus 25 source-anchored FY2024/25 national values R01112–R01136. Git blob SHA `f375c15a9b5fa134147330810d4535e695f85782`, verified via fetch_blob after write. v15 blob `d314d9ded50d882e85c2099fefa16a6d320ab6be`.
- `00_catalog/progress/GB-013_2024_25_indicator_registry_delta_v2.csv` — 25×37 fields, corrected all FY2023/24 inherited metadata, official release 26 Mar 2026. Some stable indicator codes retain historical suffix `_2022_23`; this is flagged, not falsely relabeled.
- `00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v12.csv` — 28 cases, MB-028 verified official Ashfield Serco rebid 01 Nov 2024 (same prison/operator), parliamentary MoJ answer 27 Jan 2025.
- `00_catalog/MICROTASK_QUEUE_WAVE1_v18.csv` — GB-013 still in progress, crosswalk and issue update recorded.

## Original source/QA
- `GB/costs-per-place-per-prisoner-2024-2025-supplementary-information.ods`, original SHA `bfb4795029d60ebf1351502b95b803d13c9ffcf1`; 3 sheets, 92 source rows, 457 populated cells extracted. Cover original release 26 March 2026.
- `00_catalog/progress/GB-013_2024_25_supplement_arithmetic_QA_v1.csv`: 23 checks, 20 PASS / 3 REVIEW; per-unit PFI ratio differences £6 and £4, Fosse Way £8. Publisher states totals formed from unrounded averages, plausible cause but underlying averages not available.
- T1 total overall £4,926,302,564 vs T2 £4,926,302,565; source discrepancy retained. Concession £592,839,053 is a child of nonpay, not additive.
- Do not infer Fosse Way efficiency from 2023/24 to 2024/25 reported place cost: capacity exposure changes.

## Next
Broaden arithmetic QA and reconcile subgroup totals and contracted establishment rows, classify three REVIEW outcomes as documented publisher rounding if independently supportable; if not, preserve open flag. Then mark GB-013 DONE and proceed GB-014, keeping originals add-only. Full GB-013 evidence in `00_catalog/progress/`; no original modification.

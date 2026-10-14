# GB-013 FY2024/25 supplementary — closure audit v3 (14 October 2026)

**Microtask GB-013 DONE: source catalogue and financial consistency audit, with source-level rounding caveat.** Scope: original FY2024/25 England/Wales HMPPS/MoJ supplemental ODS, NOT full research harmonisation.

## Original identity / preservation
`GB/costs-per-place-per-prisoner-2024-2025-supplementary-information.ods`, Git blob SHA-1 `bfb4795029d60ebf1351502b95b803d13c9ffcf1`. `Cover_!A19` publisher date 26 March 2026. Three actual sheets, 92 populated source rows, 457 preserved populated text/value cells in `GB-013_2024_25_supplement_original_cells_v1.csv`. Existing facility detail (119 previously inspected original FY2024/25 rows) not re-extracted.

## Financial QA (do not overwrite publisher numerics)
- Initial 23 tests: 20 displayed-value PASS, three REVIEW arising from PFI/Fosse Way unit cost divisions by displayed rounded denominators.
- Expanded `GB-013_2024_25_expanded_arithmetic_QA_v2.csv`: 64 checks, 46 displayed-value matches under tolerance and 18 displayed-value ratio differences. Aggregation checks for public+contracted, PFI+M&M, constituent prison totals, England+Wales, payroll+nonpay+income, nonpay child costs and overheads reconcile within a maximum absolute source-display 3 GBP/unit tolerance.
- `GB-013_2024_25_ratio_rounding_interval_QA_v1.csv`: all **40/40** T1 unit ratios tested fall inside the *possible* interval when denominators and costs are displayed to nearest integer. Method: published cost in [C-0.5, C+0.5], printed denominator in [N-0.5, N+0.5]; compare displayed published whole-unit ratio against interval [ (C-0.5)/(N+0.5)-0.5, (C+0.5)/(N-0.5)+0.5 ]. PFI F32/G32 and Fosse Way G42, previously REVIEW, are **ROUNDING_COMPATIBLE**, not numerical transcription errors. This is compatibility with the publisher's explicit T1 row54 and T2 row67 rounding note, *not verified exact hidden denominators or ratios*.
- Minor non-identical published national tables retained: T1 E7 £4,926,302,564 and T2 H59 £4,926,302,565; T1 F7 £59,026 vs T2 I59 £59,025 per CNA. No silent value correction.
- FY2024/25 national T2 B59 83,460 CNA, C59 87,009 average prisoners, D59 £3,292,840,593 direct and H59 £4,926,302,565 overall. Service Concession Arrangements D49 £592,839,053 is nested in nonpay D42, NOT an additional total expense.

## Cross-year contract / operational issues
- Altcourse previously documented category transfer MB-026; remains M&M, not additional facility.
- Fosse Way MB-027: 2023/24 first partial opening period vs 2024/25 larger CNA (1,143 vs 1,715), no claim of like-for-like unit-cost efficiency. Exact site capacity-time exposure remains unresolved.
- Ashfield MB-028 (registry v12): UK Parliament MoJ answer 27 Jan 2025 confirms Serco 1999 contract ended 31 Oct 2024 and next Serco contract started 1 Nov 2024. Contract rebid, NOT new physical prison. No claim of unchanged contractual scope.

## Catalog persistence
- `INDICATOR_PERIOD_COVERAGE_REGISTRY_v16.csv` Git blob SHA `f375c15a9b5fa134147330810d4535e695f85782`: 1,136 rows incl. 25 new original 2024/25 source-anchored national FY values R01112–R01136. 37 columns; original previous v15 1,111 rows preserved. Historical indicator code names containing `_2022_23` flagged as legacy semantic naming, not a period assignment.
- `METHODOLOGICAL_BREAKS_AND_ANOMALIES_v12.csv`: 28 issues, including MB-028 confirmed contract rebid.
- **Open methodological questions are not blockers to cataloguing this source**: exact unrounded denominator figures, underlying £1 printed T1/T2 differences, capacity-time exposure at Fosse Way. Preserve caveats in downstream analysis.
- GB-013 closure concerns original source inspection, arithmetic plausibility, provenance and registry; it does not imply full causal longitudinal comparability.

**NEXT:** GB-014, 2015/16 narrative PDF (source page, methodology, publication-vintage audit). Keep all existing originals and versions unchanged.

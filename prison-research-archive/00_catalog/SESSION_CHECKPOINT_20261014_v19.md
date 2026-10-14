# Checkpoint v19 — GB-013 original extraction and QA IN PROGRESS (2026-10-14)

**Last finished task: GB-012. GB-013 PARTIALLY PROCESSED; NOT DONE.** Prior checkpoint: [v18](SESSION_CHECKPOINT_20261014_v18.md). No existing originals changed.

## Original source
`GB/costs-per-place-per-prisoner-2024-2025-supplementary-information.ods`, Git blob SHA-1 `bfb4795029d60ebf1351502b95b803d13c9ffcf1` (not publisher SHA-256), MoJ cover `Cover_!A19`: Published **26 March 2026**. England and Wales FY2024/25. 3 sheets, 92 source nonempty rows, 457 nonempty cell records. Read original ODS ZIP content.xml; some pound symbols became mojibake in plain-text extraction, **numeric typed values valid**. Verify source identifiers prior to analytical reuse.

- [Original cell extraction](progress/GB-013_2024_25_supplement_original_cells_v1.csv).
- [Preliminary audit](progress/GB-013_2024_25_supplement_source_audit_v1.md).
- [23 arithmetic checks](progress/GB-013_2024_25_supplement_arithmetic_QA_v1.csv) — 20 PASS, 3 REVIEW. Review PFI total ratios (difference £6/CNA and £4/prisoner against reported whole-number denominator) and Fosse Way prisoner ratio (difference £8). Values may be due to hidden underlying unrounded denominators; do not silently adjust printed source numbers. Other published national comparisons have £1 differences.
- National source T2 `B59` CNA 83,460; `C59` prisoners 87,009; `D59` direct £3,292,840,593; `H59` overall £4,926,302,565; `I59/J59` £59,025/£56,618. T2 `D49` service concession £592,839,053 nested in non-pay (not additive).
- T1 `E7` overall £4,926,302,564 vs T2 `H59` £4,926,302,565. T1 `F7` £59,026/CNA place vs T2 `I59` £59,025.
- Fosse Way T1 `A42:G42`: CNA 1,715, average pop 1,698, overall £59,876,871, £34,914/place, £35,255/prisoner. Revisit capacity-time exposure vs GB-012 first-year MB-027.
- Altcourse T1 `A36:G36` remains Manage & Maintain with Jun 2023 contract start; MB-026 applies.
- Ashfield T1 `A40:G40` lists Nov 2024 contract start; investigate classification and prior-year source before new methodological break.

**Next**: resolve 3 QA reviews and inspect FY2023/24 and FY2024/25 subgroup definitions, match with 119 previously verified FY2024/25 detailed rows (no duplicate extraction), then **only after completed assessment** version indicator register, issue register, task queue, INDEX and checkpoint. Current active index v23, queue v16, indicator register v15 (1,111), issue register v10 (27). This note does not claim GB-013 completion.

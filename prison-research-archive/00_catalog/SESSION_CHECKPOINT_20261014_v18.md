# Checkpoint v18 — GB-012 completed (2026-10-14)

**Last actual task DONE: GB-012. NEXT: GB-013, FY2024/25 UK supplement.** All previous originals and versioned files preserved. Verified main head before checkpoint: `16562432e6354473eda9b6c00633956b7fe164ba`.

## Actual source and result
Original `GB/costs-per-prison-place-prisoner-2023-24-supplementary-information.ods`, Git blob `59f04c2bb5a7c0b7aeb8b54eca7cc506131aa277`, 42,993 bytes. `Cover!A19`: **3 April 2025**. England and Wales FY2023/24, not UK-wide/calendar-year. Three actual source sheets: Cover 8, T1 43, T2 44 = **95 nonempty rows**, A–K source strings saved. Source worksheets contain no formula attributes. Original publisher binary hash unverified.

Exact national `T2_Supplementary_Data`: **B59 CNA 82,258**; **C59 FY-average prisoners 87,129**; **D59 direct cost £3,054,089,482**; **H59 overall cost £4,687,647,356**; **E59/F59 £37,128/£35,053** direct per place/prisoner; **I59/J59 £56,986/£53,801** overall unit costs. Source `D49` concession costs **£589,026,938** nested in Non Pay parent `D42`. Publisher printed whole numbers sometimes differ by up to **3 units** from sums of independently rounded components; preserve original values. All 45 source-anchored QA checks passed.

**New MB-026:** Altcourse switches from FY2022/23 PFI (`T1!A29` historical Dec1997 start) to FY2023/24 Manage & Maintain (`T1!A42` new Jun2023 start). MoJ annual account separately says May2023; start-month meanings unresolved. Contract counts 8 PFI+6 M&M → 7 PFI+8 M&M. This is NOT another physical Altcourse prison.

**New MB-027:** FY2023/24 first financial row for Fosse Way `T1!A47:G47`: May2023 start, 1,143 CNA, 974 FY-average prisoners, £58,338,786 overall, £51,048/place. MoJ official announcement verifies first prisoners 29 May 2023. Comparability to fully operating full-year sites needs verified available place-days. Five Wells `T1!A46` now 1,680 CNA, 1,567 annual-average prisoners, £54,213,607. Detailed original FY2023/24 prison file already has 120 validated financial rows, none duplicated.

## Saved artifacts (each verified by fetching from GitHub)

- [All 95 source rows](progress/GB-012_2023_24_supplement_full_source_cells_v1.csv): blob `d4200c301faf0af8c6c0c0c1628c5229b7585a48`.
- [45 arithmetical checks](progress/GB-012_2023_24_supplement_arithmetic_QA_v1.csv): blob `a976b4abe9bdb02594c9a9ab837c75bd0d576c0f`.
- [Detailed forensic/source report](progress/GB-012_2023_24_supplement_source_audit_v1.md): blob `17734a6f86186e97baa5d5d4c48a546384e77671`.
- [Indicator × period register v15](INDICATOR_PERIOD_COVERAGE_REGISTRY_v15.csv): **1,111 entries**, +25 FY2023/24 source measures R01087–R01111, blob `d314d9ded50d882e85c2099fefa16a6d320ab6be`. Large CSV fully validated by GitHub contents text (37 fields each).
- [Methodological issues v10](METHODOLOGICAL_BREAKS_AND_ANOMALIES_v10.csv): **27**, +MB-026 and MB-027; blob `55b3276c57f3994896eb064bf31d92294004f205`.
- [Queue v16](MICROTASK_QUEUE_WAVE1_v16.csv): **16 DONE, 1 prior-audit reconciled, 1 NEXT, 10 PENDING, 2 BLOCKED, 1 WAITING**; blob `1cfefc9af1db3c82b23160ecf5c77736269414ad`.

**Plan:** 31 tasks total; **17 completed/reconciled**, **14 remaining** (11 actionable including GB-013, plus 3 dependency-limited). Remaining GB-013 UK FY2024/25 supplemental, GB-014–018 narrative cost PDFs, GB-019 UK synthesis, RU-002–004, INT-002, plus unresolved GB-002/003 and RU-001. This first wave is not the complete archived research corpus.

**Next microtask GB-013:** `GB/costs-per-place-per-prisoner-2024-2025-supplementary-information.ods`. Reuse 119 previously checked FY2024/25 detailed finance rows, do not extract them again. Check new source edition, Fosse Way second FY, Altcourse contract category, source expense hierarchy and exact FY dates. Update queue and twin registers only on new source evidence. No background work.

# SESSION CHECKPOINT v13 — GB-007 FY2018/19 prison cost supplementary (2026-10-14)

**Last actually completed task: GB-007 DONE**. Original source fetched and decompressed; source SHA and full source physical rows inspected; all new artifacts re-fetched after creation. **GB-008 NEXT**. Previous `main` verified head `ab0ddef9e1aa29ac5d7ef22628e25b3b65aa4961`. Add-only versioning; no original source, by-prison source row or old catalog version overwritten.

## Original source and source rows
- `GB/costs-per-prison-place-prisoner-2018-19-supplementary-information.ods`, Git blob `b76237a93416b737e437ef32b8a0e75566957abe`, original **42,316 bytes**. `Cover_!A10` 2018-19, `Cover_!A19` **Published 31 October 2019**. England and Wales FY2018/19, not UK-wide or 2019 calendar year.
- Three genuine source ODS tabs, **97 real nonempty physical rows**: `Cover_` 8, `T1_Contracted_Prisons` 41, `T2_Supplementary_Data` 48. Every A–K stored cell, including unlabeled residual and zero cells, transcribed into full source CSV with exact physical sheet row. No `table:formula` attributes in three audited tabs, no external links followed.
- Existing 2018/19 **117 initial + 117 restated by-establishment** source financial accounting rows independently inspected earlier; NOT re-extracted or duplicated.
- **Source T1** `A5:A7`: 103 public establishments + 14 contracted = **117** classified by main type at FY end (`A13`); numerical equality with the 117 original FY financial rows does NOT establish one-to-one facility identity.
- **National source totals** `T2_Supplementary_Data!B59:J59`: **78,774** places (`B59`); **82,751** FY-average prisoners (`C59`); original direct expense **£2,162,543,754** (`D59`), overall **£3,404,055,441** (`H59`); direct cost per place/prisoner **£27,453 / £26,133**; overall cost per place/prisoner **£43,213 / £41,136**. `D49` **Service Concession Arrangements £473,874,996**.
- FY2018/19 source directly agrees with previously audited restated source's original (pre-revision) `T2_Summary_Comparison!D5` £2,162,543,754. Prior source's `D6` £129,111,488 education/training attributable change yields revised `D7` **£2,291,655,242**, while prior `H5=H7` **£3,404,055,441** overall. Reuse **MB-004**; no false new year or economic cost shock.
- Source `T1!A10:A11` and `T2!A64`: public/private cost scope not directly comparable; `T2!A63` categorizes mixed prisons by majority use; FY-average population is NOT one-day prison stock and CNA is NOT usable/operational capacity.
- `T2!D42` publisher **Non Pay parent £926,110,397**, children `D43:D50` printed integer source cells sum to **£926,110,399**, difference **+£2** from individual-rounded values. Do not add parent plus children. Payroll `D41` £1,357,655,066, signed Income `D51` −£121,221,709. Overall-only `H53:H58` separate from direct.
- `T2!C7` and `C36` each have **unlabeled −1** printed entries; labels absent so cannot claim publisher motivation beyond residual-like numerical role; no negative prisoner or source-line interpretation.
- **33** arithmetic reconciliation equations with physical source references; largest abs discrepancy **2 in corresponding check units** (GBP, places, or rounded population as tagged). Publisher `T1!A56:A57`, `T2!A67` warns sums of rounded printed figures may differ from unrounded-source-formed totals.

## Catalogues outcome

- [Indicator × period registry v10](INDICATOR_PERIOD_COVERAGE_REGISTRY_v10.csv): **983 evidence-classified entries**, newly added **25 `R00959`–`R00983`** 2018/19 source original-vintage national accounting and denominator/unit cost measures; Git blob `8c9ad987f769b8fa0d0396969d8da2fa25a38c8a`, commit `31a1ec9c52929a8967447f91361019d05fdc90b6`. **Not 983 comparable indicators or time series**.
- [Methodological breaks v6](METHODOLOGICAL_BREAKS_AND_ANOMALIES_v6.csv): unchanged at **20** issues; **NO_NEW_BREAK**. Existing MB-004 restatement, MB-010 private/public perimeter, MB-020 historical building/capital category caption retained. Unlabeled residuals documented in QA instead of invented new break.
- [Microtask queue v11](MICROTASK_QUEUE_WAVE1_v11.csv): **11 DONE**, 1 DONE_PRIOR_AUDIT_RECONCILED, 2 BLOCKED, 1 WAITING, 15 PENDING, 1 NEXT = 31; **GB-008 NEXT**. Blob `31b4ae2305183e2e3d782d26a6ca4dae9437a6bb`, commit `ab0ddef9e1aa29ac5d7ef22628e25b3b65aa4961`.

## Artifacts saved and independently re-fetched

1. [GB-007 all 97 source rows A–K](progress/GB-007_2018_19_supplement_full_source_cells_v1.csv), source-row provenance, Git blob `2cd1f668e3ff70035287a829769b831885934181`, commit `6af64e0bfb79fce71989c782c35af4898fb9bb0b`.
2. [GB-007 33 reconciliations](progress/GB-007_2018_19_supplement_arithmetic_QA_v1.csv), blob `907183000f081adccf6f3477fed2fbfb1bced0c3`, commit `260b886108aa16f2fa76da5c1e8b5c556c297d2a`.
3. [GB-007 detailed source forensic QA](progress/GB-007_2018_19_supplement_source_audit_v1.md), blob `5b0b51c31a9f0f9ab0b4e61e112465b4e84dac0e`, commit `a8e2e9c3b6125ef213491f82d3d380af84eead8d`.
4. [GB-007 additive QA precision correction](progress/GB-007_2018_19_source_QA_erratum_v1.md), blob `90cd7e1627ed20103d19fffdcf070a595ea2f3a4`, commit `f6e5b13547324967e90f87f4a3c9a57dadc78ee6`. This is authoritative for exactly **+£2** children minus printed Non Pay parent; earlier QA sentence saying "equal" was too loose.

## NEXT small task: GB-008 FY2019/20 original financial supplement

Original `GB/costs-prison-place-prisoner-2019-20-supplementary-information.ods`. First consult latest [queue v11](MICROTASK_QUEUE_WAVE1_v11.csv), [indicator registry v10](INDICATOR_PERIOD_COVERAGE_REGISTRY_v10.csv), [break ledger v6](METHODOLOGICAL_BREAKS_AND_ANOMALIES_v6.csv), and **MB-005** concerning July 2019 public takeover of Birmingham (FY2019/20 has 118 operator-period financial source lines and 117 reported institution categories). Also consult [102-source-sheet cost inventory](gb_cost_original_22_spreadsheets_102_worksheets_v2.csv) before extracting anything already reviewed. Only audit missing exact source measures, verify publication edition, source cells, financial year and rounding; decide updates to both catalogues, queue v12, checkpoint v14, index v19.

Original Git SHA-1 identifies repository binary only, not publisher SHA-256; no background jobs currently run.

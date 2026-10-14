# SESSION CHECKPOINT v15 — GB-009 original FY2020/21 prison financial supplementary (2026-10-14)

**Last COMPLETED microtask: GB-009 DONE. NEXT: GB-010 FY2021/22.** Git `main` reference independently confirmed before this checkpoint: `2ce33e6f8c60f129790d77134aac398168518fdd`. Existing originals, prior archive versions and source panels remain unchanged (add-only). No background jobs are running.

## Source identity and direct content verification

- Original `GB/costs-per-prison-place-prisoner-2020-21-supplementary-information.ods`, Git blob SHA-1 `afd2878188b41d88fed7f39e6cd255cae95c87c6`, **41,987 bytes**. This confirms repository binary identity, NOT external publisher SHA-256 equality.
- Source cover `Cover_!A10` = 2020-21 supplementary, `Cover_!A19` = **Published 27 January 2022**. Source scope **England and Wales** prison accounts; FY2020/21 is **1 April 2020–31 March 2021**, NOT 2021 calendar year.
- Original ZIP/ODS `content.xml` directly parsed (**815,857 bytes decompressed**) and all real sheets audited: `Cover_` **8**, `T1_Contracted_Prisons` **39**, `T2_Supplementary_Data` **44** nonempty **physical worksheet rows**, **91 in all**, source A–K numeric/text cells preserved with original sheet row addresses. No `table:formula` attributes on those three sheets; no external formulas followed.
- Detailed institution-level FY2020/21 originally published file has **117 source finance rows / 936 already independently checked numeric fields** in `gb_cost_FY2018_21_469_raw_operator_facility_year_rows_v2_physical_rows.csv` and `gb_2018_21_469_rows_independent_3752_fields_and_Birmingham_restatement_QA_v1.md`. **Do not produce another 117-row duplicate.**

## Verified publisher original FY2020/21 national source values

Original worksheet `T2_Supplementary_Data`:
- `B59`: **79,364 CNA places**; certified normal accommodation, NOT operational/useable capacity.
- `C59`: **78,959 annual-average prisoners**; FY mean, NOT a one-day prison stock.
- `D59`: **£2,583,235,767 Direct Resource Expenditure**.
- `H59`: **£3,822,319,464 Overall Resource Expenditure**.
- `E59,F59`: direct cost per CNA place / FY-average prisoner **£32,549 / £32,716**.
- `I59,J59`: overall cost per CNA place / FY-average prisoner **£48,162 / £48,409**.
- `D49`: **£492,029,748 Service Concession Arrangements**, a child of Non Pay.
- `D41`: **£1,552,786,632 Payroll**; `D42`: **£1,080,644,846 Non Pay parent**; `D51`: **−£50,195,711 signed Income**. Eight children `D43:D50` sum to the Non Pay parent exactly in displayed pounds; **do not add the parent to the children**. Additional allocations `H53:H58` are overall-only, not direct.

## Proven source accounting and data quality boundaries

1. **No FY2019/20 Birmingham hidden O&M subtotal amount is present this FY.** `T1!A5,A6`: 104 public + 13 contracted **at FY-end**, total 117; `T1!A22:A38` has 10 named PFI facilities and `T1!A42,A45,A46` has 3 named O&M facilities. Publisher subtotals `T1!C38:E38`, `C47:E47` match those names up to one printed unit. Existing MB-005/MB-021 are **past FY2019/20-specific** operator-period cases, not assumed current in FY2020/21.
2. **Small publisher discrepancies explicitly retained** (not 'fixed'): `T1!C5` public CNA = **66,697**, `T2!B19` = **66,696**; `T1!C5 + C6` = **79,365**, whereas T1 `C7` and T2 `B59` national CNA both **79,364**. Likewise T1 `E7` national overall £3,822,319,463 while T2 `H59` prints £3,822,319,464. Exact relevant original publisher values saved, largest check difference **one whole unit**. `T1!A54:A55`, `T2!A67` state totals may differ from rounded printed components; the CNA discrepancy is flagged as small source presentation QA and does **not** prove a one-place closure or method discontinuity.
3. **FY2019/20 → FY2020/21 numeric shifts verified, meaning unresolved:** `T2!D43` Non payroll services **£186,243,148 → £56,153,094**; `T2!D48` Prisoner related costs **£185,656,507 → £287,153,177**; average prisoner count **82,890 → 78,959** and overall nominal resource spending **£3,536,900,071 → £3,822,319,464**. Original supplementary source `T2!A63:A67` does **not** provide a definitional bridge or causal explanation. **Do not infer COVID causation, stable component equivalence or mechanical spending elasticity** from catalogue data alone.
4. `T1!A10:A11`, `T2!A64` explicitly warn public/private accounting perimeters not directly comparable (MB-010). `T2!A63` describes majority-use classification of mixed prisons; original `T2!A53` wording still *Depreciation of buildings and capital repayment*, not identical to FY2016/17 category (existing MB-020).

## New artifacts saved then independently re-fetched

1. [Original 91 physical nonempty source rows A–K](progress/GB-009_2020_21_supplement_full_source_cells_v1.csv) — Git blob `a916c3fba4ed6ce54aa05f2c42c887c70c1f112a`, write commit `2938be34b01d28bac20aa965bcd754e019a1a25a`.
2. [36 source-cell reconciliation equations](progress/GB-009_2020_21_supplement_arithmetic_QA_v1.csv) — blob `c1032d627ae68a7a9fbc20c9de1db97e884430c1`, commit `706e8231d800ff216d93a84fa86db9f1d1b25b06`.
3. [Detailed GB-009 original publisher source QA](progress/GB-009_2020_21_supplement_source_audit_v1.md) — blob `d890be08b01fd7ca40e219c172b163942f0f00be`, commit `d3f1d32ffc3728639fa4b291454876ef7588ea5b`.
4. [Indicator × reporting-period registry v12](INDICATOR_PERIOD_COVERAGE_REGISTRY_v12.csv): **1,036 evidence-classified records**, newly added **25 source-original FY2020/21 measures R01012–R01036**. Blob `65bf684bebf95edf10361060cc5ce5d061eceaa2`, commit `e004825cd94fe26266af052ac17ee73c11f61e1f`.
5. [Methodological breaks v7](METHODOLOGICAL_BREAKS_AND_ANOMALIES_v7.csv): **unchanged, 21 issue records** — **NO_NEW_BREAK** for GB-009; the 1-place / £1 original source issues are preserved in source QA without an unsupported methodological-break conclusion. Git blob `efe563b894417d431da696268f604394abc4fcce`.
6. [Atomic task queue v13](MICROTASK_QUEUE_WAVE1_v13.csv): **13 DONE, 1 DONE_PRIOR_AUDIT_RECONCILED, 2 BLOCKED, 1 WAITING, 13 PENDING, 1 NEXT = 31**. GB-009 DONE, **GB-010 NEXT**. Git blob `638014f127ed7511673cd04acaf28d62bb036d19`, commit `2ce33e6f8c60f129790d77134aac398168518fdd`.

## NEXT GB-010 — FY2021/22 national supplementary source

Target original `GB/costs-per-prison-place-and-prisoner-2021-2022-supplementary-information.ods` (exact queue path, not guessed). Before any extraction consult [queue v13](MICROTASK_QUEUE_WAVE1_v13.csv), [indicator registry v12](INDICATOR_PERIOD_COVERAGE_REGISTRY_v12.csv), [breaks v7](METHODOLOGICAL_BREAKS_AND_ANOMALIES_v7.csv), latest [GB-009 source QA](progress/GB-009_2020_21_supplement_source_audit_v1.md), source 102-tab cost inventory, and earlier already fully audited FY2021/22 **by-establishment** panel in the 2021/22–2024/25 financial source register. Check whether 2021/22 source changes structure, national denominators, staff cost/capital/education categories or contracted estate scope. Don't infer a pandemic effect or inflation without primary source or appropriate adjustment. Only create new source-cell QA and missing source-specific FY measures. Explicitly decide two catalogues, then add-only queue v14, checkpoint v16 and index v21. Preserve originals and previous file versions. No asynchronous work ongoing.

# GB-009 — original FY2020/21 prison costs supplementary source forensic QA

**Completed 2026-10-14.** Original `GB/costs-per-prison-place-prisoner-2020-21-supplementary-information.ods`, original **Git blob SHA-1** `afd2878188b41d88fed7f39e6cd255cae95c87c6`, **41987 bytes**; `content.xml` 815857 uncompressed bytes decoded directly from ZIP/ODS. **England and Wales**, not UK-wide; fiscal year 2020/21 (1 April 2020–31 March 2021), not calendar-year data. External publisher-hosted binary hash is **not** independently verified.

## Source, original rows and edition
- `Cover_!A10` says 2020-21 supplementary, `Cover_!A19` confirms **Published 27 January 2022**, publisher HMPPS/MoJ.
- Real tabs: `Cover_` **8**, `T1_Contracted_Prisons` **39**, `T2_Supplementary_Data` **44** nonempty original physical rows, **91 in total**, all original A–K stored numeric/text values plus original sheet row preserved in [full source-cell audit](GB-009_2020_21_supplement_full_source_cells_v1.csv). Three original sheets have no `table:formula`; no author formula calculations nor external reference follow-up. Source repeated blank tails excluded.
- Prior original **117 by-establishment FY2020/21 accounting lines**, with independent checks of **936** original numeric fields, already archived in `gb_cost_FY2018_21_469_raw_operator_facility_year_rows_v2_physical_rows.csv` and separately described in `gb_2018_21_469_rows_independent_3752_fields_and_Birmingham_restatement_QA_v1.md`. **No duplicate facility rows created.**

## Original-publisher FY2020/21 national figures (source worksheet `T2_Supplementary_Data`)

| Measure | Original source cell | Reported value |
|---|---|---:|
| Certified Normal Accommodation CNA (not operational capacity) | `B59` | **79364 places** |
| Annual-average prisoner population (not a one-day snapshot) | `C59` | **78959 persons** |
| Direct Resource Expenditure | `D59` | **£2583235767** |
| Overall Resource Expenditure | `H59` | **£3822319464** |
| Direct cost per place / per prisoner | `E59/F59` | **£32549 / £32716** |
| Overall cost per place / per prisoner | `I59/J59` | **£48162 / £48409** |
| Service Concession Arrangements, Non Pay child | `D49` | **£492029748** |

Source national totals in `T1_Contracted_Prisons!C7:E7` also show 79,364 CNA / 78,959 population / £3,822,319,463 overall while `T2!H59` shows **£3,822,319,464**. The difference is GBP **1**, consistent with published rounding caveat but still explicitly preserved.

## Establishment counts, perimeter and fine numerical differences

`T1!A5:A6` identifies **104 public + 13 contracted FY-end institutions = 117**, matching previous year 104+13, while three listed O&M contracts and 10 PFI names sum to 13 contracted names. **The FY2019/20 G4S Birmingham hidden operator-period contribution (MB-021) is not reproduced in FY2020/21**: here the three named O&M and ten PFI subtotals reconcile to group totals under original rounding. Existing MB-005 and MB-021 remain relevant **historical** source issues, not assumptions for this year.

- In `T1!C5`, public CNA = **66,697**, in `T2!B19`, public CNA = **66,696**; both original XLSX-equivalent source numbers independently retained, **difference +1 CNA place**. `T1!C5 + T1!C6 = 79,365`, while T1 printed national `C7` = **79,364** and T2 national `B59` = **79,364**. Cannot silently harmonize the divergent *published integer* CNA without publisher definition. Note this **ONE-PLACE source inconsistency**, and avoid calling it evidence of one prison/closure: classification vs CNA total can differ by rounded presentation. Unlike G4S MB-021 this is only a small displayed-source discrepancy and is not independently proven methodological scope change.
- The group total `T1!E7` (£3,822,319,463) differs by **−£1** from `T2!H59` (£3,822,319,464). Both source cells retained, do not overwrite one with the other. `T1!A54:A55` and `T2!A67` explicitly say totals come from **unrounded** source values, potentially differing from rounded parts; precise publisher source numbers, not corrected means, are the archived truth.
- CNA is a certified accommodation number, NOT used/operational accommodation, and annual FY mean population cannot be treated as one-day or prison-year average of site-specific reported monthly points without a defensible method. Public/private expenditures remain **not directly comparable** (`T1!A10:A11`, `T2!A64`); institution type based on FY-end classification and mixed use assigned by majority-use source rules (`T2!A63`).

## Original cost-accounting hierarchy and screening

- `T2!D41` Payroll £1552786632, `D42` **Non Pay PARENT** £1080644846, eight children `D43:D50` (not additional amounts on top of parent), `D51` signed Income £-50195711. Six **overall-only** `H53:H58` allocations are not direct prison expenditure; `D49` concession costs are nested in Non Pay.
- `T2!A53` says **Depreciation of buildings and capital repayment**, matching FY2017/18–FY2019/20 but different FY2016/17 label, existing **MB-020** still open.
- Compared with verified FY2019/20 exact source cells, **Non payroll services** `D43` fell **£186,243,148 → £56,153,094** and **Prisoner related costs** `D48` rose **£185,656,507 → £287,153,177**; original FY2020/21 footnotes `T2!A63:A67` do **not** provide a publisher reclassification bridge. Changes may reflect pandemic conditions, contract treatment, classification or operating costs — **none is causally established by these two source supplements alone**. Flag for external official accounting-note investigation, **not as proven methodological break**.
- Source FY2020/21 average population is **78,959**, down from FY2019/20 **82,890**, while original Overall Resource Expenditure rises from **£3,536,900,071** to **£3,822,319,464**. This is consistent with, but **does not identify**, inflexible spending under falling occupancy. Theoretical economic causation is an external analysis stage, not a raw-file cataloguing conclusion.

## Arithmetic QA; dual-catalog decision

[36 original physical cell anchored reconciliation equations](GB-009_2020_21_supplement_arithmetic_QA_v1.csv) check public/contracted totals, 10 PFI and 3 O&M names, multiple independent national category partitions, signed payroll/nonpay/income, and overall-only allocations. Largest absolute difference in displayed source units **1** (source-unit differences from rounded whole values; see each row's units); no anomaly was "corrected" through source overwriting. **No additional 117-source-line facility panel created.**

**Indicator×period registry:** append **25 source-original FY2020/21 national observed accounting and denominator components** with exact source cell, fiscal-year vintage and Git SHA; do not double count Non Pay hierarchy. **Methodological breaks ledger: NO_NEW_BREAK**. Existing MB-005/021 historical Birmingham issue, MB-010 public/private perimeter and MB-020 category-label difference suffice. FY2020/21 1-place public CNA inconsistency is documented here as source presentation QA, not a proven definitional discontinuity. Next GB-010 FY2021/22.

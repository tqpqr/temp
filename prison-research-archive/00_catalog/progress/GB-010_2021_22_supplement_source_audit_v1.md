# GB-010 — original FY2021/22 MoJ/HMPPS prison costs supplementary: source-cell forensic audit

**GB-010 COMPLETED, 2026-10-14.** England and Wales only; fiscal year 2021/22 (1 April 2021–31 March 2022). Source is neither a whole-UK nor a 2022 calendar-year financial dataset.

## Original file and source content
- `GB/costs-per-prison-place-and-prisoner-2021-2022-supplementary-information.ods`, original Git SHA-1 `a0346d48d785c01e7fb1a8dcf55f1379d1d5a2da`, 42056 source bytes, 830191 uncompressed bytes in ODS `content.xml` read directly. Publisher-hosted historical original byte SHA-256 not independently verified.
- `Cover_!A10` 2021-22 Supplementary information, `Cover_!A19` **Published 9 March 2023** (HMPPS/MoJ). Three real spreadsheet tabs: `Cover_` **8** nonempty original rows, `T1_Contracted_Prisons` **40**, `T2_Supplementary_Data` **48**: **96 exact source nonempty physical rows**. All A–K original numeric values/text and physical source row addresses stored in [GB-010 full original source cells](GB-010_2021_22_supplement_full_source_cells_v1.csv); absent publisher cells remain blank, zero values retained. No original `table:formula` attribute in three sheets, no formulas recalculated, no external links followed.
- Original **FY2021/22 119 institution-level financial observations** were already independently collected under `gb_cost_FY2021_22_to_FY2023_24_358_establishment_source_rows_v2_physical_rows.csv` (and 477-row FY2021/22–24/25 source union). **Do not re-extract/double count those 119**. Publisher year-end count `T1!A5:A6` is **105 public + 14 contracted = 119** but numerical equality alone is not institutional identity proof.

## Original source measurements

| Measure | Publisher original | Source anchor |
|---|---:|---|
| CNA places (NOT operational/usable capacity) | 80362 | `T2_Supplementary_Data!B59` |
| FY-average prisoner population (NOT one-day stock) | 79113 | `T2!C59` |
| Direct resource expenditure GBP | 2490214500 | `T2!D59` |
| Overall resource expenditure GBP | 3752632094 | `T2!H59` |
| Direct cost per CNA place / average prisoner | 30987 / 31476 GBP | `T2!E59/F59` |
| Overall cost per CNA place / average prisoner | 46696 / 47434 GBP | `T2!I59/J59` |
| Service Concession Arrangements | 502322541 GBP | `T2!D49` |

`T1` public+contract and PFI/O&M groups and `T2` published category partitions are separately checked against the publisher totals; see [original 35-equation arithmetic ledger](GB-010_2021_22_supplement_arithmetic_QA_v1.csv). Maximum absolute printed-component discrepancy **1 units in the explicitly tagged units**. `T1!A55:A56` and `T2!A67` explain unrounded publisher totals may not equal sums of separately rounded displayed parts. Source numbers are preserved even when one-pound rounding differences appear.

## New partial-year comparability warning — Five Wells

- The issuer `T1_Contracted_Prisons!A45,B45` directly identifies **Five Wells**, contract start **Feb 2022** (inside the LAST TWO MONTHS of FY2021/22). `C45` CNA **960 places**, `D45` FY-average population **205**, `E45` Overall Resource Expenditure **£7,926,414**, `F45/G45` published overall unit values **£8,257 per CNA place / £38,760 per average prisoner**.
- Source-independent prior by-establishment original `GB/costs-per-prison-place-and-prisoner-by-individual-prison-2021-2022.ods`, Git blob `f7d847c3477e3fcc3e4e563b723cfa00cda3e310`, `T3_Cost_by_Establishment!B34,C34,H34,I34,J34` exactly confirms **960, 205, £7,926,414, £8,257, £38,760** under name Five Wells. The original year end estate has 14 contracted prisons vs 13 in FY2020/21 and original O&M named list has new Five Wells (4 vs 3).
- Published unit-place amount `E45/C45` etc reflects FY total divided by **reported 960 CNA**, while original source explicitly gives a **February 2022** contract start inside FY. This combination raises a confirmed *partial-year comparability issue*: **£8,257/place is not automatically a comparable full-year operational efficiency or all-year unit cost**. **Do not claim** actual prison opening date, months of actual services, staff ramp-up or publisher use of a full-year CNA time-exposure denominator without further official records. Historical event category **MB-022** should record these source fields and classify full-year economic interpretation as unresolved.
- Published Five Wells ratio of annual average population to CNA also is not direct occupancy measured only over its operational months. Do not treat 205/960 as its mature operating occupancy rate or infer its staffing/cost elasticity from this first FY.

## Expense hierarchy and unresolved cross-year movements
- `T2!D41` Payroll 1503126526 GBP; `D42` **Non Pay PARENT** 1044165690 GBP; **8 nested children** `D43:D50` (NOT additional amounts on top of parent); `D51` Income -57077716 GBP (negative sign retained); additional six overall-only items `H53:H58`. `D49` Service Concession Arrangements 502322541 belongs inside parent Non Pay.
- `T2!A53` continues caption **Depreciation of buildings and capital repayment**, so FY2020/21→FY2021/22 no newly verified caption break here. Earlier FY2016/17 buildings and central ICT caption difference **MB-020** remains unresolved.
- Original FY2020/21 **Non payroll services** `D43` £56,153,094 vs FY2021/22 **£30,512,062**; FY2020/21 **Prisoner related costs** `D48` £287,153,177 vs FY2021/22 **£286,303,117**. Any pandemic/contracting/classification or inflation interpretation is beyond this file, not verified by issuer footnote in the supplementary sheets.
- `T1!A10:A11`, `T2!A64` still warn direct public-versus-private finance comparisons invalid without adjusting PFI and accounting scope. `T2!A63` categorises whole mixed prisons by majority use. CNA is not operational capacity. Average population is financial-year mean, not point date stock. All 3 source tabs are original stored values, not annualized rates calculated by the assistant.

## Registry decisions
- **Indicator registry** add new 25 national FY2021/22 issuer-original numeric/cost-component observations with physical cell anchors and publisher vintage; optionally source direct Five Wells partial-year item as an explicitly **facility-specific observed** record with MB-022 link, avoiding existing by-establishment extraction duplication. **Do not duplicate entire 119 institution source rows**.
- **Methodological breaks** add **MB-022** for **contract-date/partial-year first observation comparability**; do NOT assert an actual accounting error or economic causal explanation. Existing MB-021 past 2019/20 Birmingham case retained.
- Task status **DONE** when registry decisions, source QA, queue and checkpoint saved with direct Git verification. Next **GB-011 FY2022/23** (exact queue source path), check reclassification of 4 establishments in FY2022/23 before comparing institutional cost categories.

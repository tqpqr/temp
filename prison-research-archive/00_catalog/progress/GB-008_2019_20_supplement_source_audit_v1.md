# GB-008 — FY2019/20 original UK prison-cost supplementary ODS: full source audit

**Completed 2026-10-14.** England and Wales prison estate only, financial year 2019/20 (not a 2020 calendar or UK-wide series).

## Source identity
Original `GB/costs-prison-place-prisoner-2019-20-supplementary-information.ods`, Git blob SHA-1 `c5ec73b1d01770d0229f46a85d14f53ebb21d0e6`, **41569 bytes**; `Cover!A10` = 2019-20 supplementary, `Cover!A19` = **Published 29 October 2020**. Exact ODS `content.xml` read directly (838930 uncompressed bytes); source download from publisher not independently byte-identical-verified. Three real tabs, `Cover` **8**, `T1_Contracted_Prisons` **41**, `T2_Supplementary_Data` **44** nonempty physical original rows (**93 total**), source fields A–K copied without changing original numeric strings or blanks to [complete source-cell CSV](GB-008_2019_20_supplement_full_source_cells_v1.csv). All 3 tabs have **zero `table:formula`** attributes; no formulas recalculated. Existing **118 original FY2019/20 institution/operator finance rows** separately verified in prior research, and NOT duplicated.

## Publisher FY2019/20 original source totals

| National reported measure | Original cell | Verbatim source number |
|---|---|---:|
| Certified Normal Accommodation (CNA; not usable capacity) | `T2_Supplementary_Data!B59` | 79232 |
| Annual-average prisoner population (not a one-day census) | `T2!C59` | 82890 |
| Direct Resource Expenditure (GBP) | `T2!D59` | 2401640556 |
| Overall Resource Expenditure (GBP) | `T2!H59` | 3536900071 |
| Direct cost per place / prisoner (GBP) | `T2!E59/F59` | 30311 / 28974 |
| Overall cost per place / prisoner (GBP) | `T2!I59/J59` | 44640 / 42670 |
| Service Concession Arrangements (GBP; Non Pay child) | `T2!D49` | 470891780 |

Publisher `T1!A5:A6` lists **104 public and 13 contracted establishments** at FY-end, versus FY2018/19 **103+14**; the total remains 117. `T1!A13` uses main type at year end, while annual detailed FY2019/20 finance has **118** financial operator-period lines. **Birmingham transferred to public management in July 2019** (existing event MB-005). Do not count two finance lines as different physical prisons.

## NEW exact finding — contracted O&M subtotal includes unlisted operator-period financial contribution (MB-021)

In the original FY2019/20 `T1_Contracted_Prisons`, O&M detailed named source rows are **Doncaster row 43; Oakwood row 46; Sodexo Northumberland row 47**, with published subtotal at row 48. `G4S Birmingham` is **not listed** in the FY2019/20 contracted-source list (unlike FY2018/19); nevertheless the difference between publisher O&M subtotal and these three named rows is:
- **CNA places** `274` from `C48 - (C43+C46+C47)`;
- **FY-average persons** `234` from `D48 - (D43+D46+D47)`;
- **Overall Resource Expenditure** **£7586785** from `E48-(E43+E46+E47)`.

An already independently audited original source, `GB/costs-prison-place-prisoner-individual-prison-2019-20.ods`, Git blob `969df2a0a07b426ab6440e193bc8ea446637cc43`, exact original `T3_Cost_by_Establishment!B156:J156`, contains **G4S Birmingham** (FY transition operator-period financial line) **CNA 275, annual-average population 235, overall expense £7586786**. Each matches the FY2019/20 supplementary source O&M residual to within **1 original published unit** (source independently rounded whole units). This is strong source-to-source evidence that the subtotals include the historical private operator-period financial contribution even though the list includes only three named current contracts. No new prison created; **do not remove the £7586785 difference** or claim the publisher subtotal itself is wrong. Distinction between year-end contracted *identity list* vs annual *expenditure aggregate* is an independent explicit source presentation mismatch, and should be catalogued as **MB-021** linked to the broader operator-period event **MB-005**. Source does not explicitly narrate the subtotal's construction; the residual attribution is mathematically corroborated, not claimed to be a publisher explanatory footnote.

## Accounting and perimeters
`T2!D41` Payroll GBP 1457687306, `T2!D42` Non Pay **parent** GBP 1066908261, eight `D43:D50` nested children, `T2!D51` signed Income GBP -122955011, six **overall-only** overhead/capital allocation categories `H53:H58`. **Never add Non Pay parent plus children**. `T2!D49` Service Concession Arrangements GBP 470891780 belongs within Non Pay; possible historical category changes from FY2015/16 (MB-001–003) remain unresolved. `T2!A53` uses "Depreciation of buildings and capital repayment" as FY2017/18 and FY2018/19; older FY2016/17 caption differs (MB-020).

**Unresolved screening issue:** source `T2!D43` Non payroll services = **£186,243,148** vs previously source-verified FY2018/19 £50,452,976, and `D45` Admin running costs = **£1,052,657** vs prior £10,028,427. Without explicit publisher reclassification bridge, cannot know whether operational change, accounting recode or mix; document as **OPEN comparative analytical question**, not new confirmed break.

`T1!A10:A11` and `T2!A64` warn that public vs contracted expenses are NOT directly comparable (capital interest, other service-scope differences). 2019/20 issuer notes `T1!A11` do not repeat the older explanatory private healthcare phrase, but **text omission does not prove a healthcare scope change**. `T2!A63` classifies mixed-use prisons wholly by majority category. `T1!A55:A56`, `T2!A67` say rounding of source components means totals formed on unrounded amounts need not equal sum of printed integers.

## Reconciliations and twin-catalogue outcome
[32 source-cell arithmetic checks](GB-008_2019_20_supplement_arithmetic_QA_v1.csv), including the **three explicit O&M residual-to-G4S source-to-source checks** above, yield maximum remaining rounding discrepancy **2 in corresponding original source units**. The **unexplained before-crosswalk O&M source gap** is not a standard rounding error; it is specifically crosswalked to original G4S Birmingham entry. All other publisher national total vs category sums checked with original integer values; original *source* totals remain authoritative.

- **Indicator × period registry:** add 25 verified FY2019/20 national totals/accounting categories, exact cells and original source blob; 118 detailed finance source lines already in archive **not copied again**.
- **Methodological-break registry:** add **MB-021** as a confirmed source presentation/scope mismatch, cross-referenced to existing MB-005 (Birmingham operator transition). No other new break inferred from numerical changes.
- **Next task GB-009 FY2020/21** (subject to queue update) with pandemic-era caveats verified only when stated by source, not inferred from year name.


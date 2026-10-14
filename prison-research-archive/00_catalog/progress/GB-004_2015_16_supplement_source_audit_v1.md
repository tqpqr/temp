# GB-004 — COMPLETE: FY2015/16 MoJ prison-cost supplementary workbook, source-faithful audit

**Original file:** `GB/costs-place-cost-prisoner-2015-16-supplementary-information.xlsx`
**Source original Git blob SHA-1:** `c5605a10b66c2b2e312f07329153a436a90451d5`
**Audit scope:** ONE original XLSX, covering all three true sheets and all nonempty raw worksheet rows. Source data only, not a cross-year matched panel and not the missing FY2015/16 *restated* by-prison edition.
**Workbook publication:** Cover!A19 says **Published 27 October 2016**. Cover!A12–A17 identify the National Offender Management Service, Ministry of Justice and the Management Information Addendum. The workbook internal `docProps/core.xml` modified date is 2016-10-19 (not the official release date).

## Exact extraction
- CSV: [GB-004 source worksheet cells A–K](GB-004_2015_16_supplement_full_source_cells_v1.csv). `100` nonempty physical XLSX rows; all retained original textual and stored numeric values in columns A–K; blank spreadsheet cells remain blank, not zero. Each record has original path, original SHA, verbatim worksheet name and **physical Excel row number**.
- Sheet `Cover ` (trailing space is part of exact sheet name): 8 nonempty source rows.
- Sheet `T1_Contracted Prisons`: 41 nonempty rows. Table 1a: public vs contracted (A3:G13). Table 1b: 14 contracted facilities and PFI vs Operate & Maintain (A17:G57).
- Sheet `T2_Supplementary Data`: 51 nonempty rows. Classification by male/female (A3:J6), adults/YOI (A10:J13), public/contracted (A17:J20), England/Wales (A24:J35), and **functional expenditure accounting decomposition** (A39:J68).
- Source ZIP XML has **zero worksheet `<f>` formulas** across these three sheets: numerical values here are stored XLSX cell values, not re-evaluated formulas. The workbook does include **three externalLinks ZIP parts** and **127 legacy defined names containing `#REF!`**; these do **not** establish errors in the extracted stored numerical cells, but Excel's external links are not used or updated.

## Content findings, with original worksheet+cell anchors
1. `T1_Contracted Prisons!C5:G7`: 105 public establishments; 14 contracted; full fiscal-year overall resource expenditure **£2,753,747,261** (E7), Certified Normal Accommodation **78,271** (C7), average population **84,705** (D7). Number of establishments is categorization **as of end of 2015/16** per `A13`; this is not a longitudinal unit key.
2. `T1_Contracted Prisons!A23:G38`: **10 PFI named facilities**; group totals at `C39:G39`; `A43:G48` lists **4 Operate & Maintain facilities**, group totals `C49:G49`; combined `C52:G52`. Contract start dates are explicitly in column B.
3. `T2_Supplementary Data!B19:J20`: published public direct resource expenditure **£1,452,336,159** (D19) and contracted **£445,636,082** (D20). Published overall totals **£2,245,352,178** (H19), **£508,395,083** (H20). Source distinguishing **direct** (D) from **overall** (H) is material: never present overall costs as direct operational response to changing occupancy.
4. `T2_Supplementary Data!A41:J60`: breakdown of payroll, non-payroll services, staff costs, administration, accommodation, depreciation of plant & equipment, prisoner direct costs/regime/training, other costs, **income (negative)**, and buildings/ICT depreciation, rates/rent, major maintenance, regional overheads, PECS apportionment and HQ overheads. Direct expenditure **£1,897,972,242** (`D60`), overall expenditure **£2,753,747,261** (`H60`). These are **national accounting components for this FY**, not facility-component measurements and not evidence of corresponding decomposition in the Russian dataset.
5. **Comparability caveat directly in publisher cells** `T1_Contracted Prisons!A10:A11` and `T2_Supplementary Data!A65`: public and private expenses **not directly comparable** because of different accounting treatment and scope; publisher explicitly notes PFI interest on capital and private healthcare coverage. `T2_Supplementary Data!A64`: each whole prison assigned to its majority prisoner category. `T1_Contracted Prisons!A56:A57` and `T2_Supplementary Data!A68`: averages/expenditures rounded and totals constructed from unrounded numbers.

## Independently recomputed checks (source line sums minus publisher stated totals, GBP)
- `contracted_PFI_10_individual_E_minus_group_total`: **+1 GBP** (within rounding tolerance)
- `contracted_OM_4_individual_E_minus_group_total`: **+0 GBP** (within rounding tolerance)
- `contracted_both_groups_minus_overall_E`: **-1 GBP** (within rounding tolerance)
- `public_plus_private_expense_minus_total_E`: **+0 GBP** (within rounding tolerance)
- `direct_payroll_plus_nonpay_plus_income_minus_total_D`: **+0 GBP** (within rounding tolerance)
- `all_broken_out_overall_components_minus_published_total_H`: **+1 GBP** (within rounding tolerance)
- `sector_overall_minus_total_H`: **+0 GBP** (within rounding tolerance)

This workbook's source cells support **exact layout and provenance** of the listed financial concepts, not a statistical claim that contracted and public sector operating economics are directly comparable. Save remaining cross-year concept map separately as GB-019 after reviewing all supplementary versions.

**GB-004: DONE.** Source extraction has actual physical cell anchors and raw zero/blank distinctions. Next small independent issue: **RU-001**, or continuing numeric GB order **GB-005** if the rotation is deferred. GB-002 remains blocked for binary retrieval; GB-003 dependent on it.

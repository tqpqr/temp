# GB-005 — DONE: 2016/17 MoJ prison-cost supplementary workbook source audit

## Source identity / full read
- **Original repository source:** `GB/costs-per-prison-place-per-prisoner-2016-2017-supplementary-information.xlsx`
- **Original Git SHA-1:** `38e68d1ff7cf3dfe68847819850d24b40427d15d` (independently fetched raw XLSX via connected GitHub and decompressed worksheet XML).
- Original Cover A19 publishes **26 October 2017**; Cover A10 = 2016–17 supplementary information. `T1_Contracted Prisons!G8` identifies **HM Prison & Probation Service** as immediate numeric source.
- [Complete nonempty original source rows](GB-005_2016_17_supplement_full_source_cells_v1.csv): `99` actual XLSX physical sheet rows, columns A–K (including untouched blanks and zero), exact sheet names, original row addresses, source path, Git SHA.
- Three sheets: `Cover ` (trailing space, 8 nonempty rows), `T1_Contracted Prisons` (41), `T2_Supplementary Data` (50). Stored numerical values, **zero `<f>` formulas** in source worksheets. Existing legacy external links/defined names not followed.

## Numeric and methodological facts, original cell coordinates
- `T1_Contracted Prisons!A5:G7`: **108 public prison establishments** and **14 contracted**, CNA 78800 places, average population 84750, overall resource spending **£2,997,687,957**. The published `A13` categorization counts are **as of end of 2016/17**, and not proof of 122 fixed identities across years.
- `T1_Contracted Prisons!A23:G52`: **10 PFI** prisons and **4 Operate & Maintain** prisons; per-facility contract start date in B; group subtotals rows 39, 49 and 52.
- `T2_Supplementary Data!D59`: national **direct resource expenditure £1,943,546,987**.
- `T2_Supplementary Data!H59`: national **overall resource expenditure £2,997,687,957**.
- National non-pay category `T2_Supplementary Data!D42`: **£888,704,203**.
- **Critical accounting-classification feature**: `T2_Supplementary Data!A49,D49` contains **Service Concession Arrangements, £454,911,681** (part of non-pay direct expenses), while analogous inspected `GB-004` FY2015/16 supplement has **NO separate line with this title** in source expenditure classifications. FY2015/16 `T2_Supplementary Data!A43,D43` records **Non payroll services £487,329,372**, FY2016/17 `T2_Supplementary Data!A43,D43` records **£68,670,120**. These row headings/categories are **not stable across the two vintages**. It is UNVERIFIED whether reclassification, methodological revisions, or real cost changes account for the apparent difference; **do not attribute difference to operations**.
- Source `T1_Contracted Prisons!A10:A11` and `T2_Supplementary Data!A64`: public vs contracted not directly comparable (PFI capital-interest accounting, private healthcare scope differences). Source `T2_Supplementary Data!A63`: mixed prisons categorized by majority use. Rounding caveat in `T1_Contracted Prisons!A56:A57` and `T2_Supplementary Data!A67`.
- New published classifications vs FY2015/16: 2016/17 `A48` **Prisoner related costs**, `A49` **Service Concession Arrangements**; FY2015/16 uses `A48` Prisoner direct costs, `A49` Prisoner regime, `A50` Prisoner training, `A51` Other. **No invented category-level continuity.**

## Recomputed publisher subtotal integrity — differences in GBP
- public+contracted E vs published 2016/17 overall: **-1 GBP**
- 10 PFI prison expenditures vs source subtotal: **+0 GBP**
- 4 O&M prison expenditures vs source subtotal: **+1 GBP**
- PFI+O&M source subtotals vs combined: **+0 GBP**
- non-pay detail category components vs published Non Pay: **+1 GBP**
- payroll+non-pay+income vs published Direct: **+1 GBP**
- direct+six allocated overheads vs published Overall: **+0 GBP**
- England + Wales vs national overall: **-1 GBP**
- public+contracted vs national overall: **-1 GBP**

All checks differ by **at most £1**, which fits the printed whole-pound and unrounded-summation caveat. This does not establish direct cross-year comparability of accounting classifications.

## Availability-registry update
The **FY2016/17** exact measured year, original source cells, and `service_concession_arrangements` / `non_payroll_services` etc. can be added as **2016/17 specific national expenditure-component indicator observations** in `INDICATOR_PERIOD_COVERAGE_REGISTRY_v2.csv` along with the analogous **2015/16 FY-specific** categories from completed GB-004. Do not claim a continuous 2015/16–2016/17 `Service Concession Arrangements` series.

**GB-005: DONE**, source original unchanged and original physical cells stored. **Next** GB-014 (2015/16 summary PDF) or rotate to INT-001 (Italy source), after adding new registry coverage.

# Independent UK finance cell and physical-row audit, FY2014/15–FY2021/22 (14 October 2026)

## Problem and resolution
ODS `content.xml` can use `table:number-rows-repeated` to compact blank spreadsheet rows. Some first-pass extractors treated XML row *elements* as their displayed spreadsheet numbers. This introduced **wrong sheet/row/cell addresses**, although the originally extracted **numeric values were correct**. Here an independent, second extraction read original workbook bytes, checked actual source coordinates, and compared values to the first extraction. This is an audit of **nine original publisher workbook editions**, not nine distinct fiscal years (FY2018/19 has initial and restated editions).

| Original financial source edition | Establishment financial lines | Independently checked numeric cells | Incorrect first-pass physical source-row addresses |
|---|---:|---:|---:|
| FY2014/15 restated XLSX | 119 | 952 | 0 |
| FY2015/16 initial XLSX | 119 | 952 | 0 |
| FY2016/17 initial XLSX | 122 | 976 | 0 |
| FY2017/18 initial ODS | 117 | 936 | **63** |
| FY2018/19 initial ODS | 117 | 936 | **62** |
| FY2018/19 restated ODS | 117 | 936 | **110** |
| FY2019/20 initial ODS | 118 | 944 | **111** |
| FY2020/21 initial ODS | 117 | 936 | **108** |
| FY2021/22 initial ODS | 119 | 952 | **110** |
| **Total** | **1,065 source edition lines** | **8,520 checked values; 0 mismatches** | **564 distinct accounting lines** |

Eight original numeric columns for every inspected source row: `B,C,D,E,F,H,I,J`. The checks tested the actual published cells including zeros and empty cells; independently re-read values match prior CSV observations. No values, names, original source or archive mirrors were changed. `Git blob SHA-1` identifies the opened original Git object, not a hash of a file downloaded afresh from the publisher.

### Corrected data (preferred for source-cell referencing)
- [FY2014/15–FY2017/18, all 477 accounting rows, corrected ODS physical row addresses](gb_cost_FY2014_18_477_source_establishment_accounting_rows_v2.csv); older `v1` retained only for audit history.
- [FY2014–18, 44 original function subtotals, corrected source row numbers](gb_cost_FY2014_18_44_published_function_subtotals_QA_v2.csv). **8** FY2017/18 subtotal rows corrected.
- [FY2018/19–FY2020/21, all 469 source edition records with actual ODS sheet row](gb_cost_FY2018_21_469_raw_operator_facility_year_rows_v2_physical_rows.csv). **391** of 469 rows corrected.
- [FY2018/19–FY2020/21, 40 original function subtotals](gb_cost_FY2018_21_category_and_subtotal_integrity_v2_physical_rows.csv). **34** subtotal row numbers corrected.
- [FY2021/22–FY2024/25, 477 reporting lines, corrected FY2021/22 source row addresses](gb_cost_FY2021_25_477_unharmonized_establishment_year_rows_v2_physical_rows.csv). **110** of 119 FY2021/22 source rows corrected.
- [FY2021/22–FY2023/24, 358 full eight-field records with corrected source cell references](gb_cost_FY2021_22_to_FY2023_24_358_establishment_source_rows_v2_physical_rows.csv). **110** FY2021/22 records corrected; same physical source lines as in preceding 477-record index, **not additional prison-year observations**.

The 564 number counts unique affected source edition accounting rows: 63 (2017/18) + 62 + 110 + 111 + 108 (FY2018/19–2020/21) + 110 (FY2021/22); duplication of FY2021/22 records in two downstream tables **is not double counted**. Additionally 8 + 34 = **42 source subtotal coordinate corrections**.

### Example proving the issue
FY2017/18 Glen Parva source `T3_Cost_by_Establishment`: initial catalogue called this XML row **198**, but after physically expanding prior repeated empty spreadsheet rows the actual source is **row 203**, e.g., `B203`, `C203`, `D203`, `H203`. Its average population **122** and positive expenses coexist with printed unit costs **0**. They remain exactly as published and are flagged for interpretation, not silently repaired.

### No extra numeric observations inferred
Workbooks FY2022/23–FY2024/25 were inspected for interior repeated blank XML rows and none were detected. This removes this specific address-shift risk for those three books, but is not an independent revalidation of all their numerical observations as part of the 8,520 count. Earlier detailed source-value checks remain separately documented. Other historical CSVs that still link to the old v1 source-row ordinates (particularly quality notes) should link to the v2 equivalents before quoting exact cell addresses.

### Remaining evidence requirements
- Obtain and archive separately the officially published **FY2015/16 restated edition**, which is missing among the original 27 UK finance source files; record original official URL and exact downloaded binary hash before claiming byte identity.
- Thoroughly read **10 UK cost supplementary workbooks** beyond initial sheet/header samples and **five cost-summary PDFs**, including differences in public/private accounting treatment, annual fiscal denominators, function changes, FY restatement.
- Build longitudinal institution identity/crosswalk with source-linked opening, closure, category and operator history; reporting-row counts cannot be called stable physical prison years.
- Resume whole archive work (Russian judicial `sud` forms, budget/FSIN/7z, 189 GB monthly prison-population bulletins, 53 staffing reports, European SPACE national institution evidence, US correctional finance). Preserve all 1,124 originals and 1,067 research-original exact categorized copies.

**Policy**: add-only versions. All originals, source mirrors and earlier catalogue versions are intact.

# UK financial 2018/19–2020/21: independent second-pass source verification — 2026-10-14

## Verification of original prison costs

Read the four *original* ODS sources a second time, decoding the `T3_Cost_by_Establishment` original worksheet and joining to the newly saved `gb_cost_FY2018_21_469_raw_operator_facility_year_rows_v1.csv` by **source file path, original Git SHA-1 and original sheet row**.

| Reporting fiscal year and source edition | Original operational line items | Independently checked numeric fields |
|---|---:|---:|
| 2018/19 originally published | 117 | 936 |
| 2018/19 restated | 117 | 936 |
| 2019/20 original | **118** | 944 |
| 2020/21 original | 117 | 936 |
| **Total** | **469** | **3,752** |

All **3,752 of 3,752** original source numeric comparisons passed, **0 mismatches**, and all original published source-line prison labels match. Eight fields compared: Certified Normal Accommodation (B), Annual Average Population (C), Direct Resource Expenditure GBP (D), direct cost/place (E), direct cost/prisoner (F), overall expenditure GBP (H), overall cost/place (I), overall cost/prisoner (J).

**Important:** These 469 rows are **not 469 distinct prisons**: 2018/19 is present **twice**, once in the original edition and once in the restated edition. The FY2019/20 source lists **118 operator-specific numeric lines** while its ten category headings describe **117 establishments**, because the Male local category lists **33 establishments but 34 numeric lines** including two separately accounted lines `Birmingham` (source row 147) and `G4S Birmingham` (source row 148). They reflect the return of HMP Birmingham to state management in July 2019, as explicitly indicated by the source's `Notes_to_T3` text (note around original worksheet row 7). This is not proof of two independent institutions and is not silently collapsed. Group published Direct Resource Expenditure totals differ from sum of displayed rounded 34 component rows by £3; overall expenditure sums match.

## Original and restated 2018/19 financial versions

Source files and immutable Git blob SHA-1:
- Original `GB/costs-per-prison-place-prisoner-individual-prison-2018-19.ods`, `966ec7a10ce70e89144a2c3a356fc910efd655d8`.
- Restated `GB/costs-prison-place-prisoner-individual-prison-2018-19-restated-tables.ods`, `dc3947e07a83462393484db85b4164b4ec3701ef`.

In the **restated workbook** `T2_Summary_Comparison`, original row 6 column D explicitly publishes **£129,111,488** moved into establishment direct education/training expenditure; original full FY total rows 5/7 compare D5 **£2,162,543,754** with D7 **£2,291,655,242**. Published aggregate `Overall Resource Expenditure` stays **£3,404,055,441** (H5=H7).

Independent prison-row-by-row comparison of the two source editions yielded **101 changed establishment rows**, sum of original row-level direct-spending differences **£129,111,482**, **£6 below** the official restatement due to original integer/rounding allocation. Original row-level overall expenditure difference summed to **£0**. The complete original-vs-restated list, including changes in *reported* per-prisoner costs, is separately preserved in `gb_cost_FY2018_19_original_vs_restated_source_rows_v1.csv`.

Do not construct two different FY2018/19 datapoints from the same source edition set. The restatement is a reporting-basis change, not evidence of an economically generated £129 million year-on-year spending shock. Direct vs overall expenditures have different reporting universes.

## Coverage context

Across 2018/19–2024/25 the source archive now has **946 original accounting line items**: 469 in this new data source, plus 477 FY2021/22–FY2024/25 source observations. That includes **117 additional copies of FY2018/19 observations in a distinct restated edition**, so **946 is not the number of unique institution×year observations**. Excluding the extra FY2018/19 edition yields **829 distinct published original rows over seven financial years**; FY2019/20 includes a Birmingham operator-period split, so even 829 is not automatically a unique physical-prison×year count.

Further work: harmonize institutions and reclassifications *only after* inspecting source notes and verifiable identifiers; never infer cross-year facility identity by string alone. Five historic cost PDF releases still need page-based reading; older 2014/15–2017/18 XLSX/ODS tables remain to be decoded at every prison row. The 2018/19 corrected vs uncorrected published versions both remain available, with original SHA preserved.

No source originals, existing archive mirrors, old notes or old CSVs were edited.

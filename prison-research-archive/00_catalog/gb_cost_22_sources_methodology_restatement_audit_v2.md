# UK MoJ / HMPPS prison cost archive — 22 original spreadsheets, 102 worksheet records (14 October 2026)

## Actual work and coverage

Read original XLSX/ODS bytes directly through GitHub with original Git SHA verification, unpacked their XML and inspected actual row/column structures for **all 22 UK prison cost spreadsheets** in `GB/`. Their **102 real source worksheets** are indexed by path, SHA, fiscal-year-labelled file, real tab name, source sheet row count, first title, header/row number and one original numeric sample where available:

- [All 102 sheet-index records](gb_cost_original_22_spreadsheets_102_worksheets_v2.csv).
- [22 per-source workbook summaries](gb_cost_22_spreadsheets_file_level_verified_v2.csv).
- Raw verified sheet mini-index batches: `gb_cost_original_sheet_content_batch_01_v1.csv`, `batch_02_v1.csv`, `batch_03_v1.csv`.
- Read-only [ZIP-based parser](tools/gb_cost_spreadsheet_catalog_v1.js).

Remaining **five PDF financial summary documents** have *not* been audited page-by-page at source content level. All 27 originals are preserved.

### Why direct-cost comparisons can be badly misleading

The 2018/19 **restated** establishment workbook (original `GB/costs-prison-place-prisoner-individual-prison-2018-19-restated-tables.ods`, Git SHA `dc3947e07a83462393484db85b4164b4ec3701ef`) contains table `T2_Summary_Comparison`, original rows 5–9: **£129,111,488** transfer of education/training expenditure to prisons, changing `Direct Resource Expenditure` attribution without increasing `Overall Resource Expenditure`. Preserve both the original FY2018/19 and restated FY2018/19 variants; **a change in reporting allocation is not a prison-system cost shock**.

The 2022/23 by-establishment workbook, `T3_Cost_by_Establishment` notes (original `GB/costs-per-prisoner-individual-prison-2022-2023.ods`), expressly say four establishments were reclassified to the expanded male Category C / Resettlement group. Cross-category averages should not be compared without reassignment.
The 2024/25 original `Notes_to_T3` records substantial institution-specific classification/operation changes (including capacity closures and transitions) and cautions that contracted versus public prisons are not directly comparable due to financing and scope.

### Financial denominator distinction

Original worksheets differentiate `Certified Normal Accommodation` (prison *places*) versus `Average Population` (*prisoners*, averaged across fiscal year); and `Direct Resource Expenditure` versus `Overall Resource Expenditure`. Annual cost per prisoner uses annual average prisoner population, not the monthly one-day `Population` observed in the separate GB bulletins. GOV.UK official releases corroborate direct/overall accounting and separate annual prison costs for:
- FY2022/23: https://www.gov.uk/government/publications/prison-performance-data-2022-to-2023
- FY2023/24: https://www.gov.uk/government/publications/prison-performance-data-2023-to-2024
- FY2024/25: https://www.gov.uk/government/publications/prison-performance-data-2024-to-2025

These are *verified official publication pages*, not proven exact archived download byte-hashes. Older source-file original download URLs remain to be recovered.

### Technical issue in archived 2022/23 ODS files

The two FY2022/23 ODS originals each include **632 link/reference-only table objects**, some with external workbook URL or workstation pathname. These are not extra source financial tables. The new parser deliberately does **not** follow or reproduce any such external links in the catalogue. Genuine source tabs number 6 (individual establishment) and 3 (supplementary) as shown in the resulting index. This also prevents spurious giant table counts.

### Remaining content work

The 102 sheet-level entries document the **actual source schema and sample values**, **not** validation of every numeric cell. Next perform row-level establishment/fiscal-year full extracts, reconcile public/private accounting and historical restatements (especially 2018/19), and identify exact institutional identifiers. Keep source fiscal-year reports distinct from dated occupancy snapshots and workforce reference dates. Then inspect the remaining five PDF summary documents.

All actions were add-only under `prison-research-archive/00_catalog`; original `GB/` and preexisting mirrors remain unchanged.

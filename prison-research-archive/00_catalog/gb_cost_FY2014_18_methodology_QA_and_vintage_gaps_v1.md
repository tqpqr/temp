# UK historical establishment costs FY2014/15–FY2017/18 — source-content and vintage QA (14 October 2026)

## Completed in this pass
Four original, byte-identified `GB/` workbooks were decoded directly from their original XLSX/ODS contents, at their published `T3_Cost by Establishment` worksheets. All source establishment accounting rows and all **eight** numeric source columns **B,C,D,E,F,H,I,J** were transcribed without recomputing published averages or ratios. Each extracted source row includes original path, Git blob SHA-1, worksheet, row, exact original cell addresses, publication group and financial year. This is an **initial complete single-parser extraction with category/subtotal cross-check**, not a second independently implemented cell-by-cell re-extraction.

| Fiscal year | Source edition | Actual accounting rows | Published function groups | Original blob SHA |
|---|---|---:|---:|---|
| 2014/15 | 2014/15 restated in 2015/16 release | 119 | 11 | `071f1af676051b6af7a119beb4d9118407b68799` |
| 2015/16 | initial published edition | 119 | 11 | `09ae7bb2b1455657015f7203fdc7ea7eb283d707` |
| 2016/17 | initial published edition | 122 | 11 | `c18518c03b8f15923ac714616ac834a2dfbec36d` |
| 2017/18 | initial published edition | 117 | 11 | `2261d528d67e9daa57cb54888945d1160718d02c` |
| **Total** | | **477** | **44** | |

- Raw unharmonized source records: [477 rows](gb_cost_FY2014_18_477_source_establishment_accounting_rows_v1.csv).
- Original subtotal reconciliation: [44 group audits](gb_cost_FY2014_18_44_published_function_subtotals_QA_v1.csv).
- Primary publisher release and attachment links (including absent restatement): [official source register](gb_cost_FY2014_18_official_attachment_provenance_and_missing_2015_16_restatement_v1.csv).

All 44 published function groups have matching accounting-row counts except **2016/17 Other**, whose original printed header says **2 establishments** while its actual table contains **3 financial rows** — Blantyre House, Dover, Haslar. All three are preserved. Across the 44 groups, the largest absolute discrepancy between sum of printed individual **direct resource expenditure** and published group subtotal is **£4**, and for **overall resource expenditure £2** (consistent with displayed integer precision, but no hidden unrounded source is claimed).

## Exact source caveats

1. **FY2014/15**: the local workbook is explicitly the **restated** vintage. Downview shows zero annual average population but nonzero resource expenditure. This edition must not be relabelled as the first publication.
2. **FY2015/16**: 119 establishment financial lines from the **initial 2016 release**. Blantyre House and Downview have blank average-population cells but positive expenses; do not impute zero or calculate per-person cost.
3. **FY2016/17**: the `Other (2 establishment)` count label disagrees with three source financial records. All three have blank average population. Count-of-accounting-lines is not a stable measure of physical prisons.
4. **FY2017/18**: Glen Parva shows published CNA=222, annual average population=122, direct expenditure=£3,931,216, overall expenditure=£3,931,216, but published **cost per place/per prisoner = 0**. Preserve the printed zeros and flag them as non-interpretable unit costs for economic analysis.
5. Publication **2016/17** explicitly includes a **restated FY2015/16 establishment workbook**, absent from the local original 27 GB cost files. Official attachment: https://assets.publishing.service.gov.uk/media/5a82f0f140f0b62305b9523d/costs-per-prison-place-per-prisoner-by-individual-prison-2015-2016-restated-tables.xlsx. Publication page: https://www.gov.uk/government/statistics/prison-performance-statistics-2016-to-2017. **Not downloaded, not hashed, not in the baseline**. Do not silently substitute the initial 2015/16 values for this revised edition.

## Date, population, public/private accounting, and verification

A financial-year **annual average prisoner population** is not a month-end actual stock. `Certified Normal Accommodation` is a specific accommodation concept and must not be relabelled as `operational capacity`. Exact original institution names are retained but not matched automatically across years or to staff/payroll records. Original columns `D` and `H` are distinct direct versus overall resource expenditure and cannot be interchanged. Publication-vintage revisions, contract-operated prisons, category changes, changes in budget allocation, and source-specific unit-cost rounding may invalidate a naive fixed-effect panel or annual comparison.

Source SHA-1 values identify the exact original Git objects that were opened through the authenticated repository, **not external publisher binary hashes**. Four precise official attachment URLs have been identified from the government's own release pages; matching names, extensions and listed sizes support provenance, but downloaded bytes have **not** been compared to the Git blobs. The official 2015/16 restated attachment is a known missing source, not a claimed archival copy.

## Next actions

1. Independently re-read the 477 × 8 original numeric cells with a separate extraction path; check all edge-case group and money fields.
2. Obtain and hash the separately published FY2015/16 restated workbook as a **new provenance-labelled external source** (do not alter original folders or existing mirrors); compare to the original FY2015/16 source. Also examine 2014/15 original vintage if useful.
3. Finish source-level content inspection of the **10 remaining UK cost supplementary XLSX/ODS** and **five UK cost summary PDFs**, with publication version, page or sheet, methodology and definitions.
4. Crosswalk 2014–2025 reporting identities with opening/closure/function/operator events only after source-accurate observations have been secured. Distinguish exact source records from unique institutions and financial years.
5. Continue full-archive tasks for 189 UK monthly occupancy bulletins, 53 staff workbooks, 507 Russian judicial files, FSIN/budgets, SPACE national primary sources, and US corrections finance.

No original files, binary mirrors, previous CSV versions or older indexes are modified by this note.

# GB-006 — completed direct original-source audit: FY2017/18 UK prison costs supplementary ODS

**Original**: `GB/costs-per-prison-place-cost-per-prisoner-2017-2018-supplementary-information.ods`; SHA-1 Git blob `e4d0f28ec9b9ab7349de258b9fe0a4e1bb0c68a1`, **44,358 bytes**. Published date from `Cover_!A19` **25 October 2018**, fiscal year from `Cover_!A10` **2017–18**. Source cover `A12:A17` names National Offender Management Service, Ministry of Justice, Management Information Addendum. Region: **England and Wales** (not UK-wide including Scotland/Northern Ireland). Original byte identity from repository only; no independently checked publisher-original hash.

## Previously completed versus new work

Existing `00_catalog/gb_cost_original_22_spreadsheets_102_worksheets_v2.csv` had already verified exactly **three real source sheets** and inspected their captions/samples. This GB-006 task does not recreate the earlier original-sheet index or annual by-establishment cost panel. Newly extracted **all 93 nonempty physical worksheet rows** with original A–K values and exact source row into [source-cell CSV](GB-006_2017_18_supplement_full_source_cells_v1.csv): **8 cover rows**, **41 T1 rows**, **44 T2 rows**. ODS `content.xml` read directly, physical row/column addresses expanded for `table:number-rows-repeated`, `table:number-columns-repeated` and covered-table-cells; source stored numeric values preserved as strings. **Zero original table:formula attributes** in the three actual sheets; no formulas recalculated or third-party external references followed. ODS may allocate huge repeated blank tails; the recorded 93 are *nonempty physical source rows*, not millions of data records. The previously existing FY2017/18 **117 accounting lines** in `00_catalog/gb_cost_FY2014_18_477_source_establishment_accounting_rows_v2.csv` are a **different original by-establishment financial workbook** (Git blob `2261d528d67e9daa57cb54888945d1160718d02c`); do not duplicate that extraction.

## Source structure and evidence

- `T1_Contracted_Prisons!A1:G57`: `T1!A5:G7` compares **102 public vs 14 contracted establishment end-FY categories** (publisher `A13`), with 77,865 CNA places, **84,710 fiscal-year average population**, overall resource spending **£3,180,266,865**, £40,843 per place, £37,543 per prisoner. `A10:A11` explicitly warns public/private are **not directly comparable** because of accounting/scope differences: PFI capital-interest and private-sector healthcare treatment. `A17:G52` lists 10 PFI named reporting entities, 4 O&M named entities and 3 printed subtotal rows; contract dates in source column B. `A56:A57` states all averages and expenditure are rounded to integers but totals formed from unrounded values.
- `T2_Supplementary_Data!A3:J6` (male/female), `A10:J13` (adult/YOI), `A17:J20` (public/contracted), `A24:J35` (England/Wales and operator), `A39:J59` (national category breakdown). Do **not** add category dimensions as independent populations, they are alternative partitions of the same system.
- `T2!B59` **77,865 Certified Normal Accommodation places**, `C59` **84,710 average prisoners** (fiscal-year mean, NOT single date prison Population), `D59` **£2,045,831,827 Direct Resource Expenditure**, `H59` **£3,180,266,865 Overall Resource Expenditure**. `E59:F59` unit direct £26,274/place and £24,151/prisoner; `I59:J59` overall £40,843/place and £37,543/prisoner. Original stored source numeric values, not reconstructed rates.
- `T2!A41:D51` accounting structure: Payroll (£1,243,418,052); **Non Pay** parent (£914,072,790); eight breakdown components `D43:D50` (sum EXACTLY same parent, not an additional expense!); **Income** (−£111,659,016); plus six separate overall-only allocations `H53:H58`. `D49` **Service Concession Arrangements £462,841,138**, identical source category caption to 2016/17 **£454,911,681** (prior GB-005), and notably different FY2015/16 label scheme (MB-001/002/003). These 2016/17 and 2017/18 recorded values do **not** establish an uninterrupted historically stable category meaning nor causal expenditure shock.
- `T2!A63`: whole mixed prisons categorized by **majority use**. `A64` public/contracted comparison caveat same as T1. `A67` rounding rule.
- `T1!D51:G51` contains unlabeled literal source zeros, NOT a fifteenth contracted prison or a new subtotal. Kept verbatim in raw cells and excluded from the 14 named PFI/O&M count. Source zero is not missing source value.

## Independent original-value arithmetic QA

[16 checks with physical source anchors](GB-006_2017_18_supplement_arithmetic_QA_v1.csv) compare sums of publisher printed whole-pound components with printed totals. Maximum discrepancy **£2** across checked expenditure identity equations; within publisher `T1!A56:A57` rounding caveat. In particular:
- `T2!D43:D50` eight non-pay component sum equals `D42` exactly, **£914,072,790**.
- `T2!D41+D42+D51` is £2,045,831,826 versus `D59` £2,045,831,827 (**−£1**).
- `T2!D59+H53:H58` is £3,180,266,866 versus `H59` £3,180,266,865 (**+£1**).
- Ten named PFI `T1!E23:E38` printed amounts sum **+£2** versus `E39` subtotal. Four named O&M `E43:E48` sum exactly to `E49`; PFI+O&M printed subtotals are £1 less than `E52`. Do **not** override publisher totals with naively summed printed values.
- Whole-system source `T1!E7` and `T2!H59` agree exactly; T2 published England + Wales and public + contracted overall totals also match.

## Count-scope issue / methodology ledger

**NEW source-to-source scope mismatch MB-019**: `T1!A5:A6; A13` says 102 public + 14 contracted establishments **as their main type at FY-end** = **116**. Existing exact original financial source extraction in `GB/costs-per-prison-place-cost-per-prisoner-by-individual-prison-2017-2018-tables.ods` has **117 unharmonized source financial accounting lines** from its `T3_Cost_by_Establishment`; they are NOT necessarily 117 unique physical prisons. Reasons for the one-line difference are NOT yet source-verified; unit universes (FY-end categorization versus annual accounting rows) differ. Do not silently convert either number into the other; do not impute which institution accounts for it before a controlled source name crosswalk. Existing 2017/18 Glen Parva published zero unit costs **MB-007** remains independently relevant.
 
**Source classification**: current publication does not provide the missing 2015/16→2016/17 classification bridge for MB-001/002/003, and does not eliminate MB-010 public/contracted scope warning. No new hypothesis about recoding policy promoted to fact.

## Registry decision / preservation

- Indicator×FY coverage: add genuine observed fiscal-year national measures for exact period **2017/2018** including national total CNA / average population / direct+overall resource expenses / source total rates and FY2017/18 accounting rows (not repeated original by-establishment records). Use original T2 row addresses and preserve parent/subcomponent distinctions. Separate source full cell extract is authoritative for all source-categorized numbers.
- Breaks ledger: preserve old 18 cases; add **MB-019 count-perimeter mismatch**, scope/open explanation (NOT asserted data-entry error or physical prison closure).
- Task **GB-006 DONE**, source originals and previous panels/files unchanged. Next **GB-007** original FY2018/19 supplement, after consult prior GB finance restatement MB-004 and method categories; no cross-year conflation.

**Technical boundary:** ODS source data and arithmetic verified from repository binary, but publisher-hosted bytes not independently compared. Original workbook stored number formats may render zero/rounded values differently; raw source strings in CSV reflect stored number fields when present, not a recalculation.

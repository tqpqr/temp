# GB-007 — 2018/19 MoJ prison costs: original supplementary source audit

**Task status: DONE (2026-10-14).** Original `GB/costs-per-prison-place-prisoner-2018-19-supplementary-information.ods`, Git blob `b76237a93416b737e437ef32b8a0e75566957abe`, 42316 source bytes, ODS `content.xml` 845893 decompressed bytes. Publisher original attachment bytes not externally matched. Only England and Wales. Reporting period FY2018/19, not calendar year and not one-day population.

**Publisher evidence:** `Cover_!A10` = 2018-19 Supplementary information, `Cover_!A19` = Published 31 October 2019. Three actual sheets `Cover_` (8 source content rows), `T1_Contracted_Prisons` (41), `T2_Supplementary_Data` (48); **97 nonempty source rows** in total. All A–K stored values including explicit blanks, physical row addresses and numeric source strings saved in [full source CSV](GB-007_2018_19_supplement_full_source_cells_v1.csv). No `table:formula` in those three sheets; no external reference links followed, no original files altered. Existing 117 original + 117 restated FY2018/19 **by-establishment** rows already independently audited; NOT duplicated here.

## National primary figures and source cell addresses

| 2018/19 original (not 2020 restatement) | Value | Original sheet and cell |
|---|---:|---|
| CNA | 78774 places | `T2_Supplementary_Data!B59` |
| Annual-average prisoners | 82751 persons | `T2_Supplementary_Data!C59` |
| Direct resource expenditure | £2162543754 | `T2_Supplementary_Data!D59` |
| Overall resource expenditure | £3404055441 | `T2_Supplementary_Data!H59` |
| Direct cost per place / prisoner | £27453 / £26133 | `T2_Supplementary_Data!E59;F59` |
| Overall cost per place / prisoner | £43213 / £41136 | `T2_Supplementary_Data!I59;J59` |
| Service Concession Arrangements, nested Non Pay child | £473874996 | `T2_Supplementary_Data!D49` |

**Restatement:** initial source direct total `D59` equals £2,162,543,754 in previously audited restated establishment workbook `T2_Summary_Comparison!D5`. That separate source publishes +£129,111,488 education/training cost moved into **direct** expenditure `D6`, giving restated £2,291,655,242 `D7`, while **overall remains £3,404,055,441** `H5=H7`. Existing methodological **MB-004** completely describes this publisher source-version change. Distinct publication vintages are NOT separate years; no £129m real spending increase established.

**Counts/scope:** source `T1_Contracted_Prisons!A5:A7` lists **103 public + 14 contracted establishments** = 117 by **main type at FY-end** (`T1!A13`); existing separate by-establishment original FY financial source has 117 source accounting rows, but exact physical institution identities have not been proven solely from identical counts. `T1!A10:A11` and `T2!A64` warn private/public expenditure scopes differ (PFI interest and healthcare). Source `T2!A63` assigns mixed prisons by majority use. Annual-average prisoners ≠ end-month stock; CNA ≠ operational capacity.

**Original category hierarchy:** Payroll `D41` = £1357655066, Non Pay **parent** `D42` = £926110397, eight **children** `D43:D50` collectively equal parent, income `D51` = £-121221709 (negative). **Do not add parent to children.** Six `H53:H58` are **overall-only** allocations; `A53` wording "Depreciation of buildings and capital repayment" repeats FY2017/18 (but NOT FY2016/17 caption; known MB-020). Service Concession Arrangements remain a FY-specific category, 2015/16-to-2016/17 bridging still open MB-001–003.

**Publisher rounding artifacts:** original `T2!B7:D7`, `T2!B14:D14`, `T2!B36:D36` contain unlabeled rounded-balance/residual values including **C7=-1** and **C36=-1**, and `T1!D51:G51` contains unlabeled zeros. All retained in original source CSV. These are **not records of negative prisoner populations, institutions or missing data**. Source `T1!A56:A57` and `T2!A67` expressly warn sums of rounded parts can differ from totals computed from unrounded data.

[Source-cell arithmetic ledger](GB-007_2018_19_supplement_arithmetic_QA_v1.csv) has 33 reconciliation equations, including 10 PFI + 4 O&M components, source 2018/19 initial vs independently previously verified restated direct expenditure and the four alternative national population/accounting partitions. Largest rounded component discrepancy 2 in the stated source units (see each check, which records whether GBP, places or persons).

**Twin registry outcome:** add new FY2018/19 initial-publication national accounting/denominator measures in indicator×period registry; **NO_NEW_BREAK**, since MB-004 original/restated accounting transfer and MB-010 public/private inclusion already exist, MB-020 historical category difference remains unresolved. Do not create new breaks from publisher unlabeled source rounding residuals or identical 117 counts. Continue next GB-008 FY2019/20 (Birmingham operator split MB-005), with original-source-first and no duplicate extraction.

Original Git SHA-1 validates repository object, not publisher-origin SHA-256. All prior files and sources preserved without overwrite.

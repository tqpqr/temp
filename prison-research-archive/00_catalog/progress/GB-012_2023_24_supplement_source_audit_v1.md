# GB-012 — original FY2023/24 HMPPS/MoJ supplementary prison-cost source audit

**Atomic task GB-012 completed 14 October 2026.** Scope **England and Wales** only (not UK-wide), financial year **1 April 2023–31 March 2024** (not 2024 calendar year, not an individual day). Original source `GB/costs-per-prison-place-prisoner-2023-24-supplementary-information.ods`, original **Git blob SHA-1 `59f04c2bb5a7c0b7aeb8b54eca7cc506131aa277`**, **42,993 bytes**; original ZIP/ODS `content.xml` **872,054 bytes** after decompression; directly read at original physical source rows. Original `Cover!A10` says **2023-24**, `Cover!A19` says **Published 3 April 2025**. Official publisher https://www.gov.uk/government/publications/prison-performance-data-2023-to-2024 corroborates edition date and England and Wales. Original publisher-hosted ODS bytes/SHA-256 have not been independently cross-hashed against archive Git object; do not claim external binary identity.

## Source preservation and auditing scope

- Exactly **three original real financial worksheets**: `Cover` **8** nonempty physical source rows, `T1_Contracted_Prisons` **43**, `T2_Supplementary_Data` **44**, for **95** source rows. All A–K original text/numeric *stored cell values*, explicit blank values, source row addresses and source SHA preserved in [full cell-level source extract](GB-012_2023_24_supplement_full_source_cells_v1.csv). No `table:formula` attributes on these source worksheets; formulas not recalculated and any unrelated source package entries/external links were not followed.
- Existing separate original FY2023/24 by-establishment source `GB/costs-per-prison-place-prisoner-individual-prison-2023-24.ods`, Git blob `4df76a9c07f3cf8431993b1c4daac205549fd0de`, **120** by-establishment accounting rows already independently audited in `00_catalog/gb_cost_FY2021_22_to_FY2023_24_358_establishment_source_rows_v2_physical_rows.csv`. **No new 120-row prison-level duplicate created.** Site cross-checks reuse this validated file and retain original T3 row identities.

## Source-original national FY2023/24 figures

All national primary fields are from `T2_Supplementary_Data!B59:J59` (source publisher whole-number printed units):

| Measure | Original value | Source cell |
|---|---:|---|
| Certified Normal Accommodation (CNA) | **82,258 places** | B59 |
| Financial-year average prisoner population | **87,129 persons** | C59 |
| Direct Resource Expenditure | **£3,054,089,482** | D59 |
| Overall Resource Expenditure | **£4,687,647,356** | H59 |
| Direct cost per CNA place / per FY average prisoner | **£37,128 / £35,053** | E59 / F59 |
| Overall cost per CNA place / per FY average prisoner | **£56,986 / £53,801** | I59 / J59 |
| Service Concession Arrangements (Non Pay child) | **£589,026,938** | D49 |

CNA is **not** operational/useable capacity and annual-average prisoners are **not** a specific prison-day population count. Costs are **nominal GBP** without inflation adjustment. FY2022/23 original comparators were **80,846 CNA**, **81,822 FY-average persons**, direct **£2,751,481,717**, overall **£4,181,725,178**, concession child **£559,567,392**. These are observations, not estimated causal fixed-cost responses.

## MB-026 — original Altcourse PFI→M&M contract source-universe transition

FY2022/23 original `GB/costs-per-place-per-prisoner-2022-2023-supplementary-information.ods` (Git `9c2f4e108de7346df4d13804ab71355210228de2`) source `T1_Contracted_Prisons!A29:G29` lists **Altcourse under PFI**, historical contract date **Dec 1997**. FY2022/23 private institutional year-end total was **14** (8 PFI+6 M&M), with **105 public**.

FY2023/24 current original `T1!A5:A7` lists **105 public + 15 contracted = 120** year-end institutional categories. Individual contract table has **7 named PFI** (publisher total `T1!C35:E35`) and **8 named Manage & Maintain** (`T1!C51:E51`), total 15 (`T1!C54:E54`). `T1!A42:G42` newly lists the **same Altcourse institution in M&M**, source contract date **Jun 2023**, with **780 CNA places, 1,156 FY-average people, £49,421,540 overall**, matching previously verified FY2023/24 original establishment finance line `T3_Cost_by_Establishment!B141,C141,H141`. This is **not opening of an additional Altcourse prison**. Contract subtype movement is directly verified and separate from older MB-023 FY2021/22→FY2022/23 Lowdham Grange and Parc contract category changes.

Official MoJ FY2023/24 departmental financial statements https://www.gov.uk/government/publications/ministry-of-justice-annual-report-and-accounts-2023-24/annual-report-and-accounts-2023-24-financial-statements-html list Altcourse M&M contract commencement **May 2023**, whereas this source `T1!B42` prints **Jun 2023**, original previous PFI table `B29` printed **Dec 1997** under the same "Contract start date" heading. Preserved as an **unresolved contract-milestone/vintage/date definition mismatch**. Dates for old and new distinct contract types need not agree, but the one-month current-edition difference cannot be resolved here; no publisher typo assumed. Departmental FY2022/23 £94.2m PFI reclassification (older MB-023) still **must not be transferred mechanically** into prison-cost supplementary source `T2!D49` or other columns without issuer-provided denominator/account-category bridge.

## MB-027 — Fosse Way newly opened partial-FY first cost exposure

`T1_Contracted_Prisons!A47:G47` first names **Fosse Way** as Manage & Maintain, `B47` **May 2023** original source contract-start, **1,143 CNA** `C47`, **974 FY-average prisoners** `D47`, **£58,338,786 overall** `E47`, published **£51,048 per place** `F47` and **£59,902 per prisoner** `G47`. Original detailed prison-cost source `T3_Cost_by_Establishment!B39,C39,H39` confirms same three principal numbers and source Direct Resource Expenditure **£44,878,310**; already part of the 120 audited FY2023/24 prison financial lines.

**Independent contemporaneous official fact:** https://www.gov.uk/government/news/new-jail-boosts-capacity-and-the-economy-in-drive-to-cut-crime states that first prisoners arrived at Fosse Way on **29 May 2023** and describes a projected **approximately 1,715-place** institution (formal opening June 2023). Official MoJ prison adaptation publication https://www.gov.uk/government/publications/climate-change-adaptation-strategy-moj/climate-change-adaptation-strategy-2024-moj also distinguishes new prison opened in 2023. The prison first appears in this FY and does **not** have a full April 2023–March 2024 operational service exposure. This raises *demonstrated first-year timing comparability risk*, not proof that the published unit cost is arithmetically wrong. Source reports CNA **1,143** rather than eventual ~1,715 planned design places; definition/time weighting of its 1,143 places, all exact first/last capacity dates and FY capacity place-days are **not independently established**. Do not annualise by a guessed month fraction or infer persistent structural efficiency.

**Five Wells** under same 2023/24 `T1!A46:G46` is **1,680 CNA, 1,567 FY-average persons, £54,213,607 overall, £32,270/place, £34,590/prisoner**, independently matched to original audited by-establishment `T3!B38,C38,H38`. Original 2022/23 was **1,620 CNA, 794 average persons, £40,682,745 overall**; reporting periods reflect maturation in source observation only. Existing Five Wells MB-022 and MB-024 historical date versus first-prisoner distinction remain open; no original-site reclassification.

FY2023/24 prison count **120** versus FY2022/23 **119** is consistent with Fosse Way's new inclusion; source counts alone do **not** establish a complete institution-ID crosswalk or unchanged physical classification in every other row.

## Source national accounting and arithmetic, scope cautions

`T2!D41` original **Payroll £1,866,600,509**, `D42` **Non Pay PARENT £1,266,654,859**, `D51` signed **Income −£79,165,887**. The eight original source child categories `T2!D43:D50` must **not be summed together with parent**. Concession costs `D49` are a child. Six expense allocations `T2!H53:H58` are **overall-only** overhead/capital components, not part of direct Resource Expenditure. `T2!A53` still says "Depreciation of buildings and capital repayment" (historical FY2016/17 caption differs, existing MB-020). `T1!A10:A11`, `T2!A64` explicitly warn public/contracted prison costs are **not directly comparable** due to PFI-related accounting treatment/scope. `T2!A63` allocates entire mixed-use prison to its majority use category.

[All **45** physical source-cell arithmetic checks](GB-012_2023_24_supplement_arithmetic_QA_v1.csv) cover 7 PFI, 8 M&M listed original contract rows and subtotals, alternative national population/expenditure partitions, signed payroll/income/nonpay arithmetic, six overall allocations and 3 already-validated institutional comparators each in 3 source units (Fosse Way, Five Wells, Altcourse). **Largest absolute published-component difference 3 units (not a material financial discontinuity)** under source `T1!A58:A59` / `T2!A67` explicit publisher whole-number rounding qualification. In particular `T1!E7` prints **£4,687,647,357** vs `T2!H59` **£4,687,647,356**, and T2 public + contracted `H19 + H20` £4,687,647,358 versus source national printed `H59` £4,687,647,356. These are **source printed figures, not errors to overwrite**.

## Twin-catalogue decision and resumption

- Add **25 national FY2023/24 original-source measures** in indicator×period registry with exact FY, publisher publication vintage `2025-04-03`, original T2 physical source cells, Git SHA. Facility observations are already verified in existing original FY2023/24 by-establishment archive; **no duplicate per-prison data rows**. Distinct institution-start and category evidence recorded in methodology ledger/this QA.
- Add **MB-026** for Altcourse old PFI→new M&M and historical/current-date measurement boundary; add **MB-027** for first FY Fosse Way operational time exposure/denominator. Preserve MB-023–025, MB-022 and all older source issues.
- **GB-012 DONE; GB-013 NEXT** (original FY2024/25 prison-cost supplement). Don't use publisher-FY source counts as stable institution longitudinal IDs, don't equate CNA/operational place capacity or year-average/point-day prison count. All originals and prior versions preserved, Git SHA-1 is not publisher SHA-256.

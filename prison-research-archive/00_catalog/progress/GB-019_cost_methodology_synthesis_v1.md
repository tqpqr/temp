# GB-019 — England and Wales prison-cost methodology, 2015/16–2024/25

**Result: UK source-methodology consolidation complete. This is an evidence-linked *catalogue*, not a harmonised longitudinal prison panel, causal estimate, or reconstructed publisher dataset.** Date of audit: 14 October 2026.

## Purpose and primary outputs

- [311-row concept/year/source-cell crosswalk](GB-019_cost_methodology_crosswalk_v1.csv): **10 actual original fiscal-year supplementary XLSX/ODS editions × their national cost concepts and published public/contracted subtotal cells**, retaining physical source worksheet, row, caption, original stored numeric, Git source SHA-1 and non-additivity/scope rules.
- [10-year three-identity reproducibility audit](GB-019_10yr_financial_identity_QA_v1.csv): original Non Pay parent vs nested children, Direct vs payroll+Non Pay+signed Income, Overall vs Direct+overall-only allocations. **30/30 comparisons pass ±3 original integer units**. The maximum absolute discrepancy is GBP 3. These are printed-source reconciliations, not independent audited expenditure books.
- [Revision/measurement chronology](GB-019_revision_chronology_v1.csv): **24 dated and source-anchored events**: 20 relevant methodological cases cross-linked to the issue ledger plus four PRICE-BASE-only conversions (not new accounting reclassifications).
- [Document-edition inventory](GB-019_source_vintage_manifest_v1.csv): **19 original or expected financial source editions**, including 10 national supplements, 5 narrative PDFs, the initially published and missing restated FY2015/16 establishment books, the later-restated FY2018/19 establishment edition and the FY2019/20 operator-period source.
- [25 UK-specific issue decisions](GB-019_UK_methodology_issue_gates_v1.csv): references the existing methodological register rather than inventing new MB issues; 13 conditional/unresolved according to status keywords, 11 confirmed within scope, one resolved requiring a source-version choice. Treat this as triage, not an independent re-adjudication of every issue.

**Existing source indicators preserved:** `00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v16.csv` has 1,136 evidence-graded records; GB-019 creates a *reference/crosswalk* only, with **zero extra source observations** appended to the indicator registry. Existing original PDFs, ODS, XLSX, and establishment records have not been overwritten, deleted, renamed, copied or mutated.

## Scope, period and observation type

**Geography:** England and Wales prison cost accounting administered by NOMS/HMPPS/MoJ, **not the United Kingdom as a whole**. Financial years run 1 April–31 March, not calendar years. This cost series is neither a daily inmate census nor the separate `Monthly_Bulletin` operating-capacity series. The published baseline establishment count is generally *main function/operator at fiscal year end*, not necessarily the number of site/operator-period financial lines within the full fiscal year (MB-019, MB-005/021).

The catalogue is **vintage-aware**: an observed FY2018/19 original cost and a FY2018/19 value re-expressed in FY2019/20 comparative accounts are *not* two FY observations. Full Git blob SHA-1 is source-file identity **inside this repository**, not evidence that publisher-hosted raw bytes match exactly by SHA-256. One FY2024/25 extracted cell CSV did not embed the blob SHA; its original ODS SHA was independently fetched in the GB-013 audit. The other 9 extracts embed their verified original SHA.

## Measurement dictionary: exact source-year exceptions

| Concept | Meaning / conversion | Source anchors and limitation |
|---|---|---|
| Baseline CNA | Certified Normal Accommodation; the published denominator for cost/place; not necessarily currently usable capacity | Original **PDF GB-014 p2** and repeated **GB-017/018 p2**. National 2015/16 **T2_Supplementary Data!B60**, 2016/17 onwards **T2_Supplementary_Data!B59** (the first two sheets contain spaces in the sheet name). |
| Average prisoner population | **Average of 12 month-end prisoner numbers**, not continuous mean prisoner-days or a single census date | **GB-014 p2**; 2015/16 **C60**, later **C59**; possible rounding when summing group means. |
| Direct resource expenditure | Net prison-managed/recorded resource costs; signed components `Payroll + Non Pay + Income` | **GB-014 p2**, 2015/16 **D60**, 2016/17 onwards **D59**. Staff/policy transfer changes what is booked directly, so compare using a chosen publisher vintage. |
| Overall resource expenditure | Direct plus net centrally/regionally booked expenditure and overhead/capital allocations; not simply direct operating spending | **GB-014 p2**, 2015/16 **H60**, later **H59**. `Overall` may remain unchanged when components move between HQ and direct sites. |
| Cost per place or per prisoner | Publisher's direct/overall cost ÷ published underlying CNA or annual-average prisoners | Original unit cells **E/F/I/J60** in 2015/16, **E/F/I/J59** thereafter; publisher totals use underlying unrounded values, so don't silently overwrite them with integer division. |
| Non Pay, income and concession costs | `D42` is parent Non Pay, **not additive to its children**; Income is signed negative | 2015/16 children **D43:D51**, income **D52**; subsequent years children **D43:D50**, signed income **D51**. Source **D49** first separately denotes Service Concession Arrangements in 2016/17; **2015/16 D49 is Prisoner regime, not the same series** (MB-001–003). |
| Overall-only allocations | Six source-line totals above Direct for depreciation/property, rent, regional overheads, PECS, HQ | FY2015/16 original **H54:H59**; FY2016/17 onward **H53:H58**. 2016/17 p/row **A53** says buildings and central ICT, 2017/18 changed to buildings and capital repayment (MB-020); don't join by row and assume identical perimeter. |
| Contracted vs public and prison group | Separate service/accounting scopes, source end-year categories and changing contracts | **GB-004/005 T1!A10:A11**, **GB-014 pp4–5**, later PDFs. PFI financing, health, education, maintenance and site/period shifts prevent raw causal cost ranking without a bridge (MB-010, MB-023/026/028). |

**Original row shift is independently source-verified:** 2015/16 national totals are row 60, income row 52, overheads H54–H59; from 2016/17 original national totals row 59, income row 51, overall allocations H53–H58. Original source tabs likewise use actual publisher naming `T2_Supplementary Data` for 2015/16–16/17 and `T2_Supplementary_Data` subsequently. The crosswalk records the exact sheet/coordinate for every observation and **does not assume numerical/semantic continuity from cell address alone**.

## Three materially different prior-year accounting adjustments

1. **FY2014/15 comparative in GB-014, MB-029:** FY2014/15 Direct originally **GBP 2,009,397,979**; maintenance costs transferred to HQ **-100,192,207** and finance staff **-901,250**, giving restated Direct **GBP 1,908,304,522**. Overall prior-year remains **GBP 2,804,394,939**. A departmental accounting allocation, *not documented savings*.
2. **FY2015/16 comparative in GB-015, MB-031:** transfer of prison education/training policy responsibility from DfE to MoJ adds **GBP 120,390,295** to prior-year **Overall** (GBP 2,753,747,261 → **2,874,137,556**), while Direct **GBP 1,897,972,242** remains unchanged. Distinct from missing revised FY2015/16 prison-by-prison Excel (MB-008).
3. **FY2018/19 comparative in GB-018, MB-004:** **GBP 129,111,488** education/training expense reallocated from HQ to prison-site **Direct** (GBP 2,162,543,754 → **2,291,655,242**); **Overall stays GBP 3,404,055,441**. The same year also has a separately identified restated by-prison worksheet; use edition as a formal dimension.

A **GDP deflator** applied after any scope reallocation is a *different transformation*, not another spending observation. Audited narrative statements include GB-015 100/97.7941, GB-016 +1.9%, GB-017 +1.9% and GB-018 +2.4% real-price factors. The revision chronology stores price-base and accounting-perimeter events separately. For a single multi-year common-price national panel, select and document **one consistent real-price base**, rather than chaining published prior-year comparison rows as if all were nominal source entries.

## Specific source failures that must be excluded or rebuilt

- **MB-032**: GB-017 (FY2018/19 PDF) Table 2b prior *FY2017/18* public/PFI/O&M sector rows instead repeat **FY2016/17** values in **12/12** financial/capacity cells; national Table 2a FY2017/18 row is correct. Do not use published Table 2b *sector growth* without reconstructing true prior-year source categories and checking the accounting perimeter. Original forensic: `GB-017_sector_comparator_QA_v2.csv`.
- **MB-033**: GB-018 (FY2019/20 PDF) Table 2b prior FY2018/19 national total **four per-place/per-prisoner unit costs** repeat O&M subgroup values. Correct original **Table 2a** FY2018/19 rates 27,453 / 26,133 Direct, 43,213 / 41,136 Overall; Table 2b instead has 18,726 / 16,113 and 25,380 / 21,839. The underlying total expenses are not thereby invalidated. Audit `GB-018_2019_20_table2b_2018_19_total_paste_QA_v1.csv`.
- **MB-006/007/009**: historic by-establishment ODS row addresses require corrected **v2 physical row indices**; Glen Parva 2017/18 printed zero rates despite positive costs; 2016/17 `Other` header count 2 vs 3 actual rows. Preserve source literals and do not silently replace anomalies.
- **MB-008 (unresolved dependency):** publisher references a **FY2015/16 revised establishment XLSX**, but actual publisher bytes and row-level differences were not obtained; **GB-002 remains BLOCKED and GB-003 WAITING**, not silently solved by GB-015's national narrative adjustment.

## Facility/operator and contract-vintage break register

- **Birmingham 2019/20 MB-005 and MB-021:** one physical institution can have two public/private financial operator-period rows; O&M annual expense subtotal includes financial contribution from G4S Birmingham although the year-end contracted prison-name list does not show that name. Never treat counts of institutional or account rows as fixed-site count.
- **Five Wells 2021/22 MB-022, MB-024:** first reported contract period near FY end and historical `contract start` recorded as Feb 2022 versus Nov 2020 in later publication. Award/mobilisation/operation milestones must be distinguished; use actual verified place-days if estimating facility efficiency.
- **Lowdham Grange and Parc MB-023; four functional reclassifications MB-025:** PFI versus M&M and Category C/YOI reporting shifts do not imply new physical prisons. Exact four-site MB-025 crosswalk remains open.
- **Altcourse MB-026:** PFI to M&M FY2023/24 and May/June commencement-date ambiguity, not a new institution.
- **Fosse Way MB-027:** FY2023/24 partial exposure after May 2023 opening; national FY2024/25 continued larger CNA cannot be read as an efficiency gain without capacity-time adjustment.
- **Ashfield MB-028:** Serco contract rebid and new 1 November 2024 contract start is verified (same operator/prison), not new construction.

## Research readiness and reuse policy

**Usable as source-specific/descriptive national financial accounting (with vintage and scope stated):** the 10 original-year aggregate totals, signed accounting hierarchy, CNA and 12-month-end average persons; each has precise original-cell provenance and 3 published financial identities reconciled for all 10 years. A sharp fall in denominator plus higher nominal cost *suggests possible fixed-cost arithmetic* but by itself does not establish a causal prison budget elasticity.

**Do not yet use for harmonised longitudinal/cross-country causal regression:** mixed publisher vintage Direct figures, pre/post education cost allocations, nominal vs deflated comparator labels, 2015/16 nonpay child class crosswalk, mislabeled sector comparatives, raw PFI vs public per-unit ratios, annual cost/available place-days without monthly capacity, or facility row counts without operator-period bridge.

**Before constructing a harmonised analytical panel:** choose a single fiscal year and publisher vintage; define direct/overall and nominal/real bases; attach appropriate MB flags; distinguish institution ID/operator spell/year accounting line; determine Baseline vs In Use vs Operational capacity; preserve source zeros and blanks; and keep original and transformed data in separate add-only artifacts with formulas and evidence.

## Completion and remaining dependencies

GB-019's *methodology catalogue* is complete under its microtask definition. It deliberately **does not** resolve the blocked original revised XLSX (GB-002/003), exact category-equivalence/accounting scope in MB-001–003/020, the full capacity-time numerator/denominator for MB-022/027, or physical identity/contract-date caveats. No new MB numbers were invented in this synthesis: the register remains v16 with **33 cases**, of which **25 directly concern GB prison finance** in this workstream. No indicator-period records were duplicated. The user can now query the source-specific concept-to-cell mapping and revision timeline without manually reopening every source.

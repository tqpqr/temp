# SESSION CHECKPOINT v14 — GB-008 original FY2019/20 supplementary costs (2026-10-14)

**Last truly finished atomic task: GB-008 DONE. NEXT: GB-009 (FY2020/21 supplementary original).** Git `main` head directly verified before checkpoint: `fb3d0a3cae660d21448a9bc2aa356326f9f4c184`. All original files and prior versioned outputs preserved, add-only. No work continues asynchronously after this response.

## Direct source inspection, provenance and date
- Original `GB/costs-prison-place-prisoner-2019-20-supplementary-information.ods`, source Git SHA-1 `c5ec73b1d01770d0229f46a85d14f53ebb21d0e6`, **41,569 bytes**; `Cover!A10` FY2019/20, `Cover!A19` **Published 29 October 2020**, England and Wales scope (NOT entire UK).
- Original ZIP/ODS `content.xml` decoded, **3 actual tabs** `Cover` (8), `T1_Contracted_Prisons` (41), `T2_Supplementary_Data` (44): **93 nonempty original physical source rows**, original A–K strings and row addresses preserved. No spreadsheet `table:formula` attributes for the 3 original source sheets.
- Already independently checked **118 FY2019/20 operator-specific detailed accounting financial rows** in `gb_cost_FY2018_21_469_raw_operator_facility_year_rows_v2_physical_rows.csv`; these have NOT been re-extracted or duplicated.

## National FY2019/20 source measurements
- `T2_Supplementary_Data!B59` Certified Normal Accommodation (CNA) **79,232 places**, **not** operational/useable capacity.
- `C59` annual-average prisoner population **82,890**, **not** a point-date monthly census.
- `D59` original Direct Resource Expenditure **£2,401,640,556**, `H59` Overall Resource Expenditure **£3,536,900,071**.
- `E59/F59` direct per place/prisoner **£30,311 / £28,974**; `I59/J59` overall per place/prisoner **£44,640 / £42,670**.
- `D49` Service Concession Arrangements child of Non Pay **£470,891,780**. Parent `D42` Non Pay **£1,066,908,261**, Payroll `D41` **£1,457,687,306**, signed income `D51` **−£122,955,011**. Parent & 8 child `D43:D50` are NOT additional expenses to add twice; overhead/capital `H53:H58` overall-only.

## New primary-source crosswalk: MB-021, linked to old MB-005 Birmingham takeover

- Original `T1_Contracted_Prisons!A5,A6,A13` reports **104 public + 13 contracted = 117** prison categories *at FY-end*. FY2018/19 source 103 + 14 = 117. Existing MB-005 independently identifies transfer of Birmingham to public sector in **July 2019**, and the 2019/20 **118** detailed financial lines have Birmingham and G4S Birmingham operator-period entries for one prison.
- In the FY2019/20 original supplementary T1, the 3 **named** Operate & Maintain contracts are Doncaster (`43`), Oakwood (`46`), Northumberland (`47`), while group subtotal is `48`. The source difference **subtotal minus these three named lines**:
  - **274 CNA places** = `C48-C43-C46-C47`.
  - **234 financial-year average prisoners** = `D48-D43-D46-D47`.
  - **£7,586,785 overall spending** = `E48-E43-E46-E47`.
- Independently audited separate original by-establishment FY2019/20 source `GB/costs-prison-place-prisoner-individual-prison-2019-20.ods`, blob `969df2a0a07b426ab6440e193bc8ea446637cc43`, `T3_Cost_by_Establishment!B156,C156,H156` **G4S Birmingham = 275 CNA, 235 average persons, £7,586,786 overall**. Three differences are **one unit each**, consistent with original publisher whole-number rounding. This strongly corroborates inclusion of a **partial-year private operator-period** in the contracted annual subtotal despite omission from the 3 year-end named contracts.
- **New MB-021** isolates this **supplementary table list-vs-subtotal source perimeter mismatch**, references existing broader **MB-005** operator-period transition. Neither issue means 118 distinct physical prisons, an additional private prison, publisher misaddition or £7.6m new extra expense outside the published subtotal. Explicit causal footnote for source subtotal bridge remains unavailable.
- Relevant cautions: `T1!A10:A11` and `T2!A64` warn public/private accounting perimeters not directly comparable. FY2019/20 `T2!D43` **Non payroll services £186,243,148** vs FY2018/19 **£50,452,976**, while `D45` Admin running expenses **£1,052,657** vs prior **£10,028,427**; these are **observed value differences only**, NOT verified method/reclassification break. Need publisher accounting definitions for causal interpretation.

## Artifacts saved, then re-fetched with exact Git blob SHA
1. [93 exact original source rows](progress/GB-008_2019_20_supplement_full_source_cells_v1.csv) blob `5e086ff118ac0435dffabd35b9860a9b79da0d05`; write commit `5c35b6c5e63ef57430f6fdc8225f96105818bf82`.
2. [32 original-source QA tests](progress/GB-008_2019_20_supplement_arithmetic_QA_v1.csv) blob `50897af4323de46e3b179b853f1fd4eeb9764fc8`; commit `847ab0e787b94893b03bc997804bffbd1646bf76`. Maximum absolute leftover whole-unit rounding discrepancy across 32 source/cross-source checks **2**, after independently matching residual to G4S source.
3. [GB-008 detailed original source-audit document](progress/GB-008_2019_20_supplement_source_audit_v1.md) blob `f8233936d1db56679b484404a9fa106428b0dc6a`; commit `c68c9a019378535b38dee569ab3812a750175169`.
4. [Indicator×reporting-period registry v11](INDICATOR_PERIOD_COVERAGE_REGISTRY_v11.csv): **1,011 evidence-graded records**, +28 `R00984`–`R01011`: 25 **original-publisher** national component/cost/denominator measures and 3 separately **labelled DERIVED original-source O&M residuals** (274/234/£7,586,785, not source-published national figures). Blob `a9ce62a33bd55c3c0e744f91dfdd3170cc88796c`; commit `5b397378f8e00bd77fa947f5fbf447364494a299`.
5. [Methodological issues ledger v7](METHODOLOGICAL_BREAKS_AND_ANOMALIES_v7.csv): **21 issues**, new **MB-021**; blob `efe563b894417d431da696268f604394abc4fcce`; commit `d94810bd087f89893edfb261b3a658fca252f0cb`.
6. [Microtask queue v12](MICROTASK_QUEUE_WAVE1_v12.csv): **12 DONE, 1 DONE_PRIOR_AUDIT_RECONCILED, 2 BLOCKED, 1 WAITING, 14 PENDING, 1 NEXT = 31**, GB-009 NEXT. Blob `a9b4d21e78fba7f6e6da2bd5f86f787597fe44aa`; commit `fb3d0a3cae660d21448a9bc2aa356326f9f4c184`.

## NEXT microtask GB-009 and prevention of duplicated work
Original `GB/costs-per-prison-place-prisoner-2020-21-supplementary-information.ods`. First consult [queue v12](MICROTASK_QUEUE_WAVE1_v12.csv), [indicator v11](INDICATOR_PERIOD_COVERAGE_REGISTRY_v11.csv), [methodological issues v7](METHODOLOGICAL_BREAKS_AND_ANOMALIES_v7.csv), existing [102 real source sheets catalogue](gb_cost_original_22_spreadsheets_102_worksheets_v2.csv) and prior FY2020/21 by-establishment **117** already checked accounting lines `gb_2018_21_469_rows_independent_3752_fields_and_Birmingham_restatement_QA_v1.md`. Check source formula/row layout, exact source category captions, FY and date, 2020/21 population vs CNA denominator and any public/contract accounting issues. **Do not assume a pandemic effect or source-meaning change without supporting original notes.** Write only missing source-specific QA/observations and explicit dual-catalogue decision, next queue v13, checkpoint v15 and index v20. No original, old catalog or audited by-establishment source rows overwritten. Original Git SHA-1 is not an externally checked publisher SHA-256; no background task runs.

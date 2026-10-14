# GB-022 — original 31 March 2020 HMPPS workforce XLSX forensic inspection

**Result:** completed original workbook audit and newly extracted **March** institution-grade source panel. Audit date 2026-10-14.

## Original identity and context
- Original source `GB/workforce/HR-tables-31-March-2020.xlsx`, original Git blob SHA-1 `c360e30210e0ef8a74d092cba474a8a423c4b6d3`, 291,448 bytes. The archived mirror/index previously recorded identical original Git SHA-1, but the original publisher binary SHA-256/download equivalence is **not independently verified**.
- ZIP/XLSX XML read directly from the original binary: `xl/workbook.xml`, `xl/sharedStrings.xml`, `xl/worksheets/sheet3.xml` (Table 1), `xl/worksheets/sheet23.xml` (Table 15), plus all workbook sheet captions for [28-sheet file inventory](GB-022_HR_March2020_28_sheet_catalog_v1.csv).
- Cover `Cover!A11:A16` identifies HMPPS Workforce Statistics Bulletin, **England and Wales**, date **31 March 2020**. This jurisdiction **is not the entire United Kingdom**.
- Table 1 source sheet `1. SIP x Structure` actual header `A4:M4`: financial year-end dates `C4:H4 = 31-Mar-2014 ... 31-Mar-2019`; quarter dates `I4:L4 = 30-Jun-2019, 30-Sep-2019, 31-Dec-2019, 31-Mar-2020`. The 2014–2019 historical values are **publication-vintage-specific**; do not assume they are unrevised contemporary publications.
- Table 15 `15. Snapshot of Estab. x Grade`, `A1`: **Snapshot of HMPPS staff in post by establishment, as at 31 March 2020**, `A2` **full time equivalent (FTE)**; `A4:Y4` has grade categories, `C:H` operational grades, `I` operational total, `J:W` non-operational grades, `X` non-operational total, `Y` grand total. **NOT headcount**; different sheets (`5. SIP x Diversity`, Table 5 etc.) explicitly use headcount and should never be merged as FTE.

## Unique source rows, numeric coverage and arithmetic QA
- `sheet23!A8:Y113`: **106 distinct source establishment names**, one original row per institution; physically complete 23 original numeric cells `C:Y` per row (2438 numeric establishment-grade cells). No nonnumeric `~` or publisher-blank `C:Y` in these 106 establishment lines.
- The collective source heading in A8 is **Prison Service and YCS Establishments**. It combines adult/public-prison and youth custody institutions; contains **no independently verified 106-name historical PSP/YCS segmentation**. Do not label all 106 as adult prisons or claim private prison employees are covered.
- New [one-day original raw panel](../../02_uk/gb_workforce_2020_03_establishment_grade_source_raw_v1.csv) stores each physical row and all 23 numeric fields with exact original XLSX value strings. No invented prison IDs, interpolation or classification; `0` retained distinct from blank. This is a NEW **2020-03-31** date, not a duplicate of older June 2020 and June 2015–2020 establishment panels.
- **All 23 column sums of 106 original institution rows agree with publisher 2020-03-31 source totals `sheet23!C114:Y114` to within 10^-6 FTE**. Maximum absolute column discrepancy: 7.276e-12 FTE.
- `sheet23!I114` operational total **27077.76114 FTE**; `X114` non-operational **8336.35967 FTE**, `Y114` combined 106-institution workforce **35414.12081 FTE**.
- Source `sheet3!L29` public prison regions **33883.90931 FTE**, `L9` youth custody **1530.2115 FTE**, equal to Table 15 106-institution total `Y114` when added. Their combined total is **not** identical to strictly PSP alone.
- `sheet23!Y7` HQ and Area Services **5186.59903 FTE**; `Y115` prison + YCS + HQ source grand total **40600.71984 FTE**. `sheet3!L37` NPS division staff **9413.80786 FTE**; adding them equals `sheet3!L38` full HMPPS **50014.5277 FTE**. All audited inter-sheet equalities within 10^-6 FTE.
- Coverage distinction: private-contracted prison personnel are not necessarily included in directly-employed HMPPS Table 15; one may not divide these staff counts by **all public + private** prison population and assert a matching sector numerator without a scope adjustment.

## Source anomalies and time-series caution (register action: NEW MB-018)

**Verified internal contradictory historical YCS dates**: original `1. SIP x Structure!A43` says “YCS, created in **April 2017**”, whereas original `15. Snapshot of Estab. x Grade!A118` says “YCS, created in **September 2017**”. Both descriptions are in **the same March 2020 workbook**. This does **not** prove which historical date is correct; causes could include different formation/operational implementation milestones or an editorial inconsistency. Keep both verbatim source anchors and flag `OPEN_CAUSAL_EXPLANATION` until checked against official administrative chronology. This affects naive time-series regrouping and should not be silently smoothed.

Other publisher notes:
- `sheet23!A119` explicitly warns that HR extracts are fixed-date captures from a dynamic database and late updates are not reflected; historic precision and revision caveat.
- `sheet23!A120`: The Verne recategorized July 2018 from immigration removal centre to category C male training prison.
- `sheet23!A121`: HMP Birmingham returned to public ownership 1 July 2019 and its staff then enter staff-in-post series; **not** automatically a true headcount growth at an unchanged institution universe. Already noted in other UK institutional-event work, not a claim of a new source duplicate.
- Raw source uses precise fractional FTE values; future analysis should preserve originals and only round in presentation, not before summing.

## Required twin-catalogue outcome

1. **Indicator × reporting period**: create additive v8 with 6 verified national/sector source measures for **2020-03-31** (HMPPS full service, PSP, YCS, HQ/Area, NPS, 106-establishment combined) and link source sheet/cells, units, evidence type. The 106 establishment source-row/grade matrix remains separately in the raw CSV; these are not comparable adult-only prison FTE measures.
2. **Methodological breaks:** create additive v5 retaining 17 old issues and new **MB-018** for divergent original YCS formation dates (open interpretation). The known Birmingham July 2019 coverage transfer is preserved in this QA as a dated administrative event, not automatically treated as unexplained staffing growth.

**GB-022 DONE. Next in queue should be first available pending task in queue v8 (choose by actual existing priority and dependencies); preserve original and all previous archive versions.**

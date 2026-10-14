# Court-form F1 forced-work anomaly (v2, supersedes v1) — 2026-10-14

## Verified source and coordinates
- Original file: `sud/2013 год/F1-2013.xls`
- Git blob SHA-1: `e3a2905fd8a77c5591f372c6617a995615d36780` (fetched from the actual original).
- OLE/BIFF sheet `Разделы 2, 3, 5` (2013 full calendar-year F1 report).
- Label **I11**: `Принудительные работы`.
- Reported numeric value **K11 = 33**. K-column header: `Всего лиц`; L-column header: `в том числе несовершеннолетних`.
- Confirmed source workbook shared strings: 450/450 decoded, and BIFF numeric cell read from source. **33 is the decoded workbook value, not a finding that 33 lawful sentences were in fact imposed.**

## Serious legal-timing contradiction
Articles introduced forced labour punishment concept in 2011, but laws of 2012 and 2013 postponed actual application of Criminal Code Art. 53.1 until **1 January 2017**. Official Prosecutor's Office confirmation:
https://epp.genproc.gov.ru/ru/proc_11/activity/legal-education/explain/e142368/
https://epp.genproc.gov.ru/ru/proc_30/activity/legal-education/explain/e283086/

Therefore **block using `2013,forced_work,33` as a valid sentenced-person trend observation** until reconciled. Possible explanations include a source-data problem, early report template/predefined formula, later historical revision, miscoding, or numerical extraction caveat. None is yet established. The presence of the label in 2013 does not establish implementation.

Cross-check exact workbook in a separate viewer; consult official annual judicial release and form notes; then compare K4 and related 2012–2016 sheets. Do not substitute zero, interpolate, delete or alter original XLS; retain the numeric cell in the raw five-anchor extraction and mark as `contradiction_pending_independent_resolution`.

The older v1 forensic note remains preserved, but v2 supplies the **exact confirmed source blob SHA** and is authoritative for this anomaly.

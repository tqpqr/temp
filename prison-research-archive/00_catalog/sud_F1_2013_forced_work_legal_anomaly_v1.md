# Forensic QA: 2013 F1 "forced work" reports 33 despite postponed implementation

**Date flagged:** 2026-10-14. **Disposition:** open research-critical anomaly; **do not amend source and do not treat as a verified operational punishment count.**

## Exact source-cell evidence

- Raw original: `sud/2013 год/F1-2013.xls`, Git blob SHA-1 `caution: use 2013 source file SHA in sud_historical_F1_K4_K7_sheet_anchors_v1.csv and source_inventory.csv` (not silently guessed here).
- Worksheet: `Разделы 2, 3, 5`.
- Label: original cell `I11` = `Принудительные работы`.
- Numeric: original cell `K11` = **33** (BIFF cell value recovered by read-only parser). Header of `K` in the third section = `Всего лиц`; `L` = minors.
- Period: 2013 calendar-year court form F1, 12-month report.
- Separate associated row under `Раздел 4` even mentions petitions to replace forced work with imprisonment and vice versa, despite subsequent effective date. Existence of headings in a reporting template is **not** evidence that those measures were operative.

## Independent legislative chronology

- 7 December 2011 Federal Law no. 420-FZ introduced the forced-work concept (Criminal Code article 53.1).
- Later federal laws no. 307-FZ (30 December 2012) and no. 431-FZ (28 December 2013) postponed practical application to **1 January 2017**.
- Official Prosecutor's Office explanation: https://epp.genproc.gov.ru/ru/proc_30/activity/legal-education/explain/e283086/ and https://epp.genproc.gov.ru/ru/proc_11/activity/legal-education/explain/e142368/
- Legislative documentation: https://base.garant.ru/70552616/

## Required investigation before inference

1. Check original file `F1-2013.xls` cell `K11` directly in a spreadsheet viewer: value 33, sheet/row/column, cell type and any formulas/footnotes.
2. Check 2013 form instructions and consolidated tables on official Судебный департамент releases and any corrections.
3. Cross-check similar data for 2012–2016 and other 2013 official forms; determine whether this is data entry, transitional coding, classification, report-vintage problem or a decoder issue.
4. If the numeral is real in the original and the code definition refers to the 2017-only penalty, treat as source anomaly rather than smoothing or filling with 0 without source commentary.

## Preservation note

The five-anchor file `sud_F1_historical_2005_2011_2013_2024_2025H1_penalties_v1.csv` intentionally retains the raw value. A future revised harmonised dataset must carry a dedicated `2013_forced_work_requires_resolution` flag, distinct from `NOT_PRESENT_IN_YEAR_FORM` used for absent 2005/2011 categories.

No original was edited, deleted or replaced.

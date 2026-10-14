# INT-001 — DONE: Italian DAP institutional prison capacity / inmate population, 31 January 2023

## Original source and scope
- **Original archived file:** `space-archive/extra/stp8/Italy_Detenuti_capienze_per_istituto_31-01-2023.html`
- **Source archived Git blob SHA-1:** `7c996ffe3d5daa3f34fa26bcd5a141dc0c1d24b6` (original and mirrored Git copies can be matched by SHA). Source HTML contains original publisher `RA4`…`RA193` HTML row identifiers.
- **Source header and caption:** `Detenuti presenti e capienza regolamentare degli istituti penitenziari; Situazione al 31 gennaio 2023`.
- **Issuer recorded in HTML:** Ministero della Giustizia, Dipartimento dell'Amministrazione Penitenziaria (DAP). Original embedded official primary URL: https://www.giustizia.it/giustizia/it/mg_1_14_1.page?contentId=SST414676 . The identical-date official statistics page's name/totals/footnote were also located in fresh web search; actual **external live page bytes were not downloaded and hashed**. Thus a government URL match is **not** an external binary-identity proof.
- **Data grain:** single calendar-day snapshot `2023-01-31`, **not** annual average, monthly mean, prison fiscal-year line, national prison budget, or stable multi-year facility identifier.
- **[Full original institution-level rows and official source total](INT-001_Italy_2023_01_31_189_facilities_original_cells_v1.csv)**: **189** individual institute lines `RA4`–`RA192` plus published `RA193` total. All original **eight columns** preserved verbatim; original source path, SHA, HTML row ID and publisher date. Typed integer copies/blank flags and `over_regulatory_capacity_derived` are clearly marked separately from original raw fields.
- Institution naming/types retained as published, not cross-country/cross-year harmonized; **20 published region names**; types found: CC, CR, CL, ICAM, CCF, IP, CRF (code definitions not independently checked).

## Original dimensions and full-source QA
| Publisher field (HTML column) | Verified sum of 189 original rows | Publisher `RA193` | Difference |
|---|---:|---:|---:|
| 5: Capienza Regolamentare (places) | 51403 | 51403 | 0 |
| 6: Detenuti presenti, totale (persons) | 56127 | 56127 | 0 |
| 7: Detenuti presenti, donne (persons) | 2392 | 2392 | 0 |
| 8: di cui stranieri (persons) | 17687 | 17687 | 0 |

All 189 rows have numeric published *capacity*, *total present persons* and *foreigners* cells. **140 of the 189 women's count cells are publisher blank HTML (`&nbsp;`), NOT numeric 0**: the CSV retains empty raw women entries and typed-null, though the national printed total equals the sum of explicit numbers. Neither this match nor apparent gender-specific institution types authorizes silently converting blanks into documented source zeros.

Published `present > regulatory capacity` in **119/189** institutional lines (source-value arithmetic) **at this one date**. This is not a validated operational-capacity exceedance measure; denominator is *regulatory*, and source explicitly says temporary departures from capacity may not be reflected. Source reg total 51403 vs present 56127 (systemwide ratio 109.19%; **derived**, not a published operational utilization rate). The published total and sum of detail agree exactly across all four national numeric fields.

## Critical official footnote — operational definition
The original archived HTML mirror **does not include the expanded capacity footnote** beneath the table. The contemporary official Ministry page (SST414676), independently read through public search indexing, gives the publisher's rule: **9 m² per single prisoner + 5 m² for each additional prisoner**, alongside sanitary services, and says the published regulatory capacity does **not** reflect temporary departures from stated available places. This exact definition requires a **separate comparability flag**. Do not equate to British `CNA`, UK operational capacity, SPACE usable capacity, staffed bed count, or number of open places. Official page: https://www.giustizia.it/giustizia/it/mg_1_14_1.page?contentId=SST414676

## Status in indicator-period register
Four directly measured institutional numerical dimensions are supported for **Italy, 2023-01-31**: `capienza_regolamentare`, `detenuti_totale`, `detenuti_donne` (only explicit source cells at 49 institutions; **140 published blanks**), `detenuti_stranieri`. Region, province, institution name and institution-type are verified dimensions of the same snapshot, not additional prison-time observations. Each observation can be retrieved by HTML source row `RA4`…`RA192`. This progresses beyond old `variable_dictionary_v2_additions.csv` `read_html_header` level; updated registry **v3** must not double count old header-only entries.

**INT-001 DONE:** all 189 institutional rows, national total and source-original exact row anchors verified. QA: four totals match exactly; all original/mirror bytes untouched. Next independent task from queue, as selected in its versioned successor.

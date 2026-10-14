# 2024 judicial source files — factual scope and inspection status (2026-10-14)

The 2024 year-folder contains **27 XLS source files**. Of those, **25 were successfully opened and parsed from original OLE/BIFF bytes**, including every BIFF8 shared string in each parsed workbook (SST decoded count equals SST declared count). Source sheet names and actual Russian titles are preserved in `sud_2024_content_verified_research_map_v2.csv`.

## Verified families (not filename assumptions)

- **F1**, first-instance criminal cases, Section 3 includes sentencing. **F6**, criminal appeals; **F8**, criminal cassation; **F11**, criminal supervisory review.
- **F3**, **F7**, **F9**, **F10** — civil/administrative justice. **F4** — criminal damages, material state recoveries and judicial expenses (related to economic effects but not punishment counts).
- **K4** — number of persons prosecuted / punishment types, original form 10.1; **K7** — punishment by most serious crime (no aggregation), original form 10.3; **K7.1** — length of imprisonment and fine size, original form 10.3.1. **K5.2** — recidivism among convicted persons. Other K forms index juvenile convictions, demography and offense types, criminal-proceedings characteristics and drug crimes.
- Seven **AC** files are arbitration-court statistical reports, not prison/judicial criminal sentencing; source title sheets explicitly say "арбитражных судов".
- **F2-2024** and **K3-2024**: connector returned empty base64 when requesting full content. The original files are present and nonzero-sized and are retained unmodified. They are **not corrupted by this evidence**; classify as *unreadable by current connector* until an alternate binary reader works.

## Verified underlying numeric dataset, not merely templates

Original `F1-2024.xls`, sheet `Раздел 3`, headings `Всего` and `Из них: несовершеннолетние лица` at D6/E6. Exact numeric BIFF source cells recovered:
- `D10=153002`: "лишение свободы на определенный срок" (2024 full year), `E10=2409` minors.
- `D12=21389`: "принудительные работы", `E12=12` minors.
- `D13=66798`: "обязательные работы", `E13=1717` minors.
- `D14=45924`: "исправительные работы", `E14=253` minors.
- `D17=116256`: conditional imprisonment, `E17=4000` minors.

A separate **2025 H1** F1 file has the same label/column arrangement and numeric values but covers only six months. Full per-cell extract preserving Git original SHA and date window: `sud_F1_2024FY_2025H1_sentencing_section3_verified_cells_v1.csv`. Never treat annual and H1 totals as equivalent time exposures; these are counts of **judicial sentencing**, not inmates actually held on an observation date.

## Longitudinal anchors

Additional original binaries inspected: 2005 `F1`, 2011/2013 `F1`, 2005/2013/2018/2023 `K4` and `K7`, 2014 `1AC`, and H1 2025 `F1` (some larger files could not be read). See `sud_historical_F1_K4_K7_sheet_anchors_v1.csv`. Verified F1 sheet counts: **four in 2005, six in 2013, nine in 2024 and H1 2025**. This corrects an earlier conversational description of 2025 F1 as having ten sheets: parsed workbook `F1-1-2025.xls` has **nine**. Even where category labels persist, sheet/row/column schemas may change by year.

## Verification boundary

A retrieved Git SHA plus decoded BIFF proves only source file identity and what labels/cells actually contain. It does **not** by itself establish that annual report universe, court classifications or punishment measures remained constant across editions. A 507-file full binary content audit remains open. All files created here are additive; no originals or older catalogues overwritten.

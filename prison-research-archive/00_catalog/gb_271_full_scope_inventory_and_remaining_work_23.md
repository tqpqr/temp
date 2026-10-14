# Britain / GB: complete original-file family inventory — archive coverage audit

## Scope and preservation
Baseline: original GitHub tree `373a14b4fe725329c050ca45a8db723d304766e5` in `tqpqr/temp`. This audit covers **all 271 original files under `GB/`** (includes `GB/workforce/`). New catalogues are stored under `prison-research-archive/00_catalog/`. No original source file modified, moved, deleted or overwritten.

## Exhaustive top-level families
| Original family | Files | Important status |
|---|---:|---|
| `GB/` monthly prisoner-population bulletins in DOC/DOCX/RTF/ODT/ODS/PDF | 189 | Complete original filename+Git blob inventory; content-level extraction **not yet finished** |
| `GB/workforce/` official HMPPS staff XLS/XLSX/ODS series | 53 | Binary family inventory complete; establishment-level FTE extracted and five-snapshot 2021–2025 matched. Full historical 2013–2026 workbook schemas still not exhausted |
| `GB/` financial prison-cost documents | 27 | FY2014/15 through FY2024/25 identified; 10 by-prison sheets, 10 supplementary, 5 summary PDFs, 2 restatements. Individual financial tables **not yet fully decoded** |
| `GB/annex-b-changes-to-format-population-bulletin-monthly.docx` | 1 | Methodology item inventoried, text not yet extracted |
| `GB/NAO_2026_costs-of-tackling-drug-harms-in-prisons.pdf` | 1 | Separate public-audit research reference, not core cost-per-prison time series; not yet text reviewed |
| **Total** | **271** | |

Raw 271-row inventory: `00_catalog/gb_all_271_files_family_manifest_v1.csv`.
Annual cost file index: `00_catalog/gb_costs_2014_2025_27_files_v1.csv`.
Population file index: `00_catalog/gb_monthly_population_189_files_date_screen_v1.csv`.

## Population dates / caution
Filename parsing recognizes 181/189 month-year labels, with **8 ambiguous** that require opening original content. Filename-year summary: 2010 1; 2011 11; 2012 12; 2013 11; 2014 11; 2015 12; 2016 8; 2017 12; 2018 12; 2019 12; 2020 11; 2021 12; 2022 12; 2023 13; 2024 11; 2025 12; 2026 8. A filename-month duplicate is not necessarily duplicate content and apparent missing months are not proof that source bulletins were not collected (see ambiguous files and filename aliases).

## Actual binary-content checks in this pass
Verified ZIP containers and `content.xml` members directly in:
- `GB/prison-pop-june-2023.ods`
- `GB/Monthly_Bulletin_June_2025_web.ODS`
- `GB/costs-per-prison-place-prisoner-individual-prison-2024-25.ods`
- `GB/costs-per-place-per-prisoner-2024-2025-supplementary-information.ods`

The first two have 5 ZIP entries; the latter two have 6 ZIP entries including embedded `media/image1.png`. **These ZIP-entry checks are not content-sheet extraction**, and do not authorize claiming variables, rows, values, or official definitions that have not been parsed.

## Priority remaining work to finish original archive task
1. Parse all 27 cost reports/tables, recording real sheet names, cost/year denominators, revisions, treatment of state-managed vs private prisons and direct financial dictionary.
2. Inspect monthly bulletin template generations and 8 ambiguous dated files, then extract monthly prisoner totals and capacity/operational-capacity definitions, preserving format breaks.
3. Audit the rest of 53 staff workbooks beyond the verified 2021–2025 Table 15: dates, sheets, levels, comparable variables.
4. Preserve source-accurate extracted CSV tables and data dictionary, trace every transformed row to original path and cell/sheet, and only afterward build population×cost×staff facility-key crosswalk.
5. **Archive-file relocation/copying remains distinct**: original files are currently in `GB/`; the catalogue and extracts are under `prison-research-archive/`. A full add-only copy of the **original binary files** into the new organized archive has *not yet happened*. Do not mark the user's original archive restructuring job complete based only on the extracted datasets.

This audit deliberately distinguishes **inventory**, **binary container validation**, **actual workbook content extraction**, and **analytical harmonization**.

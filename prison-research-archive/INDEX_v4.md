# Prison research archive — working navigator v4 (2026-10-14)

**Central research index with exact file paths, source provenance, original cell locators and explicit QA.** Previous [INDEX_v3.md](INDEX_v3.md), [INDEX_v2.md](INDEX_v2.md) and all originals remain intact. Nothing was deleted, re-encoded, renamed or silently de-duplicated.

## 1. Locate *any* source and see its original

- [Full source/copy manifest](00_catalog/archive_copy_manifest_v2.csv): 1,124 originals; 1,067 byte-identical organized copies; 57 unrelated satellite/geology sources excluded from copied collections and retained at origin.
- [SHA preservation verification](00_catalog/archive_postcommit_sha_validation_26.md): 1,067/1,067 source→mirror Git-SHA matches, zero missing, zero wrong hashes.
- [Collection content/provenance guide](00_catalog/COLLECTIONS_AND_EVIDENCE_v2.md) and [remaining work](00_catalog/REMAINING_WORK_v2.md).

## 2. Russian judicial statistics: **new source-content discoveries**

| Need | Verified catalogue / file | Evidence type |
|---|---|---|
| Find one of all 507 judicial source files by year, filename and reported window | [**Source register v5**](00_catalog/sud_form_file_register_v5.csv) | Original filename/SHA for all; new content title and sheet list where decoded |
| Browse the 27 documents published in the 2024 judicial source family by **what they actually report** | [**2024 source content map v2**](00_catalog/sud_2024_content_verified_research_map_v2.csv) | 25 actual XLS binaries read and BIFF8 shared strings fully decoded; 2 content reads blocked by provider |
| Find 2024 F-report worksheet titles, source fields | [F-series sheets](00_catalog/sud_2024_F_workbook_sheets_inspected_v1.csv) | 9 verified books |
| Find 2024 K-report worksheet titles, source fields | [K-series sheets](00_catalog/sud_2024_K_workbook_sheets_inspected_v1.csv) | 9 verified books |
| Identify arbitration-only files to avoid merging with criminal sanctions | [AC-series sheets](00_catalog/sud_2024_AC_workbook_sheets_inspected_v1.csv) | 7 verified arbitration workbooks |
| Search exact **court penalty and imprisonment labels** and source row/column | [2024 penal terminology cells](00_catalog/sud_2024_punishment_source_cell_labels_v1.csv) | 146 label cells across F1/K4/K6/K7/K7.1, actual BIFF labels |
| View **actual sentence counts** in 2024 annual and 2025 H1 court F1 | [2024 FY and 2025 H1 source cell extraction](00_catalog/sud_F1_2024FY_2025H1_sentencing_section3_verified_cells_v1.csv) | Original person-count numeric D/E cells and verbatim row names |
| Compare older F1 penalty rows by verified label and numeric cell | [**Five historical anchors**](00_catalog/sud_F1_historical_2005_2011_2013_2024_2025H1_penalties_v1.csv) | 50 code×period records for 2005/2011/2013/2024/2025-H1; absent categories remain missing, not zero |
| Track actual historical F1/K4/K7 worksheet changes | [Historical worksheet inspection](00_catalog/sud_historical_F1_K4_K7_sheet_anchors_v1.csv) | Original BIFF sheets + source headings at selected years |
| Investigate **2013 forced-work anomaly** | [2013 F1 legal-timing QA v2](00_catalog/sud_F1_2013_forced_work_legal_anomaly_v2.md) | Source cell `K11=33` conflicts with statutory 2017 start; BLOCK from inference |
| Understand F/K/AC reading status, methods and limits | [2024 content audit](00_catalog/sud_2024_workbook_content_audit_and_corrections_v2.md) | Verification and outstanding sources |

### Court-data highlights

**New primary-source interpretation verified in workbook contents:**

- `F1`: first-instance criminal cases, including section on imposed penalties; **do not equate court sentencing flows with stock of prisoners**.
- `K4`: actual `Форма 10.1`, number brought to criminal responsibility and sanction types.
- `K7`: actual `Форма 10.3`, punishment associated with the *most serious offense, before cumulation*.
- `K7.1`: actual `Форма 10.3.1`, custodial sentence duration and fine amounts.
- `K5.2`: recidivism/repeated crimes by persons sentenced.
- Seven `AC` are **arbitration courts**, distinct from criminal case sentencing; F3/F7/F9/F10 are largely civil/administrative justice.
- Source F1 has **4 sheets (2005), 6 (2013), 9 (2024), 9 (2025 H1)**. The previous conversational statement "10 sheets" for 2025 was incorrect and is explicitly corrected. Labels and cell positions changed.
- **2024 F2** (1,174,016 bytes) and **2024 K3** (1,057,792 bytes) remain uninspected at byte level because full base64 content was empty in the connector for these greater-than-1MiB XLS files. This is not evidence of corrupt sources.
- Report periods are separate: 20 full-year judicial folders (2005–2024), 2023/2024/2025 first-half-year folders, plus multiyear `Состояние судимости` summaries and one source-description PDF. 2025 is **not** yet a full-year local judicial report.

**Do not use raw 2013 F1 `Принудительные работы = 33` as a confirmed effective sentencing measure**: although a cell with this label/value is present, a later postponement law made such punishment applicable from 2017. The conflict is preserved and flagged, not edited.

### How the files were inspected

Read-only pure-JS [OLE/BIFF decoder v2](00_catalog/tools/ole_biff_xls_inspect_v2.js) fetches original XLS binaries, parses Compound File FAT/Workbook, BIFF8 sheet names, and SST+CONTINUE shared strings. The extracts record source-path+Git SHA, sheet, row and original cell labels. Selected numeric original BIFF NUMBER/RK/MULRK records were decoded separately. **All selected numeric values require cross-year validation before publication**, even with accurate source locators.

## 3. FSIN and other Russian sets

- [FSIN indicator dictionary](00_catalog/fsin_indicator_dictionary_v3.csv): 7,227 original observations; **300 unique indicator codes and 302 code/name/level variants**, actual workbook row locators, years 1995–2023.
- [FSIN 32 priority research series](00_catalog/fsin_research_series_v3.csv): prison population, personnel ceilings, correctional institutions, paid prison work, external employer labor, economic outputs and alternative penalties.
- [FSIN workbook QA](00_catalog/fsin_verified_quality_checks_v3.md): two code/label variants and 100 series with repeated nominal years.
- [Russian collection provenance](00_catalog/ru_collection_provenance_v3.csv): original statistic producers, aggregation and local datasets for FSIN, judicial archive, crime-statistics long/wide files.

**Never merge** FSIN population *stock*, court punishment *flows*, prison staff *establishment*, production and budget amounts solely on a year label. Preserve reporting dates, categories and changes in administrative coverage.

## 4. UK, SPACE and US — prior deep work remains

- Britain: [271 source manifest](00_catalog/gb_all_271_files_family_manifest_v1.csv), [189 monthly date screen](00_catalog/gb_monthly_population_189_files_date_screen_v1.csv), [27 prison cost files](00_catalog/gb_costs_2014_2025_27_files_v1.csv), workforce/capacity/cost derived records under [02_uk/](02_uk/).
- International: 111 SPACE originals (including national institutional lists/capacity references) and 14 other national sources with upstream URL mentions; [full archive map](00_catalog/archive_copy_manifest_v2.csv).
- United States: [20 JEET workbooks](00_catalog/jeet_20_workbooks_verified_index.csv) and [source attribution](00_catalog/jeet_official_source_identified.md). US *Corrections* includes non-custodial functions; per-capita spending is per resident not prisoner.

## Next forensic passes

1. Open inaccessible 2024 F2/K3 and other greater-than-1 MiB XLS by alternate binary transfer/reader; no claim of damage from GitHub connector limits.
2. Expand court F1 label/cell crosswalk to all years after identifying boundaries; then reconcile official revisions and pre-2017 forced-work discrepancy.
3. Read the 506 court-workbook types by known F/K/AC families, prioritizing K4, K7, K7.1 and recidivism data before non-criminal files.
4. Resume FSIN numeric variant-resolution, budget/7z source material and UK population/cost document-level provenance checks.

**Core rule:** originals and all previous editions are immutable in this workflow. New content catalogues and corrections are separately versioned. Source-value preservation is not the same as methodological comparability.

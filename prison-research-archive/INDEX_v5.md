# Prison research archive — working navigation v5 (14 October 2026)

**Research principle:** the goal is **not just to mirror filenames or prematurely model a chosen hypothesis**. Catalogue **what is physically inside each original**, who issued it, which date/population/unit/method applies, how extracted values connect to original sheets/pages/rows, and what remains unknown. Original files never moved, edited or overwritten.

Previous indexes [v4](INDEX_v4.md), [v3](INDEX_v3.md), [v2](INDEX_v2.md) are historical references. Their audit-stage claims can be superseded; this is the current index.

## 1. Start here — coverage of the **whole archive**, not just Britain

- [**Per-file research/evidence ledger v7 — 1,124 source originals**](00_catalog/ARCHIVE_PER_FILE_EVIDENCE_LEDGER_v7.csv): original path, byte-identical copy path if in-scope, blob SHA, collection, publisher URL when actually recorded, exact currently confirmed verification level, evidence document and next action for **every original file**.
- [**Family-level content completeness v7 — 24 collections**](00_catalog/ARCHIVE_CONTENT_COMPLETENESS_BY_COLLECTION_v7.csv): which have only filename metadata, checked containers, actual sheet/text contents or numeric cells; 57 non-prison-source originals remain explicitly excluded.
- [Source-copy hash validation](00_catalog/archive_postcommit_sha_validation_26.md): 1,067 same-SHA preserved original/copy pairs, original directory baseline preserved.
- [v7 scope and evidence update](00_catalog/ARCHIVE_EVIDENCE_STATUS_SYNC_20261014_v7.md).
- [Original-record provenance manifest](00_catalog/archive_copy_manifest_v2.csv): 1,124 original source entries; copied original Git SHA equality, upstream links only when actually recorded, unrecomputed SHA-256 manifest strings explicitly marked unverified.
- [Unfinished work list](00_catalog/REMAINING_WORK_v2.md): valid as a *baseline*, but UK ambiguous month dates, all 22 cost spreadsheet tabs and 4-year core establishment rows have since been advanced. For current gaps, consult the v7 ledger.

**Never mistake completed same-byte archival preservation for complete scientific content provenance.**

## 2. Britain — prison places, people, budgets, staff

### 27 financial documents, 22 source spreadsheets, 102 genuine worksheets

- [102 verified actual original XLSX/ODS sheets](00_catalog/gb_cost_original_22_spreadsheets_102_worksheets_v2.csv), with original path and SHA, fiscal year, real title, sheet/header and source row.
- [22-workbook original content inventory](00_catalog/gb_cost_22_spreadsheets_file_level_verified_v2.csv).
- [2018/19 accounting restatement/2022/23 reclassification/2024/25 exceptions and source interpretation](00_catalog/gb_cost_22_sources_methodology_restatement_audit_v2.md).
- [FY2021/22–FY2024/25 original **477 prison×financial-year rows**](00_catalog/gb_cost_FY2021_25_477_unharmonized_establishment_year_rows_v1.csv), with official prison name/function, CNA places, **annual average prisoners**, direct/overall costs GBP, source SHA and original worksheet row. Source counts by year: **119, 119, 120, 119**. **NOT** a harmonized four-year panel.
- [Original three-earlier-year row source and category QA](00_catalog/gb_cost_FY2021_24_3_source_workbooks_group_qa_v1.csv).
- [2024/25 original 119 institution numeric values](00_catalog/gb_2024_25_119_establishments_cost_population_source_values_v1.csv) and [second-pass independent original 952-field comparison, 0 mismatches](00_catalog/gb_2024_25_119_rows_independent_recheck_v1.md).
- [By-function original subtotal vs sum-of-published-rounded-institution rows](00_catalog/gb_2024_25_source_group_totals_reconciliation_v1.csv), [rounding denominator audit](00_catalog/gb_2024_25_cost_per_prisoner_rounding_qc_v1.csv).
- [Unharmonized exact-match-only institution name transitions](00_catalog/gb_cost_FY2021_25_prison_name_only_transitions_v1.csv). Name matches do not prove stable facilities.
- Read-only parser: [cost sheet audit helper](00_catalog/tools/gb_cost_spreadsheet_catalog_v1.js), [ODS ZIP helper](00_catalog/tools/uk_statistical_zip_parser_v2.js).

**Financial limits:** FY2018/19 direct expenditure restatement reallocates £129,111,488 of education/training without corresponding total overall expenditure rise. Unit costs use annual average population (with underlying fractional values), unlike monthly occupancy snapshots. Public/private finance, prisons under closure/reconfiguration and changed categories need special sample flags. **Five PDF financial summaries still need original page-by-page inspection.** The other 18 cost spreadsheets have had titles/headers/sample numbers inspected, **not every row decoded**.

### 189 monthly British bulletins

- [Original bulletin-date candidate screen](00_catalog/gb_monthly_population_189_files_date_screen_v1.csv).
- [Eight ambiguous source filenames now dated by opening original documents](00_catalog/gb_8_ambiguous_bulletins_content_dates_resolved_v1.csv). One alleged `.doc` source contains RTF; one `.ods` is *March 2020*.
- [Full original GB family inventory (271 files)](00_catalog/gb_all_271_files_family_manifest_v1.csv).
- **Outstanding**: source-content extraction of all bulletin templates, prison rows and capacity-type definition changes, official per-file upstream URLs.

### 53 staffing originals

- [Source family inventory](00_catalog/gb_all_271_files_family_manifest_v1.csv) and [prior five-snapshot 93-institution QA](00_catalog/gb_conservative_93_institution_sample_QA_21.md).
- **Outstanding**: all 53 workforce books full sheet/column/reference-date and public/privately-operated institution treatment audit.

## 3. Russia — full record of 507 court reports, FSIN and budgets

- [507 judicial source files with actual F/K/AC form classification where decoded](00_catalog/sud_form_file_register_v5.csv).
- [2024 actual XLS content and research families: 25 of 27 files read](00_catalog/sud_2024_content_verified_research_map_v2.csv); two >1MiB legacy workbooks unreturned through current connector but not damaged.
- [Court form F1 five source historical numeric anchors, with original row/cell reference](00_catalog/sud_F1_historical_2005_2011_2013_2024_2025H1_penalties_v1.csv). **Critical hold**: the 2013 F1 workbook reports 33 "forced work" sentences even though that punishment began taking effect in 2017; [forensic anomaly note](00_catalog/sud_F1_2013_forced_work_legal_anomaly_v2.md).
- [FSIN 300 indicator codes / 302 variants](00_catalog/fsin_indicator_dictionary_v3.csv); [32 research priority series](00_catalog/fsin_research_series_v3.csv).
- [Five Justice programme annual report/plan original DOCX titles and FSIN paragraphs](00_catalog/ru_justice_program_5_docx_actual_content_index_v1.csv) (2017, 2018, 2020, 2021 and separate implementation plan). These are not automatically federal budget expenditure records.
- [Collection source producers and attribution](00_catalog/ru_collection_provenance_v3.csv).
- **Outstanding**: 49 `fs-22/` archive budget/programme documents (especially `7z` internal content), 28 `svod/` original reports, 39 regional controls, 9 `rn1/` opaque PDFs; other 470 judiciary reports still only metadata-level in latest ledger. No silent publication-ready panel.

## 4. USA, SPACE, Germany and World Bank

- [US 2011 Census state-finance flat file original 12,777 fixed-length records, 151 E04/F04/G04 records, data-codebook position anomaly](00_catalog/us_2011_fixed_width_layout_and_corrections_audit_v1.md) and [original-source-code extract](00_catalog/us_2011_state_finance_corrections_E04_F04_G04_verified_v1.csv). `F04` and `G04` omit one respective government, not automatically a zero; separate *state* and *local* finance universes.
- [BJS JEET 20-source-workbook inventory](00_catalog/jeet_20_workbooks_verified_index.csv); `Corrections` broader than penitentiary prison operations, metrics include per-resident denominators.
- [Actual German official Destatis tables and World Bank PPP definitions + separate U.S. local government finances](00_catalog/international_reference_source_content_and_units_v1.md). In `24321-0003` German `Belegung` excludes temporarily absent prisoners, whereas UK prison bulletin `Population` may include authorized absence. GDP PPP is NOT the same as government-consumption PPP.
- SPACE original reports, national facility registries, and recorded upstream manifest links in [preservation source manifest](00_catalog/archive_copy_manifest_v2.csv). Country-by-country actual roster source/definition and operating-vs-nominal-capacity reconciliation remain open.

## Methodological / conservation contract

1. Original bytes and paths are immutable. Add new versioned audits; never delete or overwrite to "fix" errors.
2. A cell value should have original Git SHA + path + original workbook sheet and coordinate, or PDF page/row; reference period + statistical population + unit + revisions + publisher; derived transformations separate.
3. Keep **file/physical preservation**, **source found**, **original content decoded**, **numeric cells checked**, **cross-year comparable**, and **analysis-ready** as different statuses.
4. A dataset may contain published source anomalies or incomplete reports; preserve the anomalous raw number but mark inferential use blocked pending source/legal investigation.
5. Full scientific catalogue is unfinished until the remaining originals are content-inspected and exact upstream provenance distinguished from agency collection links. Track progress against v7 coverage ledger, not impressions.

**Next priority:** complete 5 British cost PDFs and historical 18 finance workbook numeric data; harmonize 477 raw institution-year rows with prison-function/restatement controls; then resume full UK monthly source contents plus Russian court and budget source-inspection passes, without neglecting SPACE and US evidence.

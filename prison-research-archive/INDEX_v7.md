# Prison research archive — navigation v7 (14 October 2026)

**CURRENT START PAGE** for the add-only catalogue. Earlier [v6](INDEX_v6.md), [v5](INDEX_v5.md), and original [README](README.md) are historical snapshots, not deleted or overwritten. Everything below is a *research inventory*, **not** one harmonized analytic dataset.

## Preservation (independently rechecked this session)
- Current original scope: **1,124** Git blobs outside `prison-research-archive/`; **1,067** in-scope prison research original blobs each have a matching byte-identical Git object within categorized `original_sources/` mirrors, and **57** separate satellite/geology blobs remain excluded and untouched.
- Existing copy/source provenance: [original-to-mirror manifest](00_catalog/archive_copy_manifest_v2.csv) and [older preservation audit](00_catalog/archive_postcommit_sha_validation_26.md). Matching **Git blob SHA-1** is content identity within Git; do not confuse this with external SHA-256.
- Latest [1,124-file evidence ledger **v10**](00_catalog/ARCHIVE_PER_FILE_EVIDENCE_LEDGER_v10.csv) records exact original/mirror path, SHA, inspection class, content, known publisher pages and remaining action. [Collection inspection rollup **v10**](00_catalog/ARCHIVE_CONTENT_COMPLETENESS_BY_COLLECTION_v10.csv): **24 families**, only **12 of 27** UK cost files have exhaustive T3 institution/accounting source-row extraction, ten other cost workbooks have sheet/header/sample content, five cost-summary PDFs remain metadata-only.

## UK 2014/15–2024/25 finance: source-accurate, not institution-harmonized
- **NEW** [FY2014/15–FY2017/18: 477 unharmonized actual-source establishment accounting lines](00_catalog/gb_cost_FY2014_18_477_source_establishment_accounting_rows_v1.csv) from four original source books (119 + 119 + 122 + 117).
- **NEW** [FY2014–2018, 44 published-function subtotal checks](00_catalog/gb_cost_FY2014_18_44_published_function_subtotals_QA_v1.csv) and [interpretation and missing-vintage flags](00_catalog/gb_cost_FY2014_18_methodology_QA_and_vintage_gaps_v1.md).
- **NEW** [Primary MoJ release and attachment URLs](00_catalog/gb_cost_FY2014_18_official_attachment_provenance_and_missing_2015_16_restatement_v1.csv). FY2015/16 **restated edition published in 2017** exists on government site but is **not** in the 27 original local GB finance files; do not silently substitute original FY2015/16.
- [FY2018/19 original and restated, FY2019/20, FY2020/21: 469 original accounting lines](00_catalog/gb_cost_FY2018_21_469_raw_operator_facility_year_rows_v1.csv), [second-pass 3,752 numeric source-cell checks](00_catalog/gb_2018_21_469_rows_independent_3752_fields_and_Birmingham_restatement_QA_v1.md). FY2018/19 appears twice; FY2019/20 Birmingham/G4S operator split is two reporting lines, not proof of two prisons.
- [FY2021/22–FY2024/25: 477 accounting rows](00_catalog/gb_cost_FY2021_25_477_unharmonized_establishment_year_rows_v1.csv), [second-pass 2,862 numeric checks](00_catalog/gb_2021_25_477_rows_independent_2862_numeric_cells_recheck_v1.md). [FY2024/25 119×8 field audit](00_catalog/gb_2024_25_119_rows_independent_recheck_v1.md).
- Total available extracted **source accounting lines 1,423** = 477 + 469 + 477. Removing 117 duplicate-vintage 2018/19 source rows **yields 1,306 reporting lines**, **NOT 1,306 analytically validated unique prison-years**. 2016/17 Other printed category count differs from actual reporting lines; other facility identity/scope changes remain unharmonized.
- [All 22 original cost workbooks and their 102 worksheets](00_catalog/gb_cost_original_22_spreadsheets_102_worksheets_v2.csv). Remaining UK cost source work: **10 supplementary workbooks**, **5 narrative PDFs**, **independent reread of 2014–18**, publication vintage and external byte-hash verification.

## UK population and prison workforce
- [271-file original UK family map](00_catalog/gb_all_271_files_family_manifest_v1.csv), comprising 189 monthly population bulletins, 53 workforce files, 27 finance originals, one bulletin methodology document, and one NAO report.
- [Eight ambiguous bulletin dates recovered](00_catalog/gb_8_ambiguous_bulletins_content_dates_resolved_v1.csv); [monthly actual-population extracts](02_uk/) need template-level denominator checks and consistency validation.
- [Previously tested 93-institution staffing subset](00_catalog/gb_conservative_93_institution_sample_QA_21.md); [2021–2025 workforce/population source matched draft](02_uk/gb_june_2021_2025_staff_population_capacity_annotated_join_v1.csv). Full 53-workbook sheet/year audit and robust institution event crosswalk still open; do not call the whole family individually source-cell verified on the basis of summary extracts.

## Russia
- [507 original judicial report files and inspected contents/limitations](00_catalog/sud_form_file_register_v5.csv); [five historical F1 original sentencings](00_catalog/sud_F1_historical_2005_2011_2013_2024_2025H1_penalties_v1.csv). [2013 apparent forced-work legal anomaly](00_catalog/sud_F1_2013_forced_work_legal_anomaly_v2.md) unresolved and never to be erased by automatic harmonization.
- [FSIN indicator dictionary](00_catalog/fsin_indicator_dictionary_v3.csv); [FSIN series](00_catalog/fsin_research_series_v3.csv); [Russian archive provenance](00_catalog/ru_source_recovery_and_sud_audit_v3.md). Other legal archives, 7z annual budget evidence, government reports and old XLS must be inspected by content.

## International / US
- [SPACE/country reference issues](00_catalog/international_reference_source_content_and_units_v1.md), [US Census 2011 original finance layout and corrections](00_catalog/us_2011_fixed_width_layout_and_corrections_audit_v1.md), [JEET official source inventory](00_catalog/jeet_20_workbooks_verified_index.csv). Official web links vs local downloaded-file byte identity and capacity metric comparability remain different proof grades.

## How to resume without repeating work
Read [**session checkpoint 2026-10-14**](00_catalog/SESSION_CHECKPOINT_20261014_v1.md) before making a new change. Continue new *versioned add-only* source-linked catalogues, always verify original SHA/labels/cells, and distinguish **preserved** / **metadata inventoried** / **actual source sheet read** / **numeric cells extracted** / **independently checked** / **analysis ready**.

**No deletion, replacement, renaming, or moving of original files; no destructive cleanup of earlier catalogues.**

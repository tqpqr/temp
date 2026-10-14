# Prison research archive — working index v3

**Last substantive catalogue pass: 14 October 2026.** This index points to the newest verified material. It is additive: [INDEX_v2.md](INDEX_v2.md) retains the complete source-copy layout and baseline preservation map.

## Find a file and verify preservation

- [Source → archive manifest](00_catalog/archive_copy_manifest_v2.csv): 1,124 baseline originals, 1,067 same-Git-blob archived copies, 57 separately scoped other-project originals.
- [Independent SHA check](00_catalog/archive_postcommit_sha_validation_26.md): 1,067/1,067 matches, 0 mismatches. No original was changed, deleted or replaced.
- [Collections by content and method](00_catalog/COLLECTIONS_AND_EVIDENCE_v2.md) and [open content-audit queue](00_catalog/REMAINING_WORK_v2.md).

## Russia: source documents and actual content-level inspections

### FSIN — source cells actually inspected

| Question | Open this file | Verification level |
|---|---|---|
| Find one of 300 indicator codes by Russian name/category | [FSIN indicator dictionary](00_catalog/fsin_indicator_dictionary_v3.csv) | **Original XLSX contents**, 302 code/category/name variants with source row locators |
| Find prison labour, production, staffing, capacity, alternative punishments | [32 curated research series](00_catalog/fsin_research_series_v3.csv) | Original code + year range + Excel row positions |
| Interpret these for the research programme | [FSIN research navigation](00_catalog/FSIN_RESEARCH_NAVIGATION_v3.md) | Analytical guidance with explicit no-silent-join cautions |
| Check unexpected years, duplicates and name conflicts | [FSIN quality-check log](00_catalog/fsin_verified_quality_checks_v3.md) | Verified workbook, 7,227 source observations, 300 codes, two variant codes, 100 repeated-year series |

**Why this matters:** The original FSIN file has 1995–2023 nominal-year labels despite its publisher's headline 2005–2023. Its series include `Y808000168–174` for paid labour in prison production versus external sites; but repeated code-years and shifting institution boundaries require caution. No actual numeric time series has yet been harmonized or silently de-duplicated.

Underlying collection: https://tochno.st/datasets/fsin_info (secondary compilation from FSIN, Rosstat and archived official publications).

### Judicial reports — fully located, not yet cell-decoded

| Question | Open this file | Verification level |
|---|---|---|
| Which of 507 court-source files, in which year/period, at which exact Git path? | [Court source-by-file index v4](00_catalog/sud_form_file_register_v4.csv) | Original path and SHA, nominal year and filename form code |
| How many reports per FY/H1, and which form names appear? | [Judicial period matrix v4](00_catalog/sud_period_form_matrix_v4.csv) | **20 full-year folders, 3 half-year folders**, multiyear-summaries and metadata PDF distinguished |
| Why earlier v3 interpreted metadata incorrectly? | [Correction log v4](00_catalog/sud_period_source_corrections_v4.md) | Explicit v4 supersession of v3 for FY/H1 coverage |

**Do not use 2025 as a complete judicial year:** only H1 2025 is in the current archive. The [aggregator collection](https://tochno.st/datasets/suddep_archive) describes 511 reports; this archive contains 506 XLS files plus one PDF. The difference of five report files is not yet reconciled.

### Crime statistics / collection origins

[Collection attribution register](00_catalog/ru_collection_provenance_v3.csv) covers FSIN, regional crime data and court forms. The `data_crimes_stat/` long/wide datasets are *two representations* of the [General Prosecutor's Office-derived crime collection](https://tochno.st/datasets/crime), not independent observations.

### Russian budgets and reports

The 49 `fs-22/` justice/budget files, 28 `svod/` government reports and 39 regional covariate spreadsheets remain mirrored and indexed by original paths, but their internal data dictionaries are **not yet exhaustive**. See [archive manifest](00_catalog/archive_copy_manifest_v2.csv).

## Britain, international and United States

- **UK**: 271 original files fully mirrored. [UK source inventory](00_catalog/gb_all_271_files_family_manifest_v1.csv), [population source date screen](00_catalog/gb_monthly_population_189_files_date_screen_v1.csv), [cost-file index](00_catalog/gb_costs_2014_2025_27_files_v1.csv), [staff QA and audit notes](00_catalog/gb_271_full_scope_inventory_and_remaining_work_23.md), derived `02_uk/*.csv`. Full multi-format bulletin and cost extraction is still open.
- **SPACE**: 111 originals plus 14 external country reference files. Two source manifests include 54 references to **52 distinct paths**, with upstream URLs as recorded in those manifests; SHA-256 values are not independently recomputed.
- **US JEET**: 20 BJS Justice Expenditure and Employment Tool books verified at worksheet XML level. [Source attribution](00_catalog/jeet_official_source_identified.md) and [workbook index](00_catalog/jeet_20_workbooks_verified_index.csv). `Corrections` is not prison-only, and per-capita denominators are residents, not prisoners.

## Verification vocabulary

- **preserved**: original and archived Git blobs share the same SHA — unchanged source bytes.
- **source attributed**: an authoritative aggregator/publisher has been identified, but individual file bytes may not yet be redownloaded and matched to the external original.
- **sheet examined**: Excel ZIP/workbook/XML parsed from the source file, with exact header and data row checks.
- **indexed by filename**: safe navigation only; the underlying XLS/PDF pages, variable meanings, and statistical universes are not yet validated.
- **analysis-ready**: not a status conferred by the previous four stages. It requires dates, source units, definitions, transformations and duplicates to be reconciled.

## Next work tranche

1. Unpack/inspect the 506 legacy judicial XLS files at table/sheet level and map codes to actual form titles; prioritize penal-sentencing and prison-related forms rather than blindly parsing every court report.
2. Audit the original FSIN description PDF by indicator, then build a documented source-date/priority rule for overlapping records, keeping all raw versions.
3. Inspect crime long/wide XLSX fields and regional units; validate actual row counts and variable codes.
4. Verify all 27 UK financial tables and 189 population bulletins at content level, then reconcile institution-level variables across cost, staff and capacity.
5. Continue international SPACE institution/capacity provenance checks by source country and publication year.

**Preservation rule:** do not edit, delete, rename or deduplicate anything in original folders. Add further versioned catalogues and extracts with exact source-line/cell references.

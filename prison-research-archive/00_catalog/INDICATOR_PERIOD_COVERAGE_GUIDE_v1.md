# Unified indicator × period availability registry — seed v1 (2026-10-14)

**Purpose:** unified, filterable entry point for which indicator *or form token*, geography, reporting window and evidence grade is actually documented in this archive. It **does not yet constitute a fully audited year-by-year/region-by-region indicator panel**. Do not infer availability for unlisted years or unexamined file cells.

**Machine-readable [registry CSV](INDICATOR_PERIOD_COVERAGE_REGISTRY_v1.csv) currently has 856 rows**. This is the first seed **built entirely from existing versioned catalogs, not new data acquisition**.

## What each row represents
- `indicator_nominal_bounds`: 302 rows
- `existing_variable_dictionary_entry`: 38 rows
- `file_presence_form_by_period_NOT_indicators`: 503 rows
- `source_numeric_values_extracted_all_available_editions`: 6 rows
- `source_numeric_values_extracted_subset_of_editions`: 2 rows
- `staff_sheet_snapshot_discovery`: 5 rows

These are different evidence objects, not necessarily 856 distinct economic indicators. They must **not** be added together as observations. The original two `variable_dictionary_v1.csv` / `variable_dictionary_v2_additions.csv` entries remain as imported reference records, even when they only provide a filename-derived conjecture. More recent verified UK financial field rows take precedence over old `GB-COST` title-only hints.

## The crucial period/evidence distinction
- `listed_periods_exact` is populated only when the existing register explicitly enumerates **verified file years**, an actual report form window, or a specifically observed date. A UK 2018/19 accounting edition may be represented twice in the source **without creating two calendar years**.
- `first_period_recorded` and `last_period_recorded` for **FSIN indicators are nominal bounds** indexed from source code/year rows. `distinct_nominal_years` preserves the count provided by source dictionary. Because individual year sets **have not been re-derived here**, **do not fill intermediate years automatically**, even if their span matches the count. Among 302 FSIN indicator records, 101 flag repeated code-year records. Actual multiple publications/codes and changed definitions need separate audit.
- `file_presence_form_by_period_NOT_indicators` identifies **source judicial form present** in a particular annual/H1 reporting folder. It does **not** claim any specific form numeric cell or sentencing measure has been extracted or remains comparable across form vintages. Historical extra multi-year 'Состояние судимости' documents remain in `sud_period_form_matrix_v4.csv`; not relabelled as annual forms.
- `source_numeric_values_extracted_all_available_editions` means **verified numeric source accounting-line cells**, not harmonized prisons. Original figures are separate for direct vs overall resource expense, and CNA vs annual average population.
- `staff_sheet_snapshot_discovery` distinguishes June 2021–2023 sheet recognition from 2024–2025 available extraction; snapshots are not interchangeable with annual staff strength.
- `existing_variable_dictionary_entry` deliberately retains the original `evidence_level` and raw-period wording rather than upgrading filename or metadata hints into a complete observational series.

## Data dictionary (key fields)
`source_domain`: collection/jurisdiction; `record_type`: fundamental evidence class; `indicator_code`: exact source code or court-form token; `indicator_name_original`: descriptive name (for English derived finance concepts, not an asserted official original English sheet header); `temporal_grain`: date, FY, calendar year, H1, source-specific; `listed_periods_exact`: explicit set when available; `coverage_evidence` and `numeric_evidence`: independent evidence strengths; `original_source_path`: exact single source path only when known; `original_git_blob_sha1`: source Git SHA-1 only (not downloaded external SHA-256); `source_reference`: authoritative prior evidence.

## Missing yet, not to disguise
1. **True per-indicator/per-year/per-territory coverage matrix** with `numeric_present`, `missing`, `blank`, `zero`, `not_checked`, and `publication_vintage` is not built yet for most sources.
2. FSIN actual per-code year enumeration/deduplication, source units and issuer verification incomplete.
3. Judicial form content and numerical field-level coverage remains largely unexamined (existence by year is strong, indicator coverage is not).
4. GB monthly bulletins 189 original files and 53 workforce books still await source-cell audits; year spans from filenames must not be counted as continuous usable series.
5. SPACE I/II country-variable-year coverage absent (country reports and data definitions differ); U.S. original financial raw layouts/methodology still partial.
6. Cross-jurisdiction concept equivalence, provider-accounting revisions, annual fiscal vs calendar periods, stable-institution identifiers need separate mapping.

## Next workflow rule
For every atomic audit task (e.g. RU-001, GB-005, INT-001), explicitly record **indicator code/name, units, target geographies, actual periods, source sheet/cell/page, publication version, numeric presence, source SHA and evidence grade**. Publish a **new additive registry v2/v3** when newly audited source fields or years are established; never silently overwrite this snapshot or infer continuous coverage.

**Master purpose:** answer both 'где лежит документ?' and 'есть ли показатель по этому периоду?' without confusing file availability and measurement availability.

## Existing authoritative source registers
- [FSIN indicator codes](fsin_indicator_dictionary_v3.csv); [FSIN selected research series](fsin_research_series_v3.csv)
- [Russian court form-year matrix](sud_period_form_matrix_v4.csv); [source form individual files](sud_form_file_register_v5.csv)
- [Variable dictionary v1](variable_dictionary_v1.csv); [additions v2](variable_dictionary_v2_additions.csv)
- [UK 2014/15–2017/18 original financial line extraction](gb_cost_FY2014_18_477_source_establishment_accounting_rows_v2.csv), [2018/19–2020/21](gb_cost_FY2018_21_469_raw_operator_facility_year_rows_v2_physical_rows.csv), [2021/22–2024/25](gb_cost_FY2021_25_477_unharmonized_establishment_year_rows_v2_physical_rows.csv)
- [UK workforce 2021–2025 sheet-level identification](gb_workforce_june_2021_2025_table15_coverage_10.md)
- [Completeness by 24 source families](ARCHIVE_CONTENT_COMPLETENESS_BY_COLLECTION_v11.csv)

**Integrity rule:** original sources, mirrors, past dictionaries, prior checkpoints and research panel data all remain unchanged.

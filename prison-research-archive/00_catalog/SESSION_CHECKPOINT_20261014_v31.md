# Checkpoint v31 — RU-002/RU-003 blocked, RU-004 completed; NEXT INT-002 (2026-10-14)

## Last completed full source inspection: RU-004
Original XLSX `fsin/data_fsin_info_103_v20240627.xlsx`, Git blob SHA-1 **ebc0c08de7a7e4279e6035637dea6df0ff519c4c**, binary bytes independently decoded from GitHub base64. ZIP XLSX 384430 bytes; 16 internal parts, one worksheet **data_clear** and 857 shared strings; 7228 source rows including header (7227 data records), **301 indicator codes**, 5149 distinct code-year groups.

Original row evidence:
- `00_catalog/progress/RU-004_fsin_Y808000001_original_cells_v1.csv` = 121 source rows for indicator code `Y808000001`, original `data_clear` physical row addresses/values/rounded/date/source preserved.
- `00_catalog/progress/RU-004_fsin_one_indicator_provenance_v1.md` = verified methods and source provenance. 2005 original row 3: od 825558 dated 2005-12-31 unrounded; row 4: short 828900 dated 2006-02-01 rounded; row 5339: rosstat 823400 dated 2005-12-31 rounded.
- Original XLSX includes 1079 code-year groups with >1 row; 619 with differing printed values; 328 with distinct data_date_t; 1059 with differing data_source. This is source heterogeneity, not proof of source error or that the three different numbers represent identical operational definitions.
- `00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v17.csv` = **34 cases**, +MB-034 `NON_UNIQUE_CODE_YEAR_ACROSS_SOURCE_DATE_AND_ROUNDING_VINTAGES`. Do not deduplicate by code-year or code-year-date without source/vintage/scope checks.
- `00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v16.csv` stays at **1136**: no new FY numeric rows inserted until canonical key/vintage and primary source meaning established. RU-004 task DONE for one representative indicator, NOT complete all-code statistical dataset.

## Source blockers preserved
- RU-002 exact original `sud/2024 год/K3-2024.xls`, Git SHA `f8ba40bf800be6733818f93fab28bb829cb2f5b9`, **1057792** Git directory bytes. Existing source mirror has same SHA; `fetch_file(base64)` returns empty content, binary blob fetch fails UTF-8 decode, runtime raw HTTP fails DNS. Workbook contents were NOT read. Block report `00_catalog/progress/RU-002_sud_K3_2024_binary_READ_BLOCKED_v1.md`. Status **BLOCKED**, no inferred name/sheets/indicators.
- RU-003 original `fs-22/2025 ПрФЗ.Прил_2_Расходы.7z`, Git SHA `7bb55f5a448c3498ff946f55e538a82ec051d26c`, **11653826** Git directory bytes. Current connector returns no binary data, no 7z entry listing possible. Block report `00_catalog/progress/RU-003_fs22_expense_7z_BINARY_BLOCKED_v1.md`. Status **BLOCKED** and no budget draft/actual identification beyond filename.
- Both sources remain intact in original Git paths. Authorized byte download or exact user-supplied originals needed before classification.

## Queue and source registries
- `00_catalog/MICROTASK_QUEUE_WAVE1_v26.csv`: **RU-002 BLOCKED**, **RU-003 BLOCKED**, **RU-004 DONE**, **INT-002 sole NEXT**. Across all 31 first-wave tasks, 24 DONE + 1 DONE_PRIOR_AUDIT_RECONCILED = **25 completed/reconciled**; 4 BLOCKED (GB-002, RU-001/002/003); 1 WAITING (GB-003); 1 NEXT (INT-002).
- `00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v17.csv`: **34** issues total (+MB-034).
- `00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v16.csv`: **1136** rows, intentionally unchanged. Prior UK GB-019 crosswalk/index remains available; original sources preserved add-only.

## NEXT: INT-002
`space-archive/extra/stp8/Finland_Paatos_vankipaikkojen_jakautumisesta_22.11.2021.pdf`. Read actual PDF (pages, images and footnotes), determine exact capacity regulation, institution names, effective date, issuer and why regulatory seats differ from operational capacity/persons. Preserve PDF original SHA and page anchors; never assume capacity is equivalent to British Baseline CNA or Italy capienza regolamentare. Link to already audited Italy INT-001 without false harmonisation. Source may need PDF skill and page screenshots when inspecting via web PDF.

**No background processes.** Resume from v31 checkpoint; next microtask INT-002 only. Previous checkpoint v30 GB-019 DONE.

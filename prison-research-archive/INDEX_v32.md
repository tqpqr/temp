# Prison research archive — active index v32 (2026-10-14)

**RU-004 DONE (sampled FSIN source), RU-002/RU-003 BLOCKED (binary access). NEXT INT-002.** [Checkpoint v31](00_catalog/SESSION_CHECKPOINT_20261014_v31.md).

## Latest original source inspections

- **RU-004, actual XLSX decoded:** original `fsin/data_fsin_info_103_v20240627.xlsx`, Git blob `ebc0c08de7a7e4279e6035637dea6df0ff519c4c`, 384430 decoded bytes. One genuine sheet `data_clear` (`A1:K1` column headers). 7227 original data rows, 301 distinct indicator codes, 5149 source code-year group keys.
- [RU-004 one-indicator audit](00_catalog/progress/RU-004_fsin_one_indicator_provenance_v1.md) and [121 original source rows for Y808000001](00_catalog/progress/RU-004_fsin_Y808000001_original_cells_v1.csv): 1079 repeated code-year groups in whole XLSX, of which 619 have differing printed values. 328 have differing reporting dates and 1059 differing source labels. One FY 2005 source cluster: 825558 (od, 2005_12_31), 828900 (short, 2006_02_01), 823400 (rosstat, 2005_12_31). Do not collapse or silently choose one.
- **MB-034** new: year+indicator_code are not unique stable observational keys in this FSIN source, sometimes not even code+year+date. Add source, round flag, observation date, publisher provenance and original physical row when designing the subsequent normalized series.
- **RU-002** [K3-2024 legacy XLS block report](00_catalog/progress/RU-002_sud_K3_2024_binary_READ_BLOCKED_v1.md): exact Git SHA `f8ba40bf800be6733818f93fab28bb829cb2f5b9`, 1057792 bytes, original/mirror identical Git object; connector yields no old XLS binary. Source indicator names, geography and numbers **unverified**.
- **RU-003** [2025 draft budget expense 7z block report](00_catalog/progress/RU-003_fs22_expense_7z_BINARY_BLOCKED_v1.md): exact Git SHA `7bb55f5a448c3498ff946f55e538a82ec051d26c`, 11653826 bytes, cannot list internal 7z entries without true bytes; draft not treated as actual spending.

## Current catalogues and queue

- [Queue v26](00_catalog/MICROTASK_QUEUE_WAVE1_v26.csv): RU-002 BLOCKED; RU-003 BLOCKED; RU-004 DONE; **INT-002 sole NEXT**. Among **31** first-wave tasks, **25 done/reconciled**, **4 blocked**, **1 waiting on another task**, **1 next**.
- [Indicator-period registry v16](00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v16.csv): **1136** entries unchanged. RU-004 7227 data rows are **not yet harmonized/inserted** because code-year duplicates require issuer/date-sensitive keys. No double counting.
- [Methodological breaks v17](00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v17.csv): **34** total (+MB-034 source/vintage duplication).
- Prior [GB-019 UK cost methodology synthesis](00_catalog/progress/GB-019_cost_methodology_synthesis_v1.md) and [main index v31](INDEX_v31.md) intact: 311 source cell/year concept mappings across FY2015/16–2024/25, 30/30 source accounting identity checks.

## Next
**INT-002** original PDF `space-archive/extra/stp8/Finland_Paatos_vankipaikkojen_jakautumisesta_22.11.2021.pdf`, audit regulation of prisoner-place distribution and definitions with exact pages/footnotes. Link to Italy INT-001 as different legal/operational capacity concepts rather than equating them. Original repo files remain untouched; archived artifacts only created with new version paths.

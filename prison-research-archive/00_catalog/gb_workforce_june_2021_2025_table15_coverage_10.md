# GB workforce historical establishment sheet discovery — June 2021–2025

## Direct source inspection
Five repository ODS source files were downloaded via connected GitHub and their compressed `content.xml` read (DEFLATE, in memory). The 2024 and 2025 records had been previously extracted fully; the 2021–2023 runs verified sheet names and XML table row counts.

| Snapshot | Original file | Workbook sheets | Table 15 XML rows (including headings/totals) |
|---|---|---:|---:|
| 2021-06-30 | `GB/workforce/hmpps-workforce-statistics-tables-jun-2021_final_version.ods` | 28 | 122 |
| 2022-06-30 | `GB/workforce/hmpps-workforce-statistics-tables-jun-2022_final.ods` | 28 | 121 |
| 2023-06-30 | `GB/workforce/hmpps-workforce-statistics-tables-jun-2023_final.ods` | 31 | 120 |
| 2024-06-30 | `GB/workforce/hmpps-workforce-statistics-tables-jun-2024_final.ods` | 31 | 122 |
| 2025-06-30 | `GB/workforce/hmpps-workforce-statistics-tables-jun-2025_final.ods` | 31 | 123 |

In each workbook, worksheet `15__Snapshot_of_Estab__x_Grade` contains an internal caption `Snapshot of HMPPS staff in post by establishment, as at 30 June <year>`.

**Evidence boundary:** The 2021–2023 sheets were identified and counted only. Institution lists, column-level comparability, staff numbers and exact series harmonization were not yet extracted. Do not describe this as a completed 2021–2025 facility panel. The 2024–2025 harmonized extract and its quality audit are separate: `02_uk/gb_workforce_2024_2025_establishment_panel_v1.csv` and `00_catalog/gb_workforce_institution_reconciliation_2024_2025_09.md`.

A 2026 source file and multiple 2013–2020 workbooks remain for the next historical schema audit. The data group may include Youth Custody Service and HQ categories, which need exclusion/stratification before prison-only analysis.

No original source files edited or deleted. New archive notes are add-only.

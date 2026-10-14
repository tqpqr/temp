# HMPPS June 2021–2025: completed five-snapshot extraction and panel audit

Date: 2026-10-14. Add-only operations in tqpqr/temp; all original source files remain untouched.

## Sources and outputs

Each source ODS `content.xml` was fetched as GitHub base64, DEFLATE-decompressed, and the table named `15__Snapshot_of_Estab__x_Grade` parsed:
- 2021: `GB/workforce/hmpps-workforce-statistics-tables-jun-2021_final_version.ods`
- 2022: `GB/workforce/hmpps-workforce-statistics-tables-jun-2022_final.ods`
- 2023: `GB/workforce/hmpps-workforce-statistics-tables-jun-2023_final.ods`
- 2024: `GB/workforce/hmpps-workforce-statistics-tables-jun-2024_final.ods`
- 2025: `GB/workforce/hmpps-workforce-statistics-tables-jun-2025_final.ods`

New files:
1. `prison-research-archive/02_uk/gb_workforce_2021_2023_establishments_extracted_v1.csv` — all 321 named 2021–2023 observations, 29 fields incl. operational and non-operational grade counts; HQ/area service rows included.
2. `prison-research-archive/02_uk/gb_workforce_2021_2025_institution_long_panel_v1.csv` — 536 named observations, 18 harmonized fields. This combines the preceding extract with earlier `gb_workforce_2024_2025_establishment_panel_v1.csv`. Both old output files remain unchanged.

## Verified five-year coverage

| Date | Institution/YCS rows | HQ or area/frontline support rows | Sum institutional operational FTE (includes YCS) |
|---|---:|---:|---:|
| 2021-06-30 | 105 | 2 | 27594.32502 |
| 2022-06-30 | 105 | 2 | 27258.59464 |
| 2023-06-30 | 105 | 2 | 28376.39845 |
| 2024-06-30 | 105 | 2 | 29783.23079 |
| 2025-06-30 | 106 | 2 | 28765.54227 |

Exactly **105 institution names** appear across all five years; **106 unique names** appear at any time; the additional 2025 entry is **Lowdham Grange**. These name matches are not proof of identical administrative or operational perimeter, and do not establish prison-only membership.

## QA
- 536/536 rows passed `operational_total_fte + nonoperational_total_fte == grand_total_fte` within 0.02 FTE.
- 536/536 rows have nonempty unit name and numeric top-level FTE totals.
- The 2021–2023 source table includes two Healthcare columns; these are not directly present in 2025 schema. The full-source extract preserves those columns, while the harmonized panel excludes them.
- 2021–2023 use `Bands 9–11 / Senior Managers (Operational)`, whereas 2024–2025 use `Bands 9–12 / Senior Managers`. A dedicated grade-definition flag preserves this nonidentical coverage.
- The original 2024–2025 raw positional export has a year-dependent schema shift; the harmonized files do not assume fixed positions for non-operational totals.

## Still not demonstrated
- Adult prison versus youth custody service flags for every institution.
- Renames, public/private transfers, functional changes, effective staffing universe.
- Longitudinal continuity back to 2013 or forward to 2026.
- Institution-specific inmate population and costs linkage.

**Interpretation:** a technically extracted five-snapshot **institution-name-based** workforce panel, *not* yet a validated causal analysis or strictly adult-prison balanced panel.

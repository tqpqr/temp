# GB HMPPS establishment staffing: direct comparison of June 2024 and June 2025

**Verified by parsing ODS content.xml from both original binaries**, not merely by consulting official website summaries.

## Source files
- `GB/workforce/hmpps-workforce-statistics-tables-jun-2024_final.ods`
- `GB/workforce/hmpps-workforce-statistics-tables-jun-2025_final.ods`

Both ODS archives were decompressed in memory (ZIP DEFLATE); each contains **31 sheets**, including `15__Snapshot_of_Estab__x_Grade`.

## Table structure
- 2024 table title: `Table 15: Snapshot of HMPPS staff in post by establishment, as at 30 June 2024`.
- 2025 table title: `Table 15: Snapshot of HMPPS staff in post by establishment, as at 30 June 2025`.
- Units: `full time equivalent` (FTE).
- Table XML rows incl. headings / subtotals: **122** (2024), **123** (2025).
- Both contain `Group` and `Establishment` fields and the same directly observed initial operational-grade columns: Bands 9-12/Senior Managers; Bands 6-8/Managers; Band 5/Custodial Managers; Band 4/Supervising Officer; Bands 3-4/Prison Officer (incl. specialists); Band 2/Operational Support; Operational Total.
- Non-operational grade breakdown follows the operational columns.
- Table group is `Prison Service and YCS Establishments`: **not solely adult prisons**. HQ/Frontline Support rows also precede institution rows.

## Matched institution sample — Operational Total (FTE)
| Establishment | 30 June 2024 | 30 June 2025 |
|---|---:|---:|
| Askham Grange | 53.79733 | 55.71624 |
| Aylesbury | 238.00571 | 233.66647 |
| Bedford | 233.60811 | 246.08109 |
| Belmarsh | 599.92178 | 571.77317 |

**These four matched rows were read from the original files.** This is enough to confirm an establishment × year analytical opportunity, *not* yet a fully harmonized panel covering every institution and year.

## Next validation before analytic use
1. Parse the complete establishment columns (including all non-operational fields) and all rows for both snapshots.
2. Classify prison versus YCS and exclude HQ/support/overall subtotal rows.
3. Match facility identifiers and identify establishment openings/closures/mergers/name changes across vintages.
4. Audit the other 2013–2026 workbook series for snapshot date, FTE versus headcount, source definition and establishment-level coverage.
5. Preserve archive originals. Only add new normalized series and crosswalk files.

Status: `two_actual_workbook_snapshots_verified; matched_sample_verified; full_panel_pending`.

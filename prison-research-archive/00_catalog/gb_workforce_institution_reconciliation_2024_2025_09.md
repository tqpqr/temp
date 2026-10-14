# Completed establishment-row reconciliation: HMPPS June 2024 vs June 2025

## Source and output
Original files read in full from repository `tqpqr/temp`:
- `GB/workforce/hmpps-workforce-statistics-tables-jun-2024_final.ods`
- `GB/workforce/hmpps-workforce-statistics-tables-jun-2025_final.ods`

Both original ODS `content.xml` files were DEFLATE-decompressed in memory and all rows of `15__Snapshot_of_Estab__x_Grade` parsed. No original was changed.

Canonical **year-specific corrected harmonized extraction**:
`prison-research-archive/02_uk/gb_workforce_2024_2025_establishment_panel_v1.csv`

Auxiliary raw positional dump:
`00_catalog/gb_workforce_establishment_rows_2024_2025_raw_v1.csv`.
**Important**: the positional raw dump uses 2025 labels as a common header; its 2024 non-operational-grade columns shift because two 2024 healthcare fields no longer appear in 2025. Do not use its column headings for year-2024 non-operational grades. Use the corrected harmonized panel, which explicitly maps source-year positions. Retain both files for audit.

## Full reconciliation
- 2024: 107 named rows (2 HQ/support + **105** institution rows).
- 2025: 108 named rows (2 HQ/support + **106** institution rows).
- Exact name matches among institution rows: **105**.
- 2024-only names: **none**.
- 2025-only name: **Lowdham Grange**.
- Do **not** assert Lowdham Grange is a genuinely newly opened prison. Entry into the HMPPS public-sector staff table can reflect operating-contract/administrative perimeter changes.
- The institutional group name in the source is `Prison Service and YCS Establishments`. Thus the 105 matched institutions include youth custody entities; adult-prison-only subset has not been independently tagged yet.

## Harmonization
Verified shared measurements: operational bands 9–12, 6–8, band 5 custodial managers, band 4 supervising officer, bands 3–4 prison officers incl. specialists, band 2 operational support, operational total, selected first 7 non-operational categories, non-operational total, grand total. Unit: FTE. Snapshot dates: **2024-06-30** and **2025-06-30**.

2024 contains additional non-operational columns `Healthcare - Nursing Grades` and `Healthcare - Other healthcare` that were absent from 2025 table headings. This is a **schema break**, not a reason to align columns by fixed numeric position. Non-operational total and grand total were mapped year-specifically. The reason for disappearance is not established and **cannot be inferred as actual staffing change**.

## Quality checks
- Harmonized dataset includes 215 named rows (HQ/support retained and flagged by literal group/name).
- Exactly 107 distinct names in 2024, 108 in 2025.
- Missing establishment or operational/nonoperational/grand total in the 215 rows: **zero**.
- `operational_total_fte + nonoperational_total_fte == grand_total_fte` to within 0.02 FTE: **215/215 passed**.
- Institutional operational FTE sums (includes YCS, excludes HQ/support):
  - 2024: **29,783.23079**;
  - 2025: **28,765.54227**.
  These are not directly the HMPPS overall staff totals. Changes must be adjusted for shifting boundaries and possibly YCS classifications.
- The 105 exact-name matched institutions form an initial **balanced 2024–2025 matched set**, with no assertion of a longer time series.
- Large observed change example: Dartmoor `Operational Total` 195.86562 FTE to 21.16218 FTE; this demands institutional-status investigation, not automatic treatment as generic attrition.

## Important outstanding item
The two snapshots have **not yet been systematically separated into adult prisons versus YCS institutions**, nor reconciled with 2013–2023 files. Those are separate completeness requirements for a full longitudinal 2013–2026 panel. Do not claim that multi-year panel exists yet.

Research-safe version: use the 2024/2025 matched panel with explicit administrative caveats; do not claim full UK workforce project completed.

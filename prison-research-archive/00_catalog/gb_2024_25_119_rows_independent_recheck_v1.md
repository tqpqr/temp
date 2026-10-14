# Independent second-pass recheck of 2024/25 UK by-prison source table (2026-10-14)

Original `GB/costs-per-prison-place-prisoner-individual-prison-2024-25.ods`, Git SHA-1 `f30558ca485065dfe3802ff52a3eb255d0a5ed0b`, original sheet `T3_Cost_by_Establishment`.

## Extraction integrity: independent source vs published archived extract
- **119 unique prison establishments** in the previously published 119-row source extract; no duplicated prison names/row numbers.
- Re-fetched the original `.ods` from the unmodified `GB/` source and independently joined each published row back to `T3` **by original worksheet row number**.
- Compared all **eight original numeric fields per establishment**, plus source institution name and Git original SHA: **952 of 952 numeric field comparisons match exactly**, with **0 discrepancies**.
- Re-extracted the original nine function-group `Totals` and compared with the corresponding sums of individually published institution rows, keeping their rounding difference as a separate QA dataset (see `gb_2024_25_source_group_totals_reconciliation_v1.csv`). The original financial document explicitly cautions that totals calculated from unrounded values may not equal sums of rounded line items.
- `gb_2024_25_cost_per_prisoner_rounding_qc_v1.csv`: an additional row-by-row ratio audit. Source calculated cost per prisoner **must NOT** be replaced by expenditure divided by rounded displayed average prisoners. The implied unrounded denominator from the ratio `expenditure / published cost per prisoner` is close to printed average population. This is a **consistency check**, not exact reconstruction of underlying unpublished fractional-year prison population. The cost ratio itself is also rounded.

## Policy- and research-critical denominator issue

Low-occupancy institutions exhibit nontrivial computed ratio errors if a researcher divides original spending by the displayed rounded mean population. E.g. original `Dartmoor` published mean population **53** and direct unit cost **£322,969**; direct expenditure per printed mean yields approximately **£325,000**, a >£2,000 arithmetic discrepancy entirely compatible with the original mean representing approximately **53.333** people. `Cookham Wood` has similar nontrivial deviation. The original 2024/25 `Notes_to_T3` separately flags their closures/reconfiguration as atypical. **Do not discard, repair or normalize these source values**, and do not treat these two institutions as steady-state prisons without explicit sample/period controls.

The original financial row itself is primary data; the implied figure is diagnostic only. The QA does not independently resolve original publisher recalculation formulas, monthly exposure adjustment, public/contracted financing, or historical establishment continuity.

## All prior work remains intact

This audit is ADD-ONLY. Prior 22 original workbook ×102 sheet catalogue, 119 original establishment extract, and all original UK/Census/Russia sources remain unchanged.

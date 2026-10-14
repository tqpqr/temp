# UK source-level cost table 2021/22–2024/25 (v1, 14 October 2026)

Four distinct, original `GB/` source files contribute 119+119+120+119=**477 original establishment × financial year observations**. All extracted from each year's original `T3_Cost_by_Establishment` tab with original Git blob SHA and worksheet row, without aggregate `Totals` rows.

Source data:
- `GB/costs-per-prison-place-and-prisoner-by-individual-prison-2021-2022.ods` — 119 institutions
- `GB/costs-per-prisoner-individual-prison-2022-2023.ods` — 119
- `GB/costs-per-prison-place-prisoner-individual-prison-2023-24.ods` — 120
- `GB/costs-per-prison-place-prisoner-individual-prison-2024-25.ods` — 119

[477-source-row union](gb_cost_FY2021_25_477_unharmonized_establishment_year_rows_v1.csv), [three earlier years source group QA](gb_cost_FY2021_24_3_source_workbooks_group_qa_v1.csv), [2024/25 independent numeric-cell verification](gb_2024_25_119_rows_independent_recheck_v1.md).

**Do not label these 477 rows as a stable four-year institution-level panel.** The original report category changed (e.g. the adult young offender classification folded into a broader category from 2022/23). Prison names are from the source originals. Name matches are direct textual matches only: possible renaming, openings/closures, co-managed facilities, ownership and prison-function changes have NOT been harmonized.

[Exact name overlap audit](gb_cost_FY2021_25_prison_name_only_transitions_v1.csv) records which literal prison names appear in adjacent annual cost tables; this is **not** evidence of stable same institution/custodial function, and source counts may differ by year. The annual reference population is financial-year average, while monthly GB population bulletins are date snapshots.

No original values, files or earlier schema audits overwritten.

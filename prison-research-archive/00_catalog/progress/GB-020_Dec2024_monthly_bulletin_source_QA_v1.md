# GB-020 — DONE: original December 2024 HMPPS monthly prison bulletin

**Original:** `GB/Monthly_Bulletin_December_2024_web.ODS`, Git SHA-1 `c99e84252254f04b29cfe01122b41b4cf09bfdae`, 11,570 bytes. Organized mirror has same SHA. Source tab `MonthlyBulletin`; A1 “Monthly Bulletin - December 2024”, **A2 Report Date : 30/12/2024**. A130 says compiled on *last working Monday* of December. These represent a **single dated stock snapshot**, not monthly mean, calendar-year mean or financial-year mean.

**Duplicate-work check:** all **120 original prison rows**, physical worksheet rows **5–124**, were already present in [2024 report-date validated source extract v2](../../02_uk/gb_monthly_prison_population_capacity_2024_report_date_validated_v2.csv). Re-read original ODS XML and compared its exact date, original row, establishment name and four numeric source fields against all 120 earlier records. **0 mismatches.** Reuse that already archived 120-row extraction; no extra redundant prison panel generated. Physical row references 5–160 are unaffected by ODS repeated-blank-row compression (repetitions occur after row 160). The original 2024 source-date error in a differently named April source is already recorded in [earlier correction](../gb_monthly_population_report_date_erratum_2023_2024.md), not rediscovered here.

## Verified original source numbers and non-additive total
See [five-number source reconciliation](GB-020_Dec2024_monthly_bulletin_national_source_reconciliation_v1.csv).

| Numeric field | Sum of 120 original institution cells | Published total, source row 125 | Difference |
|---|---:|---:|---:|
| Baseline CNA, B5:B124 | 83,596 | B125 83,596 | 0 |
| In Use CNA, C5:C124 | 79,409 | C125 79,409 | 0 |
| Operational Capacity, D5:D124 | **90,038** | **D125 88,688** (marked **) | **1,350** |
| Population, E5:E124 | 85,618 | E125 85,618 | 0 |

**MB-016, confirmed publisher transformation:** original footnotes **A129 and A149:A152** explicitly specify a national **operating margin of 1,350 places**: *Useable Operational Capacity* = sum of establishments' operational capacity minus margin. Thus **D125 is NOT the simple sum of D5:D124**, despite being printed below that column. The term “Useable” in the publisher is not interchangeable with In Use CNA (C125). An analyst who totals prison rows or copies printed total uses **90,038 or 88,688**, respectively: these are different denominators and must be named distinctly.

**Other publisher definitions and caveats:** A134:A135: CNA is the Prison Service's uncrowded accommodation concept; A137:A140: Baseline CNA excludes certain segregation and healthcare accommodation; A142:A143: In Use CNA = Baseline less temporarily unavailable spaces (for instance building work); A145:A147: individual Operational Capacity depends on operational security and regime judgement; A151:A152: national operating margin allows differentiated prisoner-placement needs. A128 says the printed population includes prisoners on authorised absence, so it need not equal number physically unlocked. A155:A156 distinguishes potential prison crowding from measured crowded individuals. **Not equivalent** to Italy's regulatory capacity.

**MB-017, local source exception:** `Littlehey`, **source row 72**, reports B72 Baseline CNA **1,176**, C72 In Use CNA **1,240**, D72 operational **1,236**, E72 population **1,234**. C72 exceeds B72 by **64**, contrary to the bulletin's verbal definition of In Use CNA as baseline minus unavailable cells. Source reading/previous CSV both agree, but the **cause is unverified**; preserve source values and flag as anomalous, do not force C≤B or alter raw cells. 18 source establishments have published operational capacity lower than in-use CNA; that alone does not prove error because operational restrictions may differ from certified accommodation.

All 120 rows have numeric values in each of the four fields, and no population exceeds its establishment's stated operational capacity in this particular file. The published **national** capacity margin remains a separate system-level adjustment.

**Indicator register decision:** add five verified `2024-12-30` entries: national Baseline CNA, In Use CNA, sum of original establishment operational capacities (derived source sum), national publisher usable operational capacity (D125), and national Population. Include original source cells, edition, original SHA, numeric evidence grade, method-break links MB-016 and MB-017, and clarify the 120 original institution rows were already recorded in older 2024 source panel.

**Breaks decision:** add MB-016 and MB-017 as source-anchored methodological anomalies to a new additive register. The first is fully explained by original notes; the second remains an **open interpretation**.

**GB-020 DONE**. Next independent task GB-021 (January and February 2025, two related ODS files), only if prior extraction does not already satisfy acceptance; otherwise move to the next unverified family.

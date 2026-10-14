# GB-021 — DONE: HMPPS original January and February 2025 monthly bulletins

**Audit date:** 2026-10-14. **Jurisdiction:** England and Wales, HMPPS (not UK-wide). **Granularity:** one-day stock snapshot on the last working Monday, **not** a monthly mean, calendar-year mean or fiscal-year average. **Original worksheet:** `MonthlyBulletin`.

## Original data and physical source anchors

| Original binary | Source Git blob SHA-1 | Source bytes | Exact A2 report date |
|---|---|---:|---|
| `GB/Monthly_Bulletin_January_2025_web.ODS` | `c6b2e940b63667f25d8056239c656d3a784f6e93` | 11,563 | `Report Date : 27/1/2025` |
| `GB/Monthly_Bulletin_February_2025_web.ODS` | `10aeba9b3c131918c6e32c406691c0ecc9577c96` | 11,581 | `Report Date : 24/2/2025` |

Source originals are ZIP/ODS binaries; decoded original `content.xml` contains respectively 155,007 and 155,025 uncompressed bytes. The existing original-row dataset `02_uk/gb_monthly_prison_population_capacity_2025_raw_v1.csv` was consulted **before** re-extracting. Both months already have **120 original prison records each** with report dates `2025-01-27` and `2025-02-24`, physical source rows **5–124** (A name; B Baseline CNA; C In Use CNA; D Operational Capacity; E Population). Comparing source row numbers and all four source numeric values with the existing 2025 source-row panel yields **120/120 matching institutions and 480/480 matching numeric fields for each bulletin** (960/960 numeric cells across both). No second 240-row prison dataset has been produced. One *non-numeric* string-escaping difference is present: `Peterborough (Male & Female)` in original source `A90` versus `Peterborough (Male &amp; Female)` in the existing CSV export; treat as HTML-entity encoding during name comparison, not a new prison, institutional split, or numerical data disagreement. Existing panel is deliberately unchanged.

## Original-source total reconciliation, both source row 125

| Source field (row 125) | Institution cells | Jan 27 2025 sum / published | Feb 24 2025 sum / published |
|---|---|---|---|
| Baseline CNA, `B125` | `B5:B124` | 83,560 / 83,560 | 83,557 / 83,557 |
| In Use CNA, `C125` | `C5:C124` | 79,428 / 79,428 | 79,340 / 79,340 |
| Operational Capacity | `D5:D124` vs **printed national `D125`** | **90,012 / 88,662\*\*** | **89,985 / 88,635\*\*** |
| Population, `E125` | `E5:E124` | 86,463 / 86,463 | 87,199 / 87,199 |

**Same verified mechanism as MB-016:** in **each** original, publisher footnotes `A129` and `A149:A152` explicitly define printed national **Useable Operational Capacity** as the sum of 120 prison Operational Capacities **less 1,350 operating-margin places**. Thus Jan `90,012 - 1,350 = 88,662`; Feb `89,985 - 1,350 = 88,635`. Both margins independently checked; the December 2024 margin was **not assumed unchanged**. Printed `D125` is not a simple column D sum, and is not the same concept as Baseline CNA or In Use CNA. In each edition `A128` notes population includes prisoners on authorised absence. `A130` specifies the last working Monday. `A134:A152` defines CNA/Operational/Useable capacity. Publisher external binary download/version identity remains **not independently checked**, although the two repository originals and their original Git identities were directly read.

## Local comparisons and anomaly decision

- January and February 2025: none of the 120 prison rows has **In Use CNA greater than Baseline CNA**; compare earlier source-local **MB-017 Littlehey December 2024** with January and February `A72:E72`: **Littlehey Baseline/In Use/Operational/Population = 1,125 / 1,125 / 1,237 / 1,235** (January), **1,125 / 1,125 / 1,237 / 1,231** (February). This establishes only that December's numerical anomaly is absent in these two later files; **it does not establish the reason for the December discrepancy**.
- Jan 19, Feb 18 original institutions have their individual Operational Capacity smaller than In Use CNA; this is not necessarily an internal inconsistency because operational capacity and certified accommodation are conceptually different.
- No automatic match or longitudinal classification for changing prison names/operators; no annualized rates calculated from dated snapshots.

## Two-catalogue decision and what was reused

**Indicator/period catalogue: UPDATE v7**, adding ten distinct *national one-day measure observations* (five for each exact date, source row and definition). They do **not** constitute new source facility rows, annual averages, or new sources. See [GB-021 10 source-cell observations](GB-021_monthly_two_sources_v1.csv). Source indicator `GB_monthly_operational_capacity_before_margin` is an explicitly **derived** sum of 120 published D-row cells; the national published usable value is in D125.

**Methodological break/anomaly register: NO_NEW_BREAK.** Existing [MB-016 in v4](../METHODOLOGICAL_BREAKS_AND_ANOMALIES_v4.csv) correctly describes the national margin mechanism and applies also on 2025-01-27 / 2025-02-24. MB-017 is kept OPEN for December Littlehey. The Peterborough HTML-entity distinction is documented here as a string normalization/QC note, **not** falsely promoted to an institutional or accounting break. Thus the versioned break register remains v4 (17 issues), unchanged.

**Original preservation:** source ODS, source mirror, existing 2025 prison-panel data, previous index/checkpoints/registries unchanged. **Task GB-021 DONE**; queue next **GB-022** (2020 HR source workbook staffing measure / units).

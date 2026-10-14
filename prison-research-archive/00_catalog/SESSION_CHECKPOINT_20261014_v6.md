# CHECKPOINT v6 — 2026-10-14: finalized atomic source round and mandatory coverage-register link

**Current latest Git `main` before this checkpoint:** `0f7facb429e1a99f1cf8fa50ebdc60e9b2b034d6`, corresponding to [active index v11](../INDEX_v11.md). This checkpoint is saved as a new versioned file, not an edit of v5. All source paths and previous catalogues are preserved.

## Integrity test
Untruncated Git recursive tree confirms **1,124 original blobs** outside archive folder and **1,067 source-identical classified mirror blobs**; the remaining **57** are deliberately non-prison geology/satellite originals in `alt/`, `alt2/`, `alt3/`, excluded from archive copies. All previously committed new outputs listed below found in the tree.

## Completed and remaining
- **RU-001 BLOCKED:** `sud/2024 год/F2-2024.xls` legacy binary is 1,174,016 bytes, Git blob SHA `061f154ecc737c69a21e9a3bac3793fef45efcc5`, identical copy. Binary content retrieval returns zero bytes or binary refusal in GitHub connector; runtime network unable to resolve raw GitHub. **No actual headers/numeric indicators discovered**, so **no new indicator entry**. [Evidence file](progress/RU-001_sud_F2_2024_binary_READ_BLOCKED_v1.md), commit `42f2f4f89ca2591528e038d0bab4f0c8380b6ba4`.
- **GB-005 DONE:** `GB/costs-per-prison-place-per-prisoner-2016-2017-supplementary-information.xlsx`, original SHA `38e68d1ff7cf3dfe68847819850d24b40427d15d`. All **99 original nonempty physical XLSX rows** copied into [exact source cell CSV](progress/GB-005_2016_17_supplement_full_source_cells_v1.csv); [methodology/QA note](progress/GB-005_2016_17_supplement_source_audit_v1.md). 9 reconciliations discrepancies ≤£1. National direct FY2016/17 resources **£1,943,546,987**, overall **£2,997,687,957**. Original `T2_Supplementary Data!D49` FY2016/17 reports **£454,911,681 Service Concession Arrangements**, absent as separate category name from inspected FY2015/16 supplement; potential category classification break, **no inferred operational cost movement**.
- **GB-004 previously DONE:** FY2015/16 companion [source cell CSV](progress/GB-004_2015_16_supplement_full_source_cells_v1.csv) and [QA note](progress/GB-004_2015_16_supplement_source_audit_v1.md) available. Original 100 nonempty physical rows; direct resources **£1,897,972,242**, overall **£2,753,747,261**.
- **GB-002 BLOCKED** from official 2015/16 restated source binary download limitation; **GB-003 WAITING** on these publisher bytes. No invented restatement comparison.

## Coverage registry and mandatory maintenance
[Unified indicator-period registry **v2**](INDICATOR_PERIOD_COVERAGE_REGISTRY_v2.csv) consists of **899 entries = old 856 + 43 source-cell verified UK fiscal year/accounting lines**; each new row stores original source path, Git SHA, source sheet+cell, fiscal year, numeric status/value and publisher date. **FY2015/16 contributed 22 new rows (18 component / 4 totals) and FY2016/17 contributed 21 new rows (17 component / 4 totals)**. [Administrative erratum](REGISTRY_v2_YEAR_OBSERVATION_COUNTS_ERRATUM_v1.md) corrects old queue v3/checkpoint v5 reversed year attribution, **not a data error**. Original unchanged v1 registry and source data preserved.

[Updated microtask protocol v2](MICROTASK_PROTOCOL_AND_QUEUE_v2.md) explicitly requires every completed task to make a **registry update or `REGISTRY_UNCHANGED` statement supported by evidence**. [Latest queue v4](MICROTASK_QUEUE_WAVE1_v4.csv) now correctly records exact task results and registry additions. Count: **DONE 4, BLOCKED 2, WAITING 1, PENDING 23, NEXT 1.** Both new protocol and queue were re-fetched after commits and verified.
[Active master index v11](../INDEX_v11.md). Original complete archive scientific source map remains at [index v8](../INDEX_v8.md).

## Immediate next action, independently bounded
**INT-001 NEXT:** `space-archive/extra/stp8/Italy_Detenuti_capienze_per_istituto_31-01-2023.html`. Header-level Italian entries already exist in `variable_dictionary_v2_additions.csv`, so the task must **examine numeric facility rows and source date / capacity definitions**, not just repeat those headings. If actual numeric evidence confirmed, add verified date-specific indicators to an **additive registry v3**; if not, record reason unchanged. Save `progress/INT-001_italy_capacity_source_v1.md`; then update queue v5, next checkpoint v7. Still do not alter original/mirrored source data.

## Latest durable commits (all actual writes, not prospective)
- GB-005 raw rows `8018ebee4ae2735d7233fd7d4ed6b1eb1b2c887f`; GB-005 QA `61132b9d2abd0bd99e2a145b08c91ee190d6b4a5`.
- Indicator v2 `2249b215b3046e6f31d19ffd93b6cc7d11f49559`.
- Protocol v2 `30945f9fed7942e1b6e1aa2cc615a282a6b92226`.
- Corrected queue v4 `ecd364476c6a79a988a1ec8b20e2dad430c98c79`.
- Active index v11 `0f7facb429e1a99f1cf8fa50ebdc60e9b2b034d6`.

**No asynchronous work ongoing.** On next turn use the paths and newest Git head, do not restart completed rounds.

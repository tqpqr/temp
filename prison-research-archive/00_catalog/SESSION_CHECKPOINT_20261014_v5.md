# CHECKPOINT v5 — 2026-10-14: RU-001 blocked, GB-005 audited, registry v2 updated

**Latest verified Git `main` HEAD before this checkpoint:** `e40e5157016d43993cb582dd280828bf66397d64`. All files below are new, add-only documents or derived catalogs. Do not overwrite past versions.

## Original archive preservation verification
Full Git recursive tree non-truncated, source category verification passed: **1,124** original blob paths outside `prison-research-archive/`, of which **1,067** have a categorized mirror blob with exact Git SHA identity, plus **57** unrelated geology/satellite sources in `alt/`, `alt2/`, `alt3/` deliberately not mirrored. New files are additive, all pre-existing originals and mirrors remain at their expected Git SHA.

## Tasks completed / blocked this session
**RU-001 BLOCKED**, original `sud/2024 год/F2-2024.xls`, 1,174,016 bytes, original/mirror SHA `061f154ecc737c69a21e9a3bac3793fef45efcc5`. GitHub file interface returns no binary payload (but does return metadata/SHA), direct Git blob fetch refuses binary, and runtime cannot DNS-resolve raw GitHub. **No content cells or titles have been read.** [Original-file read blocker](progress/RU-001_sud_F2_2024_binary_READ_BLOCKED_v1.md), commit `42f2f4f89ca2591528e038d0bab4f0c8380b6ba4`. Registry stays `file_presence_form_by_period_NOT_indicators` (as it should).

**GB-005 DONE**, original `GB/costs-per-prison-place-per-prisoner-2016-2017-supplementary-information.xlsx`, Git source SHA `38e68d1ff7cf3dfe68847819850d24b40427d15d`. [All three sheets, 99 nonempty source rows with true sheet addresses](progress/GB-005_2016_17_supplement_full_source_cells_v1.csv), commit `8018ebee4ae2735d7233fd7d4ed6b1eb1b2c887f`; [source audit](progress/GB-005_2016_17_supplement_source_audit_v1.md), commit `61132b9d2abd0bd99e2a145b08c91ee190d6b4a5`. Both files were fetched back after commit and exact text verified. Publisher 2016/17 national *direct* expense £1,943,546,987, *overall* £2,997,687,957. Nine independent publisher-reconciliation tests all within £1 rounding. FY2016/17 separate *Service Concession Arrangements* component **£454,911,681** at `T2_Supplementary Data!D49`; this category is not separately labelled in the FY2015/16 supplement. Also other category labels/allocations change. **Do not infer actual expense change from category-level shifts.** Public and private costs not directly comparable due to publisher's scope/accounting caution.

**GB-004 previously DONE**. FY2015/16 supplementary 100 original nonempty rows, original SHA `c5605a10b66c2b2e312f07329153a436a90451d5`. Source exact files [CSV](progress/GB-004_2015_16_supplement_full_source_cells_v1.csv) / [audit](progress/GB-004_2015_16_supplement_source_audit_v1.md). Direct/overall national totals £1,897,972,242 / £2,753,747,261.

**GB-002 BLOCKED** (missing publisher FY2015/16 restated XLSX actual binary), **GB-003 waiting** on it; these remain unchanged.

## Mandatory new catalog integration completed
[Unified indicator × time evidence registry v2](INDICATOR_PERIOD_COVERAGE_REGISTRY_v2.csv): **899 rows**, preserving all 856 old rows plus **43 verified new national accounting category/total rows** (21 FY2015/16, 22 FY2016/17), each period-specific, with original SHA, original Excel sheet/cell, published value, units, publisher edition, numeric evidence level, and accounting noncomparability. New registry commit `2249b215b3046e6f31d19ffd93b6cc7d11f49559`, re-fetched exact content verified. 302 legacy FSIN nominal range entries and 503 Russian judicial period×form source presence entries remain just that; **not 805 verified numerical series**.

[Protocol v2](MICROTASK_PROTOCOL_AND_QUEUE_v2.md) now explicitly requires **for every single-source audit**: evaluate new indicator and period evidence; update versioned registry if actually verified new observations; otherwise write `REGISTRY_UNCHANGED` and why. [Queue v3](MICROTASK_QUEUE_WAVE1_v3.csv) has `DONE=4`, `BLOCKED=2`, `WAITING_ON_GB-002=1`, `PENDING=23`, `NEXT=1`, status reasons and registry update instruction; both file writes separately re-read and confirmed. Active [index v10](../INDEX_v10.md), previous v9 and v8 preserved.

## Next one-source job — INT-001
Original `space-archive/extra/stp8/Italy_Detenuti_capienze_per_istituto_31-01-2023.html`.
- Verify original Git SHA/mirror, contents, issuer, actual date 2023-01-31, prison-level facility and columns; distinguish legal/rated capacity from operational capacity and occupancy.
- Existing `variable_dictionary_v2_additions.csv` already lists Italian headings but at `read_html_header` grade. **Do not repeat superficial header inspection**: read data rows and determine exact numeric availability & reported coverage.
- Save one new versioned `progress/INT-001_italy_capacity_source_v1.md` and narrow source data extract if needed; re-fetch saved artifacts.
- Update **indicator period registry v3 only if new verified numerical indicator-period evidence was read**; otherwise explicit unchanged reason. Then update queue v4 and checkpoint v6 if status changed.

**No work is happening asynchronously beyond these Git commits.** Current user request is complete for this bounded round; resume from these exact versioned artifacts.

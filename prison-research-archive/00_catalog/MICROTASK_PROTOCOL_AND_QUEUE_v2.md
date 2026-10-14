# Atomic archive work protocol v2 — source + period-indicator registry coupling (2026-10-14)

This version **supersedes v1 for new tasks**, but does not overwrite it: [historical v1](MICROTASK_PROTOCOL_AND_QUEUE_v1.md). Work proceeds by short atomic microtasks in [current wave queue v3](MICROTASK_QUEUE_WAVE1_v3.csv). This protocol retains the original goal: faithfully and deeply cataloguing the original prison-research archive so source, variables, periods, provenance and caveats can be found later.

## Non-negotiable microtask unit
- **One original file**, or two source files only for a narrow edition comparison. One question and one bounded source read per task.
- Confirm original repository path, Git blob SHA, size and categorized byte-identical mirror before reading. **Never edit/delete/rename/move** original data, categorized mirrors, older QA, indices, snapshots or progress.
- Extract what is actually in the file: original report title/issuer, geography, fiscal/calendar/half-year/monthly/snapshot dates, **actual indicator code and unit**, headers, year-by-year coverage, sheet/page/physical cell address, source version, numerical existence and blanks/zeros, numerical values if relevant and feasible.
- Keep separate: `FILE_PRESENT`, `HEADER_READ`, `NUMERIC_ORIGINAL_CELL_CHECKED`, `SOURCE_SERIES_COMPATIBLE`. A form-token or filename never constitutes a numerically verified indicator. Do **not** assume that year bounds imply no missing years.
- Publish a **new versioned task evidence file** in `00_catalog/progress/`, containing source SHA, addresses, explicitly unresolved questions and substantive findings. Large extracted rows in their own versioned source CSV. Re-fetch new files, verify exact contents, then report the resulting commit.
- If a byte-access or format limit prevents analysis, record `BLOCKED` with an exact tool failure, original SHA and a resumption condition. Do not guess its contents; proceed to another independent task.

## New mandatory step: update the indicator × period register

**Every task's completion checklist now includes a registry decision.**

1. Match each real observed field to a code or exact publisher field label, original geographic unit and source reporting window. Distinguish entire FY, calendar year, H1, month, and one-day snapshot. Preserve edition/vintage and original source SHA.
2. Record an explicit **period × indicator × source** entry for each genuinely checked period, including actual source cell/page and `numeric_status` (observed value, published zero, blank, not inspected, unavailable) where this has been verified.
3. **If new indicator-period facts exist**, publish an additive `INDICATOR_PERIOD_COVERAGE_REGISTRY_vN.csv` deriving from latest verified prior version and append only verified new source coverage (retain earlier evidence, never silently upgrade it). If no new facts exist, write **`REGISTRY_UNCHANGED` with why** in that task's progress report and queue, not a speculative row.
4. Split accounting parent totals from subordinate expense categories; never sum the same expenditures twice. If publication classifications or methodology change, make **period-specific entries and mark comparability unresolved** (e.g., 2015/16 vs 2016/17 UK Service Concession Arrangements, Non-payroll services).
5. A file may be preserved/metadata-indexed yet still have **no verified indicator**; a category may appear in FY2016/17 but not separately in FY2015/16. Missing label is **not numerical zero**. Do not fill gaps or create a tidy synthetic panel while cataloguing sources.
6. The most recent full indicator-period register is [v2 (899 entries)](INDICATOR_PERIOD_COVERAGE_REGISTRY_v2.csv), with **43 newly checked UK national component/total observations for FY2015/16 and 2016/17**. [v1 (856 entries)](INDICATOR_PERIOD_COVERAGE_REGISTRY_v1.csv) remains preserved. Original fiscal source-cell records for v2 additions: [GB-004](progress/GB-004_2015_16_supplement_full_source_cells_v1.csv) and [GB-005](progress/GB-005_2016_17_supplement_full_source_cells_v1.csv). This remains a progressive **evidence registry**, not a harmonized national/institutional numerical panel.

## Done definition and interruption handling
`DONE` requires **(a)** source verified/read to stated depth, **(b)** progress artifact committed and re-fetched, **(c)** indicator-registry added with verified coverage **or explicit reason no update**, and **(d)** appropriate versioned task status in queue. Do not claim completion when binary remains unreadable: `BLOCKED` is distinct.

After disconnection resume from latest [index v10](../INDEX_v10.md), latest numbered checkpoint, the queue v3, and specifically its `NEXT` task; compare Git head and file existence before retrying. Never repeat all previous steps just because an assistant turn was interrupted.

## Current results and immediate next source
- `GB-004 DONE` — FY2015/16 supplementary costs, 100 original nonempty sheet rows, 7 checks, period-specific expense components in registry v2.
- `RU-001 BLOCKED` — 1,174,016-byte `sud/2024 год/F2-2024.xls` content inaccessible; original Git blob/mirror verified but internal columns NOT read. The registry must **stay file-presence only** for this file.
- `GB-005 DONE` — FY2016/17 supplementary costs, 99 original nonempty sheet rows, 9 checks, *Service Concession Arrangements* £454,911,681 appears as own accounting category with **classification break** relative to FY2015/16; 2016/17 categories appear in register v2. **This does not establish real change in operations.**
- `INT-001 NEXT`: `space-archive/extra/stp8/Italy_Detenuti_capienze_per_istituto_31-01-2023.html`, one source, facility count/regulatory capacity/present prisoner definitions and exact point-in-time period. Verify content, source SHA, original column provenance. Append new evidence to next registry version only when genuinely new.
- Other independent pending streams in queue: `GB-014` finance PDF, `US-001` finance codebook, `GB-020` first population bulletin, `RU-003` 7z budget container.

**Scope reminder:** the archive includes 1,067 in-scope research original copies, so systematic evidence catalogue must eventually cover RU judicial, FSIN, SPACE, population, workforce, cost, and US records, not only the subset in this wave.

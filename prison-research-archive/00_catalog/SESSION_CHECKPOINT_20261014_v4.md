# CHECKPOINT v4 — indicator period registry added (2026-10-14)

**Latest HEAD before checkpoint:** `e12b0399e59c70e96fa3e9ce16b0bbe588644846` (`prison-research-archive/INDEX_v9.md`). Continue from [active index v9](../INDEX_v9.md), not older INDEX v8; the latter remains intact and holds all earlier source datasets. No deletions, moves, source rewrites or overwrites.

## Preserved original data
Entire recursive Git tree complete, not truncated: **1,124 originals**, **1,067 byte-identical research mirrors**, **57 deliberately excluded other-project originals** under `alt/`, `alt2/`, `alt3/`. All preservation comparisons still passed after new documentation commits.

## Newly saved and read-back verified
- [`INDICATOR_PERIOD_COVERAGE_REGISTRY_v1.csv`](INDICATOR_PERIOD_COVERAGE_REGISTRY_v1.csv), **856 entries**: 302 FSIN nominal indicator range records; 503 RU form token × calendar-year/H1 `file exists` records; 38 entries from old variable dictionaries; 6 GB cost source fields tracked across fiscal years 2014/15–2024/25; 2 per-place fields currently confirmed in 2014/15–2020/21 v2 extracts; 5 GB workforce dated sheet discoveries.
- [`INDICATOR_PERIOD_COVERAGE_GUIDE_v1.md`](INDICATOR_PERIOD_COVERAGE_GUIDE_v1.md): meaning of evidence grades and unverified gaps. **Neither 856 rows nor 302 FSIN codes constitutes 856 or 302 verified gap-free comparable numeric series**.
- [Active index v9](../INDEX_v9.md); original full [index v8](../INDEX_v8.md) left unchanged.
- New registry CSV commit `645b91aa90bcac2a80e3d0664664fbd086ca4e85`, guide commit `6c340884f777f122c5f00a96fc1b3017790e73da`, active index v9 commit `e12b0399e59c70e96fa3e9ce16b0bbe588644846`. All new file contents were re-fetched verbatim after write.

## Previous microtask statuses still current
PRE-000 DONE, GB-001 DONE, GB-002 BLOCKED (publisher's FY2015/16 restated XLSX *bytes* unavailable), GB-003 WAITING_ON_GB-002, GB-004 DONE (100 original nonempty rows of FY2015/16 supplementary workbook). See [previous checkpoint v3](SESSION_CHECKPOINT_20261014_v3.md), [task queue v2](MICROTASK_QUEUE_WAVE1_v2.csv). No GB source numbers were changed.

## Next task
**RU-001 NEXT:** one source file `sud/2024 год/F2-2024.xls` — recover actual sheet names, row/column headers and evidence via appropriate legacy XLS reader, not filename guesses. Save one new versioned `progress/RU-001_sud_F2_2024_v1.md`, and if useful a small source-cell inventory. After committing, update additive microtask queue snapshot v3 and indicator coverage register v2 *only if new numeric-indicator or date evidence is genuinely established*. Otherwise leave old register values unchanged and mark partial/blocker.

## Future extension
The current master is deliberately **index-of-evidence seed** rather than final matrix: true `indicator × period × territory × source edition × status` requires original per-source numerical examination. Detailed 189 monthly GB original bulletin windows, SPACE country report variables and 7z budget internal components remain to be audited in bounded tasks. Preserve distinct not-reviewed/missing/blank/zero states and distinct calendar/fiscal/H1/monthly/snapshot time axes.

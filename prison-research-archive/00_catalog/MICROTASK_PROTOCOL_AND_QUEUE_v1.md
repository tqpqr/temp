# Prison archive: atomic microtask protocol & wave-1 queue (2026-10-14)

**Purpose:** prevent long, fragile multi-source operations and preserve the initial objective: content-level systematic organization, original paths, real primary provenance, and reusable retrieval. **This is a new add-only protocol, not a claim that the scientific archive is complete.**

## Current verified starting point

Latest pre-plan Git `main` commit: `6519ac3274eb9b22f5fdcd73a875d1ab883bd1ed` (`INDEX_v8.md`). Current full, untruncated Git tree independently shows **1,124 original files** outside `prison-research-archive/`; **1,067** matching content-identical research source blobs in categorized mirrors; remaining **57** geology/satellite files in `alt/`, `alt2/`, `alt3/` intentionally not mirrored. Nothing in the original archive needs to be deleted.

Start from [INDEX v8](../INDEX_v8.md), [evidence ledger v11](ARCHIVE_PER_FILE_EVIDENCE_LEDGER_v11.csv), and [checkpoint v2](SESSION_CHECKPOINT_20261014_v2.md). Source-cell physical addressing fixes in prior British work are recorded in `gb_cost_FY2014_22_8520_independent_cell_checks_and_ODS_row_address_QA_v1.md`. Prefer corrected `v2` finance datasets.

## One task = one self-contained round

1. **Before action**: verify latest Git head and original source presence, size, Git blob SHA; check source-specific prior note. If the exact output artifact already exists and is supported, **audit it** rather than repeat extraction.
2. **Scope limit**: normally **one original file**, exceptionally **two very closely related files**, **one narrowly defined question**. No unrelated countries, financial years, archive formats, or research hypotheses in the same round. Never read all 507 judicial files as a single atomic task.
3. **Evidence boundary**: metadata seen ≠ sheet/page examined ≠ numeric original values checked ≠ upstream URL verified ≠ external bytes hashed ≠ longitudinally comparable. Explicitly retain `unverified`, `partial`, `not_accessible` statuses. Preserve blank/zero distinctions and financial-vintage differences.
4. **Save**: publish **one small new versioned evidence artifact** under `00_catalog/progress/`, with source path, original SHA, observed content, precise sheet/page/physical cell addresses, issuer and URL grade, findings, open questions. Large extraction can use one source CSV plus one small note. Do not overwrite any existing file.
5. **Verify save**: require returned Git commit SHA and re-fetch the new path and verify SHA/content. Only **then** say `DONE`. Never promise a future background continuation; work stops with the tool call and Git commit.
6. **On interruption**: open newest `MICROTASK_*_vN` plan / `progress/` files and compare Git tree. Repeat **at most the in-flight task**, not all earlier completed work. Do not assume an interrupted write succeeded or failed without checking.
7. **Completion report to user (compact)**: `task id → DONE/PARTIAL/BLOCKED`; concrete finding, exact saved path + commit SHA, original integrity check, **one next task ID**. No lengthy discourse unless a material methodological issue is found.

**Source-preservation rule:** no deleting/renaming/moving/overwriting original data, copies, historical catalogues, or older QA versions. Restated official publisher files that were not present in the baseline must be placed in **additional labelled official-source paths**, not represented as existing originals. Never conflate Git SHA-1 with a fresh external SHA-256. The source archive is distinct from cleaned analytic panels.

## Wave 1 task queue (exact source inputs and acceptance criteria in CSV)

[Machine-readable queue, **31 atomic tasks**](MICROTASK_QUEUE_WAVE1_v1.csv). `PRE-000` is done: initial integrity/restore state independently checked. Start **GB-001** (2015/16 missing restatement publisher link), then GB-002 binary capture (if available), GB-003 version differences, but alternate later between UK, Russia, SPACE, and USA so the **whole** archive is not forgotten.

### Recommended rotation (after immediate 2015/16 gap)
**GB-004 → RU-001 → GB-014 → INT-001 → GB-005 → US-001 → GB-020 → RU-003**, then resume numbered pending GB supplement/PDF items. This avoids only perfecting the British branch while leaving court, budget, SPACE and U.S. originals content-unexamined.

## Major waves not yet decomposed

- **UK population:** 189 monthly bulletins → first determine format generations/date/variables, then one or two original bulletins per unit, source-cell anchors and capacity definitions. Staff: 53 originals → one source workbook per task, build institution lineage only after source and sector definitions checked.
- **Russia:** 507 judicial original XLS/PDF → one original report form at a time, gradually build audited form-year/variable register. Budget `fs-22` 49 files, 28 government report files, remaining FSIN and regional controls → one archive/document per task.
- **SPACE:** national facility/capacity documents → one document/country/date per task; distinguish legal maximum/rated/operating/used units, country reporting scope.
- **U.S.:** 2011 Census source codebook, fixed width data and repeated JEET metrics → small original-file or code-family checks, no forced prison-level joins.

### Status ledger conventions
`DONE_THIS_TURN`: complete evidence for preflight read directly. `NEXT`: next actionable item. `PENDING`: not attempted in this wave. `PARTIAL`: some source evidence saved but acceptance not met. `BLOCKED`: external binary/tool unavailable; report what is known. Queue `status_at_creation` is a historical snapshot; **completed results are evidenced by immutable per-task progress files** and future numbered queue snapshots. Do not silently edit older queue status.

**Next single atomic task:** GB-001 — verify the official MoJ FY2015/16 restatement reference and whether this is truly absent in the original local 27-file finance collection. No copying or comparing yet.

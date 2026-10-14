# Post-commit, full archive SHA validation — checkpoint 26 (2026-10-14)

## Result

**PASS: 1,067 / 1,067 expected archived raw-source paths present, all 1,067 Git blob SHAs equal to baseline originals; 0 missing paths, 0 wrong-hash paths.**

- Baseline original Git tree: `373a14b4fe725329c050ca45a8db723d304766e5` (1,124 blobs). The current Git root was independently compared with this baseline: 58/58 original root entries had the **same SHA**, none were removed; only `prison-research-archive/` was added.
- Raw-source copy commit: `0b84d933cac9168e9aa5bd85c834fcd6ad1d3dd3`.
- Full index/provenance commit: `3bb83e1ae4312f8f179a6ed197774fc2080e0943`.
- 57 `alt/`, `alt2/`, `alt3/` project files are deliberately not copied and are still in the original repo (57/57 represented in the inventory).
- The 271 UK source copies previously checked also passed this **independent archive-wide crosswalk validation**, alongside 796 new source copies.

## How it was checked

1. Fetched `00_catalog/source_inventory.csv` with original paths and Git blob SHAs.
2. Retrieved GitHub Git Trees API **recursively** for the seven main archive source-family subtrees. All recursive responses reported `truncated=false`.
3. Constructed the expected source → archival copy path by the explicit mapping documented in `INDEX_v2.md`.
4. For each of 1,124 original files: excluded the 57 separately scoped satellite-project paths; looked up the remaining 1,067 copy paths in the actual remote Git trees; compared the returned blob SHA with the baseline original blob SHA.
5. Result: **1,067 exact matches, 0 mismatches, 0 missing**.

## Audited subtree counts

Counts below include all blobs in the subtree, not only the raw copied originals. UK includes earlier derived CSVs, metadata and thematic second mirror.

| Subtree | Git blobs observed |
|---|---:|
| `01_international/` | 125 |
| `02_uk/` | 577 |
| `03_russia/` | 589 |
| `04_us/` | 29 |
| `70_related_context/` | 39 |
| `80_tools/` | 1 |
| `90_unverified/` | 13 |

Expected raw-source copy counts by source group are in `INDEX_v2.md` and `archive_copy_manifest_v2.csv`. The larger UK subtree count is intentional, because raw copies coexist with derivatives and the separately organized `source_mirror/`.

## Scope and limits

Matching **Git blob SHA-1** proves byte-for-byte identity of the Git-managed original content and the archived copy; it is **not** a recomputed SHA-256 and says nothing about whether statistical definitions and source publication URLs have been checked. Analytical extraction, document-level provenance and variable crosswalks remain separate tasks, explicitly listed in `REMAINING_WORK_v2.md`.

No original source, historical version, or previously created research file was overwritten, moved, deleted or renamed.

# Prison research archive — navigation v2 (14 October 2026)

This is an **add-only preservation and provenance index** for original files from `tqpqr/temp`. Original source paths, older research tables and older catalog versions remain unchanged.

## Main lookup

- [Full inventory and source → copy register](00_catalog/archive_copy_manifest_v2.csv): **1,124 original rows**; for each: exact original path, new path (or excluded), file type and bytes, matching original/copy Git blob SHA-1, interpreted topic and contents, evidence level, identified organization, external URL when recorded and unresolved provenance.
- [What each group contains](00_catalog/COLLECTIONS_AND_EVIDENCE_v2.md): scope, verified content and important compatibility restrictions.
- [Collection counts](00_catalog/archive_collection_rollup_v2.csv) and [Git-exact duplicate originals](00_catalog/original_blob_duplicates_v2.csv).
- [Remaining content-level work](00_catalog/REMAINING_WORK_v2.md) and [copy audit](00_catalog/archive_wide_preservation_checkpoint_25.md).

## Browse organized originals

| New directory | Original directory | Number |
|---|---|---:|
| `01_international/space_archive/original_sources/` | `space-archive/` | 111 |
| `01_international/country_extra/original_sources/` | `extra/` | 14 |
| `02_uk/original_sources/` | `GB/` | 271 |
| `03_russia/judicial_reports/original_sources/` | `sud/` | 507 |
| `03_russia/justice_budget/original_sources/` | `fs-22/` | 49 |
| `03_russia/fsin_statistics/original_sources/` | `fsin/` | 2 |
| `03_russia/government_reports/original_sources/` | `svod/` | 28 |
| `03_russia/crime_statistics/original_sources/` | `data_crimes_stat/` | 3 |
| `04_us/jeet_bjs/original_sources/` | `jeet/` | 20 |
| `04_us/correctional_finance/original_sources/` | `us/` | 9 |
| `70_related_context/ru_socioeconomic/original_sources/` | Root `data_*.xlsx` | 39 |
| `80_tools/original_sources/` | Root `ipt_final.py` | 1 |
| `90_unverified/opaque_pdfs/original_sources/` | `rn1/` | 9 |
| `90_unverified/root_misc/original_sources/` | Four unclassified root files | 4 |

**Result:** 1,067 original research/context/pending files represented with identical Git blob objects; 57 satellite/geology-project files not copied, **but still indexed and preserved in the original folders**. No identical-content variants were discarded.

### What "preserved" does and does not mean

The earlier complete UK 271-file mirror was independently SHA-checked. On 14 October the additional 796 were added by pointing the new Git tree entries to the exact original blob SHA values (commit `0b84d933cac9168e9aa5bd85c834fcd6ad1d3dd3`). That gives byte-identical content without re-encoding the binary files. It **does not prove** source pages, workbook columns or statistical methods were exhaustively checked. Derived `02_uk/*.csv` tables remain separate from the original `02_uk/original_sources/` documents.

A Git blob SHA-1 is not a conventional file SHA-256; reported SPACE manifest SHA-256 values and upstream URLs are **preserved metadata, not freshly independently verified**.

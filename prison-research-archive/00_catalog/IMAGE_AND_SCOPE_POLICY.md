# Image and topical scope policy

Add-only decision log. This note does not change, delete, move or overwrite any pre-existing files.

## Scope decision

- Exclude the satellite imagery in original `alt/`, `alt2/`, and `alt3/` from the prison research archive's **copied collections**. These belong to a separate mineral-prospecting project.
- Do **not** exclude images as a file type. Retain prison-related scans, maps, photographed statistical tables, figures, and other visual evidence.
- Preserve every original path in the baseline metadata inventory, including out-of-scope materials, for audit completeness.
- Classification is based on **content**, not extension or top-level folder alone.
- A figure embedded inside a PDF/DOC is treated as a potential data source; further review is required before cataloguing its variables.
- No original image needs to be deleted or moved.
- Out-of-scope files have scope status `excluded_from_copy`, not `deleted`.

## Baseline checks (Git tree 373a14b4fe725329c050ca45a8db723d304766e5)

There are 57 standalone files with common image extensions:
- `alt/`: 9
- `alt2/`: 29
- `alt3/`: 18
- `space-archive/`: 1

The 56 files under `alt*` are excluded from copying as satellite imagery. One JPG outside these groups (`space-archive/extra/lp/RO_HG_756_2016_Anexa_unitati_subordonate.jpg`) remains **pending content inspection**, not excluded.

Images embedded in PDFs and office documents are *not* counted among the 57 standalone images.

## Two independent classifications

`topic_scope`: `prison_research`, `related_context`, `out_of_scope`, `unreviewed`.

`representation`: `structured_data`, `text`, `scanned_table`, `graph`, `map`, `photograph`, `mixed_document`, `unknown`.

Never imply that merely locating a file or identifying its extension establishes its research contents. 

# Content review — pass 01 (add-only)

Baseline tree: `373a14b4fe725329c050ca45a8db723d304766e5`

## Materials actually read
- `space-archive/README.md`: explicitly identifies SPACE I prison statistics, SPACE II probation, key findings, annual source manifests and Part F expenditure comparability notes. These are **statements in the repository's README**, not independent methodological verification.
- `space-archive/manifest.csv`: CSV headers `category,year,file,size_bytes,size_mb,pages,sha256,source_url`; includes supplied source URLs and SHA-256 strings.
- `space-archive/manifest-space-ii.csv`: headers `year,file,size_bytes,size_mb,pages,sha256,source_url`.
- `space-archive/extra/wb/Metadata_Indicator_API_PA.NUS.PPP_DS2_en_csv_v2_6254.csv`: identifies `PA.NUS.PPP` as GDP purchasing-power parity conversion factor (LCU per international dollar).
- `space-archive/extra/stp8/LaikomuAsmenuStatistika.csv`: has `laikotarpis` (time period), `ist_pav` (institution), `asm_sk` (persons count), and counts by custody / sex / age / other classes. Sample rows show monthly dates and institution names. Precise coverage/definitions require fuller parsing.
- `fs-22/2016.md`: accessible but empty.
- `ipt_final.py`: Python code uses OpenCV, PyMuPDF and Tesseract for detecting/extracting ruled tables and OCR; categorize as processing code, not observational data.

## High-value collection discoveries (path-based, unverified contents)
- `GB/`: 271 files, including a sequence of prison population bulletins and institution-level cost-per-prisoner/prison-place tables.
- `sud/`: 507 files, reports organized into year subdirectories.
- `fs-22/`: 49 files; budget execution .7z archives, justice programme and annual reports.
- `space-archive/`: 111 files, including official country-level prison capacity and facility lists used in earlier research.
- `fsin/`: 2 files, XLSX + matching description PDF.
- `alt/`, `alt2/`, `alt3/`: 57 files in total, including **56 standalone images**. All are outside the user-defined prison research scope, and will not be copied.

## Methodological cautions
- Git blob SHA-1 is **not** SHA-256. Existing SPACE manifest SHA-256 values have been read as metadata but not recomputed against actual PDFs.
- Filename-derived categories must not be mistaken for validated data coverage or source provenance.
- Similar institutional indicators may use different definitions (rated capacity, operational capacity, accommodation places, staffing ceiling vs actual staffing); keep definitions at variable level.
- Binary image inspection via the connected GitHub text-file interface failed for `space-archive/extra/lp/RO_HG_756_2016_Anexa_unitati_subordonate.jpg`; keep it pending review rather than excluding it.
- No content binaries have been copied into the new archive.

## Outputs
- `00_catalog/source_inventory.csv`: 1124 original files, Git object identities.
- `00_catalog/topic_scope_first_pass.csv`: initial topic/scope and copy-action labels, most marked as filename-only and requiring content review.
- This review note.

## Priority queue
1. Validate the SPACE manifests against tracked report paths and check rows/coverage.
2. Inventory spreadsheet sheet names and variable headers; separate original source tables from derived exports.
3. Build an institution-level provenance crosswalk for official national capacity sources.
4. Inspect `GB/` cost and population series, and Russian `sud/` series.
5. Once copy destinations are stable, make additive verified copies only.

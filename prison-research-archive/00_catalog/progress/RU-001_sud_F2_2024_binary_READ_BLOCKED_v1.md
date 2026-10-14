# RU-001 — BLOCKED: F2-2024 legacy XLS original cannot be decoded via current source connector

## Exact original
- Repository `tqpqr/temp`, main, **original file**: `sud/2024 год/F2-2024.xls`
- Preserved byte-identical classified mirror: `prison-research-archive/03_russia/judicial_reports/original_sources/2024 год/F2-2024.xls`
- **Git original blob SHA-1: `061f154ecc737c69a21e9a3bac3793fef45efcc5`; Git recorded byte length: 1,174,016.** Original and mirror Git tree entries have exactly the same SHA and byte size. This is verified storage/preservation, **not independently downloaded-byte content verification**.
- Annual reporting-year folder: `2024 год`; date window `2024-01-01` to `2024-12-31` is **folder classification**, not independently confirmed by opening the form. Form token `F2` is also filename evidence only.
- [Existing source register v5](../sud_form_file_register_v5.csv) correctly flags this exact file `READ_BLOCKED_LIMIT`, `source_contents_checked=NO`, `2024 title not decoded - source interface blocked`.

## Attempts and observed outcome
1. Direct GitHub `fetch_file` with `encoding=base64` for `sud/2024 год/F2-2024.xls`: file metadata and exact original SHA returned, but **empty content string**.
2. Repeated with categorized mirror exact path: metadata and original SHA returned, **empty content string**.
3. GitHub Git blob direct fetch (`/git/blobs/061f... `): connector rejects binary (HTTP 400: `GitHub Fetch only accepts UTF-8 text`).
4. Independent raw GitHub HTTPS request in current sandbox could not resolve `raw.githubusercontent.com` (network unavailable in runtime). Thus there are no real bytes to pass to an OLE2/BIFF reader.

## What is verified and what is not
**Verified**: original and mirror paths, byte size from Git tree, SHA-1 identity, folder's nominal 2024 annual form token. **NOT verified**: actual BIFF version, worksheet names, title, sheet count, exact tabular indicators, column definitions, numerical cells, period text inside the file, primary issuer URL.

**Do not upgrade the matching unified indicator-period registry line** from `file_presence_form_by_period_NOT_indicators` to a confirmed F2 numeric-indicator series. File existence does not identify the statistical fields.

## Resume only if bytes can be obtained
A byte-exact uploaded original XLS or an authorized byte-preserving retrieval path should allow XLS OLE parsing (e.g. `xlrd` / LibreOffice programmatic reader), preserving original SHA and source sheet+cell addresses. Compare obtained source content's Git blob SHA with `061f154ecc737c69a21e9a3bac3793fef45efcc5` before accepting it as the original.

**RU-001: BLOCKED**, not DONE. No original or mirrored source touched, no fabricated source-cell records. Continue next independent **GB-005**: `GB/costs-per-prison-place-per-prisoner-2016-2017-supplementary-information.xlsx`.

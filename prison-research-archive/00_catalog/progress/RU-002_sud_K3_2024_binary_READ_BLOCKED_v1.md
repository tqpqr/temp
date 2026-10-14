# RU-002 — BLOCKED: K3-2024 legacy XLS binary could not be decoded

**Microtask attempted and documented, but source content remains UNINSPECTED.** Do not label numeric source, indicators, workbook title or sheet layout as verified.

## Exact original and mirror (verified GitHub)
- Original: `sud/2024 год/K3-2024.xls` (repo `tqpqr/temp`, default branch).
- Add-only pre-existing archive mirror: `prison-research-archive/03_russia/judicial_reports/original_sources/2024 год/K3-2024.xls`.
- Both have **identical Git blob SHA-1** `f8ba40bf800be6733818f93fab28bb829cb2f5b9`.
- Recorded GitHub directory byte count **1,057,792** (verified directly from authenticated GitHub Contents directory listing and existing `sud_form_file_register_v5.csv`).
- Source register v5 correctly records `content_status_v5=READ_BLOCKED_LIMIT`, `source_contents_checked=NO`, and blank publisher-exact sheet/title fields.
- Folder `2024 год` and token `K3` are **only file-path evidence**; annual 2024 scope is **not independently verified by reading workbook cells**.

## Byte retrieval attempts
1. `mcp__GitHub__fetch_file` at exact original with `encoding=base64`: valid file metadata and original SHA returned, but `content` is **empty string**.
2. The categorized mirror via same action also returned metadata with same SHA, but **zero content bytes**.
3. `mcp__GitHub__fetch_blob` original SHA fails to decode original non-UTF8 bytes (UnicodeDecodeError, byte 0xD0 at position 0).
4. Generic GitHub REST `fetch` for exact content URL and Git blob URL rejected responses as `GitHub Fetch only accepts UTF-8 text`.
5. Independent runtime HTTPS fetch of GitHub raw and API binary failed name resolution for `raw.githubusercontent.com` / `github.com` / `api.github.com`.
6. No exact binary backing file has been mounted into the runtime. A Library search for the named K3 file yielded no matching library file, only a different research master spreadsheet.

**Consequence:** impossible to verify OLE/BIFF format, sheet names/counts, number/date values, headings, whether formulas exist, blanks vs zeros, geographic breakdown, actual reporting period, and source calculations. Git blob SHA-1 is a repository object identity, not an independently observed publisher-file SHA-256.

## External provenance (collection only; not the individual XLS)
- Existing source register links the wider Судебный департамент archives to `https://tochno.st/datasets/suddep_archive`; current live dataset page `https://dev.tochno.st/datasets/suddep_archive` independently describes an official judicial reporting archive. **This does NOT establish any specific field, form title or numbers inside K3-2024.xls**, nor binary identity against that publisher.
- No numeric indicator-period registry additions and no methodology break created from absent content. Original and mirror preserved.

## Restart protocol
Obtain **actual bytes** of the exact original via authorized byte-preserving channel; check `git blob SHA-1 f8ba40bf800be6733818f93fab28bb829cb2f5b9` against obtained bytes and validate OLE/BIFF container. Extract sheet/cell values with reader supporting old XLS. Only then populate verified title, indicators, 2024 reporting period and provenance. **Until then RU-002 BLOCKED, not DONE.**

RU-001 F2 similarly blocked; source-specific attempt and SHA are different. RU-003 original budget 7z archive can be inspected independently; do not confuse K3 contents with neighboring forms.

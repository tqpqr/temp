# RU-003 — BLOCKED: FY2025 draft expenditure 7z archive, entries not decoded

**Status BLOCKED_BINARY_READ, not DONE.** One exact original targeted: `fs-22/2025 ПрФЗ.Прил_2_Расходы.7z` in GitHub repo `tqpqr/temp` (default branch).

## Verified file metadata
- Exact Git blob SHA-1 `7bb55f5a448c3498ff946f55e538a82ec051d26c`.
- Original byte count **11,653,826**, returned by GitHub Contents directory listing at `fs-22`. GitHub `fetch_file(encoding="base64")` returns valid SHA but empty original binary content in current connector.
- Independent container HTTPS GitHub/raw requests blocked by name resolution. Byte-exact 7z data not loaded into a 7z decoder.
- Archive name suggests `2025 ПрФЗ` (draft federal law, expenditure appendix) **by filename only**; contents, individual fiscal classifications, tab names, fiscal periods, and appropriations/actual spending are **NOT INSPECTED**.

## Required task: list internal archive files
No entry names, counts, file sizes, encryption status, nested folder structure, encoding, and original file bytes can be verified without downloading the archive. Do NOT populate the intended `GB`/RU indicator registry or claim an entry-level CSV has been created.

## Resume checklist
Obtain byte-identical 7z through a tool supporting full binary download (or user-supplied original); verify reconstructed Git blob SHA-1 against `7bb55f5a448c3498ff946f55e538a82ec051d26c`; extract a read-only complete 7z file list with path, uncompressed size, CRC if present, and encryption/damaged-entry status. Only after that classify nested source pages. Note draft budget appropriations **cannot** be equated to actual FSIN spending.

Original file preserved unmodified. Next independent dataset task: `RU-004 fsin/data_fsin_info_103_v20240627.xlsx`, which **does** have readable base64 bytes through the connector.

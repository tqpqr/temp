# GB-002 — BLOCKED (2026-10-14): FY2015/16 restated official XLSX not yet captured

## Scope
Obtain *actual bytes* of the UK Ministry of Justice's FY2015/16 restated prison establishment accounting XLSX, verify ZIP/Excel integrity and hashes, store the original binary as a **new additional official-source** item, leaving all original research data and previous archive copies untouched.

## Official source verified from publisher
- Official release: https://www.gov.uk/government/statistics/prison-performance-statistics-2016-to-2017
- Publisher: UK Ministry of Justice; release date **26 October 2017**.
- Specifically listed attachment: **Costs per prison place and cost per prisoner by individual prison establishment 2015 to 2016: restated tables** (the publisher labels it Excel, ~92 KB).
- Source URL: https://assets.publishing.service.gov.uk/media/5a82f0f140f0b62305b9523d/costs-per-prison-place-per-prisoner-by-individual-prison-2015-2016-restated-tables.xlsx
- The government source page currently resolves. The linked XLSX URL is listed on that page; **its actual file content was not downloaded**.

## Attempts / observed limits
1. The web reader tried the direct government XLSX URL and clicked the actual official release attachment. Both report *unsupported content type application/vnd.openxmlformats-officedocument.spreadsheetml.sheet*. This indicates a viewer restriction, not file failure.
2. The separate binary-download tool returned `download failed` for the exact publisher URL.
3. A direct runtime HTTP request using `requests` failed name resolution for `assets.publishing.service.gov.uk` (restricted network in computation sandbox).
4. The connected GitHub API **supports byte-exact binary upload via `create_blob(content, encoding="base64")` followed by new-tree/commit/ref**, but this is immaterial until the true publisher XLSX bytes are retrievable.

## Audit state
`official_document_listed=YES`, `source_url_verified_as_govuk_attachment=YES`, `http_bytes_downloaded=NO`, `external_sha256=NULL`, `git_blob_sha=NULL`, `xlsx_validated=NO`, `new_repo_binary_uploaded=NO`. **No claim that an official file has been archived, and no fabricated hash.**

Local baseline initial workbook: `GB/costs-per-place-cost-per-prisoner-individual-prison-establishment-2015-16_tables.xlsx`; it is **not** the restated attachment.

## Resume trigger
If file becomes accessible via an allowed byte-preserving retrieval channel (e.g. a locally uploaded publisher XLSX), compute SHA-256 and SHA-1 Git blob from actual downloaded bytes and compare against newly persisted bytes, then create versioned progress `GB-002_*_v2.md`. Do not overwrite this blocked-status record.

**Dependent GB-003 remains blocked (cannot compare restatement without publisher binary). Next independent queue task: GB-004**, one source-specific FY2015/16 supplementary methodology workbook.

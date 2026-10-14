# RU-004 — direct original XLSX audit: FSIN one indicator and duplicate code-year vintages

**Status DONE for the expressly scoped representative-indicator original-source audit.** This is NOT a canonical FSIN time series or complete review of all 301 codes.

## Source identity and access
- Original repository binary: `fsin/data_fsin_info_103_v20240627.xlsx`, Git blob SHA-1 **`ebc0c08de7a7e4279e6035637dea6df0ff519c4c`**. Exact `fetch_file(encoding=base64)` returned the full bytes with ZIP PK magic; base64 whitespace removed before decoding. Decoded ZIP file: **384,430 bytes**. No claim of independent publisher-hosted binary SHA-256 identity.
- Original ZIP/XLSX was parsed from its actual workbook.xml, sharedStrings.xml, and worksheet XML via local read-only JavaScript ZIP/DEFLATE parsing of connector-fetched bytes (no edits to workbook).
- Original Excel sheet **`data_clear`**, one real sheet. The actual physical first row fields `data_clear!A1:K1`: `indicator_code`, `indicator_category`, `main_level`, `indicator_name`, `year`, `indicator_value`, `rounded`, `data_date`, `data_date_t`, `data_source`, `data_source_2`.
- Parsed **7,228** physically populated rows including the header (**7,227 data rows**) and **857 shared-string dictionary entries**.
- Distinct indicator codes **301**. Unique code/year pairs **5,149**. **1,079** pairs occur multiple times; **619** of these have >1 distinct original printed value, **328** have >1 `data_date_t`, **1,059** have >1 `data_source` string. These are source-duplicate flags, NOT 619 proven mistakes; changes could reflect publication dates, rounding, source definitions or revisions.
- `rounded` field occurrences: string `0`: **6,174**, string `1`: **1,050**, absent/empty: **3**. Preserve blanks as missing, not 0. Original `data_source` labels observed: `short`, `od`, `od,stat`, `stat`, `fsin_report`, `fsin_report2`, `fsin_report,short`, `concept-2020`, `rosstat`. Codes/labels are **not yet full authenticated original issuer URLs**.

## Verified case — indicator code Y808000001

Header and data at original source `data_clear!A2:K...`, physical original-row provenance in [121-row original-cell extract](RU-004_fsin_Y808000001_original_cells_v1.csv).

- Original name `indicator_category=заключенные и осужденные`; `main_level=осужденных, всего`; `indicator_name=в учреждениях УИС, всего`. Interpret with publisher meanings; do not silently equate to a particular stock measure or person-days.
- Fiscal/calendar label **2005** has at least three original records:
  - **row 3 (A3:K3)**: `year=2005`, `indicator_value=825558`, `rounded=0`, `data_date_t=2005_12_31`, `data_source=od`; original Excel `data_date` is numeric serial `38717`.
  - **row 4 (A4:K4)**: `year=2005`, `indicator_value=828900`, `rounded=1`, `data_date_t=2006_02_01`, `data_source=short`; date serial `38749`.
  - **row 5339 (A5339:K5339)**: `year=2005`, `indicator_value=823400`, `rounded=1`, `data_date_t=2005_12_31`, `data_source=rosstat`; `data_date` is source text `31.12.2005`.
- Thus **code+year** is not unique; even **code+year+normalized date** can have differing printed values (825558 vs 823400 on 31 Dec 2005), source and rounded flag.
- One indicator has **121 source rows** in workbook, retained in the auxiliary CSV, with no deduplication, imputation or source selection.

## Specific research methodological decision — MB-034

The user-level analytical grain cannot be only `indicator_code,year`. Future normalized data should at minimum include `original_workbook_sha1,original_sheet,original_row,indicator_code,year,indicator_value,rounded,data_date_t,data_source,data_source_2` and actual source caption/category. A unique `observation_id` derived from original physical row is essential. Matching date and source label does not on its own establish identical universe or methodology; external primary-issuer documentation is required before choosing a preferred series.

This is **new MB-034**, created in `METHODOLOGICAL_BREAKS_AND_ANOMALIES_v17.csv`; no unexplained spreadsheet entries are silently dropped. This is a source-vintage/duplicate-key issue, not evidence of a particular FSIN statistical error.

## Scope of completion and next research step

RU-004 original **one-indicator** source audit is complete; **full 301-indicator year/source dictionary and source URL verification remains a follow-on opportunity**. No new entries were added to the main indicator-period registry v16 because duplicates and source semantics need a controlled design. The original XLSX and all prior archive versions remained unchanged.

Previous RU-002 `sud/2024 год/K3-2024.xls` and RU-003 2025 budget 7z are genuinely binary-access **BLOCKED** despite verified path/SHA; do not confuse with successful decoding of the different zipped XLSX source.

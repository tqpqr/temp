# Russian statistical collections — verified source recovery (2026-10-14)

Three previously incomplete collection-level upstream citations have been recovered:

| Local family | Aggregator dataset page | Underlying issuer | Important limitation |
|---|---|---|---|
| `fsin/` | https://tochno.st/datasets/fsin_info | FSIN and Rosstat, including preserved historical sources | Aggregated/reconciled by «Если быть точным»; not an untouched single official spreadsheet |
| `data_crimes_stat/` | https://tochno.st/datasets/crime | Prosecutor-General's legal statistics portal | Regional *registered/investigated crimes*, not convicted persons or prison population |
| `sud/` | https://tochno.st/datasets/suddep_archive | Court Department / published judicial reporting forms | Court outcomes/convictions, not prison stock |

All three dataset identifiers and version dates coincide with the corresponding local file naming and aggregator pages; this establishes **collection-level attribution**, not downloaded-byte identity with the external provider.

## Judicial form inventory

- Original `sud/` family: **507** files = **506 legacy XLS tables + 1 description PDF**.
- **25 directory categories**: 20 full calendar years 2005–2024, 3 half-year folders 2023–2025, one multiyear sentencing summary folder (3 XLS), plus the dataset-description PDF.
- Each original XLS filename, reporting window, Git SHA, size and provisional filename form token is in `sud_form_file_register_v3.csv`. Per-folder counts and list of identified filename tokens are in `sud_period_form_matrix_v3.csv`.
- Publisher describes **511 report documents**; current local copy has **506 XLS**. The difference **five** is recorded as open reconciliation, not evidence of specific missing forms.
- For 2025, current local files are only the **first half-year**, not 2025 annual totals. Annual and H1 report files are not interchangeable.
- Form token extraction is **syntactic only**; no judicial XLS data cells or titles were yet parsed.

## FSIN content verified so far

Source `fsin/data_fsin_info_103_v20240627.xlsx` opened as a real ZIP/XLSX and `xl/workbook.xml`, `xl/sharedStrings.xml`, `xl/worksheets/sheet1.xml` parsed, independently of publisher description:

- Worksheet `data_clear`, original range `A1:K7228`; **7227 data rows**, 11 column headings.
- Exactly **300 unique indicator codes** in column A, and categories such as inmates and offenders, staffing, infrastructure, internal crime and human-rights violations.
- Same indicator and nominal year can have multiple observations with different publication/date/source labels; therefore **do not deduplicate by code+year** or choose the most recent without justification.
- First actual source row references nominal year **2004** with reporting date `2005_01_01`, even though aggregator describes coverage as 2005–2023. Index must distinguish date-of-observation and year-of-report.

## Statistical boundaries

`FSIN_103` is national system **stocks/infrastructure/personnel**; `CRIME_107` is registered crimes **event flow** by region; `COURT_165` is court adjudication / sentencing **event flow** by reporting period. Join only with explicit definitions and time alignment.

All new catalogues are additive. Original source files, archived mirrors, and preceding tables are untouched.

# Nested-content audit — pass 02

Baseline: Git tree `373a14b4fe725329c050ca45a8db723d304766e5`.

## Directly inspected source contents

1. `space-archive/extra/stp8/Italy_Detenuti_capienze_per_istituto_31-01-2023.html`
   - Internal attribution: Italian Ministry of Justice / DAP, with source URL.
   - Caption: *Detenuti presenti e capienza regolamentare degli istituti penitenziari*, 31 January 2023.
   - Columns: region, province abbreviation, institution, institution type, **regulatory capacity**, present detainees total, women and foreign detainees.
   - Note: regulatory capacity must not be treated as operational capacity without checking methodology.
2. `space-archive/extra/wb/ICP2021_PPP_GovFinalConsumption_9270000.csv`
   - Indicator `9270000` is **general government final consumption expenditure PPP**, LCU per USD.
   - Column headings include 2017–2023; example rows have blank 2022–2023 values, so actual coverage must be measured separately.
   - Distinct from GDP PPP (`PA.NUS.PPP`) already catalogued.
3. `us/raw data/2011/11state35.txt`
   - A sampled record has fixed-width machine-coded fields; not interpretable as named variables without `public-use-file-layout.xlsx`.
4. `us/raw data/jail/local_govt_correction_expenditure_2012_2017_2022.csv`
   - Values are nominal USD thousands, local-government *correction* expenditure for 2012/2017/2022; not directly state-prison operating budgets.
5. Original SPACE I & II manifest CSV files were parsed as path inventories. 34 listed records in `manifest.csv` refer to existing paths; `manifest-space-ii.csv` contains 20 rows, including a `../space-i/` relative-path entry which resolves to an existing SPACE I report. This is an intentional-looking cross-category reference, not automatically a missing file.

## Nested directory findings

- `GB/workforce/`: 53 standalone workforce source files, separate from `GB/` population and prison cost tables.
- `space-archive/extra/stp8/`: 19 source files, heterogeneous country-specific prison statistics and institutional evidence.
- `space-archive/extra/lp/`: 19 standalone files; country lists, plans, regulations and annual reports, pending content-level inspection.
- `jeet/2016–2021/`: 20 `national_map` workbook variants; filenames alone do not establish meaning.
- `svod/2017/`: 22 opaque-named PDFs, pending inspection.

## Binary workbook inspection boundary

The connected GitHub tool can return XLSX/ODS **base64 source content**, but it does not decode workbook ZIP structures or return internal worksheet headings. Three exemplar binaries (`GB/workforce/...jun-2025...ods`, `jeet/2018/national_map exp.xlsx`, `fsin/data_fsin_info_103_v20240627.xlsx`) were confirmed downloadable through the connection, but their internal sheets have **not** been read. Do not invent worksheet column names or assert verified workbook content.

## Add-only outputs

- `00_catalog/nested_directory_audit_v1.csv` — 58 directories containing files; independently classified.
- `00_catalog/variable_dictionary_v1.csv` — initial variable dictionary.
- `00_catalog/variable_dictionary_v2_additions.csv` — 12 additional entries, with evidence labels.
- This note.

Nothing original was changed or removed. No binary bulk copy has yet been performed.

# Russian FSIN source separation, stage1, 2026-10-16

Continues [RU-004](RU-004_fsin_one_indicator_provenance_v1.md). Original source remains unchanged. Complete XML extraction preserves all 7227 rows and all11 original field literals; each observation ID combines Git blob SHA, sheet and original row. `data_date` retains raw numeric Excel serial or original text. `data_date_t` remains the supplied label; its meaning as observation/publication date is not inferred.

## Findings

There are **300 distinct indicator codes**, independently counted using XLSX XML and openpyxl. The earlier statement of301 codes was incorrect. There are302 distinct code/name pairs: codes Y808000077 and Y808000298 each have two indicator captions. Retain separate captions; this is not a reason to delete rows or merge meanings.

Key diagnostics (groups with different source value literals): code+year619; adding supplied date472; adding both source fields74; adding rounded flag16. These are nested-key diagnostics, not a causal decomposition of errors. Adding category, main level and indicator caption does not resolve the last16 groups. Each row remains retained.

Fourteen remaining groups concern year2020, source od, supplied date2020_07_17; two concern Rosstat2012 (Y808000050:2293/2289; Y808000074:2180/2176). These require original-document verification. Repeated values within a date label are not proven revisions or errors. Do not select maximum, last row, or average.

## Outputs and use

- RU-MB034_all_source_rows_v1.csv.gz: complete lossless CSV, gzip compressed. Read with pandas.read_csv(path, compression='gzip', dtype=str, keep_default_na=False); raw source dates are deliberately not converted.
- RU-MB034_key_diagnostics_v1.json: source hashes, CSV checksum, group diagnostics.
- RU-MB034_same_key_conflicts_v1.csv:16 residual groups and physical source-cell anchors.
- Registry v36 upgrades302 existing code/name records with exact year lists and source-row coverage; no record deleted or duplicated. Other registry records unchanged. Units and original issuer URLs remain unverified.
- Methodology v40 supplements MB-034 and corrects its code count. Previous versions retained unchanged.

Next: read the dataset description to distinguish date meanings and resolve source abbreviations, then verify the14 od2020 groups and2 Rosstat2012 groups against primary records. A canonical annual series is not yet produced.

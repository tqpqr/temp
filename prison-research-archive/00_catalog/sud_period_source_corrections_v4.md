# Judicial period and source-document correction — v4 (2026-10-14)

This corrects the filename-derived catalogue v3 **without modifying v3 or the originals**.

## Explicit corrections

- `sud/description_suddep_archive_165_v20260424.pdf` is **source documentation dated April 2026**, **not** an annual judicial report for 2026. In v4 its reporting year is empty and `window_type=documentation`.
- `sud/Состояние судимости/Состояние судимости_2003-2007.xls`, `..._2008-2019.xls` and `..._2020-2024.xls` are **multiyear summary XLS**. Their time coverage comes from the filename's full year interval; they have no single-year form token.
- There are **24 true content subdirectories** of judicial material: 20 full-year folders (2005–2024), three first-half folders (2023, 2024, 2025), and one multiyear-summary folder. The 25th catalogue grouping is the **PDF at the root of `sud/`**, not another physical folder.
- The 2025 archive portion contains **H1 2025 only**, not an annual 2025 report. Full-year and first-half exposure must be kept separate.

## Resulting files

- `sud_form_file_register_v4.csv`: 507 rows, exact source/mirror paths and SHA, year, reporting window, source filename/form code with evidence flag.
- `sud_period_form_matrix_v4.csv`: 25 logical groupings including root metadata (20 FY, 3 H1, 1 multiyear group, 1 documentation).
- These are **path-level verified metadata** only, not a claim that the 506 XLS workbooks were decoded. Official direct download URLs and historical form changes remain to be resolved.

Underlying dataset page: https://tochno.st/datasets/suddep_archive . It describes 511 reports, compared with 506 XLS originals + 1 PDF in this repository. The five-report discrepancy is open.

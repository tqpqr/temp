# Verified workbook inspection — jeet, pass 03

Original data was accessed via the connected GitHub repository and XLSX ZIP members inspected directly (no file edits).

Files read: `jeet/2018/national_map exp.xlsx`, `jeet/2018/national_map empl.xlsx`, `jeet/2018/national_map pay.xlsx`, `jeet/2021/national_map pay.xlsx`.

In these four workbooks, `xl/workbook.xml` directly confirms seven sheet names:
`Expenditures`, `Employees`, `Pay`, `Total Expenditures`, `Monthly Total Employee Pay`, `Total Expenditures per Capita`, `Total Employees`.

In each of the three 2018 workbooks, direct inspection of `xl/worksheets/sheet1.xml` confirms first-row columns:
`State Abbreviation`, `Function`, `Metric & View`, `Measure`, `Population`, `Pay`.

Observed `Function` entry: `Corrections`.

Observed `Metric & View` cells (2018):
- `national_map exp.xlsx`: `Expenditures Per Capita`.
- `national_map empl.xlsx`: `Employees Per 10k Residents`.
- `national_map pay.xlsx`: `Average Pay`.

The 2021 `pay` workbook also contains `Average Pay` in the inspected rows.

Important: `Corrections` is a government function classification, **not** proof of prison-only coverage. The three workbooks each contain sheets with identical names; contents have not yet been fully compared for duplicate values. State/correctional function scope, definitions and denominator need source metadata before cross-study use.

The binary `fsin/data_fsin_info_103_v20240627.xlsx` was successfully accessed, but its worksheet XML was ZIP-DEFLATE compressed; the method used for the above four workbooks cannot decode its cell contents. It therefore remains `binary_accessed_not_parsed` rather than verified.

All source files remain unchanged. Further inspection pending for the other `jeet` workbooks.

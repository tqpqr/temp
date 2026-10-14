# JEET US state correctional data — complete first-row workbook audit

Source tree: `373a14b4fe725329c050ca45a8db723d304766e5`.

## Verified directly from XLSX internals

All **20** workbooks under `jeet/2016` through `jeet/2021` were opened via GitHub base64 and their uncompressed XLSX ZIP members `xl/workbook.xml` and `xl/worksheets/sheet1.xml` were read.

Each contains seven worksheet tabs:
1. Expenditures
2. Employees
3. Pay
4. Total Expenditures
5. Monthly Total Employee Pay
6. Total Expenditures per Capita
7. Total Employees

The headers in sheet 1 (in directly sampled books): State Abbreviation; Function; Metric & View; Measure; Population; Pay. The first observed state is WY and function is Corrections. First-row indicator values and populations are recorded for all twenty files in `jeet_20_workbooks_verified_index.csv`.

## Verified filename-to-metric classification

- Expenditures Per Capita: 2016 national_map.xlsx; 2017 national_map (2).xlsx; 2018 national_map (3).xlsx and national_map exp.xlsx; 2019 national_map exp.xlsx; 2020 national_map exp.xlsx; 2021 national_map exp1.xlsx.
- Employees Per 10k Residents: 2016 national_map (2).xlsx; 2017 national_map.xlsx; 2018 national_map empl.xlsx and national_map.xlsx; 2019 national_map empl.xlsx; 2020 national_map.xlsx; 2021 national_map empl.xlsx.
- Average Pay: 2016 national_map (1).xlsx; 2017 national_map (1).xlsx; 2018 national_map pay.xlsx; 2019 national_map pay.xlsx; 2020 national_map pay.xlsx; 2021 national_map pay.xlsx.

These counts cover 7 expenditure files, 7 employment files, and 6 pay files; the 2018 expenditure and employment sets each contain an additional workbook, not yet proven to be byte-identical or value-identical beyond the checked sample.

## Further quality questions (not assumed answers)

- 2016 and 2017 `Average Pay` first-row values match exactly (3865.787018255578), despite differing first-row population entries. This may be legitimate or a copied calculation: inspect formula/data origin before longitudinal analysis.
- The two 2018 Expenditures Per Capita and two Employees Per 10k workbooks match on their tested first-row values; full-file duplication is **not verified**.
- Seven tabs have the same names across workbooks, but sheet-level content equivalence is **not verified**.
- Units, government sector coverage, payroll period, headcount versus FTE, and corrections functional classifications must be checked against primary documentation.
- There are no grounds yet for treating these as institution-level prison data.

## Inspection boundaries

Only sheet names, first-row headers (spot-checked) and first data row were read for each workbook. **Do not label all sheets/all rows content-verified.** The future next stage is worksheet-wide extraction and provenance checking.

## Preservation

Only new catalogue files have been created. No source file was moved, deleted, replaced or altered.

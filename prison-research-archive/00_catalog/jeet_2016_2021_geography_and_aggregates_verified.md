# US JEET 2016–2021: geographic granularity and aggregate worksheet verification

Verification method: opened one representative XLSX workbook per filename year using the connected GitHub integration and parsed all seven worksheet XML members. Original sources untouched. Baseline tree: `373a14b4fe725329c050ca45a8db723d304766e5`.

## Year coverage (directly checked)

| Folder year | Representative source | State records per sheet 1–3 | Distinct states / DC | Function |
|---|---|---:|---:|---|
| 2016 | jeet/2016/national_map.xlsx | 51 | 50 states + DC | Corrections |
| 2017 | jeet/2017/national_map.xlsx | 51 | 50 states + DC | Corrections |
| 2018 | jeet/2018/national_map exp.xlsx | 51 | 50 states + DC | Corrections |
| 2019 | jeet/2019/national_map exp.xlsx | 51 | 50 states + DC | Corrections |
| 2020 | jeet/2020/national_map exp.xlsx | 51 | 50 states + DC | Corrections |
| 2021 | jeet/2021/national_map exp1.xlsx | 51 | 50 states + DC | Corrections |

The inspected sheets 1–3 contain exactly 52 XML rows (header + 51 territory records), without missing state codes or repeated state codes. Identical geographical coverage across these six representative books is verified. This does not prove the entire contents of all 20 workbooks are duplicates.

## Aggregate values observed in sheets 4–7

| Year | Total Expenditures (raw number) | Monthly Total Employee Pay (raw) | Total Expenditures per Capita (raw) | Total Employees (raw) |
|---|---:|---:|---:|---:|
| 2016 | 77884697000 | 4290.5129068035785 | 241.17291392305026 | 714102 |
| 2017 | 79286733000 | 4290.5129068035785 | 243.97003400203602 | 714102 |
| 2018 | 81499820000 | 4567.510983094767 | 249.47333384511703 | 716227 |
| 2019 | 82516604000 | 4693.303572152964 | 251.391432834857 | 715687 |
| 2020 | 86036620000 | 4925.437723615326 | 259.56476097738096 | 713996 |
| 2021 | 86905855000 | 5046.056531337679 | 261.7260133886815 | 688982 |

These are the *literal stored values*, not externally validated national statistics. Particularly, identical 2016/2017 total employee count and monthly employee pay values should be checked with the data's original source methodology. Do not assign unverified units to expenditure/payroll fields.

## Dictionary implication

Observation grain for worksheets 1–3: one record per US state or DC × folder year × worksheet indicator. Summary sheets 4–7: single aggregate records, not states.

**Important:** `Corrections` is a functional public-finance category; prison-only coverage, correctional employees' definitions, payroll time basis, and whether expenditure is state-only or broader have not yet been independently confirmed.

No original file modified. This note is a new addition.

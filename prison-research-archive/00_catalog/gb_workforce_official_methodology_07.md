# GB workforce — primary methodology and scope crosswalk (audit 07)

Baseline repository tree: `373a14b4fe725329c050ca45a8db723d304766e5`.

This is an **additive official-source methodology supplement**, not a claim that all 53 source workbook cell tables have been parsed. The ZIP-compressed XLSX/ODS tables remain pending direct worksheet parsing.

## Official source pages
- June 2025 HMPPS quarterly bulletin: https://www.gov.uk/government/statistics/hm-prison-and-probation-service-workforce-quarterly-june-2025
- June 2025 HTML with statistical breakdown: https://www.gov.uk/government/statistics/hm-prison-and-probation-service-workforce-quarterly-june-2025/hm-prison-and-probation-service-workforce-quarterly-june-2025
- Workforce statistics guide: https://www.gov.uk/government/statistics/hm-prison-probation-service-workforce-quarterly-june-2026/workforce-statistics-guide
- June 2026 release: https://www.gov.uk/government/statistics/hm-prison-probation-service-workforce-quarterly-june-2026

## Scope to keep separately in the dictionary
- `Public Sector Prisons (PSP)`: personnel in state/public-sector prisons.
- `Youth Custody Service (YCS)`: separate youth custody institutions.
- `Probation Service`: non-prison probation employees; do not group with prison staff.
- `HQ and Frontline Support`: administrative/frontline support units.
- `HMPPS Total`: sum/agency scope; not equivalent to prison staffing.
- `Operational prison staff` versus `non-operational prison staff` must be separated.
- `FTE` versus `headcount` must be preserved as separate measures.
- Official guide describes possible publication detail by individual prison establishment, prison region, function, grade, service length and probation delivery unit. Verify which breakdowns appear in each archived workbook.

## 30 June 2025 official example (NOT values extracted from archive ODS)
Overall HMPPS: 64,561 FTE;
PSP: 36,627 FTE;
Probation: 20,823 FTE;
HQ + Frontline Support: 5,771 FTE;
YCS: 1,339 FTE.
These published rounded components can differ by 1 FTE on summation.

## Structural breaks
- NOMS replaced by HMPPS on 1 April 2017.
- June 2021 Probation Service absorbed over 7,000 former private-sector CRC staff; a jump in public employment is not necessarily an increase in total service-sector employment.

## Research cautions
- Published data concern **England and Wales**, not all UK prison systems.
- Privately-operated prison staff are not necessarily included in the directly-employed HMPPS workforce. This must be considered before calculating staffing-to-total-prison-population ratios.
- Publication vintage, revised definitions and time series need crosswalks.
- Do not conflate institutional staff counts, staffing targets, aggregate HMPPS staffing, or payroll.
- Archive 53-file metadata inventory: `00_catalog/gb_workforce_53_file_binary_inventory.csv`.
- The user requires original repository preservation: **no deletion, modification, overwriting, renaming or moving originals**.

Status: `external_official_methodology_verified; archived_workbook_values_pending_parsing`.

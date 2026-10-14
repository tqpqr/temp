# GB workforce 2021–2025: initial official-source YCS classification overlay

This is an **add-only overlay** for `02_uk/gb_workforce_2021_2025_institution_long_panel_v1.csv`; it does not alter any original or harmonized data.

Overlay file: `02_uk/gb_workforce_2021_2025_ycs_status_overlay_v1.csv` (536 institution/HQ-year rows; original operational and grand FTE values included for audit).

## Confirmed statuses and caveats
- `Werrington`, `Wetherby`: named **public Youth Custody Service YOIs** in official HMPPS sources. Exclude from a strictly adult prison sample.
- `Feltham`: **mixed** Feltham A youth + Feltham B over-18 estate, but the workforce table has one row. Requires splitting or exclusion before adult-only FTE estimates.
- `Cookham Wood`: official parliamentary statement says it **closed as a YOI in August 2024**. Hence 2021–June 2024 YOI status and 2025 after-closure status must be separated; presence in 2025 workforce rows does not establish operating role.
- `HMPPS HQ` and `Area Services` or `Frontline Support`: administrative, not prison institution rows.
- All **other** 506 year-rows: marked `provisional_adult_or_other`. They are **NOT yet individually verified** as adult-only institutions. Some may be specialist or mixed. Do not call 506 a validated adult sample count.

## Official methodological evidence
- https://www.gov.uk/government/statistics/hm-prison-and-probation-service-workforce-quarterly-september-2025/workforce-statistics-guide
- https://prisonandprobationjobs.gov.uk/about-hmpps/youth-custody-service/
- https://www.gov.uk/guidance/feltham-yoi
- https://lordsbusiness.parliament.uk/ItemOfBusiness?businessPaperDate=2025-11-27&itemOfBusinessId=163210&sectionId=50

## Coverage
- 536 total year-rows
- 10 administrative rows
- 10 Werrington/Wetherby youth year-rows
- 5 mixed Feltham year-rows
- 5 Cookham Wood year-rows (status transition)
- 506 provisionally unspecified year-rows

Status is time-dependent and classification references originate in external official sources; it is not a recovered classification column from original ODS.

The overlay is for sample screening; full establishment-by-establishment validation, ownership transfer, closures and institution identity links remain unfinished.

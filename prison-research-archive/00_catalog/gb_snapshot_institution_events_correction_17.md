# UK HMPPS institutional events: snapshot-date correction, pass 17

This is an **add-only correction overlay**, not a revision of original source files or previously generated classification datasets.

Machine-readable dated events: `02_uk/gb_institution_status_change_events_v1.csv`.

## Corrections to prior year-level descriptions
- **Cookham Wood June 2024:** Do **not** infer youth custody at 2024-06-30 merely because FY 2023/24 appendices and the historic institution name said YOI. The Ministry of Justice announced re-role on 2024-03-21; government YCS annex says the last child transferred out **by the end of May 2024**. Exact date of receiving first adult prisoners and final organizational transfer still requires separate confirmation. Label June 2024 as `post_youth_exit_adult_transition`, not simply `YCS_youth`. By June 2025, adult status is supported by official current prison guidance.
- **Morton Hall June 2021:** Immigration Removal Centre until **2021-07-23**, reopened in HMP category C administrative status on **2021-07-24**; admitted prisoners starting in **December 2021**. Classify 2021-06-30 as `immigration_removal_centre`, not adult-prison.
- **Lowdham Grange:** Temporary public sector step-in management began **2023-12-18**; **permanent return to public control completed August 2024**. These are two distinct events. June 2024 presence/absence and June 2025 presence in HMPPS direct workforce series reflect a changing staff perimeter, not opening a new building.

## Explicit provenance
- https://imb.org.uk/document/morton-hall-2021-annual-report/
- https://cdn.websitebuilder.service.justice.gov.uk/uploads/sites/13/2025/07/Morton-Hall-IMB-2024-annual-report.pdf
- https://www.gov.uk/government/news/ministry-of-justice-takes-over-running-of-hmp-lowdham-grange
- https://assets.publishing.service.gov.uk/media/6903408be2ebc0fb39a51fd2/HMPPS_Annual_Report_and_Accounts_2024_to_25_-_1.0_WEB.pdf
- https://www.gov.uk/government/news/young-offenders-institution-to-be-repurposed
- https://www.gov.uk/government/statistics/prison-performance-ratings-2024-to-2025/ycs-annex-2024-25
- https://www.gov.uk/guidance/cookham-wood-prison

## Cross-file status
The earlier `gb_workforce_2021_2025_ycs_status_overlay_v1.csv` and `gb_historical_institution_status_verified_examples_v1.csv` encode annual/older labels that **must be qualified** by this dated event log. They are intentionally not edited (strict add-only). Prefer event log when constructing June snapshot classification.

## Methodological design
Track separately `source_digest_FY_function`, `snapshot_date_function`, `management_perimeter`, `youth_or_adult_occupants`, `date_precision`, and `verified_source`. Distinguish administrative re-designation, actual inmate intake, and public-sector direct-employment coverage.

Do not yet claim a complete 105-unit x 5-year historical validation. This note establishes *dated corrections for priority cases*, not an exhaustive institutional reconciliation.

No source files deleted, changed, moved, renamed, or overwritten.

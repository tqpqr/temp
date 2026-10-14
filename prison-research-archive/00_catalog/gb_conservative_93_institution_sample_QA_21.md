# UK HMPPS 2021–2025: conservative-scope sensitivity panel, QA 21

Generated on 2026-10-14 under strict **add-only** preservation.
Derived dataset: `02_uk/gb_workforce_2021_2025_conservative_scope_screen_93_v1.csv`
Original five-snapshot extract: `02_uk/gb_workforce_2021_2025_institution_long_panel_v1.csv`
Historical role/operator events: `02_uk/gb_historical_role_operator_events_audit_v2.csv`

## Inclusion rule and exact exclusions
The original workforce panel contains 105 named prison/YCS institutions in each 2021–2024 snapshot and 106 in 2025. Administratively non-institutional rows are always removed. For a **conservative sensitivity-screen**, exclude these 13 named risk cases across all dates (the 13th, Lowdham Grange, only occurs in 2025):

| Name | Why the unit is screened out |
|---|---|
| Werrington, Wetherby | Under-18 Youth Custody Estate |
| Feltham | Combined Feltham A (under-18 YCS) and Feltham B (adult) staffing not separately identified |
| Cookham Wood | Converted from YCS to adult role during 2024 |
| Morton Hall | IRC at 2021 June workforce snapshot; converted to prison later 2021 |
| Aylesbury, Brinsford, Deerbolt | Young-offender/Category C functional changes (YOI does not automatically imply under-18) |
| High Down | Changed predominant function Male Local to Category C |
| Belmarsh | Official predominant function changed from Male Reception in FY 2023/24 to High Security in FY 2024/25 |
| Dartmoor | Temporarily closed after radon-related inmate decant in July 2024; remained closed July 2025 |
| Usk/Prescoed | One workforce staffing row corresponds to Usk Category C and Prescoed Open |
| Lowdham Grange | Private-to-public operator transition; absent from workforce until 2025 |

These are deliberate **risk exclusions**, not evidence all excluded observations were unusable; the sensitivity specification sacrifices population coverage for easier institutional interpretation. In particular, adults in some former YOIs may be valid for a broader sample.

## Full source-panel versus 93-site stable-name risk-screen

| June year | Source-site rows (includes YCS) | Source operational FTE | Screened-site rows | Screened operational FTE | Screened grand total FTE |
|---|---:|---:|---:|---:|---:|
| 2021 | 105 | 27,594.32502 | 93 | 24,317.64078 | 31,741.29259 |
| 2022 | 105 | 27,258.59464 | 93 | 23,926.95466 | 31,217.01288 |
| 2023 | 105 | 28,376.39845 | 93 | 24,964.10318 | 32,773.41173 |
| 2024 | 105 | 29,783.23079 | 93 | 26,245.29003 | 34,294.01098 |
| 2025 | 106 | 28,765.54227 | 93 | 25,325.60104 | 33,468.74876 |

## Numerical validation
- 93 distinct name-identical institutions x 5 dates = **465 complete rows**.
- Every institution has all five years, no duplicated (name, year).
- Every row passes `operational_total_fte + nonoperational_total_fte = grand_total_fte` (differences at floating-point machine precision).
- The source row, original workbook path, and source year are retained.
- These are **staff FTE**, not employee headcount and not prison inmate population.
- The screened 2024→2025 operational FTE drop is approximately **3.50%**; this is descriptive, not an identified staffing elasticity.

## Still unverified — material
- The 93 are NOT a certified adult-only panel or all guaranteed operationally stable over the full observation period. They merely avoid listed *known/strongly suspected* breaks.
- Official prison-function register is published by **financial year**, and does not in itself establish exact 30 June status.
- Source FY2024/25 full 106-name Appendix C crosswalk exists in `02_uk/gb_2024_25_complete_106_establishment_function_crosswalk_v1.csv`; some earlier source crosswalks only have historical examples.
- HMPPS Annual Digest FY2025/26 dropped the prior prison functions/regions annex and the agency announced the Digest itself will end after FY2025/26. Future year classifications require different registers.

## Official sources
- Annual 2021/22: https://assets.publishing.service.gov.uk/media/62e16bbcd3bf7f75b9121a14/HMPPS_Annual_Digest_2021-22_Guide_FINAL.pdf
- Annual 2022/23: https://assets.publishing.service.gov.uk/media/64c24b107aea5b000d075040/HMPPS_Annual_Digest_2022-23_Guide_FINAL.pdf
- Annual 2023/24: https://assets.publishing.service.gov.uk/media/66a12dbe0808eaf43b50d6a4/Guide_to_HMPPS_Annual_Digest_2023-24.pdf
- Annual 2024/25: https://assets.publishing.service.gov.uk/media/6889f4186478525675738fda/Guide_to_HMPPS_Annual_Digest_2024_to_2025.pdf
- Dartmoor closure: https://questions-statements.parliament.uk/written-questions/detail/2025-07-04/HL9110/
- FY2025/26 changes: https://www.gov.uk/government/statistics/hmpps-annual-digest-april-2025-to-march-2026

No source file or earlier derived file changed, moved or deleted.

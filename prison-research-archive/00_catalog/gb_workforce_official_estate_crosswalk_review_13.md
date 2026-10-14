# Official HMPPS estate crosswalk — conservative second pass (2026 publication)

Input: 106 unique names from `02_uk/gb_workforce_2021_2025_institution_long_panel_v1.csv`. The source is the June 2026 HMPPS Workforce Statistics Guide, whose organizational group listing includes public prison establishments and a separate Youth Custody Estate.

Output: `02_uk/gb_workforce_official_2026_guide_crosswalk_v1.csv`.

## Actual classifications grounded in official list
- **90** archive names were explicitly matched to prison-estate organizational entries in the official guide *excerpt*.
- **3** matched the separate Youth Custody Estate group: Feltham, Werrington, Wetherby. Feltham is a mixed site (Feltham A youth and B adult), which cannot be separated by the original workforce workbook row.
- **13** were not found in the portion of the 2026 guide list reviewed. **This does NOT mean they are not prisons or not public sector**. These stay unresolved.
- Historical YCS-to-adult role of Cookham Wood, new workforce coverage in 2025 of Lowdham Grange and historical Aylesbury role change require year-specific evidence. A current guide cannot be extrapolated backwards uncritically.

## Statistical perimeter caveats
- The guide is a **2026 cross-sectional administrative map**, while the study panel runs **2021–2025**. Treat these as different temporal objects. The 90 matching entries are NOT certified to have been exclusively adult prisons for all five years.
- Public prison estate includes adult women, adult men, some young-adult units and specialized facilities, not necessarily exclusively adult prisons.
- The older overlay `gb_workforce_2021_2025_ycs_status_overlay_v1.csv` is deliberately unchanged; this new file is a source-specific supplement, not a destructive recoding.
- Do not create an adult-only balanced sample by simply discarding 13 unmatched institutions.
- Individual institution regulatory profiles, status dates and administrative transfers remain to validate for an adult-only sample.

## Primary evidence
- https://www.gov.uk/government/statistics/hm-prison-probation-service-workforce-quarterly-june-2026/workforce-statistics-guide
- https://www.gov.uk/government/collections/prisons-in-england-and-wales
- https://www.gov.uk/government/publications/prisons-and-their-resettlement-providers
- https://www.gov.uk/government/statistics/prison-performance-ratings-2025-to-2026/ycs-annex-2025-26
- https://hmiprisons.justiceinspectorates.gov.uk/hmipris_reports/hmp-aylesbury-2/

## Next confidence elevation
Acquire archival official institutional lists for **2021, 2022, 2023, 2024 and 2025** (government resettlement-provider register has historical updates) and verify exact date status. Reconcile overlaps with five workforce snapshots. Keep adult-only and entire public estate analysis samples separate.

Add-only operation: repository originals and previously-created panels not modified.

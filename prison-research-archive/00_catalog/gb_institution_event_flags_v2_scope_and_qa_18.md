# Event-sensitive GB workforce panel flags, revision 2 — scope correction

Produced `02_uk/gb_workforce_2021_2025_event_sensitive_panel_flags_v2.csv` (536 rows, one per row of existing five-year workforce panel), without editing originals or prior derived files.

## Research-critical handling
- 2024/25 Annex C lists formerly-unmatched names as public prisons; being absent from a **partial 2026 guide excerpt** was not evidence of missing prison status.
- Feltham A and Feltham B are separately listed in Annex C while workforce has `Feltham` aggregated; never treat it as a pure adult or youth facility staffing row.
- Werrington, Wetherby: YCS youth.
- Cookham Wood: 2024 youth-to-adult conversion; exact June 30 status requires dated role/occupancy data and must not be inferred from FY 2023/24 label.
- Morton Hall: 2021-06-30 immigration removal centre; statutory prison re-designation July 2021, initial inmate occupancy December 2021.
- Lowdham Grange: first in 2025 directly employed staff table after government takeover, NOT a newly built prison.
- Aylesbury/Brinsford/Deerbolt: institution function classification transitions, distinguish young adults from under-18 youth.
- Dartmoor: flagged for independent status review given extremely large 2024–25 FTE change; the field does NOT assert a cause.

## Limits and audit
The new CSV is a **risk-screening overlay**, NOT a year-specific official estate classification for all 536 observations. In particular, 2024/25 appendix fields, where present, cannot establish a 2021 snapshot institution function. Blank `as_of_2024_25_annual_digest_public` means not individually transcribed into this overlay, NOT private sector.

2024/25 appendix C source:
https://assets.publishing.service.gov.uk/media/6889f4186478525675738fda/Guide_to_HMPPS_Annual_Digest_2024_to_2025.pdf

The browser retrieved parsed PDF content, but its screenshot facility returned cache-miss on the requested PDF page. Accordingly, visual footnotes and layout have not been checked in this turn. The previously generated partial institution event and historical crosswalk files remain valid with their stated evidence limits.

The data needed to complete the larger task remain exhaustive FY 2020/21–2024/25 annual register extraction, point-in-time function and operator changes, and independent facility identity reconciliation, plus youth/adult flags. The current deliverable is specifically a complete **panel-wide risk layer**, not an institutionally certified historical panel.

All source files and existing derived archive products unchanged.

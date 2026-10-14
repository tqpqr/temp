# US-001 original US Census source-layout audit — completed (2026-10-14)

Original: `us/raw data/2011/public-use-file-layout.xlsx` (Git blob SHA-1 `723b170c572df098a9c760294ec521e311132410`, 11,902 bytes), sheet `public-use-file-layout`. Its exact organized mirror shares the blob SHA.

[Six original worksheet source fields, cells A11:E16](US-001_2011_layout_six_fields_v1.csv) preserved in CSV. Records are fixed-width 35-character ASCII (B4:B8).

Original positions: Government ID 1–14 (row 11), Item Code 15–17 (row 12), Amount in thousands **printed 18–32** but **start 18, length 12** (row 13), Survey Year 30–31 (row 14), Data Year 32–33 (row 15), Origin 34–35 (row 16). Therefore the **nonoverlapping amount position is 18–29**. This source discrepancy is independently supported by [previous 12,777-record source audit](../us_2011_fixed_width_layout_and_corrections_audit_v1.md), which already checked `us/raw data/2011/11state35.txt` (SHA `31b2db0eafbab431dd1e4e33f5f52ecc7b233eaa`). No redundant re-parsing performed. Source B6 says one field per record while six separate fields appear on rows 11–16.

Metadata `docProps/core.xml`: created 2023-10-06T12:01:48Z, modified 2025-03-24T19:35:10Z. **Do not claim this is an unchanged original 2011-vintage data-layout publication.** Source layout does not embed meanings for item codes E04, F04, G04. It links external official item-code and government-ID dictionaries in A12 and A11, respectively. It describes *state-government finances*, not prisons-only or local-government jail expenditure.

**Registry:** six layout fields are *format metadata*, not six prison indicator observations; add to indicator-period ledger with source-cell anchors, explicit evidence grade, year 2011 from companion filename. **Breaks:** MB-013 wrong amount range plus B6 label inconsistency; MB-014 retrospective layout-file metadata (2023–25) relative to 2011 data. Do not hypothesize corrections to 2011 numbers.

**US-001 DONE**: six original fields decoded, source/mirror SHA verified, source values left unchanged. Next source can rotate outside the already-audited 2011 raw TXT.

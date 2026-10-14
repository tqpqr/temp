# Checkpoint v8 — 14 October 2026 — USA 2011 layout + existing source audit integrated

**Active index:** [INDEX v13](../INDEX_v13.md); [queue v6](MICROTASK_QUEUE_WAVE1_v6.csv); [microtask protocol v4](MICROTASK_PROTOCOL_AND_QUEUE_v4.md). Current Git HEAD checked before checkpoint: `58735b66a9d7213db46319a9ba662204f4c34e8d`.

## Preservation and verified saved files
Complete (nontruncated) Git tree: **1,124 baseline original files**, **1,067 content-identical organized research mirrors**, **57 unrelated originals in alt/alt2/alt3 excluded**. Source `us/raw data/2011/public-use-file-layout.xlsx` blob `723b170c572df098a9c760294ec521e311132410` and `us/raw data/2011/11state35.txt` blob `31b2db0eafbab431dd1e4e33f5f52ecc7b233eaa` retain identical categorized mirrors. All newly generated entries and old evidence still exist. No source file overwritten, relocated or deleted.

## US-001 DONE — one original XLSX
- Original sheet `public-use-file-layout`, all six field rows A11:E16 saved [CSV](progress/US-001_2011_layout_six_fields_v1.csv), commit `71612a088241523e27ef8819e216dd7844e4390a` and verified [audit](progress/US-001_finance_codebook_2011_v1.md), commit `f50bd692effa9d2ff5e06fe131679c114298075e`.
- Published `Amount (thousands)` field B13 says chars **18–32** but C13=18 / D13=12 means **18–29**; 30–31 survey year, 32–33 data year, 34–35 origin. Six nonoverlapping fields fill exact 35 ASCII characters. Another documentation ambiguity B6 says one field while six appear on A11:E16. **MB-013 confirmed**.
- Original document metadata in `docProps/core.xml`: created **2023-10-06**, modified **2025-03-24** despite data in 2011 folder; original historical 2011-vintage workbook claim unverified. **MB-014 confirmed**. Original XLSX includes URLs to distinct Census item code and government ID glossaries, **not** their actual definitions. Item E04/F04/G04 semantic names remain UNVERIFIED.

## US-002 DONE_PRIOR_AUDIT_RECONCILED — previous full evidence saved and reused
- Existing [all 12,777-record audit](us_2011_fixed_width_layout_and_corrections_audit_v1.md) and [151 source-native numeric records E04/F04/G04](us_2011_state_finance_corrections_E04_F04_G04_verified_v1.csv) were inspected/reconciled without redoing fixed-width parse. [Progress record](progress/US-002_completed_from_prior_2011_fixed_width_audit_v1.md), commit `923f88b8ab167c0e9d8548f6a6a0ded8cfe99746`.
- 2011 code E04 has 51 government identifiers; F04 has 50 (missing `32000000000000`); G04 has 50 (missing `04000000000000`). Missing source rows **are not zeros**. National aggregate source code values in thousands current USD: E04 37,492,787, F04 1,254,079, G04 261,607; economic code definitions require publisher item-code glossary.
- Three original observed source-code coverage entries in [indicator registry v5](INDICATOR_PERIOD_COVERAGE_REGISTRY_v5.csv) are **state-government source data**, NOT prisons-only. Full original line IDs and amounts remain in prior 151-row CSV; numeric values have not been independently rederived anew from the TXT in this turn.

## Current two catalogues and saved statuses
- [Indicator × reporting period coverage v5](INDICATOR_PERIOD_COVERAGE_REGISTRY_v5.csv) **912 records**: earlier v3 903 + six nonnumeric original source-layout metadata entries v4 + three source-value code coverage entries v5. v4 commit `fc89e5cd293a72d0bfff184ac015007a65ae31fa`, v5 commit `82ae3cf523683a85a02558159605e9c440c61cad`. All files re-fetched and verified. **Count not comparable numeric series count.**
- [Methodological breaks/anomalies v3](METHODOLOGICAL_BREAKS_AND_ANOMALIES_v3.csv) **15 cases**: v2 adds MB-013/014 (`90a3f062d90dea027d263c1121e8fe950543671e`); v3 adds **MB-015** two code×government missing entries (`b77f96e653e1dbb92f318d6bc5c4206801d69252`). Source-cell evidence and separate hypothesis/interpretation status preserved.
- [Protocol v4](MICROTASK_PROTOCOL_AND_QUEUE_v4.md), commit `be62e131878719a2e5a38a9fda9e3c8510fc8edd`, explicitly says **if acceptance criterion already fulfilled by prior audited source, mark DONE_PRIOR_AUDIT_RECONCILED rather than repeating extract**.
- [Queue v6](MICROTASK_QUEUE_WAVE1_v6.csv), commit `11d1acee2555f8d0fdd75d89576bac503e5a33d4`: DONE 6, DONE_PRIOR_AUDIT_RECONCILED 1, BLOCKED 2, WAITING 1, PENDING 20, NEXT 1. [Index v13](../INDEX_v13.md), commit `58735b66a9d7213db46319a9ba662204f4c34e8d`, is active.

## Next task — GB-020, one original file
`GB/Monthly_Bulletin_December_2024_web.ODS`. Inspect actual original report date, sheet/column meanings for Certified Normal Accommodation (CNA), used capacity, operational places and people present, institutional row source cells. **Never assume month-end stock equals FY annual average or Italian regulatory denominator**. Add indicator/date source evidence to new registry v6 if actual numeric cells verified; add genuinely new break or write NO_NEW_BREAK. Commit one bounded progress CSV/note, then queue v7 and checkpoint v9; do not repeat completed US/GB work.

No asynchronous work is ongoing beyond these committed Git artifacts.

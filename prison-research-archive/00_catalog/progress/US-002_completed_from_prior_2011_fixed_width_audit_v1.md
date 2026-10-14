# US-002 — DONE by preserved prior full-source audit, no duplicate extraction

Original `us/raw data/2011/11state35.txt` (Git SHA-1 `31b2db0eafbab431dd1e4e33f5f52ecc7b233eaa`), 459,972 bytes; categorized mirror same SHA. This source was **already fully read** in [2011 raw-record QA](../us_2011_fixed_width_layout_and_corrections_audit_v1.md): 12,777 original 35-character records, 51 distinct government IDs, 358 item codes, signed amounts in positions 18–29, 30 valid negative amounts. New [US-001 layout audit](US-001_finance_codebook_2011_v1.md) independently checked original workbook layout rows 11–16 and original position contradiction MB-013.

[Already published 151 source-cell-anchored E04/F04/G04 records](../us_2011_state_finance_corrections_E04_F04_G04_verified_v1.csv) were re-read now as a CSV, with original source record positions and raw text (not the entire 12,777-line TXT re-parsed).

| Code (meaning not independently verified) | Actual 2011 source records | National aggregate government ID 00000000000000, thousands of nominal USD |
|---|---:|---:|
| E04 | 51 | 37,492,787 |
| F04 | 50 | 1,254,079 |
| G04 | 50 | 261,607 |

Exactly **51** government IDs among the 151 lines. F04 lacks the original government ID `32000000000000`, G04 lacks `04000000000000`. These two code/government pairs are **source missingness, NOT numeric zeros**; all E04 IDs are present. All source years are `11`. The row-level correctional financial meaning of E04/F04/G04 **cannot be established solely by the layout workbook**, which references an external item-code definition file. The economic scope is U.S. *state government finance*, not city/county jail or individual prisons.

**Outcome:** existing full-source prior evidence exceeds the narrower task acceptance criterion (validate a sample). No redundant work and no new source measurements manufactured. Indicator registry v5 can add **three code-specific, 2011-only source-value coverage records**, preserving actual per-code government-ID counts and exact source records; their substantive semantic labels remain NOT VERIFIED. Add missingness warning MB-015 to breaks register; existing MB-013 amount-position error reused rather than rediscovered.

**US-002 DONE_PRIOR_AUDIT** (evidence reconciled today, new source re-extraction not necessary). Next independently scoped task should leave U.S. branch to maintain archive-wide rotation.

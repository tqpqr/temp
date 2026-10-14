# GB-013 follow-up v3 — confirmed Ashfield contractual rebid, rounding bounds

## Independent external provenance (official and operator)
- UK Parliament, MoJ written answer 27 Jan 2025, HL3980: https://questions-statements.parliament.uk/written-questions/detail/2025-01-13/hl3980 . Ashfield former Serco contract **01/11/1999–31/10/2024**; next Serco contract **01/11/2024–31/10/2034**. Same operator and facility, *not a new prison*.
- Serco announcement 23 Apr 2024: https://www.serco.com/uk/media-and-news/2024/serco-awarded-ps200m-contract-to-manage-hmp-ashfield-for-further-ten-years ; competitive rebid, around £200 million for ten years; already operating Ashfield since 2005.
- MoJ annual account FY2024/25 (official PDF): https://assets.publishing.service.gov.uk/media/691213e3e9348ac8fb54f4c4/36.27_MOJ_Annual_Report_and_Accounts_2024-2025_WEB.pdf lists Ashfield November 2024 contract start. Underlying PDF has not been independently screenshot-audited in this pass; parliamentary text is sufficient for dates.
- Source FY2023/24 T1 row26 Nov 1999, FY2024/25 T1 row40 Nov 2024. MB-028 changed to CONFIRMED_CONTRACT_REBID_SAME_OPERATOR in registry v12. Do not infer unchanged accounting terms or service scope.

## Three source-unit cost differences: investigate denominator rounding, not fabricate correction
From published FY2024/25 ODS:
- T1 PFI: £341,221,566 total, printed CNA 5,287, printed average population 6,233; printed per-place £64,534 vs division on displayed CNA rounding to £64,540; printed per-prisoner £54,740 vs displayed population rounding to £54,744.
- T1 Fosse Way £59,876,871 overall, population 1,698, printed per-prisoner £35,255 vs division with displayed integer rounding to £35,263.
- Source expressly says averages and expenditure values rounded and totals calculated from unrounded figures (`T1!A54`; `T2!A67`). Using fractional denominators implied by reported ratio yields about **5,287.5 PFI places**, **6,233.5 PFI annual-average prisoners**, and **1,698.4 Fosse Way prisoners**; these are *inverse-calculated diagnostics*, NOT observed source data. They are consistent with the possibility of independently rounded denominators, but the precise values are not established. This is a plausible arithmetic mechanism, not an independently verified calculation protocol.
- The 20/23 preliminary QA passes and 3 REVIEW remain unchanged. Do not silently change original monetary amounts.

## Registry blocker
`INDICATOR_PERIOD_COVERAGE_REGISTRY_v15.csv` is too large for GitHub connector file-content fetch: both whole and line-window queries returned empty despite blob identity `d314d9ded50d882e85c2099fefa16a6d320ab6be`. Do NOT rebuild, overwrite or append blind. Registry remains v15, 1,111 source-graded entries pending byte-level access. Existing FY2024/25 detailed 119 records must not be duplicated.

GB-013 remains IN_PROGRESS until indicator-register crosswalk and fuller QA.

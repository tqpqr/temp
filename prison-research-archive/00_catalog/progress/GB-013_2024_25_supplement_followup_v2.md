# GB-013 contract-date comparison and arithmetic follow-up v2

## Source-verified Ashfield comparison
- Prior FY2023/24 original ODS: `GB/costs-per-prison-place-prisoner-2023-24-supplementary-information.ods` SHA `59f04c2bb5a7c0b7aeb8b54eca7cc506131aa277`, T1 row 26: Ashfield, **Nov 1999**, CNA 416, annual-average prisoners 410, overall £19,876,502.
- FY2024/25 original ODS: `GB/costs-per-place-per-prisoner-2024-2025-supplementary-information.ods` SHA `bfb4795029d60ebf1351502b95b803d13c9ffcf1`, T1 row 40: Ashfield, **Nov 2024**, CNA 416, annual-average prisoners 408, overall £21,481,522.
- **MB-028** preserves the changed contract-start-date field. A new contractual vintage does not establish a new prison opening. The reason for the date change is UNVERIFIED pending contracts/procurement evidence.
- Altcourse remains M&M (prior MB-026). Fosse Way denominator/exposure caveat prior MB-027 still applies.

## Arithmetic findings (23 checks stored separately)
- 20 PASS with published-source tolerances; 3 REVIEW, not source corrections:
  - T1 PFI E32/C32 printed full ratio calculation £64,540 vs source F32 £64,534, six-pound gap.
  - T1 PFI E32/D32 calculation £54,744 vs source G32 £54,740, four-pound gap.
  - T1 Fosse Way E42/D42 calculation £35,263 vs source G42 £35,255, eight-pound gap.
- Published `T1!A54` and `T2!A67` expressly say averages/expenditures rounded and totals calculated from unrounded figures. Hidden decimal population or CNA values could explain some gaps but have **not been observed**; do not assert that this is the cause.
- T1 E7 £4,926,302,564 vs T2 H59 £4,926,302,565, and T1 F7 £59,026 vs T2 I59 £59,025, preserved as published cross-table discrepancies.
- Not a full recomputation of every row or an evidence-supported restatement.

## State
Source extraction and initial checks saved; issue register v11 has 28 items including MB-028; queue v17 explicitly sets GB-013 IN_PROGRESS_SOURCE_AUDIT. Indicator-period registry stays **v15** pending review of existing records and no duplication of prior FY2024/25 source rows. GB-013 not marked DONE.

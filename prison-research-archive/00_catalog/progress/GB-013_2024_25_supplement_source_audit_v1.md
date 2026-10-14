# GB-013 — FY2024/25 supplemental ODS, source-anchored initial audit v1

Status: PARTIAL SOURCE AUDIT; do not mark GB-013 DONE until complete reconciliation, register decisions and checkpoint. Scope: England and Wales, financial year 2024/25, not whole UK.

## Original source identity and extraction
- Original: `GB/costs-per-place-per-prisoner-2024-2025-supplementary-information.ods`.
- Git blob SHA-1: `bfb4795029d60ebf1351502b95b803d13c9ffcf1`.
- ODS decompressed directly from GitHub binary, not inferred from filename. Cover A19: `Published 26 March 2026`.
- Three original sheets: `Cover_` (9 nonempty rows), `T1_Contracted_Prisons` (39), `T2_Supplementary_Data` (44). 92 nonempty rows total; 457 nonblank text/numeric cell records. Byte-decoding extraction yielded mojibake `Â£` for the pound sign in rendered string; `numeric_value` is read from the original typed ODS cell attribute, and original cell coordinates are preserved.
- Full source cell extraction: `GB-013_2024_25_supplement_original_cells_v1.csv` (all nonempty cells, `sheet,row,cell,source_text,numeric_value`).
- Original binary Git SHA-1 is NOT an external publisher SHA-256. Source is not independently downloaded from publisher.

## National key cells (T2_Supplementary_Data)
- B59 CNA 83,460; C59 financial-year average prisoners 87,009.
- D59 direct resource expenditure £3,292,840,593; E59/F59 direct cost per CNA place / prisoner £39,454 / £37,845.
- H59 overall resource expenditure £4,926,302,565; I59/J59 overall per CNA place / prisoner £59,025 / £56,618.
- D49 Service Concession Arrangements £592,839,053, nested under Non Pay D42 £1,350,206,626. **Do not sum D49 on top of Non Pay**.
- T1_Contracted_Prisons: C7/D7/E7/F7/G7 83,460 / 87,009 / £4,926,302,564 / £59,026 / £56,618. The £1 whole-unit difference T1 E7 vs T2 H59 and £1 per-CNA-place difference T1 F7 vs T2 I59 must be retained as a source discrepancy, NOT silently normalized. T1 row54 and T2 row67 explain rounded figures and totals from unrounded parts. Further reconciliation pending.

## Contracted establishments (T1)
- PFI total C32:G32: CNA 5,287; population 6,233; overall £341,221,566; per place £64,534; per prisoner £54,740.
- Manage & Maintain total C46:G46: CNA 9,872; population 11,255; overall £412,585,668; per place £41,794; per prisoner £36,658.
- All contracted C49:G49: CNA 15,159; population 17,488; overall £753,807,234; per place £49,727; per prisoner £43,104.
- Altcourse T1 A36:G36: M&M, contract start Jun 2023, CNA 784, average population 1,179, overall £45,231,143; cross-year contract category change was already MB-026, do not create another facility or duplicate issue.
- Fosse Way T1 A42:G42: M&M, start May 2023, CNA 1,715, average population 1,698, overall £59,876,871, £34,914/CNA place, £35,255/prisoner. For FY2023/24 (GB-012) CNA 1,143, FY-average population 974, overall £58,338,786 and £51,048/CNA place. Capacity and operating exposure changed. Do not claim like-for-like efficiency increase or full-year identical denominator without place-day evidence.
- Ashfield T1 A40:G40: M&M, printed contract start Nov 2024, CNA 416, FY-average 408, overall £21,481,522. Prior-year contractual category/date must be checked before classifying as new contract, transfer or physical facility.
- Five Wells T1 A41:G41: M&M, Jan 2022, CNA 1,689, FY-average 1,705, overall £63,593,607.

## What remains before GB-013 DONE
1. Source arithmetic: all contracted components, parent-child expense subtotals, cost-per-place/prisoner divisions, publisher rounding and T1/T2 £1 discrepancy; save per-check QA.
2. Review source definitions and notes, any reclassification/category drift, potential Ashfield contract transfer and comparisons to GB-012/previous detailed FY2024/25 rows (119 pre-audited, no duplication).
3. Add only genuinely new national indicators to indicator-period registry; document crosswalk and methodological issues, keep source editions distinct.
4. Update queue, registers, checkpoint and INDEX version additively; verify created blobs/commits.

# Prison research archive — ACTIVE INDEX v19 (14 October 2026)

## Resume point, original source preservation

**GB-008 DONE; GB-009 NEXT.** Detailed [checkpoint v14](00_catalog/SESSION_CHECKPOINT_20261014_v14.md) is authoritative for completed source verification, source row addresses, original Git blob SHA, issue MB-021 and all new artifacts.

- [Microtask queue v12](00_catalog/MICROTASK_QUEUE_WAVE1_v12.csv): 31 bounded tasks; **12 DONE**, 1 DONE_PRIOR_AUDIT_RECONCILED, 2 BLOCKED, 1 WAITING, 14 PENDING, **1 NEXT: GB-009**.
- [Indicator × period registry v11](00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v11.csv): **1,011 evidence-graded records**. GB-008 adds 25 directly publisher-reported financial FY2019/20 source indicators `R00984–R01008` plus **3 explicitly derived source-cell O&M differences** `R01009–R01011` — these are not separately published indicators or 3 extra prisons. Registry count is **not** a count of comparable empirical series.
- [Methodological issues ledger v7](00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v7.csv): **21 independent issue records**, newly added **MB-021** source list/subtotal operator-year scope issue linked to prior **MB-005** Birmingham takeover. Other older matters including **MB-004** 2018/19 direct expenditure restatement, **MB-010** public/private finance perimeter and **MB-020** capital category captions remain available and unchanged.
- [Previous active index v18](INDEX_v18.md) for GB-007 FY2018/19 source and [source-preservation microtask protocol](00_catalog/MICROTASK_PROTOCOL_AND_QUEUE_v4.md). Originals, previous indices and source panels are **never overwritten**.

## FY2019/20 original MoJ/HMPPS prison costs: GB-008

Original `GB/costs-prison-place-prisoner-2019-20-supplementary-information.ods` **Git SHA-1 `c5ec73b1d01770d0229f46a85d14f53ebb21d0e6`**, 41,569 bytes, `Cover!A19` publisher date **29 October 2020**. Geography: **England and Wales**, not the whole UK. FY2019/20 **year-average denominators**, not one-day population.

Completed original-source audit:
- [Full research note and publisher methodology](00_catalog/progress/GB-008_2019_20_supplement_source_audit_v1.md)
- [93 source nonempty worksheet rows with verbatim A–K numeric/textual values and physical row addresses](00_catalog/progress/GB-008_2019_20_supplement_full_source_cells_v1.csv)
- [32 original-source and source-to-source numerical reconciliation checks](00_catalog/progress/GB-008_2019_20_supplement_arithmetic_QA_v1.csv)

Three actual source ODS sheets: `Cover`, `T1_Contracted_Prisons`, `T2_Supplementary_Data` (8+41+44 nonempty rows). No source-sheet `table:formula` attributes; all national totals below are original stored source numbers.

| Original fiscal FY2019/20 measure | Publisher value | Original source |
|---|---:|---|
| Certified Normal Accommodation | **79,232 places** | `T2_Supplementary_Data!B59` |
| Annual average prison population | **82,890 people** | `T2!C59` |
| Direct Resource Expenditure | **£2,401,640,556** | `T2!D59` |
| Overall Resource Expenditure | **£3,536,900,071** | `T2!H59` |
| Direct cost per place / prisoner | **£30,311 / £28,974** | `T2!E59:F59` |
| Overall cost per place / prisoner | **£44,640 / £42,670** | `T2!I59:J59` |
| Service Concession Arrangements child category | **£470,891,780** | `T2!D49` |

### Critical new primary-source finding — MB-021

**The 2019/20 contracted Operate & Maintain subtotal contains a private Birmingham operator-period financial contribution that is absent from the list of currently named contracts.**

Original `T1_Contracted_Prisons` names only **Doncaster (row 43)**, **Oakwood (46)** and **Sodexo Northumberland (47)** under O&M. Subtracting the three listed individual rows from source publisher subtotal **row 48** leaves **274 CNA places, 234 annual-average persons and £7,586,785 overall spending**.

In the already independently validated **different** original FY2019/20 by-establishment file `GB/costs-prison-place-prisoner-individual-prison-2019-20.ods` (blob `969df2a0a07b426ab6440e193bc8ea446637cc43`), source `T3_Cost_by_Establishment!B156,C156,H156` **G4S Birmingham operator-period** independently publishes **275 CNA, 235 average persons, £7,586,786 overall**, matching *all three derived discrepancies within one whole rounded unit*. Prior **MB-005** documents Birmingham returning to public operation in July 2019.

Publisher `T1!A5:A6` counts **104 public + 13 private institutions at year end = 117**, while source financial statements still have **118 operator-period accounting lines** (not 118 physical prisons). At year-end the prior FY2018/19 counts were **103+14 = 117**. The data distinguish current operator names from financial-year expense inclusion. **Do not drop the unmatched £7.6m from the reported total, invent a 14th private prison still operating at year end, or count the original G4S entry a second time on top of the publisher subtotal.**

Remaining note: 2018/19 to 2019/20 **Non payroll services** and **Admin running costs** source values move substantially, but causal/category equivalence is NOT proven: archive as screening questions, not confirmed breaks. Non Pay parent and its eight children are hierarchical and not additive with one another. Original public/private perimeters are cautioned against by publisher.

## NEXT GB-009

Source `GB/costs-per-prison-place-prisoner-2020-21-supplementary-information.ods`. First consult [latest checkpoint](00_catalog/SESSION_CHECKPOINT_20261014_v14.md), [queue](00_catalog/MICROTASK_QUEUE_WAVE1_v12.csv), [registry v11](00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v11.csv), [breaks v7](00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v7.csv), and existing original FY2020/21 by-establishment 117 audited financial source lines. Verify original source date/vintage, all actual source sheet cells, numerical relationships and potential financial-category definition changes. Do not infer COVID-19 impacts or reporting changes from the fiscal year label alone. Update two catalogs only with new evidence, queue v13, checkpoint v15, index v20. Preserve all originals and old versioned assets.

All source Git SHA-1 values represent **repository Git objects**, not verified publisher-side binary hashes. No background work is running.

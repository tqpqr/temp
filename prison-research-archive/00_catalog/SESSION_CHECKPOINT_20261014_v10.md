# SESSION CHECKPOINT v10 — GB-021 two original UK 2025 monthly bulletins (2026-10-14)

**Last Git HEAD before this checkpoint:** `22a0026131ce32c37421105e73240e6751469557` (direct `refs/heads/main` read). Existing original files and previous versioned files have not been edited. New additive files listed below were independently re-fetched after writing.

## Last task actually completed: GB-021 DONE

Originals independently read **in ZIP/ODS content.xml**, not inferred from filenames or old spreadsheet exports:
- `GB/Monthly_Bulletin_January_2025_web.ODS`, Git blob `c6b2e940b63667f25d8056239c656d3a784f6e93`, **11,563 bytes**, sheet `MonthlyBulletin!A2` says **27/1/2025**.
- `GB/Monthly_Bulletin_February_2025_web.ODS`, Git blob `10aeba9b3c131918c6e32c406691c0ecc9577c96`, **11,581 bytes**, sheet `MonthlyBulletin!A2` says **24/2/2025**.

Each original has **120 prisons** `A5:E124`, 4 numeric fields B–E per prison, `B125:E125` official totals. Both sets **already exist** in `02_uk/gb_monthly_prison_population_capacity_2025_raw_v1.csv` with exact source report dates/rows and 960/960 numeric field values matching. No duplicate 240-row facility export created; the sole name text encoding case is Peterborough A90 `&` (original) versus literal `&amp;` in prior exported CSV. Treat this as text HTML-entity normalization, not a change of prison or a numeric break. No longitudinal source name-to-ID assumptions.

National source fields in Jan / Feb respectively:
- **Baseline CNA B125:** 83,560 / 83,557 (institution B-row sums exact)
- **In Use CNA C125:** 79,428 / 79,340 (institution C-row sums exact)
- **Facility Operational Capacity sum D5:D124:** 90,012 / 89,985 (**derived**, no equality with printed national D125)
- **Published national Useable Operational Capacity D125:** 88,662 / 88,635
- **Population E125:** 86,463 / 87,199 (institution E-row sums exact)

Original source `A129`, `A149:A152`: **1,350-place operating-margin deduction** in each monthly edition. Arithmetic exact (90,012−1,350=88,662 and 89,985−1,350=88,635). Existing **MB-016** reused; ledger remains **v4, 17 cases, NO_NEW_BREAK**. Existing December **MB-017** anomaly for Littlehey is absent January/February 2025 (source row 72 has 1,125=1,125 Baseline/In Use), but historical cause remains **OPEN**; no retrospective correction.

## Newly saved and re-fetched artifacts

1. [GB-021 10 verified source-cell observations](progress/GB-021_monthly_two_sources_v1.csv): 11 CSV records counting header, blob `b29411cd390752e59cb61a80e29e665e973edec4`, write commit `f0b38a4b06e46d99bb2eb65db525fc266fed5b30`.
2. [GB-021 original ODS source audit, definitions and reconciliation](progress/GB-021_JanFeb2025_original_bulletins_QA_v1.md): blob `eacdce5c7892ba55f85178fb32201b588ef9c12b`, write commit `be2c45d4e4b207b7f847ec34db24ec7ceaadf6a5`.
3. [Indicator × period registry v7](INDICATOR_PERIOD_COVERAGE_REGISTRY_v7.csv): **927 records**, up from 917; new `R00918`–`R00927` are distinct exact-day national measures, not ten new original documents. Blob `694d387befdb3ca2ccbae72bb349023cbc04b21b`, commit `f3058b1eff066961621d6c16515a95f1ac744623`.
4. [Microtask queue v8](MICROTASK_QUEUE_WAVE1_v8.csv): GB-021 DONE, GB-022 NEXT; **8 DONE, 1 DONE_PRIOR_AUDIT_RECONCILED, 2 BLOCKED, 1 WAITING, 18 PENDING, 1 NEXT = 31**. Blob `151716917b09f19efdba34ede9d1e3cce79523af`, commit `22a0026131ce32c37421105e73240e6751469557`.

[Latest methodological breaks and anomalies register v4](METHODOLOGICAL_BREAKS_AND_ANOMALIES_v4.csv) is unchanged. Older indices, queue versions, inventories, original ODS and copies deliberately remain intact. These are Git blob SHA-1 identities, **not** external SHA-256. No external publisher archive file hash equivalence claimed. Preservation confidence for this task is based on add-only writes and source SHA checks, **not** a new 1,124-file baseline hash traversal.

## Resume instruction and NEXT microtask

**GB-022 NEXT:** `GB/workforce/HR-tables-31-March-2020.xlsx`, starting from [queue v8](MICROTASK_QUEUE_WAVE1_v8.csv). Before parsing it again, consult existing `gb_workforce_june_2015_2020_establishment_xlsx_QA_corrected_v3.csv` and `gb_workforce_binary_audit_06.md` / `gb_workforce_official_methodology_07.md` and [per-file evidence ledger v11](ARCHIVE_PER_FILE_EVIDENCE_LEDGER_v11.csv) to avoid duplicating prior complete audits. Verify original SHA, exact reporting date, sheet/table, workforce **FTE versus headcount**, group and territorial coverage, source cells, and previous source-row coverage. If full acceptance already met, use `DONE_PRIOR_AUDIT_RECONCILED` with evidence; otherwise perform only missing checks. Either extend indicator registry to v8 **or** record `REGISTRY_UNCHANGED`. Explicitly decide `BREAKS_UPDATED` or `NO_NEW_BREAK`; never confuse UK England/Wales prison stock with Great Britain/UK workforce or fiscal-year observations.

**No asynchronous or background work is running.**

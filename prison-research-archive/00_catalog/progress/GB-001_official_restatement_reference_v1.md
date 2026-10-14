# GB-001 — DONE: official FY2015/16 restated prison-cost source reference (2026-10-14)

## Narrow task
Verify **existence of official FY2015/16 restated establishment-cost XLSX**, exact publishing authority and attachment URL, and whether it is already present among the 27 original local GB financial files. **Do not download, compare, or add a publisher binary in this task.**

## Verified upstream publication (official government primary source)
- Publisher: **Ministry of Justice (United Kingdom)**, `Prison performance statistics 2016 to 2017`, published **26 October 2017**.
- Exact official release: https://www.gov.uk/government/statistics/prison-performance-statistics-2016-to-2017
- Original attachment title exactly as printed: **Costs per prison place and cost per prisoner by individual prison establishment 2015 to 2016: restated tables**.
- Publisher describes file as **MS Excel Spreadsheet, 92 KB**; this is the provider's rounded display size, **not an observed downloaded-byte count**.
- Direct publisher attachment: https://assets.publishing.service.gov.uk/media/5a82f0f140f0b62305b9523d/costs-per-prison-place-per-prisoner-by-individual-prison-2015-2016-restated-tables.xlsx
- The release's own `Details` explicitly says this 2016/17 publication **restates statistics covering 2015/16**.
- The government page was read and this specific attachment followed; the web reader returned `Unsupported content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`. This is **not proof of a broken upstream link**, nor proof that XLSX file bytes have been successfully downloaded and checked.

## Local archive comparison
- Complete and non-truncated GitHub tree for `tqpqr/temp` at starting main commit `6519ac3274eb9b22f5fdcd73a875d1ab883bd1ed`: **1,124** original blobs outside the new archive; **1,067** original research blobs mirrored exactly; **57** other-project files untouched.
- Exactly **27** original `GB/` financial-cost source files present. Includes the **initial** FY2015/16 workbook `GB/costs-per-place-cost-per-prisoner-individual-prison-establishment-2015-16_tables.xlsx` (Git blob `09ae7bb2b1455657015f7203fdc7ea7eb283d707`, 89,232 bytes).
- The **restated FY2015/16** XLSX attachment is **not among these 27 local GB financial originals**, and must not be confused with the **FY2014/15 restated** XLSX (`GB/costs-per-place-per_prisoner-individual-prison-establishment-2014-15-restated-tables.xlsx`).
- Existing previous [official source register](../gb_cost_FY2014_18_official_attachment_provenance_and_missing_2015_16_restatement_v1.csv) records the same expected URL. This task **independently verifies the web release and link and does not double-count an additional source file**.

## Evidence grade and task completion
**GB-001: DONE**. Publisher, publication date, attachment title and exact official URL verified by live official release. Local absence checked in Git tree. **Not yet verified**: downloaded bytes, SHA-256, sheet content, revised cells, exact reasons for restatement, existence of an exact match in other unindexed external stores.

## Next independent microtask
**GB-002**: retrieve the exact publisher file, calculate SHA-256 and Git blob hash from actual downloaded bytes, validate Excel ZIP structure, and save as **separately labelled additional official research source** without modifying any original or earlier mirror. If binary GitHub upload unavailable, record limitation and do not claim stored. Later **GB-003** will compare actual initial and restated 2015/16 source data.

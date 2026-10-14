# Prison research archive — active index v33 (2026-10-14)

**INT-002 DONE with original-source corruption documented; NEXT INT-003 (Finnish decision Annex 2 recovery).** [Checkpoint v32](00_catalog/SESSION_CHECKPOINT_20261014_v32.md).

## INT-002 Finland — strongest findings
- Archive source named `space-archive/extra/stp8/Finland_Paatos_vankipaikkojen_jakautumisesta_22.11.2021.pdf` is **actually 154,203-byte HTML 404**, not a PDF. Git blob SHA-1 **7007835861b6ee8a6dcae8ef6624cdb5bb8c8288**; original bytes read directly via GitHub connector. HTML page title = `Sivua ei löytynyt - Rikosseuraamuslaitos`. Original not modified. New **MB-035**.
- Authenticated seven-page Finnish Prison and Probation Service (**RISE**) decision from **22 Nov 2021**, **Dnro 12/280/2021**, was located from publisher's **1 Dec 2021** STT news service press release. [Official publisher-linked PDF](https://www.sttinfo.fi/data/attachments/00037/3fe38edf-552e-428d-a53c-31b19201c702.pdf). Read page-labelled text 1–7. Screenshots timed out; no binary SHA256 or byte upload of independently recovered PDF. [Publisher announcement](https://www.sttinfo.fi/tiedote/69926272/vankipaikkauudistuksella-vaikutuksia-laajasti-kaikkiin-vankiloihin-erityisryhmille-perustetaan-uusia-osastoja?publisherId=2090).
- It specifies **planned specialised prison-place allocations** with conditional future implementation **2022–2025** (additional longer-term proposals), based on forecast prisoner counts and **90% target occupancy** (PDF p5), with at least annual reassessment. These are **not** 2021 operational capacity or prison-site occupied bed-days. New **MB-036**.
- **Annex 2** `Valtakunnallinen vankipaikkataulukko` lists complete planned prison-site numbers according to p1/p7, but **is NOT included** in the accessible seven-page publisher PDF. No official national or full by-prison place total obtained. Separate retrieval microtask **INT-003** added to queue.
- [Source audit](00_catalog/progress/INT-002_finland_capacity_v1.md); [18 selected planned ward allocations with exact pages and non-additivity](00_catalog/progress/INT-002_finland_planned_capacity_policy_items_v1.csv); [source-type/identity check](00_catalog/progress/INT-002_finland_source_payload_identity_QA_v1.csv). These are **policy item observations only**, not additional main indicator-period registry actual-capacity rows.
- International interpretation: do not equate Finland's allocation plan with Italy's DAP `capienza regolamentare` on **31 Jan 2023** (INT-001, 189 individual facilities) or British fiscal-year **Baseline CNA** (GB-019). Capacity concepts and observation timing are substantively different.

## Queue and status
- [Queue v27](00_catalog/MICROTASK_QUEUE_WAVE1_v27.csv): **32 tasks**, **26 completed/reconciled**, four blocked, one waiting, **INT-003 NEXT**.
- [Methodological cases v18](00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v18.csv): **36 cases**, new MB-035 and MB-036. Do not merge these two: source byte-integrity defect vs analytical concept mismatch.
- [Indicator-period registry v16](00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v16.csv): **1,136** original evidence records, intentionally unchanged; Finland 2021 allocations are not actual measured capacity and missing Annex 2 cannot be imputed.
- Prior [index v32](INDEX_v32.md) and UK [GB-019 synthesis](00_catalog/progress/GB-019_cost_methodology_synthesis_v1.md) remain intact; originals preserved add-only.

**NEXT INT-003:** obtain annex 2 (full prison allocation table) for RISE 12/280/2021 or document authoritative byte retrieval blocker. Do not fabricate missing institutions, counts, enactment dates or national sums.

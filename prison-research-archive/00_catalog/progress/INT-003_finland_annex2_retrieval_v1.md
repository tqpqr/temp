# INT-003 — Finland RISE 2021 decision Annex 2 retrieval audit

**Result: BLOCKED — authoritative Annex 2 was not found in publicly retrievable source material during 14 October 2026 investigation. Do not fill it from conjectures.**

## Document whose missing annex matters
- RISE decision 22 November 2021, docket Dnro 12/280/2021, `Päätös vankipaikkojen valtakunnallisesta jakautumisesta`.
- Genuine seven-page PDF original, now **successfully archived at** `prison-research-archive/03_international/Finland/original_sources/RISE_Dnro_12-280-2021_decision_2021-11-22.pdf`, Git SHA-1 `8431f59ce96bfeeed99fc50a75a8e94e78a717c1`, bytes **134230**, SHA-256 `5937807ed705f3bf522f986e31efa753afbf093f5346ad2d5560da3a1e8aff69`.
- Contemporaneous official RISE release https://www.sttinfo.fi/tiedote/69926272/vankipaikkauudistuksella-vaikutuksia-laajasti-kaikkiin-vankiloihin-erityisryhmille-perustetaan-uusia-osastoja?publisherId=2090 ; publisher-hosted original https://www.sttinfo.fi/data/attachments/00037/3fe38edf-552e-428d-a53c-31b19201c702.pdf .
- **Printed main-decision p1 explicitly explains** that `vankipaikkataulukko (liite 2)` gives planned specified prisoner counts/allocations for each facility, in addition to group-specific places; **p7 explicitly lists Annex 2 `Valtakunnallinen vankipaikkataulukko`**, but only the main seven pages are published in that accessible PDF.
- This is a **planned allocation**, not operational/realised places: decision p5 works from prisoner forecasts and a 90% target occupancy and indicates at-least-annual revision; see MB-036.

## Retrieval and exclusion checks, 2026-10-14
1. The STT public **1 Dec 2021 official RISE announcement** attachment list contains **one PDF**, the main decision, and no separate entry for Annex 2.
2. The original old RISE /material/collections/20211201115130/7VE6s7dyb/... decision PDF is indexed but currently serves a broken/404 response (the earlier repository file saved that error as an HTML blob). The old path is NOT a separate Annex 2.
3. Finnish search of the exact phrase `Valtakunnallinen vankipaikkataulukko`, `vankipaikkataulukko liite`, decision docket `12/280/2021`, and alternative wording `vankipaikkojen valtakunnallinen jakautuminen`, including searches on RISE and STT, found repeated *references to the decision* but not the **actual full facility annex document or a verifiable authoritative version**.
4. The freshly archived seven-page PDF has verified PDF magic and full text by pypdf; its visible page 7 is the annex **list**, not Annex 2 tables. Source p1 explicitly identifies the missing table as a separate annex. The PDF was not modified or expanded.
5. Italy's 189-institute `capienza regolamentare` source and Finnish 2021 statistical annual report cannot stand in for this **specific planned Annex 2**, since concepts and dates differ.

## What remains unknowable without Annex 2
Exact complete planned prison-by-prison values, national sum, subgroup breakdown, effect/implementation dates and revision history. The 18 already catalogued special-unit example rows from the main decision are a **partial subset**, not a valid substitute or exhaustive table. Do not reverse-engineer national total by summing examples.

## Next permitted action
The authoritative register contact printed on RISE decision p7 is **kirjaamo.rise@om.fi**. Prepare request for a complete electronic copy of **Annex 2 to decision Dnro 12/280/2021**, plus later dated amended versions and, if available, implementation-status evidence. Request drafted in `INT-003_finland_annex2_official_request_fi_v1.md`. **No outgoing request or email was sent** in this run. Once original bytes arrive, verify source title/docket/annex metadata and archive original unchanged; keep planned place allocations separate from observed prison capacity. No main indicator registry entry is authorized while Annex 2 absent.

**Task status: BLOCKED_EXTERNAL_DOCUMENT_NOT_PUBLICLY_OBTAINED.** True original main PDF archived successfully; its custody is separately documented in `INT-002_authentic_pdf_binary_preservation_v1.md`.

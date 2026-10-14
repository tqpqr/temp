# Checkpoint v32 — INT-002 DONE with source defect; INT-003 NEXT (2026-10-14)

Last completed first-wave source audit **INT-002**, Finland administrative planned placement decision dated 22 Nov 2021, RISE docket **12/280/2021**. Original archival repository artifact `space-archive/extra/stp8/Finland_Paatos_vankipaikkojen_jakautumisesta_22.11.2021.pdf` is **NOT a PDF**. Git source blob `7007835861b6ee8a6dcae8ef6624cdb5bb8c8288` was decoded through GitHub base64, yielded **154203 bytes of HTML 404** titled `Sivua ei löytynyt - Rikosseuraamuslaitos`. Do not pretend this path contains official PDF content. Original untouched.

Independent authentic signed decision linked by **RISE publisher press release 1 Dec 2021**:
- Release https://www.sttinfo.fi/tiedote/69926272/vankipaikkauudistuksella-vaikutuksia-laajasti-kaikkiin-vankiloihin-erityisryhmille-perustetaan-uusia-osastoja?publisherId=2090
- Authentic **7-page PDF** https://www.sttinfo.fi/data/attachments/00037/3fe38edf-552e-428d-a53c-31b19201c702.pdf
- Web extracted all 7 printed PDF pages with page references; **screenshot calls timed out, direct PDF bytes SHA256 not acquired or uploaded to repo**. Publisher PDF is independently linked source, not same Git file.
- PDF p1 planning for 2022–24 and provisional 2024–26; p2–4 specialised ward/site implementation dates; p5 forecast inmate numbers and **90% target institutional occupancy**, review at least annually; p7 enumerates but **does not contain Annex 2** (`Valtakunnallinen vankipaikkataulukko`) listing full facility allocations.
- No actual prison capacity for **2021** and no national 2022–25 operational capacity series can be inferred from these planned institutional allocations.
- 18 source-page-anchored illustrative **planned policy items** separately recorded; no extra main indicator registry observations.

Persisted and fetched:
- `00_catalog/progress/INT-002_finland_capacity_v1.md` page-anchored 7-page narrative audit and original-mislabeled payload finding;
- `00_catalog/progress/INT-002_finland_planned_capacity_policy_items_v1.csv` 18 original institution-specific planned allocations, dates, double-counting flags;
- `00_catalog/progress/INT-002_finland_source_payload_identity_QA_v1.csv` two provenance records: 404 HTML archived blob vs valid external publisher PDF. Publisher PDF bytes not stored;
- `00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v18.csv` **36 cases** (+MB-035, archive MIME/content failure; MB-036 planned 90% capacity allocation not observed). Older MB-011 Italy regulatory capacity and GB MB-030 Baseline CNA measurement differences remain separate.
- `00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v16.csv` **1136** records, unchanged. Do not promote policy target numbers into actual measured prison-year observations.
- `00_catalog/MICROTASK_QUEUE_WAVE1_v27.csv`: **INT-002 DONE**, **INT-003 NEXT**, now 32 tasks total: 26 done or previously reconciled, 4 blocked, 1 waiting and 1 next. No other NEXT.
- Original GitHub source files preserved, all artifacts are new versioned UTF8 text documents.

NEXT INT-003: specifically obtain **Annex 2** to RISE Finland decision docket 12/280/2021, validate official bytes, facility rows, planned/reference/effective dates, changes and checksum. Old RISE static path may now 404; RISE STT 2021 release includes only seven-page decision, not Annex 2. If Annex 2 cannot be found independently, record explicit source availability blocker rather than creating conjectural prison capacity numbers.

Prior checkpoint `SESSION_CHECKPOINT_20261014_v31.md`: RU-004 DONE and binary blockers RU-002/RU-003 etc.

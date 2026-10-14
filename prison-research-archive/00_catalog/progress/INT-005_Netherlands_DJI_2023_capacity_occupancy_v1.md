# INT-005 — Netherlands DJI capacity and occupancy, January–April 2023

**DONE.** Original 14-page DJI source audited, all 53 original facility charts visually inspected and paired by exact name and chart position with 2022 September–December source INT-004. No enquiries or messages to government offices.

## Primary source provenance
- Original immutable GitHub archive: `space-archive/extra/stp8/Netherlands_DJI_capaciteit_bezetting_jan-apr_2023.pdf`.
- Git blob SHA-1 **054f279bd0512d8b3d5e4cf994bcc619d5dbc246**, **738848 bytes**, PDF 1.4, **14 pages**.
- Source SHA-256 **f9c6cc22543343f6505dffc934b8c2ea967d9b1fb8742c05d36b7a2727a8e0a3**.
- Official DJI issued **9 June 2023**. Publisher landing page: https://www.dji.nl/documenten/2023/06/09/capaciteit-en-bezetting-januari-t-m-april-2023 .
- Independent real official publisher PDF file https://www.dji.nl/site/binaries/site-content/collections/documents/2023/06/09/capaciteit-en-bezetting-januari-t-m-april-2023/Capaciteit%2Ben%2Bbezetting%2Bjanuari%2Btm%2Bapril%2B2023.pdf was downloaded again and verified **BYTE-FOR-BYTE IDENTICAL** to preserved original (same byte count and SHA256), via completed one-off GitHub Actions run 38632597942. Both file origins and validation in `INT-005_DJI_2023_original_binary_metadata_v1.json`.
- PDF creation metadata **8 June 2023**, not evidence of a different reporting period or public release date.
- `INT-005_DJI_2023_14p_original_text_v1.md` and `INT-005_DJI_2023_original_layout_blocks_v1.json` retain original page text and raw text-block coordinates. All **14 original PDF pages rendered and checked visually** (source-derived PNG `INT-005_DJI_2023_original_page_01_visual_QA_v1.png` through `_14_visual_QA_v1.png`). No OCR or inferred chart-bar heights used where numeric labels available.

## Actual measurement definitions
The document reports averages for **1 January–30 April 2023**, not daily totals, year-end census, or annual capacity.
- `bezet` (and juvenile/FPC `gem. bezet jan t/m apr`): averaged occupied places in original DJI charts.
- `leeg, direct inzetbaar`: averaged empty places immediately deployable for detainees.
- `buiten gebruik`: out-of-use places, which DJI defines on its own website as closed for repairs, personnel limitations or reserve designation. Not usable operational seats.
- Original labels are rounded displayed whole-place quantities (averages across months); rounding makes derived totals approximate. Empty gray/green segments without printed numbers are **null, not evidence of exactly zero**. Forensic psychiatric FPC charts pp9–11 publish **occupation only**, not deployable capacity.
- As in INT-004, **Veldzicht (GW), p8** uniquely labels **4 places `leeg`** rather than `leeg, direct inzetbaar`; these generic-empty places remain in a separate field, not in immediately available slots.

## Complete data assets
- `INT-005_Netherlands_DJI_2023_53_facility_chart_rows_v1.csv`: 53 original location chart rows with page anchors, original category labels, numbers, missing flags and publication-source SHA. Exactly **31 adult prison/detention sites, 11 forensic clinics, 11 juvenile sites**. No FPC capacity invented.
- `INT-005_DJI_2022Q4_2023Q1_source_facility_bridge_v1.csv`: **53 exact location-name / same PDF page and chart panel matches** to INT-004; preserves both source published period values and conditional deltas for 53 locations, with missing/availability/source footnote safeguards. Same names and PDF positions establish source reporting comparability at display level, NOT verified equivalence of staffing, contract, regime or other latent site state.
- `INT-005_DJI_two_period_comparable_field_QA_v1.csv`: 11 explicit analyst-derived comparative series/counts, each stating number of locations with printed fields in both reports. No unsupported source national aggregate.
- All source original files, image QA, prior records remain unchanged.

## Within-source rounded chart-label sums (NOT publisher national sums)
| Scope | Sites | 2022 Sep–Dec | 2023 Jan–Apr | Delta |
|---|---:|---:|---:|---:|
| All adult/DC/JC **occupied** | 31 | 8837 | 9209 | +372 |
| Matched adult sites with explicit direct-vacant category **occupied** | 30 | 8806 | 9176 | +370 |
| Same 30 sites: **empty immediately deployable** | 30 | 1361 | 1066 | -295 |
| Same 30 sites: **occupied + direct empty** | 30 | 10167 | 10242 | +75 |
| Same 27 adult sites with printed gray numbers in BOTH periods: **out of use** | 27 | 2272 | 2195 | -77 |
| FPC forensic occupancy only | 11 | 1564 | 1599 | +35 |
| JJI juvenile occupancy | 11 | 486 | 502 | +16 |
| Same 10 JJI with both direct-vacant labels | 10 | 84 | 69 | -15 |
| Same 10 JJI occupied+direct-vacant | 10 | 472 | 471 | -1 |
| Veldzicht (GW) generic `leeg`, not direct-vacant | 1 | 9 | 4 | -5 |

For the **30 adult directly comparable charts**, computed occupied/(occupied+immediately vacant) rises **86.61% → 89.59%**, **+2.98 percentage points**. This is an **analyst-derived ratio of rounded four-month-mean source labels**; not DJI-certified national official occupancy percentage, nor a prison financial elasticity estimate. For adult sites with both printed gray labels, out-of-use places fall 77, but a no-gray-label site cannot be assigned zero from silence. Across all 31 adult sites, numeric gray printed-only totals are 2272 vs 2197, a *different source coverage comparison* (27 vs 28 printed gray entries) and should **not** be reported as matched change -75.

## Selected real matched site movement
- **DC Rotterdam p2:** 2022 occupied 357 / immediately empty 113 / out of use 170 → 2023 **432 / 82 / 125**; occupied +75, available capacity +44, out-of-use -45.
- **JC Schiphol p5:** 186 / 150 / 134 → **247 / 78 / 145**; occupied +61, immediately available spare -72, operational-like occupied+immediate empty **-11**. Excluded **24 KMAR places** in both chart notes.
- **PI Grave p2:** 355 / 83 / 29 → **328 / 47 / 91**; occupied -27, directly usable -63, out-of-use +62. May reflect temporary unavailability but publication alone does not establish a particular cause.
- **DC Zeist p2:** 100 / 107 / 163 → **80 / 85 / 205**; occupied -20, usable -42, out-of-use +42.
- **PI Alphen Maatschapslaan p1:** 316 / 22 / 108 → **352 / 14 / 80**; occupied +36, usable +28.
- **PI Zwolle p6:** 275 / 27 / 102 → **312 / 20 / 71**; occupied +37, usable +30.

## Exclusions persist in identical original graph positions
PDF p3 PI Haaglanden–Scheveningen excludes **96 places** for international tribunals; p5 JC Schiphol **24 KMAR**; p7 PI Vught **6 Forzo** and PI Zuid-Oost–Ter Peel **72 JJI**. Preserve exclusions, do not add excluded places to the directly-deployable series automatically.

## Catalogue policy and continuation
- Prior **MB-037** already covers three-state capacity distinction and four-month reporting period; **MB-038** covers mixed adult/FPC/JJI publication, out-of-scope places and `Veldzicht (GW)` ambiguous green caption. Both remain valid in the 2023 edition, so **no additional MB issue was invented**. Global methodology registry stays **v20, 38 cases**.
- `INDICATOR_PERIOD_COVERAGE_REGISTRY_v18.csv` adds **8** Jan–Apr 2023 group×measurement source coverage records with original PDF file/hash and source CSV references, now **1152 source coverage records**. No 53 duplicate national measurements inserted.
- First-wave queue **v30**: INT-005 DONE and no immediately available next task. Out of **34 current first-wave tasks**, **28 DONE or prior reconciled**, **5 BLOCKED** and **1 WAITING_ON_GB-002**, so 6 still unresolved and dependent on missing/binary sources. Do not expand first-wave task count just to avoid declaring the existing bounded wave finished.
- Further public DJI reports exist for May–Aug 2023 and later, but the survey of the *entire* original repository is not complete. If user elects a second wave, inspect at least one source per new geography/fiscal panel and build same-site/time series without falsely merging legal capacity and actively staffed immediate places.

No government or agency contacted.

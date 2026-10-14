# Checkpoint v34 — INT-004 Netherlands DJI original PDF DONE, INT-005 NEXT (2026-10-14)

**Latest completed microtask INT-004; next independent INT-005.** No requests were sent to agencies or registry offices; work used public DJI web materials and original preserved GitHub files only.

## Exact original/publisher proof
- `space-archive/extra/stp8/Netherlands_DJI_capaciteit_bezetting_sep-dec_2022.pdf`, Git blob SHA1 **db2f73de005d37842c06290a0d27b8a83aa8e6cc**, **724073 bytes**, **14 pages**.
- PDF SHA256 **adfa88fcdd993d710944796296e4c07c5dc0532de77ef71b770b3cc7920442d9**. Independently downloaded official DJI PDF URL and compared byte-by-byte to repository original: **BYTE_IDENTICAL True**. File `progress/INT-004_DJI_2022_official_binary_match_v1.txt` and DJI publisher https://www.dji.nl/documenten/2023/01/10/capaciteit-en-bezetting-september-t-m-december-2022, published **10 Jan 2023**. Original PDF internal Excel creation date 6 Jan 2023 is not publisher date.
- **All 14 pages** extracted with direct verified source bytes and individually visually QA rendered. Preserve `progress/INT-004_DJI_2022_14p_original_text_v1.md`, `progress/INT-004_DJI_2022_original_layout_blocks_v1.json`, `progress/INT-004_DJI_2022_original_binary_metadata_v1.json`, plus visual rendered `progress/INT-004_DJI_2022_original_page_01_visual_QA_v1.png` through `_14_visual_QA_v1.png`.

## Source-original measured concepts and chart evidence
- Audit `progress/INT-004_Netherlands_DJI_2022_capacity_occupancy_v1.md`; **53 individual source graphs** preserving original location, original page, originally printed average integer values in `progress/INT-004_Netherlands_DJI_2022_53_facility_chart_rows_v2.csv`.
- PDF pp1–8: **31 adult prison/detention centres** (PI, DC, JC, Veldzicht GW) printed blue occupied sum 8837, directly deployable green vacant 1361, gray out-of-use 2272 (4 no printed gray numeric labels). **Veldzicht (GW), p8** only labels 31 occupied and 9 plain `leeg`, not confirmed immediately deployable; v2 stores generic vacancy separately and excludes it from directly deployable denominator.
- Comparable explicitly classified **30-chart adult subset** occupied 8806 + immediately vacant 1361 = **10167 derived published-rounding four-month average places**; not source-published national aggregate.
- PDF pp9–11: **11 FPC forensic clinics occupation only**, sum occupied 1564; free and unavailable capacity **NOT PUBLISHED** in same FPC charts, so no safe occupancy-rate denominator.
- PDF pp12–14: **11 juvenile institution charts**, occupied sum 486, directly available vacant 86, printed out-of-use 19 (6 unlabelled gray categories); do not include JJI in adult-prison capacity.
- Four original institution exclusions: p3 **PI Haaglanden-Scheveningen 96 international tribunals**; p5 **JC Schiphol 24 KMAR**; p7 **PI Vught 6 Forzo**, **PI Zuid-Oost Ter Peel 72 JJI**. Recorded directly on matching 53-row CSV institution lines. Do not add these to national comparisons uncritically.
- DJI website glossary: `bezet` occupied; `leeg direct inzetbaar` empty immediately usable; `buiten gebruik` out of operation for maintenance, staffing or reserve; all as **Sep–Dec 2022 four-month means, not a year-end census**, https://www.dji.nl/over-dji/feiten-en-cijfers/cijfers-en-publicaties/capaciteit-en-bezettingscijfers.

## Persistent catalog statuses
- `00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v20.csv`: **38 cases**, +MB-037 three-state four-month average capacity concepts, +MB-038 mixed groups, missing FPC denominator, generic empty Veldzicht, source footnote exclusions.
- `00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v17.csv`: **1144 records** (prior 1136 + eight *period × institution-group × original source field* coverage records), not 53 pseudo-national observations. Exact 53 original chart source rows in separate CSV.
- `00_catalog/MICROTASK_QUEUE_WAVE1_v29.csv`: **34 tasks**, INT-004 DONE, INT-005 sole NEXT. 27 done/reconciled, five blocked, one waiting, one next.
- Original archive PDF and prior register versions preserved unmodified; temporary one-off GitHub Actions extraction/raster/byte-comparison workflows are to be removed after successful evidence archiving.

## Next INT-005
`space-archive/extra/stp8/Netherlands_DJI_capaciteit_bezetting_jan-apr_2023.pdf`, original Git tree SHA1 `054f279bd0512d8b3d5e4cf994bcc619d5dbc246` (metadata previously verified); audit original pages, official publisher exact byte hash, source charts, same sectors and footnotes. Only then calculate pairwise Sep-Dec 2022 vs Jan-Apr 2023 facility changes with explicit comparable facility IDs/sector scope. **No official mail requests**.

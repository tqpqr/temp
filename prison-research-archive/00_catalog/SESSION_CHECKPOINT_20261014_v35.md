# SESSION_CHECKPOINT_20261014_v35 — first-wave INT-005 done; 6 blocked/dependent tasks remain

## Latest verified source/task
**INT-005 DONE**. Netherlands DJI original `space-archive/extra/stp8/Netherlands_DJI_capaciteit_bezetting_jan-apr_2023.pdf`, original Git SHA-1 **054f279bd0512d8b3d5e4cf994bcc619d5dbc246**, PDF 1.4 **14 pages**, **738848 bytes**, SHA-256 **f9c6cc22543343f6505dffc934b8c2ea967d9b1fb8742c05d36b7a2727a8e0a3**.

DJI official original PDF published **9 June 2023**, source https://www.dji.nl/documenten/2023/06/09/capaciteit-en-bezetting-januari-t-m-april-2023 , identical to archive PDF **byte-for-byte**; extraction and independent publisher hash preserved in `progress/INT-005_DJI_2023_original_binary_metadata_v1.json`. Direct GitHub source bytes (not re-created PDF) were validated in an isolated one-time GitHub Actions job, source PDF rendered at all 14 pages. All original document bytes and previous analyses kept unchanged.

**Artifacts**:
- `progress/INT-005_Netherlands_DJI_2023_capacity_occupancy_v1.md` original-source report;
- `progress/INT-005_Netherlands_DJI_2023_53_facility_chart_rows_v1.csv`, 53 real issuer-chart rows;
- `progress/INT-005_DJI_2022Q4_2023Q1_source_facility_bridge_v1.csv`, 53 exact location-name and identical page/chart-position paired comparisons to INT-004;
- `progress/INT-005_DJI_two_period_comparable_field_QA_v1.csv`, 11 explicitly paired analytic subseries;
- `progress/INT-005_DJI_2023_14p_original_text_v1.md`, `progress/INT-005_DJI_2023_original_layout_blocks_v1.json` and fourteen `INT-005_DJI_2023_original_page_XX_visual_QA_v1.png` image evidence (01–14).

## Key measurement results (source published display values)
**31 adult/DC/JC location plots** repeated exactly by source name/page panel. All adult occupied sum of rounded 4-month means **8837 → 9209** (+372), but **Veldzicht (GW)** publishes 9 → 4 generic `leeg` without explicitly stating directly deployable. Its occupied values 31 → 33 should be segregated from the 30 strict subset. The **30 valid paired adult charts** have occupied **8806 → 9176** (+370), immediately deployable vacant **1361 → 1066** (-295), derived occupied+vacant **10167 → 10242** (+75), occupancy-proxy **86.61% → 89.59% (+2.98 pp)**. Treat as sums/ratios of rounded publisher 4-month means, NOT official national totals or site-day exposure.

Among **27 adult sites with both out-of-use categories numerically printed**, out-of-use **2272 → 2195** (-77). Summing all *printed* gray labels gives 2272 → 2197, but 2022 has 27 printed and 2023 28; this is NOT the same panel and must not be called a -75 change without qualification.

**11 forensic FPC centres** print average occupied only: **1564 → 1599** (+35), NO directly-usable capacity denominator in publisher graphs. **11 juvenile JJI sites** printed occupied **486 → 502** (+16), but one location loses printed vacant-green figure in 2023; matched **10 JJI** comparable direct-vacant **84 → 69** (-15), derived capacity **472 → 471** (-1). Publisher blank ≠ numeric 0.

Four original source scope exclusions in both periods: PI Haaglanden Scheveningen 96 international tribunals, JC Schiphol 24 KMAR, PI Vught 6 Forzo, PI Zuid-Oost Ter Peel 72 JJI. UK Baseline CNA, Italy regulatory capacity, Finland planned places are distinct concepts from DJI immediately deployable places and time means. See MB-037/038, **no new MB issue**.

## Current primary registries
- `00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v18.csv`: **1152** original indicator/period source coverage records, +8 Jan–Apr 2023 DJI family×field categories beyond v17=1144. Do not add each chart as fake source-published national total.
- `00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v20.csv`: **38 existing cases**, unchanged; MB-037/038 apply to both DJI periods. No invented new break ID.
- `00_catalog/MICROTASK_QUEUE_WAVE1_v30.csv`: **34 tasks total**, **27 DONE + 1 DONE_PRIOR_AUDIT_RECONCILED = 28 complete/reconciled**, **5 BLOCKED**: GB-002 (missing publisher revised XLSX), RU-001 (XLS binary unreadable), RU-002 (K3 legacy XLS binary unreadable), RU-003 (budget 7z binary unreadable), INT-003 (Finnish RISE decision annexes missing); **1 WAITING_ON_GB-002** GB-003. **No NEXT task in this deliberately bounded first-wave queue**. The 6 unresolved are source-access dependencies, not concealed incomplete audits. Broad repository cataloguing is **not complete**: 34 queue tasks are a working wave, not an exhaustive inventory of every original repository object.
- Temporary read-only one-off GitHub Actions helper workflow `.github/workflows/oneoff-dji-int005.yml` can be removed once all saved artifacts are inspected and verified.

## Next potential work — not an added task
If a **second wave** is authorized, independently inspect another new source/period such as DJI May–Aug 2023 and build a three-period matched 2022–23 capacity/presence panel, or prioritize unclassified files already present in repository. Do not treat sourcing blocked tasks as DONE and do not request documents from government authorities. Preserve original archive files and add-only versioned catalogues.

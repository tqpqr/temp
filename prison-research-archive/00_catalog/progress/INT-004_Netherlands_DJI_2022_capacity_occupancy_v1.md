# INT-004 — Netherlands DJI, September–December 2022 PDF source audit

**DONE — source verified and 14/14 pages inspected.** DJI published on **10 January 2023** a 14-page PDF of mean occupied, directly deployable vacant, and out-of-use places by location for **Sep–Dec 2022**. This is a 4-month mean, not a point-in-time or full-year capacity census.

## Source integrity
- Original: `space-archive/extra/stp8/Netherlands_DJI_capaciteit_bezetting_sep-dec_2022.pdf`
- Git SHA1: `db2f73de005d37842c06290a0d27b8a83aa8e6cc`; bytes: **724073**.
- SHA256: `adfa88fcdd993d710944796296e4c07c5dc0532de77ef71b770b3cc7920442d9`.
- Official landing: https://www.dji.nl/documenten/2023/01/10/capaciteit-en-bezetting-september-t-m-december-2022
- Exact official PDF: https://www.dji.nl/site/binaries/site-content/collections/documents/2023/01/10/capaciteit-en-bezetting-september-t-m-december-2022/Capaciteit%2Ben%2Bbezetting%2Bseptember%2Bt-m%2Bdecember%2B2022.pdf
- **Independent byte comparison against live DJI original: identical** size and SHA256. See `INT-004_DJI_2022_official_binary_match_v1.txt`. PDF original metadata generation date 6 January 2023 is not the publication date.
- Exact Git blob verified before extraction. PyMuPDF text/layout extraction saved in `INT-004_DJI_2022_14p_original_text_v1.md`, `INT-004_DJI_2022_original_layout_blocks_v1.json`. **All 14 pages rendered and visually checked**; image QA files `INT-004_DJI_2022_original_page_01_visual_QA_v1.png` through `_14_visual_QA_v1.png`.

## Verified source categories and coverage
The publisher explains `bezet` = occupied; `leeg, direct inzetbaar` = empty but immediately usable; `buiten gebruik` = out-of-use due to repair, staff shortages or reserves. Publisher definitions: https://www.dji.nl/over-dji/feiten-en-cijfers/cijfers-en-publicaties/capaciteit-en-bezettingscijfers .

[**53 original source chart rows with exact PDF page and original printed values**](INT-004_Netherlands_DJI_2022_53_facility_chart_rows_v2.csv), NOT a single homogeneous prison population:
- PDF pp1–8: **31 adult prison/detention-centre location charts**, printed occupied total 8837, printed direct-vacant total 1361, printed unavailable total 2272. Four unavailable grey categories not numerically labelled. Special p8 **Veldzicht (GW)** prints 31 occupied and **9 only `leeg`**, NOT expressly directly deployable. Those 9 are in `generic_empty_leeg_reported`, not direct-vacant.
- PDF pp9–11: **11 forensic clinic FPC charts**, printed occupied sum 1564; **NO vacant or out-of-use capacity data** published for these clinics. Cannot derive occupancy percentage.
- PDF pp12–14: **11 juvenile JJI/location charts**, printed occupied sum 486, direct-vacant 86, out-of-use 19; six grey unavailable values not printed as numbers. Not adult prisons.
- Summed rounded chart labels are **analyst-derived descriptive sums, not published DJI national totals**. Do not treat unprinted bars as recorded numeric zeros.
- Strictly using 30 adult chart locations with explicit immediately deployable category: occupied = **8806**, vacant/direct = **1361**, sum = **10167** average places; Veldzicht GW separately records 31 occupied + 9 generic empty. Not daily usable place-days.

## Publisher-specified exclusions (do not silently add)
- PDF p3 PI Haaglanden–Scheveningen excludes **96** international tribunals places.
- PDF p5 JC Schiphol excludes **24** KMAR places.
- PDF p7 PI Vught excludes **6** Forzo places; PI Zuid-Oost–Ter Peel excludes **72** JJI places.
- All four source page footnotes are attached to the correct original institution rows in **v2** CSV.

## Analytical gates and registers
- **MB-037**: four-month average of occupied/direct-vacant/unavailable statuses differs from Britain fiscal Baseline CNA, Italy regulatory capacity and Finnish planned seat targets. Unavailable is not usable capacity.
- **MB-038**: mixed chart scopes (31 PI/DC/JC, 11 occupancy-only FPC, 11 juvenile), Veldzicht generic vacancy, four exceptions for excluded places, unprinted grey segments.
- New methodology registry `METHODOLOGICAL_BREAKS_AND_ANOMALIES_v20.csv` = **38** cases.
- New indicator-period coverage registry `INDICATOR_PERIOD_COVERAGE_REGISTRY_v17.csv` = **1144** source coverage rows (+8 sector/type categories), with original values held in the 53-row chart source CSV instead of 53 duplicate national observations.
- Original PDF unchanged. The source does not give a single total across comparable institution/capacity definitions.

**NEXT INT-005**: review exact original `space-archive/extra/stp8/Netherlands_DJI_capaciteit_bezetting_jan-apr_2023.pdf` (Git SHA `054f279bd0512d8b3d5e4cf994bcc619d5dbc246`); compare site definitions and periods only after each source is independently verified.

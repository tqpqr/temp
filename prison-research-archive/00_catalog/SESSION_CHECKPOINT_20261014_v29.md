# Checkpoint v29 — GB-018 DONE, GB-019 NEXT (2026-10-14)

**Last actual fully completed microtask: GB-018. Next GB-019 UK prison-cost method and revision crosswalk.** Previous checkpoint v28 and active index v29 kept. All original archive binaries remain unchanged.

## GB-018 original and independently inspected publication
- Original `GB/costs-prison-place-costs-prisoner-2019-2020-summary.pdf` verified in GitHub, Git SHA-1 `4c306371727a0d0354546b418e8f19fbc0533ec6`. 5-page MoJ/HMPPS official PDF, cover published **29 October 2020**, England and Wales FY2019/20.
- Official publisher PDF `https://assets.publishing.service.gov.uk/media/5f96b7c2e90e077b054f58d8/costs-prison-place-costs-prisoner-2019-2020-summary.pdf`. All 5 pages read from publisher, screenshots p1–p5 examined. Exact binary publisher-vs-repo SHA256 match **not verified**, and Git blob SHA1 is not a publisher byte hash.
- Detailed page report `00_catalog/progress/GB-018_2019_20_pdf_v1.md` (verified Git blob SHA `4ad2b03499350b46d5757cdc3434a51759229fc5`).

## Direct findings and checks
- Table 2a, PDF p3: FY2019/20 CNA **79,232**, 12-month-end average prisoners **82,890**, direct GBP **2,401,640,556**, overall GBP **3,536,900,071**. FY2018/19 originally direct **2,162,543,754**, overall **3,404,055,441**.
- Existing **MB-004** verified directly: 2018/19 education/training expenses GBP **129,111,488** moved from HQ to prison direct costs; 2018/19 restated direct = **GBP 2,291,655,242**, overall unchanged. Sector adjustment = public **118,006,171** + PFI **1,865,739** + Operate & Manage **9,239,578**. GDP deflator **2.4%** (ONS 2020-09-30) is a **subsequent distinct correction**: restated real comparative direct GBP **2,347,643,607**, overall **3,487,221,310**; FY2019/20 change +2.3% real direct, +1.4% real overall.
- `progress/GB-018_2019_20_summary_arithmetic_QA_v1.csv`: **23 checks; 22 exact PASS, 1 REVIEW**. Sole review sector FY2018/19 populations **82,750** sum of printed rounded components, Table 2a source **82,751**; one-person source rounding gap, not established source error.
- **New MB-033**: PDF p4 Table 2b `Total (as per Table 2a), FY2018/19 Totals` prints four national per-unit costs **18,726; 16,113; 25,380; 21,839**, exactly duplicating FY2018/19 Operate & Manage sector row. Correct national values in *same PDF* p3 Table 2a **27,453; 26,133; 43,213; 41,136**. This is four confirmed mis-filled national cost cells, cannot be rounded differences. Exact 4-cell forensic in `progress/GB-018_2019_20_table2b_2018_19_total_paste_QA_v1.csv`. Original printed values retained, direct sector sums still correct. Do NOT consume wrong FY2018/19 Table2b national unit rates.
- Existing **MB-005** Birmingham prior public/contracted operator-period split survives from original 2019/20 detailed ODS; summary PDF does not itself document prison-by-prison operator bridge. Do not read O&M total decline as synonymous with Birmingham.
- Previously registered MB-010 and MB-030 public/private comparability and Baseline CNA/12-month-end mean definitions remain. No extra duplicates.
- FY2019/20 national values already in `INDICATOR_PERIOD_COVERAGE_REGISTRY_v16.csv` 1,136 entries (e.g. R01003 direct and R01004 overall from audited supplementary). Do not reinsert as new source-year facts.

## Persistent output and next step
- `00_catalog/METHODOLOGICAL_BREAKS_AND_ANOMALIES_v16.csv`: **33 total cases** (+MB-033), verified SHA `c847656b7c01ef0b8d1e28e5d728592be6c3f980`.
- `00_catalog/MICROTASK_QUEUE_WAVE1_v24.csv`: **GB-018 DONE**, **GB-019 NEXT**, verified SHA `a538667ed10b4fd5377c44dffff0fb153515733e`.
- `00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v16.csv`: 1,136 unchanged.
- All created assets GitHub-verified by fetch_file, originals unchanged.

**NEXT GB-019**: synthesize GB-001 through GB-018 narrative/financial definitions, exact published vintages and restatements (MB-004 / 008 / 029 / 031 / 032 / 033) and cost/denominator crosswalk, retaining multiple sources and ambiguity **without generating a harmonized prison panel** or duplicating source indicators.

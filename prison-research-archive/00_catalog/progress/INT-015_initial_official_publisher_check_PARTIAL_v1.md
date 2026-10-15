# INT-015 — initial official publisher source check (PARTIAL, not DONE)

2026-10-15. Expected archival object: `space-archive/extra/stp8/Scotland_AuditScotland_SPS_2022-23_s22.pdf`, Git blob SHA1 `7e993349b17c6ec0f177862134091092ea86f18e`, archived size 1,107,330 bytes. **Original archive PDF binary has not yet been fetched / byte-compared in this stage. Do not assert identical publisher PDF or mark DONE.**

Independent issuer report: Audit Scotland, Auditor General for Scotland, *The 2022/23 audit of the Scottish Prison Service*, section 22 report, issued December 12, 2023; publisher PDF 21 physical pages: https://www.audit-scotland.gov.uk/uploads/docs/report/2023/s22_231212_scottish_prison_service.pdf . This is a plausible corresponding original; independent binary equality is pending.

Issuer PDF physical p5 paragraph8: FY2022/23 spending GBP499m **including** capital expenditure GBP70.9m; staff costs GBP221.7m, staff establishment 4,562. Do not add CAPEX to total, do not assume all staff costs apply to prison guards.

Physical p4 key messages and p14 para40: FY2022/23 **average prison population 7,426**, FY maximum 7,583; period is Scottish financial year, not calendar 2022 and not December snapshot. Historical 2013/14–2022/23 average 7,653 (ten-year aggregate). Highest FY average 2019/20 8,198 and maximum 8,336.

Physical p14 paras41-42: 2023-11-13 prisoners 7,948; 2023-11 target capacity 8,007, *extended operating capacity* 8,475 (different operational/restricted-regime concepts). Forecast 8,166 for March 2024 — **forecast only**, never put into observations. Five prisons above target 2023-11-02.

Physical p5 para5: 15 directly managed prisons and 2 PFI prisons, not 15 total institutions. Physical p17 para48: March 2023 avg 2,368 persons /31.5% accommodated in shared double cells: NOT a bed capacity measure. Physical p18 para51: Barlinnie design capacity 987, 2022/23 avg occupancy 1,235, 2023-11-13 occupancy 1,406. Those have different time grains.

Physical p12 para30: >GBP4m cumulative escort contractor service credits 2019/20–2022/23, not annual prison spending; p13 para32 additional contract costs projected GBP1.8m FY2023/24 and GBP2.2m annually thereafter, not observed FY2022/23. Physical p18 para57 Glasgow capital cost estimate GBP100m 2014, GBP387.6m October2019, later unquantified increase; estimates not actual CAPEX.

Further steps before closing INT-015: obtain exact archived 1,107,330-byte PDF via a binary-capable workflow and check SHA1, compare its length/hash with publisher PDF; inspect chart Exhibits 1–5 visually against source text; reconcile all useful observations with registry v27 and existing MB IDs, add new records only after exact source verification; update registry/MB/queue/checkpoint/index atomically or with tracked commits. No government correspondence.

# Russian source/date semantics and16 residual groups: stage2

Previous [stage1](RU-MB034_source_separation_stage1_v1.md) is retained unchanged. Read the7-page dataset description from original fsin/description_fsin_info_103_v20240626.pdf, particularly pp3–7. This is compiler documentation, not an independent endorsement of every source value.

## Source and date meanings

Six labels are explicitly defined on p4; see source-label dictionary with counts. `fsin_report2` occurs11 times but is not defined. Composite labels retain both sources; do not infer a preferred issuer. `year` means reporting year, `data_date` date of relevance, `data_date_t` its text representation (p3).

On p5 the compiler says short observations are at the first day of publication month and January1 is assigned to the preceding reporting year. It describes od/stat counts as year-end, but the six recovered od snapshot files below contain no internal reference date. Do not force this general statement onto all od records. The phrase describing year-end as an average also needs care: it does not authorize treating every stock as an annual mean.

Documentation inconsistencies: p5 calls Rosstat values year-end but then says31 January; the actual disputed rows label31 December. Retain the discrepancy without silent correction. The stated coverage2005–2023 omits532 source rows before2005 (actual nominal bounds1995–2023). The metadata says no missing rounded values, whereas the XLSX has3 blanks. These are documentation limitations, not reasons to change source data.

## Fourteen od2020 groups traced to original-form CSV files

Downloaded the two archives linked on p7. Both are RAR5 despite the description calling the first ZIP. Preserve exact downloaded bytes, SHA256 and compiler-hosted provenance. Only selected six od CSVs are additionally unpacked for inspection; no claim of independent current FSIN-hosted byte identity.

The six files in archive member directory05_statistics carry the same20200717 date and different times:0843,0859,1052,1108,1157,1212. All 63 disputed source rows across14 groups have matching subject/value evidence in those files. The crosswalk has 84 candidate links because repeated values can occur in multiple files. A match does not prove a unique file assignment. The source workbook has lost this file-level distinction.

These files have17 column headers and one value record. They contain no explicit observation-period field. Therefore file provenance is now recovered, but chronology and true reference dates remain OPEN. Do not interpret filename times as observation times or label the six values as six revisions of one point. Do not infer January–June solely from declining prison totals.

## Two Rosstat2012 groups remain unresolved

Y808000050:2293 vs2289; Y808000074:2180 vs2176. Both pairs differ by4; both total-minus-men combinations equal113. Arithmetic consistency cannot choose between them. Secondary search results reproduce2289/2176 but do not establish the edition/cells for both variants. The official publication catalogue https://www.rosstat.gov.ru/folder/210/document/13212 was reachable in search indexing but direct/web retrieval returned502/timeouts during this check. Neither pair is selected as canonical.

## Decisions

MB-034 remains open for annual canonical selection;14 groups now have recovered file-level provenance and2 require Rosstat edition tracing. New MB-109 records documentation/date ambiguity. Indicator registry v36 remains current (REGISTRY_UNCHANGED): no new numeric indicator or period is promoted; this sidecar supplies provenance for already covered rows. Old files and original values retained. Next evidence needed: od dataset passport/version metadata with observation dates, and Rosstat2013/2014/2015 original tables for2012.

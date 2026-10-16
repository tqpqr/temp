# GB-002 / GB-003 — official restated FY2015/16 workbook recovered

Checked2026-10-16. Repository not modified during this investigation.

Official release: https://www.gov.uk/government/statistics/prison-performance-statistics-2016-to-2017 , Ministry of Justice, 26October2017. Explicitly lists FY2015/16 restated establishment tables.
Downloaded via HTTPS with certificate validation, HTTP200:
https://assets.publishing.service.gov.uk/media/5a82f0f140f0b62305b9523d/costs-per-prison-place-per-prisoner-by-individual-prison-2015-2016-restated-tables.xlsx

Restated file:94217 bytes; SHA256 d6917220c8f78beb69c5a612719cb868808aef9317894bbc095a703f5d37b415; Git blob SHA1 3b1b37ebf5195019e1ccda45b013ec58fd30ea1c. XLSX opens, six worksheets. Source bytes preserved as restated_2015_16.xlsx.
Original archive path: GB/costs-per-place-cost-per-prisoner-individual-prison-establishment-2015-16_tables.xlsx;89232 bytes; Git blob SHA1 09ae7bb2b1455657015f7203fdc7ea7eb283d707. Downloaded from repository main on check date; source bytes retained as original_2015_16.xlsx. No original overwritten.

## Main comparison

Restated T2_Summary Comparison!A6 identifies transfer of education and training provision from DoE. H6=120390295 GBP. H5=2753747261 original overall resource expenditure; H7=2874137556 restated. Exact identity H7-H5=H6. Direct resource expenditure D5=D7=1897972242; D6=0. This is a publication-vintage accounting-scope change for the same FY, not observed year-on-year growth.

Both T3 sheets contain119 named establishment accounting rows with identical name sets. Matched by exact source name after verifying uniqueness; source physical row addresses retained in CSV. Eight numeric fields compared: CNA, average population, direct expenditure, direct unit costs, overall expenditure, overall unit costs. Cached source values read; source formulas not recalculated.

CNA unchanged for all119. Direct expenditure unchanged for all119. Overall expenditure changes in97;22 unchanged. Sum of establishment expenditure deltas120390294 GBP vs national120390295: difference1 GBP. Publisher explicitly states totals formed from unrounded figures; difference is compatible with rounding, not proof of a missing institution. Do not force-reconcile the source by changing a value.

T1 national unit costs: overall per-place35182->36720 GBP; per-prisoner32510->33931 GBP. National CNA78271 and population84705 unchanged. Unit cost increase around4.4% is revision of the same FY accounting perimeter.

## Blank-to-zero source revision

Blantyre House and Downview: original population and four unit-cost fields blank; restated values0 (10 cells). Notes to T3 note2 says these establishments were undergoing conversion, excluded from calculations although CNA and expenditure retained in aggregate data. Preserve old blanks and new published zeros as distinct source encodings; no invented numeric delta for blank-to-zero. Zero unit costs must not be used as real operating cost estimates. No causal claim about actual population change from this encoding revision.

## Scope and next catalogue integration

GB-002 byte retrieval blocker resolved locally; official binary ready for a new additional-source path. GB-003 paired numeric comparison completed for all119 T3 rows and national revision bridge. This is not a full audit of every cell, formula, formatting difference, or budget category. Does not resolve other service-concession category breaks.

Next integration should archive official binary unchanged, append indicator vintage observations, update MB-008 retrieval blocker and MB-031 restatement evidence while retaining IDs, and link the blank/zero clarification to existing MB-007 if its scope matches. Read current ledgers before assigning any new MB ID. Full catalogue updates and protocol publication closure not performed in this package.

Evidence: GB-003_2015_16_establishment_vintage_diff_v1.csv; GB-003_checks.json; both source workbooks. Blank differences are deliberately not assigned arithmetic deltas.

## Catalogue integration
Official XLSX archived at prison-research-archive/02_uk/additional_official_sources/FY2015_16_restated/costs_2015_16_restated.xlsx. MB-008 resolved; MB-031 supplemented; MB-108 records FY2015/16 blank-to-zero revision (MB-007 concerns a different year/site and remains unchanged). Registry v35 appends eight restated field-coverage objects over119 source rows; national totals already represented in earlier evidence are not duplicated. Queue pending publication verification.

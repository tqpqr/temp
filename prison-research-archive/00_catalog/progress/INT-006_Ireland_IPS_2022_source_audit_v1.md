# INT-006 — Ireland Irish Prison Service prisoner population and bed capacity, 31 January 2022

**DONE** — first original-source audit in second wave, one PDF page, 13 main institution/gender reporting rows plus 3 non-additive Portlaoise blocks and one national totals line, all directly checked in the original rendered page.

## Original identity, publication and exact scope
- Original `space-archive/extra/stp8/Ireland_IPS_Prisoner_Population_31-Jan-2022.pdf` Git blob SHA-1 **3f685dc0557616e8dc27ad04646fb9c900b1fb3b** and **21354 bytes**, PDF 1.5, **one page**, rendered visually at 1.7×; exact page source extraction and text-block geometries preserved.
- Independently calculated SHA-256 **d28146b9533419dd66bdb5ac0205dd48c8ee151abee876bcf471aacbe3720b9d**. Excel-generated PDF metadata: 31 Jan 2022 16:56 UTC, author `cxmcauley`. This creation date is NOT separately verified public posting date.
- Public Irish Prison Service issuer PDF https://www.irishprisons.ie/wp-content/uploads/documents_pdf/31-January-2022.pdf appears in its official 2022 daily prisoner-population index https://www.irishprisons.ie/information-centre/statistics-information/2015-daily-prisoner-population/2022-prison-population/ and reproduced exact matching text. An independent second GitHub Actions download of issuer URL yielded **byte-identical** 21354-byte PDF and SHA-256 matching the archive. **Transport caveat**: initial HTTPS request failed server certificate chain validation, and second retrieval used a context disabling *issuer TLS certificate validation*. Thus exact received bytes match and official index links to this URL, but independent secure issuer transport is not asserted. Evidence `INT-006_Ireland_IPS_2022_publisher_binary_comparison_v2.json`; failed stricter attempt `_v1.json` preserved.
- All rows and original percentages [INT-006_Ireland_IPS_2022_original_prisoner_capacity_rows_v1.csv](INT-006_Ireland_IPS_2022_original_prisoner_capacity_rows_v1.csv), 17 original source table lines including 13 top-level institution/gender lines, three nested Portlaoise A/C/E Block lines and one national publisher Totals row, with exact page anchor and blanks preserved. Original source PDF unchanged.
- Exact one-page source material `INT-006_Ireland_IPS_2022_original_text_v1.md`, `INT-006_Ireland_IPS_2022_source_page_blocks_v1.json`, [original page visual](INT-006_Ireland_IPS_2022_page_01_visual_QA_v1.png), and `INT-006_Ireland_IPS_2022_original_binary_metadata_v1.json`.

## Verified *publisher national figures* at the precise day 2022-01-31
| Published header | Exact original total | Concept and arithmetic |
|---|---:|---|
| Number in Custody | **3835 people** | Physical in-prison population; numerator for printed occupancy percentage |
| Date to Date TR | **5 people** | 1 Loughan House, 4 Shelton Abbey; structured day-to-day temporary release |
| No. On Temp Release* | **262 people** | Broader temporarily released persons, includes 5 structured TR listed in separate type table; DO NOT add DTD to it |
| No. On Trial/Remand | **825 people** | Subset of prisoner custody/legal status; not a separate additive inmate stock |
| Total Prisoners in System** | **4257 people** | Includes prisoners in custody, temporary release, hospital/CMH and lifers in community, **not physical occupied beds** |
| Bed Capacity | **4375 beds** | Issuer-labelled same-day bed capacity; not independently proven identical to UK CNA, Dutch direct-deployable capacity, or Italy regulatory capacity |
| % of Bed Capacity | **88%** | 3835/4375=87.66%, rounded to whole source percent. NOT 4257/4375 |

**Six out of six source numeric totals** exactly reproduced from 13 main reporting lines, excluding nested Portlaoise blocks. Within Portlaoise three blocks: custody **27+157+18=202**, released **0+4+0=4**, remand **0+0+11=11**, total-system **27+162+18=207**, bed capacity **40+181+70=291**, plus date-to-date TR blank or zero by source; all six original parent fields reconcile. Six temporary release types **0+77+40+5+38+102=262**, exactly matching source release total. All arithmetic checks and exception rows in [27-row arithmetic and nested-block QA](INT-006_Ireland_IPS_2022_arithmetic_and_nested_block_QA_v1.csv): **25 PASS, two specifically flagged source-% reviews**.

## Two exactly reproducible source-percentage exceptions — MB-039
The original file prints:
- **Loughan House** p1: **97 custody / 140 beds = 69.2857%**, ordinarily rounds to **69%**; issuer original prints **70%** (difference **+1 percentage point** from nearest integer).
- **Shelton Abbey** p1: **77 / 115 = 66.9565%**, ordinarily rounds to **67%**; issuer original prints **70%** (difference **+3 percentage points**).
All remaining 11 top-level institution/gender source printed percentages, and the national total, match nearest-integer custody/bed quotient, including **Limerick (f): 29/28 = 104%** as actually printed. Both unusual institutions are **open centres**, but the cause of the uniform printed 70% is **NOT VERIFIED**; could be another operational/reporting rule rather than mistake. Preserve original 70% fields and separate computed quotients, do not silently overwrite. New **MB-039** documents this exception.

## Scope and nesting — MB-040
- The publisher distinguishes **in custody 3835** from **in system 4257**. Difference is 422 persons, of which 262 are recorded as temporarily released; the arithmetic remaining 160 cannot independently be attributed to a single subclass because the source provides only its categorical inclusion definition (hospital/CMH, lifers in community), not a complete source breakdown. Do not infer a new exact hospital count.
- `No. On Trial/Remand=825` is an included legal-status breakdown, not 825 additional people to add to custody. `Date to Date TR=5` also appears as structured release category in the 262 total, not independent persons to double count.
- Portlaoise red `A Block`, `C Block`, `E Block` source rows are children of Portlaoise parent. Summing these together with Portlaoise source parent doubles that institution; they are deliberately labelled `NESTED_BLOCK_NOT_ADDITIVE` in source-extract CSV.
- Bed capacity 4375 is issuer's `Bed Capacity` as of one day, **not** a four-month mean; it is semantically distinct from Finland planned 90%-occupancy allocation, Italian regulatory facility snapshot and DJI four-month occupied/direct-vacant/closed. No source-cell evidence of beds currently staffed vs licensed, so do not assume one. **MB-040** captures correct measurement grains and nested/non-additive records.

## Main catalogue changes and status
- [Indicator-period registry v19](../INDICATOR_PERIOD_COVERAGE_REGISTRY_v19.csv): **1160** source-coverage entries (prior v18 1152 plus eight verified Irish source fields/date with original exact national numeric values). These are eight source *indicator descriptors*, not an assumption of eight annual observations. The 17 source rows retain all raw institution values separately.
- [Methodological register v21](../METHODOLOGICAL_BREAKS_AND_ANOMALIES_v21.csv): **40** cases (prior 38 + MB-039 and MB-040). Definitions/percent interpretation not deduplicated.
- Bounded [second-wave stp8 queue v2](../MICROTASK_QUEUE_WAVE2_v2.csv): INT-006 DONE, INT-007 NEXT (original `LaikomuAsmenuStatistika.csv`), 13 other source files still PENDING; 15 scoped tasks total. Original first-wave queue v30 unchanged with five blocked and GB-003 waiting; do not confuse two queues.
- Original repository metadata listing of 19 stp8 blobs with 4 previously audited and 15 originally remaining in [wave2 source manifest v1](../MICROTASK_QUEUE_WAVE2_STP8_SOURCE_MANIFEST_v1.csv).

**Next:** `INT-007` source `space-archive/extra/stp8/LaikomuAsmenuStatistika.csv`, exact Git SHA-1 `acd029c2f0975ec123007889e0e8cfd274d401f1`, **63903 bytes**. Determine actual Lithuanian geography/data date/CSV encoding and substantive indicator definitions; do not assume merely from source filename or conflate prison custody with population-in-system.

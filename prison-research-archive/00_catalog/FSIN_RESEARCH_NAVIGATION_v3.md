# Research-oriented index to FSIN raw series — v3

## Main task
Find stock, capacity, sentencing and prison-labour series quickly in the original 7,227-row FSIN workbook `fsin/data_fsin_info_103_v20240627.xlsx`. Use `fsin_research_series_v3.csv` as a curated index and `fsin_indicator_dictionary_v3.csv` as the exhaustive 302-row code/name-variant index.

**No original statistics have been transformed**. Source Excel row positions remain in place; look them up by the original `indicator_code`.

## Research workstreams

### Transformation of prison labour
- Institutional production landscape: Y808000158–165 (enterprises; industrial/agricultural enterprises; workshops; labour adaptation centres; unitary enterprises).
- Production economic output: Y808000166–167 (volume, profits; check original currency, prices and revisions).
- Work participation: Y808000168–170 (paid labour, housekeeping inclusion choices), Y808000171–172 (production inside institutions versus on third-party premises), Y808000173–174 (productivity-norm and housekeeping work).
- Different bases are **not assumed additive**. Compare definitions and dates in the separate FSIN description before constructing shares or ratios.

### Penal substitution versus confinement
- Y808000001 and Y808000003 are national prison/colony system stocks.
- Y808000080, Y808000081, Y808000083, Y808000085 refer to forced/correctional/mandatory labour as types of punishment or registrations; **not** prison production staffing. Do not conflate with Y808000168–174.

### Capacity, staffing and public spending
- Y808000205–210 explicitly relate to authorised **staffing establishment**, not observed FTE or headcount. Differences versus prison workforce should not be interpreted as realized wage-bill elasticity.
- Y808000133, 137, 140 are limits for selected institution families, not a universal direct equivalent of British CNA/operational capacity or SPACE regulatory places.
- The 2023 entries Y808000300 and Y808000301 explicitly say **excluding new territories**; any cross-year boundary harmonisation must flag this. The broader system totals may have different boundaries, which must be assessed.

## Important QA

- The underlying FSIN workbook actually includes nominal years back to 1995 (29 year labels through 2023). Its aggregator's front-page description gives 2005–2023; the difference needs source date interpretation, not silent truncation.
- 100 of the 300 indicator codes have repeated nominal years. Two codes have multiple distinct labels/hierarchy combinations; see `fsin_verified_quality_checks_v3.md`.
- Original `data_source` and `data_source_2` labels distinguish historical FSIN publications and aggregations. Inference requires source-specific verification of the definitions and units.

## Provenance

Collection: https://tochno.st/datasets/fsin_info . Secondary compilation by «Если быть точным», from FSIN official materials, Rosstat and archived sources. The unit of observation for this compilation is **the FSIN national system**, not one prison facility.

Next stage: derive source-faithful year×indicator tables with **original row ID**, separate `year` vs `data_date_t`, `rounded`, citation text, and explicit rules for selecting (not silently collapsing) competing yearly observations.

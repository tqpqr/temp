# Prison research archive — active index v9 (14 October 2026)

## New: indicator × period coverage and evidence grade

- **[UNIFIED INDICATOR–PERIOD COVERAGE REGISTRY v1 (856 rows)](00_catalog/INDICATOR_PERIOD_COVERAGE_REGISTRY_v1.csv)**: one queryable master list of 302 Russian FSIN code-period ranges, 503 annual/half-year Russian judicial *form-presence* records (NOT numerical indicator values), 38 earlier variable-dictionary records with their original evidence grades, 8 audited British facility cost series fields, and 5 dated UK workforce source-sheet summaries. Counts are **not additive comparable series**.
- **[Registry user guide / quality protocol](00_catalog/INDICATOR_PERIOD_COVERAGE_GUIDE_v1.md)**: defines exact period lists vs first/last nominal bounds, data existence vs file presence, original source links, numerator/denominator/source-vintage issues, not-yet-reviewed areas.
- Important: FSIN 302 code entries give first/last nominal years and count of distinct nominal years, **not a guaranteed gap-free series**. Judicial 503 entries confirm the presence of filenames/forms in annual or H1 collections, **not numerical form fields**. The original 189 UK monthly bulletins, many SPACE documents, and most budget/year/region variables still lack audited variable-by-month/country availability matrices.

## Current work queue and recovery

- [Atomic-task protocol](00_catalog/MICROTASK_PROTOCOL_AND_QUEUE_v1.md) and [latest historical task status snapshot v2](00_catalog/MICROTASK_QUEUE_WAVE1_v2.csv).
- [Checkpoint v4](00_catalog/SESSION_CHECKPOINT_20261014_v4.md) tracks the new unified coverage registry. Resume **RU-001** (single `sud/2024 год/F2-2024.xls` legacy workbook) without rereading finished British audit tasks.
- Complete prior source archive content, including UK direct financial source-cell audits, country sources, RU judicial forms and FSIN, and U.S. finances, remains indexed in **[full archive INDEX v8](INDEX_v8.md)**. The v8 text has not been overwritten; this v9 is an additive master entry point.

## Working integrity rule

Every new source microtask should carry **indicator code, geography, reporting period (fiscal/annual/month/snapshot), unit, original source SHA, original sheet/cell/page, provenance and verification state**. Only documented periods are included. Distinguish `file exists`, `header observed`, `numeric value checked`, `indicator comparable over time`. Issue a new versioned registry on material incremental coverage; never silently overwrite previous catalogues or original data.

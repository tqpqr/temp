# GB monthly prison population: source-date correction and 2023–2024 validated output

The archived file `GB/Population_bulletin_monthly_April_2023_Corrected.ods` has an apparently misleading filename: its internal `Report Date` reads **2024-04-26**, not 2023. It contains 120 institution rows and corresponds to **April 2024**. The original archive copy and all earlier uncorrected extracts were preserved verbatim.

Consequently, two **add-only** corrected extracts were created:
- `02_uk/gb_monthly_prison_population_capacity_2023_report_date_validated_v2.csv`: **1,436 rows**, 12 unique report dates, Jan–Dec 2023.
- `02_uk/gb_monthly_prison_population_capacity_2024_report_date_validated_v2.csv`: **1,440 rows**, 12 unique report dates, Jan–Dec 2024, including 120 rows from the oddly named April file.

The earlier `2023_raw_v1.csv` and `2024_raw_v1.csv` are retained to show the original filename-based extraction.

**Data definitions** (extracted directly from monthly spreadsheet): establishment, Baseline CNA, In Use CNA, Operational Capacity, Population, internal Report Date and source XML row. A monthly bulletin reflects a *specific reporting day* rather than a monthly mean, and includes privately run prisons. It is not automatically comparable to HMPPS direct-employment staff FTE.

**Prohibition for analysis:** do not use file-name-inferred year; always use internal `Report Date`. Do not represent missing values as zero, or take nominal June 30 as reporting date without reading the report.

No originals overwritten or deleted; all files appended under the research archive.

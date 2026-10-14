# British source archive: byte-identical preservation checkpoint 24

## Confirmed git-copy operation

On 2026-10-14 copied **all 271** original `GB/` files into a new, add-only preservation namespace:
`prison-research-archive/02_uk/original_sources/`

Path mapping: `GB/<relative_path>` -> `prison-research-archive/02_uk/original_sources/<relative_path>`. The original `GB/` tree is intact.

Git commit: `c562b53b0b4904e8b8e6b0e08d794aa713c45c93`
Git tree: `d801d620004efde49f5ecf3899f641c68984ce61`

A direct comparison of both trees after commit confirmed:
- 271 originals, 271 copies
- **0 blob SHA mismatches**
- total source bytes = total archived bytes = **28,219,267**
- both parent files and `workforce/` child files copied.
- Git blobs are reused (not transcoded); copying does not alter underlying file content.

## Related catalogs
- `00_catalog/gb_all_271_files_family_manifest_v1.csv`: full original path/sha/size/family coverage.
- `00_catalog/gb_monthly_population_189_files_date_screen_v1.csv`: 189 population-bulletin files with 181 preliminary filename dates and 8 unresolved.
- `00_catalog/gb_costs_2014_2025_27_files_v1.csv`: 27 prison cost files FY2014/15–FY2024/25.
- `00_catalog/gb_271_full_scope_inventory_and_remaining_work_23.md`: work plan and evidence boundaries.

## Important limits
This checkpoint **does complete binary archival of GB original source files**, but does NOT mean every file's internal tables or date has been read and harmonized. In particular, 189 monthly bulletin files and 27 cost files still require comprehensive content-level inspection and data dictionaries. Existing 53 workforce files are inventoried but only partially harmonized.

For data analysis avoid treating filenames as verified publication dates. Preserve financial-year vs June point-in-time distinctions and historical facility boundary changes.

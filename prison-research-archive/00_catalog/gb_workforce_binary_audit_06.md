# GB/workforce inspection report — pass 06

## Boundary of review

Snapshot: `373a14b4fe725329c050ca45a8db723d304766e5`. There are **53 files** directly in `GB/workforce/`: **7 .xls**, **22 .xlsx**, **24 .ods**.

New full file register: `gb_workforce_53_file_binary_inventory.csv`.

Three binary files were fetched by GitHub and their ZIP directory entries actually inspected:
- `GB/workforce/hmpps-workforce-statistics-tables-jun-2025_final.ods`: ODS `content.xml` is ZIP method **8 (DEFLATE)**, not direct readable XML; package includes `mimetype` and an embedded PNG.
- `GB/workforce/noms-workforce-statistics-december-2015-tables.xlsx`: XLSX `xl/workbook.xml`, `xl/sharedStrings.xml`, `xl/worksheets/sheet1.xml` are ZIP method **8 (DEFLATE)**. The package contains an embedded PNG.
- `GB/workforce/hmpps-workforce-statistics-tables-dec-2019.xlsx`: XLSX workbook, strings, sheet XML likewise use ZIP method **8**, with an embedded PNG.

**No cells, sheet names, staffing definitions, units or values are claimed as read** from these three books. The archive lists NOMS/HMPPS/HR and publication year only as *filename-derived*. The distinction between prison staff, headquarters and probation staff cannot yet be resolved from the book contents. Preserve this verification boundary.

## Next extraction

To complete the variable dictionary, decompress XLSX/ODS XML and interpret XLS binary files with dedicated parsers; catalogue each worksheet title, headers, units, periods, statistical universe and definitions. Inspect images embedded in the books when needed. This step requires moving the original bytes into a compatible parser; connected GitHub binary retrieval alone does not decompress files in the current execution environment.

No original files changed and no new thematic binary copies made.

# USA 2011 state finances — actual 35-character Census records decoded

Original `us/raw data/2011/11state35.txt` Git blob SHA-1 `31b2db0eafbab431dd1e4e33f5f52ecc7b233eaa`.
Source's own layout: `us/raw data/2011/public-use-file-layout.xlsx` Git blob SHA-1 `723b170c572df098a9c760294ec521e311132410`.

- **12777 records of exactly 35 characters**, 51 source government identifiers, 358 source item codes.
- All records have survey year `11`, data year `11`, survey-origin field preserved. **30 valid negative amount records**, mostly item `Y08`, were correctly preserved as legitimate signed numerical text.
- Government identifier at characters 1–14, item code at 15–17, amount (signed USD thousands) at 18–29, survey year at 30–31, data year 32–33, origin 34–35. Source layout workbook says amount range **18–32**, overlapping with subsequent year fields; this is an internal source documentation discrepancy. The 18–29 range is the only nonoverlapping interpretation that parses **all 12777 actual records**, including negatives.
- **151 E04/F04/G04 original item rows** extracted preserving exact source record number and raw amount text. Code E04 occurs 51 times, **F04 50** and **G04 50**. Two *absences are real absences in this file*, not zeros: F04 missing `32000000000000`; G04 missing `04000000000000`. Do not complete the 51×3 table by filling missing 0.
- U.S. aggregate government ID `00000000000000` entries, amounts in thousand current USD: E04 = 37,492,787; F04 = 1,254,079; G04 = 261,607. Financial interpretation beyond raw code labels needs the contemporaneous official Census item-code dictionary.
- These are state government finances, *not* local government jail/correction finance. Do not aggregate directly with the separate 2012/2017/2022 Census local-government data. Source web context: https://www.census.gov/data/developers/data-sets/govsstatefin.html and https://www.census.gov/programs-surveys/state/data.html.
- Exact original transfer/download URL, item-code meaning, geography label mapping and historical revisions remain open. This is a scientific source inventory, not a finished panel.

The original file and companion layout were read only; no raw values or archival copies were changed.

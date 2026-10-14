# FSIN source-content verification — 14 October 2026

Original XLSX: `fsin/data_fsin_info_103_v20240627.xlsx`
Git blob SHA-1: `ebc0c08de7a7e4279e6035637dea6df0ff519c4c`
External dataset: https://tochno.st/datasets/fsin_info

The original XLSX ZIP members were decompressed and actual first worksheet cells parsed.

- Worksheet: `data_clear`
- Source data: 7,227 observation rows, 11 fields, Excel A1:K7228
- Exact field names: `indicator_code`, `indicator_category`, `main_level`, `indicator_name`, `year`, `indicator_value`, `rounded`, `data_date`, `data_date_t`, `data_source`, `data_source_2`.
- 300 distinct indicator codes.
- 302 distinct combinations of (code, category, level, label).
- 2 codes carry more than one combination: `Y808000077` and `Y808000298`.
- 100 indicator codes have two or more rows for at least one nominal year; these may be distinct report dates or sources. Keep all versions.
- Actual nominal-year labels range **1995 through 2023**, with 29 distinct years. Publisher's headline says 2005–2023: record this as a coverage disagreement, not grounds for dropping older data.
- Source categories are national FSIN inmate and offender counts, institution infrastructure, production, education, medical and religious institutions, staff, violations and incidents.
- Field `data_date` sometimes stores numeric Excel date serials; `data_date_t` is a source-provided normalized text label.
- Neither `year` nor `data_date_t` can automatically be treated as the sole observation identity.

## Two confirmed code-name changes (not necessarily errors)

| Source code | Recorded variants | Rows by variant |
|---|---|---|
| `Y808000077` | `осужденных женщин, в ИК` (level `женщин, всего`); `осужденных женщин, в ИК общего режима` (level `женщин, в ИК`) | 60; 1 |
| `Y808000298` | `свыше 5 лет`; `в ВК, срок ЛС, свыше 5` (both at level `в ВК, по сроку ЛС`) | 9; 19 |

**Research rule:** do not collapse by indicator code and nominal year until the source date, original label and publication source have been reconciled. Preserve the two code-description variants. Units and denominators remain unverified pending the accompanying description PDF.

This is a quality-check log only; the original source was not changed.

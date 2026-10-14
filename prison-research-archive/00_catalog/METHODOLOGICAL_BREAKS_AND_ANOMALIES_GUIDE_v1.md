# Methodological breaks, revisions and anomaly ledger v1 — avoid redoing research

The [machine-readable register](METHODOLOGICAL_BREAKS_AND_ANOMALIES_v1.csv) has **12 evidence-anchored issues**. This is **not** a list of proven shocks in prison operations: it includes source schema changes, financial category breaks, publisher restatements, source row/address corrections, atypical printed zeros, duplicate administrative lines, blank-value coding and capacity denominator incompatibilities.

## Permanent two-level status discipline
- `EXACT_OBSERVATION`: what the actual source cells and official footnotes unambiguously state. `CAUSAL_EXPLANATION_STATUS`: whether an *explanation* for a change is validated. A confirmed mismatch is not a confirmed causal mechanism.
- `CONFIRMED_*`: the difference is evidenced, but if the explanation is unknown that remains explicitly unknown. `OPEN_*`: avoid reconciling by guess. `BLOCKED_*`: further work depends on absent external bytes. `RESOLVED_USE_V2`: source-row/address correction has a verified replacement and should not be re-investigated from old XML indices.
- Each row carries exact original Git paths, SHA-1 and original source cells or HTML IDs, plus prior deep audit reference, disallowed interpretations and the precise resumption condition.
- A `source date/fiscal year` is not a `publication_vintage`. A numerical source revision is not a new fiscal period; a prison operator-year line is not a new physical prison; a blank cell is not necessarily a zero.
- `original_source_b` may be empty because some anomalies are **internal to one document**, not comparisons between two physical source files.

## New mandatory condition for every archive microtask
1. Open this **breaks ledger** before interpreting unusual source values or adding a purported comparable indicator to [indicator-period registry v3](INDICATOR_PERIOD_COVERAGE_REGISTRY_v3.csv).
2. At task close explicitly mark `BREAKS_REGISTER_UPDATED` when genuinely new verified issue is discovered, or `NO_NEW_BREAK` otherwise.
3. If a prior break has an improved explanation, source corrected address or resolution, **make a new additive vN breaks register**, preserving the original row ID and source evidence. Do not delete unresolved history.
4. Dataset extraction/analysis should carry or link `break_id` to affected indicator/edition observations; this avoids repeating the same source problem when multiple research papers use the archive.

**First major issues:** GB **MB-001** Service Concession Arrangements **£454,911,681** new *separately labelled* FY2016/17 published category without an FY2015/16 equivalent; GB **MB-004** FY2018/19 national direct-spending restatement **£129,111,488** with unchanged overall spending; **MB-005** Birmingham 2019/20 two operator-period rows with corrected physical source addresses; **MB-006** ODS physical source row correction affecting **564** original financial accounting lines; **MB-011** Italy regulatory capacity not UK operating/CNA.

**Coverage limit:** This v1 ledger lists 12 confirmed relevant examples, not exhaustive methodological breaks across all 1,124 originals. Continue discovering them as original files are actually inspected. Preservation of original byte-identical mirrors and prior catalogues remains compulsory.

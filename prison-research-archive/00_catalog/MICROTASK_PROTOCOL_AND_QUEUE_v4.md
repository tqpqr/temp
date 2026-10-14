# Atomic prison archive work protocol v4 — continuity and previously completed source audits

Inherits all preservation, source-cell evidence and TWO-catalogue obligations from [protocol v3](MICROTASK_PROTOCOL_AND_QUEUE_v3.md). No older protocol, original source, mirror, register, queue, or checkpoint is edited.

## PREVIOUSLY AUDITED source gate — new explicit requirement
Before each task, look in [source evidence ledger v11](ARCHIVE_PER_FILE_EVIDENCE_LEDGER_v11.csv), latest [indicator registry v5](INDICATOR_PERIOD_COVERAGE_REGISTRY_v5.csv), latest [methodological-break ledger v3](METHODOLOGICAL_BREAKS_AND_ANOMALIES_v3.csv), and source-specific existing audits and extracts. Check actual source SHA. If the task acceptance criteria are ALREADY MET, mark `DONE_PRIOR_AUDIT_RECONCILED` with direct links to the existing evidence; **do not run the same extraction again solely to obtain a new task ID**. Validate existing exported source rows / counts sufficiently to confirm coverage, and record what wasn't independently rechecked.

If evidence is only partial, perform only the smallest missing check rather than redo the completed half. Keep `BLOCKED` when original binary cannot be read, even if path and SHA are confirmed.

## Two required catalogue outcomes at each source task
1. Indicators/periods: issue a **new additive coverage registry vN** for genuinely new checked observations, or `REGISTRY_UNCHANGED` with evidence. Preserve source-vintage, date granularity, units and explicit `numeric` vs `header` vs `file` status. Code E04 alone does not prove a corrections-spending definition.
2. Methodological break/anomaly: issue a **new additive breaks ledger vN** for newly evidenced mismatch or clarification, or `NO_NEW_BREAK`. Distinguish source contradiction, missingness, reclassification, denomination, temporal and causal interpretation. Link a stable break ID to affected indicator rows.

Source file originals and byte-identical categorized copies are NEVER mutated. New task evidence + new queue version + new checkpoint are committed and re-fetched. Source SHA from Git is not external publisher SHA-256.

## Current examples
- `US-001 DONE`: six layout fields (2011 historical source), publisher amount positions internally inconsistent; verified source field CSV. Source workbook creation 2023, modified 2025; never pretend original 2011 publication vintage.
- `US-002 DONE_PRIOR_AUDIT_RECONCILED`: preexisting full 12,777-line 2011 TXT audit and 151 original source-code rows already meet sample-check requirements. Code-level registry v5 adds E04/F04/G04 2011 source coverage **without pretending definitions are verified**. MB-015 documents two true source omissions, not zero.
- **Next `GB-020`**: read one original UK monthly population bulletin for December 2024, audit its exact report date, original capacity and occupancy field definitions and real institution-row format. Publish observed date indicators if checked, linked to source physical sheet/cell. Do not infer an annual average from a one-day snapshot.

Use [queue v6](MICROTASK_QUEUE_WAVE1_v6.csv) and [active index v13](../INDEX_v13.md) after interruptions.

# Plan To Address Current Limitations

This checklist prioritizes changes that most improve correctness while staying
feasible with public data and reviewable implementation steps. Priorities 1 and
2 now have code support in this branch; the remaining unchecked items require
curated data or later implementation work.

## Progress Snapshot

- Updated: 2026-08-31.
- Branch: `feature/clinsr-pipeline`.
- PR: `https://github.com/DrSquare/ClinicalTrialSuccess/pull/1`.
- Latest progress commit: `c8c22db Implement curated approval and synonym
  workflows`.
- Verification completed:
  - `py -3.13 -m py_compile clinical_trial_success.py tools\convert_pdf_to_markdown.py`
  - `py -3.13 -m unittest discover -s tests -v`
  - Result: 18 tests passed.
- Current state: the pipeline can ingest reviewed condition-specific approvals
  and reviewed drug synonyms, records input hashes, and emits a drug-name
  standardization review report. Full strict P3SR/OSR remains blocked on a
  curated condition-specific FDA approval dataset.

## Priority 1: Condition-Specific Approval Ground Truth

Build or ingest a condition-specific approval table keyed by normalized drug and
indication.

- Feasibility: High if a curated CSV is provided or assembled manually from FDA
  labels/review documents; medium if automated from label text.
- Impact: Critical. Enables strict CDP P3SR and OSR instead of leaving them
  unestimated.
- Checklist:
  - [x] Define a versioned `approvals.csv` schema.
  - [x] Add `data/approvals.template.csv` with required review metadata.
  - [x] Validate required fields, schema version, approval dates, source, and
    reviewer metadata.
  - [x] Require indication-specific approval rows in the default strict
    `--approval-match condition` mode.
  - [x] Reject duplicate canonical drug-indication approval dates.
  - [x] Support `canonical_drug` and `canonical_condition` override columns.
  - [x] Record `--approvals-csv` path, schema version, and SHA-256 hash in
    `summary.json`.
  - [x] Add regression tests where one drug has approvals for one indication but
    not another.
  - [ ] Curate a complete condition-specific FDA approval dataset for the target
    run window.
  - [ ] Re-run strict output with nonblank P3SR/OSR after curated approvals are
    available.
- Progress details:
  - Implemented in `clinical_trial_success.py` with
    `APPROVALS_SCHEMA_VERSION = "1"` and `load_approvals_csv(...)`.
  - Strict mode now requires `condition` in `--approval-match condition`; rows
    without indication-level evidence fail validation instead of silently
    becoming broad drug-level approvals.
  - Required review metadata now includes `source` and `reviewed_by`; optional
    `reviewed_at` is date-validated when provided.
  - Canonical matching uses `canonical_drug` and `canonical_condition` when
    present, preserving source fields for audit.
  - Duplicate canonical `(drug_key, condition_key, approval_date)` rows are
    rejected.
  - Template saved at `data/approvals.template.csv`.
  - Tests added for missing strict condition fields, canonical overrides,
    duplicate approvals, and offline CLI use with curated approval input.

## Priority 2: Canonical Drug Synonyms

Create a versioned synonym map for trial intervention names, development codes,
brand names, generic names, and active ingredients.

- Feasibility: High for user-provided CSV; medium for automated enrichment from
  public sources.
- Impact: Critical for merging fragmented CDPs and detecting phase progression.
- Checklist:
  - [x] Expand the synonym schema to version 1 with `alias`, `canonical`,
    `source`, and `reviewed_by`.
  - [x] Add `data/synonyms.template.csv` with optional `entity_type`,
    `reviewed_at`, and notes fields.
  - [x] Validate required fields, schema version, source, reviewer metadata, and
    drug-only entity type.
  - [x] Reject conflicting alias-to-canonical mappings.
  - [x] Continue using ClinicalTrials.gov `otherNames` while allowing curated
    synonym overrides.
  - [x] Emit `drug_standardization_report.csv` for unresolved or
    high-fragmentation drug names.
  - [x] Record `--synonyms-csv` path, schema version, and SHA-256 hash in
    `summary.json`.
  - [x] Add regression tests for code-name-to-INN mappings and fragmentation
    reporting.
  - [ ] Populate a comprehensive curated synonym map from FDA labels,
    ClinicalTrials.gov aliases, and external drug databases.
- Progress details:
  - Implemented in `clinical_trial_success.py` with
    `SYNONYMS_SCHEMA_VERSION = "1"` and `load_synonyms(...)`.
  - Required review metadata now includes `source` and `reviewed_by`; optional
    `entity_type` is accepted only when blank or `drug`.
  - Conflicting alias mappings are rejected so a development code cannot point
    to multiple canonical drugs.
  - ClinicalTrials.gov `otherNames` remain part of intervention name selection;
    curated CSV mappings override normalized aliases after extraction.
  - `drug_standardization_report.csv` is now generated for every run and
    highlights uncurated high-fragmentation drug-name groups.
  - Template saved at `data/synonyms.template.csv`.
  - Tests added for versioned synonym ingestion, conflicting alias rejection,
    standardization report rows, and end-to-end summary hash metadata.

## Priority 3: Disease Standardization

Map ClinicalTrials.gov conditions to stable disease identifiers and hierarchy
levels.

- Feasibility: Medium. Automated mapping can cover common conditions, but manual
  review is still needed for ambiguous oncology and rare-disease terms.
- Impact: High. Reduces condition-name fragmentation and enables disease-class
  ClinSR.
- Checklist:
  - [ ] Add `conditions.csv` with `condition_alias`, `canonical_condition`,
    `condition_id`, `disease_class`, and `source`.
  - [ ] Support ICD-11 or another controlled vocabulary when available.
  - [ ] Emit unresolved condition reports.
  - [ ] Add tests for synonym collapsing and disease-class aggregation.

## Priority 4: Basket/Umbrella Trial Curation

Replace residual study-level Cartesian drug-condition pairing with curated or
arm-linked associations.

- Feasibility: Medium. ClinicalTrials.gov arms help, but many complex trials need
  manual or NLP-assisted review.
- Impact: High. Reduces false drug-condition CDPs in oncology and multi-arm
  protocols.
- Checklist:
  - [ ] Add an `association_confidence` filter to optionally exclude
    `study_level_cartesian` rows from rate calculations.
  - [ ] Generate a review queue for studies with multiple experimental drugs and
    multiple conditions.
  - [ ] Add a curated association CSV keyed by `nct_id`, `drug`, and
    `condition`.
  - [ ] Add tests for basket, umbrella, comparator, and multi-condition studies.

## Priority 5: Label-State Audit Reports

Add explainability reports for why each CDP phase was labeled as success,
failure, or ongoing.

- Feasibility: High.
- Impact: Medium-high. Improves reviewability and catches systematic labeling
  mistakes.
- Checklist:
  - [ ] Write per-CDP timelines sorted by date.
  - [ ] Add counts by evidence type, phase, disease class, and association
    confidence.
  - [ ] Add sampled audit files for manual review.

## Priority 6: Offline Reproducibility

Make every output reproducible without live API calls.

- Feasibility: High.
- Impact: Medium-high.
- Checklist:
  - [ ] Add `--openfda-json` input support.
  - [x] Record hashes for currently supported optional approvals/synonyms CSV
    inputs.
  - [x] Add an offline CLI regression test using a small synthetic studies JSON
    fixture.
  - [ ] Add a `Makefile` or PowerShell task file for standard runs.
- Progress details:
  - `summary.json` now records path and SHA-256 hash for `--approvals-csv` and
    `--synonyms-csv`.
  - The offline CLI regression test runs with `--studies-json`, `--no-openfda`,
    `--approvals-csv`, and `--synonyms-csv`, then verifies summary hashes and
    the generated drug standardization report.

## Priority 7: Semantic Markdown Conversion

Improve the PDF conversion from page-traced text to structured Markdown.

- Feasibility: Medium.
- Impact: Medium. Helpful for paper review, but does not affect ClinSR outputs.
- Checklist:
  - [ ] Detect headings and section hierarchy.
  - [ ] Reconstruct tables and equations where possible.
  - [ ] Clean split words and common PDF extraction artifacts.
  - [ ] Add a short method-summary Markdown file separate from full extracted
    text.

## Priority 8: Nine-Year Dynamic Window Support

Add rolling-window runs matching the paper's preferred nine-year dynamic ClinSR
strategy.

- Feasibility: High once approval and standardization inputs exist.
- Impact: Medium. Improves comparability with the paper.
- Checklist:
  - [ ] Add `--rolling-window-years` and `--rolling-window-start/end`.
  - [ ] Output one row per window and phase.
  - [ ] Compare five-year and nine-year sensitivity outputs.

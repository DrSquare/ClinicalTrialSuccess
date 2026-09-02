# Clinical Trial Success

This workspace contains a Markdown conversion of the local paper PDF and a
ClinSR-style implementation for labeling clinical development programs and
calculating clinical trial success rates.

Source paper:

- Zhou et al., "Dynamic clinical trial success rates for drugs in the 21st
  century", Nature Communications (2025), doi:10.1038/s41467-025-64552-2.
- Local Markdown conversion:
  `Dynamic Clinical Trial Success Rates for Drugs in the 21st Century.md`

## Method Implemented

The CLI follows the paper's operational definitions:

- Clinical development programs (CDPs) are approximated as normalized
  drug-condition pairs.
- Phase 1/2 trials are treated as Phase 2.
- Phase 2/3 trials are treated as Phase 3.
- Phase success labels are `success`, `failure`, or `ongoing`.
- Phase 1 success means progression to Phase 2, Phase 3, or approval.
- Phase 2 success means progression to Phase 3 or approval.
- Phase 3 success means final approval.
- Failure is assigned when a program is discontinued/terminated without later
  trial activity, or when no new trial activity appears after the configured
  two-year threshold.
- By default, final approval must be condition-specific for CDP success-rate
  labels. Drug-level openFDA approvals are saved as evidence but are not used as
  CDP successes unless `--approval-match drug` is selected as a sensitivity run.
- If no condition-specific approval records are supplied, strict P3SR and OSR
  are left blank rather than reported as zero.
- Overall success rate (OSR) is `P1SR * P2SR * P3SR`.

The paper recommends a nine-year time window for robust dynamic ClinSR
estimates. The default command below uses the requested five-year window, so
recent labels can be affected by boundary effects. The implementation now
fetches full matching trial history through the analysis end date, then selects
success/failure events inside the requested five-year window.

## Run

Install the PDF conversion dependency if needed:

```powershell
py -3.13 -m pip install -r requirements.txt
```

```powershell
py -3.13 clinical_trial_success.py --output-dir output
```

By default, the script uses the past five years ending on the current local date.
For the saved full run in this workspace, the window is 2021-08-30 through
2026-08-30.

Explicit dates:

```powershell
py -3.13 clinical_trial_success.py `
  --start-date 2021-08-30 `
  --end-date 2026-08-30 `
  --output-dir output
```

Smoke run:

```powershell
py -3.13 clinical_trial_success.py --max-studies 500 --output-dir output_smoke
```

## Outputs

The command writes:

- `trial_records.csv`: flattened drug-condition trial records from
  ClinicalTrials.gov.
- `phase_labels.csv`: CDP phase labels and evidence.
- `success_rates.csv`: P1SR, P2SR, P3SR, and OSR.
- `drug_standardization_report.csv`: review queue for curated synonym gaps and
  high-fragmentation drug names.
- `summary.json`: source URLs, exact queries, counts, hashes, rates, and method
  notes.
- `clinicaltrials_studies_<start>_<end>.json`: raw ClinicalTrials.gov records
  used for the run.
- `openfda_drugsfda_<start>_<end>.json`: raw openFDA Drugs@FDA records used for
  the run.

## Optional Inputs

Use a version 1 synonym CSV to improve drug-name merging. Start from
`data/synonyms.template.csv`; the required columns are `schema_version`, `alias`,
`canonical`, `source`, and `reviewed_by`.

```csv
schema_version,alias,canonical,entity_type,source,reviewed_by,reviewed_at,notes
1,NEOD001,birtamimab,drug,manual_registry_review,reviewer@example.com,2026-08-31,development code to INN
```

Use a version 1 approvals CSV for condition-specific Phase 3 success labels.
Start from `data/approvals.template.csv`; in the default strict mode the
required columns are `schema_version`, `drug`, `approval_date`, `condition`,
`source`, and `reviewed_by`. Optional `canonical_drug` and
`canonical_condition` columns override source text for matching while preserving
the original fields.

```csv
schema_version,drug,canonical_drug,approval_date,condition,canonical_condition,condition_id,application_number,submission_type,submission_class_code,source,reviewed_by,reviewed_at,notes
1,alemtuzumab,alemtuzumab,2014-11-14,multiple sclerosis,multiple sclerosis,,BLA103948,SUPPL,EFFICACY,manual_fda_label_review,reviewer@example.com,2026-08-31,condition-specific FDA label review
```

Then run:

```powershell
py -3.13 clinical_trial_success.py `
  --synonyms-csv synonyms.csv `
  --approvals-csv approvals.csv `
  --output-dir output
```

To run the less strict drug-level openFDA sensitivity analysis:

```powershell
py -3.13 clinical_trial_success.py `
  --approval-match drug `
  --output-dir output_drug_level_sensitivity
```

## Data Sources

- ClinicalTrials.gov API v2:
  `https://clinicaltrials.gov/api/v2/studies`
- openFDA Drugs@FDA API:
  `https://api.fda.gov/drug/drugsfda.json`

openFDA approval data does not include indication-level matching in the API
records used here. The default CDP output therefore treats openFDA as drug-level
evidence only and lets a user-supplied approvals CSV supply condition-specific
approval labels. Use `--approval-match drug` only when a molecular-entity-level
sensitivity analysis is acceptable. `summary.json` records the schema version,
path, and SHA-256 hash for both optional CSV inputs when provided.

## Review Notes

The implementation is an approximation of the paper, not a full reproduction.
The paper additionally uses registry synonyms, external drug databases, ICD-11
disease mapping, manual validation, and curated handling of basket/umbrella
trials. This code uses public API fields and exposes unresolved study-level
drug-condition pairings through the `association_confidence` column.

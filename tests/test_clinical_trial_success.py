from __future__ import annotations

import io
import json
import unittest
from contextlib import redirect_stderr, redirect_stdout
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory

from clinical_trial_success import (
    ApprovalRecord,
    TrialRecord,
    build_drug_standardization_report,
    calculate_rates,
    flatten_studies,
    label_all_cdps,
    load_approvals_csv,
    load_synonyms,
    main,
    normalize_drug,
    normalize_phase,
    write_drug_standardization_report,
)


def trial(
    nct_id: str,
    drug: str,
    condition: str,
    phase: int,
    status: str,
    start: date,
    completion: date | None = None,
) -> TrialRecord:
    return TrialRecord(
        nct_id=nct_id,
        brief_title=f"{drug} {condition}",
        drug=drug,
        drug_key=normalize_drug(drug),
        condition=condition,
        condition_key=condition.lower(),
        phase=phase,
        intervention_type="DRUG",
        overall_status=status,
        start_date=start,
        completion_date=completion,
    )


class ClinicalTrialSuccessTests(unittest.TestCase):
    def test_phase_normalization_matches_paper_rules(self) -> None:
        self.assertEqual(normalize_phase(["EARLY_PHASE1"]), 1)
        self.assertEqual(normalize_phase(["PHASE1", "PHASE2"]), 2)
        self.assertEqual(normalize_phase(["PHASE2", "PHASE3"]), 3)
        self.assertIsNone(normalize_phase(["PHASE4"]))
        self.assertIsNone(normalize_phase(["NA"]))

    def test_success_from_higher_phase(self) -> None:
        records = [
            trial("NCT00000001", "Examplemab", "Asthma", 1, "COMPLETED", date(2021, 9, 1)),
            trial("NCT00000002", "Examplemab", "Asthma", 2, "RECRUITING", date(2023, 3, 1)),
        ]
        labels = label_all_cdps(records, [], date(2021, 8, 30), date(2026, 8, 30))
        p1 = [label for label in labels if label.phase == 1][0]
        self.assertEqual(p1.label, "success")
        self.assertEqual(p1.evidence, "progressed_to_phase_2")

    def test_failure_from_two_year_inactivity(self) -> None:
        records = [
            trial(
                "NCT00000003",
                "Dormantide",
                "Migraine",
                2,
                "COMPLETED",
                date(2021, 9, 1),
                date(2022, 1, 1),
            )
        ]
        labels = label_all_cdps(records, [], date(2021, 8, 30), date(2026, 8, 30))
        p2 = [label for label in labels if label.phase == 2][0]
        self.assertEqual(p2.label, "failure")
        self.assertEqual(p2.evidence, "no_new_trial_for_2_years")

    def test_phase_three_success_from_approval(self) -> None:
        records = [
            trial("NCT00000004", "Approximab", "Lymphoma", 3, "COMPLETED", date(2022, 6, 1))
        ]
        approvals = [
            ApprovalRecord(
                drug="Approximab",
                drug_key=normalize_drug("Approximab"),
                approval_date=date(2024, 4, 1),
                application_number="BLA123456",
                submission_type="ORIG",
                submission_class_code="TYPE 1",
                source="test",
                condition="Lymphoma",
                condition_key="lymphoma",
            )
        ]
        labels = label_all_cdps(records, approvals, date(2021, 8, 30), date(2026, 8, 30))
        p3 = [label for label in labels if label.phase == 3][0]
        self.assertEqual(p3.label, "success")
        self.assertEqual(p3.evidence, "progressed_to_approval")
        self.assertEqual(p3.approval_application, "BLA123456")

    def test_skipped_phase_is_imputed_as_success(self) -> None:
        records = [
            trial("NCT00000005", "Jumpase", "Glioma", 1, "COMPLETED", date(2022, 1, 1)),
            trial("NCT00000006", "Jumpase", "Glioma", 3, "RECRUITING", date(2024, 1, 1)),
        ]
        labels = label_all_cdps(records, [], date(2021, 8, 30), date(2026, 8, 30))
        p2 = [label for label in labels if label.phase == 2][0]
        self.assertEqual(p2.label, "success")
        self.assertEqual(p2.evidence, "imputed_success_from_phase_jump")

    def test_rate_calculation_and_osr(self) -> None:
        records = [
            trial("NCT00000007", "Ratex", "Pain", 1, "COMPLETED", date(2021, 9, 1)),
            trial("NCT00000008", "Ratex", "Pain", 2, "COMPLETED", date(2022, 9, 1)),
            trial("NCT00000009", "Ratex", "Pain", 3, "COMPLETED", date(2023, 9, 1)),
        ]
        approvals = [
            ApprovalRecord(
                drug="Ratex",
                drug_key=normalize_drug("Ratex"),
                approval_date=date(2024, 9, 1),
                application_number="NDA123456",
                submission_type="ORIG",
                submission_class_code="TYPE 1",
                source="test",
                condition="Pain",
                condition_key="pain",
            )
        ]
        labels = label_all_cdps(records, approvals, date(2021, 8, 30), date(2026, 8, 30))
        rates = calculate_rates(labels, date(2021, 8, 30), date(2026, 8, 30))
        by_metric = {row.metric: row for row in rates}
        self.assertEqual(by_metric["P1SR"].rate, 1.0)
        self.assertEqual(by_metric["P2SR"].rate, 1.0)
        self.assertEqual(by_metric["P3SR"].rate, 1.0)
        self.assertEqual(by_metric["OSR"].rate, 1.0)

    def test_conditionless_approval_requires_explicit_opt_in(self) -> None:
        records = [
            trial("NCT00000010", "Broadmab", "Asthma", 3, "COMPLETED", date(2022, 6, 1))
        ]
        approvals = [
            ApprovalRecord(
                drug="Broadmab",
                drug_key=normalize_drug("Broadmab"),
                approval_date=date(2024, 4, 1),
                application_number="BLA555555",
                submission_type="ORIG",
                submission_class_code="TYPE 1",
                source="test",
            )
        ]
        strict = label_all_cdps(records, approvals, date(2021, 8, 30), date(2026, 8, 30))
        strict_p3 = [label for label in strict if label.phase == 3][0]
        self.assertEqual(strict_p3.label, "failure")

        sensitivity = label_all_cdps(
            records,
            approvals,
            date(2021, 8, 30),
            date(2026, 8, 30),
            allow_conditionless_approvals=True,
        )
        sensitivity_p3 = [label for label in sensitivity if label.phase == 3][0]
        self.assertEqual(sensitivity_p3.label, "success")

    def test_approval_csv_requires_condition_in_strict_mode(self) -> None:
        with TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "approvals.csv"
            path.write_text(
                "schema_version,drug,approval_date,source,reviewed_by\n"
                "1,Indicamab,2024-01-02,manual_fda_label_review,qa\n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "missing required columns.*condition"):
                load_approvals_csv(str(path), require_condition=True)

    def test_approval_csv_uses_canonical_drug_and_condition(self) -> None:
        with TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "approvals.csv"
            path.write_text(
                "schema_version,drug,canonical_drug,approval_date,condition,"
                "canonical_condition,source,reviewed_by\n"
                "1,Brand X,Genericx,2024-01-02,NSCLC,"
                "non-small cell lung cancer,manual_fda_label_review,qa\n",
                encoding="utf-8",
            )

            approvals = load_approvals_csv(str(path), require_condition=True)

        self.assertEqual(len(approvals), 1)
        self.assertEqual(approvals[0].drug_key, "genericx")
        self.assertEqual(approvals[0].condition_key, "non-small cell lung cancer")
        self.assertEqual(approvals[0].source, "manual_fda_label_review")

    def test_approval_csv_rejects_duplicate_canonical_approval_dates(self) -> None:
        with TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "approvals.csv"
            path.write_text(
                "schema_version,drug,canonical_drug,approval_date,condition,"
                "canonical_condition,source,reviewed_by\n"
                "1,Brand X,Genericx,2024-01-02,NSCLC,"
                "non-small cell lung cancer,manual_fda_label_review,qa\n"
                "1,Genericx,,2024-01-02,non-small cell lung cancer,,"
                "manual_fda_label_review,qa\n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "duplicates canonical drug-condition"):
                load_approvals_csv(str(path), require_condition=True)

    def test_synonyms_csv_accepts_versioned_review_metadata(self) -> None:
        with TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "synonyms.csv"
            path.write_text(
                "schema_version,alias,canonical,entity_type,source,reviewed_by,"
                "reviewed_at,notes\n"
                "1,NEOD001,birtamimab,drug,manual_registry_review,qa,"
                "2026-08-31,code-name mapping\n",
                encoding="utf-8",
            )

            synonyms = load_synonyms(str(path))

        self.assertEqual(synonyms["neod001"], "birtamimab")

    def test_synonyms_csv_rejects_conflicting_aliases(self) -> None:
        with TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "synonyms.csv"
            path.write_text(
                "schema_version,alias,canonical,source,reviewed_by\n"
                "1,NEOD001,birtamimab,manual_registry_review,qa\n"
                "1,NEOD001,othermab,manual_registry_review,qa\n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "earlier row maps it"):
                load_synonyms(str(path))

    def test_drug_standardization_report_marks_curated_and_unresolved_rows(self) -> None:
        records = [
            TrialRecord(
                nct_id="NCT00000101",
                brief_title="Curated alias",
                drug="NEOD001",
                drug_key="birtamimab",
                condition="Amyloidosis",
                condition_key="amyloidosis",
                phase=2,
                intervention_type="DRUG",
                overall_status="COMPLETED",
                start_date=date(2022, 1, 1),
                completion_date=None,
            ),
            TrialRecord(
                nct_id="NCT00000102",
                brief_title="Curated canonical",
                drug="birtamimab",
                drug_key="birtamimab",
                condition="Amyloidosis",
                condition_key="amyloidosis",
                phase=3,
                intervention_type="DRUG",
                overall_status="RECRUITING",
                start_date=date(2024, 1, 1),
                completion_date=None,
            ),
            TrialRecord(
                nct_id="NCT00000103",
                brief_title="Unresolved spelling",
                drug="Examplex low dose",
                drug_key="examplex",
                condition="Pain",
                condition_key="pain",
                phase=1,
                intervention_type="DRUG",
                overall_status="COMPLETED",
                start_date=date(2022, 1, 1),
                completion_date=None,
            ),
            TrialRecord(
                nct_id="NCT00000104",
                brief_title="Unresolved spelling",
                drug="Examplex injection",
                drug_key="examplex",
                condition="Pain",
                condition_key="pain",
                phase=2,
                intervention_type="DRUG",
                overall_status="RECRUITING",
                start_date=date(2024, 1, 1),
                completion_date=None,
            ),
        ]

        rows = build_drug_standardization_report(records, {"neod001": "birtamimab"})
        by_key = {row.drug_key: row for row in rows}

        self.assertEqual(by_key["birtamimab"].needs_review, "false")
        self.assertEqual(by_key["examplex"].needs_review, "true")

        with TemporaryDirectory() as tmp_dir:
            report_path = Path(tmp_dir) / "drug_standardization_report.csv"
            write_drug_standardization_report(report_path, rows)
            report_text = report_path.read_text(encoding="utf-8")

        self.assertIn("drug_key,trial_records,cdps", report_text)
        self.assertIn("examplex", report_text)

    def test_cli_records_curated_input_hashes_and_standardization_report(self) -> None:
        with TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            studies_path = tmp_path / "studies.json"
            approvals_path = tmp_path / "approvals.csv"
            synonyms_path = tmp_path / "synonyms.csv"
            output_dir = tmp_path / "output"
            studies_path.write_text(
                json.dumps(
                    {
                        "studies": [
                            {
                                "protocolSection": {
                                    "identificationModule": {
                                        "nctId": "NCT00000105",
                                        "briefTitle": "Brand X NSCLC",
                                    },
                                    "statusModule": {
                                        "overallStatus": "COMPLETED",
                                        "startDateStruct": {"date": "2022-01-01"},
                                        "completionDateStruct": {"date": "2023-01-01"},
                                    },
                                    "conditionsModule": {
                                        "conditions": ["non-small cell lung cancer"]
                                    },
                                    "designModule": {
                                        "studyType": "INTERVENTIONAL",
                                        "phases": ["PHASE3"],
                                    },
                                    "armsInterventionsModule": {
                                        "armGroups": [
                                            {"label": "Brand X", "type": "EXPERIMENTAL"}
                                        ],
                                        "interventions": [
                                            {
                                                "type": "DRUG",
                                                "name": "Brand X",
                                                "armGroupLabels": ["Brand X"],
                                                "otherNames": ["Genericx"],
                                            }
                                        ],
                                    },
                                }
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            approvals_path.write_text(
                "schema_version,drug,canonical_drug,approval_date,condition,"
                "canonical_condition,source,reviewed_by\n"
                "1,Brand X,Genericx,2024-01-02,NSCLC,"
                "non-small cell lung cancer,manual_fda_label_review,qa\n",
                encoding="utf-8",
            )
            synonyms_path.write_text(
                "schema_version,alias,canonical,source,reviewed_by\n"
                "1,Brand X,Genericx,manual_registry_review,qa\n",
                encoding="utf-8",
            )

            with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                result = main(
                    [
                        "--start-date",
                        "2021-08-30",
                        "--end-date",
                        "2026-08-30",
                        "--studies-json",
                        str(studies_path),
                        "--no-openfda",
                        "--approvals-csv",
                        str(approvals_path),
                        "--synonyms-csv",
                        str(synonyms_path),
                        "--output-dir",
                        str(output_dir),
                    ]
                )

            summary = json.loads((output_dir / "summary.json").read_text(encoding="utf-8"))

        self.assertEqual(result, 0)
        self.assertEqual(summary["analysis"]["approvals_schema_version"], "1")
        self.assertEqual(summary["analysis"]["synonyms_schema_version"], "1")
        self.assertRegex(summary["artifacts"]["approvals_csv_sha256"], r"^[a-f0-9]{64}$")
        self.assertRegex(summary["artifacts"]["synonyms_csv_sha256"], r"^[a-f0-9]{64}$")
        self.assertEqual(summary["drug_standardization_report_rows"], 1)
        p3_rate = {row["metric"]: row for row in summary["rates"]}["P3SR"]
        self.assertEqual(p3_rate["rate"], 1.0)

    def test_future_discontinued_completion_is_not_failure(self) -> None:
        records = [
            trial(
                "NCT00000011",
                "Futurestop",
                "Dermatitis",
                2,
                "TERMINATED",
                date(2025, 1, 1),
                date(2027, 1, 1),
            )
        ]
        labels = label_all_cdps(records, [], date(2021, 8, 30), date(2026, 8, 30))
        p2 = [label for label in labels if label.phase == 2][0]
        self.assertEqual(p2.label, "ongoing")

    def test_parallel_active_trial_prevents_discontinued_failure(self) -> None:
        records = [
            trial(
                "NCT00000012",
                "Parallelix",
                "Anemia",
                2,
                "TERMINATED",
                date(2022, 1, 1),
                date(2023, 1, 1),
            ),
            trial(
                "NCT00000013",
                "Parallelix",
                "Anemia",
                2,
                "ACTIVE_NOT_RECRUITING",
                date(2022, 6, 1),
                date(2025, 1, 1),
            ),
        ]
        labels = label_all_cdps(records, [], date(2021, 8, 30), date(2026, 8, 30))
        p2 = [label for label in labels if label.phase == 2][0]
        self.assertEqual(p2.label, "ongoing")

    def test_skipped_phase_requires_forward_chronology(self) -> None:
        records = [
            trial("NCT00000014", "Chronolog", "Glioma", 3, "COMPLETED", date(2022, 1, 1)),
            trial("NCT00000015", "Chronolog", "Glioma", 1, "RECRUITING", date(2024, 1, 1)),
        ]
        labels = label_all_cdps(records, [], date(2021, 8, 30), date(2026, 8, 30))
        phase2_successes = [
            label for label in labels if label.phase == 2 and label.label == "success"
        ]
        self.assertEqual(phase2_successes, [])

    def test_flatten_studies_prefers_experimental_other_names(self) -> None:
        studies = [
            {
                "protocolSection": {
                    "identificationModule": {
                        "nctId": "NCT00000016",
                        "briefTitle": "Dose escalation",
                    },
                    "statusModule": {
                        "overallStatus": "RECRUITING",
                        "startDateStruct": {"date": "2024-06-24"},
                    },
                    "conditionsModule": {"conditions": ["Prostate Cancer"]},
                    "designModule": {"studyType": "INTERVENTIONAL", "phases": ["PHASE1"]},
                    "armsInterventionsModule": {
                        "armGroups": [
                            {
                                "label": "0.01mg/kg DGPR1008 Injection Dose Group 1",
                                "type": "EXPERIMENTAL",
                            },
                            {
                                "label": "Dose Group 0",
                                "type": "PLACEBO_COMPARATOR",
                            },
                            {
                                "label": "0.04mg/kg DGPR1008 Injection Dose Group 3",
                                "type": "ACTIVE_COMPARATOR",
                            },
                        ],
                        "interventions": [
                            {
                                "type": "DRUG",
                                "name": "0.01mg/kg DGPR1008 Injection Dose Group 1",
                                "armGroupLabels": [
                                    "0.01mg/kg DGPR1008 Injection Dose Group 1"
                                ],
                                "otherNames": ["DGPR1008"],
                            },
                            {
                                "type": "DRUG",
                                "name": "Dose Group 0",
                                "armGroupLabels": ["Dose Group 0"],
                                "otherNames": ["placebo control group"],
                            },
                            {
                                "type": "DRUG",
                                "name": "0.04mg/kg DGPR1008 Injection Dose Group 3",
                                "armGroupLabels": [
                                    "0.04mg/kg DGPR1008 Injection Dose Group 3"
                                ],
                                "otherNames": ["DGPR1008"],
                            },
                        ],
                    },
                }
            }
        ]
        records = flatten_studies(studies)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].drug_key, "dgpr1008")
        self.assertEqual(records[0].arm_group_types, "EXPERIMENTAL")


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import unittest
from datetime import date

from clinical_trial_success import (
    ApprovalRecord,
    TrialRecord,
    calculate_rates,
    flatten_studies,
    label_all_cdps,
    normalize_drug,
    normalize_phase,
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

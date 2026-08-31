"""ClinSR-style data labeling and success-rate calculation.

This module implements a reproducible approximation of the method in:

Zhou et al. "Dynamic clinical trial success rates for drugs in the 21st
century", Nature Communications (2025), doi:10.1038/s41467-025-64552-2.

The implementation uses public ClinicalTrials.gov API v2 data for trial
progression and, by default, openFDA Drugs@FDA data for drug approval evidence.
It is intentionally conservative: phase labels are emitted as success, failure,
or ongoing; only success and failure labels enter phase success-rate denominators.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import http.client
import importlib.metadata
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Iterable


CLINICALTRIALS_URL = "https://clinicaltrials.gov/api/v2/studies"
OPENFDA_DRUGSFDA_URL = "https://api.fda.gov/drug/drugsfda.json"
APPROVALS_SCHEMA_VERSION = "1"
SYNONYMS_SCHEMA_VERSION = "1"

DRUG_INTERVENTION_TYPES = {"DRUG", "BIOLOGICAL", "GENETIC"}
DISCONTINUED_STATUSES = {
    "TERMINATED",
    "WITHDRAWN",
    "SUSPENDED",
    "NO_LONGER_AVAILABLE",
    "TEMPORARILY_NOT_AVAILABLE",
}
ACTIVE_OR_PENDING_STATUSES = {
    "NOT_YET_RECRUITING",
    "RECRUITING",
    "ENROLLING_BY_INVITATION",
    "ACTIVE_NOT_RECRUITING",
    "AVAILABLE",
}
EXPERIMENTAL_ARM_TYPES = {"EXPERIMENTAL"}
COMPARATOR_ARM_TYPES = {
    "ACTIVE_COMPARATOR",
    "PLACEBO_COMPARATOR",
    "SHAM_COMPARATOR",
    "NO_INTERVENTION",
}
PHASE_VALUES = {
    "EARLY_PHASE1": 1,
    "PHASE1": 1,
    "PHASE2": 2,
    "PHASE3": 3,
}
PHASE_LABELS = {
    1: "Phase 1 to Phase 2",
    2: "Phase 2 to Phase 3",
    3: "Phase 3 to Approval",
}
PLACEBO_OR_CARE_RE = re.compile(
    r"\b(placebo|vehicle|sham|standard of care|best supportive care|usual care|"
    r"physician'?s choice|investigator'?s choice|active comparator)\b",
    re.IGNORECASE,
)
VAGUE_DRUG_RE = re.compile(
    r"^(drug|biological product|biologic|cell therapy|stem cell product|"
    r"car[- ]?t cells?|human umbilical cord mesenchymal stem cells?)$",
    re.IGNORECASE,
)
DOSE_PREFIX_RE = re.compile(
    r"^(very\s+)?(low|medium|mid|high|higher|lower|ascending|single|multiple|"
    r"fixed|loading)\s+(dose|dosage)\s+",
    re.IGNORECASE,
)
TRAILING_ROUTE_RE = re.compile(
    r"\b(tablets?|capsules?|injections?|injectable|solution|suspension|powder|"
    r"infusion|oral|intravenous|subcutaneous|intramuscular|topical)\b",
    re.IGNORECASE,
)
DOSE_OR_ARM_RE = re.compile(
    r"(\b\d+(\.\d+)?\s*(mg/kg|mg|mcg|ug|g|ml|%)\b|"
    r"\b(dose|dosage|group|arm|cohort|part|n\s*=\s*\d+|treatment group)\b)",
    re.IGNORECASE,
)
GENERIC_OTHER_NAME_RE = re.compile(
    r"^(treatment group|study drug|investigational product|experimental drug|"
    r"active treatment|test product|drug product)$",
    re.IGNORECASE,
)
APPROVALS_REQUIRED_COLUMNS = {
    "schema_version",
    "drug",
    "approval_date",
    "source",
    "reviewed_by",
}
SYNONYMS_REQUIRED_COLUMNS = {
    "schema_version",
    "alias",
    "canonical",
    "source",
    "reviewed_by",
}


@dataclass(frozen=True)
class TrialRecord:
    nct_id: str
    brief_title: str
    drug: str
    drug_key: str
    condition: str
    condition_key: str
    phase: int
    intervention_type: str
    overall_status: str
    start_date: date | None
    completion_date: date | None
    arm_group_labels: str = ""
    arm_group_types: str = ""
    association_confidence: str = "study_condition"


@dataclass(frozen=True)
class ApprovalRecord:
    drug: str
    drug_key: str
    approval_date: date
    application_number: str
    submission_type: str
    submission_class_code: str
    source: str
    condition: str = ""
    condition_key: str = ""


@dataclass(frozen=True)
class PhaseLabel:
    cdp_id: str
    drug: str
    drug_key: str
    condition: str
    condition_key: str
    phase: int
    transition: str
    label: str
    label_date: str
    first_start_date: str
    last_activity_date: str
    evidence: str
    trial_ids: str
    association_confidence: str = ""
    approval_application: str = ""
    approval_source: str = ""


@dataclass(frozen=True)
class RateRow:
    window_start: str
    window_end: str
    metric: str
    successes: int | str
    failures: int | str
    ongoing: int | str
    rate: float | str


@dataclass(frozen=True)
class DrugStandardizationReportRow:
    drug_key: str
    trial_records: int
    cdps: int
    unique_surface_forms: int
    unique_source_keys: int
    curated_aliases: str
    sample_surface_forms: str
    needs_review: str


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Fetch ClinicalTrials.gov studies, label ClinSR-style phase "
            "progressions, and calculate success rates."
        )
    )
    parser.add_argument(
        "--start-date",
        help="Inclusive label/fetch window start date. Defaults to end-date minus lookback years.",
    )
    parser.add_argument(
        "--end-date",
        help="Inclusive label/fetch window end date. Defaults to today's local date.",
    )
    parser.add_argument(
        "--lookback-years",
        type=int,
        default=5,
        help="Years to look back when --start-date is omitted. Default: 5.",
    )
    parser.add_argument(
        "--failure-threshold-years",
        type=int,
        default=2,
        help="No-new-trial threshold used to label inactive CDPs as failure. Default: 2.",
    )
    parser.add_argument(
        "--output-dir",
        default="output",
        help=(
            "Directory for trial_records.csv, phase_labels.csv, success_rates.csv, "
            "drug_standardization_report.csv, summary.json."
        ),
    )
    parser.add_argument(
        "--page-size",
        type=int,
        default=1000,
        help="ClinicalTrials.gov page size. Default: 1000.",
    )
    parser.add_argument(
        "--max-studies",
        type=int,
        help="Optional cap for API smoke runs.",
    )
    parser.add_argument(
        "--studies-json",
        help="Use a saved ClinicalTrials.gov API JSON payload instead of fetching live data.",
    )
    parser.add_argument(
        "--save-studies-json",
        help="Optional path for saving the fetched ClinicalTrials.gov studies payload.",
    )
    parser.add_argument(
        "--fetch-history-start-date",
        help=(
            "Optional lower bound for trial-history retrieval. By default, all "
            "matching trial history through --end-date is fetched so CDP "
            "trajectories can cross the analysis window boundary."
        ),
    )
    parser.add_argument(
        "--save-openfda-json",
        help=(
            "Optional path for saving raw openFDA Drugs@FDA records. Defaults "
            "to output/openfda_drugsfda_<start>_<end>.json when openFDA is used."
        ),
    )
    parser.add_argument(
        "--approvals-csv",
        help=(
            "Optional version 1 CSV with condition-specific approval ground truth. "
            "Required columns include schema_version, drug, approval_date, condition, "
            "source, and reviewed_by in the default condition-matching mode."
        ),
    )
    parser.add_argument(
        "--synonyms-csv",
        help=(
            "Optional version 1 CSV with schema_version, alias, canonical, source, "
            "and reviewed_by columns for drug-name normalization."
        ),
    )
    parser.add_argument(
        "--no-openfda",
        action="store_true",
        help="Disable openFDA Drugs@FDA approval retrieval.",
    )
    parser.add_argument(
        "--orig-only",
        action="store_true",
        help="Use only original NDA/BLA approvals from openFDA, excluding efficacy supplements.",
    )
    parser.add_argument(
        "--approval-match",
        choices=("condition", "drug"),
        default="condition",
        help=(
            "Condition-level matching is the default for CDP rates. Use 'drug' "
            "only for a sensitivity analysis that lets conditionless openFDA "
            "approvals count for all indications of a drug."
        ),
    )
    parser.add_argument(
        "--allow-future-end-date",
        action="store_true",
        help="Allow --end-date after the local system date.",
    )
    return parser.parse_args(argv)


def parse_partial_date(value: str | None) -> date | None:
    if not value:
        return None
    value = value.strip()
    for fmt in ("%Y-%m-%d", "%Y-%m", "%Y", "%Y%m%d"):
        try:
            parsed = datetime.strptime(value, fmt)
            return parsed.date()
        except ValueError:
            continue
    raise ValueError(f"Unsupported date format: {value!r}")


def add_years(value: date, years: int) -> date:
    try:
        return value.replace(year=value.year + years)
    except ValueError:
        return value.replace(month=2, day=28, year=value.year + years)


def safe_get(mapping: dict[str, Any], *keys: str, default: Any = None) -> Any:
    current: Any = mapping
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current


def request_json(url: str, params: dict[str, Any], retries: int = 3) -> dict[str, Any]:
    encoded = urllib.parse.urlencode(params)
    full_url = f"{url}?{encoded}"
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            request = urllib.request.Request(
                full_url,
                headers={"User-Agent": "ClinicalTrialSuccess/1.0"},
            )
            with urllib.request.urlopen(request, timeout=60) as response:
                body = response.read().decode("utf-8")
            return json.loads(body)
        except (
            ConnectionError,
            TimeoutError,
            http.client.HTTPException,
            urllib.error.URLError,
            json.JSONDecodeError,
        ) as exc:
            last_error = exc
            if attempt == retries:
                break
            time.sleep(1.5 * attempt)
    raise RuntimeError(f"Failed to retrieve {full_url}: {last_error}") from last_error


def normalize_text(value: str) -> str:
    value = value.lower().strip()
    value = value.replace("&", " and ")
    value = re.sub(r"[\u2018\u2019`]", "'", value)
    value = re.sub(r"[^a-z0-9+./'-]+", " ", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip(" -_'")


def csv_value(row: dict[str, Any], column: str, default: str = "") -> str:
    return str(row.get(column, default) or "").strip()


def csv_row_has_value(row: dict[str, Any]) -> bool:
    return any(str(value or "").strip() for value in row.values())


def require_csv_columns(path: str, fieldnames: Iterable[str] | None, required: set[str]) -> None:
    actual = set(fieldnames or [])
    missing = required - actual
    if missing:
        raise ValueError(f"{path} is missing required columns: {sorted(missing)}")


def validate_schema_version(path: str, row_number: int, value: str, expected: str) -> None:
    version = value.strip()
    if version != expected:
        raise ValueError(
            f"{path} row {row_number} has schema_version {version!r}; expected {expected!r}"
        )


def parse_required_date(path: str, row_number: int, column: str, value: str) -> date:
    try:
        parsed = parse_partial_date(value)
    except ValueError as exc:
        raise ValueError(
            f"{path} row {row_number} has invalid {column}: {value!r}"
        ) from exc
    if not parsed:
        raise ValueError(f"{path} row {row_number} is missing required {column}")
    return parsed


def validate_optional_date(path: str, row_number: int, column: str, value: str) -> None:
    if value:
        parse_required_date(path, row_number, column, value)


def load_synonyms(path: str | None) -> dict[str, str]:
    if not path:
        return {}
    synonyms: dict[str, str] = {}
    with Path(path).open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        require_csv_columns(path, reader.fieldnames, SYNONYMS_REQUIRED_COLUMNS)
        for row_number, row in enumerate(reader, start=2):
            if not csv_row_has_value(row):
                continue
            validate_schema_version(
                path,
                row_number,
                csv_value(row, "schema_version"),
                SYNONYMS_SCHEMA_VERSION,
            )
            validate_optional_date(path, row_number, "reviewed_at", csv_value(row, "reviewed_at"))
            entity_type = csv_value(row, "entity_type").lower()
            if entity_type and entity_type != "drug":
                raise ValueError(
                    f"{path} row {row_number} has entity_type {entity_type!r}; expected 'drug'"
                )
            alias_raw = csv_value(row, "alias")
            canonical_raw = csv_value(row, "canonical")
            if not alias_raw or not canonical_raw:
                raise ValueError(
                    f"{path} row {row_number} must include non-empty alias and canonical values"
                )
            if not csv_value(row, "source") or not csv_value(row, "reviewed_by"):
                raise ValueError(
                    f"{path} row {row_number} must include source and reviewed_by values"
                )
            alias = normalize_text(alias_raw)
            canonical = normalize_text(canonical_raw)
            existing = synonyms.get(alias)
            if existing and existing != canonical:
                raise ValueError(
                    f"{path} row {row_number} maps alias {alias_raw!r} to "
                    f"{canonical_raw!r}, but an earlier row maps it to {existing!r}"
                )
            synonyms[alias] = canonical
    return synonyms


def normalize_drug(value: str, synonyms: dict[str, str] | None = None) -> str:
    value = re.sub(r"^\s*(drug|biological|genetic)\s*:\s*", "", value, flags=re.I)
    value = DOSE_PREFIX_RE.sub("", value.strip())
    value = re.sub(r"^\s*\d+(\.\d+)?\s*(mg/kg|mg|mcg|ug|g|ml|%)\s+", "", value, flags=re.I)
    value = re.sub(r"\s+dose group\b.*$", "", value, flags=re.I)
    value = re.sub(r"\s+to be administered\b.*$", "", value, flags=re.I)
    value = TRAILING_ROUTE_RE.sub(" ", value)
    normalized = normalize_text(value)
    normalized = re.sub(r"\b(low|medium|high)\s+dose\b", " ", normalized)
    normalized = re.sub(r"\b(dose group|group|arm)\s+\d+\b.*$", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip()
    if synonyms and normalized in synonyms:
        return synonyms[normalized]
    return normalized


def normalize_condition(value: str) -> str:
    return normalize_text(value)


def is_excluded_drug_name(value: str) -> bool:
    cleaned = normalize_text(value)
    if not cleaned:
        return True
    if PLACEBO_OR_CARE_RE.search(cleaned):
        return True
    if VAGUE_DRUG_RE.match(cleaned):
        return True
    return False


def normalize_phase(phases: Iterable[str] | None) -> int | None:
    values: list[int] = []
    for phase in phases or []:
        normalized = str(phase).upper().replace(" ", "").replace("_", "")
        if normalized == "EARLYPHASE1":
            normalized = "EARLY_PHASE1"
        elif normalized == "PHASE1":
            normalized = "PHASE1"
        elif normalized == "PHASE2":
            normalized = "PHASE2"
        elif normalized == "PHASE3":
            normalized = "PHASE3"
        elif normalized in {"PHASE4", "NA", "NOTAPPLICABLE"}:
            continue
        else:
            continue
        if normalized in PHASE_VALUES:
            values.append(PHASE_VALUES[normalized])
    if not values:
        return None
    return max(values)


def drug_name_score(value: str) -> tuple[int, int, str]:
    normalized = normalize_text(value)
    score = 0
    if not normalized or is_excluded_drug_name(normalized):
        score += 100
    if GENERIC_OTHER_NAME_RE.match(normalized):
        score += 80
    if DOSE_OR_ARM_RE.search(normalized):
        score += 20
    if len(normalized.split()) > 5:
        score += 10
    if re.match(r"^[a-z]{1,6}[- ]?\d+[a-z0-9-]*$", normalized, re.I):
        score -= 5
    return score, len(normalized), normalized


def choose_intervention_name(intervention: dict[str, Any]) -> str:
    candidates = [str(intervention.get("name", "")).strip()]
    candidates.extend(str(name).strip() for name in intervention.get("otherNames", []) or [])
    candidates = [candidate for candidate in candidates if candidate and not is_excluded_drug_name(candidate)]
    if not candidates:
        return ""
    return min(candidates, key=drug_name_score)


def arm_type_by_label(arms_module: dict[str, Any]) -> dict[str, str]:
    arm_types: dict[str, str] = {}
    for arm in arms_module.get("armGroups", []) or []:
        label = str(arm.get("label", "")).strip()
        arm_type = str(arm.get("type", "")).upper()
        if label:
            arm_types[label] = arm_type
    return arm_types


def intervention_arm_metadata(
    intervention: dict[str, Any],
    arm_types: dict[str, str],
) -> tuple[list[str], list[str]]:
    labels = [str(label).strip() for label in intervention.get("armGroupLabels", []) or []]
    labels = [label for label in labels if label]
    types = sorted({arm_types[label] for label in labels if label in arm_types})
    return labels, types


def is_experimental_intervention(
    intervention: dict[str, Any],
    arm_types: dict[str, str],
) -> bool:
    labels, types = intervention_arm_metadata(intervention, arm_types)
    if not labels:
        return True
    if any(arm_type in EXPERIMENTAL_ARM_TYPES for arm_type in types):
        return True
    if types and all(arm_type in COMPARATOR_ARM_TYPES for arm_type in types):
        return False
    return not types


def fetch_clinicaltrials_studies(
    end_date: date,
    start_date: date | None = None,
    page_size: int = 1000,
    max_studies: int | None = None,
) -> list[dict[str, Any]]:
    fields = ",".join(
        [
            "NCTId",
            "BriefTitle",
            "OverallStatus",
            "WhyStopped",
            "StartDate",
            "CompletionDate",
            "Phase",
            "StudyType",
            "InterventionType",
            "InterventionName",
            "InterventionOtherName",
            "InterventionArmGroupLabel",
            "ArmGroupLabel",
            "ArmGroupType",
            "ArmGroupInterventionName",
            "Condition",
        ]
    )
    start_bound = start_date.isoformat() if start_date else "MIN"
    query_term = (
        "AREA[StudyType]INTERVENTIONAL AND "
        "(AREA[InterventionType]DRUG OR AREA[InterventionType]BIOLOGICAL OR "
        "AREA[InterventionType]GENETIC) AND "
        "(AREA[Phase]PHASE1 OR AREA[Phase]PHASE2 OR AREA[Phase]PHASE3) AND "
        f"AREA[StartDate]RANGE[{start_bound},{end_date.isoformat()}]"
    )
    studies: list[dict[str, Any]] = []
    page_token = ""
    while True:
        effective_page_size = min(max(page_size, 1), 1000)
        if max_studies:
            effective_page_size = min(effective_page_size, max(max_studies - len(studies), 1))
        params: dict[str, Any] = {
            "format": "json",
            "pageSize": effective_page_size,
            "countTotal": "true",
            "fields": fields,
            "query.term": query_term,
        }
        if page_token:
            params["pageToken"] = page_token
        payload = request_json(CLINICALTRIALS_URL, params)
        batch = payload.get("studies", [])
        studies.extend(batch)
        print(
            f"Fetched ClinicalTrials.gov studies: {len(studies)}"
            + (f" / {payload.get('totalCount')}" if payload.get("totalCount") else ""),
            file=sys.stderr,
        )
        if max_studies and len(studies) >= max_studies:
            return studies[:max_studies]
        page_token = payload.get("nextPageToken") or ""
        if not page_token or not batch:
            return studies


def load_studies(path: str) -> list[dict[str, Any]]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(payload, list):
        return payload
    return list(payload.get("studies", []))


def flatten_studies(
    studies: Iterable[dict[str, Any]],
    synonyms: dict[str, str] | None = None,
) -> list[TrialRecord]:
    records: list[TrialRecord] = []
    seen: set[tuple[str, str, str, int]] = set()
    for study in studies:
        protocol = study.get("protocolSection", {})
        ident = protocol.get("identificationModule", {})
        status = protocol.get("statusModule", {})
        design = protocol.get("designModule", {})
        conditions_module = protocol.get("conditionsModule", {})
        interventions_module = protocol.get("armsInterventionsModule", {})

        if str(design.get("studyType", "")).upper() != "INTERVENTIONAL":
            continue
        phase = normalize_phase(design.get("phases", []))
        if phase not in {1, 2, 3}:
            continue

        nct_id = str(ident.get("nctId", "")).strip()
        if not nct_id:
            continue
        brief_title = str(ident.get("briefTitle", "")).strip()
        overall_status = str(status.get("overallStatus", "")).upper()
        start = parse_partial_date(safe_get(status, "startDateStruct", "date"))
        if not start:
            continue
        completion = parse_partial_date(safe_get(status, "completionDateStruct", "date"))

        conditions = [
            condition
            for condition in conditions_module.get("conditions", [])
            if normalize_condition(str(condition))
        ]
        if not conditions:
            continue
        interventions = interventions_module.get("interventions", [])
        arm_types = arm_type_by_label(interventions_module)
        candidates: list[tuple[str, str, str, str, str]] = []
        for intervention in interventions:
            intervention_type = str(intervention.get("type", "")).upper()
            if intervention_type not in DRUG_INTERVENTION_TYPES:
                continue
            if not is_experimental_intervention(intervention, arm_types):
                continue
            drug = choose_intervention_name(intervention)
            if is_excluded_drug_name(drug):
                continue
            drug_key = normalize_drug(drug, synonyms)
            if not drug_key:
                continue
            labels, types = intervention_arm_metadata(intervention, arm_types)
            candidates.append(
                (
                    drug,
                    drug_key,
                    intervention_type,
                    ";".join(labels),
                    ";".join(types),
                )
            )
        for drug, drug_key, intervention_type, arm_labels, arm_type_text in candidates:
            confidence = (
                "direct_study_condition"
                if len(candidates) == 1 or len(conditions) == 1
                else "study_level_cartesian"
            )
            for condition in conditions:
                condition_text = str(condition).strip()
                condition_key = normalize_condition(condition_text)
                key = (nct_id, drug_key, condition_key, phase)
                if key in seen:
                    continue
                seen.add(key)
                records.append(
                    TrialRecord(
                        nct_id=nct_id,
                        brief_title=brief_title,
                        drug=drug,
                        drug_key=drug_key,
                        condition=condition_text,
                        condition_key=condition_key,
                        phase=phase,
                        intervention_type=intervention_type,
                        overall_status=overall_status,
                        start_date=start,
                        completion_date=completion,
                        arm_group_labels=arm_labels,
                        arm_group_types=arm_type_text,
                        association_confidence=confidence,
                    )
                )
    return records


def openfda_approval_query(start_date: date, end_date: date) -> str:
    start = start_date.strftime("%Y%m%d")
    end = end_date.strftime("%Y%m%d")
    return (
        f"(submissions.submission_status_date:[{start} TO {end}]) AND "
        'submissions.submission_status:"AP" AND '
        "(application_number:NDA* OR application_number:BLA*)"
    )


def iter_openfda_results(
    start_date: date,
    end_date: date,
    limit: int = 100,
) -> Iterable[dict[str, Any]]:
    query = openfda_approval_query(start_date, end_date)
    skip = 0
    total: int | None = None
    while True:
        payload = request_json(
            OPENFDA_DRUGSFDA_URL,
            {"search": query, "limit": limit, "skip": skip},
        )
        meta_results = safe_get(payload, "meta", "results", default={})
        if total is None:
            total = meta_results.get("total")
        results = payload.get("results", [])
        if not results:
            break
        for result in results:
            yield result
        skip += len(results)
        print(
            f"Fetched openFDA approval applications: {skip}"
            + (f" / {total}" if total else ""),
            file=sys.stderr,
        )
        if total is not None and skip >= total:
            break


def approval_submission_dates(
    record: dict[str, Any],
    start_date: date,
    end_date: date,
    include_efficacy_supplements: bool,
) -> list[tuple[date, str, str]]:
    approvals: list[tuple[date, str, str]] = []
    for submission in record.get("submissions", []):
        if str(submission.get("submission_status", "")).upper() != "AP":
            continue
        approval_date = parse_partial_date(str(submission.get("submission_status_date", "")))
        if not approval_date or not (start_date <= approval_date <= end_date):
            continue
        submission_type = str(submission.get("submission_type", "")).upper()
        class_code = str(submission.get("submission_class_code", "")).upper()
        class_description = str(
            submission.get("submission_class_code_description", "")
        ).upper()
        is_original = submission_type == "ORIG"
        is_efficacy_supplement = (
            include_efficacy_supplements
            and submission_type == "SUPPL"
            and ("EFFICACY" in class_code or "EFFICACY" in class_description)
        )
        if is_original or is_efficacy_supplement:
            approvals.append((approval_date, submission_type, class_code))
    return approvals


def approval_names(record: dict[str, Any]) -> set[str]:
    names: set[str] = set()
    openfda = record.get("openfda", {})
    for field in ("brand_name", "generic_name", "substance_name"):
        for value in openfda.get(field, []) or []:
            if value:
                names.add(str(value))
    for product in record.get("products", []) or []:
        brand = product.get("brand_name")
        if brand:
            names.add(str(brand))
        ingredients = [
            str(item.get("name", "")).strip()
            for item in product.get("active_ingredients", []) or []
            if item.get("name")
        ]
        for ingredient in ingredients:
            names.add(ingredient)
        if len(ingredients) > 1:
            names.add(" and ".join(ingredients))
    return names


def fetch_openfda_approvals(
    start_date: date,
    end_date: date,
    synonyms: dict[str, str] | None = None,
    include_efficacy_supplements: bool = True,
    raw_records: list[dict[str, Any]] | None = None,
) -> list[ApprovalRecord]:
    approvals: list[ApprovalRecord] = []
    seen: set[tuple[str, date, str, str, str]] = set()
    for record in iter_openfda_results(start_date, end_date):
        if raw_records is not None:
            raw_records.append(record)
        application_number = str(record.get("application_number", "")).upper()
        if not (application_number.startswith("NDA") or application_number.startswith("BLA")):
            continue
        dates = approval_submission_dates(
            record,
            start_date,
            end_date,
            include_efficacy_supplements=include_efficacy_supplements,
        )
        if not dates:
            continue
        names = approval_names(record)
        for approval_date, submission_type, class_code in dates:
            for name in names:
                if is_excluded_drug_name(name):
                    continue
                key = normalize_drug(name, synonyms)
                dedupe_key = (key, approval_date, application_number, submission_type, class_code)
                if not key or dedupe_key in seen:
                    continue
                seen.add(dedupe_key)
                approvals.append(
                    ApprovalRecord(
                        drug=name,
                        drug_key=key,
                        approval_date=approval_date,
                        application_number=application_number,
                        submission_type=submission_type,
                        submission_class_code=class_code,
                        source="openFDA Drugs@FDA",
                    )
                )
    return approvals


def load_approvals_csv(
    path: str | None,
    synonyms: dict[str, str] | None = None,
    require_condition: bool = True,
) -> list[ApprovalRecord]:
    if not path:
        return []
    approvals: list[ApprovalRecord] = []
    seen: dict[tuple[str, str, date], int] = {}
    with Path(path).open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        required = set(APPROVALS_REQUIRED_COLUMNS)
        if require_condition:
            required.add("condition")
        require_csv_columns(path, reader.fieldnames, required)
        for row_number, row in enumerate(reader, start=2):
            if not csv_row_has_value(row):
                continue
            validate_schema_version(
                path,
                row_number,
                csv_value(row, "schema_version"),
                APPROVALS_SCHEMA_VERSION,
            )
            validate_optional_date(path, row_number, "reviewed_at", csv_value(row, "reviewed_at"))
            drug = csv_value(row, "drug")
            canonical_drug = csv_value(row, "canonical_drug") or drug
            condition = csv_value(row, "condition")
            canonical_condition = csv_value(row, "canonical_condition") or condition
            if not drug:
                raise ValueError(f"{path} row {row_number} is missing required drug")
            if require_condition and not condition:
                raise ValueError(
                    f"{path} row {row_number} is missing condition; strict CDP "
                    "approval matching requires indication-specific approvals"
                )
            if not csv_value(row, "source") or not csv_value(row, "reviewed_by"):
                raise ValueError(
                    f"{path} row {row_number} must include source and reviewed_by values"
                )
            approval_date = parse_required_date(
                path,
                row_number,
                "approval_date",
                csv_value(row, "approval_date"),
            )
            drug_key = normalize_drug(canonical_drug, synonyms)
            condition_key = normalize_condition(canonical_condition) if canonical_condition else ""
            if not drug_key:
                raise ValueError(f"{path} row {row_number} normalizes to an empty drug key")
            if require_condition and not condition_key:
                raise ValueError(f"{path} row {row_number} normalizes to an empty condition key")
            duplicate_key = (drug_key, condition_key, approval_date)
            previous_row = seen.get(duplicate_key)
            if previous_row:
                raise ValueError(
                    f"{path} row {row_number} duplicates canonical drug-condition approval "
                    f"from row {previous_row}: {drug_key!r}, {condition_key!r}, "
                    f"{approval_date.isoformat()}"
                )
            seen[duplicate_key] = row_number
            approvals.append(
                ApprovalRecord(
                    drug=canonical_drug,
                    drug_key=drug_key,
                    approval_date=approval_date,
                    application_number=csv_value(row, "application_number"),
                    submission_type=csv_value(row, "submission_type", "CSV") or "CSV",
                    submission_class_code=csv_value(row, "submission_class_code"),
                    source=csv_value(row, "source"),
                    condition=canonical_condition,
                    condition_key=condition_key,
                )
            )
    return approvals


def cdp_identifier(drug_key: str, condition_key: str) -> str:
    digest = hashlib.sha1(f"{drug_key}|{condition_key}".encode("utf-8")).hexdigest()
    return digest[:12]


def group_cdps(records: Iterable[TrialRecord]) -> dict[tuple[str, str], list[TrialRecord]]:
    cdps: dict[tuple[str, str], list[TrialRecord]] = {}
    for record in records:
        cdps.setdefault((record.drug_key, record.condition_key), []).append(record)
    for group in cdps.values():
        group.sort(
            key=lambda item: (
                item.start_date or date.min,
                item.completion_date or date.min,
                item.phase,
                item.nct_id,
            )
        )
    return cdps


def index_approvals(
    approvals: Iterable[ApprovalRecord],
) -> dict[str, list[ApprovalRecord]]:
    indexed: dict[str, list[ApprovalRecord]] = {}
    for approval in approvals:
        indexed.setdefault(approval.drug_key, []).append(approval)
    for records in indexed.values():
        records.sort(key=lambda item: item.approval_date)
    return indexed


def max_date(values: Iterable[date | None]) -> date | None:
    actual = [value for value in values if value is not None]
    return max(actual) if actual else None


def min_date(values: Iterable[date | None]) -> date | None:
    actual = [value for value in values if value is not None]
    return min(actual) if actual else None


def date_to_string(value: date | None) -> str:
    return value.isoformat() if value else ""


def in_window(value: date | None, window_start: date, window_end: date) -> bool:
    return value is not None and window_start <= value <= window_end


def find_approval(
    drug_key: str,
    condition_key: str,
    approvals_by_drug: dict[str, list[ApprovalRecord]],
    earliest_allowed: date | None,
    window_end: date,
    allow_conditionless_approvals: bool = False,
) -> ApprovalRecord | None:
    for approval in approvals_by_drug.get(drug_key, []):
        if approval.condition_key:
            if approval.condition_key != condition_key:
                continue
        elif not allow_conditionless_approvals:
            continue
        if earliest_allowed and approval.approval_date < earliest_allowed:
            continue
        if approval.approval_date <= window_end:
            return approval
    return None


def transition_success_from_trial(
    phase: int,
    phase_records: list[TrialRecord],
    all_records: list[TrialRecord],
    window_end: date,
) -> TrialRecord | None:
    first_start = min_date(record.start_date for record in phase_records)
    candidates = []
    for record in all_records:
        if record.phase <= phase or not record.start_date:
            continue
        if first_start and record.start_date < first_start:
            continue
        if record.start_date <= window_end:
            candidates.append(record)
    return min(candidates, key=lambda item: item.start_date or date.max) if candidates else None


def has_active_or_later_trial_after(
    records: list[TrialRecord],
    phase: int,
    after_date: date | None,
    window_end: date,
) -> bool:
    if not after_date:
        return False
    for record in records:
        if not record.start_date:
            continue
        if record.phase < phase or record.start_date > window_end:
            continue
        if record.overall_status in DISCONTINUED_STATUSES:
            continue
        activity_end = record.completion_date
        if record.overall_status in ACTIVE_OR_PENDING_STATUSES and (
            activity_end is None or activity_end > window_end
        ):
            activity_end = window_end
        if record.start_date > after_date:
            return True
        if activity_end and activity_end >= after_date:
            return True
    return False


def make_phase_label(
    records: list[TrialRecord],
    phase: int,
    label: str,
    label_date: date | None,
    first_start: date | None,
    last_activity: date | None,
    evidence: str,
    approval: ApprovalRecord | None = None,
) -> PhaseLabel:
    first = records[0]
    trial_ids = ";".join(sorted({record.nct_id for record in records}))
    association_confidence = ";".join(
        sorted({record.association_confidence for record in records if record.association_confidence})
    )
    return PhaseLabel(
        cdp_id=cdp_identifier(first.drug_key, first.condition_key),
        drug=first.drug,
        drug_key=first.drug_key,
        condition=first.condition,
        condition_key=first.condition_key,
        phase=phase,
        transition=PHASE_LABELS[phase],
        label=label,
        label_date=date_to_string(label_date),
        first_start_date=date_to_string(first_start),
        last_activity_date=date_to_string(last_activity),
        evidence=evidence,
        trial_ids=trial_ids,
        association_confidence=association_confidence,
        approval_application=approval.application_number if approval else "",
        approval_source=approval.source if approval else "",
    )


def label_cdp(
    records: list[TrialRecord],
    approvals_by_drug: dict[str, list[ApprovalRecord]],
    window_start: date,
    window_end: date,
    failure_threshold_years: int = 2,
    allow_conditionless_approvals: bool = False,
) -> list[PhaseLabel]:
    if not records:
        return []

    labels: list[PhaseLabel] = []
    by_phase: dict[int, list[TrialRecord]] = {phase: [] for phase in (1, 2, 3)}
    for record in records:
        by_phase[record.phase].append(record)

    phases_observed = {record.phase for record in records}

    for phase in (1, 2, 3):
        phase_records = by_phase[phase]
        if not phase_records:
            # The paper counts direct jumps as success for skipped phases.
            lower = [record for record in records if record.phase < phase]
            higher = [record for record in records if record.phase > phase]
            lower_start = min_date(record.start_date for record in lower)
            lower_activity = max_date(record.completion_date or record.start_date for record in lower)
            higher_after_lower = [
                record
                for record in higher
                if record.start_date
                and (lower_activity is None or record.start_date >= lower_activity)
                and record.start_date <= window_end
            ]
            jumped_to_higher = min_date(record.start_date for record in higher_after_lower)
            if lower and higher_after_lower and jumped_to_higher:
                if in_window(jumped_to_higher, window_start, window_end):
                    labels.append(
                        make_phase_label(
                            lower + higher_after_lower,
                            phase,
                            "success",
                            jumped_to_higher,
                            lower_start,
                            max_date(
                                record.completion_date or record.start_date
                                for record in lower + higher_after_lower
                            ),
                            "imputed_success_from_phase_jump",
                        )
                    )
                continue
            if lower:
                approval = find_approval(
                    records[0].drug_key,
                    records[0].condition_key,
                    approvals_by_drug,
                    lower_start,
                    window_end,
                    allow_conditionless_approvals=allow_conditionless_approvals,
                )
                if approval and phase <= 3 and in_window(approval.approval_date, window_start, window_end):
                    labels.append(
                        make_phase_label(
                            lower,
                            phase,
                            "success",
                            approval.approval_date,
                            lower_start,
                            max_date(record.completion_date or record.start_date for record in lower),
                            "imputed_success_from_direct_approval",
                            approval,
                        )
                    )
            continue

        first_start = min_date(record.start_date for record in phase_records)
        last_activity = max_date(
            record.completion_date or record.start_date for record in phase_records
        )

        higher_trial = transition_success_from_trial(phase, phase_records, records, window_end)
        approval = find_approval(
            records[0].drug_key,
            records[0].condition_key,
            approvals_by_drug,
            first_start,
            window_end,
            allow_conditionless_approvals=allow_conditionless_approvals,
        )

        if phase < 3 and higher_trial:
            if not in_window(higher_trial.start_date, window_start, window_end):
                continue
            labels.append(
                make_phase_label(
                    phase_records,
                    phase,
                    "success",
                    higher_trial.start_date,
                    first_start,
                    last_activity,
                    f"progressed_to_phase_{higher_trial.phase}",
                )
            )
            continue
        if approval and (phase == 3 or phase < 3):
            if not in_window(approval.approval_date, window_start, window_end):
                continue
            labels.append(
                make_phase_label(
                    phase_records,
                    phase,
                    "success",
                    approval.approval_date,
                    first_start,
                    last_activity,
                    "progressed_to_approval",
                    approval,
                )
            )
            continue

        discontinued = [
            record
            for record in phase_records
            if record.overall_status in DISCONTINUED_STATUSES
        ]
        discontinued.sort(
            key=lambda item: item.completion_date or item.start_date or date.max
        )
        if discontinued:
            failure_anchor = discontinued[-1].completion_date or discontinued[-1].start_date
            if failure_anchor and failure_anchor <= window_end and not has_active_or_later_trial_after(
                records, phase, failure_anchor, window_end
            ):
                if in_window(failure_anchor, window_start, window_end):
                    labels.append(
                        make_phase_label(
                            phase_records,
                            phase,
                            "failure",
                            failure_anchor,
                            first_start,
                            last_activity,
                            "discontinued_or_terminated_without_later_trial",
                        )
                    )
                continue

        if last_activity and add_years(last_activity, failure_threshold_years) <= window_end:
            failure_date = add_years(last_activity, failure_threshold_years)
            if in_window(failure_date, window_start, window_end):
                labels.append(
                    make_phase_label(
                        phase_records,
                        phase,
                        "failure",
                        failure_date,
                        first_start,
                        last_activity,
                        f"no_new_trial_for_{failure_threshold_years}_years",
                    )
                )
            continue

        evidence = "active_or_boundary_ongoing"
        if any(record.overall_status in ACTIVE_OR_PENDING_STATUSES for record in phase_records):
            evidence = "active_trial_status"
        elif phase == 3 and not approvals_by_drug.get(records[0].drug_key):
            evidence = "no_approval_match_and_within_failure_threshold"
        elif phase not in phases_observed:
            evidence = "not_observed"

        labels.append(
            make_phase_label(
                phase_records,
                phase,
                "ongoing",
                None,
                first_start,
                last_activity,
                evidence,
            )
        )

    return labels


def label_all_cdps(
    records: Iterable[TrialRecord],
    approvals: Iterable[ApprovalRecord],
    window_start: date,
    window_end: date,
    failure_threshold_years: int = 2,
    allow_conditionless_approvals: bool = False,
) -> list[PhaseLabel]:
    approvals_by_drug = index_approvals(approvals)
    labels: list[PhaseLabel] = []
    for cdp_records in group_cdps(records).values():
        labels.extend(
            label_cdp(
                cdp_records,
                approvals_by_drug,
                window_start=window_start,
                window_end=window_end,
                failure_threshold_years=failure_threshold_years,
                allow_conditionless_approvals=allow_conditionless_approvals,
            )
        )
    labels.sort(key=lambda item: (item.phase, item.drug_key, item.condition_key, item.label))
    return labels


def calculate_rates(
    labels: Iterable[PhaseLabel],
    window_start: date,
    window_end: date,
    unestimable_phases: set[int] | None = None,
) -> list[RateRow]:
    rows: list[RateRow] = []
    phase_rates: dict[int, float | None] = {}
    unestimable_phases = unestimable_phases or set()
    label_list = list(labels)
    for phase in (1, 2, 3):
        phase_labels = [label for label in label_list if label.phase == phase]
        terminal_labels = [
            label
            for label in phase_labels
            if label.label in {"success", "failure"}
            and in_window(parse_partial_date(label.label_date), window_start, window_end)
        ]
        successes = sum(1 for label in terminal_labels if label.label == "success")
        failures = sum(1 for label in terminal_labels if label.label == "failure")
        ongoing = sum(1 for label in phase_labels if label.label == "ongoing")
        denominator = successes + failures
        rate: float | str
        if phase in unestimable_phases:
            phase_rate = None
            rate = ""
        elif denominator:
            phase_rate: float | None = successes / denominator
            rate = round(phase_rate, 6)
        else:
            phase_rate = None
            rate = ""
        phase_rates[phase] = phase_rate
        rows.append(
            RateRow(
                window_start=window_start.isoformat(),
                window_end=window_end.isoformat(),
                metric=f"P{phase}SR",
                successes=successes,
                failures=failures,
                ongoing=ongoing,
                rate=rate,
            )
        )

    if all(rate is not None for rate in phase_rates.values()):
        osr = 1.0
        for rate in phase_rates.values():
            assert rate is not None
            osr *= rate
        osr_value: float | str = round(osr, 6)
    else:
        osr_value = ""
    rows.append(
        RateRow(
            window_start=window_start.isoformat(),
            window_end=window_end.isoformat(),
            metric="OSR",
            successes="",
            failures="",
            ongoing="",
            rate=osr_value,
        )
    )
    return rows


def write_csv(path: Path, rows: Iterable[Any]) -> None:
    row_list = list(rows)
    if not row_list:
        path.write_text("", encoding="utf-8")
        return
    dictionaries = [asdict(row) for row in row_list]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(dictionaries[0].keys()))
        writer.writeheader()
        writer.writerows(dictionaries)


def write_trial_records(path: Path, records: Iterable[TrialRecord]) -> None:
    rows: list[dict[str, Any]] = []
    for record in records:
        row = asdict(record)
        row["start_date"] = date_to_string(record.start_date)
        row["completion_date"] = date_to_string(record.completion_date)
        rows.append(row)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def build_drug_standardization_report(
    records: Iterable[TrialRecord],
    synonyms: dict[str, str] | None = None,
) -> list[DrugStandardizationReportRow]:
    synonym_map = synonyms or {}
    aliases_by_canonical: dict[str, set[str]] = {}
    for alias, canonical in synonym_map.items():
        aliases_by_canonical.setdefault(canonical, set()).add(alias)

    grouped: dict[str, dict[str, Any]] = {}
    for record in records:
        group = grouped.setdefault(
            record.drug_key,
            {
                "trial_records": 0,
                "conditions": set(),
                "surface_forms": set(),
                "source_keys": set(),
            },
        )
        group["trial_records"] += 1
        group["conditions"].add(record.condition_key)
        if record.drug:
            group["surface_forms"].add(record.drug)
            group["source_keys"].add(normalize_drug(record.drug))

    rows: list[DrugStandardizationReportRow] = []
    for drug_key, group in grouped.items():
        surface_forms = sorted(group["surface_forms"])
        source_keys = sorted(group["source_keys"])
        curated_aliases = sorted(aliases_by_canonical.get(drug_key, set()))
        has_fragmentation = len(surface_forms) > 1 or len(source_keys) > 1
        needs_review = has_fragmentation and not curated_aliases
        if not has_fragmentation and not curated_aliases:
            continue
        rows.append(
            DrugStandardizationReportRow(
                drug_key=drug_key,
                trial_records=group["trial_records"],
                cdps=len(group["conditions"]),
                unique_surface_forms=len(surface_forms),
                unique_source_keys=len(source_keys),
                curated_aliases=";".join(curated_aliases[:20]),
                sample_surface_forms=";".join(surface_forms[:20]),
                needs_review=str(needs_review).lower(),
            )
        )

    rows.sort(
        key=lambda row: (
            row.needs_review != "true",
            -row.unique_surface_forms,
            -row.unique_source_keys,
            -row.trial_records,
            row.drug_key,
        )
    )
    return rows


def write_drug_standardization_report(
    path: Path,
    rows: Iterable[DrugStandardizationReportRow],
) -> None:
    fieldnames = [
        "drug_key",
        "trial_records",
        "cdps",
        "unique_surface_forms",
        "unique_source_keys",
        "curated_aliases",
        "sample_surface_forms",
        "needs_review",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def print_rates(rows: Iterable[RateRow]) -> None:
    print("metric,successes,failures,ongoing,rate")
    for row in rows:
        rate = row.rate
        if isinstance(rate, float):
            rate_text = f"{rate:.2%}"
        else:
            rate_text = ""
        print(f"{row.metric},{row.successes},{row.failures},{row.ongoing},{rate_text}")


def package_version(package: str) -> str:
    try:
        return importlib.metadata.version(package)
    except importlib.metadata.PackageNotFoundError:
        return ""


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main(argv: list[str] | None = None) -> int:
    cli_args = argv or sys.argv[1:]
    args = parse_args(cli_args)
    end_date = parse_partial_date(args.end_date) or date.today()
    start_date = parse_partial_date(args.start_date) or add_years(end_date, -args.lookback_years)
    if start_date > end_date:
        raise ValueError("--start-date must be on or before --end-date")
    if end_date > date.today() and not args.allow_future_end_date:
        raise ValueError(
            f"--end-date {end_date.isoformat()} is after local system date "
            f"{date.today().isoformat()}; use --allow-future-end-date to override."
        )

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    synonyms = load_synonyms(args.synonyms_csv)
    history_start_date = parse_partial_date(args.fetch_history_start_date)

    if args.studies_json:
        studies = load_studies(args.studies_json)
        if args.max_studies:
            studies = studies[: args.max_studies]
    else:
        studies = fetch_clinicaltrials_studies(
            end_date=end_date,
            start_date=history_start_date,
            page_size=args.page_size,
            max_studies=args.max_studies,
        )
        if args.save_studies_json:
            Path(args.save_studies_json).write_text(
                json.dumps({"studies": studies}, indent=2),
                encoding="utf-8",
            )

    records = flatten_studies(studies, synonyms)
    approvals: list[ApprovalRecord] = []
    openfda_raw_records: list[dict[str, Any]] = []
    if not args.no_openfda:
        approvals.extend(
            fetch_openfda_approvals(
                start_date=start_date,
                end_date=end_date,
                synonyms=synonyms,
                include_efficacy_supplements=not args.orig_only,
                raw_records=openfda_raw_records,
            )
        )
        openfda_json_path = Path(
            args.save_openfda_json
            or output_dir / f"openfda_drugsfda_{start_date.isoformat()}_{end_date.isoformat()}.json"
        )
        openfda_json_path.write_text(
            json.dumps({"results": openfda_raw_records}, indent=2),
            encoding="utf-8",
        )
    else:
        openfda_json_path = None
    approvals.extend(
        load_approvals_csv(
            args.approvals_csv,
            synonyms,
            require_condition=args.approval_match == "condition",
        )
    )

    labels = label_all_cdps(
        records,
        approvals,
        window_start=start_date,
        window_end=end_date,
        failure_threshold_years=args.failure_threshold_years,
        allow_conditionless_approvals=args.approval_match == "drug",
    )
    condition_specific_approval_records = sum(1 for approval in approvals if approval.condition_key)
    unestimable_phases = (
        {3}
        if args.approval_match == "condition" and condition_specific_approval_records == 0
        else set()
    )
    rates = calculate_rates(
        labels,
        window_start=start_date,
        window_end=end_date,
        unestimable_phases=unestimable_phases,
    )

    studies_json_artifact = args.save_studies_json or args.studies_json or ""
    approvals_csv_path = Path(args.approvals_csv) if args.approvals_csv else None
    synonyms_csv_path = Path(args.synonyms_csv) if args.synonyms_csv else None
    standardization_report_path = output_dir / "drug_standardization_report.csv"
    standardization_report_rows = build_drug_standardization_report(records, synonyms)

    write_trial_records(output_dir / "trial_records.csv", records)
    write_csv(output_dir / "phase_labels.csv", labels)
    write_csv(output_dir / "success_rates.csv", rates)
    write_drug_standardization_report(
        standardization_report_path,
        standardization_report_rows,
    )
    (output_dir / "summary.json").write_text(
        json.dumps(
            {
                "window_start": start_date.isoformat(),
                "window_end": end_date.isoformat(),
                "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
                "command_args": cli_args,
                "analysis": {
                    "lookback_years": args.lookback_years,
                    "failure_threshold_years": args.failure_threshold_years,
                    "approval_match": args.approval_match,
                    "approvals_schema_version": APPROVALS_SCHEMA_VERSION,
                    "synonyms_schema_version": SYNONYMS_SCHEMA_VERSION,
                    "unestimable_phases": sorted(unestimable_phases),
                    "fetch_history_start_date": date_to_string(history_start_date),
                    "max_studies": args.max_studies,
                    "page_size": args.page_size,
                    "orig_only": args.orig_only,
                },
                "source": {
                    "clinicaltrials_gov": CLINICALTRIALS_URL,
                    "openfda_drugsfda": None if args.no_openfda else OPENFDA_DRUGSFDA_URL,
                    "clinicaltrials_query": (
                        "AREA[StudyType]INTERVENTIONAL AND "
                        "(AREA[InterventionType]DRUG OR AREA[InterventionType]BIOLOGICAL OR AREA[InterventionType]GENETIC) AND "
                        "(AREA[Phase]PHASE1 OR AREA[Phase]PHASE2 OR AREA[Phase]PHASE3) AND "
                        f"AREA[StartDate]RANGE[{history_start_date.isoformat() if history_start_date else 'MIN'},{end_date.isoformat()}]"
                    ),
                    "openfda_query": None
                    if args.no_openfda
                    else openfda_approval_query(start_date, end_date),
                },
                "runtime": {
                    "python": sys.version,
                    "pypdf": package_version("pypdf"),
                },
                "artifacts": {
                    "studies_json": studies_json_artifact,
                    "openfda_json": str(openfda_json_path) if openfda_json_path else "",
                    "approvals_csv": str(approvals_csv_path) if approvals_csv_path else "",
                    "synonyms_csv": str(synonyms_csv_path) if synonyms_csv_path else "",
                    "drug_standardization_report": str(standardization_report_path),
                    "studies_json_sha256": file_sha256(Path(studies_json_artifact))
                    if studies_json_artifact and Path(studies_json_artifact).exists()
                    else "",
                    "openfda_json_sha256": file_sha256(openfda_json_path)
                    if openfda_json_path and openfda_json_path.exists()
                    else "",
                    "approvals_csv_sha256": file_sha256(approvals_csv_path)
                    if approvals_csv_path and approvals_csv_path.exists()
                    else "",
                    "synonyms_csv_sha256": file_sha256(synonyms_csv_path)
                    if synonyms_csv_path and synonyms_csv_path.exists()
                    else "",
                },
                "studies": len(studies),
                "trial_records": len(records),
                "cdps": len(group_cdps(records)),
                "approval_records": len(approvals),
                "condition_specific_approval_records": condition_specific_approval_records,
                "drug_standardization_report_rows": len(standardization_report_rows),
                "openfda_conditionless_approval_records": sum(
                    1 for approval in approvals if approval.source == "openFDA Drugs@FDA" and not approval.condition_key
                ),
                "phase_labels": len(labels),
                "rates": [asdict(row) for row in rates],
                "method_notes": [
                    "CDPs are approximated by normalized drug-condition pairs.",
                    "Phase 1/2 is treated as Phase 2; Phase 2/3 is treated as Phase 3.",
                    "Failure uses a two-year no-new-trial threshold unless overridden.",
                    "By default, conditionless openFDA approvals are saved as evidence but do not count as CDP successes; use --approval-match drug only for sensitivity analysis.",
                    "When condition-level approval evidence is absent, strict P3SR and OSR are left blank rather than reported as zero.",
                    "Use a version 1 --approvals-csv for condition-specific Phase 3 approval labels.",
                    "Use a version 1 --synonyms-csv and review drug_standardization_report.csv to reduce unresolved drug-name fragmentation.",
                    "The paper recommends nine-year windows for robust dynamic ClinSR; this run uses the requested five-year window.",
                ],
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    print_rates(rates)
    print(f"\nWrote outputs to {output_dir.resolve()}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

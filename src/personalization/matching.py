from dataclasses import dataclass
from typing import Dict, Iterable, List

from .fitid import FitID
from .garment import GarmentSpec


@dataclass(frozen=True)
class RegionAssessment:
    region: str
    required_cm: float
    available_cm: float
    gap_cm: float
    risk: str


@dataclass(frozen=True)
class FitAssessment:
    garment_id: str
    score: float
    regions: List[RegionAssessment]
    explanations: List[str]


def _risk(gap_cm: float) -> str:
    if gap_cm < -2.0:
        return "high-tightness-risk"
    if gap_cm < 0.0:
        return "tightness-risk"
    if gap_cm > 5.0:
        return "loose-fit-risk"
    return "within-target"


def assess_fit(fitid: FitID, garment: GarmentSpec, regions: Iterable[str]) -> FitAssessment:
    assessments: List[RegionAssessment] = []
    penalties = 0.0
    explanations: List[str] = []

    for region in regions:
        required = fitid.required_garment_measurement(region)
        available = garment.effective_measurement(region)
        gap = round(available - required, 2)
        risk = _risk(gap)
        assessments.append(RegionAssessment(region, required, available, gap, risk))

        if risk == "high-tightness-risk":
            penalties += 35.0
        elif risk == "tightness-risk":
            penalties += 18.0
        elif risk == "loose-fit-risk":
            penalties += 10.0

        explanations.append(
            f"{region}: garment provides {available:.1f}cm vs {required:.1f}cm target ({gap:+.1f}cm, {risk})"
        )

    score = max(0.0, 100.0 - penalties)
    return FitAssessment(garment.garment_id, score, assessments, explanations)

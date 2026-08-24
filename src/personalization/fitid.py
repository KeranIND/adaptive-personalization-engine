from dataclasses import dataclass, field
from enum import Enum
from typing import Dict


class FitPreference(str, Enum):
    SLIM = "slim"
    REGULAR = "regular"
    RELAXED = "relaxed"


@dataclass(frozen=True)
class FitID:
    fitid_id: str
    user_id: str
    version: int
    body_measurements_cm: Dict[str, float]
    preferred_ease_cm: Dict[str, float] = field(default_factory=dict)
    fit_preference: FitPreference = FitPreference.REGULAR
    style_intent: Dict[str, str] = field(default_factory=dict)

    def required_garment_measurement(self, region: str) -> float:
        body = self.body_measurements_cm.get(region, 0.0)
        ease = self.preferred_ease_cm.get(region, 0.0)
        return body + ease

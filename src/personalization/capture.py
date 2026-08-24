from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from typing import Dict, Optional


class CaptureMethod(str, Enum):
    MANUAL = "manual"
    GUIDED = "guided"
    PHONE_SCAN = "phone_scan"
    IN_PERSON_SCAN = "in_person_scan"


@dataclass(frozen=True)
class MeasurementCapture:
    capture_id: str
    user_id: str
    method: CaptureMethod
    measurements_cm: Dict[str, float]
    confidence: Dict[str, float]
    source_device: Optional[str] = None
    captured_at: datetime = datetime.now(timezone.utc)

    def validated(self, minimum_confidence: float = 0.75) -> Dict[str, float]:
        return {
            name: value
            for name, value in self.measurements_cm.items()
            if self.confidence.get(name, 0.0) >= minimum_confidence
        }

    def provenance(self) -> Dict[str, str]:
        return {
            "capture_id": self.capture_id,
            "method": self.method.value,
            "source_device": self.source_device or "unspecified",
            "captured_at": self.captured_at.isoformat(),
        }

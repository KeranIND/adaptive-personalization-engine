from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict


@dataclass(frozen=True)
class FitFeedback:
    feedback_id: str
    user_id: str
    garment_id: str
    fitid_version: int
    garment_spec_version: str
    region_feedback: Dict[str, str]
    overall_rating: int
    captured_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def evidence(self) -> Dict[str, str]:
        return {
            **{f"region:{key}": value for key, value in self.region_feedback.items()},
            "overall_rating": str(self.overall_rating),
            "fitid_version": str(self.fitid_version),
            "garment_spec_version": self.garment_spec_version,
        }

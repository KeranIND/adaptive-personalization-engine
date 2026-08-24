from dataclasses import dataclass, field
from typing import Dict


@dataclass(frozen=True)
class GarmentSpec:
    garment_id: str
    category: str
    spec_version: str
    finished_measurements_cm: Dict[str, float]
    fabric_stretch_pct: float = 0.0
    silhouette: str = "regular"
    construction: Dict[str, str] = field(default_factory=dict)

    def effective_measurement(self, region: str) -> float:
        base = self.finished_measurements_cm.get(region, 0.0)
        return base * (1.0 + self.fabric_stretch_pct / 100.0)

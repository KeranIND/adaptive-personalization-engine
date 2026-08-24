from dataclasses import dataclass
from enum import Enum
from typing import Dict


class ViewPreset(str, Enum):
    FRONT = "front"
    SIDE = "side"
    BACK = "back"


@dataclass(frozen=True)
class VisualizationRequest:
    user_id: str
    fitid_version: int
    garment_id: str
    garment_spec_version: str
    avatar_asset_id: str
    garment_mesh_id: str
    preset: ViewPreset = ViewPreset.FRONT

    def cache_key(self) -> str:
        return ":".join(
            [
                self.user_id,
                str(self.fitid_version),
                self.garment_id,
                self.garment_spec_version,
                self.avatar_asset_id,
                self.garment_mesh_id,
                self.preset.value,
            ]
        )


def measurement_callout_payload(
    measurements_cm: Dict[str, float],
    anchor_map: Dict[str, str],
) -> Dict[str, Dict[str, object]]:
    """Build world-anchored callout metadata rather than screen-positioned labels."""
    return {
        name: {
            "value_cm": value,
            "anchor": anchor_map[name],
        }
        for name, value in measurements_cm.items()
        if name in anchor_map
    }

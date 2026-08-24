from personalization.capture import CaptureMethod, MeasurementCapture
from personalization.visualization import ViewPreset, VisualizationRequest, measurement_callout_payload


def test_capture_filters_low_confidence_measurements():
    capture = MeasurementCapture(
        capture_id="cap-1",
        user_id="u-1",
        method=CaptureMethod.PHONE_SCAN,
        measurements_cm={"chest": 102.0, "waist": 88.0},
        confidence={"chest": 0.92, "waist": 0.60},
        source_device="phone-camera",
    )
    assert capture.validated(0.75) == {"chest": 102.0}
    assert capture.provenance()["method"] == "phone_scan"


def test_visualization_key_versions_fit_and_garment_state():
    request = VisualizationRequest(
        user_id="u-1",
        fitid_version=3,
        garment_id="shirt-17",
        garment_spec_version="spec-v5",
        avatar_asset_id="avatar-1",
        garment_mesh_id="mesh-shirt-17",
        preset=ViewPreset.SIDE,
    )
    assert "3" in request.cache_key()
    assert "spec-v5" in request.cache_key()
    assert request.cache_key().endswith("side")


def test_measurement_callouts_require_explicit_world_anchor():
    payload = measurement_callout_payload(
        {"chest": 102.0, "waist": 88.0},
        {"chest": "skeleton:spine_chest"},
    )
    assert payload == {
        "chest": {"value_cm": 102.0, "anchor": "skeleton:spine_chest"}
    }

from personalization.fitid import FitID, FitPreference
from personalization.garment import GarmentSpec
from personalization.matching import assess_fit


def test_fitid_matches_garment_with_region_level_explanations():
    fitid = FitID(
        fitid_id="fit-1",
        user_id="u-1",
        version=3,
        body_measurements_cm={"chest": 100.0, "waist": 88.0},
        preferred_ease_cm={"chest": 8.0, "waist": 6.0},
        fit_preference=FitPreference.REGULAR,
    )
    garment = GarmentSpec(
        garment_id="shirt-1",
        category="shirt",
        spec_version="v5",
        finished_measurements_cm={"chest": 110.0, "waist": 95.0},
    )

    result = assess_fit(fitid, garment, ["chest", "waist"])

    assert result.score == 100.0
    assert result.regions[0].gap_cm == 2.0
    assert result.regions[1].gap_cm == 1.0
    assert "chest" in result.explanations[0]


def test_tight_garment_is_penalized():
    fitid = FitID(
        fitid_id="fit-2",
        user_id="u-2",
        version=1,
        body_measurements_cm={"chest": 104.0},
        preferred_ease_cm={"chest": 8.0},
    )
    garment = GarmentSpec(
        garment_id="shirt-tight",
        category="shirt",
        spec_version="v1",
        finished_measurements_cm={"chest": 106.0},
    )

    result = assess_fit(fitid, garment, ["chest"])
    assert result.score == 65.0
    assert result.regions[0].risk == "high-tightness-risk"

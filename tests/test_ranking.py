from datetime import datetime, timezone

from personalization.events import Event, EventType
from personalization.profile import build_category_affinity
from personalization.ranking import Candidate, rank_candidates


def test_purchase_outweighs_view_and_skip():
    now = datetime.now(timezone.utc)
    events = [
        Event("u1", "p1", "shirts", EventType.PURCHASE, now),
        Event("u1", "p2", "pants", EventType.VIEW, now),
        Event("u1", "p3", "pants", EventType.SKIP, now),
    ]
    affinity = build_category_affinity(events)
    ranked = rank_candidates(
        [Candidate("shirt-2", "shirts"), Candidate("pants-2", "pants")],
        affinity,
    )
    assert ranked[0].product_id == "shirt-2"
    assert ranked[0].explanation["category_affinity"] == 4.0

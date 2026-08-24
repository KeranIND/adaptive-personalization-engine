from collections import defaultdict
from typing import DefaultDict, Dict, Iterable

from .events import Event, EventType


EVENT_WEIGHTS = {
    EventType.VIEW: 1.0,
    EventType.CART: 2.0,
    EventType.PURCHASE: 4.0,
    EventType.SKIP: -1.0,
    EventType.RETURN: -3.0,
}


def build_category_affinity(events: Iterable[Event]) -> Dict[str, float]:
    scores: DefaultDict[str, float] = defaultdict(float)
    for event in events:
        scores[event.category] += EVENT_WEIGHTS[event.event_type]
    return dict(scores)

from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class EventType(str, Enum):
    VIEW = "product_view"
    CART = "add_to_cart"
    PURCHASE = "purchase"
    SKIP = "skip"
    RETURN = "return"


@dataclass(frozen=True)
class Event:
    user_id: str
    product_id: str
    category: str
    event_type: EventType
    occurred_at: datetime

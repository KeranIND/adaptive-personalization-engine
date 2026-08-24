from dataclasses import dataclass
from typing import Dict, Iterable, List


@dataclass(frozen=True)
class Candidate:
    product_id: str
    category: str
    base_score: float = 0.0


@dataclass(frozen=True)
class RankedCandidate:
    product_id: str
    score: float
    explanation: Dict[str, float]


def rank_candidates(candidates: Iterable[Candidate], affinity: Dict[str, float]) -> List[RankedCandidate]:
    ranked = []
    for candidate in candidates:
        category_score = affinity.get(candidate.category, 0.0)
        total = candidate.base_score + category_score
        ranked.append(
            RankedCandidate(
                product_id=candidate.product_id,
                score=total,
                explanation={"base": candidate.base_score, "category_affinity": category_score},
            )
        )
    return sorted(ranked, key=lambda item: item.score, reverse=True)

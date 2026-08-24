# Adaptive Personalization Engine

A small event-driven recommendation engine that updates user preference state from observed behavior and ranks products transparently.

The point of this project is not to hide everything behind an ML model. It is to make the feedback loop inspectable: what happened, which features changed, why a product moved up or down, and how the system can reproduce a decision.

## Feedback loop

```text
Behavior event
    ↓
Event ingestion
    ↓
User feature state
    ↓
Scoring / ranking
    ↓
Recommendation
    ↓
Outcome event
    ↺
```

## Events

Supported examples:

- product_view
- add_to_cart
- purchase
- skip
- return

Each event contributes a configurable weight to category and attribute affinities.

## Design principles

- deterministic scoring before opaque modeling
- event history separated from derived feature state
- reproducible recommendations
- explainable per-feature contributions
- easy path from in-memory prototype to persistent/event-stream implementation

## Repository structure

```text
src/personalization/
  events.py
  profile.py
  ranking.py
tests/
  test_ranking.py
```

This is a generic public reference implementation. It does not contain Chanamill's proprietary FitID or fit-matching logic.
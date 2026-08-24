# Architecture

## Goal

Build a recommendation system whose decisions can be reproduced and explained from observable user behavior.

## Pipeline

```text
Behavior event
   ↓
Append to event history
   ↓
Derive user feature state
   ↓
Score candidates
   ↓
Rank + explain
   ↓
Observe outcome
   ↺
```

## Why event-derived state

User preference is modeled as derived state rather than an opaque mutable blob. Given the same event history and weighting configuration, the system should reproduce the same profile and ranking result.

This gives three operational advantages:

- historical replay after scoring changes
- easier debugging of unexpected recommendations
- clean separation between observed facts and derived features

## Current scoring model

The reference implementation maintains category affinity from weighted behavioral events. Purchase is positive evidence; return is negative evidence; view/cart interactions provide weaker signals.

Ranking is the sum of a candidate's base score and the relevant user affinity. Each ranked item includes the contribution breakdown.

## Production evolution

A larger system would add:

- durable event storage
- streaming feature updates
- event-time decay
- attribute and embedding features
- exploration/exploitation policies
- feature versioning
- offline evaluation and replay
- experiment assignment
- model-serving boundaries

The architecture deliberately keeps event ingestion, feature derivation, and ranking separate so each can evolve independently.

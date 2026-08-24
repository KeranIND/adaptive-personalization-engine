# FitID Architecture

## Context

Chanamill's fit problem is not equivalent to recommending a product category. The decision depends on the relationship between a versioned person profile and a versioned garment specification.

## Boundaries

### FitID
Owns customer-side fit state:
- body measurements
- preferred ease
- fit preference
- style intent
- version history

### Garment specification
Owns product-side physical state:
- finished garment measurements
- construction attributes
- fabric behavior metadata
- silhouette
- spec version

### Fit assessment
Pure decision layer:
- compares a FitID snapshot to a garment spec
- produces region-level gaps
- flags fit risks
- returns explanations

### Feedback evidence
Captures post-delivery observations without rewriting historical decisions:
- FitID version used for the order
- garment spec version used for production
- region-level customer feedback
- overall fit rating

## Reproducibility

A recommendation should be reconstructable later. For that reason, an order should reference immutable versions rather than "the current profile" and "the current garment".

```text
Order
 ├── fitid_snapshot_id
 ├── garment_spec_version
 └── assessment_version
```

This matters when a customer updates measurements after purchase or a pattern/spec changes between production runs.

## Separation of signals

Fit, style, and behavioral preference should not collapse into one opaque score.

```text
fit score          → physical compatibility
style score        → aesthetic preference
behavioral score   → learned interaction affinity
business rules     → availability / production constraints
```

A final recommendation can combine these layers while preserving an explanation for each component.

## Closed-loop direction

```text
FitID + garment spec
       ↓
fit assessment
       ↓
order
       ↓
manufacturing
       ↓
delivery
       ↓
fit feedback
       ↓
evidence for future FitID / spec decisions
```

This public repository demonstrates the domain architecture. Chanamill's private capture algorithms, calibration logic, data, and production integrations are intentionally excluded.
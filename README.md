# Chanamill FitID Personalization Engine

A public-safe implementation of the **core systems pattern behind Chanamill**: represent a shopper's body measurements and fit preferences as a versioned FitID, compare that profile against garment specifications, explain the recommendation, and learn from delivered-fit feedback.

This repository is directly tied to Chanamill's product architecture. It intentionally excludes proprietary measurement algorithms, private production code, provisional-patent details, supplier data, and any non-public fit heuristics.

## Core loop

```text
Measurement capture
      ↓
Versioned FitID
  body measurements
  fit preferences
  style intent
      ↓
Garment specification
  finished measurements
  fabric/stretch metadata
  construction attributes
      ↓
Explainable fit matcher
      ↓
Recommendation / MTM adjustments
      ↓
Purchase + delivered garment
      ↓
Fit feedback
      ↓
Updated FitID evidence
```

## Why this is not a generic recommender

Apparel fit depends on the relationship between **two physical models**:

1. the person's measurements and desired ease
2. the garment's finished measurements and construction

A category-affinity model alone cannot answer whether a shirt will fit someone's chest, shoulder, waist, or sleeve preference. The public implementation therefore separates:

- behavioral preference signals
- body-measurement state
- fit-preference state
- garment specifications
- fit-gap calculations
- recommendation explanations
- post-delivery feedback

## Domain model

```text
FitID
  ├── body measurements
  ├── preferred ease by region
  ├── fit preference
  └── version

GarmentSpec
  ├── garment measurements
  ├── fabric stretch
  ├── silhouette
  └── spec version

FitAssessment
  ├── region gaps
  ├── risk flags
  ├── score
  └── explanations
```

## Repository structure

```text
src/personalization/
  fitid.py
  garment.py
  matching.py
  feedback.py
  events.py
  profile.py
  ranking.py

tests/
  test_fit_matching.py
  test_feedback.py
  test_ranking.py

docs/
  fitid-architecture.md
```

The original event/ranking modules remain because Chanamill also needs to distinguish **fit intelligence** from **behavioral personalization**. A shopper can prefer a style while still being a poor fit for a specific garment spec.

## Public implementation principles

- explicit calculations instead of opaque recommendations
- immutable profile/spec versions for reproducibility
- region-level fit explanations
- fit feedback stored as evidence, not destructive overwrites
- separation of fit, style, and behavioral signals
- deterministic baseline that can later be augmented with learned models

## Relationship to the product

Chanamill already includes FitID creation, measurement onboarding, explainable apparel recommendations, garment visualization, and made-to-measure flows. Additional body-capture and 3D/phone-measurement work is being developed separately. This repository presents the underlying domain architecture in a form that can be publicly reviewed without publishing the production application or protected IP.

Product: https://chanamill.com

Demo: https://youtu.be/Ucau6x7gyYk
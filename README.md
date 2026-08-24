# Chanamill FitID Personalization Engine

A public-safe implementation of the **core systems pattern behind Chanamill**: capture measurements with provenance, represent body state and fit preferences as a versioned FitID, compare that profile against garment specifications, explain the recommendation, drive visualization, and learn from delivered-fit feedback.

This repository is directly tied to Chanamill's product architecture. It intentionally excludes proprietary measurement algorithms, private production code, provisional-patent details, supplier data, and non-public fit heuristics.

## End-to-end loop

```text
Measurement capture
 manual / guided / phone / in-person
          ↓
Capture provenance + confidence
          ↓
Versioned FitID
 body measurements
 preferred ease
 fit intent
          ↓
Garment specification
 finished measurements
 fabric / stretch
 silhouette
          ↓
Explainable fit matcher
          ↓
Recommendation / MTM adjustment
          ↓
3D visualization boundary
 avatar + garment mesh + camera preset
          ↓
Purchase / manufacturing
          ↓
Delivered-fit feedback
          ↓
Versioned evidence for future decisions
```

## Measurement capture

`capture.py` models a requirement that became important while designing Chanamill's measurement workflows: a measurement value is not enough by itself.

The system also needs:

- capture method
- confidence
- device/session provenance
- timestamp
- the FitID version derived from it

Supported public abstractions include manual, guided, phone-scan, and in-person-scan capture methods.

## FitID vs garment specifications

Apparel fit depends on the relationship between **two physical models**:

1. the person's body measurements and desired ease
2. the garment's finished measurements, fabric behavior and construction

The implementation keeps these models separate and produces region-level fit gaps and explanations rather than collapsing everything into a generic recommendation score.

## 3D visualization boundary

`visualization.py` reflects the architecture used in the Chanamill 3D work:

```text
FitID version
Garment spec version
Avatar asset
Garment mesh
      ↓
VisualizationRequest
      ↓
FRONT / SIDE / BACK camera preset
      ↓
world-anchored measurement callouts
```

The renderer is deliberately downstream of fit logic. Visual presentation should explain a decision, not silently become the source of truth for body measurements or fit.

The public model also treats measurement callouts as **world/model anchored**, because fixed screen-coordinate callouts become incorrect when a 3D avatar rotates.

## Behavioral personalization stays separate

The original event/ranking modules remain intentionally.

Chanamill needs to distinguish:

- **fit** — whether a garment specification works for the person's body and desired ease
- **style/preference** — what the shopper likes
- **behavior** — views, carts, purchases, skips and returns

A shopper can strongly prefer a style while still being a poor fit for a specific garment spec. Mixing those signals into one opaque number would make the system harder to debug and improve.

## Domain model

```text
MeasurementCapture
  ├── method
  ├── values
  ├── confidence
  └── provenance

FitID
  ├── measurements
  ├── preferred ease
  ├── fit intent
  └── version

GarmentSpec
  ├── finished measurements
  ├── stretch / construction
  ├── silhouette
  └── version

FitAssessment
  ├── region gaps
  ├── risk flags
  ├── score
  └── explanations

VisualizationRequest
  ├── FitID version
  ├── garment-spec version
  ├── avatar asset
  ├── garment mesh
  └── camera preset

FitFeedback
  ├── region feedback
  ├── overall rating
  ├── FitID version
  └── garment-spec version
```

## Repository structure

```text
src/personalization/
  capture.py
  fitid.py
  garment.py
  matching.py
  visualization.py
  feedback.py
  events.py
  profile.py
  ranking.py

tests/
  test_capture_visualization.py
  test_fit_matching.py
  test_feedback.py
  test_ranking.py

docs/
  fitid-architecture.md
```

## Product relationship

Chanamill product work has included FitID creation, measurement onboarding, explainable shirt/pant recommendations, garment visualization, made-to-measure flows, mobile scanning/image experiments, Flutter prototypes, and current 3D avatar/garment workflows. Phone-based body capture and more advanced visualization continue to evolve separately from this public reference implementation.

The architectural goal is a reusable fit identity that improves as real garments are ordered, produced, delivered and evaluated.

Product: https://chanamill.com

Demo: https://youtu.be/Ucau6x7gyYk
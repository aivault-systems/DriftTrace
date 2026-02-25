# DriftTrace

Enterprise Core Runtime Guard for Autonomous AI Systems.

DriftTrace evaluates behavioral drift inside autonomous agent execution flows and produces a structured Drift Event in real time.

## API Overview

POST /evaluate

Input:
- objective
- steps
- context

Output:
- drift_score
- severity
- objective_fidelity
- reason
- recommendation
- verdict

## Runtime Behavior

DriftTrace evaluates agent execution steps against the original objective.

If deviation exceeds a defined threshold, a structured Drift Event is generated.

The consuming platform decides whether to:
- Allow execution
- Trigger review
- Block action

DriftTrace does not replace orchestration.
It produces a runtime signal that can be consumed by enforcement or workflow systems.

## Core Runtime Capabilities

- Objective representation tracking
- Multi step directional deviation scoring
- Cumulative divergence monitoring
- Threshold based drift classification
- Structured runtime telemetry emission

## Signals Produced

Each evaluation produces:
- drift_score
- severity
- objective_fidelity
- reason
- recommendation
- verdict

Signals are export ready for SIEM, XDR, orchestration engines, or governance pipelines.

## Quickstart

Install dependencies:

pip install -r requirements.txt

Run the API locally:

python -m uvicorn app:app --reload

Open:

http://127.0.0.1:8000/docs

## Positioning

DriftTrace is a Core Runtime Guard module.

It transforms hidden reasoning drift into structured governance telemetry during execution.

## Design Partner Program

We are opening a limited design partner program for organizations building autonomous AI agents.

See details in:
DESIGN_PARTNER.md

For enterprise design partnership inquiries:
aivault@aivaultsystems.com
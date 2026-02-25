# DriftTrace

Agent Runtime Guard for Enterprise AI Systems.

Lightweight runtime module that evaluates objective deviation and produces a structured Drift Event during agent execution.

API Overview

POST /evaluate

Input

objective

steps

context

Output

drift_score

severity

objective_fidelity

reason

recommendation

verdict

Runtime Behavior

DriftTrace evaluates agent execution steps against the original objective.

If deviation exceeds a defined threshold, a structured Drift Event is generated.

The consuming platform decides whether to:

Allow execution

Trigger review

Block action

DriftTrace does not replace orchestration.
It produces a runtime signal that can be consumed by enforcement or workflow systems.

Runtime Enforcement Demo

![Runtime Enforcement Demo](enforcement.gif)

What Problem It Solves

Autonomous agents rarely fail instantly.
They drift.

Minor reasoning deviations accumulate across multi step execution.
The final output may appear valid while internal intent has already diverged.

Traditional monitoring detects issues after execution.
DriftTrace provides objective deviation scoring during execution.

Core Runtime Capabilities

Objective representation tracking

Multi step directional deviation scoring

Cumulative divergence monitoring

Threshold based drift classification

Structured runtime telemetry emission

Signals Produced

Each evaluation produces a structured Drift Event containing:

drift_score

severity

objective_fidelity

reason

recommendation

verdict

Events are export ready for orchestration engines, SOAR systems, SIEM pipelines, or workflow automation layers.

Quickstart

Install dependencies:

pip install -r requirements.txt

Run the API locally:

python -m uvicorn app:app --reload

Open:

http://127.0.0.1:8000/docs

Integration Model

DriftTrace sits between:

Agent Reasoning Layer
Tool Execution Layer

It evaluates intent before execution, not after failure.

No retraining required.
No modification of foundation model.
Designed to integrate with existing agent orchestration frameworks.

Positioning

DriftTrace is an Agent Runtime Guard module.

It transforms drift detection from postmortem analysis into structured runtime signaling that platform teams can act upon.

Design Partner Program

We are opening a limited design partner program for organizations building autonomous AI agents.

See full details here:

Design Partner Program

[Design Partner Program](DESIGN_PARTNER.md)

For enterprise design partnership inquiries:
Contact: aivault@aivaultsystems.com


# DriftTrace

Objective drift detection layer for autonomous AI agents before visible failure.

## Live Demo

![DriftTrace Demo](demo.gif)

Run locally:

    python drifttrace.py demo

Runtime behavioral drift detection signal layer for enterprise AI runtime environments.

In under 5 seconds DriftTrace simulates multi step agent behavior and detects objective drift in real time.

Overview

DriftTrace measures how far an autonomous agent deviates from its original objective during multi step execution.

Instead of waiting for visible failure, DriftTrace produces a structured drift signal in real time that can be forwarded to security and observability systems.

## Integration Concept

DriftTrace emits structured runtime signals such as drift_score, severity, and objective_fidelity.
These signals can be forwarded to XDR, SIEM, or runtime protection pipelines.
Designed to plug into existing security telemetry flows.
No model modification required.

The Problem

Autonomous agents rarely fail instantly.
They drift.

Small reasoning deviations accumulate across steps. Minor objective reinterpretations compound. The final output may still look acceptable while the internal trajectory has already diverged.

Security teams need an early warning signal, not a postmortem.

What DriftTrace Produces

DriftTrace outputs a small set of signals that are easy to ingest:

drift_score — continuous score that increases as objective deviation grows

severity — normalized level derived from drift_score and thresholds

objective_fidelity — estimated alignment of the current step to the original objective

step_index — where the drift was observed

metadata — optional context for correlation

Core Capabilities

Objective representation tracking

Multi step deviation scoring

Cumulative divergence monitoring

Threshold based alerting

Exportable telemetry record for pipelines

Quickstart

Install dependencies

pip install -r requirements.txt

Run demo

python drifttrace.py demo

The demo simulates multi step agent execution and detects objective drift automatically.

Usage Example

Conceptual usage during multi step agent execution:
from drifttrace import DriftTrace

engine = DriftTrace(objective="Generate financial risk summary")

for step in agent_execution_steps:
    signal = engine.evaluate(step)

    if signal["severity"] in ["HIGH", "CRITICAL"]:
        print("Behavioral drift detected")

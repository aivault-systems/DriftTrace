# DriftTrace

Runtime behavioral drift detection signal layer for enterprise AI runtime environments.

## Overview

DriftTrace measures how far an autonomous agent deviates from its original objective during multi step execution.

Instead of waiting for visible failure, DriftTrace produces a structured drift signal in real time that can be forwarded to security and observability systems.

## The Problem

Autonomous agents rarely fail instantly.  
They drift.

Small reasoning deviations accumulate across steps. Minor objective reinterpretations compound. The final output may still look acceptable while the internal trajectory has already diverged.

Security teams need an early warning signal, not a postmortem.

## What DriftTrace Produces

DriftTrace outputs a small set of signals that are easy to ingest:

1. drift_score, a continuous score that increases as objective deviation grows  
2. severity, a normalized level derived from drift_score and thresholds  
3. objective_fidelity, estimated alignment of the current step to the original objective  
4. step_index, where the drift was observed  
5. metadata, optional context for correlation  

## Core Capabilities

1. Objective representation tracking  
2. Multi step deviation scoring  
3. Cumulative divergence monitoring  
4. Threshold based alerting  
5. Exportable telemetry record for pipelines  

## Quickstart

Install dependencies

pip install -r requirements.txt

Run

python drifttrace.py

## Usage Example

Conceptual usage during multi step agent execution:

```python
from drifttrace import DriftTrace

engine = DriftTrace(objective="Generate financial risk summary")

for step in agent_execution_steps:
    signal = engine.evaluate(step)

    if signal["severity"] in ["HIGH", "CRITICAL"]:
        print("Behavioral drift detected")

# DriftTrace

The first runtime control gateway that actively blocks autonomous agent drift before tool execution.

Autonomous agents can silently drift into unsafe actions. DriftTrace evaluates intent in real time and stops execution before damage occurs.

Runtime Enforcement Demo

![Runtime Enforcement Demo](enforcement.gif)

Run live gateway:

DriftTrace evaluates every agent step before tool execution.
If behavioral deviation exceeds a defined threshold, the action is blocked.

No model modification required.
Zero configuration sidecar architecture.

What Problem It Solves

Autonomous agents rarely fail instantly.
They drift.

Minor reasoning deviations accumulate across multi step execution.
The final output may appear valid while internal intent has already diverged.

Traditional monitoring detects issues after execution.
DriftTrace enforces control before execution.

Core Runtime Capabilities

Objective representation tracking

Multi step directional deviation scoring

Cumulative divergence monitoring

Threshold based enforcement

Tool call interception

Structured runtime telemetry emission

Runtime Architecture

DriftTrace consists of two components:

Drift Engine

Computes directional drift score using objective similarity and behavioral continuity weighting.

Drift Gateway

Intercepts tool calls in real time.
Applies enforcement policy.
Returns ALLOW or BLOCK verdict before execution.

Designed as a drop in sidecar for agent systems.

Signals Produced

Each evaluated step produces:

drift_score

severity

objective_fidelity

step_index

reason

verdict

Signals are structured and export ready for XDR, SIEM, or runtime governance pipelines.

Quickstart

Install dependencies:

Install dependencies:

pip install -r requirements.txt

Run runtime gateway demo:

python drift_gateway.py live --workdir .

You will see:

Drift scoring per step

Severity classification

Runtime ALLOW or BLOCK decision

Enforcement trigger when threshold exceeded

Integration Concept

DriftTrace sits between:

Agent Reasoning Layer
Tool Execution Layer

It evaluates intent before execution, not after failure.

No retraining required.
No modification of foundation model.
Works with existing agent orchestration frameworks.

Example Conceptual Usage

from drifttrace import DriftTrace

engine = DriftTrace(objective="Generate financial risk summary")

for step in agent_execution_steps:
    signal = engine.evaluate(step)

    if signal["severity"] in ["HIGH", "CRITICAL"]:
        print("Behavioral drift detected")
Positioning

DriftTrace is a runtime behavioral control layer for enterprise AI systems.

It transforms drift detection from postmortem analysis into active runtime enforcement.

Design Partner Program

We are opening a limited design partner program for organizations building autonomous AI agents.

See full details here:

[Design Partner Program](DESIGN_PARTNER.md)

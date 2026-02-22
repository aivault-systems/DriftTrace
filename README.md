# DriftTrace

Objective drift detection engine for autonomous AI agents.

## Overview

DriftTrace is a runtime behavioral validation engine for autonomous AI agents.

Instead of asking whether an agent succeeded or failed, DriftTrace measures how far the agent’s execution trajectory deviates from its original objective during multi step reasoning.

It quantifies behavioral divergence over time before visible failure occurs.

## The Problem

Autonomous agents do not fail instantly.

They drift.

Small reasoning deviations accumulate across steps.  
Minor objective reinterpretations compound.  
The final output may look correct while the internal trajectory is no longer aligned with the original intent.

There is currently no simple structured metric that measures this drift in real time.

## What DriftTrace Does

DriftTrace compares intermediate reasoning states against the original objective representation and produces a cumulative deviation score.

Core capabilities:

- Objective embedding comparison  
- Multi step deviation scoring  
- Cumulative behavioral divergence tracking  
- Threshold based drift alerting  

## How to Run

Install dependencies:

pip install -r requirements.txt

Run:

python drifttrace.py

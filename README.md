# DriftTrace

Objective drift detection for autonomous agents.

DriftTrace monitors an agent task step by step and estimates how far each action drifts from the original objective.

## Why it feels different

DriftTrace uses multi vector alignment so legitimate workflows stay calm, while weird pivots spike immediately.

* Global alignment, compare each step against the original objective
* Sequential logic, compare each step against the previous accepted step
* Max similarity filter, keep the strongest semantic link to reduce false alarms
* Directional check, detect behavioral direction shifts even if single steps look harmless

## Quick start

### 1 Install

Create a virtual environment, then install dependencies.

```bash
pip install -r requirements.txt
```

### 2 Run the demo

```bash
python drifttrace.py demo
```

You should see step scores, plus short reasoning lines that explain what matched.

### 3 Run with your own task

Edit task.yaml and then run

```bash
python drifttrace.py run task.yaml
```

## Task file format

task.yaml contains:

* objective, the base goal
* steps, a list of agent actions, real or simulated
* thresholds, drift threshold settings

Example

```yaml
objective: Organize image files by year
thresholds:
  alert: 0.85
steps:
  - Scanning downloads folder for image files
  - Identifying JPG and PNG files
  - Reading creation year from image metadata
  - Moving files into target year folders
  - Accessing browser history to find user preferences
```

## Audit log

DriftTrace writes a JSON lines audit file so you can replay and analyze.

Default path is audit.jsonl.

Each line contains:

* timestamp
* objective
* step_index
* step_text
* drift_score
* sim_obj and sim_prev when available
* decision and reason

## Project layout

* drifttrace.py, CLI entry point
* drift_engine.py, embedding model cache and scoring logic
* task.yaml, example task
* audit.jsonl, example output

## Notes

The first run downloads the embedding model from Hugging Face and may take a moment.

On Windows, Python may print a warning about unauthenticated hub requests, it is safe to ignore for this demo.

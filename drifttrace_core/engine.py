import re
from typing import List, Dict


def normalize(text: str) -> List[str]:
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text.split()


def compute_fidelity(objective_tokens: List[str], step_tokens: List[str]) -> float:
    if not objective_tokens:
        return 0.0

    overlap = len(set(objective_tokens) & set(step_tokens))
    return overlap / len(set(objective_tokens))


def evaluate(objective: str, steps: List[str], context: Dict[str, str]) -> Dict:

    objective_tokens = normalize(objective)

    fidelity_scores = []
    for step in steps:
        step_tokens = normalize(step)
        fidelity = compute_fidelity(objective_tokens, step_tokens)
        fidelity_scores.append(fidelity)

    if fidelity_scores:
        avg_fidelity = sum(fidelity_scores) / len(fidelity_scores)
    else:
        avg_fidelity = 0.0

    drift_score = round(1 - avg_fidelity, 3)

    if drift_score > 0.7:
        severity = "HIGH"
        verdict = "BLOCK"
        recommendation = "Block tool execution"
    elif drift_score > 0.4:
        severity = "MEDIUM"
        verdict = "REVIEW"
        recommendation = "Manual review before execution"
    else:
        severity = "LOW"
        verdict = "ALLOW"
        recommendation = "Proceed with execution"

    return {
        "drift_score": drift_score,
        "severity": severity,
        "objective_fidelity": round(avg_fidelity, 3),
        "reason": "Objective deviation based on token overlap analysis",
        "recommendation": recommendation,
        "verdict": verdict,
        "metadata": {
            "engine_version": "core_v1",
            "steps_evaluated": str(len(steps))
        }
    }
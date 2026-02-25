from pydantic import BaseModel
from typing import List, Dict, Optional


class DriftRequest(BaseModel):
    objective: str
    steps: List[str]
    context: Optional[Dict[str, str]] = {}


class DriftResponse(BaseModel):
    drift_score: float
    severity: str
    objective_fidelity: float
    reason: str
    recommendation: str
    verdict: str
    metadata: Dict[str, str]
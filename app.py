from fastapi import FastAPI
from drifttrace_core.schemas import DriftRequest, DriftResponse
from drifttrace_core.engine import evaluate

app = FastAPI(title="DriftTrace Core API", version="1.0")

@app.post("/evaluate", response_model=DriftResponse)
def evaluate_drift(request: DriftRequest):
    result = evaluate(
        objective=request.objective,
        steps=request.steps,
        context=request.context or {}
    )
    return result
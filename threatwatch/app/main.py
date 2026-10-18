"""HTTP entrypoint for the ThreatWatch prototype."""

from fastapi import FastAPI
from app.schemas import TrafficFeatures, AnalysisResult
from app.scoring import analyze_traffic

app = FastAPI(title="ThreatWatch API", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "detector": "rule_based_baseline"}


@app.post("/api/v1/analyze", response_model=AnalysisResult)
def analyze(payload: TrafficFeatures) -> AnalysisResult:
    return analyze_traffic(payload)

"""Request and response contracts for the API."""

from pydantic import BaseModel, Field


class TrafficFeatures(BaseModel):
    duration_seconds: float = Field(ge=0, le=86400)
    packets: int = Field(ge=0, le=10_000_000)
    bytes_transferred: int = Field(ge=0, le=10_000_000_000)
    destination_port: int = Field(ge=0, le=65535)
    failed_connections: int = Field(ge=0, le=1_000_000)


class AnalysisResult(BaseModel):
    label: str
    risk_score: int = Field(ge=0, le=100)
    reasons: list[str]
    detector: str = "rule_based_baseline"

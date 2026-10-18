"""Explainable baseline, not a machine-learning prediction."""

from app.schemas import AnalysisResult, TrafficFeatures


def analyze_traffic(traffic: TrafficFeatures) -> AnalysisResult:
    score = 0
    reasons: list[str] = []

    if traffic.failed_connections >= 10:
        score += 55
        reasons.append("High number of failed connections")

    if traffic.duration_seconds > 0:
        packet_rate = traffic.packets / traffic.duration_seconds
        if packet_rate > 1000:
            score += 35
            reasons.append("Unusually high packet rate")

    if traffic.destination_port in {21, 23}:
        score += 10
        reasons.append("Traffic uses a legacy plaintext service port")

    score = min(score, 100)
    label = "suspicious" if score >= 50 else "normal"
    return AnalysisResult(label=label, risk_score=score, reasons=reasons)

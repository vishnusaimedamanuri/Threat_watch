from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_suspicious_traffic():
    response = client.post("/api/v1/analyze", json={
        "duration_seconds": 1,
        "packets": 2000,
        "bytes_transferred": 100000,
        "destination_port": 22,
        "failed_connections": 12,
    })
    assert response.status_code == 200
    assert response.json()["label"] == "suspicious"
    assert response.json()["detector"] == "rule_based_baseline"


def test_normal_traffic():
    response = client.post("/api/v1/analyze", json={
        "duration_seconds": 20,
        "packets": 40,
        "bytes_transferred": 4096,
        "destination_port": 443,
        "failed_connections": 0,
    })
    assert response.json()["label"] == "normal"


def test_invalid_input_rejected():
    response = client.post("/api/v1/analyze", json={
        "duration_seconds": -1,
        "packets": 10,
        "bytes_transferred": 100,
        "destination_port": 443,
        "failed_connections": 0,
    })
    assert response.status_code == 422

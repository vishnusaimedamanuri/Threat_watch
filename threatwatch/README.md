# ThreatWatch

An evolving network threat detection project. This first milestone is a small, testable FastAPI backend with a **transparent rule-based baseline**. It does **not** claim to be a trained ML intrusion detector yet.

## Features in milestone 1
- Health endpoint
- Traffic feature validation
- Explainable baseline risk scoring
- Automated API tests
- Local development instructions

## Requirements
Python 3.11+

## Run locally
```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs for interactive API documentation.

## Example request
```bash
curl -X POST http://127.0.0.1:8000/api/v1/analyze \
  -H "Content-Type: application/json" \
  -d '{"duration_seconds":1.2,"packets":1500,"bytes_transferred":300000,"destination_port":22,"failed_connections":12}'
```

## Tests
```bash
pytest -q
```

## Status
This is an educational prototype, not a production security control. The baseline uses simple heuristics, so it can generate false positives and miss attacks. No packet capture or ML training is implemented yet.

## Roadmap
1. Establish API and tests (this milestone)
2. Select and inspect a real, appropriately licensed intrusion dataset
3. Create reproducible preprocessing and model training/evaluation
4. Add model inference behind the API
5. Integrate authorized traffic capture and feature extraction
6. Build a dashboard, alerts, and deployment pipeline

See `docs/architecture.md` and `docs/decisions.md`.

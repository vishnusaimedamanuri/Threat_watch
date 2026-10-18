# Architecture — Milestone 1

Client -> FastAPI `/api/v1/analyze` -> Pydantic validation -> rule-based baseline -> JSON result.

The scoring component is deliberately isolated so a trained model can replace it without rewriting the HTTP layer.

**Not yet implemented:** packet capture, dataset preprocessing, model training, model versioning, persistence, authentication, dashboards, production deployment.

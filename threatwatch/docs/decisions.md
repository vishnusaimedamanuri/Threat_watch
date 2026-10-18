# Engineering decisions

## 001 — Start with a backend contract
We build the API and tests first to make later ML integration measurable and easier to debug.

## 002 — Label the initial detector accurately
The first implementation is a heuristic baseline, **not** a machine-learning model. This avoids making unsupported performance claims.

## 003 — No privileged network capture in milestone 1
Traffic capture requires permission and OS-specific setup. We first accept explicit numeric flow features via an API.

# Changelog

All notable changes to the HoneyHive OpenAPI specification will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## v2.0.0 (2026-05-08)

This release introduces a new versioned API surface under `/v1/*` and deprecates the legacy unversioned routes. It contains breaking changes — see the migration notes below.

### Added (new endpoints)

- `POST /v1/sessions` — start a new session (replaces `POST /session/start`)
- `POST /v1/events` — write a single trace event
- `POST /v1/events/batch` — write trace events in batch
- `GET /v1/events/schema` — retrieve event schema
- `POST /v1/events/search` — search events by criteria
- `GET /v1/runs/{run_id}/schema` — retrieve schema for a run
- `GET /v1/runs/{new_run_id}/compare/{old_run_id}` — compare two runs
- `GET /v1/runs/{new_run_id}/compare/{old_run_id}/events` — compare events across two runs
- `GET /v1/datasets/{dataset_id}` — fetch a dataset
- `GET /v1/datasets/{dataset_id}/{datapoint_id}` — fetch a datapoint within a dataset
- `GET /v1/metrics/{metric_id}` — fetch a metric
- `POST /v1/metrics/run` — run metrics
- `GET /v1/queues` and `GET /v1/queues/{queue_id}` — queue read endpoints
- `POST /session/{session_id}/traces` — append traces to a session

### Changed

- All operations now carry an `x-honeyhive-plane` annotation indicating whether they run on the Control Plane (`cp`) or Data Plane (`dp`).
- Tag taxonomy reorganized: `Session` → `Sessions`, and several namespace-level tag descriptions added.
- Many request/response schemas renamed and promoted to top-level components (e.g. `LegacyStartSessionRequest`).

### Deprecated

- `POST /session/start` — use `POST /v1/sessions` instead. The legacy route wraps the session object under a `session` key; the v1 route accepts a bare session object.
- `POST /events`, `PUT /events`, `POST /events/batch`, `POST /events/model`, `POST /events/model/batch` — use the corresponding `/v1/events*` routes.
- Legacy operationIds (`startSession`, `createEvent`, `updateEvent`, `createEventBatch`, etc.) renamed with a `Legacy` suffix.

### Removed

- `GET /events` — removed without deprecation period (use `POST /v1/events/search`).
- `GET /v1/sessions/{session_id}` — replaced by the new event-tree endpoint shape.
- `GET /v1/projects` — no longer part of the public surface.
- `GET /v1/events/chart` — chart aggregation removed from public spec.

### Breaking changes

- `POST /session/start`: `session` request property type changed from `string` (JSON-encoded) to `object`.
- `POST /events`: `event` request property type changed from `string` to `object`; `event/event_type` and `event/inputs` are now required.
- `PUT /events`: `outputs` request property type changed.
- `POST /events/batch` and `POST /events/model/batch`: `application/json` media type removed for `500` responses.
- `GET /v1/configurations`: response body changed from `array` to `object`.
- `PUT /v1/configurations/{id}`: `upsertedId` response property type widened to `string | null`.

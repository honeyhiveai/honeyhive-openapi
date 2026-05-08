# Changelog

All notable changes to the HoneyHive OpenAPI specification will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Changelog entries are generated deterministically with `oasdiff changelog --format markdown`.

## v2.0.0 (2026-05-08)

# API Changelog 1.1.0 vs. 2.0.0


## API Changes

### GET /events
- :warning: api removed without deprecation


### POST /events
- :warning: added the new required request property `event/event_type`
- :warning: added the new required request property `event/inputs`
- :warning: the `event` request property type/format changed from `string`/`` to `object`/``
-  api operation id `createEvent` removed and replaced with `createEventLegacy`
-  endpoint deprecated
-  added the new optional request property `event/children_ids`
-  added the new optional request property `event/config`
-  added the new optional request property `event/duration`
-  added the new optional request property `event/end_time`
-  added the new optional request property `event/error`
-  added the new optional request property `event/event_id`
-  added the new optional request property `event/event_name`
-  added the new optional request property `event/feedback`
-  added the new optional request property `event/metadata`
-  added the new optional request property `event/metrics`
-  added the new optional request property `event/outputs`
-  added the new optional request property `event/parent_id`
-  added the new optional request property `event/project`
-  added the new optional request property `event/project_id`
-  added the new optional request property `event/session_id`
-  added the new optional request property `event/source`
-  added the new optional request property `event/start_time`
-  added the new optional request property `event/user_properties`
-  the response property `event_id` became required for the status `200`


### PUT /events
- :warning: the `outputs` request property type/format changed from `object`/`` to ``/``
-  api operation id `updateEvent` removed and replaced with `updateEventLegacy`
-  endpoint deprecated
-  added the new optional request property `children_ids`
-  added the new optional request property `end_time`


### POST /events/batch
- :warning: removed the media type `application/json` for the response with the status `500`
-  api operation id `createEventBatch` removed and replaced with `createEventBatchLegacy`
-  endpoint deprecated
-  added the new optional request property `session`
-  added the new optional request property `session_properties/start_time`
-  added the new optional request property `single_session`
-  the request property `events/items/project` became optional
-  request property `events/items/project` deprecated
-  request property `is_single_session` deprecated


### POST /events/model
-  added the new optional request property `model_event/cost`
-  added the new optional request property `model_event/hyperparameters`
-  added the new optional request property `model_event/messages`
-  added the new optional request property `model_event/model`
-  added the new optional request property `model_event/model_name`
-  added the new optional request property `model_event/model_version`
-  added the new optional request property `model_event/provider`
-  added the new optional request property `model_event/response`
-  added the new optional request property `model_event/response_format`
-  added the new optional request property `model_event/template`
-  added the new optional request property `model_event/template_inputs`
-  added the new optional request property `model_event/tool_choice`
-  added the new optional request property `model_event/tools`
-  added the new optional request property `model_event/usage`
-  the request property `model_event/project` became optional
-  request property `model_event/duration` deprecated
-  request property `model_event/error` deprecated
-  request property `model_event/project` deprecated
-  the response property `event_id` became required for the status `200`


### POST /events/model/batch
- :warning: removed the media type `application/json` for the response with the status `500`
-  added the new optional request property `model_events/items/cost`
-  added the new optional request property `model_events/items/hyperparameters`
-  added the new optional request property `model_events/items/messages`
-  added the new optional request property `model_events/items/model`
-  added the new optional request property `model_events/items/model_name`
-  added the new optional request property `model_events/items/model_version`
-  added the new optional request property `model_events/items/provider`
-  added the new optional request property `model_events/items/response`
-  added the new optional request property `model_events/items/response_format`
-  added the new optional request property `model_events/items/template`
-  added the new optional request property `model_events/items/template_inputs`
-  added the new optional request property `model_events/items/tool_choice`
-  added the new optional request property `model_events/items/tools`
-  added the new optional request property `model_events/items/usage`
-  added the new optional request property `session`
-  added the new optional request property `session_properties/start_time`
-  added the new optional request property `single_session`
-  the request property `model_events/items/project` became optional
-  request property `is_single_session` deprecated
-  request property `model_events/items/duration` deprecated
-  request property `model_events/items/error` deprecated
-  request property `model_events/items/project` deprecated


### POST /session/start
- :warning: the `session` request property type/format changed from `string`/`` to `object`/``
-  api operation id `startSession` removed and replaced with `startSessionLegacy`
-  api tag `Sessions` added
-  api tag `Session` removed
-  endpoint deprecated
-  added the new optional request property `session/children_ids`
-  added the new optional request property `session/config`
-  added the new optional request property `session/duration`
-  added the new optional request property `session/end_time`
-  added the new optional request property `session/event_name`
-  added the new optional request property `session/inputs`
-  added the new optional request property `session/metadata`
-  added the new optional request property `session/outputs`
-  added the new optional request property `session/session_id`
-  added the new optional request property `session/session_name`
-  added the new optional request property `session/source`
-  added the new optional request property `session/start_time`
-  added the new optional request property `session/user_properties`
-  the response property `event_id` became required for the status `200`
-  the response property `session_id` became required for the status `200`
-  the `children_ids` response's property default value `[]` was removed for the status `200`


### POST /session/{session_id}/traces
-  endpoint added


### GET /v1/configurations
- :warning: the response's body type/format changed from `array`/`` to `object`/`` for status `200`
-  endpoint deprecated
-  added the required property `configurations` to the response with the `200` status


### POST /v1/configurations
-  endpoint deprecated


### DELETE /v1/configurations/{id}
-  endpoint deprecated


### PUT /v1/configurations/{id}
- :warning: the `upsertedId` response's property type/format changed from `null`/`` to `string, null`/`` for status `200`
-  endpoint deprecated


### GET /v1/datapoints
-  the response property `datapoints/items/ground_truth` became required for the status `200`
-  the response property `datapoints/items/inputs` became required for the status `200`
-  the response property `datapoints/items/metadata` became required for the status `200`
-  the `` response's property default value `map[]` was removed for the status `200`
-  the `ground_truth` response's property default value `map[]` was removed for the status `200`
-  the `inputs` response's property default value `map[]` was removed for the status `200`
-  the `metadata` response's property default value `map[]` was removed for the status `200`


### POST /v1/datapoints
-  the `` request property default value `map[]` was removed
-  the `ground_truth` request property default value `map[]` was removed
-  the `metadata` request property default value `map[]` was removed


### POST /v1/datapoints/batch
- :warning: removed `subschema #1, subschema #2` from the `filters` request property `anyOf` list
-  added `subschema #1, subschema #2` to the `filters` request property `anyOf` list
-  request property `events` deprecated
-  request property `mapping` deprecated


### GET /v1/datapoints/{id}
- :warning: removed the required property `datapoint/items/datapoint` from the response with the `200` status
-  added the optional property `datapoint/items/linked_datasets` to the response with the `200` status
-  added the optional property `datapoint/items/updated_at` to the response with the `200` status
-  the response property `datapoint` became required for the status `200`
-  added the required property `datapoint/items/created_at` to the response with the `200` status
-  added the required property `datapoint/items/ground_truth` to the response with the `200` status
-  added the required property `datapoint/items/history` to the response with the `200` status
-  added the required property `datapoint/items/id` to the response with the `200` status
-  added the required property `datapoint/items/inputs` to the response with the `200` status
-  added the required property `datapoint/items/linked_event` to the response with the `200` status
-  added the required property `datapoint/items/metadata` to the response with the `200` status


### PUT /v1/datapoints/{id}
-  the `` request property default value `map[]` was removed
-  the `ground_truth` request property default value `map[]` was removed
-  the `inputs` request property default value `map[]` was removed
-  the `metadata` request property default value `map[]` was removed


### DELETE /v1/datasets
-  api operation id `deleteDataset` removed and replaced with `deleteDatasetLegacy`
-  endpoint deprecated


### GET /v1/datasets
- :warning: deleted the `query` request parameter `include_datapoints`
-  the response property `datasets/items/datapoints` became required for the status `200`
-  the `datapoints` response's property default value `[]` was removed for the status `200`


### PUT /v1/datasets
-  api operation id `updateDataset` removed and replaced with `updateDatasetLegacy`
-  endpoint deprecated
-  the response property `result/datapoints` became required for the status `200`
-  the `datapoints` response's property default value `[]` was removed for the status `200`


### DELETE /v1/datasets/{dataset_id}
-  endpoint added


### PUT /v1/datasets/{dataset_id}
-  endpoint added


### POST /v1/datasets/{dataset_id}/datapoints
-  the `` request property default value `map[]` was removed


### DELETE /v1/datasets/{dataset_id}/{datapoint_id}
-  endpoint added


### POST /v1/events
-  endpoint added


### POST /v1/events/batch
-  endpoint added


### GET /v1/events/chart
- :warning: api path removed without deprecation


### POST /v1/events/export
- :warning: the `filters` request property type/format changed from ``/`` to `array`/``
- :warning: the response property `events/items/project` became optional for the status `200`
- :warning: removed the required property `totalEvents` from the response with the `200` status
- :warning: removed `#/components/schemas/FiltersArray, subschema #2` from the `filters` request property `allOf` list
- :warning: removed the request property `project`
-  api operation id `exportEvents` removed and replaced with `exportEventsLegacy`
-  endpoint deprecated
-  added the new optional request property `evaluation_id`
-  added the new optional request property `ignore_order`
-  the request property `filters` became optional
-  response property `events/items/project` deprecated
-  added the required property `count` to the response with the `200` status


### GET /v1/events/schema
-  endpoint added


### POST /v1/events/search
-  endpoint added


### DELETE /v1/events/{id}
- :warning: api removed without deprecation


### GET /v1/events/{id}
- :warning: api removed without deprecation


### PUT /v1/events/{id}
-  endpoint added


### DELETE /v1/metrics
-  api operation id `deleteMetric` removed and replaced with `deleteMetricLegacy`
-  endpoint deprecated


### GET /v1/metrics
- :warning: the response's body type/format changed from `array`/`` to `object`/`` for status `200`
-  added the required property `metrics` to the response with the `200` status


### POST /v1/metrics
- :warning: removed `subschema #1, subschema #2, subschema #3, subschema #4` from the `filters/filterArray/items/operator` request property `anyOf` list
- :warning: request property `filters/filterArray/items/operator` was restricted to a list of enum values
- :warning: the `filters/filterArray/items/operator` request property type/format changed from ``/`` to `string`/``
-  the `sampling_percentage` request property default value changed from `100.00` to `10.00`
-  added the new `after` enum value to the request property `filters/filterArray/items/operator`
-  added the new `before` enum value to the request property `filters/filterArray/items/operator`
-  added the new `contains` enum value to the request property `filters/filterArray/items/operator`
-  added the new `exists` enum value to the request property `filters/filterArray/items/operator`
-  added the new `greater than` enum value to the request property `filters/filterArray/items/operator`
-  added the new `is` enum value to the request property `filters/filterArray/items/operator`
-  added the new `is not` enum value to the request property `filters/filterArray/items/operator`
-  added the new `less than` enum value to the request property `filters/filterArray/items/operator`
-  added the new `not contains` enum value to the request property `filters/filterArray/items/operator`
-  added the new `not exists` enum value to the request property `filters/filterArray/items/operator`


### PUT /v1/metrics
- :warning: removed `subschema #1, subschema #2, subschema #3, subschema #4` from the `filters/filterArray/items/operator` request property `anyOf` list
- :warning: request property `filters/filterArray/items/operator` was restricted to a list of enum values
- :warning: the `filters/filterArray/items/operator` request property type/format changed from ``/`` to `string`/``
-  api operation id `updateMetric` removed and replaced with `updateMetricLegacy`
-  endpoint deprecated
-  the request property `description` became nullable
-  the `description` request property default value `` was removed
-  the `enabled_in_prod` request property default value `false` was removed
-  the `filters` request property default value `map[filterArray:[]]` was removed
-  the `needs_ground_truth` request property default value `false` was removed
-  the `return_type` request property default value `float` was removed
-  the `sampling_percentage` request property default value `100.00` was removed
-  added the new `after` enum value to the request property `filters/filterArray/items/operator`
-  added the new `before` enum value to the request property `filters/filterArray/items/operator`
-  added the new `contains` enum value to the request property `filters/filterArray/items/operator`
-  added the new `exists` enum value to the request property `filters/filterArray/items/operator`
-  added the new `greater than` enum value to the request property `filters/filterArray/items/operator`
-  added the new `is` enum value to the request property `filters/filterArray/items/operator`
-  added the new `is not` enum value to the request property `filters/filterArray/items/operator`
-  added the new `less than` enum value to the request property `filters/filterArray/items/operator`
-  added the new `not contains` enum value to the request property `filters/filterArray/items/operator`
-  added the new `not exists` enum value to the request property `filters/filterArray/items/operator`


### POST /v1/metrics/run
-  endpoint added


### POST /v1/metrics/run_metric
- :warning: removed `subschema #1, subschema #2, subschema #3, subschema #4` from the `metric/filters/filterArray/items/operator` request property `anyOf` list
- :warning: request property `metric/filters/filterArray/items/operator` was restricted to a list of enum values
- :warning: the request property `event` became required
- :warning: removed the enum value `COMPOSITE` of the request property `metric/type`
- :warning: removed the enum value `HUMAN` of the request property `metric/type`
- :warning: the `event` request property type/format changed from ``/`` to `object`/``
- :warning: the `metric/filters/filterArray/items/operator` request property type/format changed from ``/`` to `string`/``
- :warning: the response's body type/format changed from ``/`` to `object`/`` for status `200`
-  api operation id `runMetric` removed and replaced with `runMetricLegacy`
-  endpoint deprecated
-  added the new optional request property `event/event_name`
-  added the new optional request property `event/event_type`
-  added the new optional request property `event/feedback`
-  added the new optional request property `event/inputs`
-  added the new optional request property `event/outputs`
-  added the new optional request property `event/workspace_id`
-  the `sampling_percentage` request property default value changed from `100.00` to `10.00`
-  added the new `after` enum value to the request property `metric/filters/filterArray/items/operator`
-  added the new `before` enum value to the request property `metric/filters/filterArray/items/operator`
-  added the new `contains` enum value to the request property `metric/filters/filterArray/items/operator`
-  added the new `exists` enum value to the request property `metric/filters/filterArray/items/operator`
-  added the new `greater than` enum value to the request property `metric/filters/filterArray/items/operator`
-  added the new `is` enum value to the request property `metric/filters/filterArray/items/operator`
-  added the new `is not` enum value to the request property `metric/filters/filterArray/items/operator`
-  added the new `less than` enum value to the request property `metric/filters/filterArray/items/operator`
-  added the new `not contains` enum value to the request property `metric/filters/filterArray/items/operator`
-  added the new `not exists` enum value to the request property `metric/filters/filterArray/items/operator`
-  added the required property `explanation` to the response with the `200` status
-  added the required property `loading` to the response with the `200` status
-  added the required property `result` to the response with the `200` status
-  added the required property `success` to the response with the `200` status


### DELETE /v1/metrics/{metric_id}
-  endpoint added


### PUT /v1/metrics/{metric_id}
-  endpoint added


### DELETE /v1/projects
- :warning: api path removed without deprecation


### GET /v1/projects
- :warning: api path removed without deprecation


### POST /v1/projects
- :warning: api path removed without deprecation


### PUT /v1/projects
- :warning: api path removed without deprecation


### GET /v1/queues
-  endpoint added


### POST /v1/queues
-  endpoint added


### DELETE /v1/queues/{queue_id}
-  endpoint added


### GET /v1/queues/{queue_id}
-  endpoint added


### PUT /v1/queues/{queue_id}
-  endpoint added


### GET /v1/runs
- :warning: the `evaluations/items/` response's property type/format changed from ``/`` to `object`/`` for status `200`
-  added the optional property `evaluations/items/dataset_id` to the response with the `200` status
-  added the optional property `evaluations/items/description` to the response with the `200` status
-  added the optional property `evaluations/items/metrics` to the response with the `200` status
-  added the optional property `evaluations/items/name` to the response with the `200` status
-  added the optional property `evaluations/items/status` to the response with the `200` status
-  added the optional property `evaluations/items/updated_at` to the response with the `200` status
-  added the required property `evaluations/items/configuration` to the response with the `200` status
-  added the required property `evaluations/items/created_at` to the response with the `200` status
-  added the required property `evaluations/items/event_ids` to the response with the `200` status
-  added the required property `evaluations/items/id` to the response with the `200` status
-  added the required property `evaluations/items/is_active` to the response with the `200` status
-  added the required property `evaluations/items/metadata` to the response with the `200` status
-  added the required property `evaluations/items/results` to the response with the `200` status
-  added the required property `evaluations/items/run_id` to the response with the `200` status
-  added the required property `evaluations/items/scope_id` to the response with the `200` status
-  added the required property `evaluations/items/scope_type` to the response with the `200` status


### POST /v1/runs
- :warning: the `evaluation` response's property type/format changed from ``/`` to `object`/`` for status `200`
-  added the new optional request property `run_id`
-  the `configuration` request property default value `map[]` was removed
-  the `metadata` request property default value `map[]` was removed
-  the `results` request property default value `map[]` was removed
-  added the optional property `evaluation/dataset_id` to the response with the `200` status
-  added the optional property `evaluation/description` to the response with the `200` status
-  added the optional property `evaluation/metrics` to the response with the `200` status
-  added the optional property `evaluation/name` to the response with the `200` status
-  added the optional property `evaluation/status` to the response with the `200` status
-  added the optional property `evaluation/updated_at` to the response with the `200` status
-  the response property `evaluation` became required for the status `200`
-  added the required property `evaluation/configuration` to the response with the `200` status
-  added the required property `evaluation/created_at` to the response with the `200` status
-  added the required property `evaluation/event_ids` to the response with the `200` status
-  added the required property `evaluation/id` to the response with the `200` status
-  added the required property `evaluation/is_active` to the response with the `200` status
-  added the required property `evaluation/metadata` to the response with the `200` status
-  added the required property `evaluation/results` to the response with the `200` status
-  added the required property `evaluation/run_id` to the response with the `200` status
-  added the required property `evaluation/scope_id` to the response with the `200` status
-  added the required property `evaluation/scope_type` to the response with the `200` status


### GET /v1/runs/compare/events
- :warning: removed the optional property `pagination` from the response with the `200` status
-  api operation id `getExperimentCompareEvents` removed and replaced with `getExperimentCompareEventsLegacy`
-  endpoint deprecated
-  the response property `events` became required for the status `200`
-  added the required property `events/items/datapoint_id` to the response with the `200` status
-  added the required property `events/items/event_1` to the response with the `200` status
-  added the required property `events/items/event_2` to the response with the `200` status
-  added the required property `totalEvents` to the response with the `200` status


### GET /v1/runs/schema
- :warning: deleted the `query` request parameter `evaluation_id`
-  api operation id `getExperimentRunsSchema` removed and replaced with `getRunsSchema`
-  added the non-success response with the status `400`


### GET /v1/runs/{new_run_id}/compare-with/{old_run_id}
- :warning: for the `query` request parameter `aggregate_function`, default value `average` was removed
- :warning: removed the enum value `average` from the `query` request parameter `aggregate_function`
- :warning: removed the enum value `count` from the `query` request parameter `aggregate_function`
- :warning: removed the enum value `max` from the `query` request parameter `aggregate_function`
- :warning: removed the enum value `median` from the `query` request parameter `aggregate_function`
- :warning: removed the enum value `min` from the `query` request parameter `aggregate_function`
- :warning: removed the enum value `p90` from the `query` request parameter `aggregate_function`
- :warning: removed the enum value `p95` from the `query` request parameter `aggregate_function`
- :warning: removed the enum value `p99` from the `query` request parameter `aggregate_function`
- :warning: removed the enum value `sum` from the `query` request parameter `aggregate_function`
-  api operation id `getExperimentComparison` removed and replaced with `getExperimentComparisonLegacy`
-  endpoint deprecated
-  added the optional property `new_run/metrics` to the response with the `200` status
-  added the optional property `old_run/metrics` to the response with the `200` status
-  the response property `new_run/configuration` became required for the status `200`
-  the response property `new_run/event_ids` became required for the status `200`
-  the response property `new_run/is_active` became required for the status `200`
-  the response property `new_run/metadata` became required for the status `200`
-  the response property `new_run/results` became required for the status `200`
-  the response property `old_run/configuration` became required for the status `200`
-  the response property `old_run/event_ids` became required for the status `200`
-  the response property `old_run/is_active` became required for the status `200`
-  the response property `old_run/metadata` became required for the status `200`
-  the response property `old_run/results` became required for the status `200`
-  the `configuration` response's property default value `map[]` was removed for the status `200`
-  the `configuration` response's property default value `map[]` was removed for the status `200`
-  the `event_ids` response's property default value `[]` was removed for the status `200`
-  the `event_ids` response's property default value `[]` was removed for the status `200`
-  the `is_active` response's property default value `true` was removed for the status `200`
-  the `is_active` response's property default value `true` was removed for the status `200`
-  the `metadata` response's property default value `map[]` was removed for the status `200`
-  the `metadata` response's property default value `map[]` was removed for the status `200`
-  the `results` response's property default value `map[]` was removed for the status `200`
-  the `results` response's property default value `map[]` was removed for the status `200`


### GET /v1/runs/{new_run_id}/compare/{old_run_id}
-  endpoint added


### GET /v1/runs/{new_run_id}/compare/{old_run_id}/events
-  endpoint added


### DELETE /v1/runs/{run_id}
- :warning: for the `path` request parameter `run_id`, the type/format was changed from `string`/`` to `string`/`uuid`


### GET /v1/runs/{run_id}
- :warning: for the `path` request parameter `run_id`, the type/format was changed from `string`/`` to `string`/`uuid`
- :warning: the `evaluation` response's property type/format changed from ``/`` to `object`/`` for status `200`
-  added the optional property `evaluation/dataset_id` to the response with the `200` status
-  added the optional property `evaluation/description` to the response with the `200` status
-  added the optional property `evaluation/metrics` to the response with the `200` status
-  added the optional property `evaluation/name` to the response with the `200` status
-  added the optional property `evaluation/status` to the response with the `200` status
-  added the optional property `evaluation/updated_at` to the response with the `200` status
-  the response property `evaluation` became required for the status `200`
-  added the required property `evaluation/configuration` to the response with the `200` status
-  added the required property `evaluation/created_at` to the response with the `200` status
-  added the required property `evaluation/event_ids` to the response with the `200` status
-  added the required property `evaluation/id` to the response with the `200` status
-  added the required property `evaluation/is_active` to the response with the `200` status
-  added the required property `evaluation/metadata` to the response with the `200` status
-  added the required property `evaluation/results` to the response with the `200` status
-  added the required property `evaluation/run_id` to the response with the `200` status
-  added the required property `evaluation/scope_id` to the response with the `200` status
-  added the required property `evaluation/scope_type` to the response with the `200` status


### PUT /v1/runs/{run_id}
- :warning: for the `path` request parameter `run_id`, the type/format was changed from `string`/`` to `string`/`uuid`
- :warning: the `evaluation` response's property type/format changed from ``/`` to `object`/`` for status `200`
-  the `configuration` request property default value `map[]` was removed
-  the `metadata` request property default value `map[]` was removed
-  the `results` request property default value `map[]` was removed
-  added the optional property `evaluation/dataset_id` to the response with the `200` status
-  added the optional property `evaluation/description` to the response with the `200` status
-  added the optional property `evaluation/metrics` to the response with the `200` status
-  added the optional property `evaluation/name` to the response with the `200` status
-  added the optional property `evaluation/status` to the response with the `200` status
-  added the optional property `evaluation/updated_at` to the response with the `200` status
-  the response property `evaluation` became required for the status `200`
-  added the required property `evaluation/configuration` to the response with the `200` status
-  added the required property `evaluation/created_at` to the response with the `200` status
-  added the required property `evaluation/event_ids` to the response with the `200` status
-  added the required property `evaluation/id` to the response with the `200` status
-  added the required property `evaluation/is_active` to the response with the `200` status
-  added the required property `evaluation/metadata` to the response with the `200` status
-  added the required property `evaluation/results` to the response with the `200` status
-  added the required property `evaluation/run_id` to the response with the `200` status
-  added the required property `evaluation/scope_id` to the response with the `200` status
-  added the required property `evaluation/scope_type` to the response with the `200` status


### GET /v1/runs/{run_id}/metrics
-  the response property `events` became required for the status `200`
-  added the required property `events/items/event_name` to the response with the `200` status
-  added the required property `events/items/event_type` to the response with the `200` status
-  added the required property `events/items/metadata` to the response with the `200` status
-  added the required property `events/items/metrics` to the response with the `200` status
-  added the required property `events/items/session_id` to the response with the `200` status
-  added the required property `totalEvents` to the response with the `200` status


### GET /v1/runs/{run_id}/result
- :warning: the `metrics/details/items/datapoints` response's property type/format changed from ``/`` to `object`/`` for status `200`
- :warning: the `metrics/details/items/passing_range` response's property type/format changed from ``/`` to `object`/`` for status `200`
-  added the optional property `metrics/details/items/passing_range/max` to the response with the `200` status
-  added the optional property `metrics/details/items/passing_range/min` to the response with the `200` status
-  added the optional property `run_object/metrics` to the response with the `200` status
-  removed `#/components/schemas/MetricDatapoints, subschema #2` from the `metrics/details/items/datapoints` response property `allOf` list for the response status `200`
-  removed `#/components/schemas/PassingRange, subschema #2` from the `metrics/details/items/passing_range` response property `allOf` list for the response status `200`
-  the response property `run_object/configuration` became required for the status `200`
-  the response property `run_object/event_ids` became required for the status `200`
-  the response property `run_object/is_active` became required for the status `200`
-  the response property `run_object/metadata` became required for the status `200`
-  the response property `run_object/results` became required for the status `200`
-  the `configuration` response's property default value `map[]` was removed for the status `200`
-  the `event_ids` response's property default value `[]` was removed for the status `200`
-  the `is_active` response's property default value `true` was removed for the status `200`
-  the `metadata` response's property default value `map[]` was removed for the status `200`
-  the `results` response's property default value `map[]` was removed for the status `200`
-  added the required property `metrics/details/items/datapoints/failed` to the response with the `200` status
-  added the required property `metrics/details/items/datapoints/passed` to the response with the `200` status


### GET /v1/runs/{run_id}/schema
-  endpoint added


### POST /v1/sessions
-  endpoint added


### DELETE /v1/sessions/{session_id}
- :warning: api path removed without deprecation


### GET /v1/sessions/{session_id}
- :warning: api path removed without deprecation




## Components
-  removed the schema `DeleteDatasetQuery`
-  removed the schema `DeleteEventParams`
-  removed the schema `DeleteEventResponse`
-  removed the schema `DeleteMetricQuery`
-  removed the schema `DeleteSessionResponse`
-  removed the schema `FilterFieldType`
-  removed the schema `GetDatasetsQuery`
-  removed the schema `GetEventsBySessionIdParams`
-  removed the schema `GetEventsBySessionIdResponse`
-  removed the schema `GetEventsChartQuery`
-  removed the schema `GetEventsChartResponse`
-  removed the schema `GetEventsLegacyRequest`
-  removed the schema `GetEventsLegacyResponse`
-  removed the schema `GetExperimentRunsSchemaQuery`
-  removed the schema `GetExperimentRunsSchemaResponse`
-  removed the schema `GetSessionResponse`





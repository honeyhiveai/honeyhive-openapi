# HoneyHive CLI

Command-line interface for the [HoneyHive API](https://docs.honeyhive.ai). Manage sessions, events, datasets, experiments, and more from your terminal.

## Installation

```bash
pip install .
```

Or in development mode:

```bash
pip install -e .
```

## Quick Start

### 1. Authenticate

```bash
# Interactive login (saves to ~/.honeyhive/config.json)
hh auth login

# Or use environment variables
export HH_API_KEY="your-api-key"
export HH_API_URL="https://api.honeyhive.ai"  # optional
```

### 2. Use the CLI

```bash
# List projects
hh projects list

# List datasets (table format)
hh --output table datasets list

# Get a session by ID
hh sessions get <session-id>

# List experiment runs
hh runs list --status completed --limit 10
```

## Commands

| Group              | Description                                   |
| ------------------ | --------------------------------------------- |
| `hh auth`          | Manage authentication (`login`, `status`, `logout`) |
| `hh sessions`      | Start, get, or delete sessions                |
| `hh events`        | Create, update, list, delete, export, chart events |
| `hh metrics`       | CRUD metrics and run metric evaluations       |
| `hh datapoints`    | CRUD datapoints                               |
| `hh datasets`      | CRUD datasets, add/remove datapoints          |
| `hh projects`      | CRUD projects                                 |
| `hh runs`          | Manage experiment runs, view results, compare |
| `hh configurations`| CRUD prompt/model configurations              |

Run `hh <command> --help` for full usage details.

## Global Options

```
--api-key TEXT    Override API key
--base-url TEXT   Override API base URL
--output [json|table]  Output format (default: json)
--verbose         Show HTTP request details
--version         Show version
--help            Show help
```

## Configuration

Credentials are resolved in this order:

1. `--api-key` / `--base-url` flags
2. `HH_API_KEY` / `HH_API_URL` environment variables (also accepts `HONEYHIVE_API_KEY` / `HONEYHIVE_API_URL`)
3. `~/.honeyhive/config.json` (written by `hh auth login`)

## Examples

```bash
# Create a dataset
hh datasets create --name "My Dataset" --description "Test data"

# Create a datapoint
hh datapoints create --inputs '{"query": "hello"}' --ground-truth '{"answer": "hi"}'

# Create an experiment run
hh runs create --name "baseline-v1" --dataset-id <dataset-id>

# Compare two runs
hh runs compare <new-run-id> <old-run-id>

# Get experiment results
hh runs result <run-id> --aggregate-function average

# List metrics as a table
hh --output table metrics list

# Create a configuration
hh configurations create \
  --name "gpt4-default" \
  --provider openai \
  --parameters '{"call_type": "chat", "model": "gpt-4"}'

# Export events with filters
hh events export \
  --project "My Project" \
  --filters '[{"field": "event_type", "operator": "is", "value": "model", "type": "string"}]'
```

## OpenAPI Spec

This repository also contains the HoneyHive OpenAPI specification used to build this CLI:

| File | Format |
| --- | --- |
| [`openapi.yaml`](openapi.yaml) | YAML (OpenAPI 3.1.0) |
| [`openapi.json`](openapi.json) | JSON |

## License

[MIT](LICENSE)

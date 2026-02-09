# HoneyHive OpenAPI Specification

The official [OpenAPI](https://www.openapis.org/) specification for the [HoneyHive API](https://api.honeyhive.ai).

## Files

| File | Format | Description |
| --- | --- | --- |
| [`openapi.yaml`](openapi.yaml) | YAML | OpenAPI 3.1.0 specification |
| [`openapi.json`](openapi.json) | JSON | Same specification in JSON format |

## Usage

### API Documentation

This spec powers the API reference at [docs.honeyhive.ai](https://docs.honeyhive.ai).

### SDK Generation

Generate a client in any language using [OpenAPI Generator](https://openapi-generator.tech/) or [Speakeasy](https://www.speakeasy.com/):

```bash
# OpenAPI Generator
openapi-generator-cli generate -i openapi.yaml -g python -o ./honeyhive-python

# Speakeasy
speakeasy generate sdk -s openapi.yaml -o ./honeyhive-sdk -l python
```

### Raw URLs

Reference the spec directly via GitHub raw URLs:

```
https://raw.githubusercontent.com/honeyhiveai/honeyhive-openapi/main/openapi.yaml
https://raw.githubusercontent.com/honeyhiveai/honeyhive-openapi/main/openapi.json
```

### Postman

Import `openapi.json` into [Postman](https://www.postman.com/) to explore the API interactively.

## How This Repo Is Updated

This repository is automatically updated by CI in the HoneyHive platform repo whenever code is merged to the default branch and all checks pass. The spec is regenerated from source and pushed here in both YAML and JSON formats.

## License

[MIT](LICENSE)

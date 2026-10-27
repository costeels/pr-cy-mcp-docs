# create_keywords

Add a batch of keywords to a project, with optional target URLs and group assignments.

Operation: changes data, launches work or generates content.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

At most 100 keywords per call. Each item has a keyword and can include target_url and group_ids. Split long batches into separate calls.

## Arguments

- `project_id`: required; integer. greater than: 0. Project ID from project discovery.
- `keywords`: required; array of object. minimum items: 1; maximum items: 100. Keyword items to create.

### KeywordCreateItem

- `keyword`: required; string. minimum text length: 1. Keyword phrase.
- `target_url`: optional; string or null. Schema default: `null`. minimum text length: 1. Target page URL for a keyword.
- `group_ids`: optional; array of integer. Keyword-group IDs to associate with a keyword.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "create_keywords",
    "arguments": {
      "project_id": 123,
      "keywords": [
        {
          "keyword": "buy laptop",
          "target_url": "https://example.com/laptops/",
          "group_ids": [
            456
          ]
        }
      ]
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `result`: array of object; required in the output schema.

The complete input and output schemas are in [create_keywords.json](../../schemas/create_keywords.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

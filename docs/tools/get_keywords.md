# get_keywords

List project keywords, keyword groups and target URLs.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Arguments

- `project_id`: required; integer. greater than: 0. Project ID from project discovery.
- `limit`: optional; integer. Schema default: `100`. minimum: 1; maximum: 1000. Maximum rows or records requested for this page of results.
- `offset`: optional; integer. Schema default: `0`. minimum: 0. Starting offset; follow this tool's minimum and default.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_keywords",
    "arguments": {
      "project_id": 123,
      "limit": 20,
      "offset": 0
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `result`: array of object; required in the output schema.

The complete input and output schemas are in [get_keywords.json](../../schemas/get_keywords.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

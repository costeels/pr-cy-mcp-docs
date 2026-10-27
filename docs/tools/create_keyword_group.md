# create_keyword_group

Create a named keyword group in a project.

Operation: changes data, launches work or generates content.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Arguments

- `project_id`: required; integer. greater than: 0. Project ID from project discovery.
- `name`: required; string. minimum text length: 1. Name of the article, keyword group or project note.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "create_keyword_group",
    "arguments": {
      "project_id": 123,
      "name": "Laptops"
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `id`: integer; required in the output schema.
- `name`: string; required in the output schema.

The complete input and output schemas are in [create_keyword_group.json](../../schemas/create_keyword_group.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

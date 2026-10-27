# list_articles

List the articles available to the connected user.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Arguments

- `limit`: optional; integer. Schema default: `10`. minimum: 1; maximum: 50. Maximum rows or records requested for this page of results.
- `offset`: optional; integer. Schema default: `0`. minimum: 0. Starting offset; follow this tool's minimum and default.
- `sort`: optional; string. Schema default: `"-dateUpdated"`. Sort specification; its shape and allowed fields differ by tool.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "list_articles",
    "arguments": {
      "limit": 10,
      "offset": 0,
      "sort": "-dateUpdated"
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `result`: array of object; required in the output schema.

The complete input and output schemas are in [list_articles.json](../../schemas/list_articles.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

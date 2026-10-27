# get_keywords_positions_history

Retrieve historical project keyword rankings for a selected search setting.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Arguments

- `search_options_id`: required; integer. greater than: 0. Search-settings ID returned by keyword-project discovery.
- `date_from`: optional; string or null. Schema default: `null`. Start of the requested reporting or change period.
- `date_to`: optional; string or null. Schema default: `null`. End of the requested period; inclusivity depends on the tool.
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
    "name": "get_keywords_positions_history",
    "arguments": {
      "search_options_id": 456,
      "date_from": "2026-10-01",
      "date_to": "2026-10-20",
      "limit": 20
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `result`: array of object; required in the output schema.

The complete input and output schemas are in [get_keywords_positions_history.json](../../schemas/get_keywords_positions_history.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

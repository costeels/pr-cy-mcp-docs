# check_positions

Launch a project keyword-ranking check for one or all active search settings.

Operation: changes data, launches work or generates content.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

This launches a check and can consume account limits. Omit search_options_id only when a check of all active project search settings is intended.

## Arguments

- `project_id`: required; integer. greater than: 0. Project ID from project discovery.
- `search_options_id`: optional; integer or null. Schema default: `null`. greater than: 0. Search-settings ID returned by keyword-project discovery.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "check_positions",
    "arguments": {
      "project_id": 123,
      "search_options_id": 456
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `status`: "success" | "error"; required in the output schema.

The complete input and output schemas are in [check_positions.json](../../schemas/check_positions.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

# get_project_notes

Retrieve user-created project notes for an inclusive date range.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

Both date boundaries are inclusive. Results are newest first; deleted notes are not returned. Pagination is applied after the upstream period list is fetched, so narrowing dates reduces upstream work. Note deletion is not exposed.

## Arguments

- `project_id`: required; integer. greater than: 0. Project ID from project discovery.
- `date_from`: optional; string or null. Schema default: `null`. Start of the requested reporting or change period.
- `date_to`: optional; string or null. Schema default: `null`. End of the requested period; inclusivity depends on the tool.
- `limit`: optional; integer. Schema default: `50`. minimum: 1; maximum: 500. Maximum rows or records requested for this page of results.
- `offset`: optional; integer. Schema default: `0`. minimum: 0. Starting offset; follow this tool's minimum and default.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_project_notes",
    "arguments": {
      "project_id": 123,
      "date_from": "2026-10-01",
      "date_to": "2026-10-20",
      "limit": 20,
      "offset": 0
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `notes`: array of object; required in the output schema.
- `total`: integer; required in the output schema.
- `has_more`: boolean; required in the output schema.

The complete input and output schemas are in [get_project_notes.json](../../schemas/get_project_notes.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

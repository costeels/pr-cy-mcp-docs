# get_pages_summary_by_dates

Retrieve historical clicks, impressions and positions grouped by day, week or month.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

Requires connected search-performance data. Dates must be no later than three days before the current date. This tool has no source input in the captured schema. period is day, week or month.

## Arguments

- `project_id`: required; integer. greater than: 0. Project ID from project discovery.
- `period`: optional; "day" | "week" | "month". Schema default: `"day"`. Date grouping for search-performance history.
- `date_from`: optional; string or null. Schema default: `null`. Start of the requested reporting or change period.
- `date_to`: optional; string or null. Schema default: `null`. End of the requested period; inclusivity depends on the tool.
- `url`: optional; object with string values or null. Schema default: `null`. Search-performance URL filter object.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_pages_summary_by_dates",
    "arguments": {
      "project_id": 123,
      "period": "day",
      "date_from": "2026-10-01",
      "date_to": "2026-10-20"
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `result`: array of object; required in the output schema.

The complete input and output schemas are in [get_pages_summary_by_dates.json](../../schemas/get_pages_summary_by_dates.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

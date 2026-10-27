# get_metrika_data_by_time

Retrieve Yandex Metrika metrics grouped by a time interval.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

metrics are required. Use the captured group enum to select a time aggregation and timezone when needed.

This report requires a project with a connected Yandex Metrika counter. Most report tools use the last seven days when dates are omitted; goal listing does not take report dates.

## Arguments

- `project_id`: required; integer. greater than: 0. Project ID from project discovery.
- `metrics`: required; array of string. Yandex Metrika metric names.
- `date_from`: optional; string or null. Schema default: `null`. Start of the requested reporting or change period.
- `date_to`: optional; string or null. Schema default: `null`. End of the requested period; inclusivity depends on the tool.
- `dimensions`: optional; array of string or null. Schema default: `null`. Yandex Metrika dimension names.
- `group`: optional; "day" | "week" | "month" | "quarter" | "year". Schema default: `"day"`. Time grouping for a Metrika time series.
- `top_keys`: optional; integer. Schema default: `7`. Number of dimension keys selected for a time-series report.
- `timezone`: optional; string or null. Schema default: `null`. Time zone used for the requested report.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_metrika_data_by_time",
    "arguments": {
      "project_id": 123,
      "metrics": [
        "ym:s:visits"
      ],
      "date_from": "2026-10-01",
      "date_to": "2026-10-20"
    }
  }
}
```

## Result

Interpret the returned tool content and structured data according to the current advertised output schema.

The complete input and output schemas are in [get_metrika_data_by_time.json](../../schemas/get_metrika_data_by_time.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

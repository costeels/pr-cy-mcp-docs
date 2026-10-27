# get_metrika_custom_query

Run a custom query against the connected Yandex Metrika reporting API using metrics, dimensions and filters.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

Use this when a specialized Metrika tool does not cover the question. Up to 20 metrics, 10 dimensions, 5 sort fields and 1,000 rows are allowed. offset starts at 1. Filters use Yandex Metrika API syntax; descending sort uses a leading minus sign.

This report requires a project with a connected Yandex Metrika counter. Most report tools use the last seven days when dates are omitted; goal listing does not take report dates.

## Arguments

- `project_id`: required; integer. greater than: 0. Project ID from project discovery.
- `metrics`: required; array of string. minimum items: 1; maximum items: 20. Yandex Metrika metric names.
- `dimensions`: optional; array of string or null. Schema default: `null`. maximum items: 10. Yandex Metrika dimension names.
- `date_from`: optional; string or null. Schema default: `null`. Start of the requested reporting or change period.
- `date_to`: optional; string or null. Schema default: `null`. End of the requested period; inclusivity depends on the tool.
- `filters`: optional; string or null. Schema default: `null`. Yandex Metrika API filter expression.
- `sort`: optional; array of string. Schema default: `[]`. minimum items: 0; maximum items: 5. Sort specification; its shape and allowed fields differ by tool.
- `limit`: optional; integer. Schema default: `100`. maximum: 1000; greater than: 0. Maximum rows or records requested for this page of results.
- `offset`: optional; integer. Schema default: `1`. minimum: 1. Starting offset; follow this tool's minimum and default.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_metrika_custom_query",
    "arguments": {
      "project_id": 123,
      "metrics": [
        "ym:s:visits",
        "ym:s:users"
      ],
      "dimensions": [
        "ym:s:startURL"
      ],
      "filters": "ym:s:trafficSource=='organic'",
      "sort": [
        "-ym:s:visits"
      ],
      "date_from": "2026-10-01",
      "date_to": "2026-10-20",
      "limit": 20,
      "offset": 1
    }
  }
}
```

## Result

Interpret the returned tool content and structured data according to the current advertised output schema.

The complete input and output schemas are in [get_metrika_custom_query.json](../../schemas/get_metrika_custom_query.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

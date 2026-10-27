# get_metrika_pages_report

Retrieve a Yandex Metrika page report with selected metrics, dimensions and filters.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

The default report is users and visits by starting page URL. Metric, dimension and filter names use the Yandex Metrika API vocabulary.

This report requires a project with a connected Yandex Metrika counter. Most report tools use the last seven days when dates are omitted; goal listing does not take report dates.

## Arguments

- `project_id`: required; integer. greater than: 0. Project ID from project discovery.
- `metrics`: optional; array of string. Schema default: `["ym:s:users", "ym:s:visits"]`. minimum items: 1; maximum items: 20. Yandex Metrika metric names.
- `dimensions`: optional; array of string or null. Schema default: `["ym:s:startURL"]`. maximum items: 10. Yandex Metrika dimension names.
- `date_from`: optional; string or null. Schema default: `null`. Start of the requested reporting or change period.
- `date_to`: optional; string or null. Schema default: `null`. End of the requested period; inclusivity depends on the tool.
- `sort`: optional; array of string. Schema default: `[]`. minimum items: 0; maximum items: 5. Sort specification; its shape and allowed fields differ by tool.
- `limit`: optional; integer. Schema default: `15`. maximum: 100; greater than: 0. Maximum rows or records requested for this page of results.
- `filters`: optional; string or null. Schema default: `null`. Yandex Metrika API filter expression.
- `goal_ids`: optional; array of integer or null. Schema default: `null`. maximum items: 10. Metrika goal IDs from get_metrika_goals.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_metrika_pages_report",
    "arguments": {
      "project_id": 123,
      "date_from": "2026-10-01",
      "date_to": "2026-10-20",
      "limit": 20
    }
  }
}
```

## Result

Interpret the returned tool content and structured data according to the current advertised output schema.

The complete input and output schemas are in [get_metrika_pages_report.json](../../schemas/get_metrika_pages_report.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

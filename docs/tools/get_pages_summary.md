# get_pages_summary

Retrieve page search-performance summaries from Google Search Console and Yandex Webmaster.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

Requires connected GSC or Yandex Webmaster data. Dates must be no later than three days before the current date. A comparison requires both previous-period dates. URL filtering is an object with value and optional compare_type, default contains. Sorting uses a comma-separated string; a leading minus sign means descending.

## Arguments

- `project_id`: required; integer. greater than: 0. Project ID from project discovery.
- `source`: optional; "gsc" | "webmaster" | "all". Schema default: `"all"`. Search-performance data source.
- `date_from`: optional; string or null. Schema default: `null`. Start of the requested reporting or change period.
- `date_to`: optional; string or null. Schema default: `null`. End of the requested period; inclusivity depends on the tool.
- `prev_date_from`: optional; string or null. Schema default: `null`. Start of the comparison period; pair with prev_date_to.
- `prev_date_to`: optional; string or null. Schema default: `null`. End of the comparison period; pair with prev_date_from.
- `url`: optional; object with string values or null. Schema default: `null`. Search-performance URL filter object.
- `metrics_filter`: optional; object with object with integer or number values values or null. Schema default: `null`. Metric-range filter object in the search-performance report.
- `sort`: optional; string or null. Schema default: `"-impressions"`. Sort specification; its shape and allowed fields differ by tool.
- `limit`: optional; integer or null. Schema default: `null`. greater than: 0. Maximum rows or records requested for this page of results.
- `offset`: optional; integer or null. Schema default: `null`. minimum: 0. Starting offset; follow this tool's minimum and default.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_pages_summary",
    "arguments": {
      "project_id": 123,
      "source": "gsc",
      "date_from": "2026-10-01",
      "date_to": "2026-10-20",
      "url": {
        "value": "/blog/",
        "compare_type": "contains"
      },
      "limit": 20
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `result`: array of object; required in the output schema.

The complete input and output schemas are in [get_pages_summary.json](../../schemas/get_pages_summary.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

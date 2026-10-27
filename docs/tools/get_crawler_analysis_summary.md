# get_crawler_analysis_summary

Retrieve the latest crawler-audit summary, health score, issue counts and optional history.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

Requires a configured crawler audit. results.health.rank ranges from 0 to 1. is_updating means totals are incomplete. history=days covers the last 31 days; weeks returns weekly medians for the last year; months returns monthly medians for all history. Use history_blocks to request only relevant summary blocks.

## Arguments

- `domain`: required; string. minimum text length: 1. Project or target domain, such as example.com.
- `history`: optional; "none" | "days" | "weeks" | "months". Schema default: `"none"`. Crawler-summary history interval.
- `history_blocks`: optional; array of string or null. Schema default: `null`. Crawler-summary result blocks for which history is needed.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_crawler_analysis_summary",
    "arguments": {
      "domain": "example.com",
      "history": "none"
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `id`: string; required in the output schema.
- `domain`: string; required in the output schema.
- `created`: string or null; optional in the output schema.
- `started`: string or null; optional in the output schema.
- `updated`: string or null; optional in the output schema.
- `modified`: string or null; optional in the output schema.
- `is_updating`: boolean; required in the output schema.
- `is_expired`: boolean; required in the output schema.
- `is_not_responding`: boolean; required in the output schema.
- `pages_limit`: integer; required in the output schema.
- `indexed_links_count`: integer; required in the output schema.
- `failed_links_count`: integer; required in the output schema.
- `new_links_count`: integer; required in the output schema.
- `in_progress_links_count`: integer; required in the output schema.
- `not_canonical_links_count`: integer; required in the output schema.
- `use_robots_txt`: boolean; required in the output schema.
- `robot_type`: string or null; optional in the output schema.
- `crawler_mode`: array of string; required in the output schema.
- `used_sitemaps`: array of string; optional in the output schema.
- `crawler_user_links`: array of string; optional in the output schema.
- `results`: object; required in the output schema.
- `history`: object with object with object values values or null; optional in the output schema.

The complete input and output schemas are in [get_crawler_analysis_summary.json](../../schemas/get_crawler_analysis_summary.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

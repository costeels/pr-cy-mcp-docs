# get_changed_crawler_pages

Find audited pages whose selected tracked field changed during a date range.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

Requires a configured crawler audit. Select one tracked field per call. Date boundaries are inclusive in the account time zone. Returned page history is not clipped to the date range. Both dates should be supplied for an unambiguous range. Pages from older audits can be present.

## Arguments

- `domain`: required; string. minimum text length: 1. Project or target domain, such as example.com.
- `field`: required; "statusCode" | "title" | "description" | "h1Content" | "textLength" | "noIndexRobots" | "noIndexHttp" | "noIndexMeta" | "canonicalFromHeader" | "canonicalFromHtml". Tracked crawler history field to inspect.
- `value`: optional; boolean or integer or null. Schema default: `null`. Optional tracked-field value filter.
- `date_from`: optional; string or null. Schema default: `null`. Start of the requested reporting or change period.
- `date_to`: optional; string or null. Schema default: `null`. End of the requested period; inclusivity depends on the tool.
- `limit`: optional; integer. Schema default: `20`. minimum: 1; maximum: 100. Maximum rows or records requested for this page of results.
- `offset`: optional; integer. Schema default: `0`. minimum: 0. Starting offset; follow this tool's minimum and default.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_changed_crawler_pages",
    "arguments": {
      "domain": "example.com",
      "field": "title",
      "date_from": "2026-10-01",
      "date_to": "2026-10-20",
      "limit": 20
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `pages`: array of object; required in the output schema.
- `total_pages_count`: integer; required in the output schema.
- `has_more`: boolean; required in the output schema.

The complete input and output schemas are in [get_changed_crawler_pages.json](../../schemas/get_changed_crawler_pages.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

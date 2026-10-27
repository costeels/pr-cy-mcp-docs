# get_keywords_by_url

Retrieve keywords associated with a page URL.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Arguments

- `page_url`: required; string. Full URL of the page to inspect.
- `per_page`: optional; integer. Schema default: `20`. minimum: 1; maximum: 1000. Maximum number of page-keyword results.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_keywords_by_url",
    "arguments": {
      "page_url": "https://example.com/laptops/",
      "per_page": 20
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `task_id`: string; required in the output schema.
- `organic_keywords_total`: integer; required in the output schema.
- `organic_keywords`: array of object or null; required in the output schema.

The complete input and output schemas are in [get_keywords_by_url.json](../../schemas/get_keywords_by_url.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

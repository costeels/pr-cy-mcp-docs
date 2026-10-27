# get_position

Retrieve a domain's search ranking for several comma-separated keyword phrases in one request.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

Batch phrases in a single comma-separated keywords string. Use domain, not page_url. The captured engine and top enum values are listed below.

## Arguments

- `keywords`: required; string. Comma-separated keyword phrases.
- `domain`: required; string. Project or target domain, such as example.com.
- `engine`: optional; "google" | "yandexLive". Schema default: `"google"`. Search engine identifier supported by this tool.
- `device`: optional; "desktop" | "mobile". Schema default: `"desktop"`. Device category supported by this tool.
- `top`: optional; 10 | 20 | 50 | 100. Schema default: `10`. Maximum search-result or ranking depth.
- `region`: optional; integer or null. Schema default: `null`. Search region, or the region name for get_region.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_position",
    "arguments": {
      "keywords": "buy laptop, gaming laptop",
      "domain": "example.com",
      "engine": "google",
      "device": "desktop",
      "top": 100
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `task_id`: string; required in the output schema.
- `engine`: string; required in the output schema.
- `keywords_positions`: array of object or null; required in the output schema.

The complete input and output schemas are in [get_position.json](../../schemas/get_position.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

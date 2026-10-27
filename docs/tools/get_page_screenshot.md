# get_page_screenshot

Capture a public-page screenshot using a selected device type.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

device_type uses smartphone, tablet and desktop. This differs from the mobile value accepted by SERP tools. The captured default is tablet.

## Arguments

- `page_url`: required; string. Full URL of the page to inspect.
- `full_page`: optional; boolean. Schema default: `false`. Capture the complete page when true.
- `device_type`: optional; "smartphone" | "tablet" | "desktop". Schema default: `"tablet"`. Screenshot device type.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_page_screenshot",
    "arguments": {
      "page_url": "https://example.com/",
      "device_type": "desktop",
      "full_page": true
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `task_id`: string; required in the output schema.
- `screenshot_url`: string or null; required in the output schema.
- `page_url`: string or null; required in the output schema.

The complete input and output schemas are in [get_page_screenshot.json](../../schemas/get_page_screenshot.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

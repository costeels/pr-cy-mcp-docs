# get_serp

Retrieve search results for one keyword from Google or live Yandex search.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

engine accepts google and yandexLive. language is fixed to ru. top accepts 10, 20, 50 or 100. with_related_values can request additional related data.

## Arguments

- `keyword`: required; string. Keyword phrase.
- `engine`: optional; "google" | "yandexLive". Schema default: `"google"`. Search engine identifier supported by this tool.
- `language`: optional; "ru". Schema default: `"ru"`. Search-interface language; the captured SERP schema fixes this to ru.
- `device`: optional; "desktop" | "mobile". Schema default: `"desktop"`. Device category supported by this tool.
- `top`: optional; 10 | 20 | 50 | 100. Schema default: `10`. Maximum search-result or ranking depth.
- `region`: optional; integer or null. Schema default: `null`. Search region, or the region name for get_region.
- `with_related_values`: optional; boolean. Schema default: `false`. Include related values in a SERP response.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_serp",
    "arguments": {
      "keyword": "buy laptop",
      "engine": "google",
      "device": "desktop",
      "top": 10
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `task_id`: string; required in the output schema.
- `serp`: array of object; required in the output schema.
- `related_questions`: array of object or null; optional in the output schema.
- `related_searches`: array of object or null; optional in the output schema.

The complete input and output schemas are in [get_serp.json](../../schemas/get_serp.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

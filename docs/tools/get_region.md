# get_region

Resolve region names to region IDs for a selected search engine.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

The accepted engines are yandex, google and yandexLive. Use a region ID returned for the engine used by the subsequent request.

## Arguments

- `engine`: required; "yandex" | "google" | "yandexLive". Search engine identifier supported by this tool.
- `region`: required; string. Search region, or the region name for get_region.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_region",
    "arguments": {
      "engine": "yandexLive",
      "region": "Moscow"
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `result`: array of object; required in the output schema.

The complete input and output schemas are in [get_region.json](../../schemas/get_region.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

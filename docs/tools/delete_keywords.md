# delete_keywords

Delete selected keywords by their numeric keyword IDs.

Operation: changes data, launches work or generates content.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

At most 500 IDs per call. Read the intended keywords and use the specific IDs relevant to the requested deletion.

## Arguments

- `keyword_ids`: required; array of integer. minimum items: 1; maximum items: 500. Keyword IDs from project keyword discovery.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "delete_keywords",
    "arguments": {
      "keyword_ids": [
        123,
        124
      ]
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `status`: "success" | "error"; required in the output schema.

The complete input and output schemas are in [delete_keywords.json](../../schemas/delete_keywords.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

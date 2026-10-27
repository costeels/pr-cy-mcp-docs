# update_group_keywords

Update the assignment of keyword IDs to a keyword group.

Operation: changes data, launches work or generates content.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Arguments

- `group_id`: required; integer. greater than: 0. Keyword-group ID returned by group discovery or creation.
- `keyword_ids`: required; array of integer. minimum items: 0; maximum items: 100. Keyword IDs from project keyword discovery.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "update_group_keywords",
    "arguments": {
      "group_id": 456,
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

The complete input and output schemas are in [update_group_keywords.json](../../schemas/update_group_keywords.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

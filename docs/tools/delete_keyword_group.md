# delete_keyword_group

Delete a keyword group by its group ID.

Operation: changes data, launches work or generates content.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Arguments

- `group_id`: required; integer. greater than: 0. Keyword-group ID returned by group discovery or creation.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "delete_keyword_group",
    "arguments": {
      "group_id": 456
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `status`: "success" | "error"; required in the output schema.

The complete input and output schemas are in [delete_keyword_group.json](../../schemas/delete_keyword_group.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

# get_user_projects

List PR-CY projects available to the connected account.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Arguments

No arguments are required. Pass an empty object.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_user_projects",
    "arguments": {}
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `result`: array of object; required in the output schema.

The complete input and output schemas are in [get_user_projects.json](../../schemas/get_user_projects.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

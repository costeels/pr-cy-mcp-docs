# list_artifact_revisions

List revisions of an artifact.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Arguments

- `artifact_id`: required; integer. greater than: 0. Artifact ID returned by artifact creation or listing.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "list_artifact_revisions",
    "arguments": {
      "artifact_id": 123
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `artifact`: object; required in the output schema.
- `revisions`: array of object; required in the output schema.

The complete input and output schemas are in [list_artifact_revisions.json](../../schemas/list_artifact_revisions.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

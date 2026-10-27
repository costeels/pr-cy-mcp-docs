# read_artifact

Read the active artifact draft or a specified revision.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

Omit revision_id to read the active revision. Obtain its current revision ID before write operations.

## Arguments

- `artifact_id`: required; integer. greater than: 0. Artifact ID returned by artifact creation or listing.
- `revision_id`: optional; integer or null. Schema default: `null`. Draft revision ID; use the current revision when guarding a write.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "read_artifact",
    "arguments": {
      "artifact_id": 123
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `artifact`: object; required in the output schema.
- `revision`: object; required in the output schema.

The complete input and output schemas are in [read_artifact.json](../../schemas/read_artifact.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

# validate_artifact

Validate the active artifact revision and report errors.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

Response metadata includes is_valid and errors with line, column and message.

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
    "name": "validate_artifact",
    "arguments": {
      "artifact_id": 123
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `revision`: object; required in the output schema.
- `meta`: object or null; optional in the output schema.

The complete input and output schemas are in [validate_artifact.json](../../schemas/validate_artifact.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

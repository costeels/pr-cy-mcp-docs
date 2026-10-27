# finalize_artifact

Finalize the active artifact draft as the next version.

Operation: changes data, launches work or generates content.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

Read or edit the artifact first and use its current draft revision_id. Finalization creates the next finalized version.

## Arguments

- `artifact_id`: required; integer. greater than: 0. Artifact ID returned by artifact creation or listing.
- `revision_id`: required; integer. greater than: 0. Draft revision ID; use the current revision when guarding a write.
- `message`: optional; string or null. Schema default: `null`. Message associated with artifact finalization.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "finalize_artifact",
    "arguments": {
      "artifact_id": 123,
      "revision_id": 456,
      "message": "Publish the completed SEO report"
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `artifact`: object; required in the output schema.
- `revision`: object; required in the output schema.

The complete input and output schemas are in [finalize_artifact.json](../../schemas/finalize_artifact.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

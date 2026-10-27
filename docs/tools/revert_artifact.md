# revert_artifact

Restore the active artifact draft from a selected revision.

Operation: changes data, launches work or generates content.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

to_revision_id identifies the revision to restore. revision_id can guard against concurrent changes to the active draft.

## Arguments

- `artifact_id`: required; integer. greater than: 0. Artifact ID returned by artifact creation or listing.
- `to_revision_id`: required; integer. greater than: 0. Target revision ID for a comparison or restoration.
- `revision_id`: optional; integer or null. Schema default: `null`. Draft revision ID; use the current revision when guarding a write.
- `created_by`: optional; "assistant" | "user". Schema default: `"assistant"`. Revision author category.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "revert_artifact",
    "arguments": {
      "artifact_id": 123,
      "to_revision_id": 456,
      "revision_id": 457
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `revision`: object; required in the output schema.
- `meta`: object or null; optional in the output schema.

The complete input and output schemas are in [revert_artifact.json](../../schemas/revert_artifact.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

# diff_artifact

Compare two artifact revisions using a unified diff.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

from_revision_id identifies the source revision. Omit to_revision_id to compare with the active revision.

## Arguments

- `artifact_id`: required; integer. greater than: 0. Artifact ID returned by artifact creation or listing.
- `from_revision_id`: required; integer. greater than: 0. Source revision ID for a diff.
- `to_revision_id`: optional; integer or null. Schema default: `null`. Target revision ID for a comparison or restoration.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "diff_artifact",
    "arguments": {
      "artifact_id": 123,
      "from_revision_id": 456,
      "to_revision_id": 457
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `from_revision`: object; required in the output schema.
- `to_revision`: object; required in the output schema.
- `is_equal`: boolean; required in the output schema.
- `diff`: string; required in the output schema.

The complete input and output schemas are in [diff_artifact.json](../../schemas/diff_artifact.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

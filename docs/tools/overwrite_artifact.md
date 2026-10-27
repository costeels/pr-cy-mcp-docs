# overwrite_artifact

Replace the content of the active artifact draft using its current revision ID.

Operation: changes data, launches work or generates content.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

Use the current revision_id from a read or prior edit. Read again after a conflict. Large content is safer to build in smaller changes.

## Arguments

- `artifact_id`: required; integer. greater than: 0. Artifact ID returned by artifact creation or listing.
- `revision_id`: required; integer. greater than: 0. Draft revision ID; use the current revision when guarding a write.
- `content`: required; string. HTML draft content.
- `created_by`: optional; "assistant" | "user". Schema default: `"assistant"`. Revision author category.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "overwrite_artifact",
    "arguments": {
      "artifact_id": 123,
      "revision_id": 456,
      "content": "<h1>Updated SEO report</h1>"
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `revision`: object; required in the output schema.
- `meta`: object or null; optional in the output schema.

The complete input and output schemas are in [overwrite_artifact.json](../../schemas/overwrite_artifact.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

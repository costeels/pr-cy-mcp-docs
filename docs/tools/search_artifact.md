# search_artifact

Find text in an artifact revision and return match positions and a match count.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

The response metadata includes matches with start/end positions and text, and count. revision_id can select an older revision.

## Arguments

- `artifact_id`: required; integer. greater than: 0. Artifact ID returned by artifact creation or listing.
- `search`: required; string. minimum text length: 1. Search text, or a list of substrings for article-block filtering.
- `revision_id`: optional; integer or null. Schema default: `null`. Draft revision ID; use the current revision when guarding a write.
- `case_sensitive`: optional; boolean. Schema default: `false`. Match text with case sensitivity when true.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "search_artifact",
    "arguments": {
      "artifact_id": 123,
      "search": "SEO report"
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `revision`: object; required in the output schema.
- `meta`: object or null; optional in the output schema.

The complete input and output schemas are in [search_artifact.json](../../schemas/search_artifact.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

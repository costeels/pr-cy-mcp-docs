# replace_range_in_artifact

Replace a range of characters in an artifact draft using its current revision ID.

Operation: changes data, launches work or generates content.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

start and length describe a range in the current draft. Pass the current revision_id. A zero length inserts the replacement without deleting existing characters.

## Arguments

- `artifact_id`: required; integer. greater than: 0. Artifact ID returned by artifact creation or listing.
- `revision_id`: required; integer. greater than: 0. Draft revision ID; use the current revision when guarding a write.
- `start`: required; integer. minimum: 0. Starting character offset for an artifact range, or seasonality start month.
- `length`: required; integer. minimum: 0. Character range length, or page extraction length control.
- `replacement`: required; string. Text inserted into the selected artifact range.
- `created_by`: optional; "assistant" | "user". Schema default: `"assistant"`. Revision author category.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "replace_range_in_artifact",
    "arguments": {
      "artifact_id": 123,
      "revision_id": 456,
      "start": 0,
      "length": 0,
      "replacement": "<!-- Updated report -->"
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `revision`: object; required in the output schema.
- `meta`: object or null; optional in the output schema.

The complete input and output schemas are in [replace_range_in_artifact.json](../../schemas/replace_range_in_artifact.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

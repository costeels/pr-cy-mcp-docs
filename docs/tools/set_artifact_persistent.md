# set_artifact_persistent

Enable or disable persistent storage for a finalized artifact version.

Operation: changes data, launches work or generates content.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

version is a finalized version number, not a draft revision_id.

## Arguments

- `artifact_id`: required; integer. greater than: 0. Artifact ID returned by artifact creation or listing.
- `version`: required; integer. greater than: 0. Finalized artifact version number.
- `is_persistent`: required; boolean. Enable persistent storage of the finalized version.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "set_artifact_persistent",
    "arguments": {
      "artifact_id": 123,
      "version": 1,
      "is_persistent": true
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `revision`: object; required in the output schema.
- `meta`: object or null; optional in the output schema.

The complete input and output schemas are in [set_artifact_persistent.json](../../schemas/set_artifact_persistent.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

# create_artifact

Create an HTML artifact and its initial draft.

Operation: changes data, launches work or generates content.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

Only html artifacts are supported in the captured interface. Start large documents with a short draft, then add or replace content in smaller calls.

## Arguments

- `type`: optional; "html". Schema default: `"html"`. Artifact type; only html is supported.
- `title`: optional; string or null. Schema default: `null`. Artifact title or a title filter, depending on the tool.
- `content`: optional; string. Schema default: `""`. HTML draft content.
- `created_by`: optional; "assistant" | "user". Schema default: `"assistant"`. Revision author category.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "create_artifact",
    "arguments": {
      "type": "html",
      "title": "SEO report",
      "content": "<!doctype html><html lang=\"en\"><head><title>SEO report</title></head><body><h1>SEO report</h1></body></html>"
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `artifact`: object; required in the output schema.
- `revision`: object; required in the output schema.

The complete input and output schemas are in [create_artifact.json](../../schemas/create_artifact.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

# set_article_content

Replace an article body and remove its existing blocks.

Operation: changes data, launches work or generates content.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

This replaces existing article blocks. Read the current article first. Use incremental block inserts instead of replacing a long article in a single oversized call.

## Arguments

- `article_id`: required; string. minimum text length: 1. Article ID returned by article creation or listing.
- `body`: required; array of object. Structured article body content.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "set_article_content",
    "arguments": {
      "article_id": "ARTICLE_ID",
      "body": [
        {
          "type": "paragraph",
          "data": {
            "text": "Updated guide."
          }
        }
      ]
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `id`: string; required in the output schema.
- `name`: string; required in the output schema.
- `body`: array of object or null; optional in the output schema.
- `extraData`: object or null; optional in the output schema.
- `dateCreated`: string or null; optional in the output schema.
- `dateUpdated`: string or null; optional in the output schema.
- `hasInvites`: boolean or null; optional in the output schema.

The complete input and output schemas are in [set_article_content.json](../../schemas/set_article_content.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

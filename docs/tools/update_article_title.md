# update_article_title

Change the name of an article.

Operation: changes data, launches work or generates content.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Arguments

- `article_id`: required; string. minimum text length: 1. Article ID returned by article creation or listing.
- `name`: required; string. minimum text length: 1; maximum text length: 255. Name of the article, keyword group or project note.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "update_article_title",
    "arguments": {
      "article_id": "ARTICLE_ID",
      "name": "Updated laptop buying guide"
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `id`: string; required in the output schema.
- `name`: string; required in the output schema.
- `dateCreated`: string or null; optional in the output schema.
- `dateUpdated`: string or null; optional in the output schema.
- `hasInvites`: boolean or null; optional in the output schema.

The complete input and output schemas are in [update_article_title.json](../../schemas/update_article_title.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

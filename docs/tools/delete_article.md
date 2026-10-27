# delete_article

Delete an article identified by its article ID.

Operation: changes data, launches work or generates content.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Arguments

- `article_id`: required; string. minimum text length: 1. Article ID returned by article creation or listing.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "delete_article",
    "arguments": {
      "article_id": "ARTICLE_ID"
    }
  }
}
```

## Result

Interpret the returned tool content and structured data according to the current advertised output schema.

The complete input and output schemas are in [delete_article.json](../../schemas/delete_article.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

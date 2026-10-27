# count_article_blocks

Count article blocks matching substring and block-type filters without returning the blocks.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

Search substrings combine with OR; search and types combine with AND. This tool exposes only article_id, search and types, not the neighboring-context inputs of get_article_blocks.

## Arguments

- `article_id`: required; string. minimum text length: 1. Article ID returned by article creation or listing.
- `search`: optional; array of string or null. Schema default: `null`. Search text, or a list of substrings for article-block filtering.
- `types`: optional; array of "paragraph" | "header" | "list" | "image" | "quote" | "code" | "delimiter" | "table" or null. Schema default: `null`. Article block types to include.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "count_article_blocks",
    "arguments": {
      "article_id": "ARTICLE_ID",
      "search": [
        "laptop"
      ]
    }
  }
}
```

## Result

Interpret the returned tool content and structured data according to the current advertised output schema.

The complete input and output schemas are in [count_article_blocks.json](../../schemas/count_article_blocks.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

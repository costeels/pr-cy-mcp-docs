# get_article_blocks

Retrieve article blocks matching substring and block-type filters, with optional neighboring context.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

The search and types filters combine with AND. Individual search substrings combine with OR. Context windows from blocks_before and blocks_after are merged, preserve article order and do not increase blocksCount, which counts matches only.

## Arguments

- `article_id`: required; string. minimum text length: 1. Article ID returned by article creation or listing.
- `search`: optional; array of string or null. Schema default: `null`. Search text, or a list of substrings for article-block filtering.
- `types`: optional; array of "paragraph" | "header" | "list" | "image" | "quote" | "code" | "delimiter" | "table" or null. Schema default: `null`. Article block types to include.
- `variant`: optional; "full" | "meta". Schema default: `"full"`. Article-block response variant.
- `blocks_before`: optional; integer. Schema default: `0`. minimum: 0. Neighboring blocks before each matching article block.
- `blocks_after`: optional; integer. Schema default: `0`. minimum: 0. Neighboring blocks after each matching article block.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_article_blocks",
    "arguments": {
      "article_id": "ARTICLE_ID",
      "search": [
        "laptop"
      ],
      "blocks_before": 1,
      "blocks_after": 1
    }
  }
}
```

## Result

Interpret the returned tool content and structured data according to the current advertised output schema.

The complete input and output schemas are in [get_article_blocks.json](../../schemas/get_article_blocks.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

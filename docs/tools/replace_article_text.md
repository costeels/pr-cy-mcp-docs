# replace_article_text

Find and replace text in article block data.text, data.code and data.caption fields.

Operation: changes data, launches work or generates content.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

Replacement searches data.text, data.code and data.caption. Choose replace_all and use_regex deliberately; they are not enabled by default.

## Arguments

- `article_id`: required; string. minimum text length: 1. Article ID returned by article creation or listing.
- `search`: required; string. minimum text length: 1. Search text, or a list of substrings for article-block filtering.
- `replace`: required; string. Replacement text.
- `use_regex`: optional; boolean. Schema default: `false`. Interpret the article search expression as a regular expression.
- `replace_all`: optional; boolean. Schema default: `true`. Replace every match when true.
- `block_ids`: optional; array of string or null. Schema default: `null`. Limit article-text replacement to these block IDs.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "replace_article_text",
    "arguments": {
      "article_id": "ARTICLE_ID",
      "search": "notebook",
      "replace": "laptop",
      "replace_all": true
    }
  }
}
```

## Result

Interpret the returned tool content and structured data according to the current advertised output schema.

The complete input and output schemas are in [replace_article_text.json](../../schemas/replace_article_text.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

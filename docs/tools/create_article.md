# create_article

Create an article with a name and optional initial blocks.

Operation: changes data, launches work or generates content.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

For long articles, create a small initial article and insert the remaining blocks with modify_article_blocks. A truncated oversized call may fail with a missing name field. Keep each insert to at most 50 blocks.

## Arguments

- `name`: required; string. minimum text length: 1; maximum text length: 255. Name of the article, keyword group or project note.
- `body`: optional; array of object or null. Schema default: `null`. Structured article body content.

### CodeBlock

- `id`: optional; string or null. Schema default: `null`.
- `type`: optional; "code". Schema default: `"code"`. Artifact type; only html is supported.
- `data`: required; object.

### CodeData

- `code`: required; string.

### DelimiterBlock

- `id`: optional; string or null. Schema default: `null`.
- `type`: optional; "delimiter". Schema default: `"delimiter"`. Artifact type; only html is supported.
- `data`: required; object.

### DelimiterData


### HeaderBlock

- `id`: optional; string or null. Schema default: `null`.
- `type`: optional; "header". Schema default: `"header"`. Artifact type; only html is supported.
- `data`: required; object.

### HeaderData

- `text`: required; string. Project note text.
- `level`: required; integer. minimum: 1; maximum: 6.

### ImageBlock

- `id`: optional; string or null. Schema default: `null`.
- `type`: optional; "image". Schema default: `"image"`. Artifact type; only html is supported.
- `data`: required; object.

### ImageData

- `file`: required; object.
- `caption`: optional; string or null. Schema default: `null`.
- `withBorder`: optional; boolean or null. Schema default: `null`.
- `stretched`: optional; boolean or null. Schema default: `null`.
- `withBackground`: optional; boolean or null. Schema default: `null`.

### ImageFile

- `url`: required; string. Search-performance URL filter object.

### ListBlock

- `id`: optional; string or null. Schema default: `null`.
- `type`: optional; "list". Schema default: `"list"`. Artifact type; only html is supported.
- `data`: required; object.

### ListData

- `style`: required; "ordered" | "unordered".
- `items`: required; array of object.

### ListItem

- `content`: required; string. HTML draft content.
- `items`: optional; array of object or null. Schema default: `null`.

### ParagraphBlock

- `id`: optional; string or null. Schema default: `null`.
- `type`: optional; "paragraph". Schema default: `"paragraph"`. Artifact type; only html is supported.
- `data`: required; object.

### ParagraphData

- `text`: required; string. Project note text.

### QuoteBlock

- `id`: optional; string or null. Schema default: `null`.
- `type`: optional; "quote". Schema default: `"quote"`. Artifact type; only html is supported.
- `data`: required; object.

### QuoteData

- `text`: required; string. Project note text.
- `caption`: optional; string or null. Schema default: `null`.
- `alignment`: optional; string or null. Schema default: `null`.

### TableBlock

- `id`: optional; string or null. Schema default: `null`.
- `type`: optional; "table". Schema default: `"table"`. Artifact type; only html is supported.
- `data`: required; object.

### TableData

- `withHeadings`: optional; boolean or null. Schema default: `null`.
- `content`: required; array of array of string. HTML draft content.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "create_article",
    "arguments": {
      "name": "Laptop buying guide"
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

The complete input and output schemas are in [create_article.json](../../schemas/create_article.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

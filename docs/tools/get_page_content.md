# get_page_content

Extract a public page as Markdown, HTML, or a compact metadata-and-headings structure.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

format=md and format=html return page content. format=structure returns metadata, a heading outline and statistics without the page body. Use structure for a compact initial review of several pages.

## Arguments

- `page_url`: required; string. Full URL of the page to inspect.
- `format`: optional; "md" | "html" | "structure". Schema default: `"md"`. Page extraction format: md, html or structure.
- `delete_links`: optional; boolean. Schema default: `false`. Remove links from extracted page content when true.
- `delete_images`: optional; boolean. Schema default: `false`. Remove images from extracted page content when true.
- `length`: optional; integer. Schema default: `0`. Character range length, or page extraction length control.
- `headings_max_level`: optional; integer. Schema default: `3`. minimum: 1; maximum: 6. Deepest heading level to retain in the structure response.
- `max_headings`: optional; integer. Schema default: `200`. minimum: 1; maximum: 1000. Maximum heading count in a structure response.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_page_content",
    "arguments": {
      "page_url": "https://example.com/",
      "format": "structure"
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `task_id`: string; required in the output schema.
- `text_in_markdown`: string or null; optional in the output schema.
- `html_code`: string or null; optional in the output schema.
- `meta`: object or null; optional in the output schema.
- `outline`: array of object or null; optional in the output schema.
- `stats`: object or null; optional in the output schema.

The complete input and output schemas are in [get_page_content.json](../../schemas/get_page_content.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

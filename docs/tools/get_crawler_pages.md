# get_crawler_pages

List audited website pages with full page checks and combined issue filters.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

Requires a configured project crawler audit. Filters combine with AND. Issue flags filter when true; false behaves like an omitted flag. Responses contain pages, total_pages_count and has_more. Keep page size small when full page checks are not needed.

## Arguments

- `domain`: required; string. minimum text length: 1. Project or target domain, such as example.com.
- `url_contains`: optional; string or null. Schema default: `null`. Substring that an audited page URL must contain.
- `status_code`: optional; integer or null. Schema default: `null`. greater than: 0.
- `title_contains`: optional; string or null. Schema default: `null`.
- `title_equals`: optional; string or null. Schema default: `null`.
- `title_types`: optional; array of "none" | "short" | "long" | "normal" or null. Schema default: `null`.
- `duplicated_title`: optional; boolean. Schema default: `false`.
- `description_contains`: optional; string or null. Schema default: `null`.
- `description_equals`: optional; string or null. Schema default: `null`.
- `description_types`: optional; array of "none" | "short" | "long" | "normal" or null. Schema default: `null`.
- `duplicated_description`: optional; boolean. Schema default: `false`.
- `h1_contains`: optional; string or null. Schema default: `null`.
- `h1_equals`: optional; string or null. Schema default: `null`.
- `h1_types`: optional; array of "none" | "tooMany" | "normal" or null. Schema default: `null`.
- `duplicated_h1`: optional; boolean. Schema default: `false`.
- `h1_equals_title`: optional; boolean. Schema default: `false`.
- `canonical_status`: optional; "canonical" | "notCanonical" | "absentCanonical" | "error" or null. Schema default: `null`.
- `canonical_error_group`: optional; "all" | "multipleLinks" | "notAbsoluteLink" | "otherDomainLink" | "mismatchedLinks" | "insecureLink" or null. Schema default: `null`.
- `links_count_errors`: optional; array of "internal" | "external" | "normal" or null. Schema default: `null`.
- `charset_types`: optional; array of "success" | "info" | "error" or null. Schema default: `null`.
- `no_index`: optional; boolean or null. Schema default: `null`.
- `no_follow`: optional; boolean. Schema default: `false`.
- `slow_page`: optional; boolean. Schema default: `false`.
- `slow_ttfb`: optional; boolean. Schema default: `false`.
- `heavy_html`: optional; boolean. Schema default: `false`.
- `short_text`: optional; boolean. Schema default: `false`.
- `meta_refresh_found`: optional; boolean. Schema default: `false`.
- `redirect_is_insecure`: optional; boolean. Schema default: `false`.
- `insecure_links`: optional; boolean. Schema default: `false`.
- `absent_images_alt`: optional; boolean. Schema default: `false`.
- `links_with_double_slash`: optional; boolean. Schema default: `false`.
- `external_links_with_empty_anchor`: optional; boolean. Schema default: `false`.
- `internal_links_with_empty_anchor`: optional; boolean. Schema default: `false`.
- `links_without_href`: optional; boolean. Schema default: `false`.
- `has_broken_links`: optional; boolean. Schema default: `false`.
- `og_basic_not_filled`: optional; boolean. Schema default: `false`.
- `og_not_canonical`: optional; boolean. Schema default: `false`.
- `twitter_card_not_filled`: optional; boolean. Schema default: `false`.
- `sort`: optional; "loadTime" | "-loadTime" | "ttfb" | "-ttfb" | "htmlSize" | "-htmlSize" | "h1Count" | "-h1Count" | "title" | "-title" | "textLength" | "-textLength" | "internalLinksCount" | "-internalLinksCount" | "externalLinksCount" | "-externalLinksCount" | "insecureLinksCount" | "-insecureLinksCount" or null. Schema default: `null`. Sort specification; its shape and allowed fields differ by tool.
- `limit`: optional; integer. Schema default: `20`. minimum: 1; maximum: 100. Maximum rows or records requested for this page of results.
- `offset`: optional; integer. Schema default: `0`. minimum: 0. Starting offset; follow this tool's minimum and default.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_crawler_pages",
    "arguments": {
      "domain": "example.com",
      "duplicated_title": true,
      "limit": 20,
      "offset": 0
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `pages`: array of object; required in the output schema.
- `total_pages_count`: integer; required in the output schema.
- `has_more`: boolean; required in the output schema.

The complete input and output schemas are in [get_crawler_pages.json](../../schemas/get_crawler_pages.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

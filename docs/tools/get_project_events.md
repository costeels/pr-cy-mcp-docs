# get_project_events

Retrieve project timeline events for indexing, SSL, robots.txt, analytics and crawler-audit changes.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

Uses a domain, not project_id. Events are newest first and cannot be re-sorted. date_from is inclusive and date_to exclusive. Follow has_more even when fewer than limit events are returned. total_events_count is measured before exclusions. Event text uses the account language.

## Arguments

- `domain`: required; string. minimum text length: 1. Project or target domain, such as example.com.
- `date_from`: optional; string or null. Schema default: `null`. Start of the requested reporting or change period.
- `date_to`: optional; string or null. Schema default: `null`. End of the requested period; inclusivity depends on the tool.
- `exclude_events`: optional; array of "crawlerPagesChanged:canonicalFromHeader" | "crawlerPagesChanged:canonicalFromHtml" | "crawlerPagesChanged:description" | "crawlerPagesChanged:h1Content" | "crawlerPagesChanged:textLength" | "crawlerPagesChanged:noIndexHttp" | "crawlerPagesChanged:noIndexMeta" | "crawlerPagesChanged:noIndexRobots" | "crawlerPagesChanged:statusCode" | "expiration:future" | "expiration:past" | "expiration:soon" | "ga:connected" | "ga:disconnected" | "googleSafeBrowsing:no" | "googleSafeBrowsing:yes" | "gsc:connected" | "gsc:disconnected" | "note:created" | "pageSpeedConfigureViewport:no" | "pageSpeedConfigureViewport:yes" | "roskomnadzor:domainForbidden" | "roskomnadzor:domainPardoned" | "sitemap:exist" | "sitemap:notExist" | "todo:checked" | "todo:unchecked" | "webmaster:connected" | "webmaster:disconnected" | "weekReportStats:ga" | "wwwRedirect:exist" | "wwwRedirect:notExist" | "yandexIndex:indexed" | "yandexIndex:notIndexed" | "yandexSafeBrowsing:no" | "yandexSafeBrowsing:yes" | "crawlerPagesChanged:title" | "googleIndex:indexed" | "googleIndex:notIndexed" | "metrika:connected" | "metrika:disconnected" | "robotsTxt:allowed" | "robotsTxt:change" | "robotsTxt:disallowed" | "robotsTxt:exist" | "robotsTxt:notExist" | "ssl:exist" | "ssl:expired" | "ssl:notExist" | "ssl:renewed" | "ssl:soon_expire" | "yandexSqi:decreased" | "yandexSqi:increased" | "googleGlue:glued" | "googleGlue:notGlued" | "googleNews:exist" | "googleNews:notExist" | "httpStatusCode:siteRecovered" | "httpStatusCode:siteSick" | "keywordsGroupInTop10:decreased" | "keywordsGroupInTop10:increased" | "keywordsHistoryImport:done" | "keywordsInTop10:decreased" | "keywordsInTop10:increased" | "llmsTxt:exist" | "mailruCatalog:exist" | "mailruCatalog:notExist" | "organicSummary:changed" | "organicTopPages:clicksDecreased" | "organicTopPages:clicksIncreased" | "webArchive:exist" | "webmasterProblems:added" | "webmasterProblems:deleted" | "webmasterSearchablePagesCount:decreased" | "webmasterSearchablePagesCount:increased" | "weekReportStats:metrika" | "yandexAgs:sanctionsImposed" | "yandexAgs:sanctionsRemoved" | "yandexCatalog:exist" | "yandexCatalog:notExist" | "yandexGlue:glued" | "yandexGlue:notGlued" or null. Schema default: `null`. Event types excluded from the returned project timeline.
- `limit`: optional; integer. Schema default: `10`. minimum: 1; maximum: 500. Maximum rows or records requested for this page of results.
- `offset`: optional; integer. Schema default: `0`. minimum: 0. Starting offset; follow this tool's minimum and default.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_project_events",
    "arguments": {
      "domain": "example.com",
      "date_from": "2026-10-01",
      "date_to": "2026-10-21",
      "limit": 20,
      "offset": 0
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `events`: array of object; required in the output schema.
- `total_events_count`: integer; required in the output schema.
- `has_more`: boolean; required in the output schema.

The complete input and output schemas are in [get_project_events.json](../../schemas/get_project_events.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

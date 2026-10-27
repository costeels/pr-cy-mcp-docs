# get_user_project

Retrieve a PR-CY project by its numeric project ID.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Arguments

- `project_id`: required; integer. greater than: 0. Project ID from project discovery.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_user_project",
    "arguments": {
      "project_id": 123
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `id`: integer; required in the output schema.
- `domain`: string; required in the output schema.
- `status`: "active" | "hold" | "deleted"; required in the output schema.
- `initialized_advanced`: boolean; required in the output schema.
- `initialized_crawler`: boolean; required in the output schema.
- `initialized_keywords`: boolean; required in the output schema.
- `advanced_auto_update`: boolean; required in the output schema.
- `crawler_auto_update`: boolean; required in the output schema.
- `week_report`: boolean; required in the output schema.
- `requests_per_second`: integer; required in the output schema.
- `use_robots_txt`: boolean; required in the output schema.
- `crawler_mode`: array of "crawler" | "sitemap" | "userLinks"; required in the output schema.
- `crawler_user_links`: array of string; required in the output schema.
- `robot_type`: "*" | "Googlebot" | "Yandex" | "PR-CY-BOT"; required in the output schema.
- `crawler_restrict_rules`: array of string; required in the output schema.
- `allow_subdomains_in_serp`: boolean; required in the output schema.
- `ignore_wordstat_region`: boolean; required in the output schema.
- `wordstat_type`: "general" | "quoted" | "exact"; required in the output schema.
- `date_created`: string; required in the output schema.
- `ga_connected`: boolean or null; required in the output schema.
- `gsc_connected`: boolean or null; required in the output schema.
- `metrika_connected`: boolean or null; required in the output schema.
- `webmaster_connected`: boolean or null; required in the output schema.
- `enabled_timeline_events`: array of "crawlerPagesChanged:canonicalFromHeader" | "crawlerPagesChanged:canonicalFromHtml" | "crawlerPagesChanged:description" | "crawlerPagesChanged:h1Content" | "crawlerPagesChanged:textLength" | "crawlerPagesChanged:noIndexHttp" | "crawlerPagesChanged:noIndexMeta" | "crawlerPagesChanged:noIndexRobots" | "crawlerPagesChanged:statusCode" | "expiration:future" | "expiration:past" | "expiration:soon" | "ga:connected" | "ga:disconnected" | "googleSafeBrowsing:no" | "googleSafeBrowsing:yes" | "gsc:connected" | "gsc:disconnected" | "note:created" | "pageSpeedConfigureViewport:no" | "pageSpeedConfigureViewport:yes" | "roskomnadzor:domainForbidden" | "roskomnadzor:domainPardoned" | "sitemap:exist" | "sitemap:notExist" | "todo:checked" | "todo:unchecked" | "webmaster:connected" | "webmaster:disconnected" | "weekReportStats:ga" | "wwwRedirect:exist" | "wwwRedirect:notExist" | "yandexIndex:indexed" | "yandexIndex:notIndexed" | "yandexSafeBrowsing:no" | "yandexSafeBrowsing:yes" | "crawlerPagesChanged:title" | "googleIndex:indexed" | "googleIndex:notIndexed" | "metrika:connected" | "metrika:disconnected" | "robotsTxt:allowed" | "robotsTxt:change" | "robotsTxt:disallowed" | "robotsTxt:exist" | "robotsTxt:notExist" | "ssl:exist" | "ssl:expired" | "ssl:notExist" | "ssl:renewed" | "ssl:soon_expire" | "yandexSqi:decreased" | "yandexSqi:increased" | "googleGlue:glued" | "googleGlue:notGlued" | "googleNews:exist" | "googleNews:notExist" | "httpStatusCode:siteRecovered" | "httpStatusCode:siteSick" | "keywordsGroupInTop10:decreased" | "keywordsGroupInTop10:increased" | "keywordsHistoryImport:done" | "keywordsInTop10:decreased" | "keywordsInTop10:increased" | "llmsTxt:exist" | "mailruCatalog:exist" | "mailruCatalog:notExist" | "organicSummary:changed" | "organicTopPages:clicksDecreased" | "organicTopPages:clicksIncreased" | "webArchive:exist" | "webmasterProblems:added" | "webmasterProblems:deleted" | "webmasterSearchablePagesCount:decreased" | "webmasterSearchablePagesCount:increased" | "weekReportStats:metrika" | "yandexAgs:sanctionsImposed" | "yandexAgs:sanctionsRemoved" | "yandexCatalog:exist" | "yandexCatalog:notExist" | "yandexGlue:glued" | "yandexGlue:notGlued" or null; required in the output schema.
- `additional_timeline_events_emails`: array of string or null; required in the output schema.
- `base_analytic_system`: "ga" | "gsc" | "metrika" | "webmaster"; required in the output schema.

The complete input and output schemas are in [get_user_project.json](../../schemas/get_user_project.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

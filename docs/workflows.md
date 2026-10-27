# PR-CY MCP workflows

The JSON blocks below are tool argument objects. Replace demonstration domains and IDs with values returned by your own connection. These workflows describe how to combine tools; the examples were checked against interface schemas, not executed against a user's project.

## Keyword research and search results

Resolve the region for the search engine, then use its returned ID in the search request. `get_serp` uses `yandexLive` for Yandex search and supports a fixed `ru` search-interface language.

Tool: `get_region`.

```json
{
  "engine": "yandexLive",
  "region": "Moscow"
}
```

Tool: `get_serp`. Use the actual region ID returned above in place of the demonstration ID.

```json
{
  "keyword": "buy laptop",
  "engine": "yandexLive",
  "device": "mobile",
  "top": 10,
  "region": 213
}
```

For a first pass over competing pages, extract metadata and headings with `get_page_content.format=structure`. Fetch full Markdown only for pages that need a closer content review.

Tool: `get_page_content`.

```json
{
  "page_url": "https://example.com/laptops/",
  "format": "structure"
}
```

For keyword demand, batch phrases and accuracy types. The captured `get_wordstat` schema has no `engine` parameter. Use `types` and `regions`; the singular `type` and `region` inputs are legacy compatibility fields.

Tool: `get_wordstat`.

```json
{
  "keywords": "buy laptop, gaming laptop",
  "types": ["general", "exact"],
  "regions": [213],
  "need_related_phrases": true,
  "need_including_phrases": true
}
```

`general` is broad phrase demand; `quoted` keeps the phrase word count while allowing word forms; `exact` keeps word forms without fixing word order. The numeric result is estimated monthly search demand, not traffic to a website. A null item in `regions` requests demand without a region restriction; omitting `regions` uses the current server default, Russia in the captured schema.

For a one-off domain ranking check, batch phrases with `get_position`:

```json
{
  "keywords": "buy laptop, gaming laptop",
  "domain": "example.com",
  "engine": "google",
  "device": "desktop",
  "top": 100
}
```

## Project ranking reports

Discover the project and search settings with `get_user_keywords_projects`. Use the returned `project_id` and `search_options_id` for a report. Rankings for different search engines, regions and devices are separate settings.

Tool: `get_keywords_summaries`.

```json
{
  "project_id": 123,
  "search_options_id": 456,
  "limit": 20,
  "offset": 0
}
```

Use `get_keywords_positions_history` for historical rankings. Use `check_positions` only when the task requests a fresh ranking check; it launches work and can consume check limits. If no search option is specified, it checks all active search options for the project.

## Website audits

Start with the current audit summary. The project must have crawler auditing configured.

Tool: `get_crawler_analysis_summary`.

```json
{
  "domain": "example.com",
  "history": "none"
}
```

The audit health rank at `results.health.rank` is between 0 and 1. If `is_updating` is true, the audit is still running and summary totals are incomplete. Use `get_crawler_pages` to identify the actual affected pages rather than inferring them from summary totals.

Tool: `get_crawler_pages`.

```json
{
  "domain": "example.com",
  "duplicated_title": true,
  "limit": 20,
  "offset": 0
}
```

Filters combine with AND. Issue flags operate when true; setting an issue flag to false does not select issue-free pages. Retrieve history only for the summary blocks relevant to your investigation.

Tool: `get_crawler_analysis_summary`.

```json
{
  "domain": "example.com",
  "history": "days",
  "history_blocks": ["health", "statusCode"]
}
```

Use `get_changed_crawler_pages` to find changes to a single tracked field in an inclusive date range. Returned history may cover a longer period than the query; interpret each history entry using its date.

```json
{
  "domain": "example.com",
  "field": "title",
  "date_from": "2026-10-01",
  "date_to": "2026-10-20",
  "limit": 20,
  "offset": 0
}
```

## Traffic and conversion reports

Connect Google Search Console, Yandex Webmaster or Yandex Metrika to the relevant PR-CY project before requesting its data. Use the IDs from project and goal discovery.

For search performance, select `gsc`, `webmaster` or `all` and use periods ending at least three days before the current date. In the example, October 1-10 is compared with October 11-20.

Tool: `get_pages_summary`.

```json
{
  "project_id": 123,
  "source": "gsc",
  "date_from": "2026-10-11",
  "date_to": "2026-10-20",
  "prev_date_from": "2026-10-01",
  "prev_date_to": "2026-10-10",
  "sort": "-impressions",
  "limit": 20,
  "offset": 0
}
```

Keyword and URL filters are objects, not plain strings:

```json
{
  "value": "/blog/",
  "compare_type": "contains"
}
```

Allowed comparisons are `equals`, `notEquals`, `startsWith`, `endsWith`, `contains`, `notContains` and `regex`. The default is `contains`; regex uses RE2 syntax. Do not confuse these objects with the plain-string `url_contains` crawler filter.

For a Metrika question covered by a specialized report, use that report. Otherwise build a custom query with requested metric and dimension names, Metrika filter syntax and sort fields.

Tool: `get_metrika_custom_query`.

```json
{
  "project_id": 123,
  "metrics": ["ym:s:visits", "ym:s:users"],
  "dimensions": ["ym:s:startURL"],
  "date_from": "2026-10-01",
  "date_to": "2026-10-20",
  "filters": "ym:s:trafficSource=='organic' AND ym:s:isRobot=='No'",
  "sort": ["-ym:s:visits"],
  "limit": 20,
  "offset": 1
}
```

Custom queries accept up to 20 metrics, 10 dimensions and 1,000 returned rows. Verify metric and dimension combinations against the [Yandex Metrika API reference](https://yandex.ru/dev/metrika/en/stat/attrandmetr/dim_all).

## Articles and HTML artifacts

Articles store structured blocks. For a long article, create the article first, then insert batches of blocks. The following is an illustrative short article creation input:

Tool: `create_article`.

```json
{
  "name": "Laptop buying guide"
}
```

Use the returned article ID in `modify_article_blocks`. `afterBlockId=null` inserts at the beginning; for an append, use the ID of the current last block. Read blocks to obtain stable IDs before editing or moving them.

```json
{
  "article_id": "ARTICLE_ID",
  "operations": [
    {
      "action": "insert",
      "afterBlockId": null,
      "blocks": [
        {
          "type": "paragraph",
          "data": {
            "text": "A practical guide to choosing a laptop."
          }
        }
      ]
    }
  ]
}
```

The operations `insert`, `modify`, `remove` and `move` run in order. An insert accepts at most 50 blocks. The block structures shown here are illustrative content objects; their internal `data` is open-ended in the advertised MCP schema.

HTML artifacts store draft revisions and finalized versions. Create a small draft, read the artifact and carry its current `revision_id` into edits. Validate before finalizing; use the revision ID returned by the latest edit when finalizing.

Tool: `create_artifact`.

```json
{
  "type": "html",
  "title": "SEO report",
  "content": "<!doctype html><html lang=\"en\"><head><title>SEO report</title></head><body><h1>SEO report</h1></body></html>"
}
```

Tool: `validate_artifact`.

```json
{
  "artifact_id": 123
}
```

Draft revision IDs and finalized version numbers are different identifiers. Use `set_artifact_persistent` with a finalized `version` number, not a draft `revision_id`.

## Project events and notes

Events are read-only timeline records accessed with a domain. Notes are user-created records accessed with a project ID. Event dates end exclusively; note dates end inclusively.

Tool: `get_project_events`. This range includes October 1 through October 20.

```json
{
  "domain": "example.com",
  "date_from": "2026-10-01",
  "date_to": "2026-10-21",
  "limit": 20,
  "offset": 0
}
```

When requested, record a site change using `create_project_note`. Use plain text without emoji. After an uncertain create response, check notes for the same period before retrying because creation is not deduplicated.

```json
{
  "project_id": 123,
  "name": "Updated category titles",
  "note_date": "2026-10-20",
  "text": "Updated title tags on laptop category pages."
}
```

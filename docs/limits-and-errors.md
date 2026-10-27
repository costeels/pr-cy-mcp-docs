# Limits, errors and pagination

PR-CY tools run with the permissions and limits of the connected account. Public-page and search tasks still require an API key. Project data requires access to the project and the relevant feature or external data connection.

## Check the appropriate limit

Use `get_user_limits` with a non-empty `limits_filter`. The `competitorsAnalysis` limit requires `project_id` and should not be requested as a project-independent limit.

```json
{
  "limits_filter": ["checks", "standardAnalysis"]
}
```

```json
{
  "project_id": 123,
  "limits_filter": ["competitorsAnalysis"]
}
```

These are illustrative inputs. An omitted filter has a schema default that includes `competitorsAnalysis`; selecting the limits explicitly avoids requesting that project-specific item without a project.

## Batch sizes

- `create_keywords`: at most 100 keywords per call.
- `delete_keywords` and `update_keywords_status`: at most 500 keyword IDs per call.
- `modify_article_blocks`: at most 100 operations per call and 50 blocks per insert operation.
- `get_wordstat`: up to five regions per call; seasonality covers up to 24 months.
- `get_metrika_custom_query`: at most 20 metrics, 10 dimensions and 1,000 returned rows per call.
- `generate_image`: up to 10 reference-image URLs in the captured schema.

Some limits are documented behavioral constraints rather than explicit JSON Schema limits. Check both the schema and the tool's behavior notes.

## Pagination

Most list tools use `limit` and `offset`, but there is no universal pagination contract. Look at the individual tool's default and minimum offset, and use its response fields to determine whether more results exist.

- Crawler page lists return `pages`, `total_pages_count` and `has_more`.
- Project events return `has_more`. A response can contain fewer than `limit` events while more pages remain. `total_events_count` is measured before `exclude_events` is applied.
- Project notes fetch the period's complete note list upstream, then apply `limit` and `offset` in the MCP tool. A narrower date range reduces upstream work.
- `get_metrika_custom_query.offset` starts at **1**, not 0.

## Dates and freshness

Use `YYYY-MM-DD` for tools that require calendar dates. Metrika report tools also accept the relative date strings advertised by their schemas, such as `today`, `yesterday` and `7daysAgo`. Most Metrika reports default to the last seven days if dates are omitted.

Google Search Console and Yandex Webmaster summary tools require dates no later than three days before the current date. Comparison inputs require both `prev_date_from` and `prev_date_to`. Date order must be valid.

Date boundaries differ between tools:

- `get_project_events`: `date_from` is inclusive; `date_to` is exclusive. To include a final calendar day, use the following day as `date_to`.
- `get_project_notes`: both boundaries are inclusive.
- `get_changed_crawler_pages`: both boundaries are inclusive in the account's time zone. Its response can include older history records; filter those records by their own dates when interpreting a requested period.

## Validation failures

For a missing field, invalid type or unsupported enum value, correct the input against the current tool schema. Do not repeatedly retry an unchanged invalid call. A JSON-schema-valid example does not guarantee project permissions, available limits or upstream data.

If a long `create_article` call fails with `name: Field required`, the model's tool call may have been truncated. Create a short article first, then insert smaller batches of blocks. Apply the same approach to large artifact content.

Article content replacement removes the existing blocks. Read the article before using `set_article_content`, and use `modify_article_blocks` for incremental changes.

## Concurrent artifact edits

Artifact write tools can require the current `revision_id`. Read the current artifact first and pass the returned revision ID. If another change has occurred, read again and reapply the intended edit to the current content. Do not guess an ID or blindly overwrite a newer revision.

## Unknown outcomes and access errors

After a timeout or uncertain response to a write, inspect the resource before retrying. In particular, `create_project_note` has no duplicate prevention: repeating the call can create a second note.

Project note readers and editors can have different permissions. A user with team access may read notes but be unable to edit them unless they are the note author or project owner. At least one of `name`, `note_date` or `text` must be supplied to `update_project_note`. Omitted or null fields remain unchanged; an empty `text` clears the text. Note deletion is not exposed by this tool set.

This reference does not promise a single fixed HTTP status-code mapping for every tool. Inspect the actual protocol error or tool result, then distinguish authentication, permissions, missing data, exhausted limits, validation errors and upstream failures.

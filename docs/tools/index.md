# PR-CY MCP tool reference

The live server advertised 69 tools on 2026-10-27 (analysis 1.30.0). Each page documents input types, required fields, enum values, defaults, behavioral limits, a JSON-RPC example and the output schema.

Examples use demonstration identifiers. Resolve real IDs using the appropriate discovery tools. Use the live tools/list response for newer server versions.

## Account and projects

- [get_user_limits](get_user_limits.md): Retrieve selected limits for the connected PR-CY account or project.
- [get_user_project](get_user_project.md): Retrieve a PR-CY project by its numeric project ID.
- [get_user_project_by_domain](get_user_project_by_domain.md): Retrieve a PR-CY project by its domain.
- [get_user_projects](get_user_projects.md): List PR-CY projects available to the connected account.
- [get_user_keywords_projects](get_user_keywords_projects.md): List keyword-ranking projects and their search-engine, language, region and device settings.

## Keywords and project rankings

- [get_keywords](get_keywords.md): List project keywords, keyword groups and target URLs.
- [create_keywords](create_keywords.md): Add a batch of keywords to a project, with optional target URLs and group assignments.
- [delete_keywords](delete_keywords.md): Delete selected keywords by their numeric keyword IDs.
- [update_keywords_status](update_keywords_status.md): Set selected project keywords to active or hold.
- [check_positions](check_positions.md): Launch a project keyword-ranking check for one or all active search settings.
- [get_keywords_summaries](get_keywords_summaries.md): Retrieve project keyword summaries for a selected search setting.
- [get_keywords_positions_history](get_keywords_positions_history.md): Retrieve historical project keyword rankings for a selected search setting.

## Keyword groups

- [get_project_keyword_groups](get_project_keyword_groups.md): List keyword groups in a PR-CY project.
- [create_keyword_group](create_keyword_group.md): Create a named keyword group in a project.
- [delete_keyword_group](delete_keyword_group.md): Delete a keyword group by its group ID.
- [update_group_keywords](update_group_keywords.md): Update the assignment of keyword IDs to a keyword group.

## Search and keyword demand

- [get_wordstat](get_wordstat.md): Retrieve estimated monthly keyword demand, related phrases, including phrases and optional seasonality across regions and accuracy types.
- [get_region](get_region.md): Resolve region names to region IDs for a selected search engine.
- [get_serp](get_serp.md): Retrieve search results for one keyword from Google or live Yandex search.
- [get_position](get_position.md): Retrieve a domain's search ranking for several comma-separated keyword phrases in one request.
- [get_keywords_by_url](get_keywords_by_url.md): Retrieve keywords associated with a page URL.

## Crawler audits

- [get_crawler_analysis_summary](get_crawler_analysis_summary.md): Retrieve the latest crawler-audit summary, health score, issue counts and optional history.
- [get_crawler_pages](get_crawler_pages.md): List audited website pages with full page checks and combined issue filters.
- [get_changed_crawler_pages](get_changed_crawler_pages.md): Find audited pages whose selected tracked field changed during a date range.

## Search Console and Webmaster

- [get_keywords_pages_summary](get_keywords_pages_summary.md): Retrieve keyword and page search-performance summaries from Google Search Console and Yandex Webmaster.
- [get_pages_summary](get_pages_summary.md): Retrieve page search-performance summaries from Google Search Console and Yandex Webmaster.
- [get_pages_summary_by_dates](get_pages_summary_by_dates.md): Retrieve historical clicks, impressions and positions grouped by day, week or month.

## Yandex Metrika

- [get_metrika_visits](get_metrika_visits.md): Retrieve visit data from the project's connected Yandex Metrika counter.
- [get_metrika_goals](get_metrika_goals.md): List goals from the project's connected Yandex Metrika counter.
- [get_metrika_sources_summary](get_metrika_sources_summary.md): Retrieve a Yandex Metrika traffic-source summary.
- [get_metrika_search_engines_data](get_metrika_search_engines_data.md): Retrieve search-engine sessions and users from Yandex Metrika with optional visitor filters.
- [get_metrika_page_depth_analysis](get_metrika_page_depth_analysis.md): Retrieve sessions with more than the selected number of page views from Yandex Metrika.
- [get_metrika_goals_conversion](get_metrika_goals_conversion.md): Retrieve user counts and conversion rates for selected Yandex Metrika goals.
- [get_metrika_mobile_vs_desktop](get_metrika_mobile_vs_desktop.md): Compare mobile and desktop traffic and engagement in Yandex Metrika.
- [get_metrika_geographical_organic_traffic](get_metrika_geographical_organic_traffic.md): Retrieve the geographical distribution of organic traffic in Yandex Metrika.
- [get_metrika_data_by_time](get_metrika_data_by_time.md): Retrieve Yandex Metrika metrics grouped by a time interval.
- [get_metrika_conversion_rate_by_source_and_landing](get_metrika_conversion_rate_by_source_and_landing.md): Retrieve conversion rates by traffic source and landing page for a Yandex Metrika goal.
- [get_metrika_pages_report](get_metrika_pages_report.md): Retrieve a Yandex Metrika page report with selected metrics, dimensions and filters.
- [get_metrika_custom_query](get_metrika_custom_query.md): Run a custom query against the connected Yandex Metrika reporting API using metrics, dimensions and filters.

## Page content and images

- [get_page_content](get_page_content.md): Extract a public page as Markdown, HTML, or a compact metadata-and-headings structure.
- [get_page_screenshot](get_page_screenshot.md): Capture a public-page screenshot using a selected device type.
- [generate_image](generate_image.md): Generate an image from a text prompt, optionally using reference-image URLs.

## Project events and notes

- [get_project_events](get_project_events.md): Retrieve project timeline events for indexing, SSL, robots.txt, analytics and crawler-audit changes.
- [get_project_notes](get_project_notes.md): Retrieve user-created project notes for an inclusive date range.
- [create_project_note](create_project_note.md): Create a dated project note documenting work on a website.
- [update_project_note](update_project_note.md): Update selected fields of a project note and return the updated note.

## Articles

- [list_articles](list_articles.md): List the articles available to the connected user.
- [create_article](create_article.md): Create an article with a name and optional initial blocks.
- [get_article](get_article.md): Retrieve an article and, optionally, its block data.
- [get_article_blocks](get_article_blocks.md): Retrieve article blocks matching substring and block-type filters, with optional neighboring context.
- [count_article_blocks](count_article_blocks.md): Count article blocks matching substring and block-type filters without returning the blocks.
- [delete_article](delete_article.md): Delete an article identified by its article ID.
- [set_article_content](set_article_content.md): Replace an article body and remove its existing blocks.
- [modify_article_blocks](modify_article_blocks.md): Apply ordered insert, modify, remove and move operations to article blocks.
- [replace_article_text](replace_article_text.md): Find and replace text in article block data.text, data.code and data.caption fields.
- [update_article_title](update_article_title.md): Change the name of an article.

## HTML artifacts

- [create_artifact](create_artifact.md): Create an HTML artifact and its initial draft.
- [list_artifacts](list_artifacts.md): List HTML artifacts available to the connected user.
- [read_artifact](read_artifact.md): Read the active artifact draft or a specified revision.
- [search_artifact](search_artifact.md): Find text in an artifact revision and return match positions and a match count.
- [overwrite_artifact](overwrite_artifact.md): Replace the content of the active artifact draft using its current revision ID.
- [replace_range_in_artifact](replace_range_in_artifact.md): Replace a range of characters in an artifact draft using its current revision ID.
- [replace_substring_in_artifact](replace_substring_in_artifact.md): Replace matching text in an artifact draft using its current revision ID.
- [finalize_artifact](finalize_artifact.md): Finalize the active artifact draft as the next version.
- [list_artifact_revisions](list_artifact_revisions.md): List revisions of an artifact.
- [diff_artifact](diff_artifact.md): Compare two artifact revisions using a unified diff.
- [revert_artifact](revert_artifact.md): Restore the active artifact draft from a selected revision.
- [validate_artifact](validate_artifact.md): Validate the active artifact revision and report errors.
- [set_artifact_persistent](set_artifact_persistent.md): Enable or disable persistent storage for a finalized artifact version.

# PR-CY MCP

English documentation for the hosted PR-CY Model Context Protocol server. PR-CY gives AI agents access to keyword rankings, search results, keyword demand, website audits, Google Search Console, Yandex Webmaster, Yandex Metrika, page content, articles, and HTML artifacts.

The server is available at `https://mcp-server.pr-cy.ru` and authenticates requests with a PR-CY API key in the `Authorization: Bearer <key>` header.

This repository contains documentation and public interface schemas. It does not contain the server implementation or user account data. The reference was checked against the live server's `tools/list` response on **2026-10-27**: server `analysis`, version `1.30.0`, **69 tools**.

## Start here

- [Connect and authenticate](docs/quickstart.md)
- [Browse all 69 tools](docs/tools/index.md)
- [Keyword research, search and rankings](docs/workflows.md#keyword-research-and-search-results)
- [Website audits and changes](docs/workflows.md#website-audits)
- [Search traffic and Yandex Metrika](docs/workflows.md#traffic-and-conversion-reports)
- [Articles and HTML artifacts](docs/workflows.md#articles-and-html-artifacts)
- [Limits, errors and pagination](docs/limits-and-errors.md)
- [Protocol and response formats](docs/protocol.md)
- [Sources and update procedure](docs/sources.md)

## Connect in Codex

Make your PR-CY API key available as the `PR_CY_API_KEY` environment variable to the process running Codex. Add this server entry to your Codex `config.toml`:

```toml
[mcp_servers.pr-cy]
url = "https://mcp-server.pr-cy.ru"
bearer_token_env_var = "PR_CY_API_KEY"
```

Restart or reconnect the client after configuration changes. Ask the agent to discover the available tools, then try a task such as:

```text
Use PR-CY MCP to fetch the headings and metadata of https://example.com/.
```

For a small response, the agent can call `get_page_content` with these arguments:

```json
{
  "page_url": "https://example.com/",
  "format": "structure"
}
```

Tool argument examples use demonstration domains and IDs. Replace them with the domain and identifiers relevant to your task.

## Access requirements

An API key is needed for every connection. Public-page extraction, search results, keyword demand and one-off ranking lookups do not require a PR-CY project. Project rankings, project crawler audits and connected analytics require a project with the relevant feature and data connection. Available operations consume the limits of the user's PR-CY plan where applicable.

The current `get_serp` interface supports `google` and `yandexLive`. Its `language` parameter is fixed to `ru`. English documentation does not imply support for other search-interface languages.

## Context7

The documentation is available in [Context7](https://context7.com/costeels/pr-cy-mcp-docs), with library ID `/costeels/pr-cy-mcp-docs`. The root `context7.json` selects the English documentation.

Context7 retrieves these instructions and examples. A separate PR-CY MCP connection executes the tools. For a single-file documentation source, publish the included `llms-full.txt` and submit its public URL using Context7's llms.txt source option or API.

## Product links

- [PR-CY MCP product page](https://pr-cy.ru/pages/mcp/)
- [PR-CY connection help](https://pr-cy.ru/help/article/mcp-server-connect/)
- [Model Context Protocol](https://modelcontextprotocol.io/)

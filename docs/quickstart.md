# Connect to PR-CY MCP

PR-CY runs a hosted MCP server at `https://mcp-server.pr-cy.ru`. An MCP client discovers its tools and calls them on behalf of the connected user. No local PR-CY server or source-code checkout is required.

## Obtain an API key

Get a PR-CY API key from the API settings in your PR-CY account, using the link on the [MCP product page](https://pr-cy.ru/pages/mcp/). The server expects:

```http
Authorization: Bearer YOUR_PR_CY_API_KEY
```

`YOUR_PR_CY_API_KEY` is a placeholder. Keep a real key in your client or secret manager; do not commit it to a repository, put it in a public example, or send it to Context7.

## Codex

Provide `PR_CY_API_KEY` in the environment of the process running Codex. Add the following entry to the user's `config.toml`:

```toml
[mcp_servers.pr-cy]
url = "https://mcp-server.pr-cy.ru"
bearer_token_env_var = "PR_CY_API_KEY"
```

Reconnect the MCP server or restart the client so the configuration and environment are reloaded. See [Codex MCP documentation](https://developers.openai.com/codex/mcp/) for the current configuration options.

## Clients using mcpServers JSON

For clients that accept remote HTTP servers under `mcpServers`, use this connection shape and configure the API key through the client's supported secret or environment mechanism:

```json
{
  "mcpServers": {
    "pr-cy": {
      "url": "https://mcp-server.pr-cy.ru",
      "headers": {
        "Authorization": "Bearer YOUR_PR_CY_API_KEY"
      }
    }
  }
}
```

This is a remote-server configuration shape, not a universal configuration file. Clients differ in file locations, environment-variable interpolation and HTTP transport support. The PR-CY [product page](https://pr-cy.ru/pages/mcp/#connect) provides client-specific instructions for Cursor, Claude, OpenCode and other clients.

## Verify the connection

Have the client initialize the MCP connection and discover tools. On 2026-10-27, the server identified itself as `analysis` version `1.30.0` and advertised 69 tools. Use the tools discovered by your own connection if the server has changed.

Start with a public-page request:

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

The example is a message handled by an initialized MCP client. For direct HTTP integrations, complete the initialization and transport steps in [Protocol](protocol.md) first. This page does not show a live extraction result.

## Discover a project

For project reports, call `get_user_project_by_domain` with a domain such as `example.com` or list projects with `get_user_projects`. Use the returned `project_id` in subsequent reports. Retrieve search-option IDs with `get_user_keywords_projects` and goal IDs with `get_metrika_goals` when the task needs them.

```json
{
  "domain": "example.com"
}
```

Never substitute a keyword-group ID, search-option ID or Metrika goal ID for a project ID. Some tools accept a domain instead of a project ID; consult each tool's reference.

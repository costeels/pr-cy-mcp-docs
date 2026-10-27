# Protocol and response formats

PR-CY exposes a hosted MCP endpoint at `https://mcp-server.pr-cy.ru`. Requests authenticate with a PR-CY API key in the `Authorization: Bearer <key>` header. MCP protocol messages use JSON-RPC 2.0.

## Initialization and discovery

Use a compatible MCP client to handle HTTP transport, initialization, protocol negotiation and any session headers. During discovery on 2026-10-27, the server accepted protocol version `2025-06-18` and returned this server identity:

```json
{
  "name": "analysis",
  "version": "1.30.0"
}
```

An initialization request has the following shape:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2025-06-18",
    "capabilities": {},
    "clientInfo": {
      "name": "example-client",
      "version": "1.0.0"
    }
  }
}
```

Use the protocol version negotiated by the server. Send `notifications/initialized`, retain `Mcp-Session-Id` if returned, and use the negotiated `MCP-Protocol-Version` header as required by the transport. HTTP clients should support JSON and event-stream responses through the MCP transport rather than assuming every response body is a plain JSON object.

Discover tool definitions with `tools/list`; follow `nextCursor` when it is present:

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/list",
  "params": {}
}
```

The response advertises tool names, descriptions, input schemas and output schemas. The hosted server is the source of truth. Client-side wrappers can expose a different parameter subset; use the schema available in the actual connection through which a call will run.

## Calling a tool

Use the exact discovered tool name under `params.name`. Input fields belong under `params.arguments`, with the types and enum values declared by that tool's input schema.

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tools/call",
  "params": {
    "name": "get_user_project_by_domain",
    "arguments": {
      "domain": "example.com"
    }
  }
}
```

Do not turn MCP tool names into invented REST routes such as `/get_user_project`. MCP calls use the protocol endpoint.

## Interpreting a result

Separate a JSON-RPC protocol error from a tool result. MCP tool results can contain text, structured content and an error flag. When structured content is available, interpret it using the tool's advertised `outputSchema`. Otherwise, inspect the returned content without assuming an undocumented response shape.

The `schemas/` directory contains the input and output schemas observed for each tool, with descriptive annotations omitted to keep the schema files language-neutral. The English reference explains behavioral constraints that are not fully represented by JSON Schema.

Responses from reports may retain upstream field names, including camelCase fields. Events use the language of the PR-CY account. English documentation does not change the language of account data or search results.

## Interface differences

The live `get_wordstat` schema checked for this repository does not include an `engine` input. `get_serp` supports only `google` and `yandexLive`, while `get_region` additionally supports `yandex`. `get_page_screenshot.device_type` uses `smartphone`, `tablet` and `desktop`; `get_serp.device` uses `desktop` and `mobile`.

Use current discovery instead of adapting a similarly named parameter from another tool.

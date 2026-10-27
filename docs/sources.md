# Sources and updates

## Reference provenance

This repository's English documentation was prepared from public PR-CY product instructions and an authenticated MCP metadata discovery. Metadata discovery does not read project reports, articles or account data.

- Product and connection information: [PR-CY MCP](https://pr-cy.ru/pages/mcp/) and [connection help](https://pr-cy.ru/help/article/mcp-server-connect/).
- Tools, field names, required inputs, enums, schema defaults and output types: the live `tools/list` response from `https://mcp-server.pr-cy.ru`, captured on 2026-10-27.
- Server identity: `analysis`, version `1.30.0`; negotiated MCP protocol version `2025-06-18`; 69 advertised tools.
- Codex setup: [official MCP documentation](https://developers.openai.com/codex/mcp/).
- Context7 submission: [Adding Libraries](https://context7.com/docs/adding-libraries) and [Library Owners](https://context7.com/docs/library-owners).

The product page advertised 48 tools at the time it was checked. The reference follows the 69 tools from live metadata discovery. The checked tool schemas can also differ from a preconfigured agent's wrapper interface. The reference describes the hosted server's observed interface, not a promise that every wrapper exposes all fields.

## What was verified

Input schemas, output schemas and all tool example argument objects were validated locally against the captured schemas. Internal documentation links, Context7 configuration and the public package were checked for consistency and secret leakage.

Example domains, project IDs, goal IDs, article IDs and revision IDs are demonstration values. Examples were not executed against real projects, and illustrative content objects were not tested for application-level editing behavior. A schema-valid input can still require valid permissions, account limits, data connections or stricter service-level validation.

## Updating the reference

1. Initialize an authenticated PR-CY MCP connection and retrieve every page of `tools/list`.
2. Compare the advertised tool names, input schemas, output schemas and behavioral descriptions with this reference.
3. Update the English tool pages and language-neutral schemas together. Preserve documented service-level constraints that JSON Schema does not encode.
4. Validate examples, links and `context7.json`. Update the checked date and server identity.
5. Rebuild `llms-full.txt` from the English documentation.
6. Push documentation changes to the public repository and refresh its actual Context7 library ID.

Context7 parses documentation files and extracts explanations and code examples. Its current public-library guidance says mainly non-English documentation is skipped. This repository's indexed pages are English.

## Publishing and ownership

The files can be published in a public repository without publishing PR-CY server source code or account data. Creating the repository, submitting it to Context7 and claiming library ownership are separate actions. Ownership verification requires the repository maintainer's Context7 account and the claim instructions generated for that account; this package does not fabricate an ownership key or a library ID.

After publication, submit the repository at [Add Library](https://context7.com/add-library). Use the actual library ID returned by Context7 and wait for parsing to finish before claiming successful availability. Test retrieval with questions about connection, keyword demand, crawler pagination, project note dates and artifact revisions.

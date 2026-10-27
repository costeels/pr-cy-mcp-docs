# get_user_limits

Retrieve selected limits for the connected PR-CY account or project.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

limits_filter must be non-empty. competitorsAnalysis requires project_id. The captured schema default includes that project-specific limit, so use an explicit project-independent filter for account checks.

## Arguments

- `limits_filter`: optional; array of "checks" | "competitorsAnalysis" | "forceCrawlerUpdates" | "pdfReports" | "projects" | "projectsDaily" | "standardAnalysis" | "teams". Schema default: `["checks", "competitorsAnalysis", "forceCrawlerUpdates", "pdfReports", "projects", "projectsDaily", "standardAnalysis", "teams"]`. Non-empty list of limit names; competitorsAnalysis needs a project.
- `project_id`: optional; integer or null. Schema default: `null`. greater than: 0. Project ID from project discovery.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_user_limits",
    "arguments": {
      "limits_filter": [
        "checks",
        "standardAnalysis"
      ]
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `result`: array of object; required in the output schema.

The complete input and output schemas are in [get_user_limits.json](../../schemas/get_user_limits.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

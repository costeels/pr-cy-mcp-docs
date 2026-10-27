# get_metrika_visits

Retrieve visit data from the project's connected Yandex Metrika counter.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

This report requires a project with a connected Yandex Metrika counter. Most report tools use the last seven days when dates are omitted; goal listing does not take report dates.

## Arguments

- `project_id`: required; integer. greater than: 0. Project ID from project discovery.
- `date_from`: optional; string or null. Schema default: `null`. Start of the requested reporting or change period.
- `date_to`: optional; string or null. Schema default: `null`. End of the requested period; inclusivity depends on the tool.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_metrika_visits",
    "arguments": {
      "project_id": 123,
      "date_from": "2026-10-01",
      "date_to": "2026-10-20"
    }
  }
}
```

## Result

Interpret the returned tool content and structured data according to the current advertised output schema.

The complete input and output schemas are in [get_metrika_visits.json](../../schemas/get_metrika_visits.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

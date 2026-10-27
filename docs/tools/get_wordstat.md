# get_wordstat

Retrieve estimated monthly keyword demand, related phrases, including phrases and optional seasonality across regions and accuracy types.

Operation: retrieves or inspects data.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

Batch phrases in one comma-separated keywords string. Up to five regions and several types can be requested. general is broad demand; quoted fixes phrase word count while allowing word forms; exact keeps word forms without fixing word order. A null region item means unrestricted geography; the captured omitted-region default is Russia. Prefer types and regions over legacy type and region. Seasonality needs start and end and supports up to 24 months. No engine parameter is advertised in this captured live schema.

## Arguments

- `keywords`: required; string. Comma-separated keyword phrases.
- `types`: optional; array of "general" | "quoted" | "exact" or null. Schema default: `null`. Keyword-demand accuracy types.
- `regions`: optional; array of integer or null or null. Schema default: `null`. Keyword-demand region IDs; a null item means unrestricted geography.
- `need_related_phrases`: optional; boolean. Schema default: `true`. Include related keyword phrases.
- `need_including_phrases`: optional; boolean. Schema default: `true`. Include phrases containing the requested keyword.
- `seasonality`: optional; object or null. Schema default: `null`. Optional keyword-demand history request with start and end months.
- `type`: optional; "general" | "quoted" | "exact" or null. Schema default: `null`. Legacy single accuracy type; prefer types.
- `region`: optional; integer or null. Schema default: `null`. Legacy single region ID; prefer regions.

### WordstatSeasonalityRequest

- `start`: required; string. Starting character offset for an artifact range, or seasonality start month.
- `end`: required; string. Seasonality end month.
- `device`: optional; "desktop" | "mobile" or null. Schema default: `null`. Device category supported by this tool.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_wordstat",
    "arguments": {
      "keywords": "buy laptop, gaming laptop",
      "types": [
        "general",
        "exact"
      ],
      "regions": [
        213
      ],
      "need_related_phrases": true
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `task_id`: string; required in the output schema.
- `regions`: array of object; required in the output schema.
- `types`: array of string; required in the output schema.
- `items`: array of object; required in the output schema.
- `seasonality`: array of object or null; optional in the output schema.
- `seasonality_months`: array of string or null; optional in the output schema.
- `seasonality_device`: string or null; optional in the output schema.

The complete input and output schemas are in [get_wordstat.json](../../schemas/get_wordstat.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

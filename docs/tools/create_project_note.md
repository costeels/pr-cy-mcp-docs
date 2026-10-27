# create_project_note

Create a dated project note documenting work on a website.

Operation: changes data, launches work or generates content.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

Use plain text without emoji. Creation is not deduplicated; inspect notes after an uncertain response before retrying the call.

## Arguments

- `project_id`: required; integer. greater than: 0. Project ID from project discovery.
- `name`: required; string. minimum text length: 1; maximum text length: 200. Name of the article, keyword group or project note.
- `note_date`: required; string. Calendar date of the project note.
- `text`: optional; string or null. Schema default: `null`. maximum text length: 20000. Project note text.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "create_project_note",
    "arguments": {
      "project_id": 123,
      "name": "Updated category titles",
      "note_date": "2026-10-20",
      "text": "Updated title tags on laptop category pages."
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `id`: integer; required in the output schema.
- `name`: string; required in the output schema.
- `text`: string; required in the output schema.
- `date`: string; required in the output schema.

The complete input and output schemas are in [create_project_note.json](../../schemas/create_project_note.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

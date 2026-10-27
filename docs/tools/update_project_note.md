# update_project_note

Update selected fields of a project note and return the updated note.

Operation: changes data, launches work or generates content.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

Provide at least one of name, note_date or text. Omitted or null fields remain unchanged; empty text clears text. Only the note author or project owner can edit, even when other users have team read access. Use plain text without emoji. project_id is needed because the tool rereads project notes after updating.

## Arguments

- `note_id`: required; integer. greater than: 0. ID of the project note to update.
- `project_id`: required; integer. greater than: 0. Project ID from project discovery.
- `name`: optional; string or null. Schema default: `null`. minimum text length: 1; maximum text length: 200. Name of the article, keyword group or project note.
- `note_date`: optional; string or null. Schema default: `null`. Calendar date of the project note.
- `text`: optional; string or null. Schema default: `null`. maximum text length: 20000. Project note text.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "update_project_note",
    "arguments": {
      "note_id": 456,
      "project_id": 123,
      "text": "Updated title tags and checked the affected URLs."
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

The complete input and output schemas are in [update_project_note.json](../../schemas/update_project_note.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

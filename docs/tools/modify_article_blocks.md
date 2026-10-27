# modify_article_blocks

Apply ordered insert, modify, remove and move operations to article blocks.

Operation: changes data, launches work or generates content.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

Operations run in order and address blocks by stable IDs. afterBlockId=null inserts or moves to the beginning. Otherwise, the affected block goes immediately after the selected block. Use at most 100 operations and 50 blocks per insert. The id inside a replacement block is overridden by blockId.

## Arguments

- `article_id`: required; string. minimum text length: 1. Article ID returned by article creation or listing.
- `operations`: required; array of object. minimum items: 1. Ordered article-block edit operations.

### InsertBlockOperation

- `action`: optional; "insert". Schema default: `"insert"`. Article-block operation discriminator.
- `afterBlockId`: optional; string or null. Schema default: `null`. Insert or move immediately after this block; null means the beginning.
- `blocks`: required; array of object. minimum items: 1. Content blocks to insert.

### ModifyBlockOperation

- `action`: optional; "modify". Schema default: `"modify"`. Article-block operation discriminator.
- `blockId`: required; string. minimum text length: 1. Stable ID of the block to modify or move.
- `block`: required; object. Replacement content for a block.

### MoveBlockOperation

- `action`: optional; "move". Schema default: `"move"`. Article-block operation discriminator.
- `blockId`: required; string. minimum text length: 1. Stable ID of the block to modify or move.
- `afterBlockId`: optional; string or null. Schema default: `null`. Insert or move immediately after this block; null means the beginning.

### RemoveBlockOperation

- `action`: optional; "remove". Schema default: `"remove"`. Article-block operation discriminator.
- `blockIds`: required; array of string. minimum items: 1. Stable IDs of blocks to remove.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "modify_article_blocks",
    "arguments": {
      "article_id": "ARTICLE_ID",
      "operations": [
        {
          "action": "insert",
          "afterBlockId": null,
          "blocks": [
            {
              "type": "paragraph",
              "data": {
                "text": "A laptop buying guide."
              }
            }
          ]
        }
      ]
    }
  }
}
```

## Result

Interpret the returned tool content and structured data according to the current advertised output schema.

The complete input and output schemas are in [modify_article_blocks.json](../../schemas/modify_article_blocks.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

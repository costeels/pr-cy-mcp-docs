# generate_image

Generate an image from a text prompt, optionally using reference-image URLs.

Operation: changes data, launches work or generates content.

Reference checked against PR-CY MCP server version 1.30.0 on 2026-10-27.

## Behavior

This generates an image and can consume account limits. The captured interface accepts up to 10 reference-image URLs. Model availability may change; prefer current tool discovery over a hardcoded model list.

## Arguments

- `prompt`: required; string. Text description of the image to generate.
- `aspect_ratio`: optional; "1:1" | "9:16" | "16:9" | "3:4" | "4:3" | "2:3" | "3:2" | "4:5" | "5:4" | "21:9". Schema default: `"1:1"`. Generated-image aspect ratio.
- `model`: optional; "auto" | "gpt-image-2.5-flare" | "nano-banana-2.1" | "nano-banana-2" | "nano-banana-2-lite" | "nano-banana-pro" | "seedream/v4.5" | "flux-2" | "flux-3" | "recraft-v4" | "ideogram" | "schnell". Schema default: `"auto"`. Image-generation model selected from the current enum.
- `reference_images`: optional; array of string or null. Schema default: `null`. maximum items: 10. Reference-image URLs; at most 10 in the captured interface.

## Example call

This is an illustrative JSON-RPC message for an initialized MCP client. Replace demonstration IDs and domains with values from your own connection. The example was validated against the advertised input schema and was not executed against a project.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "generate_image",
    "arguments": {
      "prompt": "A clean editorial illustration of a laptop on a desk.",
      "aspect_ratio": "16:9",
      "model": "auto"
    }
  }
}
```

## Result

The advertised structured output has these top-level fields:

- `task_id`: string; required in the output schema.
- `image_url`: string; required in the output schema.
- `error_code`: string or null; optional in the output schema.

The complete input and output schemas are in [generate_image.json](../../schemas/generate_image.json). Behavioral checks, permissions and upstream data availability can impose additional requirements.

See [Protocol](../protocol.md), [Limits and errors](../limits-and-errors.md), and the [tool index](index.md).

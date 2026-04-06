---
name: gemini-image-gen
description: Generate blog artwork with Gemini native image models (nano banana line, e.g. gemini-3.1-flash-image-preview, gemini-3-pro-image-preview) via generateContent, including reference-driven edits. Use when the user wants AI-generated images, hero art, or image-to-image iterations for a post; includes the repo CLI gemini-image-gen.
---

# Gemini image generation (blog repo)

Google docs label these **Gemini image** / **nano banana** models (image in, image+text out through `generateContent`).

## Docs (official)

- [Image generation (Gemini native)](https://ai.google.dev/gemini-api/docs/image-generation) – `generateContent` with image-capable Gemini models; text-only or text + reference images.
- [Pricing](https://ai.google.dev/gemini-api/docs/pricing) – Gemini image models: image output priced per token (tiers differ by model, e.g. 3 Pro Image vs 3.1 Flash Image Preview vs 2.5 Flash Image).

## Default model

**`gemini-3.1-flash-image-preview`** – chosen as the **second tier** on the published image-output rate card vs **`gemini-3-pro-image-preview`** (higher) and **`gemini-2.5-flash-image`** (lower). Override with `-m` when you want Pro quality or a cheaper Flash variant.

## Where to write files

The repo gitignores `IGNORED/`. Prefer:

- Active blog post: `IGNORED/<post-slug>/` (match the markdown basename under `docs/blog/posts/`, e.g. `IGNORED/the-shifting-sands-of-AI-product-development/`).
- No specific post: `IGNORED/images/`.

Each invocation saves into a **named subdirectory** under the base output dir. Always supply `-s` with a short, human-readable topic name – e.g. `-s "2025-agent-for-loop"` or `-s "hero-march-of-progress"`. This keeps runs organised by meaning, not by image specs. If `-s` is omitted, the CLI falls back to a slug from the first few words of the prompt (which is usually ugly).

Images are numbered sequentially (`image-01`, `image-02`, …) and **never overwrite** existing files – re-running into the same subdir continues from the next available number.

## CLI

Path: `.agents/skills/gemini-image-gen/gemini-image-gen`

```bash
export GEMINI_API_KEY=...   # required

# Text-to-image
./.agents/skills/gemini-image-gen/gemini-image-gen \
  -d IGNORED/my-post-slug \
  -s "hero-march-of-progress" \
  "wide 16:9 hero, no text"
# → saves to IGNORED/my-post-slug/hero-march-of-progress/image-01.jpg

# Single reference image
./.agents/skills/gemini-image-gen/gemini-image-gen \
  -d IGNORED/my-post-slug \
  -s "2023-eyes-and-hands" \
  -i docs/blog/posts/assets/my-post-slug/hero.jpg \
  "robotic figure with glowing eyes and tool-wielding hands"

# Multiple reference images, Pro model, 5 candidates
./.agents/skills/gemini-image-gen/gemini-image-gen \
  -m gemini-3-pro-image-preview \
  -n 5 \
  -d IGNORED/my-post-slug \
  -s "2025-agent-for-loop" \
  -i path/to/style-ref.jpg \
  -i path/to/content-ref.jpg \
  "blend style of image 1 with composition of image 2"
```

Flags:

| Flag | Meaning |
|------|--------|
| `prompt` (positional) | What to generate or how to change the reference image(s) |
| `-d`, `--output-dir` | Base output directory (required) |
| `-s`, `--subdir` | **Subdirectory name – always set this to a short meaningful topic name** |
| `-n`, `--num-images` | Candidates to produce (default **3**) |
| `-m`, `--model` | Gemini image model id (default **gemini-3.1-flash-image-preview**) |
| `-i`, `--reference-image` | Reference image file; **repeat** for multiple references |

**Dependencies:** `google-genai` and `Pillow` are listed in `pyproject.toml`; from repo root run `uv sync` (or `pip install -e .`).

## Agent behavior

- Pick output dir from the user's current post slug when obvious; otherwise `IGNORED/images/`.
- **Always use `-s` with a short meaningful topic name** that describes the image concept, not the technical specs. Good: `2024-train-on-rails`. Bad: `photorealistic-wide-169-image-of-a`.
- Prefer the default Flash Image Preview model unless the user asks for Pro or 2.5 Flash Image.
- Default to **3 candidates** per run unless the user specifies otherwise.
- After generation, point the user at saved paths under `IGNORED/`; do not commit generated binaries unless they ask.
- When iterating, pass the prior result as `-i` so the model uses it as a visual anchor.
- Multiple `-i` flags are supported; describe which reference does what in the prompt (e.g. "use image 1 for style, image 2 for composition").

## Running in the background (required)

Image generation takes 30–120 s. **Always run the CLI via a shell subagent** so it does not block the main agent turn:

```
Task tool → subagent_type="shell", run_in_background=false
prompt: "cd /path/to/repo && export GEMINI_API_KEY=... && ./.agents/skills/gemini-image-gen/gemini-image-gen ..."
```

The shell subagent blocks internally while the CLI runs, then returns the saved paths. Alternatively, use the Shell tool with `block_until_ms` set high enough for the expected runtime (e.g. `block_until_ms: 120000` for Pro model, 3 candidates) – or set `block_until_ms: 0` to background immediately and poll with the `Await` tool until the terminal file shows an `exit_code` line.

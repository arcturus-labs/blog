# 06 – Reference-led graphics and image generation

## One concrete journey, not a different metaphor per slide

Choose an example that can evolve through the page. Agentic Web uses home search with Google, the ChatGPT desktop app and **Willow**, a fictional property platform. Porchlight was an earlier name, not the current identity. Other pages need their own appropriate examples.

Ask what each picture must communicate at a glance. Familiar product scenes were more effective than elaborate lost-context diagrams. The eventual contrast was a muted, ignored property page behind a prominent conversation versus coordinated overlapping app windows. An early jagged diagonal/parallax concept was superseded; don't preserve old art direction just because it is detailed.

## References, branding and privacy

- Inspect supplied screenshots. Record exact composition, important words, app identity, active state and what matters versus what can be shrunk.
- Preserve originals when requested; maintain descriptive filenames and an original-to-local manifest. Private sources are **not** public assets.
- Before sending inputs externally, remove unnecessary names, avatars, account/project history, extensions, model/permission labels, IDs, tracking URLs and personal location clues. Check final renders as well. Synthetic generic avatars are preferable to transferring the owner's identity.
- Distinguish a native desktop app from a browser. ChatGPT's app frame uses a slim title bar/icon rail, not address bars/tabs. A reference labeled Codex is a layout sample, not permission to retain Codex branding or “Full access”. Google and the property website can still have browser chrome.
- Generate an approved **brand sheet** once: wordmark, symbol, light/dark versions, favicon, app/integration badges. Pass the **whole sheet** as a reference into later edits; cropping out every logo first is unnecessary unless requested.
- Fictionalize all competitor identifiers consistently: logo, tab title, favicon, URLs, citation badges, integration name and listing cards. Use `*.example` for illustrative destinations. A later story beat may intentionally omit platform URLs/names while retaining blue property links; preserve that narrative choice.
- Light-mode UI stood out against this dark/starry site better than black-on-black. Contrast must be reviewed on the actual page, not only on an image viewer's background.

Keep fictional scenario data coherent across questions, filters, prices, selections and responses. Do not claim a synthetic scene demonstrates a shipped integration, client result or causal outcome.

## Brief exact compositions and text

Use `homepage/research/website_copy/<page>-graphics.md` plus generation prompts to record:
- what this scene establishes;
- which reference supplies composition, branding or annotation style;
- exact query/clarification/response/link text;
- secondary UI to reduce so essential words remain legible;
- privacy exclusions and fictional details;
- continuity with earlier/later scenes;
- approved text that must remain unchanged during an image-only revision.

Do not uniformly shrink a dense screenshot. A short, meaningful dialogue is better than a tiny table. Inspect images at the **actual story-panel width**, not just at 1536px. Don't rely on “View larger” links to rescue illegible artwork; the owner removed them.

## Current-model selection and generation-first workflow

Read the installed generation skill and check current official model documentation when freshness is uncertain. Distinguish latest documentation, best task fit, account access and observed output quality.

This project **actually used `gpt-image-2.5-sunburst` successfully** for the brand sheet and multiple reference-edit rounds. Its precision was useful; that is a tested project fact, not a permanent assertion that it is the best/newest model. Recheck when appropriate.

John prefers direct generation/editing with screenshots and descriptive prompts. **Do not default to meticulously recreating fake HTML websites or an elaborate text-overlay pipeline before trying the image model.** Only discuss a targeted fallback if repeated attempts fail.

Once authorized and the concepts are agreed:
1. Supply the previous approved render plus branding/style/reference images, with their roles explicit.
2. State exact changes and what must remain untouched. For small tweaks, edit the existing scene rather than regenerate unrelated compositions.
3. Bound counts/cost. Independent scenes can run in parallel. Dependent work cannot: generate a common style sheet first, inspect it, then use it in parallel scene edits.
4. Retain prompts, model/settings, original renders and selected-version metadata. Save new candidates, never overwrite the original.
5. Wait for a generation/export to complete before reading its output. A read launched in parallel with its file writer can race and fail.

## Consistent editorial annotations

When several scenes need handwritten commentary, generate a **style sample first**: large clear red hand-lettering, curved arrows, circling line and underline. Reuse that image as an input across the scenes, along with each original scene and precise instructions. The sample controls annotation style, not app typography.

Editorial notes should clearly float above the screenshot, not look like app buttons. A slight diagonal and clean hand-drawn stroke can draw attention to a clipped website result without adding more body copy. Keep lettering readable and larger than secondary UI; don't cover the essential query, link or selection.

Review arrows semantically, not just aesthetically:
- one arrowhead, plain tail where intended;
- tail at the **assistant's** matching-homes message, not the user's request;
- head into the page **generally** when the claim is “updates the page”, not accidentally at a specific property;
- reverse arrow from the selected listing to the assistant's selection message;
- labels unchanged during an arrow-only touch-up.

The final selected shared-experience render is `willow-scenes-v4/solution-3-shared-experience/image-03.png`. Earlier `image-01` had two heads; `image-02` still pointed at a property. Keep such selections explicit so integration does not accidentally reuse a rejected variant.

## Transparency and web export

- Preserve original renders. For removability, use a perfectly flat chroma-key exterior, then export a **separate true-alpha** result. A generated checkerboard is not transparency.
- Remove the exterior, not opaque app interiors, pale map greens, foliage, white windows or lettering.
- Border-connected keying protects interior colors, but red circles can enclose small greenscreen islands. Remove those with a strict near-pure-key-color test; don't delete all “green-ish” components globally.
- Inspect edge spill/halos and gaps over the site's real dark background.
- Trim transparent padding without clipping projecting notes or arrows. Export optimized alpha WebP sizes (this site uses 960/1536 widths) with correct intrinsic dimensions and responsive sources. The raw PNG is not the shipping asset.

## Gate

Inspect spelling, privacy, correct app/brand, dialogue sense, arrow semantics, contrast and actual-size legibility. Select the intended render explicitly, then integrate and inspect again. Keep unreviewed/private references out of publication and generated binaries out of commits unless authorized. The image must communicate the story without being mistaken for empirical proof.

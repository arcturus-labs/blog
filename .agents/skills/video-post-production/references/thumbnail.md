# Thumbnail Composition

Thumbnails are composed using standard image manipulation (Pillow), not AI generation. This gives precise control over logo placement and text.

## Assets

- **Logo**: `docs/assets/images/logo_with_shadow.png` — icon-only, RGBA (transparent background). Use this for watermarking.
- **Base image**: Either an AI-generated scene (Gemini) or an existing post hero image.
- **Font**: Impact at `/System/Library/Fonts/Supplemental/Impact.ttf` — bold, condensed, all-caps. Standard YouTube thumbnail style.

## Steps

### 1. Start with a base image
Use the post's hero image or generate a scene with the Gemini CLI. Target 16:9 aspect ratio.

### 2. Add the logo watermark
- Resize logo to ~15% of image width.
- Place in the corner where the image is least cluttered — **ask John which corner** before placing.
- Composite using the PNG alpha channel (`.paste(logo, pos, logo)` in Pillow).

### 3. Choose thumbnail text
The thumbnail text should **not** repeat the video title — it should be a hook that creates curiosity or stakes. Two lines work well:
- Line 1: setup or subject ("YOUR SEARCH TEAM")
- Line 2: the punch or payoff ("JUST GOT REPLACED")

Read the post/transcript to understand the core tension, then draft 2–3 options for John to pick from.

### 4. Compose text
- **Line 1**: white Impact text with a dark drop shadow (offset 3px) for legibility over varied backgrounds.
- **Line 2**: dark Impact text on a solid-color highlight rectangle (yellow `#FFD200` / RGB 255,210,0 works well; match brand as needed).
- **The yellow box must fully contain line 2** - padding on all four sides. If the black letters hang below the yellow, the layout is wrong.
- Placement: bottom-left, with ~50px margin from the left edge and ~65px margin from the bottom **to the baseline of line 2**.

**Use the `anchor="lb"` pattern below** (left baseline). It is the canonical approach - validated on real thumbnails (e.g. `branded-02.jpg` for the video-editing post).

**Do not** size the yellow box from `textbbox((0, 0), ...)` height and then draw line 2 at `(x, y2)` with default anchoring. That was the `branded-01` bug: Impact metrics shift the glyphs and the black text sits below the yellow.

For line 2:
1. `y_bottom = image.height - bottom_margin`
2. `bbox2 = draw.textbbox((x, y_bottom), line2, font=font, anchor="lb")` - measure at the **same** x, y, and anchor you will draw with
3. `draw.rectangle([bbox2[0]-pad, bbox2[1]-pad, bbox2[2]+pad, bbox2[3]+pad], ...)`
4. `draw.text((x, y_bottom), line2, font=font, anchor="lb")`

Stack line 1 above line 2 with the same anchor: `y1_bottom = bbox2[1] - gap`, then shadow + white text at `(x, y1_bottom)` with `anchor="lb"`.

When John approves a version, **stop iterating** - use that file (e.g. `branded-02.jpg`) for upload. Do not keep generating `branded-03`, `branded-04`, … unless he asks for changes.

### 5. Save output
Save to `IGNORED/video-thumbnails/<episode-slug>/` with sequential naming (`branded-01.jpg`, `branded-02.jpg`, …). Never overwrite — iterate forward.

## Pillow pattern

```python
from PIL import Image, ImageDraw, ImageFont

base = Image.open("path/to/base.jpg").convert("RGBA")
logo = Image.open("docs/assets/images/logo_with_shadow.png")  # RGBA

# Logo
logo = logo.resize((int(base.width * 0.15), ...), Image.LANCZOS)
base.paste(logo, (x, y), logo)

# Text (anchor="lb" - canonical pattern; see branded-02.jpg)
font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Impact.ttf", 125)
draw = ImageDraw.Draw(base)
x, bottom_margin, pad, gap = 50, 65, 18, 12
y_bottom = base.height - bottom_margin

bbox2 = draw.textbbox((x, y_bottom), line2, font=font, anchor="lb")
draw.rectangle(
    [bbox2[0] - pad, bbox2[1] - pad, bbox2[2] + pad, bbox2[3] + pad],
    fill=(255, 210, 0, 255),
)
draw.text((x, y_bottom), line2, font=font, fill=(20, 20, 20, 255), anchor="lb")

y1_bottom = bbox2[1] - gap
draw.text((x + 3, y1_bottom + 3), line1, font=font, fill=(0, 0, 0, 180), anchor="lb")
draw.text((x, y1_bottom), line1, font=font, fill=(255, 255, 255, 255), anchor="lb")

base.convert("RGB").save("IGNORED/video-thumbnails/.../branded-01.jpg", quality=92)
```

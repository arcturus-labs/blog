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
- **Line 2**: dark Impact text on a solid-color highlight rectangle (yellow `#FFD2D00` works well; match brand as needed).
- Generous vertical padding on the highlight rect so the text sits fully inside it.
- Placement: bottom-left, with ~50px margin from the left edge and ~65px margin from the bottom.

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

# Text
font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Impact.ttf", 125)
draw = ImageDraw.Draw(base)
# highlight rect behind line 2
draw.rectangle([x - pad, y2 - pad, x + w2 + pad, y2 + h2 + pad], fill=(255, 210, 0, 255))
# line 1: shadow + white
draw.text((x + 3, y1 + 3), line1, font=font, fill=(0, 0, 0, 180))
draw.text((x, y1), line1, font=font, fill=(255, 255, 255, 255))
# line 2: dark on yellow
draw.text((x, y2), line2, font=font, fill=(20, 20, 20, 255))

base.convert("RGB").save("IGNORED/video-thumbnails/.../branded-01.jpg", quality=92)
```

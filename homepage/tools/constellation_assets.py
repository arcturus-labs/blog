"""Export black-backed luminous artwork as variable-alpha PNG and responsive WebP.

For these deliberately black-backed light illustrations, max(R,G,B) is opacity;
unpremultiplying retains the color and intensity on black without an opaque sky.
Do not use on opaque UI screenshots or ordinary photographs.
"""
from pathlib import Path
import numpy as np
from PIL import Image


def export(source: Path, assets: Path, prefix: str, transparent=False):
    from story_page import cached_scene
    size = cached_scene(assets, prefix)
    if size:
        return size
    if transparent:
        image = Image.open(source).convert('RGBA')
    else:
        rgb = np.asarray(Image.open(source).convert('RGB'), dtype=float) / 255
        alpha = rgb.max(axis=2)
        alpha[alpha < 8 / 255] = 0
        foreground = np.divide(rgb, alpha[..., None], out=np.zeros_like(rgb), where=alpha[..., None] > 0)
        image = Image.fromarray(np.uint8(np.clip(np.dstack((foreground, alpha)), 0, 1) * 255), 'RGBA')
        image.save(source.with_name('transparent.png'))
    image = image.crop(image.getbbox())
    assets.mkdir(parents=True, exist_ok=True)
    size = image.size
    for width in (960, 1536):
        dest = assets / f'{prefix}-{width}.webp'
        resized = image.copy()
        resized.thumbnail((width, 1400))
        # Rebuilding text should not re-encode a large illustration.
        import os
        if os.environ.get('HOMEPAGE_REBUILD_ASSETS') == '1' or not dest.exists() or dest.stat().st_mtime < source.stat().st_mtime:
            resized.save(dest, quality=92, method=4)
        if width == 1536:
            size = resized.size
    return size

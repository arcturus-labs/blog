#!/usr/bin/env python3
"""Build homepage sources, then publish into MkDocs docs/ (never deploy).

uv run --group homepage python scripts/build_homepage.py [home|agentic-web|workflows|software-factories ...]
Use --assets --scenes /path/to/supporting_images to regenerate responsive artwork.
Without --assets, committed WebPs are reused and no content-production checkout is needed.
"""
import argparse
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
BUILDERS = {"home": "home", "agentic-web": "agentic_web", "workflows": "workflows", "software-factories": "software_factories"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pages", nargs="*", help="Pages to rebuild; default: all four")
    parser.add_argument("--assets", action="store_true", help="Re-export artwork from image originals")
    parser.add_argument("--scenes", type=Path, help="Path to supporting_images (or set HOMEPAGE_SCENES)")
    args = parser.parse_args()
    pages = args.pages or list(BUILDERS)
    if any(p not in BUILDERS for p in pages):
        parser.error("Pages must be: " + ", ".join(BUILDERS))
    env = os.environ.copy()
    if args.scenes:
        env["HOMEPAGE_SCENES"] = str(args.scenes.resolve())
    if args.assets:
        scenes = Path(env.get("HOMEPAGE_SCENES", ROOT / "homepage/image_sources"))
        if not scenes.is_dir():
            parser.error("--assets requires --scenes /path/to/supporting_images or HOMEPAGE_SCENES")
        env["HOMEPAGE_REBUILD_ASSETS"] = "1"
    for page in pages:
        subprocess.run([sys.executable, "-I", str(ROOT / f"homepage/tools/build_{BUILDERS[page]}.py")], check=True, env=env)
    subprocess.run([sys.executable, "-I", str(ROOT / "scripts/publish_home.py")], check=True)


if __name__ == "__main__":
    main()

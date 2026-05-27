#!/bin/zsh

if command -v uv >/dev/null 2>&1; then
  uv run mkdocs serve --livereload --watch-theme &
elif [ -x .venv/bin/mkdocs ]; then
  .venv/bin/mkdocs serve --livereload --watch-theme &
else
  echo "Could not find uv or .venv/bin/mkdocs. Run 'uv sync' first." >&2
  exit 1
fi
sleep 0.5
open http://127.0.0.1:8000/
wait
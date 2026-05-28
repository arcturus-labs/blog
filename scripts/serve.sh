#!/bin/zsh

cleanup() {
  kill "$server_pid" 2>/dev/null
  exit 0
}
trap cleanup INT TERM

if command -v uv >/dev/null 2>&1; then
  uv run mkdocs serve --livereload --watch-theme &
elif [ -x .venv/bin/mkdocs ]; then
  .venv/bin/mkdocs serve --livereload --watch-theme &
else
  echo "Could not find uv or .venv/bin/mkdocs. Run 'uv sync' first." >&2
  exit 1
fi
server_pid=$!
sleep 0.5
open http://127.0.0.1:8000/blog/
wait "$server_pid"
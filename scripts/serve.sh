#!/bin/zsh

uv run mkdocs serve --livereload --watch-theme &
sleep 0.5
open http://127.0.0.1:8000/
wait
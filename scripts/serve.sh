#!/bin/zsh

# Activate virtual environment
source ~/.virtualenvs/blog/bin/activate

# Start mkdocs development server with live reloading
# --livereload enables automatic browser refresh on file changes
# --watch-theme watches theme files for changes
open http://127.0.0.1:8000/
mkdocs serve --livereload --watch-theme

# Deactivate virtual environment
deactivate 
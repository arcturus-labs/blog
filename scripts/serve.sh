#!/bin/zsh

# Activate virtual environment
source ~/.virtualenvs/blog/bin/activate

# Start mkdocs development server with live reloading
open http://127.0.0.1:8000/
mkdocs serve 

# Deactivate virtual environment
deactivate 
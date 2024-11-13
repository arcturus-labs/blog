#!/bin/zsh

# Activate virtual environment
source ~/.virtualenvs/blog/bin/activate

# Start mkdocs development server with live reloading
mkdocs serve 

# Deactivate virtual environment
deactivate 
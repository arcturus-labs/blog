#!/bin/zsh

# Activate virtual environment
source ~/.virtualenvs/blog/bin/activate

# Build and deploy documentation to GitHub Pages
mkdocs gh-deploy

# Deactivate virtual environment
deactivate 
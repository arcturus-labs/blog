#!/bin/zsh


# Assert git workspace is clean
if [[ -n $(git status --porcelain) ]]; then
  echo "Error: Git workspace is not clean. Please commit or stash your changes before deploying."
  exit 1
fi

# Activate virtual environment
source ~/.virtualenvs/blog/bin/activate

# Build and deploy documentation to GitHub Pages
mkdocs gh-deploy

# Deactivate virtual environment
deactivate 
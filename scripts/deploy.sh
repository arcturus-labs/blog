#!/bin/zsh


# Assert git workspace is clean
if [[ -n $(git status --porcelain) ]]; then
  echo "Error: Git workspace is not clean. Please commit or stash your changes before deploying."
  exit 1
fi

# Check if on 'main' branch
if [[ $(git rev-parse --abbrev-ref HEAD) != "main" ]]; then
  echo "Error: You must be on the 'main' branch to deploy."
  exit 1
fi

# Check if local branch is ahead of remote (unpushed commits)
if [[ $(git rev-list --count HEAD...@{u} 2>/dev/null) -gt 0 ]]; then
  echo "Error: You have unpushed commits. Please push your changes before deploying."
  exit 1
fi

# Activate virtual environment
source ~/.virtualenvs/blog/bin/activate

# Build and deploy documentation to GitHub Pages
mkdocs gh-deploy

# Deactivate virtual environment
deactivate 
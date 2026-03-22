#!/bin/bash
# Deploy Cognivia static site to GitHub Pages
# Usage: 1) Create repo on GitHub (public). 2) Run this script from inside website/static/
# It will initialize git, add all files, commit, and push to main branch.

set -e

echo "=== Cognivia Static Site Deploy ==="
read -p "GitHub repo URL (e.g., https://github.com/yourusername/cognivia.github.io.git): " REPO_URL

git init
git add .
git commit -m "Deploy Cognivia landing page - 2026-03-19"
git branch -M main
git remote add origin "$REPO_URL"
git push -u origin main

echo "Push complete. Enable GitHub Pages in repo Settings → Pages (source: main branch, root)."
echo "Site will be live at: https://yourusername.github.io/ (or custom domain after DNS)."

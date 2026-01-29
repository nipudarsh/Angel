#!/usr/bin/env bash
set -euo pipefail

PROJECT_PATH="$1"
REPO_URL="$2"

if [[ -z "$PROJECT_PATH" || -z "$REPO_URL" ]]; then
  echo "Usage: ./setup-angel.sh <project-path> <repo-url>"
  exit 1
fi

mkdir -p "$PROJECT_PATH"
cd "$PROJECT_PATH"

if [[ ! -d .git ]]; then
  git init
fi

python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install --prefer-binary -r requirements.txt
pip install -e .

if ! git remote | grep -q origin; then
  git remote add origin "$REPO_URL"
fi

echo "Setup complete."

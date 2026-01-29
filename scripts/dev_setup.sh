#!/usr/bin/env bash
set -euo pipefail
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install --prefer-binary -r requirements.txt -r requirements-dev.txt
pip install -e .

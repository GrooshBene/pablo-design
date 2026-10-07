#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"
export PLAYWRIGHT_BROWSERS_PATH="$ROOT/.pablo/browsers"
npm ci --cache "$ROOT/.pablo/npm-cache" --no-audit --no-fund --fetch-retries=0
python3 -m venv "$ROOT/.venv"
"$ROOT/.venv/bin/python" -m pip install --disable-pip-version-check -r "$ROOT/scripts/pablo/requirements.lock"
"$ROOT/.venv/bin/python" "$ROOT/scripts/pablo/setup_fonts.py"
npx --no-install playwright install chromium
"$ROOT/.venv/bin/python" -m playwright install chromium
"$ROOT/pablo" doctor

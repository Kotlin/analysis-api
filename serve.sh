#!/usr/bin/env bash
# Builds the website and serves it locally with live reload.
set -euo pipefail
cd "$(dirname "$0")"

command -v python3 >/dev/null || { echo "python3 is required: https://www.python.org/downloads/" >&2; exit 1; }

[ -d .venv ] || python3 -m venv .venv
.venv/bin/pip install --quiet --upgrade zensical

exec .venv/bin/zensical serve "$@"

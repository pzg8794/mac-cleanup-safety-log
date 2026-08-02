#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
cd "$repo_root"

python3 scripts/validate_repo.py
git diff --check
git diff --cached --check

printf 'Public repository validation passed.\n'

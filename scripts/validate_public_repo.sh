#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
cd "$repo_root"

python3 scripts/validate_repo.py
git diff --check
git diff --cached --check

private_ignore_examples=(
  "backup-iphone.json"
  "export-ios.json"
  "drive-file-list.csv"
  "github-repos.json"
  "repositories.csv"
  "cleanup-plan.json"
  "report-storage.txt"
)

public_ignore_examples=(
  "docs/ROADMAP.md"
  "docs/DATA_PLACEMENT_POLICY.md"
  "scopes/github/README.md"
)

for artifact in "${private_ignore_examples[@]}"; do
  if ! git check-ignore --quiet --no-index -- "$artifact"; then
    printf 'Private-artifact ignore regression: %s\n' "$artifact" >&2
    exit 1
  fi
done

for public_path in "${public_ignore_examples[@]}"; do
  if git check-ignore --quiet --no-index -- "$public_path"; then
    printf 'Required public path is unexpectedly ignored: %s\n' "$public_path" >&2
    exit 1
  fi
done

printf 'Public repository validation passed.\n'

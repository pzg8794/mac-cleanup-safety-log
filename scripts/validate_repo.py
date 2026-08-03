#!/usr/bin/env python3
"""Validate that the tracked repository remains public-safe and internally consistent."""

from __future__ import annotations

import csv
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve().relative_to(ROOT).as_posix()

REQUIRED = {
    "README.md",
    "LICENSE",
    "DISCLAIMER.md",
    "SECURITY.md",
    "docs/SAFETY_MODEL.md",
    "docs/WORKFLOW.md",
    "docs/ROADMAP.md",
    "docs/DATA_PLACEMENT_POLICY.md",
    "docs/BACKUP_AND_RECOVERY_POLICY.md",
    "docs/RETENTION_POLICY.md",
    "docs/AUDIT_METHOD.md",
    "docs/STATUS.md",
    "docs/DECISION_LOG.md",
    "docs/APPROVAL_WORKFLOW.md",
    "docs/PRIVACY_BOUNDARY.md",
    "docs/PROVENANCE.md",
    "docs/AI_USE_LOG.md",
    "audit/2026-08-02-tier1.md",
    "data/public-metrics.csv",
    "templates/candidate-review.md",
    "templates/run-report.md",
    "scopes/mac/README.md",
    "scopes/iphone/README.md",
    "scopes/google-drive/README.md",
    "scopes/github/README.md",
}

FORBIDDEN_FILE_PARTS = {
    "_Inventory",
    "_Duplicates",
    "_Command_Log",
    "_Manifest",
    ".photoslibrary",
    ".musiclibrary",
}

FORBIDDEN_ARTIFACT_PATTERNS = {
    "iPhone or iOS export/backup": re.compile(
        r"(?:(?:iphone|ios).*?(?:exports?|backups?)|"
        r"(?:exports?|backups?).*?(?:iphone|ios))",
        re.I,
    ),
    "inventory": re.compile(r"inventor(?:y|ies)", re.I),
    "device screenshot": re.compile(r"screen[._ -]*shots?", re.I),
    "cloud or file listing": re.compile(
        r"(?:(?:cloud|drive|files?).*?(?:listings?|lists?)|"
        r"(?:listings?|lists?).*?(?:cloud|drive|files?))",
        re.I,
    ),
    "repository listing": re.compile(
        r"(?:^|[/\\])(?:github[._ -]*repos?|repositor(?:y|ies))"
        r"(?:[._ -].*)?\.(?:csv|json|tsv|txt)$",
        re.I,
    ),
    "private manifest": re.compile(r"(?:private[._ -]*)?manifests?", re.I),
    "local cleanup plan": re.compile(
        r"(?:cleanup.*?plans?|plans?.*?cleanup)", re.I
    ),
    "raw storage report": re.compile(
        r"(?:(?:raw.*?)?storage.*?reports?|reports?.*?storage)", re.I
    ),
    "device backup tree": re.compile(r"mobilesync[/\\]backup", re.I),
}

PRIVATE_PATTERN_EXAMPLES = {
    "backup-iphone.json",
    "export-ios.json",
    "drive-file-list.csv",
    "github-repos.json",
    "repositories.csv",
    "cleanup-plan.json",
    "report-storage.txt",
}

PUBLIC_PATTERN_EXAMPLES = {
    "docs/ROADMAP.md",
    "docs/DATA_PLACEMENT_POLICY.md",
    "scopes/github/README.md",
}

FORBIDDEN_SUFFIXES = {
    ".db",
    ".sqlite",
    ".sqlite3",
    ".pem",
    ".key",
    ".p12",
    ".pfx",
    ".zip",
    ".dmg",
    ".pkg",
    ".mov",
    ".mp4",
    ".m4a",
    ".zoom",
    ".png",
    ".jpg",
    ".jpeg",
    ".heic",
    ".gif",
    ".webp",
    ".tif",
    ".tiff",
    ".plist",
    ".log",
    ".tsv",
    ".ipsw",
    ".ipa",
    ".mobileconfig",
    ".mobileprovision",
}

CONTENT_RULES = {
    "absolute macOS home path": re.compile(r"/Users/[^/\s]+/"),
    "mounted-volume path": re.compile(r"/Volumes/[^/\s]+/"),
    "local file URI": re.compile(r"\bfile://"),
    "local account name": re.compile(r"\bpitergarcia\b", re.I),
    "email address": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
    "GitHub-style token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    "API key-like token": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "private-key header": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "private-file SHA-256": re.compile(r"\b[0-9a-fA-F]{64}\b"),
    "private commit or legacy device identifier": re.compile(r"\b[0-9a-fA-F]{40}\b"),
}

MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def tracked_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
    )
    return [part.decode("utf-8") for part in result.stdout.split(b"\0") if part]


def check_required(files: set[str], errors: list[str]) -> None:
    for missing in sorted(REQUIRED - files):
        errors.append(f"missing required file: {missing}")


def matching_artifact_labels(name: str) -> list[str]:
    return [
        label
        for label, pattern in FORBIDDEN_ARTIFACT_PATTERNS.items()
        if pattern.search(name)
    ]


def check_pattern_regressions(errors: list[str]) -> None:
    for name in sorted(PRIVATE_PATTERN_EXAMPLES):
        if not matching_artifact_labels(name):
            errors.append(f"private-artifact pattern regression: {name}")
    for name in sorted(PUBLIC_PATTERN_EXAMPLES):
        labels = matching_artifact_labels(name)
        if labels:
            errors.append(
                f"public path rejected by artifact pattern: {name} ({', '.join(labels)})"
            )


def check_filenames(files: list[str], errors: list[str]) -> None:
    for name in files:
        path = Path(name)
        if (ROOT / name).is_symlink():
            errors.append(f"symbolic link is tracked: {name}")
        if any(
            part.casefold()
            in {
                "private",
                "raw",
                "local",
                "quarantine",
                "device-exports",
                "device-backups",
                "cloud-exports",
                "cloud-listings",
                "repo-inventories",
                "local-plans",
                "screenshots",
                "storage-reports",
            }
            for part in path.parts
        ):
            errors.append(f"private working directory is tracked: {name}")
        if any(part.casefold() in name.casefold() for part in FORBIDDEN_FILE_PARTS):
            errors.append(f"raw/private artifact filename is tracked: {name}")
        for label in matching_artifact_labels(name):
            errors.append(f"{label} filename is tracked: {name}")
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"forbidden binary or private-data suffix is tracked: {name}")
        if path.name == ".env" or path.name.startswith(".env."):
            errors.append(f"environment file is tracked: {name}")
        size = (ROOT / name).stat().st_size
        if size > 1_000_000:
            errors.append(f"unexpected file larger than 1 MB: {name} ({size} bytes)")


def check_git_modes(errors: list[str]) -> None:
    result = subprocess.run(
        ["git", "ls-files", "--stage", "-z"],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
    )
    for raw_entry in result.stdout.split(b"\0"):
        if not raw_entry:
            continue
        metadata, name = raw_entry.decode("utf-8").split("\t", 1)
        mode = metadata.split()[0]
        if mode == "160000":
            errors.append(f"Git submodule is tracked: {name}")


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None


def check_contents(files: list[str], errors: list[str]) -> None:
    for name in files:
        if name == SELF:
            continue
        text = read_text(ROOT / name)
        if text is None:
            errors.append(f"unexpected non-text tracked file: {name}")
            continue
        for label, pattern in CONTENT_RULES.items():
            if pattern.search(text):
                errors.append(f"{label} found in {name}")


def check_markdown_links(files: list[str], errors: list[str]) -> None:
    for name in files:
        if not name.endswith(".md"):
            continue
        source = ROOT / name
        text = source.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().split()[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            relative = unquote(target.split("#", 1)[0])
            resolved = (source.parent / relative).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(f"link escapes repository in {name}: {target}")
                continue
            if not resolved.exists():
                errors.append(f"broken local link in {name}: {target}")


def check_metrics(errors: list[str]) -> None:
    path = ROOT / "data/public-metrics.csv"
    expected = ["date", "phase", "metric", "value", "unit", "notes"]
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
        if handle.seekable():
            pass
    if not rows:
        errors.append("public metrics CSV is empty")
        return
    if list(rows[0].keys()) != expected:
        errors.append("public metrics CSV schema does not match expected columns")
    seen: set[tuple[str, str, str]] = set()
    for index, row in enumerate(rows, start=2):
        key = (row["date"], row["phase"], row["metric"])
        if key in seen:
            errors.append(f"duplicate metrics key on row {index}: {key}")
        seen.add(key)
        try:
            value = int(row["value"])
        except ValueError:
            errors.append(f"non-integer metric value on row {index}")
            continue
        if value < 0:
            errors.append(f"negative metric value on row {index}")


def main() -> int:
    errors: list[str] = []
    files = tracked_files()
    file_set = set(files)
    check_required(file_set, errors)
    check_pattern_regressions(errors)
    check_filenames(files, errors)
    check_git_modes(errors)
    check_contents(files, errors)
    check_markdown_links(files, errors)
    check_metrics(errors)

    if errors:
        print("Public repository validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(files)} tracked files; no public-safety violations found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Rule 0 Workspace Maintenance — 2026-09-01

## Scope

This authorized maintenance run covered local archives, exact duplicate
generated reports, cross-course reuse, and course-repository boundaries in one
user-controlled workspace. It did not authorize operating-system, cloud,
managed-library, Trash, repository-history, or broad project-output cleanup.

Private paths, filenames, content hashes, repository identities, branch names,
and commands remain in the private evidence record.

## Rule 0 change

The workspace's recursive cleanup rule was tightened before action. It now
requires directory-specific ownership and lifecycle review, an inactive owner,
exact bounded targets, content and reference checks, recovery evidence, and an
immediate pre-execution revalidation. It also requires each course to have a
bounded repository and prefers full-commit GitHub references only for
reference-only, public-safe material.

Executable dependencies, private or submission-specific material, and
repository history remain protected.

## Archive result

- ZIP files initially inventoried: 123
- Initial ZIP allocated bytes: 615,915,520
- Initial exact whole-file ZIP duplicate groups: 44
- Duplicate ZIP files removed: 40
- ZIP files retained after action: 83
- Retained ZIP allocated bytes: 593,498,112
- Corrupt ZIPs found: 0

All 83 retained ZIPs were classified through their owning project. They include
source and provenance snapshots, course-source packages, submission or delivery
artifacts, intentionally versioned archives, and generated analytical bundles
whose deterministic recreation or durable rollback was not proven. Extension,
age, nearby extraction, and byte equality were not treated as deletion proof.

## Exact duplicate action

One ignored, untracked generated-report directory contained 80 independent
duplicate files: 40 ZIP reports and their 40 HTML counterparts. Every removed
file had one SHA-256-identical retained canonical copy in the same directory.

Preflight established:

- ordinary files on one local filesystem;
- independent inodes with link count one;
- no symbolic links, special files, or active owner;
- ignored and untracked repository state;
- canonical naming supported by the producing workflow's provenance record;
- integrity of every retained ZIP;
- unchanged identity and digest immediately before unlinking.

Post-action verification established:

- removed files: 80
- logical bytes removed: 46,823,868
- allocated bytes released at the targets: 46,993,408
- retained canonical files: 80
- remaining physical duplicate groups in that directory: 0
- tracked repository changes caused by the action: 0
- cleanup errors after deletion began: 0

Whole-volume free space changed substantially during concurrent background
activity, so no APFS-wide increase is attributed to this small target-level
action.

## Cross-course reuse result

The largest cross-course overlap was executable framework code and notebooks.
Those files are required locally by a course implementation and remain
protected as an intentional fork or vendored dependency. Web links are not a
functional replacement.

A small set of clean reference-only documents could later become commit-pinned
GitHub stubs, but the consuming repository is dirty and behind its remote.
Replacing them now would mix maintenance with unresolved work. No cross-course
file was removed or replaced in this run.

## Course-repository preflight

- Course roots reviewed: 25
- Roots with a local repository, origin, and upstream: 25
- Local heads matching the live remote head: 20
- Roots requiring reconciliation: 5
- Roots with worktree changes: 11
- Pulls, merges, resets, commits, pushes, remote changes, or history rewrites: 0

The five nonmatching roots all contain uncommitted work. Three are confirmed
behind their remote. Two also contain malformed empty Finder metadata inside
Git reference directories that blocks a normal fetch. Both conditions remain
stopped for repository-specific, non-destructive review.

## Concurrent-state boundary

Previously known runtime-state locations were already empty or absent when
this run began. No recovery is attributed to this run, and no claim is made
about when or why that material changed.

## Final decision

The exact duplicate report set passed Rule 0 and was removed. All remaining
archives, cross-course executable material, protected records, dirty repository
content, and ambiguous metadata were kept. No broad cleanup command was used.

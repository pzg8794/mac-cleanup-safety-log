# Mac Cleanup Safety Log

[![Public-safety validation](https://github.com/pzg8794/mac-cleanup-safety-log/actions/workflows/public-safety.yml/badge.svg)](https://github.com/pzg8794/mac-cleanup-safety-log/actions/workflows/public-safety.yml)

A public-safe record of a preservation-first cleanup project that began with the Mac and is expanding to connected digital-storage systems: Mac, iPhone, Google Drive, and GitHub repositories with their local clones.

This repository is the project's public-safe **decision and accountability layer**. It documents how decisions are made, what is verified, what is intentionally preserved, and what measurable result follows. Private inventories, exact targets, evidence crosswalks, and execution artifacts remain local. This is **not** a one-click cleanup utility and contains no machine-specific deletion commands.

## Current outcome

The project completed three controlled phases on 2026-08-02:

1. A read-only storage and duplicate audit.
2. A corrected second pass that removed dependency, environment, worktree, and hard-link false positives.
3. A Tier 1 cleanup limited to five revalidated, regenerable caches.

Tier 1 removed 11,792 cache files. Target-level accounting showed 856,268,800 allocated bytes released, while APFS free space increased by 845,258,752 bytes. Fourteen other provisional cache entries were skipped because their owners were active, their contents crossed a safety boundary, or their ownership was ambiguous.

No repository, environment, database, cloud-managed folder, managed media library, personal recording, research state, backup, or higher-tier candidate was changed.

This documentation expansion performs no new audit or cleanup.

## Connected scopes

| Scope | Current state | Public control page |
|---|---|---|
| Mac | Audit v1 complete; corrected audit v2 complete; Tier 1 complete; Tier 2 pending | [`scopes/mac/`](scopes/mac/README.md) |
| iPhone | Not started | [`scopes/iphone/`](scopes/iphone/README.md) |
| Google Drive | Not started | [`scopes/google-drive/`](scopes/google-drive/README.md) |
| GitHub repositories and local clones | Not started | [`scopes/github/`](scopes/github/README.md) |

Each scope requires its own audit, approval, execution, and verification phase. Evidence and approval do not transfer between systems.

## Guiding principle

> Large, old, or duplicated does not mean disposable.

Every action must pass a preservation test:

- Is the item explicitly in scope?
- Is it independently recoverable or automatically regenerable?
- Is its owning process inactive?
- Are links, repositories, environments, databases, and managed content excluded?
- Is there a canonical retained copy when redundancy is claimed?
- Has the user approved this exact risk tier?
- Can the result be measured and audited afterward?

## Repository map

| Location | Purpose |
|---|---|
| [`docs/SAFETY_MODEL.md`](docs/SAFETY_MODEL.md) | Five cleanup tiers and hard safety boundaries |
| [`docs/WORKFLOW.md`](docs/WORKFLOW.md) | End-to-end audit, approval, execution, and verification flow |
| [`docs/ROADMAP.md`](docs/ROADMAP.md) | Ordered cross-system program plan and approval gates |
| [`docs/DATA_PLACEMENT_POLICY.md`](docs/DATA_PLACEMENT_POLICY.md) | Draft canonical-location and minimal-local-storage rules |
| [`docs/BACKUP_AND_RECOVERY_POLICY.md`](docs/BACKUP_AND_RECOVERY_POLICY.md) | Draft proof required before local deletion can be proposed |
| [`docs/RETENTION_POLICY.md`](docs/RETENTION_POLICY.md) | Draft retention states and category-transition rules |
| [`docs/AUDIT_METHOD.md`](docs/AUDIT_METHOD.md) | Storage, duplicate, hard-link, and archive methodology |
| [`docs/STATUS.md`](docs/STATUS.md) | Current public-safe project status and next decision gate |
| [`docs/DECISION_LOG.md`](docs/DECISION_LOG.md) | Durable record of preservation and cleanup decisions |
| [`docs/APPROVAL_WORKFLOW.md`](docs/APPROVAL_WORKFLOW.md) | Evidence required before an action can advance |
| [`docs/PRIVACY_BOUNDARY.md`](docs/PRIVACY_BOUNDARY.md) | What must remain outside public Git |
| [`docs/PROVENANCE.md`](docs/PROVENANCE.md) | Relationship between private evidence and public summaries |
| [`docs/AI_USE_LOG.md`](docs/AI_USE_LOG.md) | AI assistance, verification, and human responsibility |
| [`audit/2026-08-02-tier1.md`](audit/2026-08-02-tier1.md) | Sanitized Tier 1 run record |
| [`data/public-metrics.csv`](data/public-metrics.csv) | Machine-readable, non-identifying project metrics |
| [`templates/`](templates) | Candidate-review and run-report templates |
| [`scripts/validate_repo.py`](scripts/validate_repo.py) | Public-safety and documentation validation |
| [`DISCLAIMER.md`](DISCLAIMER.md) | Limits, responsibility, and non-advice notice |
| [`SECURITY.md`](SECURITY.md) | Private reporting instructions for accidental disclosure |

## What is intentionally absent

The private working audit remains local. This public repository does not include:

- absolute home-directory paths or account identifiers;
- raw file inventories, duplicate manifests, or command logs;
- iPhone exports or backups, Google Drive inventories, repository inventories, cloud listings, or local cleanup plans;
- personal filenames, media, transcripts, messages, or email;
- repository worktree paths, private project names, or untracked-file details;
- device backups, cloud-storage listings, database contents, or application profiles;
- content hashes tied to private files;
- credentials, tokens, secrets, or configuration databases.

See the full [privacy boundary](docs/PRIVACY_BOUNDARY.md).

## Reusing the process

Start with the [candidate-review template](templates/candidate-review.md). Keep machine-specific evidence in a private workspace and publish only aggregated results after reviewing them against the privacy boundary. The automated validation is a backstop, not a substitute for human review.

## Project status

- Mac: Tier 1 complete and verified; Tier 2 pending
- iPhone: not started
- Google Drive: not started
- GitHub and local clones: not started
- Cross-system data-placement, backup/recovery, and retention policies: drafted in this change

This project stops at each approval boundary. A future tier requires a new evidence review and explicit authorization.

## License

Released under the [MIT License](LICENSE).

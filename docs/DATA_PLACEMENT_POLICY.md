# Data Placement Policy

Status: **Drafted**. This policy records the proposed control model; it does not authorize migration or cleanup.

## Core principle

> “Cloud-first and locally minimal, but never single-copy for irreplaceable data.”

Data placement should make the canonical copy clear without confusing synchronization with backup. Local storage should support active work and necessary offline access, while irreplaceable material must retain an independent recovery route.

## Canonical locations

| Data type | Appropriate canonical location | Important qualification |
|---|---|---|
| Source code, scripts, notebooks, and versioned documentation | GitHub | A pushed repository does not automatically include untracked, ignored, large-file, secret, environment, or generated state |
| Documents, coursework, business records, and selected research materials | Google Drive | Confirm ownership, permissions, complete file content, version needs, and synchronization behavior |
| Photographs and videos | Photo or cloud-media storage | Confirm full-resolution originals, metadata, album/export needs, and deletion propagation |
| Active working data and necessary offline access | Local devices | Keep the working set intentional, current, and recoverable |
| Irreplaceable material | A separate recovery copy | The recovery route must be independent of the canonical copy and tested |

These defaults guide review; they do not override legal, contractual, institutional, privacy, or research requirements.

## Canonical-copy test

Before designating a copy as canonical, verify:

1. the content is complete rather than a placeholder, shortcut, preview, or partial export;
2. the owner and permissions are understood;
3. the copy can be accessed through an independent route;
4. the expected version, metadata, and directory structure are retained;
5. synchronization behavior is known;
6. a separate recovery route exists when loss would be unacceptable;
7. the designation is recorded in the private audit.

## Online presence is not deletion evidence

Merely seeing a file online is not enough evidence to delete a local copy. The online item may be inaccessible to another account or device, incomplete, optimized, shared but not owned, a shortcut, or governed by synchronized deletion.

Accessibility, completeness, ownership, synchronization state, and recovery must all be verified before local deletion can even be proposed.

## Placement changes

A move between systems is a migration, not a cleanup shortcut. Treat it as its own audited operation:

- verify source and destination;
- preserve metadata and structure that matter;
- confirm upload or push completion;
- verify from another access route;
- retain a recovery copy during the hold period;
- document the result privately;
- publish only a sanitized status here.

## Related controls

- [Backup and recovery policy](BACKUP_AND_RECOVERY_POLICY.md)
- [Retention policy](RETENTION_POLICY.md)
- [Workflow](WORKFLOW.md)
- [Approval workflow](APPROVAL_WORKFLOW.md)
- [Privacy boundary](PRIVACY_BOUNDARY.md)

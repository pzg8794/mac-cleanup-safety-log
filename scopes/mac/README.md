# Mac Scope

## Purpose

Track the preservation-first audit, approval, execution, and verification of storage decisions on the Mac that began this project.

## Current status

- Audit v1: complete and read-only
- Corrected audit v2: complete and read-only
- Tier 1: complete and verified
- Rule 0 workspace maintenance: complete and verified
- Tier 2: privately proposed and awaiting explicit approval
- Higher-risk tiers: preserved or awaiting domain-specific review

The completed Tier 1 public record remains in [`audit/2026-08-02-tier1.md`](../../audit/2026-08-02-tier1.md).
The separately authorized workspace-maintenance record is in
[`audit/2026-09-01-rule0-workspace-maintenance.md`](../../audit/2026-09-01-rule0-workspace-maintenance.md).

## Major risks

- APFS allocation, clones, compression, snapshots, and dynamic swap can obscure physical recovery.
- Hard links can look like duplicates without consuming duplicate content blocks.
- Repositories, environments, databases, managed libraries, and synchronized storage require separate handling.
- Research, course, personal, historical, and backup material can be unique even when old or duplicated.

## Required evidence

- Exact private target and current size/allocation metadata
- Link, filesystem, owner-process, and material-change checks
- Content proof for redundancy claims
- Canonical retained copy or supported regeneration method
- Recovery and rollback plan
- Explicit tier and candidate approval
- Before/after target and APFS measurements

## Prohibited actions

- No broad parent-directory cleanup
- No repository, worktree, environment, database, managed-library, cloud-storage, or protected-content cleanup
- No elevated privileges or Trash emptying
- No higher-tier action based on a lower-tier approval
- No publication of machine paths, filenames, hashes, or exact commands

## Planned audit stages

1. Maintain the completed Tier 1 verification record.
2. Revalidate any Tier 2 candidate only after explicit review resumes.
3. Verify cross-system canonical copies and recovery routes.
4. Revisit history-backed and domain-specific candidates later in the roadmap.
5. Establish periodic storage and cache-regeneration checks.

## Approval boundary

The Mac scope is stopped before Tier 2. The existing proposal is not authorization to quarantine or delete anything.

## Related controls

- [Roadmap](../../docs/ROADMAP.md)
- [Data-placement policy](../../docs/DATA_PLACEMENT_POLICY.md)
- [Backup and recovery policy](../../docs/BACKUP_AND_RECOVERY_POLICY.md)
- [Retention policy](../../docs/RETENTION_POLICY.md)
- [Workflow](../../docs/WORKFLOW.md)
- [Approval workflow](../../docs/APPROVAL_WORKFLOW.md)
- [Privacy boundary](../../docs/PRIVACY_BOUNDARY.md)
- [Status](../../docs/STATUS.md)

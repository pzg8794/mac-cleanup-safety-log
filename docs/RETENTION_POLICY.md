# Retention Policy

Status: **Drafted**. These categories are proposed retention controls, not execution authority.

Retention categories describe why a copy exists and what evidence is required before its status can change. A category is not a blanket deletion rule.

## Categories

### Active local working set

Current material needed for active work or reliable offline access. Review for organization, but preserve until the working need changes and recovery is verified.

### Cloud canonical copy

The designated complete, owned, accessible cloud copy. Placeholder, shortcut, sharing, metadata, and synchronization status must be understood.

### Git-history-backed material

Source or documentation recoverable from verified repository history. Untracked, ignored, large-file, submodule, worktree, environment, secret, and generated state require separate treatment.

### Historical archive

An intentional snapshot that preserves context, structure, provenance, or prior state. Retain unless archive completeness and replacement value have been reviewed.

### Temporary cache

Automatically regenerable material with no user-authored content. It may qualify for Tier 1 only when its owner is inactive and all safety exclusions pass.

### Project-managed transient output

Run state, model checkpoints, logs, previews, results, or build output that the
owning project explicitly identifies as staged, regenerable, or offloadable.
This class remains protected while a run is active or until completion,
retention, content, restore, and recovery evidence satisfy Rule 0. A generated
name or ignored status does not establish this category.

### Verified redundant copy

An independent physical copy whose complete retained counterpart has been verified by content and context. Quarantine before any later deletion.

### Protected personal or research data

Personal records, media, evidence, course or business material, datasets, model state, checkpoints, manifests, and unpublished work. Default to retention and domain-specific review.

### Quarantine pending deletion

A reversible, dated holding state for a specifically approved candidate. Same-volume quarantine provides organizational rollback but no immediate storage recovery.

### Permanently retained recovery copy

An independent copy intentionally preserved against loss of the canonical system. Its location and test record remain private.

## Classification rules

- Age alone does not justify deletion.
- Size alone does not justify deletion.
- Matching filenames alone do not prove identical content or redundancy.
- Exact byte equality does not prove that context, metadata, packaging, or workflow value is redundant.
- A synchronized copy is not automatically a backup.
- A same-volume quarantine is not recovered storage.
- An unresolved category defaults to protected or manual review.

## Category transitions

A copy can move to a lower-retention category only when evidence supports the transition and the exact action is approved. Record transitions privately, including the old category, new category, evidence, recovery implications, approval, and verification result.

No category transition in this document authorizes cleanup.

## Related controls

- [Data-placement policy](DATA_PLACEMENT_POLICY.md)
- [Backup and recovery policy](BACKUP_AND_RECOVERY_POLICY.md)
- [Safety model](SAFETY_MODEL.md)
- [Approval workflow](APPROVAL_WORKFLOW.md)

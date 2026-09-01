# GitHub and Local Clones Scope

## Purpose

Track limited repository preflights while preserving history, remotes,
branches, worktrees, uncommitted state, and recoverability.

## Current status

A limited, authorized course-root preflight was completed on 2026-09-01.
Twenty-five course roots were checked for a local repository, origin, upstream,
worktree status, and live remote head. All had repositories and remotes; 20
heads matched, 11 worktrees had changes, and five roots required
reconciliation. No course repository was pulled, merged, reset, committed,
pushed, or reconfigured.

## Major risks

- Local clones may contain unpushed branches, uncommitted changes, untracked work, ignored artifacts, or different remotes.
- Worktrees, submodules, large-file storage, releases, actions, and package artifacts can create dependencies not visible in a simple file comparison.
- A folder without repository metadata may be a partial historical backup rather than a complete clone.
- Rewriting or replacing repository history can destroy provenance and recovery paths.
- Public and private repositories have different disclosure boundaries.

## Required evidence

- Repository identity, visibility, default branch, and configured remotes
- Local and remote branch/ref comparison
- Worktree, submodule, large-file, release, and package relationships
- Staged, unstaged, untracked, ignored, and stashed state
- Verification of what is and is not represented in durable history
- Recovery plan for unique local material
- Public/private publication review

## Prohibited actions

- No broader repository scan may be inferred from the limited course-root preflight
- No deletion, replacement, destructive reinitialization, history rewrite, force push, clean/reset operation, or remote change
- No individual-file deduplication inside repositories or worktrees
- No publication of private remotes, local paths, branch details, untracked filenames, secrets, or private commit evidence

## Planned audit stages

1. Preserve the completed private course-root inventory.
2. Review each dirty or divergent root independently.
3. Reconcile local and remote state without discarding work.
4. Identify unique local work and incomplete backups.
5. Classify generated, history-backed, protected, and externally stored material.
6. Build repository-level organization and recovery proposals.
7. Execute only separately approved, non-destructive actions.
8. Verify local/remote alignment and preserved recovery paths.

## Approval boundary

The limited preflight authorizes no synchronization or cleanup. Each dirty,
divergent, malformed, nested, or shared-remote repository requires its own
evidence review. No pull, merge, reset, push, remote change, link replacement,
or repository cleanup may be inferred from the preflight.

## Related controls

- [Roadmap](../../docs/ROADMAP.md)
- [Data-placement policy](../../docs/DATA_PLACEMENT_POLICY.md)
- [Backup and recovery policy](../../docs/BACKUP_AND_RECOVERY_POLICY.md)
- [Retention policy](../../docs/RETENTION_POLICY.md)
- [Workflow](../../docs/WORKFLOW.md)
- [Approval workflow](../../docs/APPROVAL_WORKFLOW.md)
- [Privacy boundary](../../docs/PRIVACY_BOUNDARY.md)
- [Status](../../docs/STATUS.md)

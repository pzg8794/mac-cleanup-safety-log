# GitHub and Local Clones Scope

## Purpose

Plan a future audit of GitHub repositories and local clones while preserving history, remotes, branches, worktrees, uncommitted state, and recoverability.

## Current status

No cross-system GitHub/local-clone audit or cleanup has started under this scope. Earlier Mac-scoped evidence checks, if any, do not constitute this audit. This repository is the only repository modified by this documentation change.

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

- No scan of other repositories or clones under this documentation change
- No deletion, replacement, destructive reinitialization, history rewrite, force push, clean/reset operation, or remote change
- No individual-file deduplication inside repositories or worktrees
- No publication of private remotes, local paths, branch details, untracked filenames, secrets, or private commit evidence

## Planned audit stages

1. Define the repository and clone scope privately.
2. Inventory repository identities without changing refs or worktrees.
3. Reconcile local and remote state read-only.
4. Identify unique local work and incomplete backups.
5. Classify generated, history-backed, protected, and externally stored material.
6. Build repository-level organization and recovery proposals.
7. Execute only separately approved, non-destructive actions.
8. Verify local/remote alignment and preserved recovery paths.

## Approval boundary

No audit or cleanup is authorized. Each repository or clone requires its own evidence review, and no repository action may be inferred from the Mac cleanup approval.

## Related controls

- [Roadmap](../../docs/ROADMAP.md)
- [Data-placement policy](../../docs/DATA_PLACEMENT_POLICY.md)
- [Backup and recovery policy](../../docs/BACKUP_AND_RECOVERY_POLICY.md)
- [Retention policy](../../docs/RETENTION_POLICY.md)
- [Workflow](../../docs/WORKFLOW.md)
- [Approval workflow](../../docs/APPROVAL_WORKFLOW.md)
- [Privacy boundary](../../docs/PRIVACY_BOUNDARY.md)
- [Status](../../docs/STATUS.md)

# Digital Cleanup Roadmap

This roadmap expands the project from its completed Mac foundation into a coordinated, public-safe digital-storage program. The repository remains the decision and accountability layer; machine-specific inventories, paths, manifests, and execution records remain private.

Each system has its own lifecycle:

> **Audit → Approval → Execution → Verification**

Evidence or approval from one system never authorizes action in another. Each phase stops at its next approval boundary.

## Planned order

### 1. Complete safe Mac cleanup tiers

Maintain the verified Tier 1 record and decide whether any privately reviewed Tier 2 candidate should advance. Higher-risk candidates remain preserved until separately approved.

Scope: [Mac](../scopes/mac/README.md)

### 2. Establish data-placement and recovery rules

Apply the [data-placement policy](DATA_PLACEMENT_POLICY.md), [backup and recovery policy](BACKUP_AND_RECOVERY_POLICY.md), and [retention policy](RETENTION_POLICY.md) before cross-system cleanup. A deletion proposal must identify both the canonical location and an independent recovery route when the data is irreplaceable.

### 3. Audit GitHub repositories and local clones

Inventory repository identities and relationships privately. Reconcile local clones, remotes, branches, worktrees, submodules, large-file storage, untracked work, ignored artifacts, and recoverability before proposing organization or cleanup.

Scope: [GitHub and local clones](../scopes/github/README.md)

### 4. Audit Google Drive

Distinguish complete cloud files from placeholders, shortcuts, shared items, locally allocated copies, and content governed by synchronization. Record ownership, access, completeness, and recovery privately before proposing changes.

Scope: [Google Drive](../scopes/google-drive/README.md)

### 5. Verify backups and canonical copies

Test that designated canonical copies are complete and accessible outside their current device. Confirm permissions, synchronization effects, and the independent recovery path. Merely seeing a name in a web interface is not verification.

### 6. Audit and clean the iPhone

Begin with a separate read-only audit only after recovery requirements are satisfied. Photos, videos, messages, app data, device backups, optimized storage, and synchronized deletion behavior require distinct evidence and approvals.

Scope: [iPhone](../scopes/iphone/README.md)

### 7. Revisit higher-risk Mac candidates

Return to preserved project, research, personal, historical, and backup candidates only after cross-system canonical locations and recovery routes are understood.

### 8. Establish periodic maintenance

Define a lightweight review schedule for storage health, cache regeneration, backup testing, repository synchronization, cloud ownership, device capacity, and unresolved approval items. Periodic review does not create standing deletion authority.

## Program gates

| Gate | Required result |
|---|---|
| Scope gate | One system, explicit exclusions, and no cross-system expansion |
| Audit gate | Read-only evidence is complete enough to classify uncertainty |
| Privacy gate | Private evidence is separated from the public summary |
| Approval gate | The exact system, tier, and candidates are explicitly authorized |
| Execution gate | Targets are revalidated immediately before a bounded action |
| Verification gate | Target and system-level outcomes are measured and protected data is checked |
| Stop gate | Work stops before the next system or risk tier |

## Current position

- Mac Tier 1 is complete and verified.
- Mac Tier 2 awaits approval.
- The data-placement, recovery, and retention policies are drafted.
- GitHub/local-clone, Google Drive, and iPhone audits have not started.
- No cleanup is authorized by this roadmap.

## Related controls

- [Workflow](WORKFLOW.md)
- [Approval workflow](APPROVAL_WORKFLOW.md)
- [Privacy boundary](PRIVACY_BOUNDARY.md)
- [Current status](STATUS.md)
- [Data-placement policy](DATA_PLACEMENT_POLICY.md)
- [Backup and recovery policy](BACKUP_AND_RECOVERY_POLICY.md)
- [Retention policy](RETENTION_POLICY.md)

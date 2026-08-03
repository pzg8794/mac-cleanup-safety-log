# Google Drive Scope

## Purpose

Plan a future audit of cloud organization, ownership, completeness, local allocation, synchronization, and recovery without exposing private Drive content.

## Current status

No Google Drive audit or cleanup has started. This README contains policy only and no cloud listing or inventory.

## Major risks

- A visible item may be a shortcut, placeholder, shared item, partial local copy, or inaccessible through another account or device.
- Local deletion may synchronize to the cloud, and cloud deletion may propagate to local devices.
- Shared access is not the same as ownership or durable retention.
- Coursework, business records, research, and personal documents may have legal, provenance, or version-history value.
- Moving content can change links, permissions, workflows, and ownership expectations.

## Required evidence

- Explicit folder and account scope recorded privately
- Ownership and permission status
- Complete-content verification rather than name-only presence
- Independent browser or device access test
- Shortcut, placeholder, and synchronization status
- Version, metadata, and directory-structure requirements
- Recovery route and deletion-propagation analysis
- Sanitized public result only

## Prohibited actions

- No Drive scan under this documentation change
- No deletion, move, rename, upload, download, permission change, ownership change, or sync-state change
- No publication of account identifiers, links, filenames, folder trees, screenshots, manifests, or content hashes
- No assumption that cloud presence makes a local copy disposable

## Planned audit stages

1. Define account, folder, and exclusion boundaries.
2. Inventory categories privately without changing content.
3. Determine ownership, access, completeness, and synchronization state.
4. Map canonical locations and independent recovery routes.
5. Identify organizational proposals separately from deletion proposals.
6. Build a private approval table.
7. Execute and verify only a separately approved scope.

## Approval boundary

No audit or cleanup is authorized. Any future Drive access requires a separate explicit audit request, and any change requires a later approval.

## Related controls

- [Roadmap](../../docs/ROADMAP.md)
- [Data-placement policy](../../docs/DATA_PLACEMENT_POLICY.md)
- [Backup and recovery policy](../../docs/BACKUP_AND_RECOVERY_POLICY.md)
- [Retention policy](../../docs/RETENTION_POLICY.md)
- [Workflow](../../docs/WORKFLOW.md)
- [Approval workflow](../../docs/APPROVAL_WORKFLOW.md)
- [Privacy boundary](../../docs/PRIVACY_BOUNDARY.md)
- [Status](../../docs/STATUS.md)

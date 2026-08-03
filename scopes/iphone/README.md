# iPhone Scope

## Purpose

Plan a future preservation-first audit of iPhone storage, synchronized content, device backups, and recovery dependencies.

## Current status

No iPhone audit or cleanup has started. This README defines governance only and records no device inventory.

## Major risks

- Deleting synchronized photos, videos, messages, or files may propagate across devices and cloud services.
- Optimized storage may show a local representation without a full-resolution local original.
- Device backups can be incomplete, encrypted, stale, inaccessible, or tied to account ownership.
- App data may lack an independent export or recovery path.
- Erasure, reset, and backup replacement can be irreversible.

## Required evidence

- Explicit audit scope and exclusions
- Current backup type, completeness, accessibility, ownership, and test status
- Full-resolution or complete-content verification for cloud media and files
- Synchronization and deletion behavior
- Independent recovery route for irreplaceable material
- Private inventory and sanitized public summary
- Separate approval for audit, execution, and verification

## Prohibited actions

- No device scan under this documentation change
- No deletion of photos, videos, messages, files, app data, or backups
- No device erase, reset, restore, sync-state change, account change, or backup replacement
- No publication of device identifiers, account details, screenshots, media, or inventory listings

## Planned audit stages

1. Define read-only scope and exclusions.
2. Verify backup and recovery prerequisites.
3. Collect a private storage-category inventory.
4. Classify synchronized, local-only, regenerable, and protected data.
5. Build an item-level private approval table.
6. Execute only an explicitly approved tier.
7. Verify device function, synchronization, backup state, and storage outcome.

## Approval boundary

No audit or cleanup is authorized. A future iPhone audit requires a separate explicit request before any device access.

## Related controls

- [Roadmap](../../docs/ROADMAP.md)
- [Data-placement policy](../../docs/DATA_PLACEMENT_POLICY.md)
- [Backup and recovery policy](../../docs/BACKUP_AND_RECOVERY_POLICY.md)
- [Retention policy](../../docs/RETENTION_POLICY.md)
- [Workflow](../../docs/WORKFLOW.md)
- [Approval workflow](../../docs/APPROVAL_WORKFLOW.md)
- [Privacy boundary](../../docs/PRIVACY_BOUNDARY.md)
- [Status](../../docs/STATUS.md)

# Backup and Recovery Policy

Status: **Drafted**. This policy defines evidence requirements but grants no deletion approval.

Deletion is not approved merely because another pathname or online entry exists. The retained copy must support recovery.

## Minimum recovery requirements

Before deleting local data, all of the following must be true:

1. **The canonical copy exists.** Its intended system and ownership are identified in the private audit.
2. **It is accessible through another route.** Verify from another device or browser rather than relying on the source device's cache.
3. **The complete file is retained.** A placeholder, shortcut, preview, optimized representation, or partial synchronization is not sufficient.
4. **Ownership and permissions are confirmed.** Shared access can expire and is not equivalent to ownership or durable recovery.
5. **Synchronization effects are understood.** Determine whether deleting locally will also delete or hide the canonical copy on other devices.
6. **Irreplaceable data has an independent recovery route.** The recovery copy must not share the same single point of failure as the canonical copy.
7. **The verification is recorded privately.** Include the method, date, result, limitations, and next review trigger.
8. **Only a sanitized result is published here.** Do not publish private paths, filenames, account details, device identifiers, hashes, or recovery locations.

Failure of any requirement means **keep** or **manual review**.

## Recovery classes

| Class | Meaning | Cleanup implication |
|---|---|---|
| Regenerable | A supported tool can recreate the material | May qualify for Tier 1 after owner and boundary checks |
| Canonical plus independent recovery | Complete canonical copy and a separate tested route exist | May support a later approval after synchronization review |
| History-backed | Exact material is recoverable from verified version history | Requires repository or application-specific proof |
| Single-copy | No independent recovery route exists | Do not delete |
| Unknown | Completeness, ownership, or synchronization is unresolved | Do not delete |

## Verification record

The private record should capture:

- evidence identifier;
- system and category;
- canonical-copy verification method;
- independent-access test;
- completeness and metadata result;
- owner and permission result;
- synchronization/deletion behavior;
- recovery route and last test date;
- unresolved limitations;
- approval status.

The public record should contain only the category, sanitized outcome, risk tier, and approval state.

## Recovery testing

A recovery copy that has never been accessed or restored is an assumption. Test proportionately to risk, without overwriting the working copy. Record failed, partial, or permission-limited tests as unresolved rather than treating them as success.

## Related controls

- [Data-placement policy](DATA_PLACEMENT_POLICY.md)
- [Retention policy](RETENTION_POLICY.md)
- [Approval workflow](APPROVAL_WORKFLOW.md)
- [Privacy boundary](PRIVACY_BOUNDARY.md)

# Decision Log

## D-001 — Treat cleanup as preservation work

**Decision:** Begin in audit-only mode and require proof before any filesystem change.

**Reason:** Size, age, and duplication do not establish disposability.

## D-002 — Keep raw evidence private

**Decision:** Publish methods, decisions, and aggregated metrics only.

**Reason:** Raw inventories contain home paths, personal filenames, private project structure, and content-derived identifiers.

## D-003 — Rebuild the duplicate inventory

**Decision:** Exclude environments, dependency stores, package installations, repositories, and worktrees before hashing.

**Reason:** The first pass incorrectly treated dependency files as cleanup opportunities.

## D-004 — Separate hard links from physical duplicates

**Decision:** Count same-device, same-inode paths as aliases with zero recoverable content while another link remains.

**Reason:** Removing one hard-linked name does not release the underlying blocks.

## D-005 — Preserve repository state

**Decision:** Never deduplicate or clean repository content at the individual-file level.

**Reason:** History, branches, worktrees, untracked files, and generated-state relationships require repository-level analysis.

## D-006 — Execute only the revalidated Tier 1 subset

**Decision:** Clean five entries and skip fourteen.

**Reason:** Only five remained regenerable, inactive, materially unchanged, and free of excluded structures at execution time.

## D-007 — Report target and volume recovery separately

**Decision:** Publish both target allocated-block change and observed APFS free-space change.

**Reason:** Filesystem accounting and background activity can produce a measurable difference.

## D-008 — Stop before Tier 2

**Decision:** Document the next proposal without moving or deleting its candidates.

**Reason:** A completed lower tier does not authorize the next risk tier.

## D-009 — Make directory context part of Rule 0

**Decision:** Require reviewers to inspect the owning project's instructions,
lifecycle, current status, and relevant task history before classifying
pre-existing output.

**Reason:** A global scan cannot distinguish active workflow state, recoverable
generated output, evidence, or deliberately retained project history.

## D-010 — Use stable cross-course references only when function and privacy permit

**Decision:** Prefer commit-pinned GitHub references for reference-only,
public-safe material, while preserving executable dependencies, private or
submission-specific artifacts, and repository history.

**Reason:** Blind file replacement can break a course, publish protected data,
or report storage recovery that Git history still consumes.

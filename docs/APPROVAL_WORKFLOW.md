# Approval Workflow

Every cleanup candidate receives a stable public-safe ID. Machine paths and private evidence remain in a separate local approval record.

## Required evidence

| Field | Requirement |
|---|---|
| Candidate ID | Stable, non-identifying identifier |
| Category | Cache, redundant directory, archive, generated output, backup, media, or protected material |
| Risk tier | One of the five documented tiers |
| Directory contract | Owning project instructions, lifecycle, and relevant task record reviewed |
| Run state | Producing workflow complete and owner inactive |
| Evidence | Why the item is regenerable or redundant |
| File count | Number of affected ordinary files |
| Logical size | Sum of file lengths |
| Allocated size | Measured allocated blocks |
| Expected recovery | Physical estimate, including uncertainty |
| Retained copy | Canonical copy or regeneration method |
| Link state | Symlink and hard-link findings |
| Active owner | Application or process state |
| Quarantine plan | Dated, exact, reversible destination |
| Rollback | Tested inverse action or regeneration path |
| Verification strength | Cryptographic equality or stronger domain-specific proof |
| Restore or resume test | Proportionate independent recovery evidence |
| Unresolved concern | Anything preventing low-risk classification |
| Approval | Explicit user decision and date |

## Advancement rules

An entry can advance only when:

1. it appears in the current approval table;
2. its risk tier is explicitly authorized;
3. the preflight still matches the approval evidence;
4. the target is exact and not a parent directory generalization;
5. all exclusions pass;
6. the command and expected effect are shown before execution;
7. post-action measurement and verification are planned.

## Quarantine rule

For non-cache material, the default action is an intact move to a dated quarantine on the same volume. This is organizationally reversible but releases no storage immediately. Permanent deletion requires a later approval after revalidation and an agreed hold period.

Use the [candidate-review template](../templates/candidate-review.md) to propose a new entry.

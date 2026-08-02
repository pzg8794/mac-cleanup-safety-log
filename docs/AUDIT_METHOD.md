# Audit Method

## Storage accounting

The audit used supported read-only macOS and package-manager inventory commands where available. Important distinctions were maintained between:

- logical file size;
- allocated blocks reported by file metadata;
- APFS container free space;
- Data-volume consumption;
- dynamic swap usage;
- snapshots, purgeable storage, and inaccessible areas;
- cloud placeholders versus locally allocated content.

Allocated size is an estimate, not a promise of recoverable space. APFS clones, compression, snapshots, and shared extents can retain blocks after a pathname disappears.

## Exact duplicates

The corrected method was:

1. Limit traversal to approved roots on the startup filesystem.
2. Do not follow symbolic links.
3. Exclude repositories, worktrees, environments, dependency stores, bundles, managed libraries, databases, virtual machines, containers, and package installations.
4. Group ordinary files by size.
5. Compute SHA-256 only within same-size collision groups.
6. Record device, inode, link count, modification time, and allocated blocks.
7. Separate hard-linked aliases from independent physical copies.
8. Classify same-project, cross-project, generated-output, research, and personal duplicates separately.

Filename similarity was never used as duplicate proof.

## Directory-level proof

A directory is redundant only when every ordinary file has a retained hash-identical counterpart and no unique metadata, context, or workflow component would be lost. Mixed staging directories remain intact when even one unique provenance or review file exists.

## Archive proof

An archive candidate requires:

- integrity validation;
- a complete member inventory;
- safe-path checks;
- member-by-member size and content comparison;
- identification of archive-only data and metadata;
- a determination of whether packaging or historical structure has value.

An archive is not disposable merely because similarly named extracted files exist nearby.

## Repository proof

Repository-related material is preserved unless history, refs, worktrees, remotes, untracked state, and recoverability are understood. A backup without repository metadata is not assumed complete, and generated output is not assumed reproducible without evidence.

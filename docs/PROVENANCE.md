# Provenance

The public record is derived from a richer private evidence set. The private set remains the source of truth for machine-specific decisions.

## Private evidence classes

- initial read-only audit report;
- corrected second-pass audit report;
- row-level duplicate inventory;
- item-level approval table;
- Tier 1 execution manifest;
- exact command log;
- post-cleanup results report;
- read-only repository, archive, media, and storage analyses.
- any future iPhone, Google Drive, or GitHub/local-clone private inventory, approval record, execution log, or recovery test.

These artifacts are intentionally not copied into public Git.

## Public transformation

Before publication, evidence is transformed by:

1. removing absolute paths and local identifiers;
2. replacing targets with stable decision IDs or categories;
3. omitting personal and project filenames;
4. omitting private content hashes and repository state;
5. retaining aggregate counts, measurements, methods, decisions, and caveats;
6. running automated leak and link checks;
7. reviewing the staged Git diff.

## Verification responsibility

Public summaries support transparency but are not sufficient to authorize cleanup. Authorization always refers back to the current private evidence and an explicit user decision.

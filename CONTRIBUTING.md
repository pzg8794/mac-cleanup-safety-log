# Contributing

Contributions should strengthen the safety, reproducibility, or clarity of this preservation-first workflow.

## Before opening a change

1. Use public-safe identifiers instead of machine paths or personal filenames.
2. Keep raw inventories, command logs, screenshots, archives, and content hashes private.
3. Describe evidence without exposing user content.
4. Do not add an automated deletion script.
5. Run `./scripts/validate_public_repo.sh`.

## Documentation standard

A cleanup claim should identify:

- the candidate's risk tier;
- the evidence used;
- the retained canonical copy or regeneration method;
- the expected physical recovery and its uncertainty;
- the rollback or quarantine strategy;
- the approval state;
- the verification result.

Old age, size, filename similarity, or location alone is never sufficient evidence.

## Pull requests

Keep each pull request focused on one documentation, validation, or process improvement. Explain what changed, why it is safe to publish, and which validation checks passed.

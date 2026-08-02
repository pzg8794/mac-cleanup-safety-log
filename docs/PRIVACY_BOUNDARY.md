# Privacy Boundary

This repository is deliberately less detailed than the private audit. Public documentation must remain useful without becoming a map of one person's files, accounts, projects, or media.

## Never publish here

- absolute home-directory paths or local account names;
- email addresses, cloud account identifiers, or mounted-sync paths;
- raw inventory or duplicate CSV files;
- exact command logs containing private targets;
- personal filenames, recording/session names, transcripts, messages, or media;
- financial, health, relationship, application, or identity records;
- research datasets, model states, checkpoints, experiment manifests, or unpublished project names;
- repository worktree paths, private remotes, untracked filenames, or private commit evidence;
- database, browser profile, session, preference, credential, or key material;
- content hashes for private files;
- screenshots of storage tools that expose private names;
- quarantine contents or recovery archives.

## Safe to publish after review

- generalized methods and safety rules;
- aggregate counts and storage measurements;
- non-identifying decision IDs;
- tool categories when they do not expose private activity;
- sanitized success, skip, and error totals;
- reusable templates and validation scripts;
- lessons about links, APFS accounting, archives, and approval boundaries.

## Review rule

Automation helps catch obvious leaks, but a human must review every public diff. If a detail is useful only because it identifies a particular private file or project, it belongs in the private audit—not here.

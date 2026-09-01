# Rule 0 — Clean Up After Yourself

Rule 0 applies recursively to every course, project, repository, worktree, and
task in a governed workspace. A narrower project instruction may add stronger
controls but must not weaken this rule.

## Current-task hygiene

Agents must use task-scoped locations for temporary renders, extraction,
previews, caches, and build intermediates. Before handoff they remove only the
current task's unneeded temporary artifacts, stop only task-created background
processes, and verify the workspace and repository state.

## Existing material is not agent-owned

Before classifying anything that existed before the current task, the reviewer
must resolve the owning project and repository, read its local instructions and
current lifecycle, storage, handoff, recovery, and status records, and check the
relevant task or agent history when available. A global size or age scan does
not establish project context.

Existing material falls into one of three classes:

1. **Project-managed transient material** — explicitly documented by its owner
   as completed, regenerable, staged, or offloadable.
2. **Verified redundant material** — content-identical to a deliberately
   retained canonical copy in the same ownership context, with all references
   and recovery implications understood.
3. **Protected or unknown material** — source, repositories, history,
   worktrees, user changes, active or recent state, datasets, manifests,
   validated or final outputs, environments, dependencies, databases,
   credentials, managed or synchronized content, and anything whose ownership
   or recovery is unclear.

Age, size, extension, filename, directory name, ignored status, online
presence, or even equal hashes may select an item for review; none proves that
the item is disposable.

## Mandatory deletion gate

A pre-existing item may advance only when every check passes:

- the target is exact and does not generalize to a parent or wildcard;
- the owner is inactive and the producing workflow is complete;
- the project contract permits removal or establishes automatic regeneration;
- any required durable copy is complete and independently accessible;
- equality uses a cryptographic content check or stronger domain proof;
- links, repositories, worktrees, environments, dependencies, databases,
  credentials, protected output, cloud-managed content, and unique user files
  are absent;
- source, document, manifest, notebook, build, and publication references have
  been checked;
- synchronization behavior, allocated-byte recovery, supported command,
  rollback, and restore or rebuild procedure are understood;
- the exact candidate and action are explicitly authorized; and
- the full preflight still passes immediately before execution.

Any missing, unavailable, contradictory, changed, or ambiguous check yields
**STOP — KEEP**. A cleanup tool with broader scope or weaker verification must
not be used.

## Course repositories and cross-course reuse

Every course must have its own bounded repository and configured remote. At the
start and end of work, verify the repository root, branch, worktree state,
remote, and live local-versus-remote commit state. Preserve divergence and
uncommitted work; never hide it with destructive reset, forced push, history
rewrite, or replacement of repository metadata.

When one course only needs to cite material already available in an authorized
GitHub repository, prefer a Markdown reference to a full-commit `blob` URL over
a second local copy. Before replacing a copy, prove byte equality with the
committed Git object, exclude course-specific edits and protected material,
update every local reference, and record the source repository, commit, path,
and reuse permission where relevant.

A web link is not a functional replacement for code or data that must execute
locally. Such material remains an explicitly documented vendored dependency or
uses an approved dependency mechanism with pinned version, provenance,
integrity, and update instructions. Private, unpublished, restricted,
submission-specific, personal, or evidentiary material must never be published
to manufacture a link.

Removing a tracked working-tree copy does not remove its blob from Git history
and must not be reported as immediate physical recovery. Repository history
rewriting and garbage collection require a separate repository migration plan
and approval.

## Always prohibited

- elevated privileges for workspace cleanup;
- broad or pattern-based recursive deletion;
- destructive Git cleanup or reset;
- deletion through a synchronized or cloud-mounted path;
- Trash emptying as part of an audit;
- publication of private paths, filenames, hashes, manifests, process details,
  or execution commands.

Cleanup is mandatory for current-task artifacts. Guessing what can be deleted
is forbidden.

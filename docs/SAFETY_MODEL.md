# Safety Model

The project treats cleanup as a data-preservation workflow. Risk classification happens before any filesystem, device, cloud, or repository action.

## Non-negotiable boundaries

- Begin with read-only inspection.
- Give each system its own audit, approval, execution, and verification cycle.
- Never transfer evidence or approval from one system to another.
- Never infer disposability from age, size, or filename.
- Never follow symbolic links during cleanup analysis.
- Distinguish hard-linked names from independent physical copies.
- Preserve repositories, worktrees, history, remotes, and uncommitted state.
- Exclude environments, dependencies, databases, browser profiles, credentials, managed libraries, cloud-managed storage, and system-managed storage.
- Treat synchronization as possible deletion propagation, not as an independent backup.
- Keep personal, course, research, financial, and business records unless a domain-specific review proves otherwise.
- Do not use elevated privileges.
- Do not empty Trash as part of an audit.
- Require explicit approval for each new cleanup tier.
- Prefer a dated quarantine and a tested rollback before permanent deletion.

## Risk tiers

| Tier | Material | Default action |
|---|---|---|
| 1 | Revalidated, regenerable caches and disposable temporary resources | Clean only when the owner is inactive and contents pass all exclusions |
| 2 | Fully verified redundant files or intact directories with complete retained copies | Quarantine after explicit approval; verify again before later deletion |
| 3 | Material recoverable from verified history or another durable source | Require source and recovery-path verification plus domain review |
| 4 | Project, research, course, application, or personal duplicates | Manual review; preserve context and provenance |
| 5 | Unique, uncertain, protected, system-managed, cloud-managed, or workflow-critical material | Do not touch |

## Automatic stop conditions

An entry does not advance when any of these are true:

- the owning application or process is active;
- a symbolic link or unexplained hard link is present;
- the target contains a repository, worktree, environment, dependency tree, database, session, preference, credential, model, or extension;
- the item changed materially since approval;
- the retained copy is incomplete or cannot be verified by content;
- ownership, accessibility, synchronization, or recovery is uncertain;
- the expected recovery is only logical, not physical;
- rollback is unclear;
- the scope is ambiguous.

Ambiguity resolves to **keep** or **manual review**, never automatic deletion.

# Approved Browser Cache Cleanup — 2026-11-07

The user explicitly approved two exact candidates after a separate read-only
review. Execution was limited to ordinary resource/code cache entries while
both owning browsers were inactive. This was a specific offline file action;
no native clearing dialog, profile reset or application uninstall was used.

## Verified result

| Candidate | Files removed | Logical bytes | Allocated bytes |
|---|---:|---:|---:|
| BC-CHROME | 475,648 | 8,224,405,642 | 8,958,902,272 |
| BC-ATLAS | 300,861 | 7,577,382,382 | 8,066,228,224 |
| Total | 776,509 | 15,801,788,024 | 17,025,130,496 |

The measured target allocation was 15.8559 GiB. Available volume space rose
from 9,806,942,208 to 27,400,896,512 bytes around the run, an observed increase
of 17,593,954,304 bytes. The difference between target and volume accounting
includes APFS metadata and unrelated system activity; it is not claimed as
additional target recovery.

## Scope and guards

The private allowlist contained 131 exact cache backend directories. File
selection required the known entry naming convention plus the fixed binary
signature documented in Chromium's implementation. Only that signature and
file metadata were read; cached keys, URLs, HTTP headers and page bodies were
not opened.

The complete review was repeated before deletion. Every target remained an
ordinary single-link file on the approved local filesystem, with unchanged
identity, measurements and metadata fingerprint. Owner-process and open-handle
checks passed, and browser restarts were checked during execution. No
application was terminated.

The command removed only the selected flat cache entries. It preserved all
cache directories, indexes, sparse/unrecognized files and other browser
storage. History, passwords, cookies, sessions, site data, preferences,
bookmarks, extensions and downloaded user files were outside its scope.

No repository history, environment, installed dependency, research material,
personal file, cloud item, managed library, OS file, snapshot, swap or Trash
item was a cleanup target.

## Post-action verification

- Remaining selected entries: 0.
- Original cache backend directory identities preserved: 131.
- Retained index/other metadata items independently checked: 1,208.
- Retained items missing or changed in the recorded metadata: 0.
- Cleanup errors or unresolved partial actions: 0.

Protected browser stores were not opened to inspect their contents. Their
exclusion is a command-scope guarantee, not a claim that every record or sign-in
was tested. Browsers remained closed after the action.

## Regeneration and evidence boundary

The approved removal was permanent and has no byte-for-byte undo copy.
Resource caches may refill through network requests; compiled code caches may
be rebuilt. First revisits may be slower, and historical resources no longer
available online are not guaranteed to be recoverable. A same-volume
quarantine would have released no immediate storage.

Exact paths, fingerprints, commands and private evidence remain local. The
private execution source, allowlist, result, metadata baseline and verification
record are intentional audit deliverables. No unneeded task-created temporary
directory, download, browser tab or service remains.

This approval does not establish standing permission for another purge or
authorize a broader browser category.

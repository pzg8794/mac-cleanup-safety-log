# Repeat Mac Sweep — 2026-10-28

The repeat sweep removed 8,864 old compiler bytecode-cache files after
verifying their cache role, retained source files, inactive owner, age, exact
paths, file identities, content hashes, and ordinary single-link structure.

| Measurement | Result |
|---|---:|
| Ordinary cache files removed | 8,864 |
| Logical bytes removed | 103,067,674 |
| Removed target allocated bytes | 123,478,016 |
| Source files verified present after action | 8,864 |
| Recent cache files preserved | 119 |
| Old entries preserved because source mapping was absent or unavailable | 34,329 |
| Cleanup errors | 0 |
| Observed volume free-space increase around action | 126,767,104 |

The age cutoff was four calendar months before the client date. Modification
time was used only after establishing automatic regeneration; it was not
presented as last-access time or as independent deletion authority. Cache
files whose source had changed remained regenerable from the retained current
source; source contents were not opened or changed.

All exact targets were recorded privately and revalidated before unlinking.
The cache root and all source files remain present. Cache data may be rebuilt
on later imports, with a small initial performance cost. This was permanent
removal of automatically regenerable cache data, not reversible quarantine.

Target allocation and volume free-space movement are recorded separately.
Background writes and APFS accounting prevent attributing the entire observed
volume change to this action.

Other reviews found that the previously known live research-state stores were
empty or absent, old approved log locations were empty, and other download
caches were recent or had active owners. Historical research figures, mixed
temporary-looking exports, source-less cache entries, dependency installations,
and current research evidence remained protected.

Large browser cache-directory totals were recorded by size only. No browser
profile or data was opened or cleaned. Browser-cache review requires a
separate scope decision because earlier browser and recent-cache exclusions
remain active. No operating-system file, snapshot, swap, cloud item, managed
media, personal record, repository history, environment, or dependency
installation was removed. No application was terminated.

The private report, exact manifest, execution source, and verified result are
retained locally as intentional audit evidence. No task-created temporary
directories, downloads, browser tabs, or services remain.

Python's cache behavior is documented in the
[official bytecode-cache reference](https://docs.python.org/3.9/library/sys.html#sys.pycache_prefix).

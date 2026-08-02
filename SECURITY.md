# Security and Privacy Reporting

## Supported version

The current `main` branch receives privacy and validation fixes.

## Report privately

Do not open a public issue if you discover an absolute machine path, account identifier, credential-like string, personal filename, private content hash, raw inventory, or other sensitive detail.

Use GitHub's private vulnerability-reporting feature for this repository. Describe the affected file and the minimum information needed to reproduce the issue. Do not paste the sensitive value into a public issue, discussion, pull request, or commit.

## Response priorities

1. Stop further publication.
2. Determine whether the detail exists only in an unpushed change or in public Git history.
3. Preserve the repository and its history while planning a non-destructive remediation.
4. Rotate any exposed credential outside GitHub when applicable.
5. Add a regression check before resuming publication.

Deleting a file from the current tree does not erase it from Git history. Historical exposure requires a deliberate repository-level response.

---
name: suti-package-check
description: Check that a SUTI module can be transferred, opened, linked, and understood without hidden dependencies.
---

# package check

Use before sharing a module, skill, settings pack, or open release.

1. Inspect the exact package boundary and list every included file.
2. Check rights, privacy, secrets, absolute paths, and dependencies.
3. Check Markdown links and any machine-readable manifest.
4. Open the package from a clean temporary copy with the source vault unavailable.
5. Confirm the entry, one useful action, expected output, and return route.
6. Record `pass`, `partial`, `hold`, `fail`, or `not checked` for each gate.
7. Keep build success separate from publication approval.

Do not silently include private, paid, or uncertain material. Do not publish or upload unless specifically authorized.

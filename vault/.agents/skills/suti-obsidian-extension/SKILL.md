---
name: suti-obsidian-extension
description: Plan or review an Obsidian plugin or theme for a specific SUTI need, with portability, data safety, and maintainability in view.
---

# Obsidian extension

Use only when a real vault task cannot be handled well by Markdown, CSS, or Obsidian core features.

1. State the user problem and compare a note, template, CSS snippet, core feature, and plugin.
2. Prefer the smallest option that works offline and leaves files readable outside Obsidian.
3. For a plugin, inspect the source, license, release history, dependencies, permissions, network behavior, data writes, and uninstall path.
4. Explain that community plugins may access files and the network; do not install or enable one without the user's explicit request for that plugin and vault.
5. If building, use the current official Obsidian developer documentation and sample project; write a narrow feature, document compatibility, and test on a copy of the vault.
6. Provide backup, rollback, and plain-Markdown fallback.

Never treat a directory listing or community scorecard as a complete security audit. Do not upload real vault data to a plugin or test service.

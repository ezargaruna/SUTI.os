# SUTI.os

**A portable, local-first Markdown workspace for language, learning, creative work, and everyday projects.**

SUTI.os can be opened in Obsidian or any Markdown editor. The public package does not require an account, network connection, AI service, or subscription for ordinary offline use.

## Choose a language

- [English entry pack](https://github.com/ezargaruna/SUTI.os/releases/latest/download/SUTI.os-en-entry.zip) — a short English start and core navigation; the full vault is not yet translated into English.
- [Spanish entry pack](https://github.com/ezargaruna/SUTI.os/releases/latest/download/SUTI.os-es-entry.zip) — a short Spanish start and core navigation; the full vault is not yet translated into Spanish.
- [Brazilian Portuguese entry pack](https://github.com/ezargaruna/SUTI.os/releases/latest/download/SUTI.os-pt-BR-entry.zip) — a short Portuguese start and core navigation; the full vault is not yet translated into Portuguese.
- [Full SUTI.os package](https://github.com/ezargaruna/SUTI.os/releases/latest/download/SUTI.os.zip) — the current full vault, whose main content is Russian.

See [language coverage and review status](LANGUAGE_STATUS.md) before choosing a package. A localized entry is not a complete translation of the vault.

## Open without an installer

1. Download a package from the links above.
2. Extract it into a new folder.
3. Open the extracted `vault/` as a separate Obsidian vault, or read the Markdown files directly.
4. Begin with `vault/начать.md` in the full Russian package, or the `start.md` file in a localized entry pack.

Do not extract over an existing vault. On a phone, use the file manager to extract the archive; automated mobile installation has not been verified.

## Optional installer

From the extracted package folder, run:

- macOS or Linux: `python3 install.py`
- Windows PowerShell: `py install.py`

The installer asks up to four questions, creates a new target folder, and stops if that target already exists. It does not read or import other vaults or personal notes. Python is needed only for this installation route; manual extraction does not require it.

To verify package file hashes without installing, run `python3 install.py --verify-only` or `py install.py --verify-only`. The expected hashes are listed in `MANIFEST.sha256`.

## Privacy and reuse

The package contains templates and authored materials, not a user's private archive. It does not automatically upload notes. Share only the specific material you choose, and review it before sending it to an AI service, another person, or a public site.

Vault content and installer code have separate licenses. Read [content terms](LICENSE-CONTENT.md), [code terms](LICENSE-CODE.txt), and the license included with any theme or third-party asset. The SUTI name and marks are not granted automatically.

## Project links

- [SUTI.world](https://suti.world/) — public project entry
- [SUTIcore](https://github.com/ezargaruna/suticore) — shared concepts, site, and system map
- [SUTI.os language editions](language-packs/README.md)
- [Contribution guidance](vault/CONTRIBUTING.md)

## Authorship

Public byline: **Ezar Garuna · Saritama**. SUTI.os is an author-created project. A local vault or written method does not by itself establish clinical, legal, or scientific validation.

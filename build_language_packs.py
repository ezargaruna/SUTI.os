#!/usr/bin/env python3
"""Build small, explicitly partial language-entry archives for SUTI.os."""
from __future__ import annotations

import hashlib
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parent
PACKS = ROOT / "language-packs"
OUT = ROOT / "website" / "downloads"
LOCALES = ("en", "es", "pt-BR")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for locale in LOCALES:
        source = PACKS / locale
        archive = OUT / f"SUTI.os-{locale}-entry.zip"
        with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            zf.write(PACKS / "LICENSE.md", Path(f"SUTI.os-{locale}-entry") / "LICENSE.md")
            for path in sorted(p for p in source.rglob("*") if p.is_file()):
                zf.write(path, Path(f"SUTI.os-{locale}-entry") / path.relative_to(source))
        digest = hashlib.sha256(archive.read_bytes()).hexdigest()
        (OUT / f"SUTI.os-{locale}-entry.zip.sha256").write_text(
            f"{digest}  {archive.name}\n", encoding="ascii"
        )
        print(f"{archive.name}: {archive.stat().st_size} bytes sha256={digest}")


if __name__ == "__main__":
    main()

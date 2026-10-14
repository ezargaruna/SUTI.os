#!/usr/bin/env python3
"""Create a deterministic-ish public zip and checksum from this clean contour."""
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
EXCLUDE_PARTS = {".git", "__pycache__", "dist", ".github", "website"}
EXCLUDE_FILES = {"MANIFEST.sha256"}


def included(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    return not (set(rel.parts) & EXCLUDE_PARTS) and path.name not in EXCLUDE_FILES and path.is_file()


def main() -> None:
    rows = []
    for path in sorted(p for p in ROOT.rglob("*") if included(p)):
        rel = path.relative_to(ROOT).as_posix()
        rows.append((hashlib.sha256(path.read_bytes()).hexdigest(), rel))
    (ROOT / "MANIFEST.sha256").write_text("".join(f"{digest}  {rel}\n" for digest, rel in rows), encoding="utf-8")
    DIST.mkdir(exist_ok=True)
    archive = DIST / "SUTI.os.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(p for p in ROOT.rglob("*") if included(p) or p.name == "MANIFEST.sha256"):
            if not path.is_file() or "dist" in path.relative_to(ROOT).parts:
                continue
            zf.write(path, Path("SUTI.os") / path.relative_to(ROOT))
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    (DIST / "SUTI.os.zip.sha256").write_text(f"{digest}  SUTI.os.zip\n", encoding="ascii")
    print(f"built {archive.name}: {archive.stat().st_size} bytes, {len(rows) + 1} manifest entries, sha256 {digest}")


if __name__ == "__main__":
    main()

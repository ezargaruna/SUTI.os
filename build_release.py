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
    package_path = ROOT / "vault" / "_system" / "open-package.json"
    package = json.loads(package_path.read_text(encoding="utf-8"))
    previous = {row["path"]: row for row in package.get("files", [])}
    package_files = []
    for path in sorted((ROOT / "vault").rglob("*")):
        if not path.is_file() or path.name == "open-package.json":
            continue
        rel = path.relative_to(ROOT / "vault").as_posix()
        old = previous.get(rel, {})
        row = {k: v for k, v in old.items() if k not in {"sha256", "path"}}
        if rel == ".obsidian/snippets/suti-os.css":
            row["license"] = "0BSD"
            row["rights_basis"] = "оригинальный CSS-сниппет SUTI.os"
        row.setdefault("license", "CC-BY-SA-4.0; см. LICENSE.md")
        row.setdefault("rights_basis", "открытый производный пакет; сторонние материалы и личные данные не включены")
        row.update({"path": rel, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
        package_files.append(row)
    package.update({
        "status": "open-content; standalone portable release 0.2.2",
        "version": "0.2.2",
        "file_count": len(package_files) + 1,
        "files": package_files,
        "release_gate": {
            "rights_hold_files": [],
            "external_upload": "authorized for this open derivative by explicit maintainer request",
            "privacy_review": "private source vault excluded; public package reviewed",
            "visual_qa": "pending local package and browser link checks",
            "payment_or_delivery": "not-connected",
        },
        "notes": [
            "This is a public derivative of the open contour, not the private working vault.",
            "Language entry packs are partial; only the Russian base vault is complete.",
            "Personal notes and Plus/Pro packages are excluded.",
            "Licenses cover authored files only, not personal data, marks, third-party material, or user content.",
        ],
    })
    package_path.write_text(json.dumps(package, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    release_path = ROOT / "RELEASE.json"
    release = json.loads(release_path.read_text(encoding="utf-8"))
    release["version"] = "0.2.2"
    release["payload_files"] = sum(1 for p in ROOT.rglob("*") if included(p)) + 1
    release_path.write_text(json.dumps(release, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

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

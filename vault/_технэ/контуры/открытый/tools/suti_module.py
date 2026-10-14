#!/usr/bin/env python3
# SPDX-License-Identifier: 0BSD
"""Preview or safely add one SUTI module to a local Obsidian vault.

Uses Python's standard library only. Default mode is preview; --apply is required
to write. Existing files are never replaced. No network access is used.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import shutil
import sys
import tempfile


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def safe_rel(value: object) -> PurePosixPath:
    if not isinstance(value, str):
        raise ValueError("в списке есть путь без текста")
    p = PurePosixPath(value)
    if p.is_absolute() or not p.parts or ".." in p.parts or "\\" in value:
        raise ValueError(f"небезопасный путь: {value}")
    return p


def plan(package: Path, vault: Path) -> tuple[str, list[tuple[Path, Path, str]]]:
    package = package.expanduser().resolve(strict=True)
    vault = vault.expanduser().resolve(strict=True)
    if not package.is_dir() or not vault.is_dir():
        raise ValueError("пакет и хранилище должны быть папками")
    manifest_path = package / "PACKAGE-MANIFEST.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    module_id = data.get("module_id")
    if not isinstance(module_id, str) or not module_id.replace("-", "").isalnum():
        raise ValueError("в манифесте неверный module_id")
    if data.get("install_mode") != "add-only":
        raise ValueError("этот пакет не заявляет установку без замены файлов")
    files = data.get("files")
    if not isinstance(files, list) or not files:
        raise ValueError("в манифесте нет списка файлов")
    dest_root = vault / "_suti" / "modules" / module_id
    rows = []
    seen = set()
    for row in files:
        rel = safe_rel(row.get("path") if isinstance(row, dict) else None)
        if rel.as_posix() in seen:
            raise ValueError(f"повторный путь в списке: {rel}")
        seen.add(rel.as_posix())
        expected = row.get("sha256")
        if not isinstance(expected, str) or len(expected) != 64:
            raise ValueError(f"нет контрольной суммы: {rel}")
        src = package.joinpath(*rel.parts)
        cursor = package
        has_symlink_component = False
        for part in rel.parts:
            cursor = cursor / part
            has_symlink_component = has_symlink_component or cursor.is_symlink()
        if has_symlink_component or not src.is_file() or package not in src.resolve(strict=True).parents:
            raise ValueError(f"файл отсутствует или выходит за пределы пакета: {rel}")
        if sha256(src) != expected:
            raise ValueError(f"файл изменился после составления списка: {rel}")
        dest = dest_root.joinpath(*rel.parts)
        if dest.exists() or dest.is_symlink():
            raise FileExistsError(f"путь уже занят; файл оставлен без изменений: {dest}")
        parent = dest.parent
        while parent != vault and vault in parent.parents:
            if parent.is_symlink():
                raise ValueError(f"путь назначения содержит символическую ссылку: {parent}")
            parent = parent.parent
        rows.append((src, dest, expected))
    return module_id, rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Добавить пакет SUTI без замены файлов")
    parser.add_argument("--package", required=True, type=Path, help="папка пакета SUTI.plus или SUTI.pro")
    parser.add_argument("--vault", required=True, type=Path, help="папка своего хранилища")
    parser.add_argument("--apply", action="store_true", help="выполнить показанный перенос")
    args = parser.parse_args()
    try:
        module_id, rows = plan(args.package, args.vault)
        print(f"пакет: {module_id}")
        print(f"файлов: {len(rows)}")
        print(f"назначение: _suti/modules/{module_id}/")
        print("режим: добавить только в новое пространство; личные файлы не читаются")
        if not args.apply:
            print("это предварительный просмотр; для записи добавь --apply")
            return 0
        dest_root = rows[0][1]
        for _ in rows[0][1].parents:
            if _.name == module_id:
                dest_root = _
                break
        modules_root = dest_root.parent
        modules_root.mkdir(parents=True, exist_ok=True)
        if dest_root.exists() or dest_root.is_symlink():
            raise FileExistsError(f"папка модуля уже занята: {dest_root}")
        staging = Path(tempfile.mkdtemp(prefix=f".{module_id}.staging-", dir=modules_root))
        try:
            for src, dest, expected in rows:
                relative = dest.relative_to(dest_root)
                staged = staging / relative
                staged.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, staged)
                if sha256(staged) != expected:
                    raise IOError(f"копия не прошла проверку: {relative}")
            staging.rename(dest_root)
        except Exception:
            shutil.rmtree(staging, ignore_errors=True)
            raise
        print("готово: каждый файл сверён по SHA-256")
        print("пакет не запускал плагины, агентов или сетевые действия")
        return 0
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"остановлено: {exc}", file=sys.stderr)
        print("существующие файлы не заменялись", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

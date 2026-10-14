#!/usr/bin/env python3
"""Create a local SUTI.os copy. No network, dependencies, or source-vault reads."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VAULT = ROOT / "vault"

def manifest_rows() -> list[tuple[str, str]]:
    rows = []
    for line in (ROOT / "MANIFEST.sha256").read_text(encoding="utf-8").splitlines():
        digest, rel = line.split("  ", 1)
        rows.append((digest, rel))
    return rows


def verify() -> None:
    for digest, rel in manifest_rows():
        path = ROOT / rel
        if not path.is_file():
            raise SystemExit(f"не найден файл из списка: {rel}")
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != digest:
            raise SystemExit(f"проверка целостности не пройдена: {rel}")


def ask(label: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    answer = input(f"{label}{suffix}: ").strip()
    return answer or default


def safe_name(value: str) -> str:
    value = re.sub(r"\s+", " ", value.strip())
    if not value or value in {".", ".."} or any(c in value for c in "/\\\0"):
        raise SystemExit("название должно быть непустым и без символов / или \\")
    if re.search(r"[<>:\"|?*]", value):
        raise SystemExit("убери из названия символы, запрещённые в именах папок")
    return value


def main() -> None:
    parser = argparse.ArgumentParser(description="локальная установка SUTI.os")
    parser.add_argument("--verify-only", action="store_true", help="только проверить файлы")
    args = parser.parse_args()
    verify()
    if args.verify_only:
        print("проверка целостности пройдена")
        return
    if not sys.stdin.isatty():
        raise SystemExit("запусти установщик в интерактивном терминале")

    print("SUTI.os · настройка копии")
    print("ответы остаются на этом устройстве · всего не более четырёх вопросов\n")
    # 1
    name = safe_name(ask("1/4 · как назвать хранилище?", "SUTI"))
    # 2
    parent = Path(ask("2/4 · куда положить папку?", str(Path.home() / "Documents"))).expanduser()
    target = parent / name
    # 3
    print("\nвыбери стартовый вход: 1 — личный · 2 — язык · 3 — проект/команда")
    focus_choice = ask("3/4 · с чего начать?", "1")
    focus = {"1": "личное", "2": "язык", "3": "проект"}.get(focus_choice)
    if focus is None:
        raise SystemExit("выбери 1, 2 или 3")
    # final confirmation
    print(f"\nимя: {name}\nпапка: {target}\nстартовый вход: {focus}\nсостав: всё открытое хранилище")
    if ask("4/4 · создать новую папку? [да/нет]", "да").lower() not in {"да", "д", "yes", "y"}:
        print("установка отменена · исходные файлы не изменены")
        return
    if target.exists():
        raise SystemExit(f"папка уже существует, ничего не изменено: {target}")
    staged = target.with_name(target.name + ".suti-installing")
    if staged.exists():
        raise SystemExit(f"временная папка уже существует: {staged}")
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(VAULT, staged)
        settings = {
            "format": "suti.local.v1",
            "start_here": focus,
            "included_packs": ["all-open-content"],
            "locale": "ru",
            "network": "not used by installer",
            "source_data_imported": False,
        }
        settings_path = staged / "_настройки" / "локальная настройка.json"
        settings_path.parent.mkdir(parents=True, exist_ok=True)
        settings_path.write_text(json.dumps(settings, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        staged.rename(target)
    except Exception:
        shutil.rmtree(staged, ignore_errors=True)
        raise
    print(f"\nготово: {target}\nоткрой папку как хранилище Obsidian или читай Markdown напрямую")
    print("личные материалы не импортированы · можешь продолжить настройку позже")


if __name__ == "__main__":
    main()

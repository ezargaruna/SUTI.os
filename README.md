# SUTI.os · portable local-first Markdown vault

Russian full edition · short EN, ES, and PT-BR entry packs.

This repository owns the portable vault, local installer, release manifest, and language entry packs. It is separate from [SUTIcore](https://github.com/ezargaruna/suticore), which owns the semantic specifications and canonical SUTI.world source. `website/` is a versioned static snapshot published on this repository's Pages URL; `suti.world` is not configured as this Pages site's domain. Cloudflare origin settings are outside this repository and were not changed. See [repository contours](docs/REPOSITORY_CONTOURS.md) and the [13-language map](language-packs/README.md).

The vault's [symbol guide](vault/%D0%BE%D1%82%D0%BA%D1%80%D1%8B%D1%82%D0%BE%D0%B5/%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%B0/%D0%B7%D0%BD%D0%B0%D0%BA%D0%B8%20%D1%8F%D1%81%D0%BD%D0%BE%D1%81%D1%82%D0%B8.md) is the practical Russian reference; the matching [SUTIcore specification](https://github.com/ezargaruna/suticore/blob/main/app/docs/docs/canon/symbols_reference.md) documents the extended palette and access rules.

## 2026-11-13 · selected common-system review drafts

- [new common operating layer · thirteen routes](releases/2026-11-13/living-system/README.md)
- [separate system guide · thirteen draft editions](releases/2026-11-13/system-guide-13l/README.md)
- [download sets, hashes and publication scope](releases/2026-11-13/README.md)
- planned website entries: [system](https://ezargaruna.github.io/suticore/system/) · [AI system guide](https://ezargaruna.github.io/suticore/modules/ai-soul-13l/)

These selected author-owned drafts are prepared for public review by the owner's current request. They do not replace the existing stable vault or imply that the full legacy corpus is translated. Native review, fund/financial/participant operations and runtime remain separate gates. The existing CC BY-SA/MIT scopes are not silently extended to the new releases; see the [release notice](releases/2026-11-13/NOTICE.md).

## быстрый вход

- [атлас заботы](https://ezargaruna.github.io/suticore/care-atlas.html) · [Verenium с SUTI.os для работы без сети](https://ezargaruna.github.io/suticore/downloads/Verenium.zip)
- [выбрать язык и открыть SUTI.world](https://suti.world/)
- [скачать полный русский vault](https://github.com/ezargaruna/SUTI.os/releases/latest/download/SUTI.os.zip)
- [статус всех 13 языковых слоёв](language-packs/README.md)

## русское руководство

переносимое Markdown-хранилище для личной жизни, языка, обучения, творчества и дел. работает в Obsidian или любом редакторе Markdown; пользоваться можно без аккаунта, сети, ИИ и платной подписки.

## скачать и открыть без терминала

1. скачай [последний архив](https://github.com/ezargaruna/SUTI.os/releases/latest/download/SUTI.os.zip)
2. распакуй его
3. открой папку `SUTI.os/vault` как отдельное хранилище Obsidian или читай Markdown напрямую
4. начни с `vault/начать.md`

не копируй поверх уже существующего хранилища. если хочешь переименовать папку, сделай это после распаковки.

## установить с короткой настройкой

из папки распакованного пакета выполни:

- macOS или Linux: `python3 install.py`
- Windows PowerShell: `py install.py`

имя созданной папки по умолчанию — `SUTI.os`. в первом вопросе можно оставить это имя или ввести `SUTI.%username%`: установщик подставит имя текущей учётной записи только на этом устройстве. можно также ввести собственный вариант после `SUTI.`. папка с таким именем не будет перезаписана.

ответь на четыре коротких вопроса: имя копии, место, стартовый вход и подтверждение. установщик работает локально, не требует учётной записи, сети, прав администратора или сторонних библиотек. он не читает другие хранилища, не переносит личные записи и остановится, если целевая папка уже существует.

Python нужен только для этого способа. обычный путь — распаковать архив и открыть `vault` вручную. на телефоне используй ручную распаковку; автоматическая мобильная установка не проверялась.

## проверка целостности

в корне пакета выполни `python3 install.py --verify-only` или `py install.py --verify-only`. проверка сверяет SHA-256 и ничего не устанавливает. список файлов находится в `MANIFEST.sha256`.

## вход и глубина

`vault/начать.md` ведёт к короткому маршруту. карта «поле своих» соединяет человека и ситуацию, собственные слова и следующий шаг. игру можно пропустить. язэхъ сохранён отдельно как авторский эксперимент в «белом кубе SUTI».

личные заметки не отправляются автоматически. пустые шаблоны не являются профилем. данные остаются на выбранном устройстве, пока ты сам не решишь иначе. передавай помощнику только выбранные фрагменты.

## лицензии и границы

оригинальные тексты и пустые формы в `vault/` распространяются по CC BY-SA 4.0; установочный код — MIT. см. `LICENSE-CONTENT.md` и `LICENSE-CODE.txt`. лицензия не передаёт права на имя, знаки или товарные марки SUTI и не распространяется автоматически на сторонние материалы или пользовательские записи.

авторство открытых материалов: **Ezar Garuna** · [SUTI.world](https://suti.world)


оформление Obsidian заранее включено в чистую копию. CSS распространяется по 0BSD, лицензия находится рядом со сниппетом.

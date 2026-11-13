#!/usr/bin/env python3
"""Build a self-contained, dependency-free local viewer for the 13 guide editions.

This renders a small, escaped Markdown subset. It performs no network requests,
does not execute source HTML, and does not add storage or runtime connections.
Run after guide edits: python3 tools/build_viewer.py
"""
from pathlib import Path
from urllib.parse import unquote
import html
import json
import re

PACKAGE = Path(__file__).resolve().parents[1]
LOCALES = ["ru", "en", "es", "pt-br", "zh-hans", "hi", "fr", "ar", "bn", "eo", "sa", "la", "yzh"]
LANG_TAGS = {"pt-br": "pt-BR", "zh-hans": "zh-Hans", "yzh": "und"}
MACHINE_LINKS = {
    "ai-soul-system-contour.v1.json": "machine/contract.json",
    "contract.json": "machine/contract.json",
    "ai-soul-system-contour.v1.schema.json": "machine/envelope.schema.json",
    "envelope.schema.json": "machine/envelope.schema.json",
    "configuration.schema.json": "machine/configuration.schema.json",
    "default-configuration.json": "machine/default-configuration.json",
    "example-envelope.json": "machine/example-envelope.json",
}
ESC = html.escape
BT = chr(96)
INLINE = re.compile(
    re.escape(BT) + r"([^" + re.escape(BT) + r"]+)" + re.escape(BT)
    + r"|\[([^\]]+)\]\(([^)]+)\)"
    + r"|\*\*([^*]+)\*\*"
    + r"|(?<!\*)\*([^*\n]+)\*(?!\*)"
)
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
ORDERED = re.compile(r"^\s*(\d+)[.)]\s+(.+)$")
UNORDERED = re.compile(r"^\s*[-+*]\s+(.+)$")


def local_target(target, guide, package=PACKAGE):
    """Return a package-local link, remapping canonical machine aliases."""
    raw = unquote(target.strip())
    if not raw or any(ord(ch) < 32 for ch in raw):
        return None
    if raw.startswith("#"):
        return raw
    if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", raw) or raw.startswith(("/", "\\")):
        return None
    path_part, sep, anchor = raw.partition("#")
    basename = Path(path_part).name
    if basename in MACHINE_LINKS:
        resolved = MACHINE_LINKS[basename]
        return resolved + (("#" + anchor) if sep else "")
    resolved = (guide.parent / path_part).resolve()
    try:
        relative = resolved.relative_to(package.resolve()).as_posix()
    except ValueError:
        return None
    if not resolved.exists():
        return None
    return relative + (("#" + anchor) if sep else "")


def inline(text, guide, package=PACKAGE):
    """Escape source text before emitting a few safe inline elements."""
    result = []
    at = 0
    for match in INLINE.finditer(text):
        result.append(ESC(text[at:match.start()]))
        code, label, target, strong, emphasis = match.groups()
        if code is not None:
            result.append('<code dir="ltr">' + ESC(code) + "</code>")
        elif label is not None:
            href = local_target(target, guide, package)
            if href:
                result.append('<a href="' + ESC(href, quote=True) + '">' + ESC(label) + "</a>")
            else:
                result.append(ESC(label) + ' <span class="plain-target">(' + ESC(target) + ")</span>")
        elif strong is not None:
            result.append("<strong>" + ESC(strong) + "</strong>")
        else:
            result.append("<em>" + ESC(emphasis) + "</em>")
        at = match.end()
    result.append(ESC(text[at:]))
    return "".join(result)


def cells(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [value.strip().replace(r"\|", "|") for value in re.split(r"(?<!\\)\|", line)]


def is_separator(line):
    values = cells(line)
    return bool(values) and all(re.fullmatch(r":?-{3,}:?", value.replace(" ", "")) for value in values)


def prepare_markdown(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    if text.startswith("---\n"):
        split = text.find("\n---", 4)
        if split >= 0:
            text = text[split + 4:].lstrip("\n")
    text = re.sub(r"<!--\s*suti:section:[a-z-]+\s*-->", "", text)
    # The viewer supplies trusted lang/dir attributes itself. Source HTML is never executed.
    text = re.sub(r"^\s*<div\s+(?=[^>]*\bdir=)[^>]*>\s*$", "", text, flags=re.M)
    text = re.sub(r"^\s*</div>\s*$", "", text, flags=re.M)
    return text


def render_markdown(text, guide, package=PACKAGE):
    lines = prepare_markdown(text).splitlines()
    blocks = []
    i = 0
    fence = BT * 3
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.lstrip().startswith(fence):
            values = []
            i += 1
            while i < len(lines) and not lines[i].lstrip().startswith(fence):
                values.append(lines[i])
                i += 1
            i += i < len(lines)
            blocks.append('<pre dir="ltr"><code>' + ESC("\n".join(values)) + "</code></pre>")
            continue
        heading = HEADING.match(line)
        if heading:
            level = len(heading[1])
            blocks.append("<h" + str(level) + ">" + inline(heading[2], guide, package) + "</h" + str(level) + ">")
            i += 1
            continue
        if re.fullmatch(r"\s*(?:-{3,}|\*{3,}|_{3,})\s*", line):
            blocks.append("<hr>")
            i += 1
            continue
        if i + 1 < len(lines) and "|" in line and is_separator(lines[i + 1]):
            headers = cells(line)
            align_cells = cells(lines[i + 1])
            table = ['<div class="table-scroll" tabindex="0" role="region" aria-label="' + ESC(headers[0], quote=True) + '"><table><thead><tr>']
            table.extend("<th scope=\"col\">" + inline(value, guide, package) + "</th>" for value in headers)
            table.append("</tr></thead><tbody>")
            i += 2
            while i < len(lines) and "|" in lines[i] and lines[i].strip():
                row = cells(lines[i])
                row = (row + [""] * len(headers))[:len(headers)]
                table.append("<tr>" + "".join("<td>" + inline(value, guide, package) + "</td>" for value in row) + "</tr>")
                i += 1
            table.append("</tbody></table></div>")
            blocks.append("".join(table))
            continue
        ordered = ORDERED.match(line)
        unordered = UNORDERED.match(line)
        if ordered or unordered:
            tag = "ol" if ordered else "ul"
            pattern = ORDERED if ordered else UNORDERED
            items = []
            while i < len(lines):
                item = pattern.match(lines[i])
                if not item:
                    break
                value = item[2] if ordered else item[1]
                items.append("<li>" + inline(value, guide, package) + "</li>")
                i += 1
            blocks.append("<" + tag + ">" + "".join(items) + "</" + tag + ">")
            continue
        if line.startswith(">"):
            values = []
            while i < len(lines) and lines[i].startswith(">"):
                values.append(lines[i][1:].lstrip())
                i += 1
            blocks.append("<blockquote>" + "<br>".join(inline(value, guide, package) for value in values) + "</blockquote>")
            continue
        paragraph = [line]
        i += 1
        while i < len(lines) and lines[i].strip():
            upcoming = lines[i]
            if HEADING.match(upcoming) or ORDERED.match(upcoming) or UNORDERED.match(upcoming) or upcoming.startswith(">") or re.fullmatch(r"\s*-{3,}\s*", upcoming):
                break
            if i + 1 < len(lines) and "|" in upcoming and is_separator(lines[i + 1]):
                break
            paragraph.append(upcoming)
            i += 1
        blocks.append("<p>" + "<br>".join(inline(value, guide, package) for value in paragraph) + "</p>")
    return "\n".join(blocks)


CSS = """
:root{color-scheme:light;--paper:#f4f6f2;--surface:#fffefa;--ink:#183b38;--muted:#506a65;--line:#cfddd5;--accent:#176f68;--soft:#e3f0e9}
*{box-sizing:border-box}html{scroll-behavior:auto}body{margin:0;background:var(--paper);color:var(--ink);font:1rem/1.7 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
a{color:var(--accent);text-underline-offset:.18em;overflow-wrap:anywhere}button,select{font:inherit}button,a,select,summary{touch-action:manipulation}
:focus-visible{outline:3px solid #a04c12;outline-offset:4px}
.shell{max-width:72rem;margin:auto;padding:1.25rem}header,.controls,.guide,.machine-panel,footer{background:var(--surface);border:1px solid var(--line);border-radius:1.1rem}
header{padding:clamp(1.3rem,4vw,2.6rem);margin-block-end:1rem}.brand{font-size:.85rem;letter-spacing:.05em;color:var(--muted);margin:0}h1,h2,h3{line-height:1.28;overflow-wrap:anywhere}header h1{font-size:clamp(1.6rem,5vw,2.5rem);margin:.45rem 0 1rem}.intro{max-width:55ch;color:var(--muted);margin:0}
.controls{padding:1rem;display:flex;gap:.8rem;align-items:center;flex-wrap:wrap;margin-block-end:1rem}.field{display:flex;gap:.6rem;align-items:center;flex-wrap:wrap}select{max-width:100%;padding:.5rem .7rem;border:1px solid var(--accent);border-radius:.5rem;background:#fff;color:var(--ink)}.badge{font-size:.88rem;padding:.3rem .7rem;border-radius:2rem;background:var(--soft);color:var(--ink)}.source{margin-inline-start:auto}
.guide{padding:clamp(1.15rem,4.5vw,3rem);max-width:58rem;margin-inline:auto;margin-block-end:1rem}.guide h1{font-size:clamp(1.6rem,4vw,2.2rem)}.guide h2{font-size:1.35rem;margin-block-start:2.3rem;padding-block-start:1.2rem;border-block-start:1px solid var(--line)}.guide p,.guide li{max-width:78ch}.guide blockquote{margin:1.4rem 0;padding:.7rem 1.1rem;border-inline-start:.25rem solid var(--accent);background:var(--soft)}.guide ol,.guide ul{padding-inline-start:1.6rem}.guide li+li{margin-block-start:.45rem}
code,pre,textarea{direction:ltr;unicode-bidi:plaintext;text-align:left;font-family:ui-monospace,SFMono-Regular,Consolas,monospace}code{font-size:.88em;background:var(--soft);padding:.1em .25em;border-radius:.25em;overflow-wrap:anywhere}pre{overflow-x:auto;padding:1rem;background:var(--soft);border-radius:.6rem}pre code{padding:0;background:transparent}.table-scroll{overflow-x:auto;max-width:100%;margin-block:1.2rem}table{border-collapse:collapse;width:100%;min-width:34rem;font-size:.94rem}th,td{text-align:start;padding:.7rem .8rem;border:1px solid var(--line);vertical-align:top}th{background:var(--soft)}.plain-target{font-size:.88em;overflow-wrap:anywhere;color:var(--muted)}hr{border:0;border-block-start:1px solid var(--line);margin:2rem 0}
.machine-panel{padding:1.3rem;margin-block:1rem}.machine-panel h2{font-size:1.3rem;margin-block-start:0}.downloads{display:flex;gap:.7rem 1.1rem;flex-wrap:wrap}.copy-row{display:flex;gap:.8rem;align-items:center;flex-wrap:wrap;margin-block-start:1rem}button{background:var(--accent);color:#fff;border:0;border-radius:.55rem;padding:.6rem .9rem;cursor:pointer}.copy-status{color:var(--muted);font-size:.9rem;min-height:1.5em}textarea{display:block;min-height:15rem;width:100%;resize:vertical;margin-block-start:1rem;border:1px solid var(--line);border-radius:.6rem;padding:1rem;background:#fff;color:var(--ink);font-size:.85rem}details{margin-block-start:1rem}summary{cursor:pointer;color:var(--accent)}footer{padding:1rem 1.3rem;font-size:.9rem;color:var(--muted)}
.skip-link{position:absolute;inset-inline-start:1rem;top:-8rem;background:#fff;padding:.7rem;z-index:10}.skip-link:focus{top:1rem}
@media(max-width:38rem){.shell{padding:.65rem}.source{margin-inline-start:0}.controls{align-items:flex-start;flex-direction:column}.guide{border-radius:.7rem}.machine-panel{padding:1rem}}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}}
@media print{body{background:#fff}.controls,.machine-panel,.skip-link{display:none}.shell{padding:0}.guide,header,footer{border:0;padding:.5rem}a{color:inherit}.guide h2{break-after:avoid}.table-scroll{overflow:visible}table{min-width:0}footer{margin-block-start:1rem}}
"""


JS = """
(function () {
  "use strict";
  var data = JSON.parse(document.getElementById("viewer-data").textContent);
  var selector = document.getElementById("locale");
  var article = document.getElementById("guide");
  var ui = data.ui;
  var current = "ru";
  data.locales.forEach(function (locale) {
    var option = document.createElement("option");
    option.value = locale;
    option.textContent = ui[locale].label;
    selector.appendChild(option);
  });
  function text(id, value) { document.getElementById(id).textContent = value; }
  function normalizeLocale(value) {
    if (typeof value !== "string") { return null; }
    var key = value.trim().toLowerCase();
    if (key === "es-419") { key = "es"; }
    return Object.prototype.hasOwnProperty.call(ui, key) ? key : null;
  }
  function updateLocation(locale) {
    try {
      var url = new URL(window.location.href);
      url.searchParams.set("lang", locale);
      window.history.replaceState(null, "", url.href);
    } catch (error) {
      // Some offline hosts restrict history updates. Reading still works.
    }
  }
  function show(locale, updateUrl, fallbackUsed) {
    if (!Object.prototype.hasOwnProperty.call(ui, locale)) { locale = "ru"; }
    current = locale;
    var labels = ui[locale];
    var rtl = locale === "ar";
    document.documentElement.lang = data.tags[locale] || locale;
    document.documentElement.dir = rtl ? "rtl" : "ltr";
    document.title = labels.title + " · SUTI";
    article.lang = data.tags[locale] || locale;
    article.dir = rtl ? "rtl" : "ltr";
    article.innerHTML = data.guides[locale];
    selector.value = locale;
    text("page-title", labels.title);
    text("intro", labels.subtitle);
    text("language-label", labels.language);\n    document.getElementById("language-controls").setAttribute("aria-label", labels.language);
    text("draft-status", labels.draft);
    text("source-guide", labels.openGuide);
    document.getElementById("source-guide").href = "locales/" + locale + "/guide.md";
    text("machine-title", labels.machineFiles);
    text("contract-link", labels.downloadContract);
    text("schema-link", labels.downloadSchema);
    text("config-link", labels.downloadConfig);
    text("copy-config", labels.copyConfig);
    text("show-config", labels.showConfig);
    text("privacy", labels.privacy);
    text("skip", labels.skip);
    text("copy-status", "");
    var configField = document.getElementById("config-text");
    configField.setAttribute("aria-label", labels.downloadConfig);
    configField.value = data.configurations[locale];
    var configLink = document.getElementById("config-link");
    configLink.href = "machine/configurations/" + locale + ".json";
    configLink.download = "SUTI-configuration-" + locale + ".json";
    var fallback = document.getElementById("fallback-notice");
    fallback.hidden = !fallbackUsed;
    fallback.textContent = fallbackUsed ? labels.fallback : "";
    if (updateUrl) { updateLocation(locale); }
  }
  selector.addEventListener("change", function () { show(selector.value, true, false); });
  document.getElementById("config-link").addEventListener("click", function (event) {
    if (typeof Blob !== "function" || typeof URL.createObjectURL !== "function") { return; }
    event.preventDefault();
    var blob = new Blob([document.getElementById("config-text").value + "\\n"], { type: "application/json;charset=utf-8" });
    var objectUrl = URL.createObjectURL(blob);
    var link = document.createElement("a");
    link.href = objectUrl;
    link.download = "SUTI-configuration-" + current + ".json";
    link.hidden = true;
    document.body.appendChild(link);
    link.click();
    window.setTimeout(function () { URL.revokeObjectURL(objectUrl); link.remove(); }, 1000);
  });
  document.getElementById("copy-config").addEventListener("click", function () {
    var field = document.getElementById("config-text");
    var state = document.getElementById("config-details");
    var copyLocale = current;
    var copyValue = field.value;
    state.open = true;
    function fallback() {
      if (current !== copyLocale) { return; }
      field.focus();
      field.select();
      var copied = false;
      try { copied = document.execCommand("copy"); } catch (error) { copied = false; }
      text("copy-status", copied ? ui[current].copied : ui[current].manualCopy);
    }
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(copyValue).then(function () {
        if (current === copyLocale) { text("copy-status", ui[current].copied); }
      }, fallback);
    } else { fallback(); }
  });
  function showRequestedLocale() {
    var requested = new URLSearchParams(window.location.search).get("lang");
    var locale = normalizeLocale(requested);
    show(locale || "ru", false, Boolean(requested && !locale));
  }
  window.addEventListener("popstate", showRequestedLocale);
  showRequestedLocale();
}());
"""


def main():
    ui = json.loads((Path(__file__).parent / "ui-locales.json").read_text(encoding="utf-8"))
    if sorted(ui) != sorted(LOCALES):
        raise ValueError("UI labels must cover exactly the 13 declared locales")
    required_ui_keys = set(ui["ru"])
    for locale in LOCALES:
        if set(ui[locale]) != required_ui_keys or any(not isinstance(value, str) or not value.strip() for value in ui[locale].values()):
            raise ValueError("UI labels are incomplete for locale: " + locale)
    guides = {}
    for locale in LOCALES:
        guide = PACKAGE / "locales" / locale / "guide.md"
        guides[locale] = render_markdown(guide.read_text(encoding="utf-8"), guide)
    configurations = {}
    for locale in LOCALES:
        config_path = PACKAGE / "machine/configurations" / (locale + ".json")
        configuration = json.loads(config_path.read_text(encoding="utf-8"))
        if configuration.get("locale") != locale:
            raise ValueError("Configuration locale does not match its declared route: " + locale)
        configurations[locale] = json.dumps(configuration, ensure_ascii=False, indent=2)
    payload = json.dumps({"locales": LOCALES, "tags": LANG_TAGS, "ui": ui, "guides": guides, "configurations": configurations}, ensure_ascii=False)
    payload = payload.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    ru = ui["ru"]
    page = '''<!doctype html>
<html lang="ru" dir="ltr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; script-src 'unsafe-inline'; connect-src 'none'; img-src 'none'; font-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'">
<title>@@TITLE@@ · SUTI</title><style>@@CSS@@</style></head>
<body><a id="skip" class="skip-link" href="#guide">@@SKIP@@</a>
<div class="shell"><header><p class="brand">SUTI.world · synaura × Syntaxium · 1.1.0-draft</p><h1 id="page-title">@@TITLE@@</h1><p id="intro" class="intro">@@INTRO@@</p></header>
<nav id="language-controls" class="controls" aria-label="@@LANGUAGE@@"><div class="field"><label id="language-label" for="locale">@@LANGUAGE@@</label><select id="locale"></select></div><span id="draft-status" class="badge">@@DRAFT@@</span><a id="source-guide" class="source" href="locales/ru/guide.md">@@SOURCE@@</a><span id="fallback-notice" class="copy-status" role="status" hidden></span></nav>
<main><article id="guide" class="guide" tabindex="-1">@@GUIDE@@</article>
<section class="machine-panel" aria-labelledby="machine-title"><h2 id="machine-title">@@MACHINE@@</h2>
<div class="downloads"><a id="contract-link" href="machine/contract.json" download>@@CONTRACT@@</a><a id="schema-link" href="machine/envelope.schema.json" download>@@SCHEMA@@</a><a id="config-link" href="machine/default-configuration.json" download>@@CONFIG@@</a></div>
<div class="copy-row"><button id="copy-config" type="button">@@COPY@@</button><span id="copy-status" class="copy-status" role="status" aria-live="polite"></span></div>
<details id="config-details"><summary id="show-config">@@SHOW@@</summary><textarea id="config-text" readonly aria-label="@@CONFIG@@"></textarea></details></section></main>
<footer><span id="privacy">@@PRIVACY@@</span></footer></div>
<script id="viewer-data" type="application/json">@@DATA@@</script><script>@@JS@@</script></body></html>
'''
    tokens = {
        "TITLE": ESC(ru["title"]), "SKIP": ESC(ru["skip"]),
        "INTRO": ESC(ru["subtitle"]), "LANGUAGE": ESC(ru["language"], quote=True),
        "DRAFT": ESC(ru["draft"]), "SOURCE": ESC(ru["openGuide"]),
        "MACHINE": ESC(ru["machineFiles"]), "CONTRACT": ESC(ru["downloadContract"]),
        "SCHEMA": ESC(ru["downloadSchema"]), "CONFIG": ESC(ru["downloadConfig"], quote=True),
        "COPY": ESC(ru["copyConfig"]), "SHOW": ESC(ru["showConfig"]),
        "PRIVACY": ESC(ru["privacy"]), "GUIDE": guides["ru"],
        "CSS": CSS, "DATA": payload, "JS": JS,
    }
    for key, value in tokens.items():
        page = page.replace("@@" + key + "@@", value)
    output = PACKAGE / "index.html"
    output.write_text(page, encoding="utf-8")
    print("Built", output.name, "with", len(guides), "full locale guides; no network/storage dependencies")


if __name__ == "__main__":
    main()

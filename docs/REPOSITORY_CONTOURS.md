# Public repository contours

**id:** `suti.os.repository-contours.v1`  
**state:** public boundary note · 2026-11-04

## SUTI.os owns

- the portable Markdown vault and its release manifest;
- the local installer and package integrity list;
- the full Russian vault and partial EN, ES, and PT-BR entry packs;
- status and navigation for all 13 language layers.

SUTI.os does not own the canonical semantic specifications or SUTI.world site source. Those belong in [suticore](https://github.com/ezargaruna/suticore). The `website/` tree here is a versioned static snapshot; do not treat it as the source for site copy or sync it automatically with the other repository.

## Shared boundaries

| topic | rule |
|---|---|
| personal data | never copy user notes, private vaults, credentials, or third-party records into public releases |
| language | 13 identifiers are available for navigation; only RU has a full vault, EN/ES/PT-BR have partial entry packs, and nine locales have no archive |
| translation status | a menu item or fallback is not a completed transcreation; preserve the explicit review state in [`manifest.json`](../language-packs/manifest.json) |
| licenses | check the content, code, and asset license for each artifact; the repository description is not a blanket license |
| release | the versioned manifest and exact release artifacts define the package; local edits alone do not change a release |

## Hosting state · HOLD

The intended architecture assigns the canonical website source to `suticore`. Current GitHub Pages settings still list `suti.world` as the custom domain for this repository, and this repository's Pages workflow publishes `website/`. `suticore` has a separate Pages workflow. This overlap has not been reconciled.

No custom-domain setting is changed by this file. Before any transfer, verify DNS/CDN routing, the destination Pages build, and rollback. Keep this repository's `website/` as a clearly versioned snapshot until the route is reviewed.

## Review questions

Use these as a written Veche review, not an autonomous vote:

1. Does each repository contain only files that its role owns?
2. Does each language link reveal the real translation and package status?
3. Can a visitor choose a fallback, leave, or use the Russian full vault without sharing personal data?
4. Are rights, provenance, runtime, and hosting claims supported by the corresponding repository or release?

Record disagreements and missing evidence as `UNKNOWN` or `HOLD`.

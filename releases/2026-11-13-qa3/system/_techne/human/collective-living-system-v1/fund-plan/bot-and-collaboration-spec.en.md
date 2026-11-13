---
artifact_id: suti.bot-collaboration-spec.en.2026-11-13
source_path: bot-and-collaboration-spec.ru.md
source_locale: ru
source_sha256: 76509088c1554bb71008e7076afc0683bd2669b57b26bd0535a6b8bab19e2ffe
source_version: 2026-11-13
locale: en
audience: adult readers, content editors and technical implementers
purpose: full direct-source editorial draft of the care bot and collaboration specification
visibility: public-safe-content / local-review-only
rights_status: authorial draft / reuse terms unassigned / RELEASE_HOLD
transcreation_status: draft
format_profile: synaura quiet luxury / native orthography / Markdown
review_scope: all 12 sections, tables, technical anchors and 18 acceptance requirements
reviewer_status: model-assisted draft / independent native and technical review pending
open_questions: independent meaning and native review; accessibility; owner acceptance; implementation tests
updated_at: 2026-11-13
implementation: specification-only
acceptance_execution: NOT_RUN
release: HOLD
---

# care bot × SUTI collaborative architecture

purpose :: give a person a clear, voluntary entry into knowledge, practice, a shared project and a possible next step
state :: specification-only · this document does not create an implementation
source language :: ru
locale :: en
date :: 2026-11-13
operational connections / Telegram runtime / participant intake / payments / publication :: OFF / HOLD
source :: [Russian master](bot-and-collaboration-spec.ru.md)

This specification describes a proposed local content engine and bot adapter for the common living SUTI system. A person voluntarily enables the image of an angel of care, urban shaman or samurai of dharma. Every imaginative route has an equally available plain-language formulation. The bot helps find, express and check a next step; authorized people make final decisions about support, grants, complaints, a person's role and expenditure.

<!-- suti:section:expected-first-result -->
## expected first result

The person chooses a language → reads the offer and current limitations → chooses a question or an existing topic → receives a short card with a source and a possible action → saves it for themselves or ends the route. Reading open materials requires neither a profile nor registration. Pause, skip, return and exit are available on every screen. Name, date of birth, health, documents, finances, family circumstances and private history are not requested by default.

The minimum version consists of a local knowledge catalogue, 13 language routes, search across published cards, a voluntary NITYA quest and export of one's own bookmarks. A working messenger integration, storage of user messages, an AI service, a community group, a financial module and grant intake are not automatically part of this minimum.

<!-- suti:section:user-routes -->
## user routes

| route | person's action | result | required boundary |
|---|---|---|---|
| understand the system | choose a short overview or contour | clear purpose and next route | current maturity is visible |
| find material | choose a topic or local search | card, source, language and state | results contain only the permitted public catalogue |
| microlearning | choose a short practice | one manageable step and an optional check | no punishment for skipping, breaking a streak or leaving |
| fusion map | choose an empty template | one's own editable file | completed locally; sending it to anyone is a separate choice |
| NITYA game | explicitly enable the imaginative interface | voluntary quest with a plain-text equivalent | no assigned identity or ranking of a person's worth |
| shared contribution | open the rules and propose public material | draft for human consideration | authors' rights, audience and licence are clarified before inclusion |
| human assistance | read the team's availability and limits | a chosen contact route, if it actually exists | competence, schedule and responsible person are confirmed; unavailable support is not promised |
| fund | read the project and the state of its conditions | plan, criteria and aggregate information | accepting money and applications stays disabled until separately authorized |

The age labels 0+, 12+, 18+, 21+, 33+ and 55+ are editorial views, not legal age verification or official ratings. Child and youth intake stays disabled until verified safeguarding is in place. It is enough to offer a person their chosen difficulty mode; do not collect an exact date of birth to adjust language or pace.

<!-- suti:section:proposed-architecture -->
## components of the proposed architecture

```text
public catalogue in .vault
    ↓ check source, rights, privacy and language
deterministic public-package builder
    ↓ allowlist + manifest + SHA-256
local read-only content engine
    ├─ Obsidian / Markdown
    ├─ accessible local HTML
    └─ optional bot adapter
          ↓ separately authorized runtime only
       user session / actions they have accepted
          ↓ separate consent and minimization
       user's private space outside the public catalogue
```

1. **Content catalogue.** Stable `entity_id`, source, invariant meaning, scope, limits, rights, maturity and relations. The public package does not list private paths, contacts or people's original stories.
2. **Language layer.** One identified master per object and direct editions for each locale. An unreviewed translation is never silently substituted as ready-to-use text.
3. **Router.** Deterministic commands, contours and cards. The first version needs no generative model. The response contains a clear, available step and an explicit state.
4. **Session.** Short-lived state of the current screen. By default it stays in process memory or with the user, rather than in a collective public database.
5. **Adapter.** Telegram or another channel is connected separately; secrets stay outside `.vault`, the source of updates is verified and optional events are disabled. A technical transport ID is treated as a personal identifier and does not enter the public package or ordinary logs.
6. **Private storage.** If a person chooses to save, data goes into a separate private space with an owner, restricted access, a retention period and tested deletion. A physical boundary differs from a folder inside a public vault.
7. **Editorial queue.** Contributions, objections, corrections and complaints receive restricted access, an assigned person and a state. The public record displays only an approved aggregate decision.
8. **Release check.** Before including a file, check the allowlist, rights, privacy, source, supported format, links, locale and SHA. An error stops the build of that particular release.

This diagram defines interfaces, not the existence of code. Implementation is selected after checking the existing project, team support, deployment requirements and local storage.

<!-- suti:section:locales-content-loading -->
## 13 locales and content loading

locales :: `ru`, `en`, `es`, `pt-br`, `zh-hans`, `hi`, `fr`, `ar`, `bn`, `eo`, `sa`, `la`, `yzh`

Proposed public-package structure:

```text
catalog/entities.json
catalog/relations.json
locales/<locale>/interface.json
locales/<locale>/cards/<entity_id>.md
locales/<locale>/glossary.json
manifests/content.json
manifests/locale-review.json
schemas/                  # technical contracts
```

`content.json` explicitly lists files, sizes, SHA-256, canon version and permitted locales. Language state is separate from file presence: `not-started`, `draft`, `meaning-reviewed`, `native-or-expert-reviewed`, `release-approved`. These are proposed enum values for a new contract; they do not rewrite historical registries without a separate migration.

On locale selection, the engine checks whether the card is available and whether its state is allowed for the selected mode. If text is missing, it explains this in the interface language and offers an informed choice of an available language. Substituting Russian or English for an empty locale without disclosure is prohibited. When the master changes, dependent editions are marked as versions needing reconciliation; an old SHA does not verify a new meaning.

The Arabic interface uses `dir="rtl"` and a separate check of reading, tables, numbers and mixed identifiers. Sanskrit and Latin require specialists; YZH requires an author-approved gloss with an expanded explanation and a comprehension check. Until that evidence exists, the locale receives an honest HOLD. A textual version of the meaning is available without animation, colour or special symbols.

<!-- suti:section:proposed-commands -->
## proposed commands

Command IDs are not translated; visible labels are localized. The commands are an API proposal, not evidence of a connected bot.

| command | result |
|---|---|
| `/start` | offer, language and current availability; no questionnaire |
| `/language` | explicit language selection and visible gaps |
| `/contours` | 13 contours with short purposes |
| `/learn` | short lesson and voluntary action |
| `/quest` | separately enable the voluntary game |
| `/map` | empty editable fusion-map template |
| `/sources` | provenance of the current public card |
| `/pause` | stop the current route and notifications within the service's authority |
| `/resume` | explicit resumption; no new consent is enabled |
| `/export` | one's own saved data after ownership verification |
| `/delete` | clear deletion scope and owner confirmation |
| `/privacy` | operator, purpose, retention, access, rights and contact, if approved |
| `/help` | accessible ordinary navigation and actual limits of assistance |
| `/exit` | end the session; explain any separately chosen saving |

Automatic broadcasts and daily tasks are disabled by default. A subscription has a purpose, frequency, local time and an easy unsubscribe option. A single `/start` does not mean subscribing, AI processing, joining a community or consenting to publication.

<!-- suti:section:data-ownership -->
## data and ownership

| entity | minimum fields | location and access | retention |
|---|---|---|---|
| `PublicEntity` | `entity_id`, `source_id`, `version`, `kind`, `contour_id`, `license_state`, `implementation_state` | verified public package | according to the adopted version policy |
| `LocalizedArtifact` | `entity_id`, `locale`, `source_sha256`, `target_sha256`, `review_state`, `release_state` | public text and public-safe supporting evidence | until replacement, with provenance retained outside the active package |
| `Relation` | `from_id`, `to_id`, `relation_type`, `evidence_ref` | public catalogue | according to catalogue version |
| `Session` | random `session_id`, locale, screen, pause state | memory or private storage; session owner and process only | minimum period; a specific TTL is approved and tested before runtime |
| `TransportBinding` | technical channel identifier and link to a private session | separate restricted storage; not public logs | duration justified for the chosen channel; deletion follows the scenario |
| `SavedItem` | `owner_id`, `entity_id`, person's annotation, time | with the user by default; server saving requires a separate opt-in | chosen period; correction, export and deletion |
| `ConsentRecord` | purpose, explanation version, scope, choice, time and withdrawal | separate private storage | according to the applicable obligation; no indefinite perpetual period |
| `ContributionDraft` | proposed public text, author's terms, chosen displayed authorship | restricted editorial queue before approval | queue duration and withdrawal explained before submission |
| `ModerationDecision` | contribution ID, rule, reason, human editor, appeal | restricted record; public outcome is de-identified and checked | according to the adopted policy |
| `OperationalEvent` | time, event code, package version, duration/error without message body | minimal restricted log | short approved period; not a copy of correspondence |

Free-form personal text is not a required field. Message bodies, full IP addresses, geolocation, contacts and support histories are not recorded in the standard log. Other people's data is not added from address books, chats or archives to create a “complete map”. Cross-channel correlation is not performed without a separate, clear choice by the owner and a justification.

Export verifies the owner in a current authenticated session and includes only their own data; format and scope are shown before execution. Deletion first explains the affected records and possible lawful exceptions, requires owner confirmation and returns a result with `deleted`, `retained_with_basis`, `unknown` scopes. Do not promise deletion of messages from another messenger's infrastructure or other parties' backups if the service does not control them. Server backups require a tested expiry period and handling of restores.

<!-- suti:section:api-proposals -->
## API proposals

The routes below are proposed contracts; endpoints are not implemented.

| method and route | purpose | control |
|---|---|---|
| `GET /v1/catalog?locale=<slug>` | list permitted public entities | read-only; size limit; explicit locale state |
| `GET /v1/entities/<entity_id>?locale=<slug>` | card and source | ID from manifest; protection against arbitrary file paths |
| `POST /v1/sessions` | minimal session | short duration; no optional profile |
| `PATCH /v1/sessions/<id>` | locale, screen, pause | owner verification; allowlist of fields |
| `POST /v1/consents` | separate choice for a specific purpose | text version, scope and withdrawal option |
| `DELETE /v1/consents/<id>` | withdraw a specific choice | owner verification; stop the associated future action |
| `POST /v1/exports` | export one's own data | owner verification; short-lived link or local file |
| `POST /v1/deletion-requests` | confirmed deletion in an explicit scope | renewed confirmation; result log without data body |
| `POST /v1/contributions` | proposed public-safe contribution | separate opt-in, rules and moderation before runtime |
| `POST /v1/reviews/<id>/decisions` | human editorial decision | accepted role; reason; conflict/recusal; change history |
| `GET /v1/fund/status` | project and conditions state only | no banking information or personal applications |

Payment and grant operations are absent from the minimum version. Every future financial route requires a separate contract and authorization; until then `payments_enabled=false`, `fundraising_enabled=false`, `grant_intake_enabled=false`. Symbolic SUTI coins do not call a financial API or give an advantage in selection for support.

<!-- suti:section:ai-human-decisions -->
## AI and human decisions

Generation is optional. The first version may be entirely deterministic. If a model is connected later, the user learns which data will go where, for what purpose and for how long; AI processing is a separate choice. Private corpora and applications are not sent to an external provider by default. Technical access to a local model does not replace a basis for processing. Public cards are separated from free-form user text; instructions within documents are treated as data, not as authority.

The model's response cites permitted sources and distinguishes observation, interpretation, hypothesis and unknowns. When evidence is missing, it states the limitation and proposes an available, checkable step. The model does not assign identity, diagnose, determine a person's worth, promise assistance or decide payments. Neuro-Veche is labelled as editorial simulation; actual human responses are recorded separately.

<!-- suti:section:visual-content-collaboration -->
## collaborative development of visuals and content

The common aesthetic is quiet earthly light, readable typography, moderate density and meaning that works without a decorative glyph. Images of care, the flamingo, falcon, Garuna, Finist, urban shamans and Samurai Dharma are enabled as a voluntary artistic layer with provenance and authorship. Basic scenarios work without animation, sound or symbols. Manual motion controls, reduced-motion support, keyboard operation, visible focus, adequate contrast and text alternatives are required; a separate implementation review verifies whether these requirements are met.

Collaboration proceeds through clear outputs: agree the task and rights → choose one user route → compare several sketches → check understanding and accessibility → hand over editable sources → build a prototype → review → accept a bounded result. Partners define their own suitable framing, participation format, scope, schedule and desired remuneration. Gifting authored material without payment is documented separately from a development commission; a gift creates no obligation to work for free. Do not announce a partnership, consent, shared brand or licence to another party's materials before explicit acceptance.

Proposed collaboration subjects include a language bot; a 13-language catalogue; a visual map editor; accessible NITYA quests; learning cards; generative worlds; a series of voluntary short stories; and a transparent small-project system. Payment amount, currency, code and design rights, support, infrastructure and acceptance criteria are fixed in a separate agreed commission. A partner's public pages and completing a course do not authorize extracting closed lessons or audience data, or presenting that audience as participants.

<!-- suti:section:thirteen-contours -->
## all 13 contours in one contract

| contour | bot object and function |
|---|---|
| SUTI.os | boundaries, configuration, roles, versions, backup/rollback |
| SUTI.world | public entry and the person's chosen route |
| SUTI.uni | microlearning, exercise, observable result |
| SUTI.clan | voluntary circle and accepted role; no automatic membership |
| SUTI.lab | synthetic environment and bounded experiment |
| SUTI.audit | evidence, scoped checks and corrections |
| SUTI.crystal | clear knowledge card with source and boundary |
| SUTI.oracle | alternative questions; labelled hypothesis |
| SUTI.veche | human deliberation, disagreement and accountable outcome |
| SUTI.sotkan | entity relations, dependencies and provenance |
| SUTI.game | voluntary imaginative quest; plain language available |
| SUTI.logos | terms, voice, direct transcreation and loss checking |
| SUTI.verenium | manageable next step, pause, exit and limits of assistance |

<!-- suti:section:implementation-acceptance -->
## implementation stages and acceptance

| stage | concrete output | what permits the next stage |
|---|---|---|
| A · catalogue | canon, 13 contours, allowlist, manifest, sources and actual language states | selected set is public-safe; links and SHA checked |
| B · offline prototype | reading, language selection, search, quest, export of one's own bookmarks | main routes work manually, by keyboard and without a network |
| C · rehearsal | synthetic sessions, refusal, withdrawal, deletion, moderation, failure and recovery | expected results checked; no leakage between owners |
| D · adapter | separately authorized bot in a bounded environment | operator, secrets, data, logging, limits and protection confirmed |
| E · bounded pilot | one selected context with consenting adults | accepted roles, capacity, language, care and stop criteria |
| F · expansion | evaluation of usefulness and evidence-informed changes | separate human decision; every new context is checked |

Testable implementation acceptance criteria:

1. The manifest contains exactly the 13 specified contour IDs and 13 specified locales, without presenting an empty locale as a complete translation.
2. Every displayed card has a purpose, source, version, usage right, maturity state and accessible return route.
3. A missing locale has an honest state; language switching is explicit, with no hidden substitution.
4. Arabic reads in RTL and mixed IDs preserve meaning; Sanskrit, Latin and YZH have their required separate evidence.
5. Open materials can be read without a questionnaire; minimum-profile data is not requested.
6. `/pause`, `/exit` and unsubscribing work in all tested states; pause enables no new actions.
7. Export contains only the current owner's data; an attempt by another owner is rejected.
8. Deletion confirms scope, actually removes controlled records and honestly shows what is lawfully retained or outside the service's control.
9. Ordinary logs contain no message bodies, secrets, applications, private paths or personal histories.
10. A path-read attempt outside the allowlist, an instruction embedded in content and an unsuitable file are not executed as commands.
11. Voluntary contributions undergo human moderation, conflict/recusal handling, a stated reason and an appeal route; original authorship is preserved.
12. The game layer can be disabled; plain text carries the same meaning; there are no penalties for skipping or ranks of human dignity.
13. Youth intake, payments, fundraising and grant applications stay disabled until separate confirmed conditions are met.
14. Network and external-model operation does not begin without a separately approved runtime and a clear data choice.
15. Keyboard, focus, reading, contrast, text alternatives and reduced motion are checked in the actual interface.
16. Backup/restore has a tested result, and restoration does not reintroduce deleted records against the adopted policy.
17. Load and errors do not mix sessions; the user receives a clear state and an accessible exit.
18. The report names the exact version, environment, scenario, expected result and observed result; PASS is limited to what was tested.

All criteria above are currently `NOT_RUN`: the document sets requirements, rather than confirming their implementation. The next technical step is to select one public card set and implement offline prototype B after checking set A.

<!-- suti:section:spec-language-states -->
## language states of this specification

The Russian text is the AI-first source draft, pending author and independent content review. At the time that master was written, `en`, `es`, `pt-br`, `zh-hans`, `hi`, `fr`, `ar`, `bn`, `eo`, `sa`, `la`, `yzh` were recorded as `HOLD / not-started`. This English edition is now a direct editorial draft from that master; it is not independent acceptance. YZH additionally needs an author's gloss; sa and la need specialists; ar needs an RTL review. See `bot-spec.locale-status.v1.json` for current records. Release approval for every edition remains HOLD.

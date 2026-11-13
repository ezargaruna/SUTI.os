# zorga boto × komuna arkitekturo de SUTI

celo :: doni al homo klaran, libervolan eniron al scio, praktiko, komuna projekto kaj farebla sekva paŝo
stato :: specification-only · ĉi tiu dokumento ne realigas la sistemon
fonta lingvo :: ru
locale :: eo
dato :: 2026-11-13
funkciaj konektoj / Telegram runtime / akcepto de partoprenantoj / pagoj / publikigo :: OFF / HOLD
fonto :: [rusa specifo](bot-and-collaboration-spec.ru.md)
source_sha256 :: 76509088c1554bb71008e7076afc0683bd2669b57b26bd0535a6b8bab19e2ffe
traduko :: rekta AI-helpata redakcia malneto el la rusa; sendependa lingva kaj faka revizio atendas

La specifo priskribas proponatajn lokan enhavmotoron kaj botadaptilon por la komuna viva sistemo SUTI. La homo libervole elektas la bildon de anĝelo de zorgo, urba ŝamano aŭ samurajo de darmo. Ĉiu figura vojo havas samrangan esprimon en ordinara lingvo. La boto helpas trovi, esprimi kaj kontroli sekvan paŝon; rajtigitaj homoj faras la finajn decidojn pri helpo, subvencioj, plendoj, homa rolo kaj elspezoj.

## atendata unua rezulto

La homo elektas lingvon → legas la proponon kaj aktualajn limojn → elektas demandon aŭ pretan temon → ricevas mallongan karton kun fonto kaj ebla ago → konservas ĝin por si aŭ finas la vojon. Por legi malfermajn materialojn ne necesas profilo aŭ registriĝo. Ĉiu ekrano ebligas paŭzi, preterlasi, reveni kaj eliri. Nomo, naskiĝdato, sano, dokumentoj, financoj, familiaj cirkonstancoj kaj privata historio ne estas defaŭlte petataj.

La minimuma versio konsistas el loka sciokatalogo, 13 lingvaj vojoj, serĉo en publikigitaj kartoj, libervola NITYA-kvesto kaj eksporto de propraj legosignoj. Funkcianta mesaĝila integriĝo, konservado de uzantmesaĝoj, AI-servo, komunuma grupo, financa modulo kaj akceptado de subvencipetoj ne aŭtomate apartenas al tiu minimumo.

## uzantaj vojoj

| vojo | ago de la homo | rezulto | deviga limo |
|---|---|---|---|
| kompreni la sistemon | elekti mallongan superrigardon aŭ konturon | kompreneblaj celo kaj sekva vojo | la aktuala matureco estas videbla |
| trovi materialon | elekti temon aŭ lokan serĉon | karto, fonto, lingvo kaj stato | rezultoj venas nur el la permesita publika katalogo |
| mikrolernado | elekti mallongan praktikon | unu farebla paŝo kaj laŭvola kontrolo | neniu puno pro preterlaso, interrompita serio aŭ eliro |
| fusion-mapo | elekti malplenan ŝablonon | propra redaktebla dosiero | plenigo estas loka; sendo al iu estas aparta elekto |
| ludo NITYA | eksplicite ŝalti la figuran interfacon | libervola kvesto kun ordinara teksta ekvivalento | neniu asignita identeco aŭ rangigo de homa valoro |
| komuna kontribuo | malfermi la regulojn kaj proponi publikan materialon | malneto por homa konsidero | aŭtoraj rajtoj, publiko kaj licenco estas klarigitaj antaŭ inkludo |
| homa helpo | legi la haveblecon kaj limojn de la teamo | elektita kontaktvojo, se ĝi efektive ekzistas | kompetento, laborhoroj kaj respondeculo estas konfirmitaj; nehavebla helpo ne estas promesata |
| fonduso | legi la projekton kaj staton de la kondiĉoj | plano, kriterioj kaj agregitaj informoj | ricevo de mono kaj petoj restas malŝaltita ĝis apartaj permesoj |

Aĝaj etikedoj 0+, 12+, 18+, 21+, 33+ kaj 55+ estas redakciaj prezentoj, ne jura aĝkontrolo aŭ oficialaj aĝklasifikoj. Akcepto de infanoj kaj junuloj restas malŝaltita ĝis ekzistas kontrolita protekto de neplenaĝuloj. Sufiĉas proponi kompleksecon elektatan de la homo; oni ne kolektu precizan naskiĝdaton por agordi lingvon aŭ ritmon.

## konsisto de la proponata arkitekturo

La ĉi-suba rusa skemo estas preciza citaĵo de la teknika fonto. Ĝia vojo estas: publika katalogo → kontrolo de fonto, rajtoj, privateco kaj lingvo → determinisma pakaĵkonstruado → nurlega loka motoro → laŭvola, aparte permesita botadaptilo → elektitaj sesiaj agoj → aparta konsento kaj minimumigo → privata uzanta spaco ekster la publika katalogo.

```text
публичный каталог в .vault
    ↓ проверка источника, прав, приватности и языка
детерминированный сборщик публичного пакета
    ↓ allowlist + manifest + SHA-256
локальный read-only контентный движок
    ├─ Obsidian / Markdown
    ├─ доступный локальный HTML
    └─ опциональный адаптер бота
          ↓ только отдельный разрешённый runtime
       сессия пользователя / принятые им действия
          ↓ отдельное согласие и минимизация
       личное пространство пользователя вне публичного каталога
```

1. **Enhavkatalogo.** Stabilaj `entity_id`, fonto, signif-invarianto, amplekso, limoj, rajtoj, matureco kaj rilatoj. La publika pakaĵo ne listigas privatajn vojojn, kontaktojn aŭ originalajn personajn historiojn.
2. **Lingva tavolo.** Unu difinita majstro por ĉiu objekto kaj rektaj lokaj redakcioj. Nekontrolita traduko ne estas aŭtomate prezentata kiel preta teksto.
3. **Enkursigilo.** Determinismaj komandoj, konturoj kaj kartoj. La unua versio ne bezonas generan modelon. Respondo enhavas klaran fareblan paŝon kaj eksplicitan staton.
4. **Sesio.** Mallongdaŭra stato de la nuna ekrano. Defaŭlte ĝi restas en la memoro de la procezo aŭ ĉe la uzanto, ne en komuna publika datumbazo.
5. **Adaptilo.** Telegram aŭ alia kanalo konektiĝas aparte; sekretoj restas ekster `.vault`, la fonto de ĝisdatigoj estas kontrolata kaj nebezonataj eventoj malŝaltitaj. Teknika transporta ID estas persona identigilo; ĝi ne aperas en la publika pakaĵo aŭ ordinaraj protokoloj.
6. **Privata konservado.** Se la homo elektas konservi, datumoj estas en aparta privata spaco kun posedanto, limigita aliro, konservperiodo kaj kontrolita forigo. Fizika limo malsamas ol dosierujo ene de publika vault.
7. **Redakcia atendovico.** Kontribuo, obĵeto, korekto kaj plendo ricevas limigitan aliron, nomumitan homon kaj staton. Publika protokolo montras nur permesitan agregitan decidon.
8. **Eldon-kontrolo.** Antaŭ inkludo de dosiero oni kontrolas allowlist, rajtojn, privatecon, fonton, subtenatan formaton, ligilojn, lokalon kaj SHA. Eraro haltigas la konstruadon de tiu specifa eldono.

Tiu skemo difinas interfacojn, ne la ekziston de kodo. Efektivigo estas elektata post komparo kun la ekzistanta projekto, teama kapablo kaj postuloj de disponigo kaj loka konservado.

## 13 lokaloj kaj ŝargado de enhavo

lokaloj :: `ru`, `en`, `es`, `pt-br`, `zh-hans`, `hi`, `fr`, `ar`, `bn`, `eo`, `sa`, `la`, `yzh`

Proponata strukturo de publika pakaĵo; la fonta komentario pri teknikaj kontraktoj estas konservita:

```text
catalog/entities.json
catalog/relations.json
locales/<locale>/interface.json
locales/<locale>/cards/<entity_id>.md
locales/<locale>/glossary.json
manifests/content.json
manifests/locale-review.json
schemas/                  # технические контракты
```

`content.json` eksplicite listigas dosierojn, grandecojn, SHA-256, kanonversion kaj permesitajn lokalojn. Lingva stato estas aparta de dosierekzisto: `not-started`, `draft`, `meaning-reviewed`, `native-or-expert-reviewed`, `release-approved`. Tiuj estas proponataj enum-valoroj por nova kontrakto; ili ne ŝanĝas historiajn registrojn sen aparta migrado.

Ĉe elekto de lokalo la motoro kontrolas la haveblecon de la karto kaj ĉu ĝia stato estas permesita en la elektita reĝimo. Se teksto mankas, ĝi diras tion en la interfaca lingvo kaj proponas konscie elekti haveblan lingvon. Kaŝa anstataŭigo de malplena lokalo per rusa aŭ angla estas malpermesita. Post ĝisdatigo de la majstro, dependaj redakcioj ricevas staton postulantan versian komparon; malnova SHA ne kontrolas novan signifon.

La araba interfaco uzas `dir="rtl"` kaj apartan kontrolon de legado, tabeloj, nombroj kaj miksitaj identigiloj. Sanskrito kaj latino postulas fakulojn; YZH postulas aŭtor-aprobitan gloson kun plena klarigo kaj komprenkontrolo. Ĝis tiuj bazoj ekzistas, la lokalo ricevas honestan HOLD. Teksta versio de la signifo haveblas sen animacio, koloro aŭ specialaj simboloj.

## proponataj komandoj

Komandaj ID ne estas tradukataj; videblaj etikedoj estas lokalizataj. La komandoj estas API-propono kaj ne pruvas konektitan boton.

| komando | rezulto |
|---|---|
| `/start` | propono, lingvo kaj aktuala havebleco; sen demandaro |
| `/language` | eksplicita lingvoelekto kaj videblaj mankoj |
| `/contours` | 13 konturoj kun mallongaj celoj |
| `/learn` | mallonga leciono kaj libervola ago |
| `/quest` | aparta ŝalto de la libervola ludo |
| `/map` | malplena redaktebla ŝablono de fusion-mapo |
| `/sources` | deveno de la nuna publika karto |
| `/pause` | halto de la nuna vojo kaj sciigoj en la limoj de la serva povo |
| `/resume` | eksplicita rekomenco; ne ebligas novajn konsentojn |
| `/export` | propraj konservitaj datumoj post posedkontrolo |
| `/delete` | komprenebla amplekso de forigo kaj konfirmo de la posedanto |
| `/privacy` | operatoro, celo, konservado, aliro, rajtoj kaj kontakto, se aprobitaj |
| `/help` | alirebla ordinara navigado kaj realaj helpolimoj |
| `/exit` | fino de la sesio; klarigo pri aparte elektita konservado |

Aŭtomataj dissendoj kaj ĉiutagaj taskoj defaŭlte estas malŝaltitaj. Abono havas celon, oftecon, lokan horon kaj facilan malabonan vojon. Unu `/start` ne signifas abonon, AI-prilaboradon, aliĝon al komunumo aŭ konsenton al publikigo.

## datumoj kaj posedado

| ento | minimumaj kampoj | loko kaj aliro | konservado |
|---|---|---|---|
| `PublicEntity` | `entity_id`, `source_id`, `version`, `kind`, `contour_id`, `license_state`, `implementation_state` | publika kontrolita pakaĵo | laŭ la akceptita versipolitiko |
| `LocalizedArtifact` | `entity_id`, `locale`, `source_sha256`, `target_sha256`, `review_state`, `release_state` | publikaj tekstoj kaj publike sekuraj bazoj | ĝis anstataŭigo, kun devenospuro ekster la aktiva pakaĵo |
| `Relation` | `from_id`, `to_id`, `relation_type`, `evidence_ref` | publika katalogo | laŭ la katalogversio |
| `Session` | hazarda `session_id`, lokalo, ekrano, paŭzostato | memoro aŭ privata konservejo; nur la sesioposedanto kaj procezo | minimuma periodo; konkreta TTL estas aprobata kaj provata antaŭ runtime |
| `TransportBinding` | teknika kanalidentigilo kaj ligo al privata sesio | aparta limigita konservejo; ne publikaj protokoloj | periodo estas pravigita por la elektita kanalo; scenara forigo |
| `SavedItem` | `owner_id`, `entity_id`, homa marko, tempo | defaŭlte ĉe la uzanto; servila konservado postulas apartan opt-in | elektita periodo; korekto, eksporto kaj forigo |
| `ConsentRecord` | celo, versio de klarigo, amplekso, elekto, tempo kaj revoko | aparta privata konservejo | laŭ aplikebla devo; ne eterna nedifinita periodo |
| `ContributionDraft` | proponita publika teksto, aŭtoraj kondiĉoj, elektita montrata aŭtoreco | limigita redaktora vico ĝis permeso | atendperiodo kaj revoko estas klarigitaj antaŭ sendo |
| `ModerationDecision` | kontribua ID, regulo, kialo, homa redaktoro, apelacio | limigita registro; publika rezulto senidentigita kaj kontrolita | laŭ akceptita politiko |
| `OperationalEvent` | tempo, eventokodo, pakaĵversio, daŭro/eraro sen mesaĝkorpo | minimuma limigita protokolo | mallonga aprobita periodo; ne kopio de korespondado |

Libera privata teksto ne estas deviga kampo. Mesaĝkorpoj, plenaj IP-adresoj, geoloko, kontaktoj kaj helphistorioj ne estas konservataj en la norma protokolo. Datumoj de aliaj homoj ne estas aldonataj el adresaro, babilejoj aŭ arkivoj por fari «plenan mapon». Interkanala korelacio ne okazas sen aparta klara elekto de la posedanto kaj pravigo.

Eksporto kontrolas la posedanton en aktuala aŭtentikigita sesio kaj enhavas nur ties proprajn datumojn; formato kaj amplekso estas montrataj antaŭ plenumo. Forigo unue klarigas la koncernajn registrojn kaj eblajn laŭleĝajn esceptojn, postulas posedantan konfirmon kaj liveras rezulton laŭ `deleted`, `retained_with_basis`, `unknown`. Oni ne promesu forigi mesaĝojn el infrastrukturo de alia mesaĝilo aŭ el fremdaj sekurkopioj, se la servo ne regas ilin. Servilaj sekurkopioj bezonas provitan eluzperiodon kaj traktadon de restaŭroj.

## proponoj de API

La jenaj vojoj estas kontraktoproponoj; la finpunktoj ne estas efektivigitaj.

| metodo kaj vojo | celo | kontrolo |
|---|---|---|
| `GET /v1/catalog?locale=<slug>` | listo de permesitaj publikaj entoj | read-only; grandecolimo; eksplicita lokalstato |
| `GET /v1/entities/<entity_id>?locale=<slug>` | karto kaj fonto | ID el manifest; protekto kontraŭ arbitraj dosiervojoj |
| `POST /v1/sessions` | minimuma sesio | mallonga periodo; neniu nedeviga profilo |
| `PATCH /v1/sessions/<id>` | lokalo, ekrano, paŭzo | posedkontrolo; listo de permesitaj kampoj |
| `POST /v1/consents` | aparta elekto por specifa celo | tekstoversio, amplekso kaj revokebleco |
| `DELETE /v1/consents/<id>` | revoko de specifa elekto | posedkontrolo; halto de la rilata estonta ago |
| `POST /v1/exports` | propra eksporto | posedkontrolo; mallongdaŭra ligilo aŭ loka dosiero |
| `POST /v1/deletion-requests` | konfirmita forigo en eksplicita amplekso | refoja konfirmo; rezultoprotokolo sen datumkorpo |
| `POST /v1/contributions` | publike sekura proponita kontribuo | apartaj opt-in, reguloj kaj moderigado antaŭ runtime |
| `POST /v1/reviews/<id>/decisions` | homa redakcia decido | akceptita rolo; kialo; konflikto/sindetenado; ŝanĝhistorio |
| `GET /v1/fund/status` | nur stato de projekto kaj kondiĉoj | neniuj bankaj informoj aŭ privataj petoj |

La minimuma versio ne inkludas pagojn aŭ subvenciajn operaciojn. Ĉiu estonta financa vojo bezonas apartajn kontrakton kaj permeson; ĝis tiam `payments_enabled=false`, `fundraising_enabled=false`, `grant_intake_enabled=false`. Simbolaj SUTI-moneroj ne vokas financan API kaj ne donas avantaĝon ĉe elekto de helpo.

## AI kaj homaj decidoj

Generado estas laŭvola. La unua versio povas esti tute determinisma. Se modelo poste estas konektita, la uzanto scias, kiuj datumoj iros kien, por kiu celo kaj por kiom da tempo; AI-prilaborado estas aparta elekto. Privata korpuso kaj petoj ne estas defaŭlte sendataj al ekstera provizanto. Teknika aliro al loka modelo ne anstataŭas bazon por prilaborado. Publikaj kartoj estas apartaj de libera uzantteksto; instrukcioj en dokumentoj estas traktataj kiel datumoj, ne kiel aŭtoritato agi.

Modela respondo citas permesitajn fontojn kaj distingas observon, interpreton, hipotezon kaj nekonataĵon. Sen bazo ĝi nomas la limon kaj proponas fareblan kontroleblan paŝon. La modelo ne asignas identecon, ne diagnozas, ne taksas homan valoron, ne promesas helpon kaj ne decidas pri pagoj. Neŭro-veĉeo estas markita kiel redakcia simulado; efektivaj homaj respondoj estas registrataj aparte.

## komuna evoluigo de bildaro kaj enhavo

La komuna estetiko estas trankvila tera lumo, legebla tipografio, modera denseco kaj signifo sen ornama glifo. Bildoj de zorgo, flamengo, falko, Garuna, Finist, urbaj ŝamanoj kaj Samurai Dharma estas laŭvola arta tavolo kun deveno kaj aŭtoreco. Bazaj scenaroj funkcias sen animacio, sono aŭ simboloj. Necesas mana movokontrolo, subteno de reduktita movo, klavaro, videbla fokuso, sufiĉa kontrasto kaj tekstaj alternativoj; plenumo estas konfirmata per aparta efektivigokontrolo.

Kunlaboro sekvas klarajn rezultojn: interkonsenti pri tasko kaj rajtoj → elekti unu uzantvojon → kompari plurajn skizojn → kontroli komprenon kaj alireblecon → transdoni redakteblajn fontojn → konstrui prototipon → kontroli → akcepti limigitan rezulton. Partneroj mem difinas taŭgajn kadron, partoprenformaton, amplekson, limdatojn kaj deziratan rekompencon. Senpaga donaco de aŭtora materialo estas traktata aparte de evoluiga mendo; donaco ne kreas devon senpage labori. Oni ne anoncu partnerecon, konsenton, komunan markon aŭ licencon pri fremda materialo antaŭ eksplicita akcepto.

Proponataj kunlaborobjektoj: lingva boto; 13-lingva katalogo; vida mapredaktilo; alireblaj NITYA-kvestoj; lernkartoj; generaj mondoj; serio de libervolaj mallongaj rakontoj; travidebla sistemo de malgrandaj projektoj. Pago, valuto, rajtoj pri kodo kaj dezajno, subteno, infrastrukturo kaj akceptokriterio estas fiksataj en aparta interkonsentita mendo. Publikaj partnerpaĝoj kaj trapaso de kurso ne rajtigas eltiri fermitajn lecionojn aŭ datumojn pri la kursa publiko, nek prezenti ilin kiel partoprenantojn de SUTI.

## ĉiuj 13 konturoj en unu kontrakto

| konturo | objekto kaj funkcio de la boto |
|---|---|
| SUTI.os | limoj, agordoj, roloj, versioj, backup/rollback |
| SUTI.world | publika eniro kaj vojo elektita de la homo |
| SUTI.uni | mikrolernado, ekzerco, observebla rezulto |
| SUTI.clan | libervola rondo kaj akceptita rolo; sen aŭtomata aliĝo |
| SUTI.lab | sinteza medio kaj limigita eksperimento |
| SUTI.audit | pruvoj, limigitaj kontroloj kaj korektoj |
| SUTI.crystal | klara sciokarto kun fonto kaj limo |
| SUTI.oracle | alternativaj demandoj; markita hipotezo |
| SUTI.veche | homa diskutado, malkonsento kaj respondeca rezulto |
| SUTI.sotkan | entorilatoj, dependecoj kaj provenance |
| SUTI.game | libervola figura kvesto; ordinara lingvo haveblas |
| SUTI.logos | terminoj, voĉo, rektaj transkreoj kaj perdo-kontrolo |
| SUTI.verenium | farebla sekva paŝo, paŭzo, eliro kaj helpolimoj |

## etapoj de efektivigo kaj akcepto

| etapo | konkreta rezulto | kondiĉo por daŭrigi |
|---|---|---|
| A · katalogo | kanono, 13 konturoj, allowlist, manifest, fontoj kaj realaj lingvaj statoj | elektita aro estas publike sekura; ligiloj kaj SHA kontrolitaj |
| B · eksterreta prototipo | legado, lingvoelekto, serĉo, kvesto, eksporto de propraj legosignoj | ĉefaj vojoj trapaseblas permane, klavare kaj sen reto |
| C · provludo | sintezaj sesioj, rifuzo, revoko, forigo, moderigado, paneo kaj restaŭro | atendataj rezultoj kontrolitaj; neniu liko inter posedantoj |
| D · adaptilo | aparte permesita boto en limigita medio | operatoro, sekretoj, datumoj, protokolo, limoj kaj protekto konfirmitaj |
| E · limigita piloto | unu elektita kunteksto kun konsentantaj plenkreskuloj | akceptitaj roloj, kapablo, lingvo, zorgo kaj haltokriterioj |
| F · vastigo | takso de utileco kaj ŝanĝoj laŭ datumoj | aparta homa decido; ĉiu nova kunteksto estas kontrolata |

Kontroleblaj akceptokriterioj de la efektivigo:

1. Manifest enhavas precize la 13 difinitajn konturajn ID kaj 13 difinitajn lokalojn, sen prezenti malplenan lokalon kiel pretan tradukon.
2. Ĉiu montrata karto havas celon, fonton, version, uzrajton, maturecon kaj alireblan revenvojon.
3. Mankanta lokalo estas honeste indikita; lingvoŝanĝo estas eksplicita, sen kaŝa anstataŭigo.
4. La araba eldono legiĝas RTL; miksitaj ID ne rompas la signifon; sanskrito, latino kaj YZH havas siajn postulatajn apartajn bazojn.
5. Malfermaj materialoj legeblas sen demandaro; minimumaj profildatumoj ne estas petataj.
6. `/pause`, `/exit` kaj malabono funkcias en ĉiuj kontrolitaj statoj; paŭzo ne komencas novajn agojn.
7. Eksporto enhavas nur datumojn de la aktuala posedanto; provo de alia posedanto estas rifuzata.
8. Forigo konfirmas amplekson, efektive forigas regatajn registrojn kaj honeste montras laŭleĝe konservatajn kaj neregeblajn datumojn.
9. Ordinara protokolo ne enhavas mesaĝkorpojn, sekretojn, petojn, privatajn vojojn aŭ personajn historiojn.
10. Provo legi vojon ekster allowlist, instrukcio enkonstruita en enhavo kaj netaŭga dosiero ne plenumiĝas kiel komando.
11. Libervola kontribuo trapasas homan moderigon, konflikton/sindetenadon, klarigitan kialon kaj apelacian vojon; originala aŭtoreco restas.
12. La luda tavolo estas malŝaltebla; ordinara teksto esprimas la saman signifon; forestas punoj pro preterlaso kaj rangoj de homa digno.
13. Junulara akcepto, pagoj, monkolektado kaj subvencipetoj restas malŝaltitaj ĝis apartaj konfirmitaj kondiĉoj.
14. Reta laboro kaj ekstera modelo ne komenciĝas sen aparta aprobita runtime kaj klara datumelekto.
15. Alirebleco estas kontrolita en la efektiva interfaco por klavaro, fokuso, legado, kontrasto, tekstaj alternativoj kaj reduktita movo.
16. backup/restore havas kontrolitan rezulton; restaŭro ne revenigas forigitajn registrojn kontraŭ la akceptita politiko.
17. Ŝarĝo kaj eraroj ne miksas sesiojn; la uzanto ricevas klaran staton kaj alireblan eliron.
18. La raporto nomas precizajn version, medion, scenaron, atendatan kaj observitan rezulton; PASS limiĝas al tio, kio estis kontrolita.

Ĉiuj supraj kriterioj nun havas staton `NOT_RUN`: la dokumento difinas postulojn, ne konfirmas ilian efektivigon. La sekva teknika paŝo estas elekti unu publikan kartaron kaj efektivigi eksterretan prototipon B post kontrolo de aro A.

## lingvaj statoj de la specifo

La rusa teksto estas fonta AI-first malneto atendanta aŭtoran kaj sendependan enhavan revizion. La fonta stato registris `en`, `es`, `pt-br`, `zh-hans`, `hi`, `fr`, `ar`, `bn`, `eo`, `sa`, `la`, `yzh` kiel `HOLD / not-started`. Ĉi tiu rekta Esperanto-redakcio nun estas malneto; tiu historia listo ne signifas, ke ĉi tiu dosiero mankas. La aktuala familiregistro estas `bot-spec.locale-status.v1.json`. YZH aldone bezonas aŭtoran gloson; sa kaj la bezonas fakulojn; ar bezonas RTL-kontrolon. Ĉiuj eldonoj atendas apartan eldonpermeson; ĉi tiu malneto restas HOLD por sendependa revizio.

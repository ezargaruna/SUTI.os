---
artifact_id: suti.bot-collaboration-spec.fr.2026-11-13
source_path: bot-and-collaboration-spec.ru.md
source_locale: ru
source_sha256: 76509088c1554bb71008e7076afc0683bd2669b57b26bd0535a6b8bab19e2ffe
source_version: 2026-11-13
locale: fr
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

# bot de soin × architecture collaborative SUTI

finalité :: offrir à chacun une entrée claire et volontaire dans les connaissances, la pratique, un projet commun et une prochaine étape possible
état :: specification-only · ce document ne crée pas d'implémentation
langue source :: ru
locale :: fr
date :: 2026-11-13
connexions opérationnelles / Telegram runtime / admission de participants / paiements / publication :: OFF / HOLD
source :: [maître russe](bot-and-collaboration-spec.ru.md)

Cette spécification décrit un moteur local de contenu et un adaptateur de bot proposés pour le système vivant commun SUTI. La personne active volontairement l'image d'un ange de soin, d'un chaman urbain ou d'un samouraï du dharma. Chaque parcours imagé dispose d'une formulation équivalente en langage courant. Le bot aide à trouver, exprimer et vérifier une prochaine étape ; des personnes habilitées prennent les décisions finales concernant l'aide, les subventions, les plaintes, le rôle d'une personne et les dépenses.

<!-- suti:section:expected-first-result -->
## premier résultat attendu

La personne choisit une langue → lit la proposition et les limites actuelles → choisit une question ou un thème disponible → reçoit une courte fiche avec une source et une action possible → la conserve pour elle-même ou termine le parcours. Lire les ressources ouvertes ne nécessite ni profil ni inscription. Chaque écran permet de mettre en pause, passer, revenir ou sortir. Nom, date de naissance, santé, documents, finances, situation familiale et histoire privée ne sont pas demandés par défaut.

La version minimale comprend un catalogue local de connaissances, 13 parcours linguistiques, une recherche dans les fiches publiées, une quête volontaire NITYA et l'export de ses propres favoris. Une intégration de messagerie fonctionnelle, le stockage des messages des utilisateurs, un service d'IA, un groupe communautaire, un module financier et la réception de demandes de subvention ne font pas automatiquement partie de ce minimum.

<!-- suti:section:user-routes -->
## parcours d'utilisation

| parcours | action de la personne | résultat | limite obligatoire |
|---|---|---|---|
| comprendre le système | choisir un aperçu ou un contour | finalité claire et prochain parcours | maturité actuelle visible |
| trouver une ressource | choisir un thème ou une recherche locale | fiche, source, langue et état | résultats limités au catalogue public autorisé |
| microapprentissage | choisir une pratique courte | une étape réalisable et une vérification facultative | aucune sanction pour une étape passée, une série interrompue ou une sortie |
| carte fusion | choisir un modèle vide | fichier personnel modifiable | remplissage local ; l'envoi à autrui est un choix distinct |
| jeu NITYA | activer explicitement l'interface imagée | quête volontaire avec équivalent en texte courant | aucune identité assignée ni classement de la valeur humaine |
| contribution commune | ouvrir les règles et proposer un contenu public | brouillon soumis à examen humain | droits d'auteur, public et licence précisés avant inclusion |
| aide humaine | lire les disponibilités et les limites de l'équipe | voie de contact choisie, si elle existe réellement | compétences, horaires et responsable confirmés ; l'aide indisponible n'est pas promise |
| fonds | lire le projet et l'état des conditions | plan, critères et informations agrégées | réception d'argent et de demandes désactivée jusqu'à des autorisations distinctes |

Les repères d'âge 0+, 12+, 18+, 21+, 33+ et 55+ sont des présentations éditoriales, pas une vérification légale d'âge ni des classifications officielles. L'admission des enfants et des jeunes reste désactivée tant qu'une protection vérifiée des mineurs n'est pas en place. Il suffit de proposer le niveau de difficulté choisi par la personne ; ne pas recueillir sa date de naissance exacte pour adapter la langue ou le rythme.

<!-- suti:section:proposed-architecture -->
## composants de l'architecture proposée

```text
catalogue public dans .vault
    ↓ vérifier source, droits, vie privée et langue
constructeur déterministe du paquet public
    ↓ allowlist + manifest + SHA-256
moteur local de contenu read-only
    ├─ Obsidian / Markdown
    ├─ HTML local accessible
    └─ adaptateur de bot facultatif
          ↓ uniquement un runtime autorisé séparément
       session de l'utilisateur / actions acceptées par la personne
          ↓ consentement distinct et minimisation
       espace privé de l'utilisateur hors du catalogue public
```

1. **Catalogue de contenu.** `entity_id` stable, source, sens invariant, périmètre, limites, droits, maturité et relations. Le paquet public n'énumère ni chemins privés, ni contacts, ni récits originaux de personnes.
2. **Couche linguistique.** Un maître identifié par objet et des éditions directement dérivées pour chaque locale. Aucune traduction non relue n'est substituée automatiquement à un texte en étant présentée comme prête à l'emploi.
3. **Routeur.** Commandes, contours et fiches déterministes. La première version ne nécessite pas de modèle génératif. La réponse contient une étape claire et accessible et un état explicite.
4. **Session.** État de courte durée de l'écran actuel. Il reste par défaut en mémoire du processus ou chez l'utilisateur, et non dans une base publique collective.
5. **Adaptateur.** Telegram ou un autre canal est connecté séparément ; les secrets restent hors de `.vault`, la provenance des mises à jour est vérifiée et les événements facultatifs sont désactivés. Le transport ID technique est traité comme un identifiant personnel et ne figure ni dans le paquet public ni dans les journaux ordinaires.
6. **Stockage privé.** Si la personne choisit de conserver des données, elles vont dans un espace privé séparé avec un propriétaire, un accès restreint, une durée et un effacement testé. Une frontière physique diffère d'un dossier au sein d'un vault public.
7. **File éditoriale.** Contributions, objections, corrections et plaintes reçoivent un accès restreint, une personne assignée et un état. Le registre public ne montre qu'une décision agrégée autorisée.
8. **Vérification de publication.** Avant d'inclure un fichier, vérifier allowlist, droits, vie privée, source, format pris en charge, liens, locale et SHA. Une erreur arrête la construction de cette version précise.

Ce schéma définit des interfaces, pas l'existence de code. L'implémentation est choisie après examen du projet existant, du soutien de l'équipe, des exigences de déploiement et du stockage local.

<!-- suti:section:locales-content-loading -->
## 13 locales et chargement des contenus

locales :: `ru`, `en`, `es`, `pt-br`, `zh-hans`, `hi`, `fr`, `ar`, `bn`, `eo`, `sa`, `la`, `yzh`

Structure proposée du paquet public :

```text
catalog/entities.json
catalog/relations.json
locales/<locale>/interface.json
locales/<locale>/cards/<entity_id>.md
locales/<locale>/glossary.json
manifests/content.json
manifests/locale-review.json
schemas/                  # contrats techniques
```

`content.json` énumère explicitement fichiers, tailles, SHA-256, version du canon et locales autorisées. L'état linguistique est conservé séparément de la présence d'un fichier : `not-started`, `draft`, `meaning-reviewed`, `native-or-expert-reviewed`, `release-approved`. Ce sont des valeurs enum proposées pour un nouveau contrat ; elles ne réécrivent pas les registres historiques sans migration distincte.

Lors du choix d'une locale, le moteur vérifie la disponibilité de la fiche et si son état est admissible dans le mode choisi. Si le texte manque, il l'explique dans la langue de l'interface et propose de choisir consciemment une langue disponible. Remplacer une locale vide par le russe ou l'anglais sans l'annoncer est interdit. À chaque modification du maître, les éditions dépendantes sont signalées comme nécessitant une nouvelle comparaison ; un ancien SHA ne vérifie pas un sens nouveau.

L'interface arabe utilise `dir="rtl"` et une vérification distincte de la lecture, des tableaux, des nombres et des identifiants mixtes. Le sanskrit et le latin exigent des spécialistes ; YZH exige une glose approuvée par l'auteur, avec développement et vérification de compréhension. Sans ces éléments, la locale reçoit un HOLD explicite. Une version textuelle du sens reste disponible sans animation, couleur ni symboles spéciaux.

<!-- suti:section:proposed-commands -->
## commandes proposées

Les ID des commandes ne sont pas traduits ; les libellés visibles sont localisés. Ces commandes sont une proposition d'API, pas la preuve d'un bot connecté.

| commande | résultat |
|---|---|
| `/start` | proposition, langue et disponibilité actuelle ; sans questionnaire |
| `/language` | choix explicite de langue et lacunes visibles |
| `/contours` | 13 contours avec leurs finalités brèves |
| `/learn` | courte leçon et action volontaire |
| `/quest` | activation distincte du jeu volontaire |
| `/map` | modèle vide et modifiable de carte fusion |
| `/sources` | provenance de la fiche publique actuelle |
| `/pause` | arrêt du parcours et des notifications dans les limites du pouvoir du service |
| `/resume` | reprise explicite ; aucun nouveau consentement activé |
| `/export` | ses propres données conservées, après vérification de propriété |
| `/delete` | périmètre d'effacement clair et confirmation du propriétaire |
| `/privacy` | opérateur, finalité, conservation, accès, droits et contact, s'ils sont approuvés |
| `/help` | navigation ordinaire accessible et limites réelles de l'aide |
| `/exit` | fin de session ; explication de toute conservation choisie séparément |

Les diffusions automatiques et les tâches quotidiennes sont désactivées par défaut. Un abonnement a une finalité, une fréquence, une heure locale et un moyen simple de se désabonner. Une commande `/start` ne signifie ni abonnement, ni traitement par IA, ni entrée dans une communauté, ni consentement à publier.

<!-- suti:section:data-ownership -->
## données et propriété

| entité | champs minimaux | emplacement et accès | conservation |
|---|---|---|---|
| `PublicEntity` | `entity_id`, `source_id`, `version`, `kind`, `contour_id`, `license_state`, `implementation_state` | paquet public vérifié | selon la politique de versions adoptée |
| `LocalizedArtifact` | `entity_id`, `locale`, `source_sha256`, `target_sha256`, `review_state`, `release_state` | textes publics et éléments justificatifs publiables sans données privées | jusqu'au remplacement, avec provenance conservée hors du paquet actif |
| `Relation` | `from_id`, `to_id`, `relation_type`, `evidence_ref` | catalogue public | selon la version du catalogue |
| `Session` | `session_id` aléatoire, locale, écran, état de pause | mémoire ou stockage privé ; propriétaire de la session et processus uniquement | durée minimale ; TTL précis approuvé et testé avant runtime |
| `TransportBinding` | identifiant technique du canal et lien vers une session privée | stockage séparé et restreint ; pas de journaux publics | durée justifiée pour le canal choisi ; effacement selon le scénario |
| `SavedItem` | `owner_id`, `entity_id`, annotation de la personne, heure | chez l'utilisateur par défaut ; conservation sur serveur sur opt-in distinct | durée choisie ; correction, export et effacement |
| `ConsentRecord` | finalité, version de l'explication, périmètre, choix, heure et retrait | stockage privé séparé | selon l'obligation applicable ; pas de durée perpétuelle indéfinie |
| `ContributionDraft` | texte public proposé, conditions de l'auteur, attribution affichée choisie | file éditoriale restreinte avant approbation | durée de la file et retrait expliqués avant envoi |
| `ModerationDecision` | ID de contribution, règle, motif, éditeur humain, recours | registre restreint ; résultat public désidentifié et vérifié | selon la politique adoptée |
| `OperationalEvent` | heure, code d'événement, version du paquet, durée/erreur sans corps de message | journal minimal restreint | courte durée approuvée ; pas une copie de correspondance |

Le texte personnel libre n'est pas un champ obligatoire. Le journal standard ne conserve ni corps de messages, ni IP complètes, ni géolocalisation, ni contacts, ni historiques d'aide. Les données d'autrui ne sont pas ajoutées à partir de carnets d'adresses, de discussions ou d'archives pour produire une « carte complète ». Aucune corrélation entre canaux n'est effectuée sans un choix distinct et clair du propriétaire et une justification.

L'export vérifie le propriétaire dans une session authentifiée en cours et ne contient que ses propres données ; format et périmètre sont affichés avant l'exécution. L'effacement explique d'abord les enregistrements concernés et les éventuelles exceptions légales, demande la confirmation du propriétaire et fournit un résultat avec les périmètres `deleted`, `retained_with_basis`, `unknown`. Il ne faut pas promettre d'effacer des messages dans l'infrastructure d'une autre messagerie ou des sauvegardes de tiers si le service ne les contrôle pas. Les sauvegardes serveur nécessitent une durée d'expiration testée et un traitement des restaurations.

<!-- suti:section:api-proposals -->
## propositions d'API

Les routes suivantes sont des propositions de contrat ; les endpoints ne sont pas implémentés.

| méthode et route | finalité | contrôle |
|---|---|---|
| `GET /v1/catalog?locale=<slug>` | lister les entités publiques autorisées | read-only ; taille limitée ; état explicite de la locale |
| `GET /v1/entities/<entity_id>?locale=<slug>` | fiche et source | ID issu du manifest ; protection contre les chemins de fichiers arbitraires |
| `POST /v1/sessions` | session minimale | courte durée ; pas de profil facultatif |
| `PATCH /v1/sessions/<id>` | locale, écran, pause | vérifier le propriétaire ; liste des champs autorisés |
| `POST /v1/consents` | choix distinct pour une finalité précise | version du texte, périmètre et possibilité de retrait |
| `DELETE /v1/consents/<id>` | retrait d'un choix précis | vérifier le propriétaire ; arrêter l'action future associée |
| `POST /v1/exports` | export de ses propres données | vérifier le propriétaire ; lien temporaire ou fichier local |
| `POST /v1/deletion-requests` | effacement confirmé dans un périmètre explicite | nouvelle confirmation ; journal du résultat sans corps de données |
| `POST /v1/contributions` | contribution proposée publiable sans données privées | opt-in distinct, règles et modération avant runtime |
| `POST /v1/reviews/<id>/decisions` | décision éditoriale humaine | rôle accepté ; motif ; conflit/déport ; historique des modifications |
| `GET /v1/fund/status` | état du projet et des conditions uniquement | aucune information bancaire ni demande personnelle |

La version minimale ne comprend aucune opération de paiement ou de subvention. Toute future voie financière nécessite un contrat et une autorisation distincts ; jusque-là `payments_enabled=false`, `fundraising_enabled=false`, `grant_intake_enabled=false`. Les pièces symboliques SUTI n'appellent pas d'API financière et ne donnent aucun avantage dans la sélection des aides.

<!-- suti:section:ai-human-decisions -->
## IA et décisions humaines

La génération est facultative. La première version peut être entièrement déterministe. Si un modèle est connecté plus tard, l'utilisateur sait quelles données iront où, pour quelle finalité et pour quelle durée ; le traitement par IA fait l'objet d'un choix distinct. Corpus privés et demandes ne sont pas envoyés par défaut à un fournisseur externe. L'accès technique à un modèle local ne remplace pas un fondement de traitement. Les fiches publiques sont séparées du texte libre de l'utilisateur ; les instructions contenues dans les documents sont traitées comme des données, et non comme un pouvoir d'agir.

La réponse du modèle cite les sources autorisées et distingue observation, interprétation, hypothèse et inconnu. Faute de fondement, elle indique la limite et propose une étape disponible et vérifiable. Le modèle n'assigne pas d'identité, ne diagnostique pas, ne détermine pas la valeur d'une personne, ne promet pas d'aide et ne décide pas de versements. Le neuro-veche est signalé comme simulation éditoriale ; les réponses réelles des personnes sont enregistrées séparément.

<!-- suti:section:visual-content-collaboration -->
## développement collaboratif du visuel et des contenus

L'esthétique commune est une lumière terrestre paisible, une typographie lisible, une densité modérée et un sens qui reste clair sans glyphe décoratif. Les images de soin, du flamant, du faucon, de Garuna, de Finist, des chamans urbains et de Samurai Dharma sont activées comme couche artistique volontaire avec provenance et attribution d'auteur. Les scénarios de base fonctionnent sans animation, son ni symboles. Contrôle manuel du mouvement, réduction des animations, utilisation au clavier, focus visible, contraste suffisant et alternatives textuelles sont requis ; leur réalisation est confirmée par une vérification distincte de l'implémentation.

La collaboration suit des résultats clairs : convenir de la tâche et des droits → choisir un parcours utilisateur → comparer plusieurs esquisses → vérifier compréhension et accessibilité → remettre les sources modifiables → construire un prototype → vérifier → accepter un résultat délimité. Les partenaires définissent eux-mêmes le cadre qui leur convient, leur mode de participation, le périmètre, les délais et la rémunération souhaitée. Le don gratuit d'un contenu d'auteur est formalisé séparément d'une commande de développement ; un don ne crée pas l'obligation de travailler gratuitement. Ne pas annoncer partenariat, consentement, marque commune ou licence sur les contenus d'autrui avant acceptation explicite.

Sujets de collaboration proposés : bot linguistique ; catalogue en 13 langues ; éditeur visuel de cartes ; quêtes NITYA accessibles ; fiches pédagogiques ; mondes génératifs ; série de courtes histoires volontaires ; système transparent de petits projets. Montant, devise, droits sur le code et le design, support, infrastructure et critères d'acceptation sont fixés dans une commande distincte convenue. Les pages publiques d'un partenaire et le fait d'avoir suivi une formation n'autorisent pas à extraire des leçons fermées, des données d'audience ni à présenter cette audience comme des participants.

<!-- suti:section:thirteen-contours -->
## les 13 contours dans un contrat commun

| contour | objet et fonction du bot |
|---|---|
| SUTI.os | limites, configuration, rôles, versions, backup/rollback |
| SUTI.world | entrée publique et parcours choisi par la personne |
| SUTI.uni | microapprentissage, exercice, résultat observable |
| SUTI.clan | cercle volontaire et rôle accepté ; aucune adhésion automatique |
| SUTI.lab | environnement synthétique et expérience délimitée |
| SUTI.audit | éléments de preuve, vérifications circonscrites et corrections |
| SUTI.crystal | fiche de connaissance claire avec source et limite |
| SUTI.oracle | questions alternatives ; hypothèse signalée |
| SUTI.veche | délibération humaine, désaccord et conclusion dont un humain répond |
| SUTI.sotkan | relations entre entités, dépendances et provenance |
| SUTI.game | quête imagée volontaire ; langage courant disponible |
| SUTI.logos | termes, voix, transcréations directes et contrôle des pertes |
| SUTI.verenium | prochaine étape réalisable, pause, sortie et limites de l'aide |

<!-- suti:section:implementation-acceptance -->
## étapes d'implémentation et acceptation

| étape | résultat concret | condition pour poursuivre |
|---|---|---|
| A · catalogue | canon, 13 contours, allowlist, manifest, sources et états linguistiques réels | sélection publiable sans données privées ; liens et SHA vérifiés |
| B · prototype hors ligne | lecture, langue, recherche, quête, export de ses propres favoris | principaux parcours vérifiés manuellement, au clavier et sans réseau |
| C · répétition | sessions synthétiques, refus, retrait, effacement, modération, panne et reprise | résultats attendus vérifiés ; aucune fuite entre propriétaires |
| D · adaptateur | bot autorisé séparément dans un environnement délimité | opérateur, secrets, données, journal, limites et protection confirmés |
| E · pilote délimité | un contexte choisi avec des adultes consentants | rôles acceptés, capacité, langue, soin et critères d'arrêt |
| F · extension | évaluation de l'utilité et modifications fondées sur les résultats | décision humaine distincte ; chaque nouveau contexte est vérifié |

Critères vérifiables d'acceptation de l'implémentation :

1. Le manifest contient exactement les 13 ID de contours et les 13 locales spécifiés, sans présenter une locale vide comme une traduction complète.
2. Chaque fiche affichée possède une finalité, une source, une version, un droit d'usage, un état de maturité et un retour accessible.
3. Une locale manquante présente un état honnête ; le changement de langue est explicite, sans substitution cachée.
4. L'arabe se lit en RTL et les ID mixtes préservent le sens ; sanskrit, latin et YZH disposent des éléments distincts requis.
5. Les ressources ouvertes se lisent sans questionnaire ; aucune donnée de profil minimal n'est demandée.
6. `/pause`, `/exit` et le désabonnement fonctionnent dans tous les états testés ; la pause n'active aucune action nouvelle.
7. L'export contient seulement les données du propriétaire actuel ; la tentative d'un autre propriétaire est refusée.
8. L'effacement confirme son périmètre, supprime réellement les enregistrements contrôlés et montre honnêtement les éléments conservés légalement ou hors du contrôle du service.
9. Les journaux ordinaires ne contiennent ni corps de messages, ni secrets, ni demandes, ni chemins privés, ni histoires personnelles.
10. Une tentative de lecture hors allowlist, une instruction intégrée au contenu et un fichier inadapté ne sont pas exécutés comme commandes.
11. Une contribution volontaire passe par une modération humaine, un traitement du conflit/déport, un motif et une voie de recours ; l'attribution d'origine est conservée.
12. La couche de jeu peut être désactivée ; le texte courant transmet le même sens ; il n'y a ni sanction pour une étape passée ni classement de la dignité humaine.
13. Admission des jeunes, paiements, collecte de fonds et demandes de subvention restent désactivés jusqu'à des conditions confirmées séparément.
14. Aucun fonctionnement en réseau ou avec un modèle externe ne commence sans runtime approuvé séparément et choix clair concernant les données.
15. Clavier, focus, lecture, contraste, alternatives textuelles et réduction du mouvement sont vérifiés dans l'interface réelle.
16. Backup/restore possède un résultat testé et une restauration ne réintroduit pas des enregistrements effacés contrairement à la politique adoptée.
17. La charge et les erreurs ne mélangent pas les sessions ; l'utilisateur reçoit un état compréhensible et une sortie accessible.
18. Le rapport précise version exacte, environnement, scénario, résultat attendu et observé ; PASS se limite à ce qui a été vérifié.

Tous ces critères sont actuellement `NOT_RUN` : le document définit des exigences sans confirmer leur implémentation. La prochaine étape technique consiste à sélectionner un ensemble public de fiches et à réaliser le prototype hors ligne B après vérification de l'ensemble A.

<!-- suti:section:spec-language-states -->
## états linguistiques de cette spécification

Le russe est le brouillon source AI-first, en attente de vérification de l'auteur et d'un examen indépendant du contenu. Lors de la rédaction de ce maître, `en`, `es`, `pt-br`, `zh-hans`, `hi`, `fr`, `ar`, `bn`, `eo`, `sa`, `la`, `yzh` étaient inscrits comme `HOLD / not-started`. Cette édition française existe désormais comme brouillon éditorial dérivé directement de ce maître ; elle ne constitue pas une acceptation indépendante. YZH nécessite en plus une glose de l'auteur ; sa et la nécessitent des spécialistes ; ar exige une vérification RTL. Voir les états actuels dans `bot-spec.locale-status.v1.json`. L'autorisation de publication de toutes les éditions reste HOLD.

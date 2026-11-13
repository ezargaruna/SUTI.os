---
artifact_id: suti.bot-collaboration-spec.es.2026-11-13
source_path: bot-and-collaboration-spec.ru.md
source_locale: ru
source_sha256: 76509088c1554bb71008e7076afc0683bd2669b57b26bd0535a6b8bab19e2ffe
source_version: 2026-11-13
locale: es
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

# bot de cuidados × arquitectura colaborativa SUTI

propósito :: ofrecer a cada persona una entrada clara y voluntaria al conocimiento, la práctica, un proyecto compartido y un siguiente paso posible
estado :: specification-only · este documento no crea una implementación
idioma fuente :: ru
locale :: es
fecha :: 2026-11-13
conexiones operativas / Telegram runtime / admisión de participantes / pagos / publicación :: OFF / HOLD
fuente :: [máster ruso](bot-and-collaboration-spec.ru.md)

Esta especificación describe un motor local de contenidos y un adaptador de bot propuestos para el sistema vivo común SUTI. Cada persona activa voluntariamente la imagen de un ángel de cuidados, un chamán urbano o un samurái del dharma. Cada recorrido simbólico dispone de una formulación equivalente en lenguaje cotidiano. El bot ayuda a encontrar, expresar y comprobar un siguiente paso; las personas autorizadas toman las decisiones finales sobre apoyo, subvenciones, quejas, el papel de una persona y los gastos.

<!-- suti:section:expected-first-result -->
## primer resultado esperado

La persona elige un idioma → lee la propuesta y las limitaciones actuales → elige una pregunta o un tema disponible → recibe una tarjeta breve con una fuente y una acción posible → la guarda para sí o termina el recorrido. Leer materiales abiertos no requiere un perfil ni registro. En cada pantalla se puede pausar, omitir, volver o salir. No se solicitan por defecto nombre, fecha de nacimiento, salud, documentos, finanzas, circunstancias familiares ni historia privada.

La versión mínima consta de un catálogo local de conocimientos, 13 recorridos lingüísticos, búsqueda en las tarjetas publicadas, un recorrido voluntario NITYA y exportación de los marcadores propios. La integración funcional con un servicio de mensajería, el almacenamiento de mensajes de usuarios, un servicio de IA, un grupo comunitario, un módulo financiero y la recepción de solicitudes de subvención no forman parte automáticamente de este mínimo.

<!-- suti:section:user-routes -->
## recorridos de uso

| recorrido | acción de la persona | resultado | límite obligatorio |
|---|---|---|---|
| comprender el sistema | elegir un resumen o un ámbito | propósito claro y siguiente recorrido | la madurez actual es visible |
| encontrar material | elegir un tema o una búsqueda local | tarjeta, fuente, idioma y estado | solo aparece el catálogo público autorizado |
| microaprendizaje | elegir una práctica breve | un paso realizable y una comprobación opcional | sin penalizar omisiones, interrupción de rachas ni salida |
| mapa fusion | elegir una plantilla vacía | archivo propio editable | se completa localmente; enviarlo a alguien exige una decisión aparte |
| juego NITYA | activar explícitamente la interfaz simbólica | recorrido voluntario con equivalente en texto cotidiano | sin asignar identidad ni clasificar el valor de una persona |
| contribución compartida | abrir las reglas y proponer material público | borrador para consideración humana | derechos de autor, público y licencia se aclaran antes de incluirlo |
| ayuda humana | leer la disponibilidad y los límites del equipo | canal de contacto elegido, si realmente existe | competencia, horario y responsable confirmados; no se promete ayuda no disponible |
| fondo | leer el proyecto y el estado de sus condiciones | plan, criterios e información agregada | la recepción de dinero y solicitudes sigue desactivada hasta autorizaciones separadas |

Las etiquetas de edad 0+, 12+, 18+, 21+, 33+ y 55+ son vistas editoriales, no verificación legal de edad ni clasificaciones oficiales. La admisión de niños y jóvenes permanece desactivada hasta contar con medidas verificadas de protección de menores. Basta ofrecer el nivel de complejidad que la persona elija; no se debe recopilar la fecha exacta de nacimiento para ajustar el lenguaje o el ritmo.

<!-- suti:section:proposed-architecture -->
## componentes de la arquitectura propuesta

```text
catálogo público en .vault
    ↓ comprobar fuente, derechos, privacidad e idioma
compilador determinista del paquete público
    ↓ allowlist + manifest + SHA-256
motor local de contenidos read-only
    ├─ Obsidian / Markdown
    ├─ HTML local accesible
    └─ adaptador de bot opcional
          ↓ solo un runtime autorizado por separado
       sesión del usuario / acciones aceptadas por la persona
          ↓ consentimiento separado y minimización
       espacio privado del usuario fuera del catálogo público
```

1. **Catálogo de contenidos.** `entity_id` estable, fuente, significado invariante, alcance, límites, derechos, madurez y relaciones. El paquete público no enumera rutas privadas, contactos ni historias originales de personas.
2. **Capa lingüística.** Un máster identificado por objeto y versiones directas para cada locale. No se sustituye automáticamente un texto por una traducción no revisada presentándola como lista para usar.
3. **Enrutador.** Comandos, ámbitos y tarjetas deterministas. La primera versión no necesita un modelo generativo. La respuesta contiene un paso claro y disponible y un estado explícito.
4. **Sesión.** Estado de corta duración de la pantalla actual. Por defecto permanece en la memoria del proceso o con el usuario, no en una base pública colectiva.
5. **Adaptador.** Telegram u otro canal se conecta por separado; los secretos permanecen fuera de `.vault`, se verifica el origen de las actualizaciones y se desactivan los eventos opcionales. El transport ID técnico se considera un identificador personal y no entra en el paquete público ni en los registros ordinarios.
6. **Almacenamiento privado.** Si la persona elige guardar, los datos se ubican en un espacio privado separado, con propietario, acceso restringido, plazo y borrado probado. Una frontera física es distinta de una carpeta dentro de un vault público.
7. **Cola editorial.** Las contribuciones, objeciones, correcciones y quejas reciben acceso restringido, una persona asignada y un estado. El registro público muestra solo una decisión agregada autorizada.
8. **Verificación de publicación.** Antes de incluir un archivo se comprueban allowlist, derechos, privacidad, fuente, formato admitido, enlaces, locale y SHA. Un error detiene la compilación de esa versión concreta.

El esquema define interfaces, no la existencia de código. La implementación se elige tras revisar el proyecto existente, el apoyo del equipo, los requisitos de despliegue y el almacenamiento local.

<!-- suti:section:locales-content-loading -->
## 13 locales y carga de contenidos

locales :: `ru`, `en`, `es`, `pt-br`, `zh-hans`, `hi`, `fr`, `ar`, `bn`, `eo`, `sa`, `la`, `yzh`

Estructura propuesta del paquete público:

```text
catalog/entities.json
catalog/relations.json
locales/<locale>/interface.json
locales/<locale>/cards/<entity_id>.md
locales/<locale>/glossary.json
manifests/content.json
manifests/locale-review.json
schemas/                  # contratos técnicos
```

`content.json` enumera explícitamente archivos, tamaños, SHA-256, versión del canon y locales permitidas. El estado lingüístico se guarda por separado de la existencia del archivo: `not-started`, `draft`, `meaning-reviewed`, `native-or-expert-reviewed`, `release-approved`. Son valores enum propuestos para un contrato nuevo; no reescriben los registros históricos sin una migración aparte.

Al seleccionar una locale, el motor comprueba la disponibilidad de la tarjeta y si su estado está permitido en el modo elegido. Si falta el texto, lo explica en el idioma de la interfaz y ofrece elegir conscientemente un idioma disponible. Está prohibido sustituir una locale vacía por ruso o inglés sin avisar. Cuando se actualiza el máster, las versiones dependientes se marcan como pendientes de cotejo; un SHA antiguo no verifica un significado nuevo.

La interfaz árabe usa `dir="rtl"` y una revisión específica de lectura, tablas, números e identificadores mixtos. El sánscrito y el latín requieren especialistas; YZH requiere una glosa aprobada por el autor, con desarrollo y comprobación de comprensión. Hasta contar con esas bases, la locale recibe un HOLD explícito. El significado está disponible en texto sin animación, color ni símbolos especiales.

<!-- suti:section:proposed-commands -->
## comandos propuestos

Los ID de comandos no se traducen; las etiquetas visibles se localizan. Los comandos son una propuesta de API, no prueba de un bot conectado.

| comando | resultado |
|---|---|
| `/start` | propuesta, idioma y disponibilidad actual; sin cuestionario |
| `/language` | elección explícita de idioma y vacíos visibles |
| `/contours` | 13 ámbitos con sus propósitos breves |
| `/learn` | lección breve y acción voluntaria |
| `/quest` | activación separada del juego voluntario |
| `/map` | plantilla vacía y editable de mapa fusion |
| `/sources` | procedencia de la tarjeta pública actual |
| `/pause` | detener el recorrido y las notificaciones dentro de las facultades del servicio |
| `/resume` | reanudación explícita; no activa nuevos consentimientos |
| `/export` | datos propios guardados tras verificar la titularidad |
| `/delete` | alcance claro de borrado y confirmación del propietario |
| `/privacy` | operador, finalidad, conservación, acceso, derechos y contacto, si están aprobados |
| `/help` | navegación ordinaria accesible y límites reales de la ayuda |
| `/exit` | finalizar la sesión; explicar por separado cualquier guardado elegido |

Los envíos automáticos y las tareas diarias están desactivados por defecto. Una suscripción tiene finalidad, frecuencia, horario local y una forma sencilla de cancelarla. Un solo `/start` no significa suscribirse, aceptar tratamiento mediante IA, entrar en una comunidad ni consentir una publicación.

<!-- suti:section:data-ownership -->
## datos y titularidad

| entidad | campos mínimos | ubicación y acceso | conservación |
|---|---|---|---|
| `PublicEntity` | `entity_id`, `source_id`, `version`, `kind`, `contour_id`, `license_state`, `implementation_state` | paquete público verificado | según la política de versiones adoptada |
| `LocalizedArtifact` | `entity_id`, `locale`, `source_sha256`, `target_sha256`, `review_state`, `release_state` | textos públicos y bases seguras para el público | hasta su sustitución, conservando provenance fuera del paquete activo |
| `Relation` | `from_id`, `to_id`, `relation_type`, `evidence_ref` | catálogo público | según la versión del catálogo |
| `Session` | `session_id` aleatorio, locale, pantalla, estado de pausa | memoria o almacenamiento privado; solo propietario de la sesión y proceso | plazo mínimo; el TTL concreto se aprueba y prueba antes del runtime |
| `TransportBinding` | identificador técnico del canal y vínculo con una sesión privada | almacenamiento separado y restringido; no registros públicos | plazo justificado para el canal elegido; borrado según escenario |
| `SavedItem` | `owner_id`, `entity_id`, anotación de la persona, hora | con el usuario por defecto; guardar en servidor requiere opt-in separado | plazo elegido; corrección, exportación y borrado |
| `ConsentRecord` | finalidad, versión de la explicación, alcance, elección, hora y retirada | almacenamiento privado separado | según la obligación aplicable; sin plazo perpetuo e indefinido |
| `ContributionDraft` | texto público propuesto, condiciones de autor, autoría visible elegida | cola editorial restringida antes de aprobar | plazo de cola y retirada explicados antes del envío |
| `ModerationDecision` | ID de contribución, regla, motivo, editor humano, recurso | registro restringido; resultado público desidentificado y comprobado | según la política adoptada |
| `OperationalEvent` | hora, código de evento, versión del paquete, duración/error sin cuerpo del mensaje | registro mínimo y restringido | plazo breve aprobado; no copia de conversaciones |

El texto personal libre no es un campo obligatorio. El registro estándar no conserva cuerpos de mensajes, IP completas, geolocalización, contactos ni historias de ayuda. No se agregan datos de otras personas desde agendas, chats o archivos para obtener un «mapa completo». No se correlacionan canales sin una elección separada y clara del propietario y una justificación.

La exportación verifica al propietario en una sesión autenticada vigente e incluye solo sus propios datos; muestra el formato y el alcance antes de ejecutar. El borrado explica primero los registros afectados y posibles excepciones legales, exige confirmación del propietario y devuelve un resultado con los ámbitos `deleted`, `retained_with_basis`, `unknown`. No se debe prometer borrar mensajes de la infraestructura de otro servicio de mensajería ni de copias de terceros si el servicio no las controla. Las copias de seguridad del servidor requieren un plazo de caducidad probado y un tratamiento de las restauraciones.

<!-- suti:section:api-proposals -->
## propuestas de API

Las rutas siguientes son propuestas de contrato; los endpoints no están implementados.

| método y ruta | finalidad | control |
|---|---|---|
| `GET /v1/catalog?locale=<slug>` | listar entidades públicas permitidas | read-only; límite de tamaño; estado explícito de locale |
| `GET /v1/entities/<entity_id>?locale=<slug>` | tarjeta y fuente | ID del manifest; protección frente a rutas de archivo arbitrarias |
| `POST /v1/sessions` | sesión mínima | plazo breve; sin perfil opcional |
| `PATCH /v1/sessions/<id>` | locale, pantalla, pausa | verificar propietario; lista de campos permitidos |
| `POST /v1/consents` | elección separada para una finalidad concreta | versión del texto, alcance y posibilidad de retirada |
| `DELETE /v1/consents/<id>` | retirar una elección concreta | verificar propietario; detener la acción futura asociada |
| `POST /v1/exports` | exportación propia | verificar propietario; enlace de corta duración o archivo local |
| `POST /v1/deletion-requests` | borrado confirmado con alcance explícito | nueva confirmación; registro del resultado sin cuerpo de datos |
| `POST /v1/contributions` | contribución propuesta segura para publicación | opt-in separado, reglas y moderación antes del runtime |
| `POST /v1/reviews/<id>/decisions` | decisión editorial humana | rol aceptado; motivo; conflicto/recusación; historial de cambios |
| `GET /v1/fund/status` | solo estado del proyecto y de las condiciones | sin información bancaria ni solicitudes personales |

La versión mínima no incluye operaciones de pago ni subvención. Cualquier ruta financiera futura necesita contrato y autorización propios; hasta entonces `payments_enabled=false`, `fundraising_enabled=false`, `grant_intake_enabled=false`. Las monedas simbólicas de SUTI no invocan una API financiera ni dan ventajas para recibir apoyo.

<!-- suti:section:ai-human-decisions -->
## IA y decisiones humanas

La generación es opcional. La primera versión puede ser totalmente determinista. Si más adelante se conecta un modelo, el usuario conoce qué datos llegarán a dónde, con qué finalidad y durante cuánto tiempo; el tratamiento mediante IA tiene una elección separada. No se envían por defecto corpus privados ni solicitudes a un proveedor externo. El acceso técnico a un modelo local no sustituye una base para tratar datos. Las tarjetas públicas se separan del texto libre del usuario; las instrucciones de los documentos se tratan como datos, no como facultades para actuar.

La respuesta del modelo cita fuentes permitidas y distingue observación, interpretación, hipótesis y desconocimiento. Si no hay base, comunica el límite y propone un paso disponible y comprobable. El modelo no asigna identidad, no diagnostica, no determina el valor de una persona, no promete ayuda ni decide pagos. El neuro-veche se señala como simulación editorial; las respuestas reales de personas se registran por separado.

<!-- suti:section:visual-content-collaboration -->
## desarrollo colaborativo de imagen y contenido

La estética común es una luz terrestre serena, tipografía legible, densidad moderada y significado comprensible sin un glifo decorativo. Las imágenes de cuidados, flamenco, halcón, Garuna, Finist, chamanes urbanos y Samurai Dharma se activan como capa artística voluntaria con procedencia y autoría. Los escenarios básicos funcionan sin animación, sonido ni símbolos. Se requieren control manual del movimiento, soporte de movimiento reducido, teclado, foco visible, contraste suficiente y alternativas textuales; una revisión separada de la implementación verifica estos requisitos.

La colaboración avanza mediante resultados claros: acordar tarea y derechos → elegir un recorrido de uso → comparar varios bocetos → comprobar comprensión y accesibilidad → entregar fuentes editables → construir un prototipo → revisar → aceptar un resultado delimitado. Los colaboradores definen su propio marco adecuado, modalidad de participación, alcance, plazos y remuneración deseada. La entrega gratuita de material de autor se documenta aparte de un encargo de desarrollo; un regalo no crea la obligación de trabajar gratis. No se anuncia colaboración, consentimiento, marca común ni licencia sobre material ajeno antes de una aceptación explícita.

Posibles objetos de colaboración: bot lingüístico; catálogo de 13 idiomas; editor visual de mapas; recorridos NITYA accesibles; tarjetas educativas; mundos generativos; serie de historias breves voluntarias; sistema transparente de proyectos pequeños. Importe, moneda, derechos sobre código y diseño, soporte, infraestructura y criterio de aceptación se fijan en un encargo separado y acordado. Las páginas públicas de un colaborador y haber realizado un curso no autorizan extraer lecciones cerradas, datos de su público ni presentar a ese público como participantes.

<!-- suti:section:thirteen-contours -->
## los 13 ámbitos en un contrato

| ámbito | objeto y función del bot |
|---|---|
| SUTI.os | límites, configuración, roles, versiones, backup/rollback |
| SUTI.world | entrada pública y recorrido elegido por la persona |
| SUTI.uni | microaprendizaje, ejercicio, resultado observable |
| SUTI.clan | círculo voluntario y rol aceptado; sin ingreso automático |
| SUTI.lab | entorno sintético y experimento delimitado |
| SUTI.audit | evidencias, comprobaciones de alcance definido y correcciones |
| SUTI.crystal | tarjeta clara de conocimientos con fuente y límite |
| SUTI.oracle | preguntas alternativas; hipótesis identificada |
| SUTI.veche | deliberación humana, desacuerdo y resultado con responsable |
| SUTI.sotkan | relaciones entre entidades, dependencias y provenance |
| SUTI.game | recorrido simbólico voluntario; lenguaje cotidiano disponible |
| SUTI.logos | términos, voz, transcreación directa y control de pérdidas |
| SUTI.verenium | siguiente paso realizable, pausa, salida y límites de la ayuda |

<!-- suti:section:implementation-acceptance -->
## etapas de implementación y aceptación

| etapa | resultado concreto | condición para avanzar |
|---|---|---|
| A · catálogo | canon, 13 ámbitos, allowlist, manifest, fuentes y estados lingüísticos reales | conjunto seleccionado seguro para publicar; enlaces y SHA verificados |
| B · prototipo sin conexión | lectura, idioma, búsqueda, recorrido, exportación de marcadores propios | recorridos principales comprobados manualmente, con teclado y sin red |
| C · ensayo | sesiones sintéticas, rechazo, retirada, borrado, moderación, fallo y recuperación | resultados esperados comprobados; sin filtración entre propietarios |
| D · adaptador | bot autorizado por separado en un entorno delimitado | operador, secretos, datos, registros, límites y protección confirmados |
| E · piloto delimitado | un contexto elegido con adultos que consienten | roles aceptados, capacidad, idioma, cuidados y criterios de parada |
| F · ampliación | evaluación de utilidad y cambios basados en evidencia | decisión humana separada; se verifica cada contexto nuevo |

Criterios verificables de aceptación de la implementación:

1. El manifest contiene exactamente los 13 ID de ámbitos y las 13 locales especificados, sin presentar una locale vacía como traducción completa.
2. Cada tarjeta mostrada tiene finalidad, fuente, versión, derecho de uso, madurez y un recorrido accesible de regreso.
3. Una locale ausente muestra un estado honesto; el cambio de idioma es explícito, sin sustitución oculta.
4. El árabe se lee en RTL y los ID mixtos preservan el significado; sánscrito, latín y YZH cuentan con las bases separadas requeridas.
5. Los materiales abiertos se leen sin cuestionario; no se solicitan datos de un perfil mínimo.
6. `/pause`, `/exit` y la cancelación de suscripción funcionan en todos los estados probados; la pausa no activa nuevas acciones.
7. La exportación contiene solo datos del propietario actual; se rechaza el intento de otro propietario.
8. El borrado confirma su alcance, elimina realmente los registros controlados y muestra con honestidad lo conservado legalmente y lo que queda fuera de control.
9. El registro ordinario no contiene cuerpos de mensajes, secretos, solicitudes, rutas privadas ni historias personales.
10. No se ejecutan como órdenes un intento de leer fuera de la allowlist, una instrucción incrustada en contenidos ni un archivo inadecuado.
11. La contribución voluntaria pasa por moderación humana, gestión de conflicto/recusación, motivo y vía de recurso; se conserva la autoría original.
12. La capa de juego se puede desactivar; el texto cotidiano transmite el mismo significado; no hay penalización por omitir ni rangos de dignidad humana.
13. La admisión juvenil, pagos, recaudación y solicitudes de subvención permanecen desactivados hasta cumplir condiciones confirmadas por separado.
14. No se inicia la operación en red ni con un modelo externo sin un runtime aprobado por separado y una elección clara sobre los datos.
15. Se comprueban teclado, foco, lectura, contraste, alternativas textuales y movimiento reducido en la interfaz real.
16. Backup/restore tiene un resultado probado y la restauración no recupera registros borrados en contra de la política adoptada.
17. La carga y los errores no mezclan sesiones; el usuario recibe un estado comprensible y una salida accesible.
18. El informe indica versión exacta, entorno, escenario, resultado esperado y observado; PASS se limita a lo comprobado.

Todos los criterios anteriores están actualmente `NOT_RUN`: el documento establece requisitos, no confirma su implementación. El siguiente paso técnico es seleccionar un conjunto público de tarjetas e implementar el prototipo sin conexión B después de comprobar el conjunto A.

<!-- suti:section:spec-language-states -->
## estados lingüísticos de esta especificación

El ruso es el borrador fuente AI-first, pendiente de revisión del autor e independiente del contenido. Al redactarse ese máster, `en`, `es`, `pt-br`, `zh-hans`, `hi`, `fr`, `ar`, `bn`, `eo`, `sa`, `la`, `yzh` figuraban como `HOLD / not-started`. Esta versión española es ahora un borrador editorial directo de ese máster, sin aceptación independiente. YZH requiere además glosa del autor; sa y la requieren especialistas; ar requiere revisión RTL. Los registros actuales están en `bot-spec.locale-status.v1.json`. La autorización de publicación de todas las versiones sigue en HOLD.

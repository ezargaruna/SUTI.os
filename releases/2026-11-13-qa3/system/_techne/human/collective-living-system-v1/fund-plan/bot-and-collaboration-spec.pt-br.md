---
artifact_id: suti.bot-collaboration-spec.pt-br.2026-11-13
source_path: bot-and-collaboration-spec.ru.md
source_locale: ru
source_sha256: 76509088c1554bb71008e7076afc0683bd2669b57b26bd0535a6b8bab19e2ffe
source_version: 2026-11-13
locale: pt-br
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

# bot de cuidado × arquitetura colaborativa SUTI

finalidade :: oferecer à pessoa uma entrada clara e voluntária no conhecimento, na prática, em um projeto compartilhado e em um próximo passo possível
estado :: specification-only · este documento não cria uma implementação
idioma-fonte :: ru
locale :: pt-br
data :: 2026-11-13
conexões operacionais / Telegram runtime / admissão de participantes / pagamentos / publicação :: OFF / HOLD
fonte :: [mestre russo](bot-and-collaboration-spec.ru.md)

Esta especificação descreve um motor local de conteúdo e um adaptador de bot propostos para o sistema vivo comum SUTI. A pessoa ativa voluntariamente a imagem de anjo de cuidado, xamã urbano ou samurai do dharma. Cada percurso simbólico tem uma formulação equivalente em linguagem cotidiana. O bot ajuda a encontrar, expressar e verificar um próximo passo; pessoas autorizadas tomam as decisões finais sobre apoio, subsídios, reclamações, o papel da pessoa e os gastos.

<!-- suti:section:expected-first-result -->
## primeiro resultado esperado

A pessoa escolhe o idioma → lê a proposta e as limitações atuais → escolhe uma pergunta ou um tema disponível → recebe um cartão curto com fonte e ação possível → salva para si ou encerra o percurso. A leitura de materiais abertos não exige perfil nem cadastro. Todas as telas oferecem pausa, pular, voltar e sair. Nome, data de nascimento, saúde, documentos, finanças, circunstâncias familiares e história privada não são solicitados por padrão.

A versão mínima contém um catálogo local de conhecimento, 13 percursos linguísticos, busca nos cartões publicados, uma jornada voluntária NITYA e exportação dos próprios favoritos. Integração funcional com mensageiro, armazenamento de mensagens de usuários, serviço de IA, grupo comunitário, módulo financeiro e recebimento de pedidos de subsídio não fazem parte automaticamente desse mínimo.

<!-- suti:section:user-routes -->
## percursos de uso

| percurso | ação da pessoa | resultado | limite obrigatório |
|---|---|---|---|
| entender o sistema | escolher resumo ou contorno | finalidade clara e próximo percurso | a maturidade atual fica visível |
| encontrar material | escolher tema ou busca local | cartão, fonte, idioma e estado | resultados apenas do catálogo público autorizado |
| microaprendizagem | escolher prática curta | um passo viável e verificação opcional | sem punição por pular, interromper sequência ou sair |
| mapa fusion | escolher modelo vazio | arquivo próprio editável | preenchimento local; envio a alguém é escolha separada |
| jogo NITYA | ativar explicitamente a interface simbólica | jornada voluntária com equivalente em texto cotidiano | sem identidade atribuída nem classificação do valor da pessoa |
| contribuição conjunta | abrir regras e propor material público | rascunho para análise humana | direitos autorais, público e licença são esclarecidos antes da inclusão |
| ajuda humana | ler disponibilidade e limites da equipe | canal escolhido de contato, se realmente existir | competência, horário e responsável confirmados; não se promete apoio indisponível |
| fundo | ler o projeto e o estado das condições | plano, critérios e informações agregadas | recebimento de dinheiro e pedidos desativado até autorizações separadas |

As marcações etárias 0+, 12+, 18+, 21+, 33+ e 55+ são apresentações editoriais, não verificação legal de idade nem classificações oficiais. A admissão de crianças e jovens permanece desativada até existir uma estrutura verificada de proteção de menores. Basta oferecer o nível de complexidade escolhido pela pessoa; não se coleta a data exata de nascimento para ajustar idioma ou ritmo.

<!-- suti:section:proposed-architecture -->
## componentes da arquitetura proposta

```text
catálogo público na .vault
    ↓ verificar fonte, direitos, privacidade e idioma
construtor determinístico do pacote público
    ↓ allowlist + manifest + SHA-256
motor local de conteúdo read-only
    ├─ Obsidian / Markdown
    ├─ HTML local acessível
    └─ adaptador opcional de bot
          ↓ apenas runtime autorizado separadamente
       sessão do usuário / ações aceitas pela pessoa
          ↓ consentimento separado e minimização
       espaço privado do usuário fora do catálogo público
```

1. **Catálogo de conteúdo.** `entity_id` estável, fonte, significado invariante, escopo, limites, direitos, maturidade e relações. O pacote público não lista caminhos privados, contatos nem histórias originais de pessoas.
2. **Camada linguística.** Um mestre identificado por objeto e versões diretas por locale. Não há substituição automática por uma tradução não revisada apresentada como texto pronto.
3. **Roteador.** Comandos, contornos e cartões determinísticos. A primeira versão dispensa modelo generativo. A resposta apresenta um passo claro e disponível e um estado explícito.
4. **Sessão.** Estado de curta duração da tela atual. Por padrão, fica na memória do processo ou com o usuário, não em uma base pública coletiva.
5. **Adaptador.** Telegram ou outro canal é conectado separadamente; segredos ficam fora da `.vault`, a origem das atualizações é verificada e eventos opcionais são desativados. O transport ID técnico é tratado como identificador pessoal e não entra no pacote público nem nos logs comuns.
6. **Armazenamento privado.** Se a pessoa escolher salvar, os dados ficam em um espaço privado separado, com proprietário, acesso restrito, prazo e exclusão testada. Uma separação física é diferente de uma pasta dentro de um vault público.
7. **Fila editorial.** Contribuições, objeções, correções e reclamações recebem acesso restrito, uma pessoa designada e um estado. O registro público mostra apenas a decisão agregada autorizada.
8. **Verificação de publicação.** Antes de incluir um arquivo, verificam-se allowlist, direitos, privacidade, fonte, formato aceito, links, locale e SHA. Um erro interrompe a construção daquela versão específica.

O esquema define interfaces, não a existência de código. A implementação é escolhida após conferir o projeto existente, o suporte da equipe, os requisitos de implantação e o armazenamento local.

<!-- suti:section:locales-content-loading -->
## 13 locales e carregamento de conteúdo

locales :: `ru`, `en`, `es`, `pt-br`, `zh-hans`, `hi`, `fr`, `ar`, `bn`, `eo`, `sa`, `la`, `yzh`

Estrutura proposta do pacote público:

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

`content.json` lista explicitamente arquivos, tamanhos, SHA-256, versão do cânone e locales permitidas. O estado linguístico é guardado separadamente da presença do arquivo: `not-started`, `draft`, `meaning-reviewed`, `native-or-expert-reviewed`, `release-approved`. São valores enum propostos para um novo contrato; não reescrevem registros históricos sem uma migração separada.

Ao escolher uma locale, o motor verifica a disponibilidade do cartão e se o estado é permitido para o modo escolhido. Se o texto estiver ausente, informa isso no idioma da interface e oferece uma escolha consciente de idioma disponível. É proibido substituir uma locale vazia por russo ou inglês sem avisar. Quando o mestre muda, as versões dependentes recebem indicação de que precisam ser conferidas; um SHA antigo não verifica um significado novo.

A interface árabe usa `dir="rtl"` e uma revisão específica de leitura, tabelas, números e identificadores mistos. Sânscrito e latim exigem especialistas; YZH exige glosa aprovada pelo autor, com desenvolvimento e verificação de compreensão. Até haver essas bases, a locale recebe um HOLD explícito. O significado está disponível em texto sem animação, cor nem símbolos especiais.

<!-- suti:section:proposed-commands -->
## comandos propostos

Os IDs dos comandos não são traduzidos; os rótulos visíveis são localizados. Os comandos são uma proposta de API, não evidência de um bot conectado.

| comando | resultado |
|---|---|
| `/start` | proposta, idioma e disponibilidade atual; sem questionário |
| `/language` | escolha explícita de idioma e lacunas visíveis |
| `/contours` | 13 contornos com suas finalidades breves |
| `/learn` | lição curta e ação voluntária |
| `/quest` | ativação separada do jogo voluntário |
| `/map` | modelo vazio e editável de mapa fusion |
| `/sources` | procedência do cartão público atual |
| `/pause` | interromper percurso e notificações dentro das atribuições do serviço |
| `/resume` | retomada explícita; não ativa novos consentimentos |
| `/export` | próprios dados salvos após verificar a titularidade |
| `/delete` | escopo claro de exclusão e confirmação do proprietário |
| `/privacy` | operador, finalidade, retenção, acesso, direitos e contato, se aprovados |
| `/help` | navegação comum acessível e limites reais da ajuda |
| `/exit` | encerrar a sessão; explicar qualquer salvamento escolhido separadamente |

Envios automáticos e tarefas diárias ficam desativados por padrão. Uma assinatura tem finalidade, frequência, horário local e opção simples de cancelar. Um único `/start` não significa assinatura, processamento por IA, entrada na comunidade nem consentimento para publicação.

<!-- suti:section:data-ownership -->
## dados e titularidade

| entidade | campos mínimos | local e acesso | retenção |
|---|---|---|---|
| `PublicEntity` | `entity_id`, `source_id`, `version`, `kind`, `contour_id`, `license_state`, `implementation_state` | pacote público verificado | segundo a política de versões adotada |
| `LocalizedArtifact` | `entity_id`, `locale`, `source_sha256`, `target_sha256`, `review_state`, `release_state` | textos públicos e bases seguras para publicação | até substituição, preservando provenance fora do pacote ativo |
| `Relation` | `from_id`, `to_id`, `relation_type`, `evidence_ref` | catálogo público | segundo a versão do catálogo |
| `Session` | `session_id` aleatório, locale, tela, estado de pausa | memória ou armazenamento privado; apenas proprietário da sessão e processo | prazo mínimo; TTL específico aprovado e testado antes do runtime |
| `TransportBinding` | identificador técnico do canal e vínculo com sessão privada | armazenamento separado e restrito; não logs públicos | prazo justificado para o canal escolhido; exclusão conforme cenário |
| `SavedItem` | `owner_id`, `entity_id`, anotação da pessoa, horário | com o usuário por padrão; salvar no servidor requer opt-in separado | prazo escolhido; correção, exportação e exclusão |
| `ConsentRecord` | finalidade, versão da explicação, escopo, escolha, horário e retirada | armazenamento privado separado | conforme obrigação aplicável; sem prazo perpétuo indefinido |
| `ContributionDraft` | texto público proposto, condições autorais, autoria exibida escolhida | fila editorial restrita antes da aprovação | prazo da fila e retirada explicados antes do envio |
| `ModerationDecision` | ID da contribuição, regra, motivo, editor humano, recurso | registro restrito; resultado público desidentificado e verificado | segundo a política adotada |
| `OperationalEvent` | horário, código do evento, versão do pacote, duração/erro sem corpo da mensagem | log mínimo e restrito | prazo curto aprovado; não uma cópia de conversas |

Texto pessoal livre não é campo obrigatório. Corpos de mensagens, IPs completos, geolocalização, contatos e históricos de apoio não são gravados no log padrão. Não se acrescentam dados de outras pessoas a partir de agendas, chats ou arquivos para formar um “mapa completo”. Não se correlacionam canais sem escolha separada e clara do proprietário e uma justificativa.

A exportação verifica o proprietário em uma sessão autenticada vigente e inclui apenas seus próprios dados; formato e escopo aparecem antes da execução. A exclusão primeiro explica os registros afetados e possíveis exceções legais, pede confirmação do proprietário e entrega um resultado com os escopos `deleted`, `retained_with_basis`, `unknown`. Não se promete apagar mensagens da infraestrutura de outro mensageiro ou de backups de terceiros se o serviço não os controla. Backups do servidor exigem prazo de expiração testado e tratamento das restaurações.

<!-- suti:section:api-proposals -->
## propostas de API

As rotas abaixo são propostas de contrato; os endpoints não estão implementados.

| método e rota | finalidade | controle |
|---|---|---|
| `GET /v1/catalog?locale=<slug>` | listar entidades públicas permitidas | read-only; limite de tamanho; estado explícito de locale |
| `GET /v1/entities/<entity_id>?locale=<slug>` | cartão e fonte | ID do manifest; proteção contra caminhos arbitrários de arquivo |
| `POST /v1/sessions` | sessão mínima | prazo curto; sem perfil opcional |
| `PATCH /v1/sessions/<id>` | locale, tela, pausa | verificar proprietário; lista de campos permitidos |
| `POST /v1/consents` | escolha separada para finalidade específica | versão do texto, escopo e possibilidade de retirada |
| `DELETE /v1/consents/<id>` | retirar escolha específica | verificar proprietário; interromper ação futura associada |
| `POST /v1/exports` | exportar os próprios dados | verificar proprietário; link de curta duração ou arquivo local |
| `POST /v1/deletion-requests` | exclusão confirmada em escopo explícito | nova confirmação; log do resultado sem corpo dos dados |
| `POST /v1/contributions` | contribuição proposta segura para publicação | opt-in separado, regras e moderação antes do runtime |
| `POST /v1/reviews/<id>/decisions` | decisão editorial humana | papel aceito; motivo; conflito/impedimento; histórico de alterações |
| `GET /v1/fund/status` | apenas estado do projeto e das condições | sem informações bancárias nem pedidos pessoais |

A versão mínima não contém operações de pagamento ou subsídio. Toda futura rota financeira exige contrato e autorização separados; até lá `payments_enabled=false`, `fundraising_enabled=false`, `grant_intake_enabled=false`. Moedas simbólicas SUTI não acionam API financeira nem dão vantagem na seleção para apoio.

<!-- suti:section:ai-human-decisions -->
## IA e decisões humanas

A geração é opcional. A primeira versão pode ser inteiramente determinística. Se um modelo for conectado depois, o usuário é informado de quais dados irão para onde, com qual finalidade e por quanto tempo; o processamento por IA é uma escolha separada. Corpus privados e pedidos não são enviados por padrão a um provedor externo. Acesso técnico a um modelo local não substitui a base para o tratamento. Cartões públicos são separados do texto livre do usuário; instruções em documentos são tratadas como dados, não como autorização para agir.

A resposta do modelo cita fontes permitidas e distingue observação, interpretação, hipótese e desconhecido. Se faltar fundamento, informa a limitação e propõe um passo disponível e verificável. O modelo não atribui identidade, não diagnostica, não define o valor de uma pessoa, não promete ajuda nem decide pagamentos. O neuro-veche é identificado como simulação editorial; respostas reais de pessoas são registradas separadamente.

<!-- suti:section:visual-content-collaboration -->
## desenvolvimento conjunto do visual e do conteúdo

A estética comum é uma luz terrestre serena, tipografia legível, densidade moderada e significado compreensível sem um glifo decorativo. Imagens de cuidado, flamingo, falcão, Garuna, Finist, xamãs urbanos e Samurai Dharma são ativadas como camada artística voluntária com procedência e autoria. Os cenários básicos funcionam sem animação, som nem símbolos. Exigem-se controle manual do movimento, suporte a movimento reduzido, teclado, foco visível, contraste suficiente e alternativas textuais; a implementação desses requisitos é confirmada em verificação separada.

A colaboração avança por resultados claros: acordar tarefa e direitos → escolher um percurso de uso → comparar esboços → verificar compreensão e acessibilidade → entregar fontes editáveis → montar protótipo → revisar → aceitar resultado delimitado. Os parceiros definem seu enquadramento adequado, formato de participação, escopo, prazos e remuneração desejada. A doação gratuita de material autoral é documentada separadamente de uma encomenda de desenvolvimento; o presente não cria obrigação de trabalhar gratuitamente. Não se anuncia parceria, consentimento, marca comum ou licença sobre materiais alheios antes da aceitação explícita.

Objetos de colaboração propostos: bot de idiomas; catálogo em 13 idiomas; editor visual de mapas; jornadas NITYA acessíveis; cartões de aprendizagem; mundos generativos; série de histórias curtas voluntárias; sistema transparente de pequenos projetos. Valor do pagamento, moeda, direitos sobre código e design, suporte, infraestrutura e critério de aceitação são fixados em encomenda separada e acordada. As páginas públicas de um parceiro e a conclusão de um curso não autorizam extrair aulas fechadas, dados de público nem apresentar esse público como participantes.

<!-- suti:section:thirteen-contours -->
## todos os 13 contornos em um contrato

| contorno | objeto e função do bot |
|---|---|
| SUTI.os | limites, configuração, papéis, versões, backup/rollback |
| SUTI.world | entrada pública e percurso escolhido pela pessoa |
| SUTI.uni | microaprendizagem, exercício, resultado observável |
| SUTI.clan | círculo voluntário e papel aceito; sem adesão automática |
| SUTI.lab | ambiente sintético e experimento delimitado |
| SUTI.audit | evidências, verificações de escopo definido e correções |
| SUTI.crystal | cartão claro de conhecimento com fonte e limite |
| SUTI.oracle | perguntas alternativas; hipótese identificada |
| SUTI.veche | deliberação humana, discordância e resultado com responsável |
| SUTI.sotkan | relações entre entidades, dependências e provenance |
| SUTI.game | jornada simbólica voluntária; linguagem cotidiana disponível |
| SUTI.logos | termos, voz, transcriações diretas e controle de perdas |
| SUTI.verenium | próximo passo viável, pausa, saída e limites da ajuda |

<!-- suti:section:implementation-acceptance -->
## etapas de implementação e aceitação

| etapa | resultado concreto | condição para avançar |
|---|---|---|
| A · catálogo | cânone, 13 contornos, allowlist, manifest, fontes e estados linguísticos reais | conjunto escolhido seguro para publicação; links e SHA verificados |
| B · protótipo offline | leitura, idioma, busca, jornada, exportação dos próprios favoritos | percursos principais testados manualmente, por teclado e sem rede |
| C · ensaio | sessões sintéticas, recusa, retirada, exclusão, moderação, falha e recuperação | resultados esperados verificados; sem vazamento entre proprietários |
| D · adaptador | bot autorizado separadamente em ambiente delimitado | operador, segredos, dados, log, limites e proteção confirmados |
| E · piloto delimitado | um contexto escolhido com adultos que consentem | papéis aceitos, capacidade, idioma, cuidado e critérios de parada |
| F · ampliação | avaliação de utilidade e mudanças baseadas em evidências | decisão humana separada; cada novo contexto é verificado |

Critérios verificáveis de aceitação da implementação:

1. O manifest contém exatamente os 13 IDs de contornos e as 13 locales especificadas, sem apresentar locale vazia como tradução completa.
2. Cada cartão exibido tem finalidade, fonte, versão, direito de uso, maturidade e percurso acessível de retorno.
3. Uma locale ausente mostra seu estado real; a troca de idioma é explícita, sem substituição oculta.
4. O árabe é legível em RTL e IDs mistos preservam o significado; sânscrito, latim e YZH têm as bases específicas exigidas.
5. Materiais abertos podem ser lidos sem questionário; não se solicitam dados de perfil mínimo.
6. `/pause`, `/exit` e cancelamento da assinatura funcionam em todos os estados testados; a pausa não ativa novas ações.
7. A exportação contém somente dados do proprietário atual; uma tentativa de outro proprietário é rejeitada.
8. A exclusão confirma o escopo, remove de fato registros controlados e mostra com honestidade o que é retido legalmente ou está fora de controle.
9. O log comum não contém corpos de mensagens, segredos, pedidos, caminhos privados nem histórias pessoais.
10. Tentativa de ler caminho fora da allowlist, instrução inserida no conteúdo e arquivo inadequado não são executados como comandos.
11. A contribuição voluntária passa por moderação humana, gestão de conflito/impedimento, motivo e via de recurso; a autoria original é preservada.
12. A camada de jogo pode ser desativada; o texto cotidiano transmite o mesmo significado; não há punições por pular nem níveis de dignidade humana.
13. Admissão juvenil, pagamentos, captação de recursos e pedidos de subsídio ficam desativados até condições confirmadas separadamente.
14. A operação em rede e com modelo externo não começa sem runtime aprovado separadamente e escolha clara sobre os dados.
15. Teclado, foco, leitura, contraste, alternativas textuais e movimento reduzido são verificados na interface real.
16. Backup/restore tem resultado testado e a restauração não devolve registros excluídos contra a política adotada.
17. Carga e erros não misturam sessões; o usuário recebe estado compreensível e saída acessível.
18. O relatório informa versão exata, ambiente, cenário, resultado esperado e observado; PASS se limita ao que foi verificado.

Todos os critérios acima estão atualmente `NOT_RUN`: o documento define requisitos, não confirma sua implementação. O próximo passo técnico é escolher um conjunto público de cartões e implementar o protótipo offline B após verificar o conjunto A.

<!-- suti:section:spec-language-states -->
## estados linguísticos desta especificação

O texto russo é o rascunho-fonte AI-first, pendente de revisão autoral e independente do conteúdo. Quando esse mestre foi escrito, `en`, `es`, `pt-br`, `zh-hans`, `hi`, `fr`, `ar`, `bn`, `eo`, `sa`, `la`, `yzh` estavam registrados como `HOLD / not-started`. Esta edição em português brasileiro agora é um rascunho editorial direto desse mestre; não constitui aceitação independente. YZH exige ainda glosa autoral; sa e la exigem especialistas; ar exige revisão RTL. Consulte os registros atuais em `bot-spec.locale-status.v1.json`. A liberação de todas as edições para publicação continua em HOLD.

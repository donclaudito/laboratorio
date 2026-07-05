# Gerador de Solicitação de Exames

Aplicação web para profissionais de saúde (médicos) montarem solicitações de exames
laboratoriais, de imagem e procedimentos de forma estruturada, e exportá-las em
Markdown, PDF ou para impressão direta.

---

## Visão Geral

O **Gerador de Solicitação de Exames** é uma ferramenta clínica voltada ao
Dr. Claudio M Orenstein (CRM-SP 58120) para acelerar e padronizar a emissão de
solicitações médicas. O profissional seleciona exames organizados por categorias
clínicas (metabólicos, renais, hepáticos, hormonais, urina/fezes, pré-operatórios,
imagem, endoscopia etc.), vincula um paciente e gera um documento formatado em
Markdown que pode ser copiado, exportado para PDF ou impresso — sempre com
cabeçalho identificando o médico, CRM, data e dados do paciente.

A interface prioriza agilidade: painéis em colunas, seleção por checkbox/radio,
modelos reutilizáveis e gestão de pacientes persistida em banco de dados.

---

## Stack Tecnológica

- **Frontend:** React 18 + Vite
- **Estilização:** Tailwind CSS + shadcn/ui (Radix UI)
- **Ícones:** lucide-react
- **Roteamento:** react-router-dom
- **Estado/Dados:** @tanstack/react-query + Base44 SDK (`@base44/sdk`)
- **Geração de PDF:** jsPDF
- **Outros libs:** date-fns, lodash, react-markdown, framer-motion
- **Backend/BaaS:** Base44 (auth, banco de dados, hospedagem, integrações)

---

## Funcionalidades Implementadas

- ✅ Seleção de exames por categoria (5 painéis em colunas + 5 seções adicionais)
- ✅ Painéis: Metabólicos, Renal/Hepática, Geral/Hormonal, Urina/Fezes, Pré-Operatórios
- ✅ Seções de imagem: ECG, Raio-X, Ultrassom, Tomografia, Ressonância, Endoscopia/Colonoscopia
- ✅ Grupos de radio para protocolos com contraste (TC/RM) — seleção mutuamente exclusiva
- ✅ Gestão de pacientes (criar, listar, selecionar, excluir)
- ✅ Modelos de solicitação salvos (conjuntos reutilizáveis de exames)
- ✅ Geração de documento em Markdown
- ✅ Cópia para área de transferência
- ✅ Exportação para PDF profissional (cabeçalho, rodapé, paginação automática)
- ✅ Impressão direta via iframe oculto
- ✅ Interface responsiva (mobile + desktop)
- ✅ Ícones Lucide com fundos coloridos por categoria
- ✅ Layout A4 otimizado (margens 12mm, sem duplicação do nome do paciente)

---

## Entidades (Banco de Dados)

### `Paciente`
| Campo | Tipo | Descrição |
|-------|------|-----------|
| `nome` | string | Nome completo (obrigatório) |
| `idade` | number | Idade do paciente |
| `paciente_id` | string | ID ou prontuário |

### `ModeloSolicitacao`
| Campo | Tipo | Descrição |
|-------|------|-----------|
| `nome` | string | Nome do modelo, ex: "Check-up Geral" (obrigatório) |
| `descricao` | string | Descrição opcional |
| `exames` | object | Mapa de exames selecionados por seção |

### `User` (entidade built-in)
- Gerenciada pelo Base44: `id`, `email`, `full_name`, `role`, `created_date`
- Apenas admins podem listar/editar/excluir outros usuários
- Convites via `base44.users.inviteUser(email, role)`

---

## Integrações de IA

O app utiliza o pacote de integrações `Core` do Base44, que disponibiliza:

- **InvokeLLM** — chamadas a LLM com prompt, schema JSON opcional e contexto da web
- **GenerateImage** — geração de imagens via IA
- **GenerateSpeech** — TTS (texto para fala)
- **GenerateVideo** — geração de vídeos curtos via IA
- **TranscribeAudio** — transcrição de áudio (Whisper)
- **UploadFile / UploadPrivateFile** — armazenamento de arquivos
- **ExtractDataFromUploadedFile** — extração estruturada de PDF/CSV/Excel/Imagem
- **SendEmail** — envio de e-mails transacionais

> ⚠️ Atualmente o app não consome ativamente InvokeLLM em fluxos de UI, mas a
> infraestrutura está disponível para futuras features como sugestão de exames
> baseada em quadro clínico, ou extração de dados de laudos anteriores.

---

## Segurança como Ativo de Confiança

- **Autenticação gerenciada pelo Base44** — tokens, sessões e verificação de e-mail
  são responsabilidade da plataforma; o app não implementa lógica de auth no backend.
- **Row-Level Security (RLS)** — entidades são user-scoped por padrão (cada usuário
  vê seus próprios registros).
- **Roles** — usuários são `admin` ou `user`; apenas admins gerenciam outros usuários.
- **Funções de backend** autenticam via `base44.auth.me()` e validam `user.role`
  quando operações administrativas são necessárias.
- **Segredos** — chaves de API nunca são expostas no frontend; ficam em variáveis
  de ambiente do Base44 e são lidas com `Deno.env.get()`.
- **Arquivos privados** — `UploadPrivateFile` + `CreateFileSignedUrl` para acesso
  temporário e controlado.

---

## Recomendações de Compliance

Este aplicativo lida com **dados de saúde (dados pessoais sensíveis)**. Recomenda-se:

1. **LGPD (Lei 13.709/2018)** — dados de pacientes são dados sensíveis (art. 11).
   Garantir base legal (consentimento ou execução de contrato de saúde).
2. **CFM** — seguir resoluções do Conselho Federal de Medicina para prontuários
   eletrônicos e prescrição/solicitação digital.
3. **Minimização de dados** — coletar apenas o necessário (`nome`, `idade`, `ID`).
4. **Retenção** — definir política de retenção e exclusão dos registros de pacientes.
5. **Auditabilidade** — considerar logs de quem gerou/solicitou cada documento.
6. **Criptografia em trânsito** — garantida pelo HTTPS do Base44.
7. **Controle de acesso** — revisar periodicamente a lista de usuários admin.
8. **Backup** — verificar a política de backup do Base44 para os dados de pacientes.
9. **Termo de uso e política de privacidade** — publicar antes de uso em produção.
10. **Assinatura digital** — para documentos com validade jurídica, avaliar
    integração com certificação digital (ICP-Brasil) no futuro.

> ⚠️ Este software **não substitui** a assinatura manual quando exigida por norma
> do CFM ou do estabelecimento de saúde.

---

## Execução Local

### Pré-requisitos
- Node.js 18+
- npm ou yarn

### Passos

```bash
# 1. Instalar dependências
npm install

# 2. Rodar em modo desenvolvimento
npm run dev

# 3. Build de produção
npm run build

# 4. Preview do build
npm run preview
```

### Variáveis de ambiente

As credenciais do Base44 (APP_ID, etc.) já estão configuradas em
`src/lib/app-params.js`. Demais segredos (chaves de API externas, quando houver)
devem ser definidos no painel do Base44 em **Settings → Environment Variables**.

---

## Funcionalidades Faltantes / Roadmap

### Curto prazo
- [ ] Busca/filtro de exames por nome (autocompletar)
- [ ] Editar exames já selecionados diretamente no resultado
- [ ] Histórico de solicitações geradas por paciente
- [ ] Exportação para Word (.docx) além de PDF
- [ ] Preview do PDF antes de salvar

### Médio prazo
- [ ] Sugestão de exames via IA a partir do quadro clínico (InvokeLLM)
- [ ] Integração com WhatsApp/Telegram para envio direto ao paciente
- [ ] Assinatura digital do documento (ICP-Brasil)
- [ ] Logo do consultório customizável no cabeçalho do PDF
- [ ] Múltiplos médicos/usuários com各自的 dados profissionais

### Longo prazo
- [ ] Integração com sistemas de laboratório (HL7/FHIR)
- [ ] App mobile (iOS/Android) via publicação do Base44
- [ ] Dashboard analítico de exames mais solicitados
- [ ] Multi-idioma (pt-BR / en-US)
- [ ] Modo offline com sincronização posterior

---

## Estrutura de Arquivos

```
src/
├── pages/
│   ├── Home.jsx                  # Landing page
│   └── SolicitacaoExames.jsx     # Página principal do gerador
├── components/
│   ├── exams/
│   │   ├── ExamSection.jsx
│   │   ├── ExamesMetabolicosPanel.jsx
│   │   ├── ExamesRenalHepaticaPanel.jsx
│   │   ├── ExamesGeralHormonalPanel.jsx
│   │   ├── ExamesUrinaFezesPanel.jsx
│   │   ├── ExamesPreOperatoriosPanel.jsx
│   │   ├── PacienteSelector.jsx
│   │   ├── ModelosSelector.jsx
│   │   └── PdfGenerator.jsx
│   └── ui/                       # Componentes shadcn/ui
├── lib/                          # Auth, utils, query-client
├── api/                          # base44Client, entities, integrations
└── App.jsx                       # Router principal

base44/
├── entities/                     # Schemas (Paciente, ModeloSolicitacao)
├── functions/                    # Backend functions (Deno)
└── agents/                       # Configuração de agentes IA
```

---

## Licença

Uso interno do consultório do Dr. Claudio M Orenstein. Todos os direitos reservados.
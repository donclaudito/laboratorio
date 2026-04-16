from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.colors import HexColor

# === PALETA ===
VERMELHO       = HexColor("#C0392B")
VERMELHO_CLARO = HexColor("#E74C3C")
AZUL_ESCURO    = HexColor("#1A2744")
AZUL_MEDIO     = HexColor("#2C3E7A")
CINZA_ESCURO   = HexColor("#2C3E50")
CINZA_MEDIO    = HexColor("#7F8C8D")
CINZA_CLARO    = HexColor("#ECF0F1")
BRANCO         = colors.white
VERDE          = HexColor("#27AE60")
LARANJA        = HexColor("#E67E22")
ROXO           = HexColor("#6A0DAD")
ESUS_VERDE     = HexColor("#1A6B3C")
ESUS_VERDE_CLR = HexColor("#27AE60")
ESUS_AMARELO   = HexColor("#F39C12")

PAGE_W, PAGE_H = A4
MARGIN         = 2 * cm
CONTENT_W      = PAGE_W - 2 * MARGIN


# =====================================================================
# BACKGROUNDS
# =====================================================================
class Background:
    def __init__(self, tipo="normal"):
        self.tipo = tipo

    def __call__(self, c, doc):
        c.saveState()
        w, h = PAGE_W, PAGE_H

        if self.tipo == "capa":
            # Fundo split: esquerda SAMU Amigo, direita e-SUS
            c.setFillColor(AZUL_ESCURO)
            c.rect(0, 0, w / 2, h, fill=1, stroke=0)
            c.setFillColor(ESUS_VERDE)
            c.rect(w / 2, 0, w / 2, h, fill=1, stroke=0)
            # Divisória
            c.setStrokeColor(BRANCO)
            c.setLineWidth(2)
            c.line(w / 2, 0, w / 2, h)
            # Faixa inferior
            c.setFillColor(VERMELHO)
            c.rect(0, 0, w, 1.0 * cm, fill=1, stroke=0)
            # Marcas d'água
            c.setFillColor(HexColor("#FFFFFF06"))
            c.setFont("Helvetica-Bold", 80)
            c.drawCentredString(w / 4, h / 2 - 20, "SAMU")
            c.drawCentredString(3 * w / 4, h / 2 - 20, "e-SUS")

        elif self.tipo == "secao":
            c.setFillColor(AZUL_MEDIO)
            c.rect(0, 0, w, h, fill=1, stroke=0)
            c.setFillColor(VERMELHO)
            c.rect(0, 0, 1.0 * cm, h, fill=1, stroke=0)
            c.setFillColor(HexColor("#FFFFFF06"))
            c.setFont("Helvetica-Bold", 80)
            c.drawCentredString(w / 2, h / 2 - 20, "vs")

        elif self.tipo == "integracao":
            c.setFillColor(HexColor("#0D1B2A"))
            c.rect(0, 0, w, h, fill=1, stroke=0)
            c.setFillColor(VERDE)
            c.rect(0, 0, 1.0 * cm, h, fill=1, stroke=0)
            c.setFillColor(HexColor("#FFFFFF04"))
            c.setFont("Helvetica-Bold", 60)
            c.drawCentredString(w / 2, h / 2 - 20, "INTEGRACAO")

        else:
            c.setFillColor(BRANCO)
            c.rect(0, 0, w, h, fill=1, stroke=0)
            # Header
            c.setFillColor(AZUL_ESCURO)
            c.rect(0, h - 1.8 * cm, w, 1.8 * cm, fill=1, stroke=0)
            c.setFillColor(VERMELHO)
            c.rect(0, h - 1.8 * cm, 0.5 * cm, 1.8 * cm, fill=1, stroke=0)
            c.setFillColor(ESUS_VERDE)
            c.rect(w - 0.5 * cm, h - 1.8 * cm, 0.5 * cm, 1.8 * cm, fill=1, stroke=0)
            c.setFillColor(BRANCO)
            c.setFont("Helvetica-Bold", 9)
            c.drawString(1.2 * cm, h - 1.2 * cm, "SAMU AMIGO  vs  e-SUS SAMU (DATASUS)")
            c.setFont("Helvetica", 9)
            c.drawRightString(w - 1.2 * cm, h - 1.2 * cm, "Ministerio da Saude · Santo Andre · 2025")
            # Footer
            c.setFillColor(AZUL_ESCURO)
            c.rect(0, 0, w, 1.0 * cm, fill=1, stroke=0)
            c.setFillColor(HexColor("#AAAAAA"))
            c.setFont("Helvetica", 8)
            c.drawCentredString(w / 2, 0.35 * cm, f"Pagina {doc.page}")

        c.restoreState()


# =====================================================================
# ESTILOS
# =====================================================================
def estilos():
    return {
        "capa_titulo":  ParagraphStyle("ct", fontName="Helvetica-Bold", fontSize=36,
                                       textColor=BRANCO, alignment=TA_CENTER, leading=44),
        "capa_vs":      ParagraphStyle("cv", fontName="Helvetica-Bold", fontSize=24,
                                       textColor=VERMELHO_CLARO, alignment=TA_CENTER, leading=30),
        "capa_sub":     ParagraphStyle("cs", fontName="Helvetica", fontSize=13,
                                       textColor=HexColor("#B0C4DE"), alignment=TA_CENTER, leading=19),
        "capa_label":   ParagraphStyle("cl", fontName="Helvetica-Bold", fontSize=10,
                                       textColor=HexColor("#AAAAAA"), alignment=TA_CENTER, leading=15),
        "secao_titulo": ParagraphStyle("st", fontName="Helvetica-Bold", fontSize=28,
                                       textColor=BRANCO, alignment=TA_CENTER, leading=36),
        "secao_sub":    ParagraphStyle("ss", fontName="Helvetica", fontSize=13,
                                       textColor=HexColor("#B0C4DE"), alignment=TA_CENTER, leading=18),
        "slide_titulo": ParagraphStyle("slt", fontName="Helvetica-Bold", fontSize=17,
                                       textColor=BRANCO, alignment=TA_LEFT, leading=22),
        "h2":           ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12,
                                       textColor=AZUL_ESCURO, leading=17, spaceAfter=5, spaceBefore=8),
        "body":         ParagraphStyle("body", fontName="Helvetica", fontSize=10,
                                       textColor=CINZA_ESCURO, leading=15, spaceAfter=4),
        "nota":         ParagraphStyle("nota", fontName="Helvetica-Oblique", fontSize=9,
                                       textColor=CINZA_MEDIO, leading=13, alignment=TA_CENTER),
        "rodape_capa":  ParagraphStyle("rc", fontName="Helvetica", fontSize=10,
                                       textColor=HexColor("#AAAAAA"), alignment=TA_CENTER, leading=14),
        "integ_titulo": ParagraphStyle("it", fontName="Helvetica-Bold", fontSize=17,
                                       textColor=BRANCO, alignment=TA_LEFT, leading=22),
    }


def sp(h):  return Spacer(1, h * cm)
def hr(cor=VERMELHO, t=2): return HRFlowable(width="100%", thickness=t, color=cor,
                                              spaceAfter=8, spaceBefore=4)
def hdr(txt, s, key="slide_titulo"): return Paragraph(txt, s[key])


# =====================================================================
# PÁGINAS
# =====================================================================

def pg_capa(s, story):
    story.append(sp(3.6))
    story.append(Paragraph("SAMU AMIGO", s["capa_titulo"]))
    story.append(sp(0.25))
    story.append(Paragraph("vs", s["capa_vs"]))
    story.append(sp(0.25))
    story.append(Paragraph("e-SUS SAMU", ParagraphStyle("esus_t", fontName="Helvetica-Bold",
                                                         fontSize=36, textColor=ESUS_VERDE_CLR,
                                                         alignment=TA_CENTER, leading=44)))
    story.append(sp(0.4))
    story.append(HRFlowable(width="55%", thickness=3, color=VERMELHO_CLARO,
                             spaceAfter=10, spaceBefore=4, hAlign="CENTER"))
    story.append(Paragraph("Analise Comparativa + Arquitetura de Integracao", s["capa_sub"]))
    story.append(sp(0.35))
    story.append(Paragraph(
        "Inovacao clinica com IA  x  Conformidade regulatoria obrigatoria",
        s["capa_label"]
    ))
    story.append(sp(0.5))
    story.append(Paragraph("DATASUS · Ministerio da Saude · Santo Andre · 2025", s["rodape_capa"]))
    story.append(PageBreak())


def pg_secao(titulo, sub, s, story, tipo="secao"):
    story.append(sp(5))
    story.append(Paragraph(titulo, s["secao_titulo"]))
    story.append(sp(0.3))
    story.append(HRFlowable(width="50%", thickness=3, color=VERMELHO_CLARO,
                             spaceAfter=10, spaceBefore=4, hAlign="CENTER"))
    story.append(Paragraph(sub, s["secao_sub"]))
    story.append(PageBreak())


def pg_visao_geral(s, story):
    story.append(hdr("Visao Geral Comparativa", s))
    story.append(hr())
    story.append(sp(0.3))

    dados = [
        ["Dimensao",         "SAMU Amigo",                        "e-SUS SAMU (DATASUS)"],
        ["Origem",           "Projeto privado / Santo Andre",     "Governo Federal — Ministerio da Saude"],
        ["Versao",           "Em desenvolvimento ativo",          "1.4.6 (estavel, ciclo lento)"],
        ["Custo",            "Gratuito",                          "Gratuito"],
        ["Tecnologia",       "React 18 + IA + Base44 (cloud)",    "Stack legada (on-premises)"],
        ["Inteligencia IA",  "Sim — ISA (triagem clinica ativa)", "Zero"],
        ["Instalacao",       "Cloud / SaaS",                      "On-premises (codigo-fonte + SQL)"],
        ["Suporte",          "Equipe interna",                    "DATASUS por e-mail"],
        ["Conformidade MS",  "Parcial (em construcao)",           "Total — e o proprio MS"],
        ["Atualizacoes",     "Continuas (sprint)",                "Lentas (ciclo governamental)"],
        ["Interface",        "Moderna / responsiva",              "Legada"],
        ["Relatorio MS",     "Parcial",                           "Sim (nativo)"],
    ]

    col_w = [CONTENT_W * p for p in [0.30, 0.35, 0.35]]

    def th(txt, bg):
        return Paragraph(txt, ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=10,
                                              textColor=BRANCO, alignment=TA_CENTER, leading=13))

    header_row = [th(dados[0][0], AZUL_ESCURO),
                  th(dados[0][1], VERMELHO),
                  th(dados[0][2], ESUS_VERDE)]

    rows = [header_row]
    for row in dados[1:]:
        rows.append([
            Paragraph(row[0], ParagraphStyle("d", fontName="Helvetica-Bold", fontSize=9,
                                              textColor=AZUL_ESCURO, leading=13)),
            Paragraph(row[1], ParagraphStyle("s", fontName="Helvetica-Bold", fontSize=9,
                                              textColor=AZUL_MEDIO, alignment=TA_CENTER, leading=13)),
            Paragraph(row[2], ParagraphStyle("e", fontName="Helvetica", fontSize=9,
                                              textColor=CINZA_ESCURO, alignment=TA_CENTER, leading=13)),
        ])

    t = Table(rows, colWidths=col_w)
    t.setStyle(TableStyle([
        ("BACKGROUND",     (0, 0), (-1, 0), AZUL_ESCURO),
        ("BACKGROUND",     (1, 0), (1, 0), VERMELHO),
        ("BACKGROUND",     (2, 0), (2, 0), ESUS_VERDE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
        ("GRID",           (0, 0), (-1, -1), 0.4, HexColor("#CCCCCC")),
        ("VALIGN",         (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",     (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING",  (0, 0), (-1, -1), 8),
        ("LEFTPADDING",    (0, 0), (-1, -1), 8),
    ]))
    story.append(t)
    story.append(PageBreak())


def pg_funcionalidades(s, story):
    story.append(hdr("Comparativo de Funcionalidades", s))
    story.append(hr())
    story.append(sp(0.3))

    SIM   = "Sim"
    NAO   = "Nao"
    PARC  = "Parcial"
    UNICO = "Exclusivo"
    BASICO= "Basico"

    dados = [
        ["Funcionalidade",                                    "SAMU Amigo",  "e-SUS SAMU"],
        ["Triagem com IA clinica (ISA)",                     UNICO,         NAO],
        ["Regulacao medica assistida",                       SIM,           BASICO],
        ["Perfis: TARM / Regulador / Frota",                 SIM,           SIM],
        ["Despacho de viaturas",                             SIM,           SIM],
        ["Registro de procedimentos medicos",                SIM,           SIM],
        ["Historico de atendimentos",                        SIM,           SIM],
        ["Rastreio GPS de viaturas",                         SIM,           NAO],
        ["Pre-alerta hospitalar (FAPH)",                     SIM,           NAO],
        ["Dashboards e Analytics",                           SIM,           BASICO],
        ["Relatorios formato Ministerio da Saude",           PARC,          SIM],
        ["Ficha de regulacao oficial",                       PARC,          SIM],
        ["Protocolos MS integrados",                         PARC,          SIM],
        ["Interface moderna / responsiva",                   SIM,           NAO],
        ["Notificacoes sonoras de alerta",                   SIM,           NAO],
        ["Multi-perfil com interfaces distintas",            SIM,           BASICO],
        ["Instalacao Cloud / SaaS",                          SIM,           NAO],
        ["Codigo aberto / customizavel",                     SIM,           SIM],
        ["Conformidade LGPD documentada",                    PARC,          PARC],
        ["Suporte 24/7",                                     NAO,           NAO],
    ]

    def estilo_cel(v):
        if v == UNICO:
            return ParagraphStyle("u", fontName="Helvetica-Bold", fontSize=9,
                                  textColor=ROXO, alignment=TA_CENTER, leading=12)
        elif v == SIM:
            return ParagraphStyle("s", fontName="Helvetica-Bold", fontSize=9,
                                  textColor=VERDE, alignment=TA_CENTER, leading=12)
        elif v == NAO:
            return ParagraphStyle("n", fontName="Helvetica", fontSize=9,
                                  textColor=VERMELHO, alignment=TA_CENTER, leading=12)
        elif v == BASICO:
            return ParagraphStyle("b", fontName="Helvetica-Oblique", fontSize=9,
                                  textColor=CINZA_MEDIO, alignment=TA_CENTER, leading=12)
        else:
            return ParagraphStyle("p", fontName="Helvetica-Oblique", fontSize=9,
                                  textColor=LARANJA, alignment=TA_CENTER, leading=12)

    col_w = [CONTENT_W * p for p in [0.56, 0.22, 0.22]]

    rows = [[
        Paragraph(dados[0][0], ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=10,
                                               textColor=BRANCO, leading=13)),
        Paragraph(dados[0][1], ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=10,
                                               textColor=BRANCO, alignment=TA_CENTER, leading=13)),
        Paragraph(dados[0][2], ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=10,
                                               textColor=BRANCO, alignment=TA_CENTER, leading=13)),
    ]]
    for row in dados[1:]:
        rows.append([
            Paragraph(row[0], ParagraphStyle("f", fontName="Helvetica", fontSize=9,
                                              textColor=CINZA_ESCURO, leading=13)),
            Paragraph(row[1], estilo_cel(row[1])),
            Paragraph(row[2], estilo_cel(row[2])),
        ])

    t = Table(rows, colWidths=col_w)
    t.setStyle(TableStyle([
        ("BACKGROUND",     (0, 0), (-1, 0), AZUL_ESCURO),
        ("BACKGROUND",     (1, 0), (1, 0), VERMELHO),
        ("BACKGROUND",     (2, 0), (2, 0), ESUS_VERDE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
        ("GRID",           (0, 0), (-1, -1), 0.4, HexColor("#CCCCCC")),
        ("VALIGN",         (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",     (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING",  (0, 0), (-1, -1), 6),
        ("LEFTPADDING",    (0, 0), (-1, -1), 7),
    ]))
    story.append(t)
    story.append(sp(0.3))

    leg = Table([[
        Paragraph("Exclusivo SAMU", ParagraphStyle("l", fontName="Helvetica-Bold", fontSize=8,
                                                    textColor=ROXO, leading=11, alignment=TA_CENTER)),
        Paragraph("Sim", ParagraphStyle("l", fontName="Helvetica-Bold", fontSize=8,
                                         textColor=VERDE, leading=11, alignment=TA_CENTER)),
        Paragraph("Parcial", ParagraphStyle("l", fontName="Helvetica-Oblique", fontSize=8,
                                             textColor=LARANJA, leading=11, alignment=TA_CENTER)),
        Paragraph("Basico", ParagraphStyle("l", fontName="Helvetica-Oblique", fontSize=8,
                                            textColor=CINZA_MEDIO, leading=11, alignment=TA_CENTER)),
        Paragraph("Nao", ParagraphStyle("l", fontName="Helvetica", fontSize=8,
                                         textColor=VERMELHO, leading=11, alignment=TA_CENTER)),
    ]], colWidths=[CONTENT_W / 5] * 5)
    leg.setStyle(TableStyle([
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("BOX",           (0, 0), (-1, -1), 0.4, HexColor("#CCCCCC")),
        ("BACKGROUND",    (0, 0), (-1, -1), CINZA_CLARO),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(leg)
    story.append(PageBreak())


def pg_diferenca_central(s, story):
    story.append(hdr("A Diferenca Central", s))
    story.append(hr())
    story.append(sp(0.4))

    itens = [
        ("O que faz",           "Auxilia o que esta acontecendo",   "Registra o que aconteceu"),
        ("Papel da tecnologia",  "IA ativa na decisao",              "Formulario digital"),
        ("Velocidade evolucao",  "Sprint continuo",                  "Ciclo governamental (anos)"),
        ("Experiencia usuario",  "Interface moderna e responsiva",   "Interface legada"),
        ("Foco principal",       "Decisao clinica correta",          "Conformidade e auditoria"),
        ("Dado em tempo real",   "Sim — suporte a decisao",          "Registro apos o fato"),
        ("Inovacao",             "Alta — IA, GPS, FAPH",             "Baixa — sistema 2010"),
    ]

    col_w = [CONTENT_W * p for p in [0.28, 0.36, 0.36]]

    rows = [[
        Paragraph("Dimensao", ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=10,
                                              textColor=BRANCO, alignment=TA_CENTER, leading=13)),
        Paragraph("SAMU Amigo", ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=10,
                                                textColor=BRANCO, alignment=TA_CENTER, leading=13)),
        Paragraph("e-SUS SAMU", ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=10,
                                                textColor=BRANCO, alignment=TA_CENTER, leading=13)),
    ]]
    for row in itens:
        rows.append([
            Paragraph(row[0], ParagraphStyle("d", fontName="Helvetica-Bold", fontSize=9,
                                              textColor=AZUL_ESCURO, leading=13)),
            Paragraph(row[1], ParagraphStyle("s", fontName="Helvetica-Bold", fontSize=10,
                                              textColor=AZUL_MEDIO, alignment=TA_CENTER, leading=14)),
            Paragraph(row[2], ParagraphStyle("e", fontName="Helvetica", fontSize=9,
                                              textColor=CINZA_MEDIO, alignment=TA_CENTER, leading=13)),
        ])

    t = Table(rows, colWidths=col_w)
    t.setStyle(TableStyle([
        ("BACKGROUND",     (0, 0), (-1, 0), AZUL_ESCURO),
        ("BACKGROUND",     (1, 0), (1, 0), VERMELHO),
        ("BACKGROUND",     (2, 0), (2, 0), ESUS_VERDE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
        ("GRID",           (0, 0), (-1, -1), 0.5, HexColor("#CCCCCC")),
        ("VALIGN",         (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",     (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING",  (0, 0), (-1, -1), 10),
        ("LEFTPADDING",    (0, 0), (-1, -1), 10),
        ("LINEAFTER",      (1, 0), (1, -1), 1.5, BRANCO),
    ]))
    story.append(t)
    story.append(sp(0.5))

    box = Table([[Paragraph(
        '"O e-SUS SAMU registra o passado.<br/>'
        'O SAMU Amigo muda o futuro do paciente."',
        ParagraphStyle("q", fontName="Helvetica-BoldOblique", fontSize=14,
                       textColor=BRANCO, alignment=TA_CENTER, leading=20)
    )]], colWidths=[CONTENT_W])
    box.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), AZUL_ESCURO),
        ("TOPPADDING",    (0, 0), (-1, -1), 18),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 18),
        ("LEFTPADDING",   (0, 0), (-1, -1), 20),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 20),
    ]))
    story.append(box)
    story.append(PageBreak())


def pg_fator_politico(s, story):
    story.append(hdr("O Fator Politico: Por que nao e uma escolha", s))
    story.append(hr())
    story.append(sp(0.3))

    alerta = Table([[Paragraph(
        "ATENCAO: O e-SUS SAMU e mandatado pelo Ministerio da Saude.",
        ParagraphStyle("al", fontName="Helvetica-Bold", fontSize=12,
                       textColor=BRANCO, alignment=TA_CENTER, leading=16)
    )]], colWidths=[CONTENT_W])
    alerta.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), ESUS_AMARELO),
        ("TOPPADDING",    (0, 0), (-1, -1), 14),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
        ("LEFTPADDING",   (0, 0), (-1, -1), 16),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 16),
    ]))
    story.append(alerta)
    story.append(sp(0.4))

    obrigacoes = [
        ("Prestacao de contas federal",
         "Os dados de producao do SAMU precisam estar no formato do MS para repasse financeiro. "
         "O e-SUS SAMU e o canal oficial para isso."),
        ("Auditoria e fiscalizacao",
         "Auditorias do Ministerio da Saude verificam se os registros estao no e-SUS SAMU. "
         "A ausencia de dados no sistema pode comprometer o financiamento."),
        ("Ficha de regulacao oficial",
         "O formulario oficial de regulacao medica e definido pelo MS. "
         "O municipio precisa preenche-lo conforme as normativas vigentes."),
        ("Protocolo padronizado",
         "Os protocolos do Ministerio da Saude estao embarcados no e-SUS SAMU. "
         "Municipios devem seguir esses protocolos para compliance regulatorio."),
    ]

    col_w = [CONTENT_W * p for p in [0.05, 0.95]]

    for i, (titulo, desc) in enumerate(obrigacoes):
        row = Table([[
            Paragraph("!", ParagraphStyle("num", fontName="Helvetica-Bold", fontSize=14,
                                          textColor=ESUS_AMARELO, alignment=TA_CENTER, leading=18)),
            [Paragraph(titulo, ParagraphStyle("ot", fontName="Helvetica-Bold", fontSize=10,
                                               textColor=AZUL_ESCURO, leading=14)),
             Paragraph(desc,   ParagraphStyle("od", fontName="Helvetica", fontSize=9,
                                               textColor=CINZA_ESCURO, leading=13))],
        ]], colWidths=col_w)
        row.setStyle(TableStyle([
            ("VALIGN",        (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING",    (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ("LEFTPADDING",   (0, 0), (-1, -1), 6),
            ("BACKGROUND",    (0, 0), (-1, -1), CINZA_CLARO if i % 2 == 0 else BRANCO),
            ("LINEBELOW",     (0, 0), (-1, 0), 0.5, HexColor("#DDDDDD")),
        ]))
        story.append(row)
        story.append(sp(0.15))

    story.append(sp(0.3))
    conclusao = Table([[Paragraph(
        "O SAMU Amigo NAO pode substituir o e-SUS SAMU.<br/>"
        "Ele precisa ser COMPLEMENTAR — ambos rodando em paralelo.",
        ParagraphStyle("cn", fontName="Helvetica-Bold", fontSize=12,
                       textColor=BRANCO, alignment=TA_CENTER, leading=18)
    )]], colWidths=[CONTENT_W])
    conclusao.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), VERMELHO),
        ("TOPPADDING",    (0, 0), (-1, -1), 16),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 16),
        ("LEFTPADDING",   (0, 0), (-1, -1), 18),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 18),
    ]))
    story.append(conclusao)
    story.append(PageBreak())


def pg_arquitetura(s, story):
    """Slide de arquitetura de integracao — fundo escuro."""
    story.append(hdr("Arquitetura de Integracao Proposta", s, "integ_titulo"))
    story.append(HRFlowable(width="100%", thickness=2, color=VERDE,
                             spaceAfter=8, spaceBefore=4))
    story.append(sp(0.3))

    story.append(Paragraph(
        "Como os dois sistemas operam em paralelo em Santo Andre:",
        ParagraphStyle("sub", fontName="Helvetica", fontSize=10,
                       textColor=HexColor("#B0C4DE"), leading=14)
    ))
    story.append(sp(0.4))

    # Diagrama de fluxo como tabela visual
    camadas = [
        # [label camada, componente esquerdo, seta, componente direito]
        ("ENTRADA",
         "Chamada 192\nCidadao liga", "->",
         "TARM recebe\ne registra"),
        ("TRIAGEM",
         "ISA (SAMU Amigo)\nanalisa clinicamente", "<->",
         "e-SUS SAMU\nregistra ocorrencia"),
        ("REGULACAO",
         "Medico Regulador\n+ IA assistindo", "->",
         "Ficha oficial\ne-SUS SAMU"),
        ("DESPACHO",
         "SAMU Amigo\ndespacha viatura + GPS", "->",
         "e-SUS SAMU\nregistra despacho"),
        ("APH",
         "FAPH (SAMU Amigo)\npre-alerta hospital", "->",
         "e-SUS SAMU\nregistra APH"),
        ("RELATORIO",
         "SAMU Amigo\nAnalytics + Dashboard", "->",
         "e-SUS SAMU\nRelatorio MS (repasse)"),
    ]

    col_w = [CONTENT_W * p for p in [0.18, 0.33, 0.08, 0.33, 0.08]]

    def camada_row(label, esq, seta, dir_):
        branco_txt = ParagraphStyle("bt", fontName="Helvetica-Bold", fontSize=9,
                                     textColor=BRANCO, alignment=TA_CENTER, leading=13)
        seta_style = ParagraphStyle("st", fontName="Helvetica-Bold", fontSize=14,
                                     textColor=VERDE, alignment=TA_CENTER, leading=18)
        lbl_style  = ParagraphStyle("ls", fontName="Helvetica-Bold", fontSize=9,
                                     textColor=ESUS_AMARELO, alignment=TA_CENTER, leading=13)
        return [
            Paragraph(label, lbl_style),
            Paragraph(esq.replace("\n", "<br/>"), branco_txt),
            Paragraph(seta, seta_style),
            Paragraph(dir_.replace("\n", "<br/>"), branco_txt),
            Paragraph("", branco_txt),
        ]

    rows = [camada_row(l, e, s2, d) for l, e, s2, d in camadas]

    bg_esq  = HexColor("#1E3A5F")
    bg_dir  = HexColor("#1A4D2E")
    bg_lbl  = HexColor("#0D1B2A")
    bg_seta = HexColor("#0D1B2A")

    t = Table(rows, colWidths=col_w,
              rowHeights=[2.0 * cm] * len(rows))
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), bg_lbl),
        ("BACKGROUND", (1, 0), (1, -1), bg_esq),
        ("BACKGROUND", (2, 0), (2, -1), bg_seta),
        ("BACKGROUND", (3, 0), (3, -1), bg_dir),
        ("BACKGROUND", (4, 0), (4, -1), bg_lbl),
        ("GRID",       (0, 0), (-1, -1), 1, HexColor("#2A4A6A")),
        ("VALIGN",     (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN",      (0, 0), (-1, -1), "CENTER"),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(t)
    story.append(sp(0.4))

    legenda = Table([[
        Paragraph("SAMU Amigo (azul)", ParagraphStyle("lg", fontName="Helvetica-Bold",
                                                       fontSize=9, textColor=HexColor("#6BA3D6"),
                                                       leading=12, alignment=TA_CENTER)),
        Paragraph("e-SUS SAMU (verde)", ParagraphStyle("lg", fontName="Helvetica-Bold",
                                                        fontSize=9, textColor=ESUS_VERDE_CLR,
                                                        leading=12, alignment=TA_CENTER)),
        Paragraph("Camada / Fase (amarelo)", ParagraphStyle("lg", fontName="Helvetica-Bold",
                                                             fontSize=9, textColor=ESUS_AMARELO,
                                                             leading=12, alignment=TA_CENTER)),
    ]], colWidths=[CONTENT_W / 3] * 3)
    legenda.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), HexColor("#111827")),
        ("GRID",          (0, 0), (-1, -1), 0.5, HexColor("#2A4A6A")),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
    ]))
    story.append(legenda)
    story.append(PageBreak())


def pg_posicionamento(s, story):
    story.append(hdr("Posicionamento: O Melhor dos Dois Mundos", s))
    story.append(hr())
    story.append(sp(0.4))

    formula = [
        ["e-SUS SAMU", "+", "SAMU Amigo", "=", "Santo Andre ideal"],
        ["Conformidade\nRegistro oficial\nRepasse federal\nProtocolos MS",
         "",
         "IA Clinica (ISA)\nUX moderna\nGPS + FAPH\nAnalitics",
         "",
         "Conformidade\n+\nInovacao\n+\nVidas salvas"],
    ]

    col_w = [CONTENT_W * p for p in [0.28, 0.06, 0.28, 0.06, 0.32]]

    def cel(txt, bg, bold=True, size=11):
        fn = "Helvetica-Bold" if bold else "Helvetica"
        return Paragraph(txt.replace("\n", "<br/>"),
                         ParagraphStyle("fc", fontName=fn, fontSize=size,
                                        textColor=BRANCO, alignment=TA_CENTER, leading=16))

    rows_f = [
        [cel("e-SUS SAMU", ESUS_VERDE),
         cel("+", AZUL_ESCURO, size=20),
         cel("SAMU Amigo", VERMELHO),
         cel("=", AZUL_ESCURO, size=20),
         cel("Santo Andre Ideal", VERDE)],
        [cel("Conformidade\nRegistro oficial\nRepasse federal\nProtocolos MS",
             HexColor("#1A4D2E"), bold=False, size=9),
         cel("", AZUL_ESCURO),
         cel("IA Clinica (ISA)\nUX moderna\nGPS + FAPH\nAnalytics",
             HexColor("#5D1A1A"), bold=False, size=9),
         cel("", AZUL_ESCURO),
         cel("Conformidade\n+\nInovacao\n+\nVidas salvas",
             HexColor("#145214"), bold=True, size=10)],
    ]

    ft = Table(rows_f, colWidths=col_w,
               rowHeights=[1.4 * cm, 3.2 * cm])
    ft.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 1), ESUS_VERDE),
        ("BACKGROUND", (1, 0), (1, 1), AZUL_ESCURO),
        ("BACKGROUND", (2, 0), (2, 1), VERMELHO),
        ("BACKGROUND", (3, 0), (3, 1), AZUL_ESCURO),
        ("BACKGROUND", (4, 0), (4, 1), VERDE),
        ("BACKGROUND", (0, 1), (0, 1), HexColor("#1A4D2E")),
        ("BACKGROUND", (2, 1), (2, 1), HexColor("#5D1A1A")),
        ("BACKGROUND", (4, 1), (4, 1), HexColor("#145214")),
        ("GRID",       (0, 0), (-1, -1), 1, BRANCO),
        ("VALIGN",     (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN",      (0, 0), (-1, -1), "CENTER"),
    ]))
    story.append(ft)
    story.append(sp(0.5))

    narrativa = Table([[Paragraph(
        '"Usamos o e-SUS SAMU para conformidade com o Ministerio da Saude.<br/>'
        'Usamos o SAMU Amigo para salvar vidas mais rapido."',
        ParagraphStyle("nv", fontName="Helvetica-BoldOblique", fontSize=13,
                       textColor=BRANCO, alignment=TA_CENTER, leading=19)
    )]], colWidths=[CONTENT_W])
    narrativa.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), AZUL_ESCURO),
        ("TOPPADDING",    (0, 0), (-1, -1), 18),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 18),
        ("LEFTPADDING",   (0, 0), (-1, -1), 20),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 20),
    ]))
    story.append(narrativa)
    story.append(PageBreak())


def pg_conclusao(s, story):
    story.append(hdr("Conclusao", s))
    story.append(hr())
    story.append(sp(0.4))

    comp = [
        ["Criterio",         "e-SUS SAMU",                      "SAMU Amigo"],
        ["Papel",            "Conformidade regulatoria",         "Inovacao clinica"],
        ["Obrigatorio?",     "Sim — mandato federal",            "Complementar"],
        ["IA",               "Nenhuma",                          "ISA — exclusivo"],
        ["Interface",        "Legada (2010)",                    "Moderna (2024+)"],
        ["GPS/Rastreio",     "Nao",                              "Sim"],
        ["FAPH",             "Nao",                              "Sim"],
        ["Relatorio MS",     "Sim — nativo",                     "Parcial (roadmap)"],
        ["Inovacao",         "Baixa",                            "Alta"],
        ["Papel em SA",      "Base regulatoria obrigatoria",     "Diferencial competitivo"],
    ]

    col_w = [CONTENT_W * p for p in [0.30, 0.35, 0.35]]

    rows = []
    for i, row in enumerate(comp):
        if i == 0:
            rows.append([
                Paragraph(c, ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=10,
                                             textColor=BRANCO, alignment=TA_CENTER, leading=13))
                for c in row
            ])
        else:
            rows.append([
                Paragraph(row[0], ParagraphStyle("d", fontName="Helvetica-Bold", fontSize=9,
                                                  textColor=AZUL_ESCURO, leading=13)),
                Paragraph(row[1], ParagraphStyle("e", fontName="Helvetica", fontSize=9,
                                                  textColor=CINZA_MEDIO, alignment=TA_CENTER, leading=13)),
                Paragraph(row[2], ParagraphStyle("s", fontName="Helvetica-Bold", fontSize=9,
                                                  textColor=AZUL_MEDIO, alignment=TA_CENTER, leading=13)),
            ])

    ct = Table(rows, colWidths=col_w)
    ct.setStyle(TableStyle([
        ("BACKGROUND",     (0, 0), (-1, 0), AZUL_ESCURO),
        ("BACKGROUND",     (1, 0), (1, 0), ESUS_VERDE),
        ("BACKGROUND",     (2, 0), (2, 0), VERMELHO),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
        ("GRID",           (0, 0), (-1, -1), 0.5, HexColor("#CCCCCC")),
        ("VALIGN",         (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",     (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING",  (0, 0), (-1, -1), 9),
        ("LEFTPADDING",    (0, 0), (-1, -1), 8),
        ("LINEAFTER",      (1, 0), (1, -1), 1.5, BRANCO),
    ]))
    story.append(ct)
    story.append(sp(0.5))

    box = Table([[Paragraph(
        "O e-SUS SAMU e o chao que todo municipio precisa ter.<br/>"
        "O SAMU Amigo e o teto que Santo Andre pode alcancar.<br/>"
        "Com os dois juntos: conformidade garantida e inovacao real.",
        ParagraphStyle("bf", fontName="Helvetica-Bold", fontSize=12,
                       textColor=BRANCO, alignment=TA_CENTER, leading=19)
    )]], colWidths=[CONTENT_W])
    box.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), AZUL_ESCURO),
        ("TOPPADDING",    (0, 0), (-1, -1), 18),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 18),
        ("LEFTPADDING",   (0, 0), (-1, -1), 22),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 22),
    ]))
    story.append(box)
    story.append(PageBreak())


# =====================================================================
# MONTAGEM
# =====================================================================
def gerar(output):
    s     = estilos()
    story = []

    pg_capa(s, story)
    pg_secao("Visao Geral", "Como os dois sistemas se posicionam", s, story)
    pg_visao_geral(s, story)
    pg_secao("Funcionalidades", "Comparativo item a item", s, story)
    pg_funcionalidades(s, story)
    pg_secao("Diferenca Central", "O que cada sistema realmente faz pelo paciente", s, story)
    pg_diferenca_central(s, story)
    pg_secao("Fator Politico", "Por que o e-SUS SAMU nao e uma escolha — e obrigacao", s, story)
    pg_fator_politico(s, story)
    pg_secao("Arquitetura", "Como integrar os dois sistemas em Santo Andre", s, story)
    pg_arquitetura(s, story)
    pg_secao("Posicionamento", "O melhor dos dois mundos", s, story)
    pg_posicionamento(s, story)
    pg_secao("Conclusao", "Sintese final — dois sistemas, um objetivo", s, story)
    pg_conclusao(s, story)

    doc = SimpleDocTemplate(
        output, pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN,  bottomMargin=MARGIN,
    )

    INTEG_PAGES = set()

    def on_page(c, doc):
        n = doc.page
        if n == 1:
            Background("capa")(c, doc)
        elif n % 2 == 0:
            Background("secao")(c, doc)
        # página de arquitetura (aprox slide 9-10)
        elif n in [11, 12]:
            Background("integracao")(c, doc)
        else:
            Background("normal")(c, doc)

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f"PDF gerado: {output}")


if __name__ == "__main__":
    gerar("samu_amigo_vs_esus_samu.pdf")

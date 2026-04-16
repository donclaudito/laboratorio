from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.colors import HexColor

# === PALETA ===
PRETO          = HexColor("#0A0F1A")
AZUL_ESCURO    = HexColor("#0D1B2A")
AZUL_MEDIO     = HexColor("#1A3A6B")
CINZA_ESCURO   = HexColor("#2C3E50")
CINZA_MEDIO    = HexColor("#7F8C8D")
CINZA_CLARO    = HexColor("#F4F6F8")
BRANCO         = colors.white
VERDE          = HexColor("#1E8449")
VERDE_CLARO    = HexColor("#27AE60")
VERMELHO       = HexColor("#C0392B")
VERMELHO_CLARO = HexColor("#E74C3C")
LARANJA        = HexColor("#E67E22")
AMARELO        = HexColor("#F1C40F")
DOURADO        = HexColor("#D4AC0D")
ROXO           = HexColor("#7D3C98")
CINZA_AZUL     = HexColor("#566573")

# Cores por empresa
SAMU_COR       = HexColor("#C0392B")
MEDSAVE_COR    = HexColor("#2C3E7A")
HEXAGON_COR    = HexColor("#0066CC")
ESUS_COR       = HexColor("#1A6B3C")
SAMU360_COR    = HexColor("#D35400")
SINESP_COR     = HexColor("#1A5276")
JOIN_COR       = HexColor("#6C3483")
SRSAMU_COR     = HexColor("#117A65")
MV_COR         = HexColor("#1F618D")
TASY_COR       = HexColor("#0D47A1")
MONUV_COR      = HexColor("#4A235A")
TOTVS_COR      = HexColor("#B7950B")

PAGE_W, PAGE_H = A4
MARGIN         = 2 * cm
CONTENT_W      = PAGE_W - 2 * MARGIN


# =====================================================================
# BACKGROUNDS
# =====================================================================
class BG:
    def __init__(self, tipo="normal"):
        self.tipo = tipo

    def __call__(self, c, doc):
        c.saveState()
        w, h = PAGE_W, PAGE_H

        if self.tipo == "capa":
            c.setFillColor(PRETO)
            c.rect(0, 0, w, h, fill=1, stroke=0)
            # Faixas horizontais sutis
            for i in range(5):
                c.setFillColor(HexColor("#1A2744"))
                c.rect(0, i * h / 5, w, h / 5, fill=1, stroke=0)
            # Barra superior vermelha
            c.setFillColor(SAMU_COR)
            c.rect(0, h - 0.7 * cm, w, 0.7 * cm, fill=1, stroke=0)
            # Barra inferior dourada
            c.setFillColor(DOURADO)
            c.rect(0, 0, w, 0.7 * cm, fill=1, stroke=0)
            # Barra lateral com cores dos concorrentes
            altura = h / 11
            cores_lat = [SAMU_COR, MEDSAVE_COR, ESUS_COR, SAMU360_COR, SINESP_COR,
                         JOIN_COR, SRSAMU_COR, MV_COR, TASY_COR, MONUV_COR, TOTVS_COR]
            for i, cor in enumerate(cores_lat):
                c.setFillColor(cor)
                c.rect(0, i * altura, 0.5 * cm, altura, fill=1, stroke=0)
            # Marca d'água
            c.setFillColor(HexColor("#FFFFFF04"))
            c.setFont("Helvetica-Bold", 120)
            c.drawCentredString(w / 2, h / 2 - 40, "MERCADO")

        elif self.tipo == "secao":
            c.setFillColor(AZUL_MEDIO)
            c.rect(0, 0, w, h, fill=1, stroke=0)
            c.setFillColor(SAMU_COR)
            c.rect(0, 0, 0.7 * cm, h, fill=1, stroke=0)
            c.setFillColor(HexColor("#FFFFFF04"))
            c.setFont("Helvetica-Bold", 70)
            c.drawCentredString(w / 2, h / 2 - 25, "COMPETIDORES")

        elif self.tipo == "mapa":
            c.setFillColor(HexColor("#080E18"))
            c.rect(0, 0, w, h, fill=1, stroke=0)
            c.setFillColor(DOURADO)
            c.rect(0, 0, 0.7 * cm, h, fill=1, stroke=0)
            c.setFillColor(HexColor("#D4AC0D08"))
            c.rect(0, 0, w, h * 0.3, fill=1, stroke=0)

        else:
            c.setFillColor(BRANCO)
            c.rect(0, 0, w, h, fill=1, stroke=0)
            c.setFillColor(AZUL_ESCURO)
            c.rect(0, h - 1.8 * cm, w, 1.8 * cm, fill=1, stroke=0)
            c.setFillColor(SAMU_COR)
            c.rect(0, h - 1.8 * cm, 0.45 * cm, 1.8 * cm, fill=1, stroke=0)
            c.setFillColor(BRANCO)
            c.setFont("Helvetica-Bold", 9)
            c.drawString(1.2 * cm, h - 1.2 * cm, "SAMU AMIGO  |  Mapa Competitivo Brasil")
            c.setFont("Helvetica", 9)
            c.drawRightString(w - 1.2 * cm, h - 1.2 * cm, "11 Concorrentes Identificados · 2025")
            c.setFillColor(AZUL_ESCURO)
            c.rect(0, 0, w, 1.0 * cm, fill=1, stroke=0)
            c.setFillColor(DOURADO)
            c.rect(0, 0, w, 0.15 * cm, fill=1, stroke=0)
            c.setFillColor(HexColor("#AAAAAA"))
            c.setFont("Helvetica", 8)
            c.drawCentredString(w / 2, 0.35 * cm, f"Pagina {doc.page}")

        c.restoreState()


# =====================================================================
# ESTILOS
# =====================================================================
def E():
    return {
        "capa_label":   ParagraphStyle("cl", fontName="Helvetica-Bold", fontSize=11,
                                        textColor=DOURADO, alignment=TA_CENTER, leading=16),
        "capa_titulo":  ParagraphStyle("ct", fontName="Helvetica-Bold", fontSize=40,
                                        textColor=BRANCO, alignment=TA_CENTER, leading=48),
        "capa_sub":     ParagraphStyle("cs", fontName="Helvetica", fontSize=14,
                                        textColor=HexColor("#B0C4DE"), alignment=TA_CENTER, leading=20),
        "capa_rodape":  ParagraphStyle("cr", fontName="Helvetica", fontSize=9,
                                        textColor=HexColor("#666666"), alignment=TA_CENTER, leading=14),
        "secao_titulo": ParagraphStyle("st", fontName="Helvetica-Bold", fontSize=28,
                                        textColor=BRANCO, alignment=TA_CENTER, leading=36),
        "secao_sub":    ParagraphStyle("ss", fontName="Helvetica", fontSize=13,
                                        textColor=HexColor("#B0C4DE"), alignment=TA_CENTER, leading=18),
        "slide_titulo": ParagraphStyle("slt", fontName="Helvetica-Bold", fontSize=17,
                                        textColor=BRANCO, alignment=TA_LEFT, leading=22),
        "mapa_titulo":  ParagraphStyle("mt2", fontName="Helvetica-Bold", fontSize=17,
                                        textColor=DOURADO, alignment=TA_LEFT, leading=22),
        "h2":           ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12,
                                        textColor=AZUL_ESCURO, leading=17, spaceAfter=5, spaceBefore=8),
        "body":         ParagraphStyle("body", fontName="Helvetica", fontSize=10,
                                        textColor=CINZA_ESCURO, leading=15, spaceAfter=4),
        "nota":         ParagraphStyle("nota", fontName="Helvetica-Oblique", fontSize=8,
                                        textColor=CINZA_MEDIO, leading=12, alignment=TA_CENTER),
        "fonte":        ParagraphStyle("fo", fontName="Helvetica-Oblique", fontSize=7,
                                        textColor=CINZA_MEDIO, leading=10),
    }


def sp(h):  return Spacer(1, h * cm)
def hr(cor=SAMU_COR, t=2):
    return HRFlowable(width="100%", thickness=t, color=cor, spaceAfter=8, spaceBefore=4)
def hdr(txt, s, key="slide_titulo"):
    return Paragraph(txt, s[key])


# =====================================================================
# PAGINAS
# =====================================================================

def pg_capa(s, story):
    story.append(sp(2.8))
    story.append(Paragraph("MAPA COMPETITIVO COMPLETO", s["capa_label"]))
    story.append(sp(0.3))
    story.append(Paragraph("SAMU AMIGO", s["capa_titulo"]))
    story.append(sp(0.2))
    story.append(Paragraph("Concorrentes no Brasil", ParagraphStyle(
        "cs2", fontName="Helvetica", fontSize=22,
        textColor=HexColor("#7FB3D3"), alignment=TA_CENTER, leading=28
    )))
    story.append(sp(0.4))
    story.append(HRFlowable(width="55%", thickness=3, color=DOURADO,
                             spaceAfter=12, spaceBefore=4, hAlign="CENTER"))
    story.append(sp(0.2))
    story.append(Paragraph(
        "6 Concorrentes Diretos  •  5 Adjacentes  •  Analise de Ameaca e Posicionamento",
        s["capa_sub"]
    ))
    story.append(sp(0.5))

    resumo = [
        ["6\nDiretos SAMU", "5\nAdjacentes", "1\nUnico com IA"],
    ]
    rt = Table([[
        Paragraph(v.replace("\n", "<br/>"), ParagraphStyle(
            "rv", fontName="Helvetica-Bold", fontSize=14,
            textColor=DOURADO, alignment=TA_CENTER, leading=19))
        for v in resumo[0]
    ]], colWidths=[CONTENT_W / 3] * 3)
    rt.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), HexColor("#0D2240")),
        ("GRID",          (0, 0), (-1, -1), 1, AZUL_MEDIO),
        ("TOPPADDING",    (0, 0), (-1, -1), 14),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(rt)
    story.append(sp(0.8))
    story.append(Paragraph(
        "Fontes: DATASUS, Governo do Ceara, Ministerio da Justica, Portal Transparencia SP, "
        "pesquisa de mercado 2025",
        s["capa_rodape"]
    ))
    story.append(PageBreak())


def pg_secao(titulo, sub, s, story, tipo="secao"):
    story.append(sp(5.2))
    story.append(Paragraph(titulo, s["secao_titulo"]))
    story.append(sp(0.3))
    story.append(HRFlowable(width="50%", thickness=3, color=DOURADO,
                             spaceAfter=10, spaceBefore=4, hAlign="CENTER"))
    story.append(Paragraph(sub, s["secao_sub"]))
    story.append(PageBreak())


def pg_visao_geral(s, story):
    story.append(hdr("Panorama: Todos os Concorrentes", s))
    story.append(hr())
    story.append(sp(0.3))

    concorrentes = [
        ["#",  "Nome",                  "Tipo",          "Alcance",       "IA?", "Ameaca"],
        ["1",  "MedSave SEMS SAMU",     "Privado",       "Nacional",      "Nao", "Alta"],
        ["2",  "e-SUS SAMU (DATASUS)",  "Gov. Federal",  "4.143 mun.",    "Nao", "Media*"],
        ["3",  "SAMU 360 (Etice/CE)",   "Gov. Estadual", "Ceara",         "Nao", "Media"],
        ["4",  "SINESP-CAD (SENASP)",   "Gov. Federal",  "22 estados",    "Nao", "Baixa"],
        ["5",  "Join Tecnologia",       "Privado",       "SP e outros",   "Nao", "Media"],
        ["6",  "SRSAMU (Sergipe)",      "Gov. Estadual", "Sergipe",       "Nao", "Baixa"],
        ["7",  "MV Saude Digital",      "Privado",       "Nacional",      "Sim", "Alta**"],
        ["8",  "Philips Tasy/Bionexo",  "Privado",       "Nacional",      "Sim", "Media**"],
        ["9",  "Monuv",                 "Privado",       "Nacional",      "Nao", "Baixa"],
        ["10", "TOTVS Saude",           "Privado",       "Nacional",      "Sim", "Alta**"],
        ["11", "HXGN OnCall (Hexagon)", "Multinacional", "Global/BR",     "Sim", "Media"],
    ]

    def ameaca_cor(a):
        if "Alta" in a:   return VERMELHO
        if "Media" in a:  return LARANJA
        return CINZA_MEDIO

    def tipo_cor(t):
        if "Federal" in t:  return ESUS_COR
        if "Estadual" in t: return SAMU360_COR
        if "Multi" in t:    return HEXAGON_COR
        return AZUL_MEDIO

    col_w = [CONTENT_W * p for p in [0.05, 0.26, 0.14, 0.14, 0.09, 0.12]]
    # Ajuste: remover coluna Alcance e adicionar Segmento
    col_w = [CONTENT_W * p for p in [0.05, 0.28, 0.14, 0.16, 0.08, 0.29]]

    rows = []
    for i, row in enumerate(concorrentes):
        if i == 0:
            rows.append([
                Paragraph(c, ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9,
                                             textColor=BRANCO, alignment=TA_CENTER, leading=12))
                for c in row
            ])
        else:
            am_cor = ameaca_cor(row[5])
            tp_cor = tipo_cor(row[2])
            rows.append([
                Paragraph(row[0], ParagraphStyle("n", fontName="Helvetica-Bold", fontSize=9,
                                                  textColor=DOURADO, alignment=TA_CENTER, leading=13)),
                Paragraph(row[1], ParagraphStyle("nm", fontName="Helvetica-Bold", fontSize=9,
                                                  textColor=AZUL_ESCURO, leading=13)),
                Paragraph(row[2], ParagraphStyle("tp", fontName="Helvetica", fontSize=8,
                                                  textColor=tp_cor, alignment=TA_CENTER, leading=12)),
                Paragraph(row[3], ParagraphStyle("al", fontName="Helvetica", fontSize=8,
                                                  textColor=CINZA_ESCURO, alignment=TA_CENTER, leading=12)),
                Paragraph(row[4], ParagraphStyle("ia", fontName="Helvetica-Bold", fontSize=8,
                                                  textColor=VERDE_CLARO if row[4] == "Sim" else CINZA_MEDIO,
                                                  alignment=TA_CENTER, leading=12)),
                Paragraph(row[5], ParagraphStyle("am", fontName="Helvetica-Bold", fontSize=9,
                                                  textColor=am_cor, alignment=TA_CENTER, leading=13)),
            ])

    t = Table(rows, colWidths=col_w)
    t.setStyle(TableStyle([
        ("BACKGROUND",     (0, 0), (-1, 0), AZUL_ESCURO),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
        ("GRID",           (0, 0), (-1, -1), 0.4, HexColor("#CCCCCC")),
        ("VALIGN",         (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",     (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING",  (0, 0), (-1, -1), 8),
        ("LEFTPADDING",    (0, 0), (-1, -1), 7),
        # Separador entre diretos e adjacentes
        ("LINEABOVE",      (0, 8), (-1, 8), 1.5, DOURADO),
    ]))
    story.append(t)
    story.append(sp(0.3))
    story.append(Paragraph(
        "* e-SUS e obrigatorio — nao substitui mas influencia adocao  |  "
        "** MV, Tasy e TOTVS: ameaca futura se entrarem no segmento SAMU  |  "
        "Linhas 1-6 = concorrentes diretos  |  Linhas 7-11 = adjacentes",
        s["nota"]
    ))
    story.append(PageBreak())


def ficha_concorrente(nome, cor, tipo, alcance, ia, ameaca, descricao, diferenciais,
                      fraquezas, fonte, s, story):
    """Card detalhado de cada concorrente."""
    # Header
    h_row = Table([[
        Paragraph(nome, ParagraphStyle("ch", fontName="Helvetica-Bold", fontSize=13,
                                        textColor=BRANCO, leading=17)),
        Paragraph(f"Ameaca: {ameaca}", ParagraphStyle("ca", fontName="Helvetica-Bold", fontSize=11,
                                                        textColor=AMARELO, alignment=TA_RIGHT,
                                                        leading=15)),
    ]], colWidths=[CONTENT_W * 0.65, CONTENT_W * 0.35])
    h_row.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), cor),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING",   (0, 0), (-1, -1), 12),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 12),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(h_row)

    # Sub-header com tipo, alcance, IA
    meta = Table([[
        Paragraph(f"Tipo: {tipo}", ParagraphStyle("mt", fontName="Helvetica-Bold", fontSize=8,
                                                   textColor=cor, leading=12)),
        Paragraph(f"Alcance: {alcance}", ParagraphStyle("mal", fontName="Helvetica", fontSize=8,
                                                          textColor=CINZA_ESCURO, leading=12,
                                                          alignment=TA_CENTER)),
        Paragraph(f"IA: {ia}", ParagraphStyle("mia", fontName="Helvetica-Bold", fontSize=8,
                                               textColor=VERDE_CLARO if ia == "Nao possui" else VERDE,
                                               leading=12, alignment=TA_RIGHT)),
    ]], colWidths=[CONTENT_W * 0.38, CONTENT_W * 0.37, CONTENT_W * 0.25])
    meta.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), HexColor("#F0F3F4")),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
        ("LINEBELOW",     (0, 0), (-1, 0), 0.5, HexColor("#DDDDDD")),
    ]))
    story.append(meta)

    # Descricao
    desc_t = Table([[
        Paragraph(descricao, ParagraphStyle("cd", fontName="Helvetica", fontSize=9,
                                             textColor=CINZA_ESCURO, leading=14)),
    ]], colWidths=[CONTENT_W])
    desc_t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), BRANCO),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
    ]))
    story.append(desc_t)

    # Diferenciais e fraquezas lado a lado
    def lista(itens, cor_bullet):
        rows_l = []
        for item in itens:
            rows_l.append([Paragraph(
                f"• {item}",
                ParagraphStyle("li", fontName="Helvetica", fontSize=8,
                               textColor=CINZA_ESCURO, leading=13, leftIndent=6)
            )])
        t = Table(rows_l, colWidths=[CONTENT_W * 0.5 - 0.2 * cm])
        t.setStyle(TableStyle([
            ("TOPPADDING",    (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ]))
        return t

    lados = Table([[
        [Paragraph("Pontos Fortes", ParagraphStyle("pf", fontName="Helvetica-Bold", fontSize=8,
                                                    textColor=VERDE, leading=12)),
         lista(diferenciais, VERDE)],
        [Paragraph("Fraquezas", ParagraphStyle("fr", fontName="Helvetica-Bold", fontSize=8,
                                                textColor=VERMELHO, leading=12)),
         lista(fraquezas, VERMELHO)],
    ]], colWidths=[CONTENT_W * 0.5, CONTENT_W * 0.5])
    lados.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), CINZA_CLARO),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("LINEAFTER",     (0, 0), (0, -1), 0.5, HexColor("#DDDDDD")),
    ]))
    story.append(lados)
    story.append(Paragraph(f"Fonte: {fonte}", s["fonte"]))
    story.append(sp(0.35))


def pg_diretos(s, story):
    story.append(hdr("Concorrentes Diretos — Regulacao SAMU", s))
    story.append(hr())
    story.append(sp(0.3))

    fichas = [
        {
            "nome": "1. MedSave SEMS SAMU",
            "cor":  MEDSAVE_COR,
            "tipo": "Empresa privada brasileira",
            "alcance": "Nacional — ~50-100 centrais ativas",
            "ia":   "Nao possui",
            "ameaca": "ALTA",
            "desc": "Unico produto comercial privado dedicado exclusivamente ao SAMU no Brasil. "
                    "Possui conformidade com o Ministerio da Saude, suporte dedicado e base de clientes "
                    "consolidada. E o concorrente mais direto e imediato do SAMU Amigo no mercado privado.",
            "difs": ["Conformidade total com protocolos MS", "Produto maduro com base de clientes",
                     "Suporte dedicado 24/7", "Relatorios no formato ministerial",
                     "Ficha de regulacao oficial"],
            "fraq": ["Zero inteligencia artificial", "Interface legada", "Sem GPS de viaturas",
                     "Sem pre-alerta hospitalar (FAPH)", "Custo de licenciamento recorrente"],
            "fonte": "medsave.com.br/medsave-sems-samu | Estimativa de mercado",
        },
        {
            "nome": "2. e-SUS SAMU (DATASUS / Ministerio da Saude)",
            "cor":  ESUS_COR,
            "tipo": "Sistema governamental federal",
            "alcance": "4.143 municipios — mandato federal",
            "ia":   "Nao possui",
            "ameaca": "MEDIA (e obrigatorio, nao substitui)",
            "desc": "Sistema oficial do governo federal, distribuido gratuitamente e mandatado para "
                    "conformidade e repasse. Nao e substituivel — o SAMU Amigo precisa ser complementar. "
                    "Versao atual: 1.4.6. Tecnologia legada, instalacao on-premises.",
            "difs": ["Mandato federal — adocao garantida", "Custo zero", "Conformidade total com MS",
                     "Ficha de regulacao oficial", "Relatorio ministerial nativo"],
            "fraq": ["Zero inovacao tecnologica", "Interface de 2010", "Sem IA, GPS ou FAPH",
                     "Atualizacoes em ciclo de anos", "Suporte apenas por e-mail"],
            "fonte": "datasus.saude.gov.br/e-sus-samu",
        },
        {
            "nome": "3. SAMU 360 (Etice — Governo do Ceara)",
            "cor":  SAMU360_COR,
            "tipo": "Empresa estadual de TI (Etice/CE)",
            "alcance": "Ceara — 166 veiculos, 12 municipios",
            "ia":   "Nao possui (GPS e tracking)",
            "ameaca": "MEDIA (pode expandir para outros estados)",
            "desc": "Desenvolvido pela Etice (empresa de TI do Governo do Ceara), o SAMU 360 modernizou "
                    "o fluxo das 3 Centrais de Regulacao do CE. Reduziu 12% o tempo de resposta. "
                    "App para ambulancias, GPS em tempo real, comunicacao integrada. "
                    "Risco: modelo replicavel para outros estados.",
            "difs": ["GPS em tempo real em 166 veiculos", "Reducao de 12% no tempo de resposta",
                     "App para equipes de campo", "Gratuito (governo estadual)",
                     "Resultado comprovado em producao"],
            "fraq": ["Sem IA clinica", "Limitado ao Ceara por ora", "Nao e produto comercializavel",
                     "Sem pre-alerta hospitalar", "Conformidade ministerial incompleta"],
            "fonte": "ceara.gov.br | etice.ce.gov.br (jun/2025)",
        },
        {
            "nome": "4. SINESP-CAD (SENASP / Ministerio da Justica)",
            "cor":  SINESP_COR,
            "tipo": "Sistema governamental federal (seguranca publica)",
            "alcance": "22 estados — integra 190, 191, 192, bombeiros",
            "ia":   "Nao possui",
            "ameaca": "BAIXA (foco e seguranca publica, nao saude)",
            "desc": "Sistema federal de despacho integrado para numeros de emergencia (190, 191, 192). "
                    "Foco em seguranca publica — policia, bombeiros e SAMU de forma integrada. "
                    "Nao tem foco clinico. Concorrente apenas no componente de despacho.",
            "difs": ["Integracao multi-agencia (policia + bombeiros + SAMU)", "Presente em 22 estados",
                     "Gratuito (governo federal)", "Padrao nacional de despacho"],
            "fraq": ["Foco em seguranca, nao em saude", "Sem regulacao medica especializada",
                     "Sem IA clinica ou operacional", "Interface generica"],
            "fonte": "novo.justica.gov.br/sinesp-cad",
        },
        {
            "nome": "5. Join Tecnologia da Informatica",
            "cor":  JOIN_COR,
            "tipo": "Empresa privada — prestadora de servicos TI",
            "alcance": "Sao Paulo e outros contratos governamentais",
            "ia":   "Nao identificado",
            "ameaca": "MEDIA (contratos de manutencao do SAMU SP)",
            "desc": "Venceu licitacao de manutencao e suporte do sistema de regulacao do SAMU "
                    "da cidade de Sao Paulo (R$ 5,87M/ano). Atua como integradora/mantenedora, "
                    "nao como fabricante de produto proprio. Mas detentora de contratos estrategicos.",
            "difs": ["Contrato ativo SAMU Sao Paulo (maior cidade BR)", "Experiencia em licitacoes publicas",
                     "Conhecimento do ambiente SAMU SP", "Base instalada consolidada em SP"],
            "fraq": ["Sem produto proprio de software SAMU", "Dependente de contratos de manutencao",
                     "Sem IA ou inovacao propria", "Vulneravel a substituicao por produto melhor"],
            "fonte": "Portal Transparencia SP 2023 — contrato R$ 5,87M/ano",
        },
        {
            "nome": "6. SRSAMU (Sistema informatizado — Sergipe)",
            "cor":  SRSAMU_COR,
            "tipo": "Sistema estadual (Sergipe)",
            "alcance": "Sergipe — uso local",
            "ia":   "Nao possui",
            "ameaca": "BAIXA (local, sem expansao aparente)",
            "desc": "Sistema informatizado referenciado no Manual Tecnico Operacional do SAMU 192 Sergipe. "
                    "Uso restrito ao estado. Pouca informacao publica disponivel. "
                    "Nao representa ameaca de expansao nacional.",
            "difs": ["Adaptado ao fluxo local do Sergipe", "Integrado ao manual operacional"],
            "fraq": ["Sem evidencias de expansao", "Tecnologia desconhecida",
                     "Sem produto comercializavel", "Baixa visibilidade"],
            "fonte": "Manual Tecnico SAMU 192 Sergipe — bvsms.saude.gov.br",
        },
    ]

    for f in fichas:
        ficha_concorrente(
            f["nome"], f["cor"], f["tipo"], f["alcance"],
            f["ia"], f["ameaca"], f["desc"],
            f["difs"], f["fraq"], f["fonte"], s, story
        )

    story.append(PageBreak())


def pg_adjacentes(s, story):
    story.append(hdr("Concorrentes Adjacentes — Ameaca Futura", s))
    story.append(hr())
    story.append(sp(0.3))

    fichas = [
        {
            "nome": "7. MV Saude Digital",
            "cor":  MV_COR,
            "tipo": "Empresa privada brasileira",
            "alcance": "Nacional — 27% mercado hospitalar BR",
            "ia":   "Sim (em expansao)",
            "ameaca": "ALTA FUTURA (se criar modulo SAMU)",
            "desc": "Maior player brasileiro de gestao hospitalar (27% de participacao). "
                    "Forte em gestao administrativa de hospitais publicos e privados. "
                    "Ainda sem modulo dedicado de regulacao SAMU — mas infraestrutura e "
                    "base de clientes permitiriam entrada rapida no segmento.",
            "difs": ["Maior market share hospitalar BR", "Relacionamento com secretarias de saude",
                     "Produto maduro com IA em desenvolvimento", "Equipe comercial nacional"],
            "fraq": ["Foco hospitalar, nao pre-hospitalar", "Sem experiencia em regulacao SAMU",
                     "Produto pesado para municipios pequenos", "Nao conhece o fluxo SAMU"],
            "fonte": "mv.com.br | saudebusiness.com",
        },
        {
            "nome": "8. Philips Tasy / Bionexo",
            "cor":  TASY_COR,
            "tipo": "Multinacional (vendido a Bionexo em 2025)",
            "alcance": "Nacional — ~500 instituicoes medicas",
            "ia":   "Sim (dispositivo medico ANVISA)",
            "ameaca": "MEDIA (mudanca de controle — direcao incerta)",
            "desc": "Primeiro prontuario eletrônico regularizado como dispositivo medico pela ANVISA. "
                    "Vendido pela Philips a Bionexo por ~R$ 1 bilhao em 2025. Foco em hospitais. "
                    "Mudanca de controle pode redirecionar estrategia para urgencia e emergencia.",
            "difs": ["Unico EMR certificado dispositivo medico ANVISA", "500+ instituicoes",
                     "Arquitetura clinica robusta", "IA embarcada"],
            "fraq": ["Transicao de controle — incerteza estrategica", "Sem modulo SAMU",
                     "Custo alto — inadequado para municipios", "Foco hospitalar"],
            "fonte": "philips.com.br | fenati.org.br (venda R$ 1 bi / 2025)",
        },
        {
            "nome": "9. Monuv",
            "cor":  MONUV_COR,
            "tipo": "Empresa privada brasileira (monitoramento urbano)",
            "alcance": "Nacional — integrado ao Smart Sampa (SP)",
            "ia":   "Nao identificado",
            "ameaca": "BAIXA (foco em frota, nao em regulacao)",
            "desc": "Plataforma de monitoramento de frotas e veiculos urbanos. Integrada ao "
                    "Smart Sampa (sistema de inteligencia da Prefeitura de SP). "
                    "Atua no componente de rastreio de viaturas — um dos modulos do SAMU Amigo.",
            "difs": ["Rastreio de frota consolidado", "Integracao com plataformas de cidade inteligente",
                     "Parceria com Prefeitura de SP"],
            "fraq": ["Sem regulacao medica", "Sem IA clinica", "Sem despacho ou triagem",
                     "Produto parcial (so frota)"],
            "fonte": "suporte.monuv.com.br (Smart Sampa / Prefeitura SP)",
        },
        {
            "nome": "10. TOTVS Saude",
            "cor":  TOTVS_COR,
            "tipo": "Empresa privada brasileira (ERP / Saude)",
            "alcance": "Nacional — 16% mercado hospitalar BR",
            "ia":   "Sim (Claude/GenAI integrado)",
            "ameaca": "ALTA FUTURA (estrategia agressiva de expansao)",
            "desc": "Terceiro maior player de TI hospitalar no Brasil (16%). A TOTVS tem estrategia "
                    "declarada de desbancar MV e Philips em sistemas de saude. Com recursos financeiros "
                    "e equipe comercial, poderia criar modulo SAMU em 12-18 meses se identificar o mercado.",
            "difs": ["Expansao agressiva declarada em saude", "Recursos para P&D rapido",
                     "Base de 40.000+ clientes em outras verticais", "IA generativa integrada"],
            "fraq": ["Ainda sem produto SAMU", "Nao conhece o ecossistema de urgencia",
                     "Foco hospitalar atual", "Produto pesado para municipios pequenos"],
            "fonte": "saudebusiness.com | totvs.com",
        },
        {
            "nome": "11. HXGN OnCall (Hexagon Safety & Infrastructure)",
            "cor":  HEXAGON_COR,
            "tipo": "Multinacional sueca — lider global CAD",
            "alcance": "Global — presenca em BR (grandes contratos)",
            "ia":   "Sim (Smart Advisor — ML operacional)",
            "ameaca": "MEDIA (custo proibitivo para municipios medios)",
            "desc": "Lider mundial em CAD (Computer-Aided Dispatch). Presente no Brasil em grandes "
                    "contratos governamentais. Plataforma completa: Dispatch + Analytics + Records + GIS. "
                    "Ameaca limitada pelo custo enterprise e foco nao-clinico.",
            "difs": ["Referencia global em CAD", "IA operacional (Smart Advisor)", "GIS enterprise",
                     "Despacho automatico por algoritmo", "SLA 99,9% garantido"],
            "fraq": ["Custo proibitivo para municipios BR medios", "Sem foco em SAMU brasileiro",
                     "Sem protocolos MS integrados", "Sem FAPH", "Sem IA clinica"],
            "fonte": "hexagon.com | Hexagon Annual Report 2024",
        },
    ]

    for f in fichas:
        ficha_concorrente(
            f["nome"], f["cor"], f["tipo"], f["alcance"],
            f["ia"], f["ameaca"], f["desc"],
            f["difs"], f["fraq"], f["fonte"], s, story
        )

    story.append(PageBreak())


def pg_matriz_ameaca(s, story):
    story.append(hdr("Matriz de Ameaca: Probabilidade x Impacto", s, "mapa_titulo"))
    story.append(HRFlowable(width="100%", thickness=2, color=DOURADO,
                             spaceAfter=8, spaceBefore=4))
    story.append(sp(0.3))

    story.append(Paragraph(
        "Avaliacao de cada concorrente pelo grau de ameaca ao SAMU Amigo "
        "(probabilidade de competir diretamente x impacto potencial no mercado):",
        s["body"]
    ))
    story.append(sp(0.4))

    # Quadrante 2x2 como tabela
    q_data = [
        ["",
         Paragraph("Impacto ALTO", ParagraphStyle("qi", fontName="Helvetica-Bold", fontSize=10,
                                                    textColor=BRANCO, alignment=TA_CENTER, leading=14)),
         Paragraph("Impacto BAIXO", ParagraphStyle("qi", fontName="Helvetica-Bold", fontSize=10,
                                                     textColor=BRANCO, alignment=TA_CENTER, leading=14))],
        [Paragraph("Prob.\nALTA", ParagraphStyle("qp", fontName="Helvetica-Bold", fontSize=10,
                                                   textColor=BRANCO, alignment=TA_CENTER, leading=14)),
         Paragraph("CRITICO\n\nMedSave SEMS SAMU\nMV Saude Digital\nTOTVS Saude",
                   ParagraphStyle("qc", fontName="Helvetica-Bold", fontSize=10,
                                  textColor=BRANCO, alignment=TA_CENTER, leading=15)),
         Paragraph("MONITORAR\n\nJoin Tecnologia\nSAMU 360 (Etice)",
                   ParagraphStyle("qm", fontName="Helvetica", fontSize=10,
                                  textColor=BRANCO, alignment=TA_CENTER, leading=15))],
        [Paragraph("Prob.\nBAIXA", ParagraphStyle("qp", fontName="Helvetica-Bold", fontSize=10,
                                                    textColor=BRANCO, alignment=TA_CENTER, leading=14)),
         Paragraph("VIGIAR\n\nHXGN OnCall\nPhilips Tasy/Bionexo\ne-SUS SAMU",
                   ParagraphStyle("qv", fontName="Helvetica", fontSize=10,
                                  textColor=BRANCO, alignment=TA_CENTER, leading=15)),
         Paragraph("BAIXA PRIORIDADE\n\nSINESP-CAD\nSRSAMU (Sergipe)\nMonuv",
                   ParagraphStyle("qb", fontName="Helvetica", fontSize=10,
                                  textColor=HexColor("#AAAAAA"), alignment=TA_CENTER, leading=15))],
    ]

    col_w = [CONTENT_W * p for p in [0.16, 0.42, 0.42]]
    qt = Table(q_data, colWidths=col_w,
               rowHeights=[1.0 * cm, 4.0 * cm, 4.0 * cm])
    qt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), AZUL_ESCURO),
        ("BACKGROUND", (1, 0), (2, 0), AZUL_MEDIO),
        ("BACKGROUND", (0, 1), (0, 2), AZUL_MEDIO),
        ("BACKGROUND", (1, 1), (1, 1), VERMELHO),         # CRITICO
        ("BACKGROUND", (2, 1), (2, 1), LARANJA),          # MONITORAR
        ("BACKGROUND", (1, 2), (1, 2), HexColor("#1A5276")),  # VIGIAR
        ("BACKGROUND", (2, 2), (2, 2), HexColor("#1C2833")),  # BAIXA PRIOR
        ("GRID",       (0, 0), (-1, -1), 2, BRANCO),
        ("VALIGN",     (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN",      (0, 0), (-1, -1), "CENTER"),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(qt)
    story.append(sp(0.4))
    story.append(Paragraph(
        "CRITICO = agir agora  |  MONITORAR = acompanhar trimestralmente  |  "
        "VIGIAR = acompanhar anualmente  |  BAIXA PRIORIDADE = sem acao imediata",
        s["nota"]
    ))
    story.append(PageBreak())


def pg_vantagem_samu(s, story):
    story.append(hdr("Por que o SAMU Amigo Supera Todos", s))
    story.append(hr())
    story.append(sp(0.3))

    vantagens = [
        (SAMU_COR, "ISA: IA Clinica que Nenhum Concorrente Tem",
         "MedSave, e-SUS, SAMU 360, SINESP, Join, SRSAMU: zero IA. "
         "MV, TOTVS e Tasy tem IA hospitalar — nao clinica para SAMU. "
         "HXGN tem IA operacional, nao clinica. "
         "A ISA e o unico diferencial tecnologico verdadeiro neste mercado."),

        (VERDE, "Custo Zero de Licenca em um Mercado de R$ 560 Mi",
         "O maior inimigo de qualquer produto neste mercado e o e-SUS gratuito. "
         "O SAMU Amigo tambem e gratuito — mas entrega o que o e-SUS nunca vai ter: "
         "IA, GPS, FAPH, interface moderna. Custo zero + inovacao = argumento imbativel."),

        (DOURADO, "FAPH: Exclusividade que Salva Vidas",
         "Pre-alerta hospitalar com sinais vitais, Glasgow, procedimentos e ETA. "
         "Nenhum dos 11 concorrentes tem um modulo equivalente. "
         "E o tipo de funcionalidade que nenhum gestor consegue ignorar "
         "quando ve uma demonstracao ao vivo."),

        (AZUL_MEDIO, "Janela de Oportunidade: MV e TOTVS Ainda Nao Chegaram",
         "Os dois players com maior poder de fogo (MV com 27% do mercado hospitalar, "
         "TOTVS com expansao agressiva declarada) ainda nao tem produto SAMU. "
         "Essa janela se fecha em 12-24 meses. O SAMU Amigo precisa ocupar o espaco agora."),

        (ROXO, "Complementaridade Estrategica com o e-SUS",
         "Ao ser complementar ao sistema federal obrigatorio, o SAMU Amigo elimina "
         "a principal objecao: 'ja temos o e-SUS'. Nenhum concorrente privado tem "
         "essa narrativa de complementaridade — todos tentam substituir o e-SUS, "
         "o que gera resistencia politica."),
    ]

    for cor, titulo, desc in vantagens:
        bg_desc = HexColor("#F8F9FA")
        if cor == SAMU_COR:   bg_desc = HexColor("#FDEDEC")
        elif cor == VERDE:    bg_desc = HexColor("#EAFAF1")
        elif cor == DOURADO:  bg_desc = HexColor("#FEF9E7")
        elif cor == AZUL_MEDIO: bg_desc = HexColor("#EAF2FF")
        elif cor == ROXO:     bg_desc = HexColor("#F5EEF8")

        bloco = Table([
            [Paragraph(titulo, ParagraphStyle("vt", fontName="Helvetica-Bold", fontSize=11,
                                               textColor=BRANCO, leading=15))],
            [Paragraph(desc, ParagraphStyle("vd", fontName="Helvetica", fontSize=9,
                                             textColor=CINZA_ESCURO, leading=14))],
        ], colWidths=[CONTENT_W])
        bloco.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (0, 0), cor),
            ("BACKGROUND",    (0, 1), (0, 1), bg_desc),
            ("TOPPADDING",    (0, 0), (-1, -1), 9),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
            ("LEFTPADDING",   (0, 0), (-1, -1), 12),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 12),
        ]))
        story.append(bloco)
        story.append(sp(0.2))

    story.append(PageBreak())


def pg_conclusao(s, story):
    story.append(hdr("Conclusao do Mapa Competitivo", s))
    story.append(hr())
    story.append(sp(0.4))

    # Tabela resumo final
    final = [
        ["Concorrente",       "Tipo",    "IA?", "Ameaca",  "Acao SAMU Amigo"],
        ["MedSave SEMS",      "Privado", "Nao", "Alta",    "Superar com ISA + FAPH + custo menor"],
        ["e-SUS SAMU",        "Gov.Fed", "Nao", "Media",   "Ser complementar — nunca competir"],
        ["SAMU 360 (Etice)",  "Gov.Est", "Nao", "Media",   "Monitorar expansao para outros estados"],
        ["Join Tecnologia",   "Privado", "Nao", "Media",   "Substituir nos proximos contratos SP"],
        ["SINESP-CAD",        "Gov.Fed", "Nao", "Baixa",   "Integrar — nao compete no clinico"],
        ["SRSAMU Sergipe",    "Gov.Est", "Nao", "Baixa",   "Ignorar — sem expansao prevista"],
        ["MV Saude Digital",  "Privado", "Sim", "Alt.Fut", "Ocupar mercado ANTES que entre"],
        ["Philips Tasy",      "Privado", "Sim", "Media",   "Acompanhar pos-aquisicao Bionexo"],
        ["Monuv",             "Privado", "Nao", "Baixa",   "Integrar API de frota se necessario"],
        ["TOTVS Saude",       "Privado", "Sim", "Alt.Fut", "Ocupar mercado ANTES que entre"],
        ["HXGN OnCall",       "Multinal","Sim", "Media",   "Diferenciar pelo custo e foco clinico"],
    ]

    col_w = [CONTENT_W * p for p in [0.22, 0.10, 0.07, 0.12, 0.49]]

    def ameaca_cor(a):
        if "Alta" in a or "Fut" in a: return VERMELHO
        if "Media" in a:              return LARANJA
        return CINZA_MEDIO

    rows = []
    for i, row in enumerate(final):
        if i == 0:
            rows.append([
                Paragraph(c, ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9,
                                             textColor=BRANCO, alignment=TA_CENTER, leading=12))
                for c in row
            ])
        else:
            rows.append([
                Paragraph(row[0], ParagraphStyle("r0", fontName="Helvetica-Bold", fontSize=8,
                                                  textColor=AZUL_ESCURO, leading=13)),
                Paragraph(row[1], ParagraphStyle("r1", fontName="Helvetica", fontSize=8,
                                                  textColor=CINZA_MEDIO, alignment=TA_CENTER, leading=12)),
                Paragraph(row[2], ParagraphStyle("r2", fontName="Helvetica-Bold", fontSize=8,
                                                  textColor=VERMELHO if row[2] == "Nao" else VERDE,
                                                  alignment=TA_CENTER, leading=12)),
                Paragraph(row[3], ParagraphStyle("r3", fontName="Helvetica-Bold", fontSize=8,
                                                  textColor=ameaca_cor(row[3]),
                                                  alignment=TA_CENTER, leading=12)),
                Paragraph(row[4], ParagraphStyle("r4", fontName="Helvetica", fontSize=8,
                                                  textColor=CINZA_ESCURO, leading=12)),
            ])

    t = Table(rows, colWidths=col_w)
    t.setStyle(TableStyle([
        ("BACKGROUND",     (0, 0), (-1, 0), AZUL_ESCURO),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
        ("GRID",           (0, 0), (-1, -1), 0.4, HexColor("#CCCCCC")),
        ("VALIGN",         (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",     (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING",  (0, 0), (-1, -1), 7),
        ("LEFTPADDING",    (0, 0), (-1, -1), 7),
        ("LINEABOVE",      (0, 7), (-1, 7), 1.5, DOURADO),
    ]))
    story.append(t)
    story.append(sp(0.3))
    story.append(Paragraph(
        "Linhas 1-6 = concorrentes diretos SAMU  |  Linhas 7-12 = adjacentes  |  Alt.Fut = ameaca futura alta",
        s["nota"]
    ))
    story.append(sp(0.5))

    msg = Table([[Paragraph(
        '"O SAMU Amigo nao tem um concorrente que faca tudo que ele faz.<br/>'
        'A janela esta aberta. O mercado esta esperando."',
        ParagraphStyle("msg", fontName="Helvetica-BoldOblique", fontSize=13,
                       textColor=DOURADO, alignment=TA_CENTER, leading=19)
    )]], colWidths=[CONTENT_W])
    msg.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), AZUL_ESCURO),
        ("TOPPADDING",    (0, 0), (-1, -1), 18),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 18),
        ("LEFTPADDING",   (0, 0), (-1, -1), 22),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 22),
        ("LINEABOVE",     (0, 0), (-1, 0), 3, DOURADO),
        ("LINEBELOW",     (0, -1), (-1, -1), 3, DOURADO),
    ]))
    story.append(msg)
    story.append(PageBreak())


# =====================================================================
# MONTAGEM
# =====================================================================
def gerar(output):
    s     = E()
    story = []

    pg_capa(s, story)
    pg_secao("Panorama Geral", "11 concorrentes identificados no mercado brasileiro", s, story)
    pg_visao_geral(s, story)
    pg_secao("Concorrentes Diretos", "Os 6 players que disputam regulacao e despacho SAMU", s, story)
    pg_diretos(s, story)
    pg_secao("Concorrentes Adjacentes", "Os 5 players que podem entrar no segmento", s, story)
    pg_adjacentes(s, story)
    pg_secao("Matriz de Ameaca", "Probabilidade x Impacto de cada concorrente", s, story)
    pg_matriz_ameaca(s, story)
    pg_secao("Vantagem Competitiva", "Por que o SAMU Amigo supera todos os 11", s, story)
    pg_vantagem_samu(s, story)
    pg_secao("Conclusao", "Plano de acao frente ao mapa competitivo", s, story)
    pg_conclusao(s, story)

    doc = SimpleDocTemplate(
        output, pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN,  bottomMargin=MARGIN,
    )

    MAPA_PAGES = {7, 8, 13, 14}

    def on_page(c, doc):
        n = doc.page
        if n == 1:
            BG("capa")(c, doc)
        elif n % 2 == 0:
            BG("secao")(c, doc)
        elif n in MAPA_PAGES:
            BG("mapa")(c, doc)
        else:
            BG("normal")(c, doc)

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f"PDF gerado: {output}")


if __name__ == "__main__":
    gerar("samu_amigo_mapa_competitivo_brasil.pdf")

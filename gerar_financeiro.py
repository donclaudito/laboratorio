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
VERDE_NEON     = HexColor("#2ECC71")
VERMELHO       = HexColor("#C0392B")
LARANJA        = HexColor("#E67E22")
AMARELO        = HexColor("#F1C40F")
DOURADO        = HexColor("#D4AC0D")
OURO           = HexColor("#F39C12")
MEDSAVE_COR    = HexColor("#2C3E7A")
HEXAGON_COR    = HexColor("#0066CC")
ESUS_COR       = HexColor("#1A6B3C")
SAMU_COR       = HexColor("#C0392B")
SAMU_DARK      = HexColor("#7B241C")

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
            # Gradiente simulado com retangulos
            for i, alpha in enumerate([0.03, 0.05, 0.04, 0.03]):
                c.setFillColor(HexColor("#1A3A6B"))
                c.rect(0, i * h / 4, w, h / 4, fill=1, stroke=0)
            # Faixa dourada superior
            c.setFillColor(DOURADO)
            c.rect(0, h - 0.6 * cm, w, 0.6 * cm, fill=1, stroke=0)
            # Faixa dourada inferior
            c.setFillColor(DOURADO)
            c.rect(0, 0, w, 0.6 * cm, fill=1, stroke=0)
            # Barra lateral tricolor
            c.setFillColor(SAMU_COR)
            c.rect(0, 0, 0.5 * cm, h / 4, fill=1, stroke=0)
            c.setFillColor(MEDSAVE_COR)
            c.rect(0, h / 4, 0.5 * cm, h / 4, fill=1, stroke=0)
            c.setFillColor(HEXAGON_COR)
            c.rect(0, h / 2, 0.5 * cm, h / 4, fill=1, stroke=0)
            c.setFillColor(ESUS_COR)
            c.rect(0, 3 * h / 4, 0.5 * cm, h / 4, fill=1, stroke=0)
            # Marca dagua R$
            c.setFillColor(HexColor("#FFFFFF04"))
            c.setFont("Helvetica-Bold", 200)
            c.drawCentredString(w / 2, h / 2 - 80, "R$")

        elif self.tipo == "secao":
            c.setFillColor(AZUL_MEDIO)
            c.rect(0, 0, w, h, fill=1, stroke=0)
            c.setFillColor(DOURADO)
            c.rect(0, 0, 0.7 * cm, h, fill=1, stroke=0)
            c.setFillColor(HexColor("#FFFFFF05"))
            c.setFont("Helvetica-Bold", 80)
            c.drawCentredString(w / 2, h / 2 - 25, "MERCADO")

        elif self.tipo == "projecao":
            c.setFillColor(PRETO)
            c.rect(0, 0, w, h, fill=1, stroke=0)
            c.setFillColor(VERDE)
            c.rect(0, 0, 0.7 * cm, h, fill=1, stroke=0)
            c.setFillColor(HexColor("#27AE6008"))
            c.rect(0, 0, w, h * 0.35, fill=1, stroke=0)

        else:  # normal
            c.setFillColor(BRANCO)
            c.rect(0, 0, w, h, fill=1, stroke=0)
            # Header
            c.setFillColor(AZUL_ESCURO)
            c.rect(0, h - 1.8 * cm, w, 1.8 * cm, fill=1, stroke=0)
            c.setFillColor(DOURADO)
            c.rect(0, h - 1.8 * cm, 0.45 * cm, 1.8 * cm, fill=1, stroke=0)
            c.setFillColor(BRANCO)
            c.setFont("Helvetica-Bold", 9)
            c.drawString(1.2 * cm, h - 1.2 * cm, "SAMU AMIGO  |  Potencial Comercial e Financeiro")
            c.setFont("Helvetica", 9)
            c.drawRightString(w - 1.2 * cm, h - 1.2 * cm, "Mercado Brasileiro · 2025")
            # Footer
            c.setFillColor(AZUL_ESCURO)
            c.rect(0, 0, w, 1.0 * cm, fill=1, stroke=0)
            c.setFillColor(DOURADO)
            c.rect(0, 0, w, 0.15 * cm, fill=1, stroke=0)
            c.setFillColor(HexColor("#AAAAAA"))
            c.setFont("Helvetica", 8)
            c.drawCentredString(w / 2, 0.35 * cm, f"Pagina {doc.page}  |  Dados de mercado e projecoes estimadas com base em contratos publicos disponíveis")

        c.restoreState()


# =====================================================================
# ESTILOS
# =====================================================================
def E():
    return {
        "capa_label":   ParagraphStyle("cl", fontName="Helvetica-Bold", fontSize=12,
                                        textColor=DOURADO, alignment=TA_CENTER, leading=17),
        "capa_titulo":  ParagraphStyle("ct", fontName="Helvetica-Bold", fontSize=42,
                                        textColor=BRANCO, alignment=TA_CENTER, leading=50),
        "capa_sub":     ParagraphStyle("cs", fontName="Helvetica", fontSize=15,
                                        textColor=HexColor("#B0C4DE"), alignment=TA_CENTER, leading=21),
        "capa_rodape":  ParagraphStyle("cr", fontName="Helvetica", fontSize=9,
                                        textColor=HexColor("#666666"), alignment=TA_CENTER, leading=14),
        "secao_titulo": ParagraphStyle("st", fontName="Helvetica-Bold", fontSize=28,
                                        textColor=BRANCO, alignment=TA_CENTER, leading=36),
        "secao_sub":    ParagraphStyle("ss", fontName="Helvetica", fontSize=13,
                                        textColor=HexColor("#B0C4DE"), alignment=TA_CENTER, leading=18),
        "slide_titulo": ParagraphStyle("slt", fontName="Helvetica-Bold", fontSize=17,
                                        textColor=BRANCO, alignment=TA_LEFT, leading=22),
        "proj_titulo":  ParagraphStyle("pt2", fontName="Helvetica-Bold", fontSize=17,
                                        textColor=VERDE_CLARO, alignment=TA_LEFT, leading=22),
        "h2":           ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12,
                                        textColor=AZUL_ESCURO, leading=17, spaceAfter=5, spaceBefore=8),
        "body":         ParagraphStyle("body", fontName="Helvetica", fontSize=10,
                                        textColor=CINZA_ESCURO, leading=15, spaceAfter=4),
        "nota":         ParagraphStyle("nota", fontName="Helvetica-Oblique", fontSize=8,
                                        textColor=CINZA_MEDIO, leading=12, alignment=TA_CENTER),
        "valor_grande": ParagraphStyle("vg", fontName="Helvetica-Bold", fontSize=22,
                                        textColor=VERDE_NEON, alignment=TA_CENTER, leading=28),
        "valor_medio":  ParagraphStyle("vm", fontName="Helvetica-Bold", fontSize=14,
                                        textColor=DOURADO, alignment=TA_CENTER, leading=18),
        "fonte":        ParagraphStyle("fo", fontName="Helvetica-Oblique", fontSize=7,
                                        textColor=CINZA_MEDIO, leading=10, alignment=TA_LEFT),
    }


def sp(h):  return Spacer(1, h * cm)
def hr(cor=DOURADO, t=2):
    return HRFlowable(width="100%", thickness=t, color=cor, spaceAfter=8, spaceBefore=4)
def hdr(txt, s, key="slide_titulo"):
    return Paragraph(txt, s[key])


# =====================================================================
# PAGINAS
# =====================================================================

def pg_capa(s, story):
    story.append(sp(2.5))
    story.append(Paragraph("ANALISE COMERCIAL E FINANCEIRA", s["capa_label"]))
    story.append(sp(0.3))
    story.append(Paragraph("SAMU AMIGO", s["capa_titulo"]))
    story.append(sp(0.2))
    story.append(Paragraph("e os Tres Concorrentes", ParagraphStyle(
        "cs2", fontName="Helvetica", fontSize=20,
        textColor=HexColor("#7FB3D3"), alignment=TA_CENTER, leading=26
    )))
    story.append(sp(0.4))
    story.append(HRFlowable(width="55%", thickness=3, color=DOURADO,
                             spaceAfter=10, spaceBefore=4, hAlign="CENTER"))
    story.append(sp(0.2))
    story.append(Paragraph(
        "Faturamento Atual  •  Mercado Brasileiro  •  Potencial de Receita",
        s["capa_sub"]
    ))
    story.append(sp(0.4))

    metricas = [
        ["4.143\nMunicipios SAMU", "R$ 560 Mi\nMercado Total BR", "R$ 2,4 Bi\nInvest. Saude Digital 2025"],
    ]
    mt = Table(metricas, colWidths=[CONTENT_W / 3] * 3)
    mt.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), HexColor("#0D2240")),
        ("TEXTCOLOR",     (0, 0), (-1, -1), DOURADO),
        ("FONTNAME",      (0, 0), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, -1), 11),
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 14),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
        ("GRID",          (0, 0), (-1, -1), 1, AZUL_MEDIO),
    ]))
    story.append(mt)
    story.append(sp(0.8))
    story.append(Paragraph(
        "Fontes: Ministerio da Saude, Portal Transparencia SP, Hexagon Annual Report 2024, estimativas de mercado",
        s["capa_rodape"]
    ))
    story.append(PageBreak())


def pg_secao(titulo, sub, s, story):
    story.append(sp(5.2))
    story.append(Paragraph(titulo, s["secao_titulo"]))
    story.append(sp(0.3))
    story.append(HRFlowable(width="50%", thickness=3, color=DOURADO,
                             spaceAfter=10, spaceBefore=4, hAlign="CENTER"))
    story.append(Paragraph(sub, s["secao_sub"]))
    story.append(PageBreak())


def pg_tamanho_mercado(s, story):
    story.append(hdr("O Mercado Brasileiro de Software para SAMU", s))
    story.append(hr())
    story.append(sp(0.3))

    story.append(Paragraph(
        "Base de calculo: 4.143 municipios cobertos pelo SAMU 192, segmentados por porte "
        "e valor medio de contrato anual com referencia ao contrato publico de Sao Paulo "
        "(R$ 5,87M/ano — Portal Transparencia SP, 2023).",
        s["body"]
    ))
    story.append(sp(0.3))

    segmentos = [
        ["Segmento",        "Populacao",    "Municipios", "Ticket Medio/Ano", "TAM Segmento"],
        ["Grande",          "> 500 mil hab","~50",        "R$ 1.500.000",     "R$ 75.000.000"],
        ["Medio-Grande",    "200-500 mil",  "~150",       "R$ 600.000",       "R$ 90.000.000"],
        ["Medio",           "100-200 mil",  "~300",       "R$ 350.000",       "R$ 105.000.000"],
        ["Medio-Pequeno",   "50-100 mil",   "~600",       "R$ 180.000",       "R$ 108.000.000"],
        ["Pequeno",         "< 50 mil",     "~3.043",     "R$ 60.000",        "R$ 182.580.000"],
        ["TOTAL MERCADO",   "—",            "4.143",      "—",                "R$ 560.580.000"],
    ]

    col_w = [CONTENT_W * p for p in [0.22, 0.18, 0.13, 0.22, 0.25]]

    rows = []
    for i, row in enumerate(segmentos):
        is_header = i == 0
        is_total  = i == len(segmentos) - 1
        fn   = "Helvetica-Bold"
        size = 10 if not is_total else 11
        tc_dim   = BRANCO if is_header else (DOURADO if is_total else AZUL_ESCURO)
        tc_val   = BRANCO if is_header else (VERDE_NEON if is_total else CINZA_ESCURO)
        tc_total = BRANCO if is_header else (VERDE_NEON if is_total else VERDE)

        rows.append([
            Paragraph(row[0], ParagraphStyle("r0", fontName=fn, fontSize=size,
                                              textColor=tc_dim, leading=14)),
            Paragraph(row[1], ParagraphStyle("r1", fontName="Helvetica", fontSize=9,
                                              textColor=tc_val, alignment=TA_CENTER, leading=13)),
            Paragraph(row[2], ParagraphStyle("r2", fontName="Helvetica-Bold", fontSize=9,
                                              textColor=tc_val, alignment=TA_CENTER, leading=13)),
            Paragraph(row[3], ParagraphStyle("r3", fontName="Helvetica-Bold", fontSize=9,
                                              textColor=tc_val, alignment=TA_CENTER, leading=13)),
            Paragraph(row[4], ParagraphStyle("r4", fontName="Helvetica-Bold", fontSize=size,
                                              textColor=tc_total, alignment=TA_RIGHT, leading=14)),
        ])

    t = Table(rows, colWidths=col_w)
    t.setStyle(TableStyle([
        ("BACKGROUND",     (0, 0), (-1, 0), AZUL_ESCURO),
        ("BACKGROUND",     (0, -1), (-1, -1), HexColor("#0D2240")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -2), [CINZA_CLARO, BRANCO]),
        ("GRID",           (0, 0), (-1, -1), 0.5, HexColor("#CCCCCC")),
        ("VALIGN",         (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",     (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING",  (0, 0), (-1, -1), 9),
        ("LEFTPADDING",    (0, 0), (-1, -1), 8),
        ("LINEABOVE",      (0, -1), (-1, -1), 2, DOURADO),
    ]))
    story.append(t)
    story.append(sp(0.4))

    # KPIs do mercado
    kpis = [
        ["R$ 560 Mi", "TAM\nMercado Total"],
        ["R$ 195 Mi", "SAM\nGrandes e Medios"],
        ["R$ 50 Mi", "SOM\nAlvo inicial SAMU Amigo"],
    ]
    kt = Table(kpis, colWidths=[CONTENT_W / 3] * 3)
    kt.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), AZUL_ESCURO),
        ("FONTNAME",      (0, 0), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (0, -1), 20),
        ("FONTSIZE",      (0, 1), (-1, -1), 9),
        ("TEXTCOLOR",     (0, 0), (0, -1), DOURADO),
        ("TEXTCOLOR",     (0, 1), (-1, -1), HexColor("#AAAAAA")),
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("GRID",          (0, 0), (-1, -1), 1, AZUL_MEDIO),
        ("TOPPADDING",    (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
    ]))
    # Corrigir estilos por célula
    kpi_rows = []
    for val, label in kpis:
        kpi_rows.append([val, label])

    kt2 = Table([[
        [Paragraph(v, ParagraphStyle("kv", fontName="Helvetica-Bold", fontSize=20,
                                     textColor=DOURADO, alignment=TA_CENTER, leading=26)),
         Paragraph(l.replace("\n", "<br/>"), ParagraphStyle("kl", fontName="Helvetica", fontSize=9,
                                                              textColor=HexColor("#AAAAAA"),
                                                              alignment=TA_CENTER, leading=13))]
        for v, l in kpis
    ]], colWidths=[CONTENT_W / 3] * 3)

    real_kpi = []
    for v, l in kpis:
        cell = Table(
            [[Paragraph(v, ParagraphStyle("kv", fontName="Helvetica-Bold", fontSize=18,
                                           textColor=DOURADO, alignment=TA_CENTER, leading=24))],
             [Paragraph(l.replace("\n", "<br/>"), ParagraphStyle("kl", fontName="Helvetica",
                                                                   fontSize=9,
                                                                   textColor=HexColor("#AAAAAA"),
                                                                   alignment=TA_CENTER, leading=13))]],
            colWidths=[CONTENT_W / 3 - 0.1 * cm]
        )
        cell.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (-1, -1), AZUL_ESCURO),
            ("TOPPADDING",    (0, 0), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ]))
        real_kpi.append(cell)

    outer_kpi = Table([real_kpi], colWidths=[CONTENT_W / 3] * 3)
    outer_kpi.setStyle(TableStyle([
        ("GRID",   (0, 0), (-1, -1), 1, AZUL_MEDIO),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(outer_kpi)
    story.append(sp(0.2))
    story.append(Paragraph(
        "TAM = Total Addressable Market  |  SAM = Serviceable Addressable Market  |  "
        "SOM = Serviceable Obtainable Market (alvo realista ano 1-3)",
        s["nota"]
    ))
    story.append(PageBreak())


def pg_faturamento_concorrentes(s, story):
    story.append(hdr("Faturamento Anual dos Concorrentes", s))
    story.append(hr())
    story.append(sp(0.3))

    story.append(Paragraph(
        "Estimativas baseadas em dados publicos, relatorios anuais e contratos disponiveis:",
        s["body"]
    ))
    story.append(sp(0.3))

    concorrentes = [
        {
            "nome":    "MedSave SEMS SAMU",
            "cor":     MEDSAVE_COR,
            "tipo":    "Empresa brasileira — produto comercial para SAMU",
            "fat_br":  "R$ 15 - 30 Mi / ano",
            "clientes":"~50-100 centrais SAMU ativas",
            "ticket":  "R$ 180.000 - R$ 400.000 / central / ano",
            "modelo":  "Licenca + suporte + atualizacoes",
            "crescim": "~15-20% a.a. (mercado emergente)",
            "fraqueza":"Sem IA clinica. Produto estatico. Nao escala internacionalmente.",
            "fonte":   "Estimativa baseada em perfil de empresa, porte e ticket medio de mercado BR",
        },
        {
            "nome":    "HXGN OnCall (Hexagon)",
            "cor":     HEXAGON_COR,
            "tipo":    "Multinacional sueca — divisao Safety & Infrastructure",
            "fat_br":  "R$ 80 - 150 Mi / ano (Brasil)",
            "clientes":"~20-40 grandes contratos publicos BR",
            "ticket":  "R$ 2.000.000 - R$ 8.000.000 / contrato / ano",
            "modelo":  "SaaS + On-premises + servicos profissionais",
            "crescim": "Hexagon SI global: EUR 140,8 Mi (Q4/2024). Brasil ~9% receita global",
            "fraqueza":"Custo proibitivo para municipios medios. Generico. Sem foco SAMU BR.",
            "fonte":   "Hexagon Year-End Report 2024 (hexagon.com). Estimativa BR proporcional.",
        },
        {
            "nome":    "e-SUS SAMU (DATASUS)",
            "cor":     ESUS_COR,
            "tipo":    "Sistema governamental — custo ao Estado, sem receita comercial",
            "fat_br":  "R$ 0 (gratuito)",
            "clientes":"~4.143 municipios (mandato federal)",
            "ticket":  "R$ 0 — distribuido pelo Ministerio da Saude",
            "modelo":  "Open-source governamental — custo de manutencao ~R$ 15-25Mi/ano (MS)",
            "crescim": "Nao aplicavel — sistema de Estado",
            "fraqueza":"Zero receita. Zero inovacao. Tecnologia legada. Atualizacoes em anos.",
            "fonte":   "DATASUS, datasus.saude.gov.br/e-sus-samu. Custo estimado de manutencao.",
        },
    ]

    for c in concorrentes:
        # Header do card
        h_row = Table([[
            Paragraph(c["nome"], ParagraphStyle("cn", fontName="Helvetica-Bold", fontSize=13,
                                                 textColor=BRANCO, leading=17)),
            Paragraph(c["fat_br"], ParagraphStyle("cf", fontName="Helvetica-Bold", fontSize=14,
                                                    textColor=AMARELO, alignment=TA_RIGHT, leading=18)),
        ]], colWidths=[CONTENT_W * 0.55, CONTENT_W * 0.45])
        h_row.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (-1, -1), c["cor"]),
            ("TOPPADDING",    (0, 0), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
            ("LEFTPADDING",   (0, 0), (-1, -1), 12),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 12),
            ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ]))
        story.append(h_row)

        detalhes = [
            ("Tipo",           c["tipo"]),
            ("Clientes ativos",c["clientes"]),
            ("Ticket medio",   c["ticket"]),
            ("Modelo",         c["modelo"]),
            ("Crescimento",    c["crescim"]),
            ("Fraqueza chave", c["fraqueza"]),
        ]
        for j, (label, val) in enumerate(detalhes):
            dr = Table([[
                Paragraph(label, ParagraphStyle("dl", fontName="Helvetica-Bold", fontSize=8,
                                                 textColor=c["cor"], leading=12)),
                Paragraph(val,   ParagraphStyle("dv", fontName="Helvetica", fontSize=9,
                                                 textColor=CINZA_ESCURO, leading=13)),
            ]], colWidths=[CONTENT_W * 0.22, CONTENT_W * 0.78])
            dr.setStyle(TableStyle([
                ("BACKGROUND",    (0, 0), (-1, -1), CINZA_CLARO if j % 2 == 0 else BRANCO),
                ("TOPPADDING",    (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("LEFTPADDING",   (0, 0), (-1, -1), 10),
                ("LINEBELOW",     (0, 0), (-1, 0), 0.3, HexColor("#DDDDDD")),
            ]))
            story.append(dr)

        story.append(Paragraph(f"Fonte: {c['fonte']}", s["fonte"]))
        story.append(sp(0.35))

    story.append(PageBreak())


def pg_potencial_samu(s, story):
    story.append(hdr("Potencial Financeiro do SAMU Amigo", s))
    story.append(hr())
    story.append(sp(0.2))

    story.append(Paragraph(
        "Modelo de precificacao baseado em ticket medio de mercado e segmentacao municipal. "
        "Projecao conservadora com crescimento organico por indicacao e conformidade gradual:",
        s["body"]
    ))
    story.append(sp(0.3))

    # Modelo de precificacao
    preco_rows = [
        ["Porte do Municipio",     "Populacao",    "Preco Anual Proposto",  "Justificativa"],
        ["Grande",                 "> 500 mil",    "R$ 480.000 / ano",      "~30% abaixo do HXGN"],
        ["Medio-Grande",           "200-500 mil",  "R$ 240.000 / ano",      "Equivalente ao MedSave"],
        ["Medio (Santo Andre)",    "100-200 mil",  "R$ 144.000 / ano",      "60% menor que mercado"],
        ["Medio-Pequeno",          "50-100 mil",   "R$ 72.000 / ano",       "Sem concorrencia direta"],
        ["Pequeno",                "< 50 mil",     "R$ 36.000 / ano",       "e-SUS gratuito — IA como diferencial"],
    ]

    col_w = [CONTENT_W * p for p in [0.26, 0.16, 0.25, 0.33]]

    p_rows = []
    for i, row in enumerate(preco_rows):
        fn   = "Helvetica-Bold" if i == 0 else "Helvetica"
        i3_fn = "Helvetica-Bold"
        p_rows.append([
            Paragraph(row[0], ParagraphStyle("pr0", fontName="Helvetica-Bold" if i == 0 else "Helvetica-Bold",
                                              fontSize=9, textColor=BRANCO if i == 0 else AZUL_ESCURO,
                                              leading=13)),
            Paragraph(row[1], ParagraphStyle("pr1", fontName=fn, fontSize=9,
                                              textColor=BRANCO if i == 0 else CINZA_ESCURO,
                                              alignment=TA_CENTER, leading=13)),
            Paragraph(row[2], ParagraphStyle("pr2", fontName=i3_fn, fontSize=9,
                                              textColor=BRANCO if i == 0 else VERDE,
                                              alignment=TA_CENTER, leading=13)),
            Paragraph(row[3], ParagraphStyle("pr3", fontName=fn, fontSize=8,
                                              textColor=BRANCO if i == 0 else CINZA_MEDIO,
                                              leading=12)),
        ])

    pt = Table(p_rows, colWidths=col_w)
    pt.setStyle(TableStyle([
        ("BACKGROUND",     (0, 0), (-1, 0), AZUL_ESCURO),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
        ("GRID",           (0, 0), (-1, -1), 0.4, HexColor("#CCCCCC")),
        ("VALIGN",         (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",     (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING",  (0, 0), (-1, -1), 8),
        ("LEFTPADDING",    (0, 0), (-1, -1), 8),
    ]))
    story.append(pt)
    story.append(sp(0.4))

    # Premissas
    story.append(Paragraph("Premissas do Modelo", s["h2"]))
    premissas = [
        "Modelo SaaS: contrato anual com mensalidade fixa + suporte incluido",
        "Implementacao: taxa unica de R$ 30.000 - R$ 80.000 por central",
        "Complementar ao e-SUS SAMU (nao substitui — adiciona inteligencia)",
        "Crescimento via licitacao publica e indicacao entre municipios",
        "Expansao nacional a partir do caso de sucesso em Santo Andre",
        "Possibilidade de modelo freemium para municipios pequenos",
    ]
    for p in premissas:
        story.append(Paragraph(f"• {p}", ParagraphStyle("pm", fontName="Helvetica", fontSize=9,
                                                          textColor=CINZA_ESCURO, leading=14,
                                                          leftIndent=10, spaceAfter=3)))
    story.append(PageBreak())


def pg_projecao_receita(s, story):
    story.append(hdr("Projecao de Receita: SAMU Amigo (5 anos)", s, "proj_titulo"))
    story.append(HRFlowable(width="100%", thickness=2, color=VERDE,
                             spaceAfter=8, spaceBefore=4))
    story.append(sp(0.2))

    anos = [
        # Ano, municipios, mix_grandes, mix_medios, mix_pequenos, receita_impl, receita_total, desc
        ("Ano 1\n2025",  1,   0,  1,  0,  "R$ 50K",  "R$ 194.000",
         "Santo Andre (piloto). Validacao do produto. Case de sucesso."),
        ("Ano 2\n2026",  5,   0,  4,  1,  "R$ 200K", "R$ 846.000",
         "5 municipios regiao ABC + Grande SP. Primeiro contrato licitado."),
        ("Ano 3\n2027",  18,  2,  10, 6,  "R$ 480K", "R$ 3.066.000",
         "18 municipios. SP, MG, RS. Conformidade LGPD concluida. IA v2."),
        ("Ano 4\n2028",  45,  5,  25, 15, "R$ 960K", "R$ 7.476.000",
         "45 municipios. Acordo com estado de SP. Modulo Records lancado."),
        ("Ano 5\n2029",  100, 10, 55, 35, "R$ 1,5M", "R$ 16.560.000",
         "100 municipios. Presenca em 10 estados. Serie A prevista."),
    ]

    col_w = [CONTENT_W * p for p in [0.13, 0.10, 0.10, 0.10, 0.10, 0.10, 0.15, 0.22]]

    header_row = [
        Paragraph(c, ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=8,
                                     textColor=BRANCO, alignment=TA_CENTER, leading=12))
        for c in ["Periodo", "Municipios", "Grandes\n(480K)", "Medios\n(192K)", "Pequenos\n(60K)",
                  "Impl.", "Receita\nAnual", "Marco Estrategico"]
    ]

    rows = [header_row]
    for ano, mun, g, m, p2, impl, receita, desc in anos:
        rows.append([
            Paragraph(ano.replace("\n", "\n"), ParagraphStyle("a", fontName="Helvetica-Bold",
                                                               fontSize=9, textColor=VERDE_CLARO,
                                                               alignment=TA_CENTER, leading=13)),
            Paragraph(str(mun), ParagraphStyle("m", fontName="Helvetica-Bold", fontSize=11,
                                                textColor=DOURADO, alignment=TA_CENTER, leading=15)),
            Paragraph(str(g) if g else "—", ParagraphStyle("g", fontName="Helvetica", fontSize=9,
                                                            textColor=CINZA_ESCURO, alignment=TA_CENTER,
                                                            leading=13)),
            Paragraph(str(m) if m else "—", ParagraphStyle("me", fontName="Helvetica", fontSize=9,
                                                            textColor=CINZA_ESCURO, alignment=TA_CENTER,
                                                            leading=13)),
            Paragraph(str(p2) if p2 else "—", ParagraphStyle("p3", fontName="Helvetica", fontSize=9,
                                                              textColor=CINZA_ESCURO, alignment=TA_CENTER,
                                                              leading=13)),
            Paragraph(impl, ParagraphStyle("im", fontName="Helvetica", fontSize=8,
                                            textColor=CINZA_MEDIO, alignment=TA_CENTER, leading=12)),
            Paragraph(receita, ParagraphStyle("r", fontName="Helvetica-Bold", fontSize=10,
                                              textColor=VERDE_NEON, alignment=TA_CENTER, leading=14)),
            Paragraph(desc, ParagraphStyle("d", fontName="Helvetica", fontSize=8,
                                            textColor=CINZA_ESCURO, leading=12)),
        ])

    t = Table(rows, colWidths=col_w)
    t.setStyle(TableStyle([
        ("BACKGROUND",     (0, 0), (-1, 0), HexColor("#0D2240")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#0F1F35"), HexColor("#0A1628")]),
        ("TEXTCOLOR",      (0, 1), (-1, -1), BRANCO),
        ("GRID",           (0, 0), (-1, -1), 0.4, HexColor("#1A3A6B")),
        ("VALIGN",         (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",     (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING",  (0, 0), (-1, -1), 8),
        ("LEFTPADDING",    (0, 0), (-1, -1), 6),
        # Destaque coluna receita
        ("BACKGROUND",     (6, 0), (6, -1), HexColor("#0D2E0D")),
        ("LINEAFTER",      (5, 0), (5, -1), 1, VERDE),
    ]))
    story.append(t)
    story.append(sp(0.4))

    # Totais acumulados
    totais = [
        ["Receita Acumulada 5 anos", "Receita Ano 5", "Projecao Ano 10"],
        ["R$ 28.142.000",            "R$ 16.560.000", "R$ 70 - 100 Mi"],
    ]

    tot_rows = [
        [Paragraph(c, ParagraphStyle("thl", fontName="Helvetica-Bold", fontSize=9,
                                     textColor=HexColor("#AAAAAA"), alignment=TA_CENTER, leading=13))
         for c in totais[0]],
        [Paragraph(v, ParagraphStyle("tvl", fontName="Helvetica-Bold", fontSize=18,
                                     textColor=DOURADO, alignment=TA_CENTER, leading=22))
         for v in totais[1]],
    ]
    tt = Table(tot_rows, colWidths=[CONTENT_W / 3] * 3,
               rowHeights=[0.8 * cm, 1.6 * cm])
    tt.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), HexColor("#0D2240")),
        ("GRID",          (0, 0), (-1, -1), 1, AZUL_MEDIO),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("LINEABOVE",     (0, 0), (-1, 0), 2, VERDE),
    ]))
    story.append(tt)
    story.append(sp(0.2))
    story.append(Paragraph(
        "Projecao conservadora. Cenario otimista: R$ 150 Mi em ano 10 com expansao para outros servicos de urgencia.",
        s["nota"]
    ))
    story.append(PageBreak())


def pg_comparativo_financeiro(s, story):
    story.append(hdr("Comparativo Financeiro: Os 4 Sistemas", s))
    story.append(hr())
    story.append(sp(0.3))

    dados = [
        ["Metrica",                    "SAMU Amigo\n(projecao)",  "MedSave\n(estimativa)",
                                        "HXGN OnCall\n(BR estimado)", "e-SUS SAMU\n(referencia)"],
        ["Faturamento atual BR",        "R$ 0\n(pre-receita)",    "R$ 15-30 Mi",
                                         "R$ 80-150 Mi",              "R$ 0 (Gov.)"],
        ["Faturamento ano 1",           "R$ 194 Mil",             "R$ 15-30 Mi",
                                         "R$ 80-150 Mi",              "R$ 0"],
        ["Faturamento ano 5",           "R$ 16,5 Mi",             "R$ 40-60 Mi",
                                         "R$ 150-200 Mi",             "R$ 0"],
        ["Faturamento potencial (BR)",  "R$ 70-100 Mi",           "R$ 80-120 Mi",
                                         "R$ 200-300 Mi",             "R$ 0"],
        ["Ticket medio por central",    "R$ 144-480 K/ano",       "R$ 180-400 K/ano",
                                         "R$ 2-8 Mi/ano",             "R$ 0"],
        ["Municipios alcancaveis BR",   "4.143 (todos)",          "~500 (medios/grandes)",
                                         "~50 (grandes)",             "4.143 (mandato)"],
        ["Custo de aquisicao cliente",  "Baixo (indicacao)",      "Medio (vendas diretas)",
                                         "Alto (enterprise sales)",   "Zero (governamental)"],
        ["Margem estimada",             "70-80% (SaaS)",          "50-65%",
                                         "30-45%",                    "N/A"],
        ["Barreira de entrada",         "Baixa",                  "Media",
                                         "Alta",                      "Zero (obrigatorio)"],
    ]

    col_w = [CONTENT_W * p for p in [0.28, 0.18, 0.18, 0.20, 0.16]]

    cores_col = [AZUL_ESCURO, SAMU_COR, MEDSAVE_COR, HEXAGON_COR, ESUS_COR]

    rows = []
    for i, row in enumerate(dados):
        if i == 0:
            rows.append([
                Paragraph(row[j], ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9,
                                                  textColor=BRANCO, alignment=TA_CENTER, leading=13))
                for j in range(5)
            ])
        else:
            rows.append([
                Paragraph(row[0], ParagraphStyle("d", fontName="Helvetica-Bold", fontSize=9,
                                                  textColor=AZUL_ESCURO, leading=13)),
                Paragraph(row[1].replace("\n", "<br/>"),
                          ParagraphStyle("s", fontName="Helvetica-Bold", fontSize=9,
                                         textColor=SAMU_COR, alignment=TA_CENTER, leading=13)),
                Paragraph(row[2].replace("\n", "<br/>"),
                          ParagraphStyle("m", fontName="Helvetica", fontSize=9,
                                         textColor=CINZA_ESCURO, alignment=TA_CENTER, leading=13)),
                Paragraph(row[3].replace("\n", "<br/>"),
                          ParagraphStyle("h", fontName="Helvetica", fontSize=9,
                                         textColor=CINZA_ESCURO, alignment=TA_CENTER, leading=13)),
                Paragraph(row[4].replace("\n", "<br/>"),
                          ParagraphStyle("e", fontName="Helvetica", fontSize=9,
                                         textColor=CINZA_MEDIO, alignment=TA_CENTER, leading=13)),
            ])

    t = Table(rows, colWidths=col_w)
    t.setStyle(TableStyle([
        ("BACKGROUND",     (0, 0), (-1, 0), AZUL_ESCURO),
        ("BACKGROUND",     (1, 0), (1, 0), SAMU_COR),
        ("BACKGROUND",     (2, 0), (2, 0), MEDSAVE_COR),
        ("BACKGROUND",     (3, 0), (3, 0), HEXAGON_COR),
        ("BACKGROUND",     (4, 0), (4, 0), ESUS_COR),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
        ("GRID",           (0, 0), (-1, -1), 0.4, HexColor("#CCCCCC")),
        ("VALIGN",         (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",     (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING",  (0, 0), (-1, -1), 8),
        ("LEFTPADDING",    (0, 0), (-1, -1), 7),
        # Destaque coluna SAMU Amigo
        ("BACKGROUND",     (1, 1), (1, -1), HexColor("#FFF5F5")),
        ("LINEAFTER",      (1, 0), (1, -1), 1.5, SAMU_COR),
        ("LINEBEFORE",     (1, 0), (1, -1), 1.5, SAMU_COR),
    ]))
    story.append(t)
    story.append(sp(0.3))
    story.append(Paragraph(
        "Dados Hexagon: Hexagon Year-End Report 2024 | MedSave e SAMU Amigo: estimativas de mercado | "
        "Contrato referencia SP: Portal Transparencia SP 2023 (R$ 5,87M/ano)",
        s["nota"]
    ))
    story.append(PageBreak())


def pg_oportunidade_unica(s, story):
    story.append(hdr("A Oportunidade Unica do SAMU Amigo", s))
    story.append(hr())
    story.append(sp(0.3))

    oportunidades = [
        (SAMU_COR,    "Mercado Sub-Atendido: R$ 365 Mi inexplorados",
         "Municipios pequenos e medio-pequenos (< 100 mil hab.) representam 87% do total de "
         "municipios com SAMU. O MedSave e HXGN nao chegam nesse segmento. O e-SUS nao tem IA. "
         "O SAMU Amigo pode ser o unico produto com IA clinica acessivel para esses municipios."),
        (VERDE,       "Modelo SaaS com Margens de 70-80%",
         "Software como servico com custo marginal baixissimo por novo cliente. "
         "Enquanto HXGN opera com margens de 30-45% por conta de servicos profissionais e infraestrutura, "
         "o SAMU Amigo pode operar com margens tipicas de SaaS medico: 70-80%."),
        (DOURADO,     "Santo Andre como Trampolim Nacional",
         "Um caso documentado de reducao de tempo de resposta em Santo Andre vale mais que "
         "qualquer campanha de marketing. Municipios brasileiros se inspiram uns nos outros. "
         "O primeiro contrato licitado e a porta para os 4.143 municipios seguintes."),
        (HEXAGON_COR, "Complementaridade com e-SUS = Sem Resistencia Politica",
         "Ao ser complementar ao e-SUS SAMU (e nao substituto), o SAMU Amigo elimina a "
         "principal barreira de adocao: resistencia politica. O gestor nao precisa abandonar "
         "o sistema federal — precisa apenas adicionar inteligencia sobre ele."),
        (LARANJA,     "IA Clinica como Vantagem Defensavel",
         "A ISA nao e apenas um diferencial de marketing — e uma barreira tecnologica real. "
         "MedSave levaria 2-3 anos para desenvolver IA clinica equivalente. HXGN nao tem "
         "incentivo para focar em SAMU brasileiro. e-SUS nunca tera IA pelo ciclo governamental."),
    ]

    for cor, titulo, desc in oportunidades:
        bloco = Table([
            [Paragraph(titulo, ParagraphStyle("ot", fontName="Helvetica-Bold", fontSize=11,
                                               textColor=BRANCO, leading=15))],
            [Paragraph(desc,   ParagraphStyle("od", fontName="Helvetica", fontSize=9,
                                               textColor=BRANCO if cor in [SAMU_COR, VERDE] else CINZA_ESCURO,
                                               leading=14))],
        ], colWidths=[CONTENT_W])

        bg_desc = HexColor("#F8F9FA") if cor not in [SAMU_COR, VERDE] else HexColor("#5D1A1A") if cor == SAMU_COR else HexColor("#145214")

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


def pg_conclusao_financeira(s, story):
    story.append(hdr("Conclusao Financeira", s))
    story.append(hr())
    story.append(sp(0.4))

    # Resumo em numeros
    numeros = [
        ("R$ 560 Mi",   "Mercado total\nBrasil / ano"),
        ("R$ 16,5 Mi",  "Receita SAMU Amigo\nno ano 5"),
        ("70-80%",      "Margem estimada\nmodelo SaaS"),
        ("4.143",       "Municipios\nalcancaveis"),
    ]

    num_cells = []
    for val, label in numeros:
        cell = Table([
            [Paragraph(val, ParagraphStyle("nv", fontName="Helvetica-Bold", fontSize=17,
                                            textColor=DOURADO, alignment=TA_CENTER, leading=22))],
            [Paragraph(label.replace("\n", "<br/>"),
                       ParagraphStyle("nl", fontName="Helvetica", fontSize=8,
                                      textColor=HexColor("#AAAAAA"), alignment=TA_CENTER, leading=12))],
        ], colWidths=[CONTENT_W / 4 - 0.1 * cm])
        cell.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (-1, -1), HexColor("#0D2240")),
            ("TOPPADDING",    (0, 0), (-1, -1), 12),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ]))
        num_cells.append(cell)

    num_outer = Table([num_cells], colWidths=[CONTENT_W / 4] * 4)
    num_outer.setStyle(TableStyle([
        ("GRID",   (0, 0), (-1, -1), 1, AZUL_MEDIO),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(num_outer)
    story.append(sp(0.5))

    # Tabela de posicionamento final
    final_comp = [
        ["Sistema",       "Faturamento BR Atual", "Potencial BR",    "Vantagem Principal"],
        ["SAMU Amigo",    "Pre-receita",           "R$ 70-100 Mi",   "IA clinica unica + custo baixo"],
        ["MedSave SEMS",  "R$ 15-30 Mi/ano",       "R$ 80-120 Mi",   "Compliance MS consolidado"],
        ["HXGN OnCall",   "R$ 80-150 Mi/ano",      "R$ 200-300 Mi",  "Escala global + GIS enterprise"],
        ["e-SUS SAMU",    "R$ 0 (governamental)",  "R$ 0 (estado)",  "Mandato federal obrigatorio"],
    ]

    col_w = [CONTENT_W * p for p in [0.22, 0.22, 0.20, 0.36]]

    fc_rows = []
    for i, row in enumerate(final_comp):
        cores_bg = [None, SAMU_COR, MEDSAVE_COR, HEXAGON_COR, ESUS_COR]
        fn = "Helvetica-Bold"
        if i == 0:
            fc_rows.append([
                Paragraph(c, ParagraphStyle("fth", fontName=fn, fontSize=10,
                                             textColor=BRANCO, alignment=TA_CENTER, leading=13))
                for c in row
            ])
        else:
            fc_rows.append([
                Paragraph(row[0], ParagraphStyle("fn0", fontName=fn, fontSize=10,
                                                  textColor=cores_bg[i], leading=14)),
                Paragraph(row[1], ParagraphStyle("fn1", fontName="Helvetica", fontSize=9,
                                                  textColor=CINZA_ESCURO, alignment=TA_CENTER, leading=13)),
                Paragraph(row[2], ParagraphStyle("fn2", fontName=fn, fontSize=9,
                                                  textColor=VERDE if i == 1 else CINZA_ESCURO,
                                                  alignment=TA_CENTER, leading=13)),
                Paragraph(row[3], ParagraphStyle("fn3", fontName="Helvetica", fontSize=9,
                                                  textColor=CINZA_ESCURO, leading=13)),
            ])

    fct = Table(fc_rows, colWidths=col_w)
    fct.setStyle(TableStyle([
        ("BACKGROUND",     (0, 0), (-1, 0), AZUL_ESCURO),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#FFF5F5"), CINZA_CLARO, BRANCO, CINZA_CLARO]),
        ("GRID",           (0, 0), (-1, -1), 0.5, HexColor("#CCCCCC")),
        ("VALIGN",         (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",     (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING",  (0, 0), (-1, -1), 10),
        ("LEFTPADDING",    (0, 0), (-1, -1), 10),
        ("LINEABOVE",      (0, 1), (-1, 1), 2, SAMU_COR),
        ("LINEBELOW",      (0, 1), (-1, 1), 1, SAMU_COR),
    ]))
    story.append(fct)
    story.append(sp(0.5))

    msg = Table([[Paragraph(
        '"O mercado ja existe. O dinheiro ja esta la.<br/>'
        'O SAMU Amigo e a unica solucao que ainda nao chegou — mas vai."',
        ParagraphStyle("msg", fontName="Helvetica-BoldOblique", fontSize=14,
                       textColor=DOURADO, alignment=TA_CENTER, leading=20)
    )]], colWidths=[CONTENT_W])
    msg.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), AZUL_ESCURO),
        ("TOPPADDING",    (0, 0), (-1, -1), 20),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 20),
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

    pg_secao("Tamanho do Mercado", "O mercado brasileiro de software para SAMU em numeros", s, story)
    pg_tamanho_mercado(s, story)

    pg_secao("Faturamento dos Concorrentes", "O que cada player fatura hoje no Brasil", s, story)
    pg_faturamento_concorrentes(s, story)

    pg_secao("Potencial SAMU Amigo", "Modelo de precificacao e premissas financeiras", s, story)
    pg_potencial_samu(s, story)

    pg_secao("Projecao de Receita", "SAMU Amigo: de Santo Andre ao Brasil", s, story)
    pg_projecao_receita(s, story)

    pg_secao("Comparativo Financeiro", "Os 4 sistemas frente a frente nos numeros", s, story)
    pg_comparativo_financeiro(s, story)

    pg_secao("A Oportunidade", "Por que agora e por que o SAMU Amigo", s, story)
    pg_oportunidade_unica(s, story)

    pg_secao("Conclusao", "Os numeros que importam para Santo Andre", s, story)
    pg_conclusao_financeira(s, story)

    doc = SimpleDocTemplate(
        output, pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN,  bottomMargin=MARGIN,
    )

    PROJECAO_PAGES = {9, 10, 11}

    def on_page(c, doc):
        n = doc.page
        if n == 1:
            BG("capa")(c, doc)
        elif n % 2 == 0:
            BG("secao")(c, doc)
        elif n in PROJECAO_PAGES:
            BG("projecao")(c, doc)
        else:
            BG("normal")(c, doc)

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f"PDF gerado: {output}")


if __name__ == "__main__":
    gerar("samu_amigo_potencial_financeiro.pdf")

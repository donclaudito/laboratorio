"""
SAMU Amigo — Commercial & Financial Potential (USD version)
Exchange rate used: R$ 5.80 = USD 1.00 (April 2025)
"""
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
FLAG_BLUE      = HexColor("#002868")
FLAG_RED       = HexColor("#BF0A30")

PAGE_W, PAGE_H = A4
MARGIN         = 2 * cm
CONTENT_W      = PAGE_W - 2 * MARGIN

# Exchange rate note
FX_NOTE = "Exchange rate: R$ 5.80 = USD 1.00 (April 2025)"


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
            for i in range(4):
                c.setFillColor(HexColor("#1A3A6B"))
                c.rect(0, i * h / 4, w, h / 4, fill=1, stroke=0)
            # Faixa superior — cores da bandeira americana
            c.setFillColor(FLAG_RED)
            c.rect(0, h - 0.6 * cm, w, 0.6 * cm, fill=1, stroke=0)
            # Faixa inferior
            c.setFillColor(FLAG_RED)
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
            # Marca dagua $
            c.setFillColor(HexColor("#FFFFFF04"))
            c.setFont("Helvetica-Bold", 200)
            c.drawCentredString(w / 2, h / 2 - 80, "$")

        elif self.tipo == "secao":
            c.setFillColor(FLAG_BLUE)
            c.rect(0, 0, w, h, fill=1, stroke=0)
            c.setFillColor(FLAG_RED)
            c.rect(0, 0, 0.7 * cm, h, fill=1, stroke=0)
            c.setFillColor(HexColor("#FFFFFF05"))
            c.setFont("Helvetica-Bold", 70)
            c.drawCentredString(w / 2, h / 2 - 25, "MARKET")

        elif self.tipo == "projecao":
            c.setFillColor(PRETO)
            c.rect(0, 0, w, h, fill=1, stroke=0)
            c.setFillColor(VERDE)
            c.rect(0, 0, 0.7 * cm, h, fill=1, stroke=0)
            c.setFillColor(HexColor("#27AE6008"))
            c.rect(0, 0, w, h * 0.35, fill=1, stroke=0)

        else:
            c.setFillColor(BRANCO)
            c.rect(0, 0, w, h, fill=1, stroke=0)
            # Header
            c.setFillColor(FLAG_BLUE)
            c.rect(0, h - 1.8 * cm, w, 1.8 * cm, fill=1, stroke=0)
            c.setFillColor(FLAG_RED)
            c.rect(0, h - 1.8 * cm, 0.45 * cm, 1.8 * cm, fill=1, stroke=0)
            c.setFillColor(BRANCO)
            c.setFont("Helvetica-Bold", 9)
            c.drawString(1.2 * cm, h - 1.2 * cm, "SAMU AMIGO  |  Commercial & Financial Potential — USD")
            c.setFont("Helvetica", 9)
            c.drawRightString(w - 1.2 * cm, h - 1.2 * cm, "Brazilian Market · 2025")
            # Footer
            c.setFillColor(FLAG_BLUE)
            c.rect(0, 0, w, 1.0 * cm, fill=1, stroke=0)
            c.setFillColor(FLAG_RED)
            c.rect(0, 0, w, 0.15 * cm, fill=1, stroke=0)
            c.setFillColor(HexColor("#AAAAAA"))
            c.setFont("Helvetica", 7)
            c.drawCentredString(w / 2, 0.35 * cm,
                f"Page {doc.page}  |  {FX_NOTE}  |  Market data and projections based on public contracts")

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
        "fonte":        ParagraphStyle("fo", fontName="Helvetica-Oblique", fontSize=7,
                                        textColor=CINZA_MEDIO, leading=10, alignment=TA_LEFT),
    }


def sp(h):  return Spacer(1, h * cm)
def hr(cor=FLAG_RED, t=2):
    return HRFlowable(width="100%", thickness=t, color=cor, spaceAfter=8, spaceBefore=4)
def hdr(txt, s, key="slide_titulo"):
    return Paragraph(txt, s[key])


# =====================================================================
# PAGINAS
# =====================================================================

def pg_capa(s, story):
    story.append(sp(2.5))
    story.append(Paragraph("COMMERCIAL & FINANCIAL ANALYSIS", s["capa_label"]))
    story.append(sp(0.3))
    story.append(Paragraph("SAMU AMIGO", s["capa_titulo"]))
    story.append(sp(0.2))
    story.append(Paragraph("vs. Three Competitors", ParagraphStyle(
        "cs2", fontName="Helvetica", fontSize=20,
        textColor=HexColor("#7FB3D3"), alignment=TA_CENTER, leading=26
    )))
    story.append(sp(0.4))
    story.append(HRFlowable(width="55%", thickness=3, color=DOURADO,
                             spaceAfter=10, spaceBefore=4, hAlign="CENTER"))
    story.append(sp(0.2))
    story.append(Paragraph(
        "Annual Revenue  •  Brazilian Market Size  •  Revenue Potential (USD)",
        s["capa_sub"]
    ))
    story.append(sp(0.4))

    metricas = [
        ["4,143\nSAMU Municipalities", "USD 96.6 M\nTotal Brazilian Market", "USD 414 M\nDigital Health Invest. 2025"],
    ]
    mt = Table([[
        Paragraph(v, ParagraphStyle("mv", fontName="Helvetica-Bold", fontSize=11,
                                     textColor=DOURADO, alignment=TA_CENTER, leading=16))
        for v in metricas[0]
    ]], colWidths=[CONTENT_W / 3] * 3)
    mt.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), HexColor("#0D2240")),
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 14),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
        ("GRID",          (0, 0), (-1, -1), 1, AZUL_MEDIO),
    ]))
    story.append(mt)
    story.append(sp(0.8))
    story.append(Paragraph(
        f"{FX_NOTE}  |  Sources: Ministry of Health Brazil, SP Transparency Portal, Hexagon Annual Report 2024",
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
    story.append(hdr("Brazilian SAMU Software Market Size (USD)", s))
    story.append(hr())
    story.append(sp(0.3))

    story.append(Paragraph(
        "Calculation base: 4,143 municipalities covered by SAMU 192, segmented by size and average "
        "annual contract value. Reference: Sao Paulo public contract USD 1.01M/year "
        "(SP Transparency Portal, 2023 — R$ 5.87M / 5.80).",
        s["body"]
    ))
    story.append(sp(0.3))

    segmentos = [
        ["Segment",       "Population",   "Municipalities", "Avg. Contract/Year", "TAM Segment"],
        ["Large",         "> 500K",        "~50",           "USD 258,620",        "USD 12,931,000"],
        ["Med-Large",     "200K-500K",     "~150",          "USD 103,448",        "USD 15,517,000"],
        ["Medium",        "100K-200K",     "~300",          "USD 60,345",         "USD 18,103,000"],
        ["Med-Small",     "50K-100K",      "~600",          "USD 31,034",         "USD 18,620,000"],
        ["Small",         "< 50K",         "~3,043",        "USD 10,345",         "USD 31,479,000"],
        ["TOTAL MARKET",  "—",             "4,143",         "—",                  "USD 96,650,000"],
    ]

    col_w = [CONTENT_W * p for p in [0.20, 0.17, 0.14, 0.23, 0.26]]

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

    # KPIs
    kpis = [
        ("USD 96.6 M", "TAM\nTotal Market"),
        ("USD 33.6 M", "SAM\nLarge & Medium"),
        ("USD 8.6 M",  "SOM\nSAMU Amigo initial target"),
    ]

    real_kpi = []
    for v, l in kpis:
        cell = Table([
            [Paragraph(v, ParagraphStyle("kv", fontName="Helvetica-Bold", fontSize=16,
                                          textColor=DOURADO, alignment=TA_CENTER, leading=22))],
            [Paragraph(l.replace("\n", "<br/>"), ParagraphStyle("kl", fontName="Helvetica",
                                                                  fontSize=9,
                                                                  textColor=HexColor("#AAAAAA"),
                                                                  alignment=TA_CENTER, leading=13))],
        ], colWidths=[CONTENT_W / 3 - 0.1 * cm])
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
        "SOM = Serviceable Obtainable Market (realistic target year 1-3)",
        s["nota"]
    ))
    story.append(PageBreak())


def pg_faturamento_concorrentes(s, story):
    story.append(hdr("Competitors Annual Revenue (USD)", s))
    story.append(hr())
    story.append(sp(0.3))

    story.append(Paragraph(
        "Estimates based on public data, annual reports, and available contracts. "
        "All values converted at R$ 5.80 = USD 1.00:",
        s["body"]
    ))
    story.append(sp(0.3))

    concorrentes = [
        {
            "nome":    "MedSave SEMS SAMU",
            "cor":     MEDSAVE_COR,
            "tipo":    "Brazilian company — commercial SaaS product for SAMU",
            "fat_br":  "USD 2.6 M - 5.2 M / year",
            "clientes":"~50-100 active SAMU regulation centers",
            "ticket":  "USD 31,000 - USD 69,000 / center / year",
            "modelo":  "License + support + updates",
            "crescim": "~15-20% p.a. (emerging market — HealthTech BR)",
            "fraqueza":"No clinical AI. Static product. No international scalability.",
            "fonte":   "Market estimate based on company profile, size and average BR market ticket",
        },
        {
            "nome":    "HXGN OnCall (Hexagon)",
            "cor":     HEXAGON_COR,
            "tipo":    "Swedish multinational — Safety & Infrastructure division",
            "fat_br":  "USD 13.8 M - 25.9 M / year (Brazil estimate)",
            "clientes":"~20-40 large public contracts in Brazil",
            "ticket":  "USD 345,000 - USD 1,379,000 / contract / year",
            "modelo":  "SaaS + On-premises + professional services",
            "crescim": "Hexagon SI global: EUR 140.8M (Q4/2024). Brazil ~9% of global revenue",
            "fraqueza":"Prohibitive cost for mid-size municipalities. Generic. No SAMU BR focus.",
            "fonte":   "Hexagon Year-End Report 2024 (hexagon.com). Brazil estimate proportional.",
        },
        {
            "nome":    "e-SUS SAMU (DATASUS)",
            "cor":     ESUS_COR,
            "tipo":    "Government system — state cost, no commercial revenue",
            "fat_br":  "USD 0 (free of charge)",
            "clientes":"~4,143 municipalities (federal mandate)",
            "ticket":  "USD 0 — distributed by the Ministry of Health",
            "modelo":  "Government open-source — maintenance cost ~USD 2.6-4.3M/year (MoH)",
            "crescim": "N/A — state system",
            "fraqueza":"Zero revenue. Zero innovation. Legacy technology. Updates take years.",
            "fonte":   "DATASUS, datasus.saude.gov.br/e-sus-samu. Maintenance cost estimated.",
        },
    ]

    for c in concorrentes:
        h_row = Table([[
            Paragraph(c["nome"], ParagraphStyle("cn", fontName="Helvetica-Bold", fontSize=13,
                                                 textColor=BRANCO, leading=17)),
            Paragraph(c["fat_br"], ParagraphStyle("cf", fontName="Helvetica-Bold", fontSize=13,
                                                    textColor=AMARELO, alignment=TA_RIGHT, leading=17)),
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
            ("Type",            c["tipo"]),
            ("Active clients",  c["clientes"]),
            ("Average ticket",  c["ticket"]),
            ("Business model",  c["modelo"]),
            ("Growth",          c["crescim"]),
            ("Key weakness",    c["fraqueza"]),
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

        story.append(Paragraph(f"Source: {c['fonte']}", s["fonte"]))
        story.append(sp(0.35))

    story.append(PageBreak())


def pg_potencial_samu(s, story):
    story.append(hdr("SAMU Amigo — Pricing Model (USD)", s))
    story.append(hr())
    story.append(sp(0.2))

    story.append(Paragraph(
        "Pricing model based on market average ticket and municipal segmentation. "
        "Positioned 30-60% below competitors to accelerate market penetration:",
        s["body"]
    ))
    story.append(sp(0.3))

    preco_rows = [
        ["Municipality Size",        "Population",    "Proposed Annual Price", "Rationale"],
        ["Large",                    "> 500K",         "USD 82,760 / year",    "~30% below HXGN OnCall"],
        ["Med-Large",                "200K-500K",      "USD 41,380 / year",    "Equivalent to MedSave"],
        ["Medium (Santo Andre)",     "100K-200K",      "USD 24,830 / year",    "60% below market avg."],
        ["Med-Small",                "50K-100K",       "USD 12,415 / year",    "No direct competition"],
        ["Small",                    "< 50K",          "USD 6,207 / year",     "e-SUS is free — AI as differentiator"],
    ]

    col_w = [CONTENT_W * p for p in [0.26, 0.16, 0.25, 0.33]]

    p_rows = []
    for i, row in enumerate(preco_rows):
        fn    = "Helvetica-Bold"
        p_rows.append([
            Paragraph(row[0], ParagraphStyle("pr0", fontName=fn, fontSize=9,
                                              textColor=BRANCO if i == 0 else AZUL_ESCURO, leading=13)),
            Paragraph(row[1], ParagraphStyle("pr1", fontName=fn if i == 0 else "Helvetica", fontSize=9,
                                              textColor=BRANCO if i == 0 else CINZA_ESCURO,
                                              alignment=TA_CENTER, leading=13)),
            Paragraph(row[2], ParagraphStyle("pr2", fontName=fn, fontSize=9,
                                              textColor=BRANCO if i == 0 else VERDE,
                                              alignment=TA_CENTER, leading=13)),
            Paragraph(row[3], ParagraphStyle("pr3", fontName="Helvetica" if i > 0 else fn,
                                              fontSize=8,
                                              textColor=BRANCO if i == 0 else CINZA_MEDIO, leading=12)),
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

    story.append(Paragraph("Business Model Assumptions", s["h2"]))
    premissas = [
        "SaaS model: annual contract with fixed monthly fee + support included",
        "Implementation: one-time fee of USD 5,172 - USD 13,793 per regulation center",
        "Complementary to e-SUS SAMU (does not replace — adds intelligence)",
        "Growth through public bidding (licitacao) and municipal referrals",
        "National expansion from the Santo Andre success case",
        "Potential freemium model for small municipalities (< 50K inhabitants)",
        "Revenue from ISA AI upgrades and premium analytics modules",
    ]
    for p in premissas:
        story.append(Paragraph(f"• {p}", ParagraphStyle("pm", fontName="Helvetica", fontSize=9,
                                                          textColor=CINZA_ESCURO, leading=14,
                                                          leftIndent=10, spaceAfter=3)))
    story.append(PageBreak())


def pg_projecao_receita(s, story):
    story.append(hdr("Revenue Projection: SAMU Amigo — 5 Years (USD)", s, "proj_titulo"))
    story.append(HRFlowable(width="100%", thickness=2, color=VERDE,
                             spaceAfter=8, spaceBefore=4))
    story.append(sp(0.2))

    story.append(Paragraph(
        "Conservative projection. Organic growth driven by public bidding and peer-to-peer "
        "referrals between municipalities. FX: R$ 5.80 = USD 1.00.",
        s["body"]
    ))
    story.append(sp(0.3))

    anos = [
        ("Year 1\n2025",  1,   0,  1,  0,  "USD 8.6K",  "USD 33,448",
         "Santo Andre (pilot). Product validation. First success case."),
        ("Year 2\n2026",  5,   0,  4,  1,  "USD 34.5K", "USD 145,862",
         "5 municipalities — ABC region + Greater SP. First public bid won."),
        ("Year 3\n2027",  18,  2,  10, 6,  "USD 82.8K", "USD 528,620",
         "18 municipalities — SP, MG, RS. LGPD compliance done. ISA v2."),
        ("Year 4\n2028",  45,  5,  25, 15, "USD 165.5K","USD 1,289,000",
         "45 municipalities. State of SP agreement. Records module launched."),
        ("Year 5\n2029",  100, 10, 55, 35, "USD 258.6K","USD 2,855,172",
         "100 municipalities. 10 states. Series A funding round."),
    ]

    col_w = [CONTENT_W * p for p in [0.13, 0.10, 0.10, 0.10, 0.10, 0.11, 0.14, 0.22]]

    header_row = [
        Paragraph(c, ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=8,
                                     textColor=BRANCO, alignment=TA_CENTER, leading=12))
        for c in ["Period", "Cities", "Large\n(83K)", "Medium\n(25K)", "Small\n(6.2K)",
                  "Impl.", "Annual\nRevenue", "Strategic Milestone"]
    ]

    rows = [header_row]
    for ano, mun, g, m, p2, impl, receita, desc in anos:
        rows.append([
            Paragraph(ano, ParagraphStyle("a", fontName="Helvetica-Bold", fontSize=9,
                                           textColor=VERDE_CLARO, alignment=TA_CENTER, leading=13)),
            Paragraph(str(mun), ParagraphStyle("m", fontName="Helvetica-Bold", fontSize=11,
                                                textColor=DOURADO, alignment=TA_CENTER, leading=15)),
            Paragraph(str(g) if g else "—", ParagraphStyle("g", fontName="Helvetica", fontSize=9,
                                                             textColor=CINZA_ESCURO,
                                                             alignment=TA_CENTER, leading=13)),
            Paragraph(str(m) if m else "—", ParagraphStyle("me", fontName="Helvetica", fontSize=9,
                                                             textColor=CINZA_ESCURO,
                                                             alignment=TA_CENTER, leading=13)),
            Paragraph(str(p2) if p2 else "—", ParagraphStyle("p3", fontName="Helvetica", fontSize=9,
                                                               textColor=CINZA_ESCURO,
                                                               alignment=TA_CENTER, leading=13)),
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
        ("BACKGROUND",     (6, 0), (6, -1), HexColor("#0D2E0D")),
        ("LINEAFTER",      (5, 0), (5, -1), 1, VERDE),
    ]))
    story.append(t)
    story.append(sp(0.4))

    totais_data = [
        ["5-Year Cumul. Revenue", "Year 5 Revenue",  "Year 10 Projection"],
        ["USD 4,852,102",         "USD 2,855,172",   "USD 12 M - 17.2 M"],
    ]
    tot_rows = [
        [Paragraph(c, ParagraphStyle("thl", fontName="Helvetica-Bold", fontSize=9,
                                     textColor=HexColor("#AAAAAA"), alignment=TA_CENTER, leading=13))
         for c in totais_data[0]],
        [Paragraph(v, ParagraphStyle("tvl", fontName="Helvetica-Bold", fontSize=18,
                                     textColor=DOURADO, alignment=TA_CENTER, leading=22))
         for v in totais_data[1]],
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
        "Conservative scenario. Optimistic scenario: USD 25.9M in year 10 with expansion to other emergency services.",
        s["nota"]
    ))
    story.append(PageBreak())


def pg_comparativo_financeiro(s, story):
    story.append(hdr("Financial Comparison: All 4 Systems (USD)", s))
    story.append(hr())
    story.append(sp(0.3))

    dados = [
        ["Metric",                      "SAMU Amigo\n(projection)",  "MedSave\n(estimate)",
                                         "HXGN OnCall\n(Brazil est.)", "e-SUS SAMU\n(reference)"],
        ["Current BR revenue",           "USD 0\n(pre-revenue)",      "USD 2.6-5.2 M",
                                          "USD 13.8-25.9 M",            "USD 0 (Gov.)"],
        ["Year 1 revenue",               "USD 33.4K",                 "USD 2.6-5.2 M",
                                          "USD 13.8-25.9 M",            "USD 0"],
        ["Year 5 revenue",               "USD 2.86 M",                "USD 6.9-10.3 M",
                                          "USD 25.9-34.5 M",            "USD 0"],
        ["Revenue potential (Brazil)",   "USD 12-17 M",               "USD 13.8-20.7 M",
                                          "USD 34.5-51.7 M",            "USD 0"],
        ["Avg. ticket per center",       "USD 24.8K-82.8K/yr",        "USD 31K-69K/yr",
                                          "USD 345K-1.38M/yr",          "USD 0"],
        ["Reachable municipalities",     "4,143 (all)",               "~500 (med/large)",
                                          "~50 (large only)",           "4,143 (mandate)"],
        ["Customer acquisition cost",    "Low (referral)",            "Medium (direct sales)",
                                          "High (enterprise sales)",    "Zero (mandatory)"],
        ["Estimated gross margin",       "70-80% (SaaS)",             "50-65%",
                                          "30-45%",                     "N/A"],
        ["Entry barrier",                "Low",                       "Medium",
                                          "High",                       "Zero (mandatory)"],
    ]

    col_w = [CONTENT_W * p for p in [0.28, 0.18, 0.18, 0.20, 0.16]]

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
        ("BACKGROUND",     (1, 1), (1, -1), HexColor("#FFF5F5")),
        ("LINEAFTER",      (1, 0), (1, -1), 1.5, SAMU_COR),
        ("LINEBEFORE",     (1, 0), (1, -1), 1.5, SAMU_COR),
    ]))
    story.append(t)
    story.append(sp(0.3))
    story.append(Paragraph(
        f"Sources: Hexagon Year-End Report 2024 | SP Transparency Portal 2023 (USD 1.01M/yr ref. contract) | "
        f"Market estimates | {FX_NOTE}",
        s["nota"]
    ))
    story.append(PageBreak())


def pg_oportunidade_unica(s, story):
    story.append(hdr("The SAMU Amigo Unique Opportunity", s))
    story.append(hr())
    story.append(sp(0.3))

    oportunidades = [
        (SAMU_COR,    "Underserved Market: USD 63 M Untapped",
         "Small and med-small municipalities (< 100K inhabitants) represent 87% of all SAMU "
         "municipalities. MedSave and HXGN do not serve this segment. e-SUS has no AI. "
         "SAMU Amigo can be the only product with affordable clinical AI for these cities."),
        (VERDE,       "SaaS Model with 70-80% Gross Margins",
         "Software-as-a-service with very low marginal cost per new customer. "
         "While HXGN operates at 30-45% margins due to professional services and infrastructure, "
         "SAMU Amigo can operate at typical medical SaaS margins: 70-80%."),
        (DOURADO,     "Santo Andre as National Launchpad",
         "A documented case of response time reduction in Santo Andre is worth more than "
         "any marketing campaign. Brazilian municipalities inspire each other. "
         "The first public bid won opens the door to the other 4,143 municipalities."),
        (HEXAGON_COR, "Complementarity with e-SUS = No Political Resistance",
         "By being complementary to e-SUS SAMU (not a replacement), SAMU Amigo eliminates "
         "the main adoption barrier: political resistance. The manager does not need to "
         "abandon the federal system — just add intelligence on top of it."),
        (LARANJA,     "Clinical AI as a Defensible Moat",
         "ISA is not just a marketing differentiator — it is a real technological barrier. "
         "MedSave would take 2-3 years to develop equivalent clinical AI. HXGN has no "
         "incentive to focus on the Brazilian SAMU. e-SUS will never have AI given government cycles."),
    ]

    for cor, titulo, desc in oportunidades:
        bg_desc = HexColor("#F8F9FA") if cor not in [SAMU_COR, VERDE] else \
                  HexColor("#5D1A1A") if cor == SAMU_COR else HexColor("#145214")
        desc_color = BRANCO if cor in [SAMU_COR, VERDE] else CINZA_ESCURO

        bloco = Table([
            [Paragraph(titulo, ParagraphStyle("ot", fontName="Helvetica-Bold", fontSize=11,
                                               textColor=BRANCO, leading=15))],
            [Paragraph(desc,   ParagraphStyle("od", fontName="Helvetica", fontSize=9,
                                               textColor=desc_color, leading=14))],
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


def pg_conclusao_financeira(s, story):
    story.append(hdr("Financial Conclusion (USD)", s))
    story.append(hr())
    story.append(sp(0.4))

    numeros = [
        ("USD 96.6 M",  "Total Market\nBrazil / year"),
        ("USD 2.86 M",  "SAMU Amigo\nYear 5 revenue"),
        ("70-80%",      "Estimated margin\nSaaS model"),
        ("4,143",       "Municipalities\nreachable"),
    ]

    num_cells = []
    for val, label in numeros:
        cell = Table([
            [Paragraph(val, ParagraphStyle("nv", fontName="Helvetica-Bold", fontSize=16,
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

    final_comp = [
        ["System",        "Current BR Revenue",    "BR Potential",       "Key Advantage"],
        ["SAMU Amigo",    "Pre-revenue",            "USD 12-17 M",       "Unique clinical AI + low cost"],
        ["MedSave SEMS",  "USD 2.6-5.2 M/yr",      "USD 13.8-20.7 M",  "Consolidated MS compliance"],
        ["HXGN OnCall",   "USD 13.8-25.9 M/yr",    "USD 34.5-51.7 M",  "Global scale + GIS enterprise"],
        ["e-SUS SAMU",    "USD 0 (government)",     "USD 0 (state)",    "Federal mandate — mandatory"],
    ]

    col_w = [CONTENT_W * p for p in [0.22, 0.22, 0.20, 0.36]]
    cores_bg = [None, SAMU_COR, MEDSAVE_COR, HEXAGON_COR, ESUS_COR]

    fc_rows = []
    for i, row in enumerate(final_comp):
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
        '"The market already exists. The money is already there.<br/>'
        'SAMU Amigo is the only solution that has not arrived yet — but it will."',
        ParagraphStyle("msg", fontName="Helvetica-BoldOblique", fontSize=13,
                       textColor=DOURADO, alignment=TA_CENTER, leading=19)
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
    story.append(sp(0.3))
    story.append(Paragraph(FX_NOTE, s["nota"]))
    story.append(PageBreak())


# =====================================================================
# MONTAGEM
# =====================================================================
def gerar(output):
    s     = E()
    story = []

    pg_capa(s, story)
    pg_secao("Market Size (USD)", "The Brazilian SAMU software market in numbers", s, story)
    pg_tamanho_mercado(s, story)
    pg_secao("Competitor Revenue", "What each player earns today in Brazil (USD)", s, story)
    pg_faturamento_concorrentes(s, story)
    pg_secao("SAMU Amigo Potential", "Pricing model and financial assumptions (USD)", s, story)
    pg_potencial_samu(s, story)
    pg_secao("Revenue Projection", "SAMU Amigo: from Santo Andre to Brazil (USD)", s, story)
    pg_projecao_receita(s, story)
    pg_secao("Financial Comparison", "All 4 systems — side by side in numbers (USD)", s, story)
    pg_comparativo_financeiro(s, story)
    pg_secao("The Opportunity", "Why now and why SAMU Amigo (USD)", s, story)
    pg_oportunidade_unica(s, story)
    pg_secao("Conclusion", "The numbers that matter for Santo Andre (USD)", s, story)
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
    gerar("samu_amigo_potencial_financeiro_usd.pdf")

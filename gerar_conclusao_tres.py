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
VERMELHO        = HexColor("#C0392B")
VERMELHO_CLARO  = HexColor("#E74C3C")
AZUL_ESCURO     = HexColor("#0D1B2A")
AZUL_MEDIO      = HexColor("#1A3A6B")
AZUL_CLARO      = HexColor("#2980B9")
CINZA_ESCURO    = HexColor("#2C3E50")
CINZA_MEDIO     = HexColor("#7F8C8D")
CINZA_CLARO     = HexColor("#F4F6F8")
BRANCO          = colors.white
VERDE           = HexColor("#1E8449")
VERDE_CLARO     = HexColor("#27AE60")
LARANJA         = HexColor("#E67E22")
AMARELO         = HexColor("#F1C40F")
ROXO            = HexColor("#7D3C98")
DOURADO         = HexColor("#D4AC0D")
MEDSAVE_COR     = HexColor("#2C3E7A")
HEXAGON_COR     = HexColor("#0066CC")
ESUS_COR        = HexColor("#1A6B3C")
SAMU_COR        = HexColor("#C0392B")

PAGE_W, PAGE_H  = A4
MARGIN          = 2 * cm
CONTENT_W       = PAGE_W - 2 * MARGIN


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
            # Fundo escuro profundo
            c.setFillColor(AZUL_ESCURO)
            c.rect(0, 0, w, h, fill=1, stroke=0)
            # Faixa diagonal decorativa
            c.setFillColor(HexColor("#C0392B22"))
            c.rect(0, h * 0.55, w, h * 0.45, fill=1, stroke=0)
            # Barra lateral esquerda tricolor
            c.setFillColor(SAMU_COR)
            c.rect(0, 0, 0.5 * cm, h / 3, fill=1, stroke=0)
            c.setFillColor(HEXAGON_COR)
            c.rect(0, h / 3, 0.5 * cm, h / 3, fill=1, stroke=0)
            c.setFillColor(ESUS_COR)
            c.rect(0, 2 * h / 3, 0.5 * cm, h / 3, fill=1, stroke=0)
            # Faixa inferior dourada
            c.setFillColor(DOURADO)
            c.rect(0, 0, w, 0.8 * cm, fill=1, stroke=0)
            # Marca d'água
            c.setFillColor(HexColor("#FFFFFF05"))
            c.setFont("Helvetica-Bold", 140)
            c.drawCentredString(w / 2, h / 2 - 50, "SAMU")

        elif self.tipo == "secao":
            c.setFillColor(AZUL_MEDIO)
            c.rect(0, 0, w, h, fill=1, stroke=0)
            c.setFillColor(SAMU_COR)
            c.rect(0, 0, 0.8 * cm, h, fill=1, stroke=0)
            c.setFillColor(HexColor("#FFFFFF05"))
            c.setFont("Helvetica-Bold", 90)
            c.drawCentredString(w / 2, h / 2 - 30, "CONCLUSAO")

        elif self.tipo == "destaque":
            c.setFillColor(HexColor("#0A0F1A"))
            c.rect(0, 0, w, h, fill=1, stroke=0)
            c.setFillColor(DOURADO)
            c.rect(0, 0, 0.8 * cm, h, fill=1, stroke=0)
            c.setFillColor(HexColor("#D4AC0D10"))
            c.rect(0, 0, w, h * 0.3, fill=1, stroke=0)

        else:
            c.setFillColor(BRANCO)
            c.rect(0, 0, w, h, fill=1, stroke=0)
            # Header tricolor
            c.setFillColor(AZUL_ESCURO)
            c.rect(0, h - 1.8 * cm, w, 1.8 * cm, fill=1, stroke=0)
            # Tiras de cor dos 3 concorrentes
            bw = w / 3
            c.setFillColor(SAMU_COR)
            c.rect(0, h - 1.8 * cm, 0.4 * cm, 1.8 * cm, fill=1, stroke=0)
            c.setFillColor(HEXAGON_COR)
            c.rect(0.4 * cm, h - 1.8 * cm, 0.4 * cm, 1.8 * cm, fill=1, stroke=0)
            c.setFillColor(ESUS_COR)
            c.rect(0.8 * cm, h - 1.8 * cm, 0.4 * cm, 1.8 * cm, fill=1, stroke=0)
            # Texto header
            c.setFillColor(BRANCO)
            c.setFont("Helvetica-Bold", 9)
            c.drawString(1.6 * cm, h - 1.2 * cm, "SAMU AMIGO  |  Conclusao Comparativa")
            c.setFont("Helvetica", 9)
            c.drawRightString(w - 1.2 * cm, h - 1.2 * cm, "Santo Andre · 2025")
            # Footer
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
def estilos():
    return {
        "capa_titulo":   ParagraphStyle("ct", fontName="Helvetica-Bold", fontSize=14,
                                         textColor=AMARELO, alignment=TA_CENTER, leading=19,
                                         spaceBefore=0, spaceAfter=4),
        "capa_nome":     ParagraphStyle("cn", fontName="Helvetica-Bold", fontSize=44,
                                         textColor=BRANCO, alignment=TA_CENTER, leading=52),
        "capa_sub":      ParagraphStyle("cs", fontName="Helvetica", fontSize=14,
                                         textColor=HexColor("#B0C4DE"), alignment=TA_CENTER, leading=20),
        "capa_concl":    ParagraphStyle("cc", fontName="Helvetica-Bold", fontSize=16,
                                         textColor=DOURADO, alignment=TA_CENTER, leading=22),
        "capa_rodape":   ParagraphStyle("cr", fontName="Helvetica", fontSize=10,
                                         textColor=HexColor("#888888"), alignment=TA_CENTER, leading=15),
        "secao_titulo":  ParagraphStyle("st", fontName="Helvetica-Bold", fontSize=30,
                                         textColor=BRANCO, alignment=TA_CENTER, leading=38),
        "secao_sub":     ParagraphStyle("ss", fontName="Helvetica", fontSize=13,
                                         textColor=HexColor("#B0C4DE"), alignment=TA_CENTER, leading=18),
        "slide_titulo":  ParagraphStyle("slt", fontName="Helvetica-Bold", fontSize=17,
                                         textColor=BRANCO, alignment=TA_LEFT, leading=22),
        "dest_titulo":   ParagraphStyle("dt", fontName="Helvetica-Bold", fontSize=17,
                                         textColor=DOURADO, alignment=TA_LEFT, leading=22),
        "h2":            ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12,
                                         textColor=AZUL_ESCURO, leading=17, spaceAfter=5, spaceBefore=8),
        "body":          ParagraphStyle("body", fontName="Helvetica", fontSize=10,
                                         textColor=CINZA_ESCURO, leading=15, spaceAfter=4),
        "nota":          ParagraphStyle("nota", fontName="Helvetica-Oblique", fontSize=9,
                                         textColor=CINZA_MEDIO, leading=13, alignment=TA_CENTER),
    }


def sp(h):  return Spacer(1, h * cm)
def hr(cor=SAMU_COR, t=2):
    return HRFlowable(width="100%", thickness=t, color=cor, spaceAfter=8, spaceBefore=4)
def hdr(txt, s, key="slide_titulo"):
    return Paragraph(txt, s[key])


# =====================================================================
# PÁGINAS
# =====================================================================

def pg_capa(s, story):
    story.append(sp(2.8))
    story.append(Paragraph("ANALISE COMPARATIVA COMPLETA", s["capa_titulo"]))
    story.append(sp(0.2))
    story.append(Paragraph("SAMU AMIGO", s["capa_nome"]))
    story.append(sp(0.3))
    story.append(HRFlowable(width="60%", thickness=3, color=DOURADO,
                             spaceAfter=12, spaceBefore=4, hAlign="CENTER"))
    story.append(sp(0.1))
    story.append(Paragraph("Conclusao Estrategica dos Tres Modelos", s["capa_concl"]))
    story.append(sp(0.4))
    story.append(Paragraph(
        "MedSave SEMS SAMU  •  HXGN OnCall (Hexagon)  •  e-SUS SAMU (DATASUS)",
        s["capa_sub"]
    ))
    story.append(sp(1.2))

    # Três badges dos concorrentes
    badges = Table([[
        Paragraph("MedSave\nCompliance BR", ParagraphStyle("b1", fontName="Helvetica-Bold",
                  fontSize=9, textColor=BRANCO, alignment=TA_CENTER, leading=13)),
        Paragraph("HXGN OnCall\nLider Global", ParagraphStyle("b2", fontName="Helvetica-Bold",
                  fontSize=9, textColor=BRANCO, alignment=TA_CENTER, leading=13)),
        Paragraph("e-SUS SAMU\nGoverno Federal", ParagraphStyle("b3", fontName="Helvetica-Bold",
                  fontSize=9, textColor=BRANCO, alignment=TA_CENTER, leading=13)),
    ]], colWidths=[CONTENT_W / 3] * 3)
    badges.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (0, 0), MEDSAVE_COR),
        ("BACKGROUND",    (1, 0), (1, 0), HEXAGON_COR),
        ("BACKGROUND",    (2, 0), (2, 0), ESUS_COR),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("GRID",          (0, 0), (-1, -1), 1, AZUL_ESCURO),
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
    ]))
    story.append(badges)
    story.append(sp(0.8))
    story.append(Paragraph("Santo Andre · 2025", s["capa_rodape"]))
    story.append(PageBreak())


def pg_secao(titulo, sub, s, story):
    story.append(sp(5.2))
    story.append(Paragraph(titulo, s["secao_titulo"]))
    story.append(sp(0.3))
    story.append(HRFlowable(width="50%", thickness=3, color=DOURADO,
                             spaceAfter=10, spaceBefore=4, hAlign="CENTER"))
    story.append(Paragraph(sub, s["secao_sub"]))
    story.append(PageBreak())


def pg_radar_tres(s, story):
    """Tabela de posicionamento dos 4 produtos em 8 dimensoes-chave."""
    story.append(hdr("Posicionamento nos Eixos Estrategicos", s))
    story.append(hr())
    story.append(sp(0.3))

    story.append(Paragraph(
        "Avaliacao comparativa dos quatro sistemas em oito dimensoes criticas (1 = fraco  |  5 = excelente):",
        s["body"]
    ))
    story.append(sp(0.3))

    # Escala visual: blocos coloridos
    def barra(n, cor, max_n=5):
        filled = "■" * n + "□" * (max_n - n)
        return Paragraph(filled, ParagraphStyle("bar", fontName="Helvetica-Bold", fontSize=10,
                                                  textColor=cor, alignment=TA_CENTER, leading=14))

    dimensoes = [
        ("Inteligencia Clinica (IA)",  5, 1, 2, 0),
        ("Conformidade Ministerio MS", 3, 4, 5, 5),
        ("Interface / UX Moderna",     5, 3, 4, 1),
        ("Escala / Multi-agencia",     1, 3, 5, 2),
        ("Custo / Acessibilidade",     5, 2, 1, 5),
        ("Integracao Telefonica 192",  1, 3, 5, 4),
        ("GPS / Rastreio Viaturas",    4, 3, 5, 1),
        ("Pre-alerta Hospitalar",      5, 2, 2, 1),
    ]

    col_w = [CONTENT_W * p for p in [0.34, 0.165, 0.165, 0.165, 0.165]]

    header_row = [
        Paragraph("Dimensao", ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9,
                                              textColor=BRANCO, leading=13)),
        Paragraph("SAMU\nAmigo",  ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9,
                                                  textColor=BRANCO, alignment=TA_CENTER, leading=13)),
        Paragraph("MedSave\nSEMS", ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9,
                                                    textColor=BRANCO, alignment=TA_CENTER, leading=13)),
        Paragraph("HXGN\nOnCall",  ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9,
                                                    textColor=BRANCO, alignment=TA_CENTER, leading=13)),
        Paragraph("e-SUS\nSAMU",   ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9,
                                                    textColor=BRANCO, alignment=TA_CENTER, leading=13)),
    ]

    rows = [header_row]
    for dim, sa, ms, hx, es in dimensoes:
        rows.append([
            Paragraph(dim, ParagraphStyle("d", fontName="Helvetica-Bold", fontSize=9,
                                           textColor=AZUL_ESCURO, leading=13)),
            barra(sa, SAMU_COR),
            barra(ms, MEDSAVE_COR),
            barra(hx, HEXAGON_COR),
            barra(es, ESUS_COR),
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
        ("TOPPADDING",     (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING",  (0, 0), (-1, -1), 9),
        ("LEFTPADDING",    (0, 0), (-1, -1), 7),
    ]))
    story.append(t)
    story.append(sp(0.3))
    story.append(Paragraph(
        "■ = dimensao atendida plenamente  |  □ = dimensao ausente ou fraca",
        s["nota"]
    ))
    story.append(PageBreak())


def pg_diferencas_criticas(s, story):
    story.append(hdr("As 5 Diferencas Mais Importantes", s))
    story.append(hr())
    story.append(sp(0.3))

    diferencas = [
        (
            "1. SAMU Amigo e o UNICO com IA Clinica",
            SAMU_COR,
            "Nenhum dos tres concorrentes — MedSave, HXGN OnCall ou e-SUS SAMU — possui uma IA que "
            "auxilia ativamente o medico regulador na decisao clinica em tempo real. A ISA (Rádio-Operadora "
            "Virtual) e um diferencial tecnologico absoluto e exclusivo do SAMU Amigo.",
            [
                "MedSave: fluxo estatico de preenchimento de formularios",
                "HXGN OnCall: IA operacional (padroes/anomalias), nao clinica",
                "e-SUS SAMU: zero inteligencia artificial",
                "SAMU Amigo ISA: auxilia a DECISAO MEDICA no momento critico",
            ]
        ),
        (
            "2. Custo: SAMU Amigo vs Licencas Comerciais",
            VERDE,
            "MedSave e HXGN OnCall cobram licencas comerciais significativas. Para um municipio "
            "brasileiro de porte medio como Santo Andre, o investimento em licenciamento de um sistema "
            "enterprise pode inviabilizar a modernizacao. O SAMU Amigo elimina esse custo.",
            [
                "MedSave: licenca comercial periodica",
                "HXGN OnCall: licenciamento enterprise alto (modular)",
                "e-SUS SAMU: gratuito (mas legado e sem inovacao)",
                "SAMU Amigo: custo zero de licenca — investimento em implantacao",
            ]
        ),
        (
            "3. Conformidade: o e-SUS SAMU e Obrigatorio",
            ESUS_COR,
            "Este e o ponto politico mais critico. O e-SUS SAMU e mandatado pelo Ministerio da Saude "
            "para prestacao de contas e repasse federal. O SAMU Amigo nao substitui o e-SUS SAMU — "
            "precisa ser complementar a ele. MedSave e HXGN tambem nao substituem.",
            [
                "e-SUS SAMU: obrigatorio para repasse federal",
                "MedSave: conformidade com MS, mas nao substitui e-SUS",
                "HXGN OnCall: padrao internacional, nao adaptado ao MS brasileiro",
                "SAMU Amigo: estrategia de complementaridade com e-SUS",
            ]
        ),
        (
            "4. Escala: HXGN e Inalcancavel — e Desnecessario",
            HEXAGON_COR,
            "O HXGN OnCall opera em centenas de agencias globais com despacho automatico e GIS "
            "enterprise. Essa escala e impressionante — mas tambem e o que Santo Andre nao precisa "
            "e nao pode pagar. O SAMU Amigo entrega o que importa para uma central municipal.",
            [
                "HXGN: multi-agencia, multi-jurisdicao — escala global",
                "HXGN: despacho automatico por algoritmo de otimizacao",
                "Para Santo Andre: 1 central, 1 municipio, 1 objetivo",
                "SAMU Amigo: certo para o tamanho e o contexto",
            ]
        ),
        (
            "5. FAPH: Exclusividade do SAMU Amigo",
            LARANJA,
            "O Pre-Alerta Hospitalar (FAPH) com sinais vitais, Glasgow, procedimentos e ETA enviado "
            "ao hospital antes da chegada da viatura e um recurso ausente no MedSave, HXGN e e-SUS. "
            "Essa funcionalidade pode literalmente salvar vidas ao preparar o hospital com antecedencia.",
            [
                "MedSave: sem modulo de pre-alerta hospitalar",
                "HXGN OnCall: sem modulo equivalente ao FAPH brasileiro",
                "e-SUS SAMU: sem pre-alerta hospitalar",
                "SAMU Amigo: FAPH completo com todos os dados clinicos",
            ]
        ),
    ]

    for titulo, cor, desc, bullets in diferencas:
        # Header da diferença
        h_row = Table(
            [[Paragraph(titulo, ParagraphStyle("dh", fontName="Helvetica-Bold", fontSize=11,
                                                textColor=BRANCO, leading=15))]],
            colWidths=[CONTENT_W]
        )
        h_row.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (-1, -1), cor),
            ("TOPPADDING",    (0, 0), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
            ("LEFTPADDING",   (0, 0), (-1, -1), 12),
        ]))
        story.append(h_row)

        # Descricao
        desc_row = Table(
            [[Paragraph(desc, ParagraphStyle("dd", fontName="Helvetica", fontSize=9,
                                              textColor=CINZA_ESCURO, leading=14))]],
            colWidths=[CONTENT_W]
        )
        desc_row.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (-1, -1), CINZA_CLARO),
            ("TOPPADDING",    (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ("LEFTPADDING",   (0, 0), (-1, -1), 12),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 12),
        ]))
        story.append(desc_row)

        # Bullets
        bul_data = [[
            Paragraph(b, ParagraphStyle("bl", fontName="Helvetica", fontSize=8,
                                         textColor=CINZA_ESCURO, leading=12,
                                         leftIndent=8))
            for b in bullets
        ]]
        # dois por linha
        bul_rows = []
        for i in range(0, len(bullets), 2):
            pair = bullets[i:i+2]
            while len(pair) < 2:
                pair.append("")
            bul_rows.append([
                Paragraph(f"• {pair[0]}", ParagraphStyle("bl", fontName="Helvetica", fontSize=8,
                                                           textColor=CINZA_ESCURO, leading=12)),
                Paragraph(f"• {pair[1]}" if pair[1] else "", ParagraphStyle("bl", fontName="Helvetica",
                                                                              fontSize=8,
                                                                              textColor=CINZA_ESCURO,
                                                                              leading=12)),
            ])
        bt = Table(bul_rows, colWidths=[CONTENT_W / 2] * 2)
        bt.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (-1, -1), BRANCO),
            ("TOPPADDING",    (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ("LEFTPADDING",   (0, 0), (-1, -1), 10),
            ("LINEBELOW",     (0, -1), (-1, -1), 0.5, HexColor("#DDDDDD")),
        ]))
        story.append(bt)
        story.append(sp(0.3))

    story.append(PageBreak())


def pg_beneficios(s, story):
    story.append(hdr("Beneficios Exclusivos do SAMU Amigo", s))
    story.append(hr())
    story.append(sp(0.3))

    beneficios = [
        ("Para o Medico Regulador",   SAMU_COR,   BRANCO, [
            "ISA reduz a carga cognitiva em chamadas simultaneas",
            "Sugestao de conduta clinica em tempo real",
            "Interface moderna que agiliza o fluxo de trabalho",
            "Alerta sonoro para emergencias criticas",
            "Historico completo do paciente na tela",
        ]),
        ("Para o Paciente",           VERDE,      BRANCO, [
            "Triagem mais rapida = menor tempo de resposta",
            "Hospital preparado antes da chegada (FAPH)",
            "Conduta clinica mais precisa desde a primeira chamada",
            "Menor risco de erro humano por sobrecarga do regulador",
            "Continuidade do atendimento com dados em tempo real",
        ]),
        ("Para o Municipio",          AZUL_MEDIO, BRANCO, [
            "Custo zero de licenciamento de software",
            "Solucao customizavel ao contexto de Santo Andre",
            "Sem dependencia de fornecedor externo global",
            "Dados e inteligencia proprios do municipio",
            "Capacidade de evolucao independente",
        ]),
        ("Para o Gestor Publico",     LARANJA,    BRANCO, [
            "Dashboard com indicadores de performance em tempo real",
            "Relatorios exportaveis para prestacao de contas",
            "Evidencia de inovacao para a populacao",
            "Argumento diferencial frente a outros municipios",
            "Base para escalar o modelo para outros servicos de saude",
        ]),
    ]

    col_w = [CONTENT_W * 0.5, CONTENT_W * 0.5]

    for linha in range(0, len(beneficios), 2):
        pair = beneficios[linha:linha + 2]
        cards = []
        for titulo, bg, fg, itens in pair:
            rows_c = [[Paragraph(titulo, ParagraphStyle("bht", fontName="Helvetica-Bold",
                                                         fontSize=11, textColor=fg,
                                                         alignment=TA_CENTER, leading=15))]]
            for item in itens:
                rows_c.append([Paragraph(
                    f"+ {item}",
                    ParagraphStyle("bi", fontName="Helvetica", fontSize=9,
                                   textColor=CINZA_ESCURO, leading=14, leftIndent=6)
                )])
            tc = Table(rows_c, colWidths=[CONTENT_W * 0.5 - 0.2 * cm])
            tc.setStyle(TableStyle([
                ("BACKGROUND",    (0, 0), (-1, 0), bg),
                ("ROWBACKGROUNDS",(0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
                ("GRID",          (0, 0), (-1, -1), 0.4, HexColor("#DDDDDD")),
                ("TOPPADDING",    (0, 0), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
                ("LEFTPADDING",   (0, 0), (-1, -1), 10),
            ]))
            cards.append(tc)

        while len(cards) < 2:
            cards.append(Paragraph("", s["body"]))

        outer = Table([cards], colWidths=col_w)
        outer.setStyle(TableStyle([
            ("VALIGN",      (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING",(0, 0), (-1, -1), 4),
        ]))
        story.append(outer)
        story.append(sp(0.25))

    story.append(PageBreak())


def pg_matriz_decisao(s, story):
    story.append(hdr("Matriz de Decisao: Qual Sistema para Qual Necessidade", s))
    story.append(hr())
    story.append(sp(0.3))

    necessidades = [
        ["Necessidade",                        "SAMU Amigo", "MedSave", "HXGN", "e-SUS"],
        ["Auxilio IA na decisao clinica",       "★★★★★",  "★☆☆☆☆", "★★☆☆☆", "☆☆☆☆☆"],
        ["Conformidade com Ministerio da Saude","★★★☆☆",  "★★★★☆", "★★☆☆☆", "★★★★★"],
        ["Custo acessivel para municipio BR",   "★★★★★",  "★★☆☆☆", "★☆☆☆☆", "★★★★★"],
        ["Interface moderna e agil",            "★★★★★",  "★★★☆☆", "★★★★☆", "★☆☆☆☆"],
        ["Pre-alerta hospitalar (FAPH)",        "★★★★★",  "★☆☆☆☆", "★☆☆☆☆", "☆☆☆☆☆"],
        ["Rastreio GPS de viaturas",            "★★★★☆",  "★★☆☆☆", "★★★★★", "☆☆☆☆☆"],
        ["Escala multi-agencia",                "★☆☆☆☆",  "★★☆☆☆", "★★★★★", "★★☆☆☆"],
        ["Integracao com linha 192",            "★★☆☆☆",  "★★★☆☆", "★★★★★", "★★★☆☆"],
        ["Customizacao para Santo Andre",       "★★★★★",  "★★☆☆☆", "★☆☆☆☆", "★★☆☆☆"],
        ["Relatorio formato MS",                "★★★☆☆",  "★★★★☆", "★★☆☆☆", "★★★★★"],
    ]

    col_w = [CONTENT_W * p for p in [0.38, 0.155, 0.155, 0.155, 0.155]]

    def star_style(produto):
        cores = {
            "SAMU Amigo": SAMU_COR,
            "MedSave": MEDSAVE_COR,
            "HXGN": HEXAGON_COR,
            "e-SUS": ESUS_COR,
        }
        return ParagraphStyle("star", fontName="Helvetica-Bold", fontSize=9,
                               textColor=cores.get(produto, CINZA_MEDIO),
                               alignment=TA_CENTER, leading=13)

    rows = []
    for i, row in enumerate(necessidades):
        if i == 0:
            rows.append([
                Paragraph(row[0], ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9,
                                                  textColor=BRANCO, leading=13)),
                Paragraph(row[1], ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9,
                                                  textColor=BRANCO, alignment=TA_CENTER, leading=13)),
                Paragraph(row[2], ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9,
                                                  textColor=BRANCO, alignment=TA_CENTER, leading=13)),
                Paragraph(row[3], ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9,
                                                  textColor=BRANCO, alignment=TA_CENTER, leading=13)),
                Paragraph(row[4], ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9,
                                                  textColor=BRANCO, alignment=TA_CENTER, leading=13)),
            ])
        else:
            rows.append([
                Paragraph(row[0], ParagraphStyle("d", fontName="Helvetica", fontSize=9,
                                                  textColor=CINZA_ESCURO, leading=13)),
                Paragraph(row[1], star_style("SAMU Amigo")),
                Paragraph(row[2], star_style("MedSave")),
                Paragraph(row[3], star_style("HXGN")),
                Paragraph(row[4], star_style("e-SUS")),
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
    ]))
    story.append(t)
    story.append(sp(0.3))
    story.append(Paragraph(
        "★★★★★ = excelente  |  ★★★☆☆ = adequado  |  ★☆☆☆☆ = fraco  |  ☆☆☆☆☆ = ausente",
        s["nota"]
    ))
    story.append(PageBreak())


def pg_veredicto(s, story):
    """Slide de destaque — fundo escuro com destaque dourado."""
    story.append(hdr("Veredicto Final", s, "dest_titulo"))
    story.append(HRFlowable(width="100%", thickness=2, color=DOURADO,
                             spaceAfter=8, spaceBefore=4))
    story.append(sp(0.3))

    veredictos = [
        (MEDSAVE_COR, "MedSave SEMS SAMU",
         "O gestor que precisa de conformidade e nao tem recurso para inovacao.",
         "Certo para quem quer um produto pronto, certificado e sem surpresas. "
         "Nao tem IA clinica. Nao tem FAPH. Nao tem diferencial tecnologico. "
         "E o sistema para quem quer 'se virar bem', nao para quem quer se destacar."),

        (HEXAGON_COR, "HXGN OnCall (Hexagon)",
         "O gestor de uma metropole com orcamento de pais desenvolvido.",
         "Referencia mundial em CAD. Mas e caro, generico e nao fala o idioma do SAMU brasileiro. "
         "Impressiona no papel. Na pratica, entrega muito do que Santo Andre nao precisa "
         "e nao entrega o que mais importa: inteligencia clinica."),

        (ESUS_COR, "e-SUS SAMU (DATASUS)",
         "Todo municipio brasileiro — como obrigacao legal, nao como escolha.",
         "Sistema oficial, gratuito e mandatado. Essencial para conformidade e repasse federal. "
         "Mas e tecnologicamente defasado, sem IA, sem GPS, sem FAPH, sem UX moderna. "
         "E o piso obrigatorio — o SAMU Amigo e o teto possivel."),

        (SAMU_COR, "SAMU AMIGO",
         "Santo Andre — e todo municipio brasileiro que queira ser referencia nacional.",
         "A unica solucao com IA clinica ativa. Custo zero de licenciamento. "
         "Interface moderna. GPS, FAPH, multi-perfil. Desenhado para o SAMU brasileiro. "
         "Complementar ao e-SUS SAMU. Com o roadmap correto, entrega conformidade E inovacao. "
         "Nao e o que o mercado tem. E o que o mercado ainda nao sabe que precisa."),
    ]

    for cor, nome, perfil, desc in veredictos:
        destaque = nome == "SAMU AMIGO"
        nome_style = ParagraphStyle("vn", fontName="Helvetica-Bold",
                                    fontSize=12 if not destaque else 14,
                                    textColor=BRANCO, leading=16)
        perfil_style = ParagraphStyle("vp", fontName="Helvetica-Oblique",
                                       fontSize=9, textColor=AMARELO if destaque else HexColor("#DDDDDD"),
                                       leading=13)
        desc_style = ParagraphStyle("vd", fontName="Helvetica",
                                    fontSize=9, textColor=BRANCO if destaque else HexColor("#CCCCCC"),
                                    leading=14)

        bg = cor if not destaque else HexColor("#8B0000")  # vermelho mais escuro para SAMU Amigo

        bloco = Table([
            [Paragraph(nome, nome_style)],
            [Paragraph(f"Para: {perfil}", perfil_style)],
            [Paragraph(desc, desc_style)],
        ], colWidths=[CONTENT_W])
        bloco.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (-1, -1), bg),
            ("TOPPADDING",    (0, 0), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
            ("LEFTPADDING",   (0, 0), (-1, -1), 14),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 14),
            ("LINEABOVE",     (0, 0), (-1, 0), 2, DOURADO if destaque else BRANCO),
        ]))
        story.append(bloco)
        story.append(sp(0.2))

    story.append(PageBreak())


def pg_mensagem_final(s, story):
    """Slide de fechamento."""
    story.append(hdr("A Mensagem que Santo Andre Precisa Ouvir", s))
    story.append(hr())
    story.append(sp(0.5))

    msg1 = Table([[Paragraph(
        "Nenhum dos tres concorrentes faz o que o SAMU Amigo faz.<br/>"
        "Nenhum deles tem a ISA.<br/>"
        "Nenhum deles foi pensado para o seu paciente.",
        ParagraphStyle("m1", fontName="Helvetica-Bold", fontSize=14,
                       textColor=BRANCO, alignment=TA_CENTER, leading=21)
    )]], colWidths=[CONTENT_W])
    msg1.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), AZUL_MEDIO),
        ("TOPPADDING",    (0, 0), (-1, -1), 20),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 20),
        ("LEFTPADDING",   (0, 0), (-1, -1), 22),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 22),
    ]))
    story.append(msg1)
    story.append(sp(0.4))

    # Os tres pilares do argumento
    pilares = [
        (VERDE_CLARO, "Conformidade",
         "e-SUS SAMU (obrigatorio)\n+ roadmap SAMU Amigo"),
        (SAMU_COR, "Inovacao",
         "ISA — IA clinica exclusiva\nsem equivalente no mercado"),
        (DOURADO, "Impacto",
         "Vidas salvas mais rapido\nSanto Andre como referencia"),
    ]

    col_w = [CONTENT_W / 3] * 3
    p_rows = [[
        Paragraph(p[1], ParagraphStyle(
            "ph", fontName="Helvetica-Bold", fontSize=12,
            textColor=BRANCO, alignment=TA_CENTER, leading=16))
        for p in pilares
    ], [
        Paragraph(p[2].replace("\n", "<br/>"), ParagraphStyle(
            "pb", fontName="Helvetica", fontSize=9,
            textColor=BRANCO, alignment=TA_CENTER, leading=14))
        for p in pilares
    ]]

    pt = Table(p_rows, colWidths=col_w,
               rowHeights=[1.2 * cm, 2.5 * cm])
    pt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 1), VERDE),
        ("BACKGROUND", (1, 0), (1, 1), SAMU_COR),
        ("BACKGROUND", (2, 0), (2, 1), HexColor("#8B6914")),
        ("GRID",       (0, 0), (-1, -1), 2, BRANCO),
        ("VALIGN",     (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN",      (0, 0), (-1, -1), "CENTER"),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(pt)
    story.append(sp(0.5))

    frase = Table([[Paragraph(
        '"O mercado tem o que sempre teve.<br/>'
        'Santo Andre pode ter o que nunca existiu."',
        ParagraphStyle("fp", fontName="Helvetica-BoldOblique", fontSize=16,
                       textColor=DOURADO, alignment=TA_CENTER, leading=22)
    )]], colWidths=[CONTENT_W])
    frase.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), AZUL_ESCURO),
        ("TOPPADDING",    (0, 0), (-1, -1), 22),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 22),
        ("LEFTPADDING",   (0, 0), (-1, -1), 22),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 22),
        ("LINEABOVE",     (0, 0), (-1, 0), 3, DOURADO),
        ("LINEBELOW",     (0, -1), (-1, -1), 3, DOURADO),
    ]))
    story.append(frase)
    story.append(PageBreak())


# =====================================================================
# MONTAGEM
# =====================================================================
def gerar(output):
    s     = estilos()
    story = []

    pg_capa(s, story)
    pg_secao("Posicionamento", "Os quatro sistemas nos eixos estrategicos", s, story)
    pg_radar_tres(s, story)
    pg_secao("5 Diferencas Criticas", "O que realmente separa o SAMU Amigo dos concorrentes", s, story)
    pg_diferencas_criticas(s, story)
    pg_secao("Beneficios", "O que o SAMU Amigo entrega que nenhum outro entrega", s, story)
    pg_beneficios(s, story)
    pg_secao("Matriz de Decisao", "Qual sistema atende cada necessidade", s, story)
    pg_matriz_decisao(s, story)
    pg_secao("Veredicto", "Para quem e cada sistema — e por que o SAMU Amigo vence", s, story)
    pg_veredicto(s, story)
    pg_secao("Mensagem Final", "O argumento definitivo para Santo Andre", s, story)
    pg_mensagem_final(s, story)

    doc = SimpleDocTemplate(
        output, pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN,  bottomMargin=MARGIN,
    )

    DESTAQUE_PAGES = {13, 14}

    def on_page(c, doc):
        n = doc.page
        if n == 1:
            BG("capa")(c, doc)
        elif n % 2 == 0:
            BG("secao")(c, doc)
        elif n in DESTAQUE_PAGES:
            BG("destaque")(c, doc)
        else:
            BG("normal")(c, doc)

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f"PDF gerado: {output}")


if __name__ == "__main__":
    gerar("samu_amigo_conclusao_tres_modelos.pdf")

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
AZUL_CLARO     = HexColor("#3498DB")
CINZA_ESCURO   = HexColor("#2C3E50")
CINZA_MEDIO    = HexColor("#7F8C8D")
CINZA_CLARO    = HexColor("#ECF0F1")
BRANCO         = colors.white
VERDE          = HexColor("#27AE60")
LARANJA        = HexColor("#E67E22")
ROXO           = HexColor("#6A0DAD")
HEXAGON_AZUL   = HexColor("#0066CC")
HEXAGON_ESCURO = HexColor("#003366")

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
            # Fundo split: esquerda SAMU, direita Hexagon
            c.setFillColor(AZUL_ESCURO)
            c.rect(0, 0, w / 2, h, fill=1, stroke=0)
            c.setFillColor(HEXAGON_ESCURO)
            c.rect(w / 2, 0, w / 2, h, fill=1, stroke=0)
            # Linha divisória
            c.setStrokeColor(BRANCO)
            c.setLineWidth(2)
            c.line(w / 2, 0, w / 2, h)
            # Faixa inferior
            c.setFillColor(VERMELHO)
            c.rect(0, 0, w, 1.0 * cm, fill=1, stroke=0)
            # Marcas d'água
            c.setFillColor(HexColor("#FFFFFF08"))
            c.setFont("Helvetica-Bold", 100)
            c.drawCentredString(w / 4, h / 2 - 30, "SAMU")
            c.drawCentredString(3 * w / 4, h / 2 - 30, "HxGN")

        elif self.tipo == "secao":
            c.setFillColor(AZUL_MEDIO)
            c.rect(0, 0, w, h, fill=1, stroke=0)
            c.setFillColor(VERMELHO)
            c.rect(0, 0, 1.0 * cm, h, fill=1, stroke=0)
            c.setFillColor(HexColor("#FFFFFF06"))
            c.setFont("Helvetica-Bold", 90)
            c.drawCentredString(w / 2, h / 2 - 30, "vs")

        else:
            c.setFillColor(BRANCO)
            c.rect(0, 0, w, h, fill=1, stroke=0)
            # Header
            c.setFillColor(AZUL_ESCURO)
            c.rect(0, h - 1.8 * cm, w, 1.8 * cm, fill=1, stroke=0)
            c.setFillColor(VERMELHO)
            c.rect(0, h - 1.8 * cm, 0.5 * cm, 1.8 * cm, fill=1, stroke=0)
            c.setFillColor(HEXAGON_AZUL)
            c.rect(w - 0.5 * cm, h - 1.8 * cm, 0.5 * cm, 1.8 * cm, fill=1, stroke=0)
            # Texto header
            c.setFillColor(BRANCO)
            c.setFont("Helvetica-Bold", 9)
            c.drawString(1.2 * cm, h - 1.2 * cm, "SAMU AMIGO  vs  HXGN OnCall (Hexagon)")
            c.setFont("Helvetica", 9)
            c.drawRightString(w - 1.2 * cm, h - 1.2 * cm, "Santo Andre · 2025")
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
        "capa_titulo": ParagraphStyle("ct", fontName="Helvetica-Bold", fontSize=38,
                                      textColor=BRANCO, alignment=TA_CENTER, leading=46),
        "capa_vs":     ParagraphStyle("cv", fontName="Helvetica-Bold", fontSize=22,
                                      textColor=VERMELHO_CLARO, alignment=TA_CENTER, leading=28),
        "capa_sub":    ParagraphStyle("cs", fontName="Helvetica", fontSize=14,
                                      textColor=HexColor("#B0C4DE"), alignment=TA_CENTER, leading=20),
        "capa_label":  ParagraphStyle("cl", fontName="Helvetica-Bold", fontSize=11,
                                      textColor=HexColor("#AAAAAA"), alignment=TA_CENTER, leading=16),
        "secao_titulo":ParagraphStyle("st", fontName="Helvetica-Bold", fontSize=30,
                                      textColor=BRANCO, alignment=TA_CENTER, leading=38),
        "secao_sub":   ParagraphStyle("ss", fontName="Helvetica", fontSize=13,
                                      textColor=HexColor("#B0C4DE"), alignment=TA_CENTER, leading=18),
        "slide_titulo":ParagraphStyle("slt", fontName="Helvetica-Bold", fontSize=17,
                                      textColor=BRANCO, alignment=TA_LEFT, leading=22),
        "h2":          ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=13,
                                      textColor=AZUL_ESCURO, leading=18, spaceAfter=6, spaceBefore=10),
        "body":        ParagraphStyle("body", fontName="Helvetica", fontSize=10,
                                      textColor=CINZA_ESCURO, leading=15, spaceAfter=4),
        "nota":        ParagraphStyle("nota", fontName="Helvetica-Oblique", fontSize=9,
                                      textColor=CINZA_MEDIO, leading=13, alignment=TA_CENTER),
        "rodape_capa": ParagraphStyle("rc", fontName="Helvetica", fontSize=10,
                                      textColor=HexColor("#AAAAAA"), alignment=TA_CENTER, leading=14),
    }


def sp(h): return Spacer(1, h * cm)
def hr(cor=VERMELHO, t=2): return HRFlowable(width="100%", thickness=t, color=cor,
                                              spaceAfter=8, spaceBefore=4)
def header(txt, s): return Paragraph(txt, s["slide_titulo"])


# =====================================================================
# PÁGINAS
# =====================================================================

def pg_capa(s, story):
    story.append(sp(3.8))
    story.append(Paragraph("SAMU AMIGO", s["capa_titulo"]))
    story.append(sp(0.3))
    story.append(Paragraph("vs", s["capa_vs"]))
    story.append(sp(0.3))
    story.append(Paragraph("HXGN OnCall", ParagraphStyle("hxgn_t", fontName="Helvetica-Bold",
                                                          fontSize=38, textColor=HEXAGON_AZUL,
                                                          alignment=TA_CENTER, leading=46)))
    story.append(sp(0.5))
    story.append(HRFlowable(width="50%", thickness=3, color=VERMELHO_CLARO,
                             spaceAfter=10, spaceBefore=4, hAlign="CENTER"))
    story.append(Paragraph("Analise Comparativa Estrategica", s["capa_sub"]))
    story.append(sp(0.4))
    story.append(Paragraph("Inteligencia Clinica Brasileira  x  Plataforma CAD Global Enterprise",
                            s["capa_label"]))
    story.append(sp(0.6))
    story.append(Paragraph("Santo Andre · 2025", s["rodape_capa"]))
    story.append(PageBreak())


def pg_secao(titulo, subtitulo, s, story):
    story.append(sp(5))
    story.append(Paragraph(titulo, s["secao_titulo"]))
    story.append(sp(0.3))
    story.append(HRFlowable(width="50%", thickness=3, color=VERMELHO_CLARO,
                             spaceAfter=10, spaceBefore=4, hAlign="CENTER"))
    story.append(Paragraph(subtitulo, s["secao_sub"]))
    story.append(PageBreak())


def pg_perfis(s, story):
    story.append(header("Perfil dos Produtos", s))
    story.append(hr())
    story.append(sp(0.3))

    col_w = [CONTENT_W * 0.5, CONTENT_W * 0.5]

    def card(titulo, cor, itens):
        rows = [[Paragraph(titulo, ParagraphStyle("ct2", fontName="Helvetica-Bold", fontSize=13,
                                                   textColor=BRANCO, alignment=TA_CENTER, leading=17))]]
        for label, val in itens:
            rows.append([
                Table([[
                    Paragraph(label, ParagraphStyle("lbl", fontName="Helvetica-Bold", fontSize=9,
                                                     textColor=cor, leading=13)),
                    Paragraph(val,   ParagraphStyle("val", fontName="Helvetica", fontSize=9,
                                                     textColor=CINZA_ESCURO, leading=13)),
                ]], colWidths=[CONTENT_W * 0.18, CONTENT_W * 0.28])
            ])
        t = Table(rows, colWidths=[CONTENT_W * 0.5 - 0.2 * cm])
        ts = TableStyle([
            ("BACKGROUND",    (0, 0), (-1, 0), cor),
            ("ROWBACKGROUNDS",(0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
            ("GRID",          (0, 0), (-1, -1), 0.4, HexColor("#CCCCCC")),
            ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING",    (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ])
        t.setStyle(ts)
        return t

    samu_itens = [
        ("Tipo",       "Open-source / inovacao"),
        ("Plataforma", "React 18 + Base44 (low-code)"),
        ("Origem",     "Brasil — Santo Andre/SP"),
        ("Foco",       "Regulacao medica SAMU"),
        ("IA",         "ISA — triagem clinica ativa"),
        ("Custo",      "Gratuito / customizavel"),
        ("Escala",     "Municipal (1 central)"),
        ("Maturidade", "Em desenvolvimento"),
        ("Integracao", "Email / Base44"),
        ("Testes",     "Zero cobertura"),
    ]
    hxgn_itens = [
        ("Tipo",       "Produto enterprise SaaS/On-prem"),
        ("Plataforma", "CAD proprietario + GIS Hexagon"),
        ("Origem",     "Suecia — global (20.000+ func.)"),
        ("Foco",       "Policia, Bombeiros, EMS global"),
        ("IA",         "Smart Advisor — padroes/anomalias"),
        ("Custo",      "Licenciamento alto (modular)"),
        ("Escala",     "Multi-agencia, multi-jurisdicao"),
        ("Maturidade", "Produto maduro em centenas de agencias"),
        ("Integracao", "NG911, GIS, Records, Analytics"),
        ("Testes",     "N/A (produto certificado)"),
    ]

    outer = Table(
        [[card("SAMU AMIGO", VERMELHO, samu_itens),
          card("HXGN OnCall  |  Hexagon", HEXAGON_AZUL, hxgn_itens)]],
        colWidths=col_w
    )
    outer.setStyle(TableStyle([
        ("VALIGN",      (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING",(0, 0), (-1, -1), 4),
    ]))
    story.append(outer)
    story.append(PageBreak())


def pg_funcionalidades(s, story):
    story.append(header("Comparativo de Funcionalidades", s))
    story.append(hr())
    story.append(sp(0.3))

    SIM   = "Sim"
    NAO   = "Nao"
    PARC  = "Parcial"
    UNICO = "Exclusivo"

    dados = [
        ["Funcionalidade",                                    "SAMU Amigo",  "HXGN OnCall"],
        ["Central de despacho CAD em tempo real",            SIM,           SIM],
        ["Triagem com IA clinica (ISA)",                     UNICO,         NAO],
        ["Smart Advisor — deteccao de padroes/anomalias",    PARC,          SIM],
        ["Despacho automatico por algoritmo",                NAO,           SIM],
        ["Pre-alerta hospitalar (FAPH)",                     SIM,           PARC],
        ["Rastreio GPS de viaturas",                         SIM,           SIM],
        ["Dashboards e Analytics",                           SIM,           SIM],
        ["Modulo de Records (historico)",                    NAO,           SIM],
        ["Planejamento de grandes eventos",                  NAO,           SIM],
        ["Multi-agencia / multi-jurisdicao",                 NAO,           SIM],
        ["Integracao telefonica (911/192 nativo)",           NAO,           SIM],
        ["NG911 / Next Generation Emergency",                NAO,           SIM],
        ["GIS / Mapeamento enterprise",                      PARC,          SIM],
        ["Modulo de seguranca (PSIM)",                       NAO,           SIM],
        ["Multi-perfil (despachante/regulador/campo)",       SIM,           PARC],
        ["Relatorios formato Ministerio da Saude",           PARC,          NAO],
        ["Protocolo SAMU brasileiro integrado",              SIM,           NAO],
        ["Open-source / customizavel",                       SIM,           NAO],
        ["Cloud ou On-premises (escolha)",                   PARC,          SIM],
        ["SLA / Uptime garantido",                           NAO,           SIM],
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
        else:
            return ParagraphStyle("p", fontName="Helvetica-Oblique", fontSize=9,
                                  textColor=LARANJA, alignment=TA_CENTER, leading=12)

    col_w = [CONTENT_W * p for p in [0.56, 0.22, 0.22]]

    header_row = [
        Paragraph(dados[0][0], ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=10,
                                               textColor=BRANCO, leading=13)),
        Paragraph(dados[0][1], ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=10,
                                               textColor=BRANCO, alignment=TA_CENTER, leading=13)),
        Paragraph(dados[0][2], ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=10,
                                               textColor=BRANCO, alignment=TA_CENTER, leading=13)),
    ]
    rows = [header_row]
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
        ("BACKGROUND",     (2, 0), (2, 0), HEXAGON_AZUL),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
        ("GRID",           (0, 0), (-1, -1), 0.4, HexColor("#CCCCCC")),
        ("VALIGN",         (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",     (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING",  (0, 0), (-1, -1), 6),
        ("LEFTPADDING",    (0, 0), (-1, -1), 7),
    ]))
    story.append(t)
    story.append(sp(0.3))

    leg_data = [[
        Paragraph("Exclusivo SAMU Amigo", ParagraphStyle("l", fontName="Helvetica-Bold", fontSize=8,
                                                          textColor=ROXO, leading=11, alignment=TA_CENTER)),
        Paragraph("Sim", ParagraphStyle("l", fontName="Helvetica-Bold", fontSize=8,
                                         textColor=VERDE, leading=11, alignment=TA_CENTER)),
        Paragraph("Parcial", ParagraphStyle("l", fontName="Helvetica-Oblique", fontSize=8,
                                             textColor=LARANJA, leading=11, alignment=TA_CENTER)),
        Paragraph("Nao", ParagraphStyle("l", fontName="Helvetica", fontSize=8,
                                         textColor=VERMELHO, leading=11, alignment=TA_CENTER)),
    ]]
    leg = Table(leg_data, colWidths=[CONTENT_W / 4] * 4)
    leg.setStyle(TableStyle([
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("BOX",           (0, 0), (-1, -1), 0.4, HexColor("#CCCCCC")),
        ("BACKGROUND",    (0, 0), (-1, -1), CINZA_CLARO),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(leg)
    story.append(PageBreak())


def pg_ia(s, story):
    story.append(header("Inteligencia Artificial: ISA vs Smart Advisor", s))
    story.append(hr())
    story.append(sp(0.3))

    col_w = [CONTENT_W * 0.5, CONTENT_W * 0.5]

    def bloco(titulo, cor, itens):
        rows = [[Paragraph(titulo, ParagraphStyle("bt", fontName="Helvetica-Bold", fontSize=12,
                                                   textColor=BRANCO, alignment=TA_CENTER, leading=16))]]
        for item in itens:
            rows.append([Paragraph(f"• {item}", ParagraphStyle("bi", fontName="Helvetica", fontSize=9,
                                                                 textColor=CINZA_ESCURO, leading=14,
                                                                 leftIndent=8))])
        t = Table(rows, colWidths=[CONTENT_W * 0.5 - 0.3 * cm])
        t.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (-1, 0), cor),
            ("BACKGROUND",    (0, 1), (-1, -1), HexColor("#F8F9FA")),
            ("GRID",          (0, 0), (-1, -1), 0.4, HexColor("#DDDDDD")),
            ("TOPPADDING",    (0, 0), (-1, -1), 9),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
            ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ]))
        return t

    isa_itens = [
        "Auxilia ativamente o medico regulador",
        "Analise clinica em linguagem natural",
        "Sugestao de conduta medica em tempo real",
        "Reducao de carga cognitiva do regulador",
        "Especifico para o fluxo SAMU brasileiro",
        "Integrado ao chat de triagem",
        "Foco: decisao clinica correta",
        "Unico no mercado brasileiro",
    ]
    smart_itens = [
        "Detecta padroes em incidentes multiplos",
        "Identifica anomalias operacionais",
        "Alerta sobre eventos complexos emergentes",
        "Correlaciona incidentes ligados",
        "Machine Learning em dados historicos",
        "Otimiza alocacao de recursos por IA",
        "Foco: eficiencia operacional",
        "Implantado em agencias globais",
    ]

    outer = Table(
        [[bloco("ISA — SAMU Amigo", VERMELHO, isa_itens),
          bloco("Smart Advisor — HXGN OnCall", HEXAGON_AZUL, smart_itens)]],
        colWidths=col_w
    )
    outer.setStyle(TableStyle([
        ("VALIGN",      (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING",(0, 0), (-1, -1), 4),
    ]))
    story.append(outer)
    story.append(sp(0.5))

    insight = Table([[Paragraph(
        "A ISA atua no nivel CLINICO: o que fazer com o paciente.<br/>"
        "O Smart Advisor atua no nivel OPERACIONAL: como gerenciar os recursos.<br/>"
        "Sao IAs complementares, nao concorrentes diretas.",
        ParagraphStyle("ins", fontName="Helvetica-Bold", fontSize=11, textColor=BRANCO,
                       alignment=TA_CENTER, leading=17)
    )]], colWidths=[CONTENT_W])
    insight.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), AZUL_ESCURO),
        ("TOPPADDING",    (0, 0), (-1, -1), 16),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 16),
        ("LEFTPADDING",   (0, 0), (-1, -1), 20),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 20),
    ]))
    story.append(insight)
    story.append(PageBreak())


def pg_vantagens(s, story):
    story.append(header("Onde cada produto vence", s))
    story.append(hr())
    story.append(sp(0.3))

    col_w = [CONTENT_W * 0.5, CONTENT_W * 0.5]

    samu_v = [
        ("IA Clinica (ISA)",        "Unico no mercado: auxilia a decisao medica, nao so operacional"),
        ("Custo zero",              "Sem licenciamento. Investimento em implantacao, nao em royalties"),
        ("Foco SAMU BR",            "100% desenhado para o fluxo de regulacao medica brasileira"),
        ("FAPH",                    "Pre-alerta hospitalar detalhado sem equivalente nos concorrentes"),
        ("Customizavel",            "Codigo aberto, adaptavel sem depender de fornecedor global"),
        ("Multi-perfil clinico",    "Interfaces distintas para regulador, despachante e campo"),
        ("Protocolos MS",           "Protocolos do Ministerio da Saude embarcados na IA"),
    ]
    hxgn_v = [
        ("Escala global",           "Centenas de agencias implantadas em todo o mundo"),
        ("Multi-agencia",           "Coordenacao entre policia, bombeiros e EMS em uma plataforma"),
        ("Despacho automatico",     "Algoritmo seleciona o recurso ideal sem intervencao humana"),
        ("GIS enterprise",          "Mapeamento geoespacial rico da propria Hexagon"),
        ("Integracao 911/192",      "Conectado ao numero de emergencia nativamente"),
        ("SLA 99,9% + suporte 24/7","Confiabilidade contratual para servico critico"),
        ("Suite completa",          "Dispatch + Analytics + Records + Planning em um ecossistema"),
    ]

    def tabela_v(titulo, cor, itens):
        rows = [[Paragraph(titulo, ParagraphStyle("tv", fontName="Helvetica-Bold", fontSize=11,
                                                   textColor=BRANCO, alignment=TA_CENTER, leading=15))]]
        for label, desc in itens:
            rows.append([Table([[
                Paragraph(label, ParagraphStyle("vl", fontName="Helvetica-Bold", fontSize=9,
                                                 textColor=cor, leading=13)),
                Paragraph(desc,  ParagraphStyle("vd", fontName="Helvetica", fontSize=9,
                                                 textColor=CINZA_ESCURO, leading=13)),
            ]], colWidths=[CONTENT_W * 0.18, CONTENT_W * 0.28])])
        t = Table(rows, colWidths=[CONTENT_W * 0.5 - 0.2 * cm])
        t.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (-1, 0), cor),
            ("ROWBACKGROUNDS",(0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
            ("GRID",          (0, 0), (-1, -1), 0.4, HexColor("#CCCCCC")),
            ("VALIGN",        (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING",    (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ]))
        return t

    outer = Table(
        [[tabela_v("SAMU AMIGO vence em:", VERMELHO, samu_v),
          tabela_v("HXGN OnCall vence em:", HEXAGON_AZUL, hxgn_v)]],
        colWidths=col_w
    )
    outer.setStyle(TableStyle([
        ("VALIGN",      (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING",(0, 0), (-1, -1), 4),
    ]))
    story.append(outer)
    story.append(PageBreak())


def pg_matriz(s, story):
    story.append(header("Matriz Estrategica: IA Clinica x Escala Global", s))
    story.append(hr())
    story.append(sp(0.3))

    story.append(Paragraph(
        "Posicionamento dos dois produtos nos eixos de inovacao clinica e escala operacional:",
        s["body"]
    ))
    story.append(sp(0.3))

    quadrantes = [
        ["",
         Paragraph("Escala Global Alta", ParagraphStyle("ql", fontName="Helvetica-Bold",
                                                         fontSize=10, textColor=BRANCO,
                                                         alignment=TA_CENTER, leading=14)),
         Paragraph("Escala Global Baixa", ParagraphStyle("ql", fontName="Helvetica-Bold",
                                                          fontSize=10, textColor=BRANCO,
                                                          alignment=TA_CENTER, leading=14))],
        [Paragraph("IA Clinica Alta", ParagraphStyle("qr", fontName="Helvetica-Bold",
                                                      fontSize=10, textColor=BRANCO,
                                                      alignment=TA_CENTER, leading=14)),
         Paragraph("OBJETIVO\nSAMU Amigo\n+ roadmap completo",
                   ParagraphStyle("qc", fontName="Helvetica-Bold", fontSize=11,
                                  textColor=BRANCO, alignment=TA_CENTER, leading=16)),
         Paragraph("SAMU Amigo\n(estado atual)",
                   ParagraphStyle("qc2", fontName="Helvetica-Bold", fontSize=11,
                                  textColor=BRANCO, alignment=TA_CENTER, leading=16))],
        [Paragraph("IA Clinica Baixa", ParagraphStyle("qr", fontName="Helvetica-Bold",
                                                       fontSize=10, textColor=BRANCO,
                                                       alignment=TA_CENTER, leading=14)),
         Paragraph("HXGN OnCall\n(estado atual)",
                   ParagraphStyle("qc3", fontName="Helvetica-Bold", fontSize=11,
                                  textColor=BRANCO, alignment=TA_CENTER, leading=16)),
         Paragraph("Sistemas Legados",
                   ParagraphStyle("qc4", fontName="Helvetica", fontSize=10,
                                  textColor=HexColor("#AAAAAA"), alignment=TA_CENTER, leading=14))],
    ]

    col_w = [CONTENT_W * 0.22, CONTENT_W * 0.39, CONTENT_W * 0.39]
    mt = Table(quadrantes, colWidths=col_w,
               rowHeights=[1.2 * cm, 3.5 * cm, 3.5 * cm])
    mt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), AZUL_ESCURO),
        ("BACKGROUND", (1, 0), (2, 0), AZUL_MEDIO),
        ("BACKGROUND", (0, 1), (0, 2), AZUL_MEDIO),
        ("BACKGROUND", (1, 1), (1, 1), VERDE),          # Objetivo
        ("BACKGROUND", (2, 1), (2, 1), VERMELHO),       # SAMU atual
        ("BACKGROUND", (1, 2), (1, 2), HEXAGON_AZUL),   # HXGN
        ("BACKGROUND", (2, 2), (2, 2), CINZA_CLARO),    # Legados
        ("GRID",       (0, 0), (-1, -1), 2, BRANCO),
        ("VALIGN",     (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN",      (0, 0), (-1, -1), "CENTER"),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(mt)
    story.append(sp(0.4))
    story.append(Paragraph(
        "Verde = posicao alvo do SAMU Amigo apos roadmap  |  "
        "Vermelho = posicao atual do SAMU Amigo  |  "
        "Azul = HXGN OnCall",
        s["nota"]
    ))
    story.append(PageBreak())


def pg_oportunidade(s, story):
    story.append(header("Oportunidade Estrategica para Santo Andre", s))
    story.append(hr())
    story.append(sp(0.3))

    itens = [
        ("Por que nao o HXGN OnCall?",
         HEXAGON_AZUL,
         [
             "Custo proibitivo de licenciamento para municipios brasileiros",
             "Produto generico (policia + bombeiros + EMS) sem foco no SAMU",
             "Sem protocolos do Ministerio da Saude brasileiro integrados",
             "Dependencia total de fornecedor global para customizacoes",
             "Nao tem FAPH nem fluxo de regulacao medica especializado",
         ]),
        ("Por que o SAMU Amigo e o caminho?",
         VERMELHO,
         [
             "ISA: a unica IA clinica para regulacao medica no mercado",
             "Custo zero de licenciamento — investimento em implantacao",
             "Desenhado 100% para o fluxo SAMU e o contexto brasileiro",
             "Customizavel para as necessidades especificas de Santo Andre",
             "Com o roadmap correto, entrega compliance E inovacao",
         ]),
    ]

    for titulo, cor, pontos in itens:
        header_row = [Paragraph(titulo, ParagraphStyle("oh", fontName="Helvetica-Bold",
                                                        fontSize=12, textColor=BRANCO,
                                                        alignment=TA_CENTER, leading=16))]
        rows = [header_row]
        for p in pontos:
            rows.append([Paragraph(f"• {p}", ParagraphStyle("op", fontName="Helvetica",
                                                              fontSize=10, textColor=CINZA_ESCURO,
                                                              leading=15, leftIndent=10))])
        t = Table(rows, colWidths=[CONTENT_W])
        t.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (-1, 0), cor),
            ("ROWBACKGROUNDS",(0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
            ("GRID",          (0, 0), (-1, -1), 0.4, HexColor("#CCCCCC")),
            ("TOPPADDING",    (0, 0), (-1, -1), 9),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
            ("LEFTPADDING",   (0, 0), (-1, -1), 12),
        ]))
        story.append(t)
        story.append(sp(0.4))

    story.append(PageBreak())


def pg_conclusao(s, story):
    story.append(header("Conclusao", s))
    story.append(hr())
    story.append(sp(0.4))

    comp = [
        ["Dimensao",        "HXGN OnCall",                   "SAMU Amigo"],
        ["Categoria",       "Ferrari das plataformas CAD",    "Disruptor clinico brasileiro"],
        ["IA",              "Operacional (padroes/recursos)", "Clinica (decisao medica)"],
        ["Custo",           "Alto (enterprise global)",       "Zero licenciamento"],
        ["Foco",            "Generica (policia/bombeiros/EMS)","100% SAMU brasileiro"],
        ["Conformidade",    "Padroes internacionais",         "Em construcao"],
        ["Escala",          "Global — multiplas agencias",    "Municipal — Santo Andre"],
        ["Diferencial chave","Despacho automatico + GIS",     "ISA — unico no mercado"],
    ]

    col_w = [CONTENT_W * p for p in [0.28, 0.36, 0.36]]

    c_rows = []
    for i, row in enumerate(comp):
        if i == 0:
            c_rows.append([
                Paragraph(c, ParagraphStyle("ch", fontName="Helvetica-Bold", fontSize=10,
                                             textColor=BRANCO, alignment=TA_CENTER, leading=13))
                for c in row
            ])
        else:
            c_rows.append([
                Paragraph(row[0], ParagraphStyle("cd", fontName="Helvetica-Bold", fontSize=9,
                                                  textColor=AZUL_ESCURO, leading=13)),
                Paragraph(row[1], ParagraphStyle("ch2", fontName="Helvetica", fontSize=9,
                                                  textColor=CINZA_ESCURO, alignment=TA_CENTER, leading=13)),
                Paragraph(row[2], ParagraphStyle("cs2", fontName="Helvetica-Bold", fontSize=9,
                                                  textColor=AZUL_MEDIO, alignment=TA_CENTER, leading=13)),
            ])

    ct = Table(c_rows, colWidths=col_w)
    ct.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), AZUL_ESCURO),
        ("BACKGROUND",    (1, 0), (1, 0), HEXAGON_AZUL),
        ("BACKGROUND",    (2, 0), (2, 0), VERMELHO),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
        ("GRID",          (0, 0), (-1, -1), 0.5, HexColor("#CCCCCC")),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("LINEAFTER",     (1, 0), (1, -1), 1.5, BRANCO),
    ]))
    story.append(ct)
    story.append(sp(0.6))

    box = Table([[Paragraph(
        "O HXGN OnCall e o padrao ouro em escala e operacoes.<br/>"
        "O SAMU Amigo e o unico produto com IA clinica para regulacao medica.<br/>"
        "Para Santo Andre: o HXGN e o que o mundo tem.<br/>"
        "O SAMU Amigo e o que o mundo ainda nao tem.",
        ParagraphStyle("bf", fontName="Helvetica-Bold", fontSize=12, textColor=BRANCO,
                       alignment=TA_CENTER, leading=19)
    )]], colWidths=[CONTENT_W])
    box.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), AZUL_ESCURO),
        ("TOPPADDING",    (0, 0), (-1, -1), 18),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 18),
        ("LEFTPADDING",   (0, 0), (-1, -1), 24),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 24),
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
    pg_secao("Perfil dos Produtos", "Quem e cada um dos dois players", s, story)
    pg_perfis(s, story)
    pg_secao("Funcionalidades", "Comparativo item a item", s, story)
    pg_funcionalidades(s, story)
    pg_secao("Inteligencia Artificial", "ISA vs Smart Advisor — diferentes camadas de IA", s, story)
    pg_ia(s, story)
    pg_secao("Vantagens Comparativas", "Onde cada produto e superior", s, story)
    pg_vantagens(s, story)
    pg_secao("Matriz Estrategica", "Posicionamento nos eixos de inovacao e escala", s, story)
    pg_matriz(s, story)
    pg_secao("Oportunidade", "Por que Santo Andre deve escolher o SAMU Amigo", s, story)
    pg_oportunidade(s, story)
    pg_secao("Conclusao", "Sintese final da analise", s, story)
    pg_conclusao(s, story)

    doc = SimpleDocTemplate(
        output, pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN,  bottomMargin=MARGIN,
    )

    def on_page(c, doc):
        n = doc.page
        if n == 1:
            Background("capa")(c, doc)
        elif n % 2 == 0:
            Background("secao")(c, doc)
        else:
            Background("normal")(c, doc)

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f"PDF gerado: {output}")


if __name__ == "__main__":
    gerar("samu_amigo_vs_hxgn_oncall.pdf")

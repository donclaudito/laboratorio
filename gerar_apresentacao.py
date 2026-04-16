from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.platypus import PageBreak
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

# === PALETA DE CORES ===
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

PAGE_W, PAGE_H = A4

# === BACKGROUND POR PÁGINA ===
class SlideBackground:
    def __init__(self, tipo="normal"):
        self.tipo = tipo

    def __call__(self, canvas_obj, doc):
        canvas_obj.saveState()
        w, h = PAGE_W, PAGE_H

        if self.tipo == "capa":
            # Fundo degradê escuro
            canvas_obj.setFillColor(AZUL_ESCURO)
            canvas_obj.rect(0, 0, w, h, fill=1, stroke=0)
            # Faixa vermelha lateral
            canvas_obj.setFillColor(VERMELHO)
            canvas_obj.rect(0, 0, 1.2*cm, h, fill=1, stroke=0)
            # Faixa inferior
            canvas_obj.setFillColor(VERMELHO_CLARO)
            canvas_obj.rect(0, 0, w, 1.2*cm, fill=1, stroke=0)
            # Marca d'água sutil
            canvas_obj.setFillColor(HexColor("#FFFFFF08"))
            canvas_obj.setFont("Helvetica-Bold", 180)
            canvas_obj.drawCentredString(w/2, h/2 - 60, "SAMU")

        elif self.tipo == "secao":
            canvas_obj.setFillColor(AZUL_MEDIO)
            canvas_obj.rect(0, 0, w, h, fill=1, stroke=0)
            canvas_obj.setFillColor(VERMELHO)
            canvas_obj.rect(0, 0, 1.2*cm, h, fill=1, stroke=0)
            canvas_obj.setFillColor(HexColor("#FFFFFF08"))
            canvas_obj.setFont("Helvetica-Bold", 120)
            canvas_obj.drawCentredString(w/2, h/2 - 40, "SAMU")

        else:
            # Normal: fundo branco com header e footer
            canvas_obj.setFillColor(BRANCO)
            canvas_obj.rect(0, 0, w, h, fill=1, stroke=0)
            # Header strip
            canvas_obj.setFillColor(AZUL_ESCURO)
            canvas_obj.rect(0, h - 1.8*cm, w, 1.8*cm, fill=1, stroke=0)
            # Faixa vermelha no header
            canvas_obj.setFillColor(VERMELHO)
            canvas_obj.rect(0, h - 1.8*cm, 0.6*cm, 1.8*cm, fill=1, stroke=0)
            # Footer strip
            canvas_obj.setFillColor(AZUL_ESCURO)
            canvas_obj.rect(0, 0, w, 1.0*cm, fill=1, stroke=0)
            # Texto header
            canvas_obj.setFillColor(BRANCO)
            canvas_obj.setFont("Helvetica-Bold", 9)
            canvas_obj.drawString(1.5*cm, h - 1.2*cm, "SAMU AMIGO  |  Análise Comparativa")
            canvas_obj.setFont("Helvetica", 9)
            canvas_obj.drawRightString(w - 1.5*cm, h - 1.2*cm, "Santo André · 2025")
            # Número da página
            canvas_obj.setFillColor(HexColor("#AAAAAA"))
            canvas_obj.setFont("Helvetica", 8)
            canvas_obj.drawCentredString(w/2, 0.35*cm, f"Página {doc.page}")

        canvas_obj.restoreState()


def build_styles():
    base = getSampleStyleSheet()

    styles = {
        "capa_titulo": ParagraphStyle(
            "capa_titulo",
            fontName="Helvetica-Bold",
            fontSize=36,
            textColor=BRANCO,
            alignment=TA_LEFT,
            leading=44,
            spaceAfter=12,
        ),
        "capa_subtitulo": ParagraphStyle(
            "capa_subtitulo",
            fontName="Helvetica",
            fontSize=16,
            textColor=HexColor("#B0C4DE"),
            alignment=TA_LEFT,
            leading=22,
            spaceAfter=6,
        ),
        "capa_badge": ParagraphStyle(
            "capa_badge",
            fontName="Helvetica-Bold",
            fontSize=11,
            textColor=BRANCO,
            alignment=TA_LEFT,
            leading=16,
        ),
        "secao_titulo": ParagraphStyle(
            "secao_titulo",
            fontName="Helvetica-Bold",
            fontSize=32,
            textColor=BRANCO,
            alignment=TA_CENTER,
            leading=40,
            spaceAfter=10,
        ),
        "secao_sub": ParagraphStyle(
            "secao_sub",
            fontName="Helvetica",
            fontSize=14,
            textColor=HexColor("#B0C4DE"),
            alignment=TA_CENTER,
            leading=20,
        ),
        "slide_titulo": ParagraphStyle(
            "slide_titulo",
            fontName="Helvetica-Bold",
            fontSize=18,
            textColor=BRANCO,
            alignment=TA_LEFT,
            leading=22,
        ),
        "h2": ParagraphStyle(
            "h2",
            fontName="Helvetica-Bold",
            fontSize=14,
            textColor=AZUL_ESCURO,
            spaceAfter=8,
            spaceBefore=12,
            leading=18,
        ),
        "body": ParagraphStyle(
            "body",
            fontName="Helvetica",
            fontSize=10,
            textColor=CINZA_ESCURO,
            leading=15,
            spaceAfter=5,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            fontName="Helvetica",
            fontSize=10,
            textColor=CINZA_ESCURO,
            leading=15,
            leftIndent=14,
            spaceAfter=4,
        ),
        "label_verde": ParagraphStyle(
            "label_verde",
            fontName="Helvetica-Bold",
            fontSize=9,
            textColor=BRANCO,
            alignment=TA_CENTER,
            leading=12,
        ),
        "label_vermelho": ParagraphStyle(
            "label_vermelho",
            fontName="Helvetica-Bold",
            fontSize=9,
            textColor=BRANCO,
            alignment=TA_CENTER,
            leading=12,
        ),
        "nota": ParagraphStyle(
            "nota",
            fontName="Helvetica-Oblique",
            fontSize=9,
            textColor=CINZA_MEDIO,
            leading=13,
            alignment=TA_CENTER,
        ),
        "rodape_capa": ParagraphStyle(
            "rodape_capa",
            fontName="Helvetica",
            fontSize=10,
            textColor=HexColor("#AAAAAA"),
            alignment=TA_LEFT,
            leading=15,
        ),
    }
    return styles


def header_slide(texto, styles):
    """Parágrafo para o header de cada slide normal."""
    return Paragraph(texto, styles["slide_titulo"])


def spacer(h_cm):
    return Spacer(1, h_cm * cm)


def divider(color=VERMELHO, thickness=2):
    return HRFlowable(width="100%", thickness=thickness, color=color, spaceAfter=8, spaceBefore=4)


# =====================================================================
# CONTEÚDO DAS PÁGINAS
# =====================================================================

def pagina_capa(styles, story):
    """Slide de capa."""
    story.append(spacer(4.5))
    story.append(Paragraph("SAMU AMIGO", styles["capa_titulo"]))
    story.append(Paragraph("vs. MedSave SEMS SAMU", styles["capa_subtitulo"]))
    story.append(spacer(0.4))
    story.append(divider(VERMELHO_CLARO, 3))
    story.append(spacer(0.3))
    story.append(Paragraph("Análise Comparativa Estratégica", styles["capa_subtitulo"]))
    story.append(spacer(0.5))
    story.append(Paragraph("Serviço de Atendimento Móvel de Urgência — Santo André · 2025", styles["rodape_capa"]))
    story.append(PageBreak())


def pagina_secao(titulo, subtitulo, styles, story):
    story.append(spacer(5))
    story.append(Paragraph(titulo, styles["secao_titulo"]))
    story.append(spacer(0.4))
    story.append(HRFlowable(width="60%", thickness=3, color=VERMELHO_CLARO,
                             spaceAfter=10, spaceBefore=4, hAlign="CENTER"))
    story.append(Paragraph(subtitulo, styles["secao_sub"]))
    story.append(PageBreak())


def tabela_comparativa_geral(styles, story):
    story.append(header_slide("Visão Geral Comparativa", styles))
    story.append(divider())
    story.append(spacer(0.3))

    dados = [
        ["Dimensão", "SAMU Amigo", "MedSave SEMS SAMU"],
        ["Tipo de solução", "Open-source / inovação", "Produto comercial consolidado"],
        ["Plataforma", "React 18 + Base44 (low-code)", "Sistema web proprietário"],
        ["Foco principal", "Inteligência clínica (IA)", "Compliance + gestão"],
        ["Usuário beneficiado", "Médico regulador / Paciente", "Gestor / Auditor"],
        ["Resultado entregue", "Despacho correto e rápido", "Relatório correto"],
        ["Custo", "Gratuito / customizável", "Licença comercial"],
        ["Suporte", "Comunidade / equipe interna", "Suporte 24/7 especializado"],
        ["Certificações", "Em desenvolvimento", "ISO 27001 · LGPD · 99,9% uptime"],
        ["Personalização", "Alta (código aberto)", "Limitada ao produto"],
    ]

    col_w = [(PAGE_W - 4*cm) * p for p in [0.30, 0.35, 0.35]]

    ts = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), AZUL_ESCURO),
        ("TEXTCOLOR",  (0, 0), (-1, 0), BRANCO),
        ("FONTNAME",   (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",   (0, 0), (-1, 0), 10),
        ("ALIGN",      (0, 0), (-1, 0), "CENTER"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
        ("FONTNAME",   (0, 1), (0, -1), "Helvetica-Bold"),
        ("FONTSIZE",   (0, 1), (-1, -1), 9),
        ("TEXTCOLOR",  (0, 1), (0, -1), AZUL_ESCURO),
        ("TEXTCOLOR",  (1, 1), (1, -1), CINZA_ESCURO),
        ("TEXTCOLOR",  (2, 1), (2, -1), CINZA_ESCURO),
        ("ALIGN",      (1, 1), (-1, -1), "CENTER"),
        ("VALIGN",     (0, 0), (-1, -1), "MIDDLE"),
        ("GRID",       (0, 0), (-1, -1), 0.4, HexColor("#CCCCCC")),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        # destaque coluna SAMU Amigo
        ("BACKGROUND", (1, 0), (1, 0), VERMELHO),
        ("FONTNAME",   (1, 1), (1, -1), "Helvetica-Bold"),
        ("TEXTCOLOR",  (1, 1), (1, -1), AZUL_MEDIO),
    ])

    t = Table([
        [Paragraph(c, ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=10,
                                     textColor=BRANCO, alignment=TA_CENTER, leading=13))
         for c in dados[0]]
    ] + [
        [Paragraph(str(cell), ParagraphStyle("td", fontName="Helvetica", fontSize=9,
                                             textColor=CINZA_ESCURO, leading=13))
         for cell in row]
        for row in dados[1:]
    ], colWidths=col_w)
    t.setStyle(ts)

    story.append(t)
    story.append(spacer(0.4))
    story.append(Paragraph(
        "* Coluna destacada em vermelho = SAMU Amigo",
        styles["nota"]
    ))
    story.append(PageBreak())


def tabela_funcionalidades(styles, story):
    story.append(header_slide("Comparativo de Funcionalidades", styles))
    story.append(divider())
    story.append(spacer(0.3))

    SIM   = "Sim"
    NAO   = "Nao"
    PARC  = "Parcial"
    UNICO = "Exclusivo"

    dados = [
        ["Funcionalidade", "SAMU Amigo", "MedSave"],
        ["Central de despacho em tempo real", SIM, SIM],
        ["Triagem com Inteligência Artificial (ISA)", UNICO, NAO],
        ["Regulação médica assistida por IA", UNICO, NAO],
        ["Rastreio GPS de viaturas", SIM, SIM],
        ["Pré-alerta hospitalar (FAPH)", SIM, PARC],
        ["Dashboards e Analytics", SIM, SIM],
        ["Relatórios em PDF", SIM, SIM],
        ["Relatórios no formato Ministerial", PARC, SIM],
        ["Protocolos Ministério da Saúde integrados", PARC, SIM],
        ["Integração nativa com linha 192", NAO, SIM],
        ["Ficha de regulação digital obrigatória", PARC, SIM],
        ["ISO 27001 / LGPD certificado", NAO, SIM],
        ["99,9% Uptime garantido", NAO, SIM],
        ["Multi-perfil (despachante/regulador/campo)", SIM, PARC],
        ["Notificações sonoras de alerta crítico", SIM, NAO],
        ["Open-source / customizável", SIM, NAO],
    ]

    def cell_style(val):
        if val == UNICO:
            return ParagraphStyle("u", fontName="Helvetica-Bold", fontSize=9,
                                  textColor=HexColor("#6A0DAD"), alignment=TA_CENTER, leading=13)
        elif val == SIM:
            return ParagraphStyle("s", fontName="Helvetica-Bold", fontSize=9,
                                  textColor=VERDE, alignment=TA_CENTER, leading=13)
        elif val == NAO:
            return ParagraphStyle("n", fontName="Helvetica", fontSize=9,
                                  textColor=VERMELHO, alignment=TA_CENTER, leading=13)
        else:
            return ParagraphStyle("p", fontName="Helvetica-Oblique", fontSize=9,
                                  textColor=LARANJA, alignment=TA_CENTER, leading=13)

    col_w = [(PAGE_W - 4*cm) * p for p in [0.54, 0.23, 0.23]]

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
        feat = Paragraph(row[0], ParagraphStyle("feat", fontName="Helvetica", fontSize=9,
                                                  textColor=CINZA_ESCURO, leading=13))
        c1   = Paragraph(row[1], cell_style(row[1]))
        c2   = Paragraph(row[2], cell_style(row[2]))
        rows.append([feat, c1, c2])

    ts = TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), AZUL_ESCURO),
        ("BACKGROUND",    (1, 0), (1, 0), VERMELHO),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
        ("GRID",          (0, 0), (-1, -1), 0.4, HexColor("#CCCCCC")),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
    ])

    t = Table(rows, colWidths=col_w)
    t.setStyle(ts)
    story.append(t)
    story.append(spacer(0.3))

    legenda_data = [
        [Paragraph("Exclusivo", ParagraphStyle("l", fontName="Helvetica-Bold", fontSize=8,
                                                textColor=HexColor("#6A0DAD"), leading=11)),
         Paragraph("Sim", ParagraphStyle("l", fontName="Helvetica-Bold", fontSize=8,
                                          textColor=VERDE, leading=11)),
         Paragraph("Parcial", ParagraphStyle("l", fontName="Helvetica-Oblique", fontSize=8,
                                              textColor=LARANJA, leading=11)),
         Paragraph("Nao", ParagraphStyle("l", fontName="Helvetica", fontSize=8,
                                          textColor=VERMELHO, leading=11))],
    ]
    leg = Table(legenda_data, colWidths=[(PAGE_W - 4*cm)/4]*4)
    leg.setStyle(TableStyle([
        ("ALIGN",   (0, 0), (-1, -1), "CENTER"),
        ("BOX",     (0, 0), (-1, -1), 0.4, HexColor("#CCCCCC")),
        ("BACKGROUND", (0, 0), (-1, -1), CINZA_CLARO),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(leg)
    story.append(PageBreak())


def pagina_diferenciais_samu(styles, story):
    story.append(header_slide("Diferenciais do SAMU Amigo", styles))
    story.append(divider())
    story.append(spacer(0.3))

    items = [
        ("IA de Triagem — ISA",
         "Rádio-Operadora Virtual com processamento de linguagem natural. Auxilia ativamente "
         "o médico regulador na tomada de decisão clínica em tempo real, reduzindo carga cognitiva "
         "e tempo de resposta. Nenhum concorrente direto oferece este recurso."),
        ("Multi-perfil Especializado",
         "Interfaces distintas e otimizadas para despachante, médico regulador e equipes de campo — "
         "cada ator vê apenas o que precisa, no momento que precisa."),
        ("Pré-alerta Hospitalar Detalhado (FAPH)",
         "Formulário completo de pré-aviso com sinais vitais, Glasgow, procedimentos, "
         "medicações e ETA — entregue ao hospital antes da chegada da viatura."),
        ("Stack Moderna e Customizável",
         "React 18 + Vite + Tailwind + Base44. Código aberto, adaptável ao contexto "
         "de cada município sem contratos de licença."),
        ("Foco Estratégico em Santo André",
         "Não é produto de prateleira. Nasce com plano de negócios, deck técnico e "
         "arquitetura desenhada para a realidade operacional do SAMU de Santo André."),
        ("Custo Zero de Licenciamento",
         "Solução open-source sem royalties. O investimento é em implantação e customização, "
         "não em licença perpétua para um fornecedor privado."),
    ]

    col_w = [(PAGE_W - 4*cm) * p for p in [0.06, 0.94]]

    for i, (titulo, desc) in enumerate(items):
        num_style = ParagraphStyle("num", fontName="Helvetica-Bold", fontSize=14,
                                   textColor=VERMELHO, alignment=TA_CENTER, leading=18)
        t_style   = ParagraphStyle("it", fontName="Helvetica-Bold", fontSize=10,
                                   textColor=AZUL_ESCURO, leading=14)
        d_style   = ParagraphStyle("id", fontName="Helvetica", fontSize=9,
                                   textColor=CINZA_ESCURO, leading=13)

        row = Table(
            [[Paragraph(str(i+1), num_style),
              [Paragraph(titulo, t_style), Paragraph(desc, d_style)]]],
            colWidths=col_w
        )
        row.setStyle(TableStyle([
            ("VALIGN",        (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING",   (0, 0), (-1, -1), 4),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 4),
            ("TOPPADDING",    (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ("BACKGROUND",    (0, 0), (-1, -1), CINZA_CLARO if i % 2 == 0 else BRANCO),
            ("LINEBELOW",     (0, 0), (-1, 0), 0.5, HexColor("#DDDDDD")),
        ]))
        story.append(row)
        story.append(spacer(0.15))

    story.append(PageBreak())


def pagina_diferenciais_medsave(styles, story):
    story.append(header_slide("Diferenciais do MedSave SEMS SAMU", styles))
    story.append(divider())
    story.append(spacer(0.3))

    items = [
        ("Conformidade Regulatória Total",
         "Protocolos padronizados do Ministério da Saúde integrados nativamente. "
         "Relatórios no formato ministerial gerados automaticamente para prestação de contas."),
        ("ISO 27001 + LGPD Certificado",
         "Segurança de dados auditada e certificada. Compliance total com a LGPD, "
         "reduzindo risco jurídico para o gestor público."),
        ("99,9% de Uptime Garantido",
         "SLA contratual com suporte especializado 24/7. Redundância e plano de "
         "continuidade de negócios para serviço crítico de emergência."),
        ("Integração Nativa com Linha 192",
         "Conectividade direta com o número de emergência. Registro automático "
         "de chamadas sem necessidade de configuração adicional."),
        ("Ficha de Regulação Digital Oficial",
         "Todos os campos obrigatórios conforme normativas vigentes, com "
         "validação e autenticidade para fins legais."),
        ("Resultado Comprovado em Produção",
         "40% de redução no tempo de resposta operacional reportado por usuários. "
         "Produto já implantado e em operação em centrais SAMU."),
    ]

    col_w = [(PAGE_W - 4*cm) * p for p in [0.06, 0.94]]

    for i, (titulo, desc) in enumerate(items):
        num_style = ParagraphStyle("num", fontName="Helvetica-Bold", fontSize=14,
                                   textColor=AZUL_MEDIO, alignment=TA_CENTER, leading=18)
        t_style   = ParagraphStyle("it", fontName="Helvetica-Bold", fontSize=10,
                                   textColor=AZUL_ESCURO, leading=14)
        d_style   = ParagraphStyle("id", fontName="Helvetica", fontSize=9,
                                   textColor=CINZA_ESCURO, leading=13)

        row = Table(
            [[Paragraph(str(i+1), num_style),
              [Paragraph(titulo, t_style), Paragraph(desc, d_style)]]],
            colWidths=col_w
        )
        row.setStyle(TableStyle([
            ("VALIGN",        (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING",   (0, 0), (-1, -1), 4),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 4),
            ("TOPPADDING",    (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ("BACKGROUND",    (0, 0), (-1, -1), CINZA_CLARO if i % 2 == 0 else BRANCO),
            ("LINEBELOW",     (0, 0), (-1, 0), 0.5, HexColor("#DDDDDD")),
        ]))
        story.append(row)
        story.append(spacer(0.15))

    story.append(PageBreak())


def pagina_posicionamento(styles, story):
    story.append(header_slide("Posicionamento Estratégico", styles))
    story.append(divider())
    story.append(spacer(0.3))

    story.append(Paragraph(
        "A pergunta decisiva para Santo André:",
        ParagraphStyle("q0", fontName="Helvetica-Bold", fontSize=12,
                       textColor=AZUL_ESCURO, leading=16)
    ))
    story.append(spacer(0.2))

    caixa = Table(
        [[Paragraph(
            '"Quantas vidas foram perdidas porque o regulador estava '
            'no limite da sua capacidade cognitiva?"',
            ParagraphStyle("q", fontName="Helvetica-BoldOblique", fontSize=13,
                           textColor=BRANCO, leading=19, alignment=TA_CENTER)
        )]],
        colWidths=[PAGE_W - 4*cm]
    )
    caixa.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), VERMELHO),
        ("TOPPADDING",    (0, 0), (-1, -1), 16),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 16),
        ("LEFTPADDING",   (0, 0), (-1, -1), 20),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 20),
        ("ROUNDEDCORNERS", [6]),
    ]))
    story.append(caixa)
    story.append(spacer(0.4))

    story.append(Paragraph(
        "A ISA do SAMU Amigo é a resposta para essa pergunta. O MedSave não tem essa resposta.",
        ParagraphStyle("resp", fontName="Helvetica-Bold", fontSize=11,
                       textColor=AZUL_MEDIO, leading=16, alignment=TA_CENTER)
    ))
    story.append(spacer(0.5))
    story.append(divider(CINZA_MEDIO, 1))

    matrix = [
        ["", "Compliance Alto", "Compliance Baixo"],
        ["IA Alta",     "SAMU Amigo\n(objetivo)",      "SAMU Amigo\n(estado atual)"],
        ["IA Baixa",    "MedSave\n(estado atual)",     "Sistemas legados"],
    ]

    col_w2 = [(PAGE_W - 4*cm) * p for p in [0.22, 0.39, 0.39]]

    def ms(r, c, bg, bold=False):
        fn = "Helvetica-Bold" if bold else "Helvetica"
        return ParagraphStyle(f"m{r}{c}", fontName=fn, fontSize=9,
                              textColor=BRANCO if bg != CINZA_CLARO else CINZA_ESCURO,
                              alignment=TA_CENTER, leading=13)

    m_rows = []
    for ri, row in enumerate(matrix):
        m_row = []
        for ci, cell in enumerate(row):
            if ri == 0 and ci == 0:
                bg = AZUL_ESCURO; bold = True
            elif ri == 0:
                bg = AZUL_MEDIO; bold = True
            elif ci == 0:
                bg = AZUL_MEDIO; bold = True
            elif ri == 1 and ci == 1:
                bg = VERMELHO; bold = True
            elif ri == 1 and ci == 2:
                bg = LARANJA; bold = False
            else:
                bg = CINZA_CLARO; bold = False
            m_row.append(Paragraph(cell, ms(ri, ci, bg, bold)))
        m_rows.append(m_row)

    mt = Table(m_rows, colWidths=col_w2)
    mt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), AZUL_ESCURO),
        ("BACKGROUND", (1, 0), (2, 0), AZUL_MEDIO),
        ("BACKGROUND", (0, 1), (0, 2), AZUL_MEDIO),
        ("BACKGROUND", (1, 1), (1, 1), VERMELHO),
        ("BACKGROUND", (2, 1), (2, 1), LARANJA),
        ("BACKGROUND", (1, 2), (1, 2), CINZA_MEDIO),
        ("BACKGROUND", (2, 2), (2, 2), CINZA_CLARO),
        ("GRID",       (0, 0), (-1, -1), 1, BRANCO),
        ("VALIGN",     (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 14),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
    ]))
    story.append(mt)
    story.append(spacer(0.3))
    story.append(Paragraph(
        "Matriz: Inovacao (IA) x Conformidade Regulatoria  |  Vermelho = posicao atual SAMU Amigo no roadmap",
        styles["nota"]
    ))
    story.append(PageBreak())


def pagina_lacunas(styles, story):
    story.append(header_slide("Lacunas Prioritarias — Roadmap SAMU Amigo", styles))
    story.append(divider())
    story.append(spacer(0.2))

    dados = [
        ["#", "Lacuna", "Prioridade", "Sprint"],
        ["1", "Remover senha hardcoded + RBAC real + MFA",                    "Critica",  "1"],
        ["2", "LGPD: consentimento, exclusao e exportacao de dados",          "Alta",     "2"],
        ["3", "Audit Log: rastreio de acoes por usuario e timestamp",         "Alta",     "3"],
        ["4", "Protocolos MS configuráveis e versionados",                    "Alta",     "4"],
        ["5", "Cobertura de testes automatizados (min. 70%)",                 "Alta",     "5"],
        ["6", "Integracao VoIP com linha 192",                                "Media",    "6"],
        ["7", "Multi-tenancy real com isolamento por municipio",              "Media",    "7"],
        ["8", "Ficha de regulacao oficial com campos obrigatórios do MS",     "Media",    "4"],
        ["9", "SLA documentado + monitoramento de uptime",                   "Baixa",    "7"],
        ["10","Integracao hospitalar bidirecional (HL7/FHIR)",               "Baixa",    "8"],
    ]

    def cor_prio(p):
        if p == "Critica": return VERMELHO
        if p == "Alta":    return LARANJA
        if p == "Media":   return AZUL_CLARO
        return VERDE

    col_w = [(PAGE_W - 4*cm) * p for p in [0.05, 0.60, 0.18, 0.17]]

    header_row = [
        Paragraph(c, ParagraphStyle("th2", fontName="Helvetica-Bold", fontSize=9,
                                    textColor=BRANCO, alignment=TA_CENTER, leading=13))
        for c in dados[0]
    ]

    rows = [header_row]
    for row in dados[1:]:
        p_color = cor_prio(row[2])
        rows.append([
            Paragraph(row[0], ParagraphStyle("rn", fontName="Helvetica-Bold", fontSize=9,
                                              textColor=AZUL_MEDIO, alignment=TA_CENTER, leading=13)),
            Paragraph(row[1], ParagraphStyle("rd", fontName="Helvetica", fontSize=9,
                                              textColor=CINZA_ESCURO, leading=13)),
            Paragraph(row[2], ParagraphStyle("rp", fontName="Helvetica-Bold", fontSize=9,
                                              textColor=p_color, alignment=TA_CENTER, leading=13)),
            Paragraph(f"Sprint {row[3]}", ParagraphStyle("rs", fontName="Helvetica", fontSize=9,
                                                          textColor=CINZA_MEDIO, alignment=TA_CENTER,
                                                          leading=13)),
        ])

    ts = TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), AZUL_ESCURO),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
        ("GRID",          (0, 0), (-1, -1), 0.4, HexColor("#CCCCCC")),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
    ])
    t = Table(rows, colWidths=col_w)
    t.setStyle(ts)
    story.append(t)
    story.append(PageBreak())


def pagina_conclusao(styles, story):
    story.append(header_slide("Conclusao", styles))
    story.append(divider())
    story.append(spacer(0.4))

    comparativo = [
        ["MedSave SEMS SAMU", "SAMU Amigo"],
        ["Estrutura robusta de gestao", "Salto tecnologico com IA"],
        ["Produto de prateleira", "Ecossistema para Santo André"],
        ["Compliance consolidado", "Inovacao clinica"],
        ["Digitaliza formularios", "Auxilia decisoes criticas"],
        ["Resolve o problema de ontem", "Resolve o problema de amanha"],
    ]

    col_w = [(PAGE_W - 4*cm) * 0.5] * 2

    c_rows = []
    for i, row in enumerate(comparativo):
        if i == 0:
            c_rows.append([
                Paragraph(row[0], ParagraphStyle("ch", fontName="Helvetica-Bold", fontSize=11,
                                                  textColor=BRANCO, alignment=TA_CENTER, leading=15)),
                Paragraph(row[1], ParagraphStyle("ch2", fontName="Helvetica-Bold", fontSize=11,
                                                  textColor=BRANCO, alignment=TA_CENTER, leading=15)),
            ])
        else:
            c_rows.append([
                Paragraph(row[0], ParagraphStyle("cb", fontName="Helvetica", fontSize=10,
                                                  textColor=CINZA_ESCURO, alignment=TA_CENTER, leading=14)),
                Paragraph(row[1], ParagraphStyle("cb2", fontName="Helvetica-Bold", fontSize=10,
                                                  textColor=AZUL_MEDIO, alignment=TA_CENTER, leading=14)),
            ])

    ct = Table(c_rows, colWidths=col_w)
    ct.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (0, 0), CINZA_MEDIO),
        ("BACKGROUND",    (1, 0), (1, 0), VERMELHO),
        ("ROWBACKGROUNDS",(0, 1), (0, -1), [CINZA_CLARO, BRANCO]),
        ("ROWBACKGROUNDS",(1, 1), (1, -1), [HexColor("#FFF0F0"), HexColor("#FFE4E4")]),
        ("GRID",          (0, 0), (-1, -1), 0.5, HexColor("#CCCCCC")),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LINEAFTER",     (0, 0), (0, -1), 2, VERMELHO),
    ]))
    story.append(ct)
    story.append(spacer(0.6))

    box_final = Table(
        [[Paragraph(
            "Para Santo André: o MedSave entrega conformidade.<br/>"
            "O SAMU Amigo entrega inteligência.<br/>"
            "Com o roadmap correto, o SAMU Amigo pode ter os dois.",
            ParagraphStyle("bf", fontName="Helvetica-Bold", fontSize=12,
                           textColor=BRANCO, alignment=TA_CENTER, leading=18)
        )]],
        colWidths=[PAGE_W - 4*cm]
    )
    box_final.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), AZUL_ESCURO),
        ("TOPPADDING",    (0, 0), (-1, -1), 18),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 18),
        ("LEFTPADDING",   (0, 0), (-1, -1), 24),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 24),
    ]))
    story.append(box_final)
    story.append(PageBreak())


# =====================================================================
# MONTAGEM DO DOCUMENTO
# =====================================================================

def gerar_pdf(output_path):
    styles = build_styles()
    story  = []

    # 1 — Capa
    doc_capa = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm,
        topMargin=2*cm,  bottomMargin=2*cm,
    )

    pagina_capa(styles, story)

    # 2 — Seção: Visão Geral
    pagina_secao("Visao Geral", "Como os dois produtos se posicionam no mercado", styles, story)
    tabela_comparativa_geral(styles, story)

    # 3 — Seção: Funcionalidades
    pagina_secao("Funcionalidades", "Comparativo funcional item a item", styles, story)
    tabela_funcionalidades(styles, story)

    # 4 — Diferenciais SAMU Amigo
    pagina_secao("SAMU Amigo", "Onde o projeto se destaca e supera o mercado", styles, story)
    pagina_diferenciais_samu(styles, story)

    # 5 — Diferenciais MedSave
    pagina_secao("MedSave SEMS SAMU", "Onde o concorrente é mais sólido", styles, story)
    pagina_diferenciais_medsave(styles, story)

    # 6 — Posicionamento
    pagina_secao("Posicionamento", "A pergunta que o gestor de Santo André precisa responder", styles, story)
    pagina_posicionamento(styles, story)

    # 7 — Lacunas
    pagina_secao("Roadmap", "O que construir para chegar ao topo", styles, story)
    pagina_lacunas(styles, story)

    # 8 — Conclusão
    pagina_secao("Conclusao", "Sintese final da analise comparativa", styles, story)
    pagina_conclusao(styles, story)

    # --- build com backgrounds alternados ---
    page_num = [0]

    CAPA_PAGES   = {1, 2}      # capa + primeira seção
    SECAO_PAGES  = {2, 4, 6, 8, 10, 12, 14}   # aprox — todas as páginas de seção

    def on_page(canvas_obj, doc):
        page_num[0] += 1
        n = doc.page
        if n == 1:
            SlideBackground("capa")(canvas_obj, doc)
        elif n % 2 == 0:
            SlideBackground("secao")(canvas_obj, doc)
        else:
            SlideBackground("normal")(canvas_obj, doc)

    doc_capa.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f"PDF gerado: {output_path}")


if __name__ == "__main__":
    gerar_pdf("samu_amigo_vs_medsave.pdf")

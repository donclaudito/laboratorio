import { jsPDF } from "jspdf";

export function gerarPDF(resultado) {
  const doc = new jsPDF({ unit: "mm", format: "a4" });
  const pageWidth = doc.internal.pageSize.getWidth();
  const pageHeight = doc.internal.pageSize.getHeight();
  const marginLeft = 20;
  const marginRight = 20;
  const usableWidth = pageWidth - marginLeft - marginRight;

  const hoje = new Date().toLocaleDateString("pt-BR");

  // ─── CABEÇALHO ───────────────────────────────────────────────────────────
  doc.setFillColor(16, 185, 129); // emerald-500
  doc.rect(0, 0, pageWidth, 28, "F");

  doc.setTextColor(255, 255, 255);
  doc.setFont("helvetica", "bold");
  doc.setFontSize(16);
  doc.text("SOLICITAÇÃO DE EXAMES", pageWidth / 2, 11, { align: "center" });

  doc.setFontSize(9);
  doc.setFont("helvetica", "normal");
  doc.text("Dr. Claudio M Orenstein  |  CRM-SP 58120", pageWidth / 2, 18, { align: "center" });
  doc.text(`Data: ${hoje}`, pageWidth / 2, 23, { align: "center" });

  // ─── LINHA SEPARADORA ────────────────────────────────────────────────────
  doc.setDrawColor(16, 185, 129);
  doc.setLineWidth(0.5);
  doc.line(marginLeft, 32, pageWidth - marginRight, 32);

  // ─── CONTEÚDO ────────────────────────────────────────────────────────────
  let y = 38;
  const lineHeight = 6;
  const footerHeight = 20;

  const lines = resultado.split("\n");

  lines.forEach((line) => {
    // Pular linhas de cabeçalho do markdown que já estão no PDF
    if (
      line.startsWith("# SOLICITAÇÃO") ||
      line.startsWith("**Médico") ||
      line.startsWith("**Data")
    ) return;

    // Nova página se necessário
    if (y > pageHeight - footerHeight - 10) {
      addFooter(doc, pageWidth, pageHeight);
      doc.addPage();
      addHeader(doc, pageWidth, hoje);
      y = 38;
    }

    if (line.startsWith("### ")) {
      // Título de seção
      if (y > 38) y += 2;
      doc.setFillColor(240, 253, 250); // fundo verde suave
      doc.roundedRect(marginLeft, y - 4, usableWidth, 8, 2, 2, "F");
      doc.setTextColor(5, 150, 105); // emerald-600
      doc.setFont("helvetica", "bold");
      doc.setFontSize(10);
      doc.text(line.replace("### ", ""), marginLeft + 3, y + 1);
      y += lineHeight + 2;

    } else if (line.startsWith("## ")) {
      // Título secundário
      if (y > 38) y += 3;
      doc.setTextColor(30, 30, 30);
      doc.setFont("helvetica", "bold");
      doc.setFontSize(11);
      doc.text(line.replace("## ", ""), marginLeft, y);
      y += lineHeight + 2;

    } else if (line.startsWith("- [x] ")) {
      // Item de exame
      doc.setTextColor(50, 50, 50);
      doc.setFont("helvetica", "normal");
      doc.setFontSize(9.5);

      // Checkbox visual
      doc.setDrawColor(16, 185, 129);
      doc.setFillColor(16, 185, 129);
      doc.roundedRect(marginLeft, y - 3.5, 4, 4, 0.8, 0.8, "FD");
      doc.setTextColor(255, 255, 255);
      doc.setFont("helvetica", "bold");
      doc.setFontSize(7);
      doc.text("✓", marginLeft + 0.7, y - 0.2);

      doc.setTextColor(50, 50, 50);
      doc.setFont("helvetica", "normal");
      doc.setFontSize(9.5);
      const examText = line.replace("- [x] ", "");
      const wrapped = doc.splitTextToSize(examText, usableWidth - 8);
      doc.text(wrapped, marginLeft + 7, y);
      y += lineHeight * wrapped.length;

    } else if (line.startsWith("---")) {
      // Linha divisória
      y += 2;
      doc.setDrawColor(200, 200, 200);
      doc.setLineWidth(0.3);
      doc.line(marginLeft, y, pageWidth - marginRight, y);
      y += 4;

    } else if (line.startsWith("* **")) {
      // Orientações importantes
      doc.setTextColor(80, 80, 80);
      doc.setFont("helvetica", "normal");
      doc.setFontSize(8.5);
      const clean = line.replace(/\*\*/g, "").replace("* ", "• ");
      const wrapped = doc.splitTextToSize(clean, usableWidth - 4);
      doc.text(wrapped, marginLeft + 2, y);
      y += lineHeight * wrapped.length;

    } else if (line.trim() !== "") {
      // Texto genérico
      doc.setTextColor(60, 60, 60);
      doc.setFont("helvetica", "normal");
      doc.setFontSize(9);
      const wrapped = doc.splitTextToSize(line, usableWidth);
      doc.text(wrapped, marginLeft, y);
      y += lineHeight * wrapped.length;
    } else {
      y += 2; // linha em branco
    }
  });

  // ─── RODAPÉ DA ÚLTIMA PÁGINA ─────────────────────────────────────────────
  addFooter(doc, pageWidth, pageHeight);

  doc.save(`solicitacao-exames-${hoje.replace(/\//g, "-")}.pdf`);
}

function addHeader(doc, pageWidth, hoje) {
  doc.setFillColor(16, 185, 129);
  doc.rect(0, 0, pageWidth, 28, "F");
  doc.setTextColor(255, 255, 255);
  doc.setFont("helvetica", "bold");
  doc.setFontSize(16);
  doc.text("SOLICITAÇÃO DE EXAMES", pageWidth / 2, 11, { align: "center" });
  doc.setFontSize(9);
  doc.setFont("helvetica", "normal");
  doc.text("Dr. Claudio M Orenstein  |  CRM-SP 58120", pageWidth / 2, 18, { align: "center" });
  doc.text(`Data: ${hoje}`, pageWidth / 2, 23, { align: "center" });
  doc.setDrawColor(16, 185, 129);
  doc.setLineWidth(0.5);
  doc.line(20, 32, pageWidth - 20, 32);
}

function addFooter(doc, pageWidth, pageHeight) {
  const footerY = pageHeight - 14;
  doc.setDrawColor(16, 185, 129);
  doc.setLineWidth(0.5);
  doc.line(20, footerY - 3, pageWidth - 20, footerY - 3);

  doc.setFillColor(16, 185, 129);
  doc.rect(0, footerY, pageWidth, 14, "F");

  doc.setTextColor(255, 255, 255);
  doc.setFont("helvetica", "normal");
  doc.setFontSize(8);
  doc.text(
    "Este documento é uma solicitação médica e deve ser apresentado ao laboratório/clínica de imagem.",
    pageWidth / 2,
    footerY + 5,
    { align: "center" }
  );
  doc.text(
    "Dúvidas? Entre em contato com o consultório.",
    pageWidth / 2,
    footerY + 10,
    { align: "center" }
  );
}
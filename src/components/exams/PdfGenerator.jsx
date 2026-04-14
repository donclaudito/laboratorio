import { jsPDF } from "jspdf";

export function gerarPDF(resultado, paciente = null) {
  const doc = new jsPDF({ unit: "mm", format: "a4" });
  const pageWidth = doc.internal.pageSize.getWidth();
  const pageHeight = doc.internal.pageSize.getHeight();
  const marginLeft = 20;
  const marginRight = 20;
  const usableWidth = pageWidth - marginLeft - marginRight;

  const hoje = new Date().toLocaleDateString("pt-BR");
  const headerHeight = paciente ? 36 : 26;

  // ─── CABEÇALHO ───────────────────────────────────────────────────────────
  addHeader(doc, pageWidth, hoje, paciente);

  // ─── CONTEÚDO ────────────────────────────────────────────────────────────
  let y = headerHeight + 10;
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
      addHeader(doc, pageWidth, hoje, paciente);
      y = (paciente ? 36 : 26) + 10;
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

export function imprimirPDF(resultado, paciente = null) {
  const doc = new jsPDF({ unit: "mm", format: "a4" });
  // Reutiliza toda a lógica de geração mas abre janela de impressão
  const blob = gerarPDFBlob(resultado, paciente, doc);
  const url = URL.createObjectURL(blob);
  const iframe = document.createElement("iframe");
  iframe.style.display = "none";
  iframe.src = url;
  document.body.appendChild(iframe);
  iframe.onload = () => {
    iframe.contentWindow.print();
    setTimeout(() => {
      document.body.removeChild(iframe);
      URL.revokeObjectURL(url);
    }, 2000);
  };
}

function gerarPDFBlob(resultado, paciente, doc) {
  // Re-run the same rendering logic and return blob
  const pageWidth = doc.internal.pageSize.getWidth();
  const pageHeight = doc.internal.pageSize.getHeight();
  const marginLeft = 20;
  const marginRight = 20;
  const usableWidth = pageWidth - marginLeft - marginRight;
  const hoje = new Date().toLocaleDateString("pt-BR");
  const headerHeight = paciente ? 36 : 26;
  const lineHeight = 6;
  const footerHeight = 20;

  addHeader(doc, pageWidth, hoje, paciente);

  let y = headerHeight + 10;
  const lines = resultado.split("\n");

  lines.forEach((line) => {
    if (line.startsWith("# SOLICITAÇÃO") || line.startsWith("**Médico") || line.startsWith("**Data")) return;

    if (y > pageHeight - footerHeight - 10) {
      addFooter(doc, pageWidth, pageHeight);
      doc.addPage();
      addHeader(doc, pageWidth, hoje, paciente);
      y = headerHeight + 10;
    }

    if (line.startsWith("### ")) {
      if (y > headerHeight + 10) y += 2;
      doc.setFillColor(240, 253, 250);
      doc.roundedRect(marginLeft, y - 4, usableWidth, 8, 2, 2, "F");
      doc.setTextColor(5, 150, 105);
      doc.setFont("helvetica", "bold");
      doc.setFontSize(10);
      doc.text(line.replace("### ", ""), marginLeft + 3, y + 1);
      y += lineHeight + 2;
    } else if (line.startsWith("## ")) {
      if (y > headerHeight + 10) y += 3;
      doc.setTextColor(30, 30, 30);
      doc.setFont("helvetica", "bold");
      doc.setFontSize(11);
      doc.text(line.replace("## ", ""), marginLeft, y);
      y += lineHeight + 2;
    } else if (line.startsWith("- [x] ")) {
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
      y += 2;
      doc.setDrawColor(200, 200, 200);
      doc.setLineWidth(0.3);
      doc.line(marginLeft, y, pageWidth - marginRight, y);
      y += 4;
    } else if (line.startsWith("* **")) {
      doc.setTextColor(80, 80, 80);
      doc.setFont("helvetica", "normal");
      doc.setFontSize(8.5);
      const clean = line.replace(/\*\*/g, "").replace("* ", "• ");
      const wrapped = doc.splitTextToSize(clean, usableWidth - 4);
      doc.text(wrapped, marginLeft + 2, y);
      y += lineHeight * wrapped.length;
    } else if (line.trim() !== "") {
      doc.setTextColor(60, 60, 60);
      doc.setFont("helvetica", "normal");
      doc.setFontSize(9);
      const wrapped = doc.splitTextToSize(line, usableWidth);
      doc.text(wrapped, marginLeft, y);
      y += lineHeight * wrapped.length;
    } else {
      y += 2;
    }
  });

  addFooter(doc, pageWidth, pageHeight);
  return doc.output("blob");
}

function addHeader(doc, pageWidth, hoje, paciente = null) {
  const headerHeight = paciente ? 36 : 26;

  // Fundo cinza claro para alto contraste P&B
  doc.setFillColor(204, 204, 204); // #CCCCCC
  doc.rect(0, 0, pageWidth, headerHeight, "F");

  // Borda preta ao redor do cabeçalho
  doc.setDrawColor(0, 0, 0);
  doc.setLineWidth(0.8);
  doc.rect(0, 0, pageWidth, headerHeight, "S");

  // Coluna esquerda: Nome do médico
  doc.setTextColor(0, 0, 0);
  doc.setFont("helvetica", "bold");
  doc.setFontSize(13);
  doc.text("Dr. Claudio M Orenstein", 8, 10);

  doc.setFontSize(9);
  doc.setFont("helvetica", "normal");
  doc.text("CRM-SP 58120", 8, 17);

  // Coluna central: Título
  doc.setFont("helvetica", "bold");
  doc.setFontSize(14);
  doc.text("SOLICITAÇÃO DE EXAMES", pageWidth / 2, 12, { align: "center" });

  // Coluna direita: Data
  doc.setFont("helvetica", "bold");
  doc.setFontSize(10);
  doc.text(`Data: ${hoje}`, pageWidth - 8, 10, { align: "right" });

  // Linha separadora preta
  doc.setDrawColor(0, 0, 0);
  doc.setLineWidth(0.5);
  doc.line(0, headerHeight, pageWidth, headerHeight);

  // Linha de paciente (fundo branco levemente cinza)
  if (paciente) {
    doc.setFillColor(235, 235, 235);
    doc.rect(0, headerHeight, pageWidth, 10, "F");
    doc.setDrawColor(0, 0, 0);
    doc.setLineWidth(0.3);
    doc.rect(0, headerHeight, pageWidth, 10, "S");

    let info = `Paciente: ${paciente.nome}`;
    if (paciente.idade) info += `   |   Idade: ${paciente.idade} anos`;
    if (paciente.paciente_id) info += `   |   ID: ${paciente.paciente_id}`;
    doc.setFont("helvetica", "bold");
    doc.setFontSize(9);
    doc.setTextColor(0, 0, 0);
    doc.text(info, pageWidth / 2, headerHeight + 6.5, { align: "center" });
  }
}

function addFooter(doc, pageWidth, pageHeight) {
  const footerY = pageHeight - 14;

  doc.setFillColor(204, 204, 204); // cinza claro P&B
  doc.rect(0, footerY, pageWidth, 14, "F");
  doc.setDrawColor(0, 0, 0);
  doc.setLineWidth(0.5);
  doc.rect(0, footerY, pageWidth, 14, "S");

  doc.setTextColor(0, 0, 0);
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